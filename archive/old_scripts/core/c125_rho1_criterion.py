r"""
c125_rho1_criterion.py -- 验证 ρ≤1 的刻画

刻画：ρ≤1 可达 ⟺ (i) α0 ∈ im R0ᵀ　(ii) L0 A N = 0　(iii) (5b)

测试方式：对每个随机实例，枚举 L0（使其满足 (ii)），
        检查 (i) 是否成立，若成立则构造并发证 (5a)(5b) 与 ρ=1。
"""
import os, io, contextlib, random, sys
from fractions import Fraction as Fr
_HERE=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,_HERE)
from exact_gcd import cond_5b

_ns={}
with open(os.path.join(_HERE,"exact_count_thm7.py"),encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(),"lib","exec"),_ns)
rk=_ns["rk"]; mm=_ns["mm"]; ker_basis=_ns["ker_basis"]

def rb(M):
    if not M or not M[0]: return []
    mr=len(M); nc=len(M[0]); A=[[Fr(x) for x in r] for r in M]; piv=[]; r=0
    for c in range(nc):
        p=None
        for i in range(r,mr):
            if A[i][c]!=0: p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]; pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for i in range(mr):
            if i!=r and A[i][c]!=0:
                f=A[i][c]; A[i]=[A[i][j]-f*A[r][j] for j in range(nc)]
        piv.append(r); r+=1
        if r==mr: break
    return [A[i][:] for i in piv]

def solve(Amat,bvec):
    m=len(Amat); n=len(Amat[0])
    M=[[Fr(Amat[i][j]) for j in range(n)]+[Fr(bvec[i])] for i in range(m)]
    piv=[]; r=0
    for c in range(n):
        p=None
        for i in range(r,m):
            if M[i][c]!=0: p=i; break
        if p is None: continue
        M[r],M[p]=M[p],M[r]; pv=M[r][c]; M[r]=[x/pv for x in M[r]]
        for i in range(m):
            if i!=r and M[i][c]!=0:
                f=M[i][c]; M[i]=[M[i][j]-f*M[r][j] for j in range(n+1)]
        piv.append(c); r+=1
        if r==m: break
    for i in range(r,m):
        if all(M[i][j]==0 for j in range(n)) and M[i][n]!=0: return None
    x=[Fr(0)]*n
    for i,c in enumerate(piv): x[c]=M[i][n]
    return x

def minv(M):
    n=len(M)
    A2=[[Fr(M[i][j]) for j in range(n)]+[Fr(1) if i==j else Fr(0) for j in range(n)] for i in range(n)]
    for c in range(n):
        p=None
        for i in range(c,n):
            if A2[i][c]!=0: p=i; break
        if p is None: return None
        A2[c],A2[p]=A2[p],A2[c]; pv=A2[c][c]; A2[c]=[x/pv for x in A2[c]]
        for i in range(n):
            if i!=c and A2[i][c]!=0:
                f=A2[i][c]; A2[i]=[A2[i][j]-f*A2[c][j] for j in range(2*n)]
    return [row[n:] for row in A2]

def invcl(M0,Ap,d):
    b=rb(M0); cur=[r[:] for r in b]
    while len(b)<d and b:
        cur=mm(cur,Ap)
        if rk(b+[r[:] for r in cur])==len(b): break
        b=b+[r[:] for r in cur]
    return rb(b)

def main():
    print("=== 验证 ρ≤1 的刻画 ===\n")
    n=6; p=1
    yes=0; yes_ok=0; no=0
    for t in range(1,60):
        rng=random.Random(9500000+t)
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
        if rk(Cc)!=1: continue
        CA=mm(Cc,A); Mrows=Cc+CA
        if rk(Mrows)!=2: continue
        N=ker_basis(Mrows)
        if not N or not N[0]: continue
        d=len(N[0])
        if d<2: continue
        AN=mm(A,N)
        Nt=[[N[i][j] for i in range(n)] for j in range(d)]
        iN=minv(mm(Nt,N))
        if iN is None: continue
        Ap=mm(mm(iN,Nt),AN)
        R0=[[AN[i][j]-mm(N,Ap)[i][j] for j in range(d)] for i in range(n)]
        if rk(R0)==0: continue
        R0rows=rb(R0)
        # 选 L0 满足 (ii) L0 A N = 0 且 L0 N != 0
        L0=None
        for _ in range(300):
            cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(cand)!=1: continue
            if rk(cand+Cc)!=2: continue
            a0=mm(cand,N)[0]
            if all(x==0 for x in a0): continue
            f0=mm(mm(cand,A),N)[0]
            if any(x!=0 for x in f0): continue     # (ii)
            L0=cand; break
        if L0 is None: continue
        a0=mm(L0,N)[0]
        # (i) α0 ∈ im R0ᵀ ？
        inR0 = rk([r[:] for r in R0rows]+[a0[:]])==rk(R0rows)
        if not inR0:
            no+=1; continue
        # 解 ℓ1: ℓ1 N = 0, ℓ1 A N = a0
        A2m=[]; b2=[]
        for j in range(d):
            A2m.append([N[i][j] for i in range(n)]); b2.append(Fr(0))
        for j in range(d):
            A2m.append([AN[i][j] for i in range(n)]); b2.append(a0[j])
        l1=solve(A2m,b2)
        if l1 is None:
            no+=1; continue
        yes+=1
        Lam=[L0[0][:], l1[:]]
        M=mm(Lam,N); F=mm(mm(Lam,A),N)
        rho=rk(M)
        K=ker_basis(M)
        ok5a=(not K or not K[0]) or rk(mm(F,K))==0
        ok5b=cond_5b(M,F)
        if rho==1 and ok5a and ok5b: yes_ok+=1
        else:
            if yes<=5: print("[%d] 预测可行但实际 rho=%d (5a)=%s (5b)=%s ✗" % (t,rho,ok5a,ok5b))
    print()
    print("满足 (i)+(ii) 的实例：%d ；其中成功构造 ρ=1 的解：%d" % (yes,yes_ok))
    print("不满足 (i) 的实例：%d" % no)
    if yes>0 and yes_ok==yes:
        print("\n⟹ *** 刻画验证通过：条件 (i)+(ii) 足以构造 ρ=1 的解 *** ✓")
    elif yes_ok>0:
        print("\n⟹ 部分通过 (%d/%d)" % (yes_ok,yes))

if __name__=="__main__":
    main()
