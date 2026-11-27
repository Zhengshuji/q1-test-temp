r"""
c126_positive_test.py -- 验证 "⇐"：e=d 时，只需 (ii) L0 A N = 0 就能构造 ρ=1 的解

p=1, n=6, d=2, e=2  ⟹  rowspace(R0) = R²  ⟹  (i) 自动
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

def main():
    print("=== 检验 ⇐ 方向：e=d, d=2 时 (ii) ⟹ ρ=1 的解 ===\n")
    n=6; p=2
    inst=0; yes=0; ok=0
    for t in range(1,80):
        rng=random.Random(9700000+t)
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc)!=p: continue
        CA=mm(Cc,A); Mrows=Cc+CA
        if rk(Mrows)!=4: continue
        N=ker_basis(Mrows)
        if not N or not N[0]: continue
        d=len(N[0])
        if d!=2: continue
        AN=mm(A,N)
        Nt=[[N[i][j] for i in range(n)] for j in range(d)]
        iN=minv(mm(Nt,N))
        if iN is None: continue
        Ap=mm(mm(iN,Nt),AN)
        R0=[[AN[i][j]-mm(N,Ap)[i][j] for j in range(d)] for i in range(n)]
        e=rk(R0)
        if e!=d: continue          # 需要 e=d=2
        # 直接求 (col AN)^perp 的基，从中取 L0（要求 L0 N != 0）
        ANt=[[AN[i][j] for i in range(n)] for j in range(d)]   # d×n
        # 零空间
        Am=[[Fr(x) for x in row] for row in ANt]
        piv=[]; r=0
        for cc in range(n):
            p=None
            for i in range(r,d):
                if Am[i][cc]!=0: p=i; break
            if p is None: continue
            Am[r],Am[p]=Am[p],Am[r]; pv=Am[r][cc]; Am[r]=[x/pv for x in Am[r]]
            for i in range(d):
                if i!=r and Am[i][cc]!=0:
                    ff=Am[i][cc]; Am[i]=[Am[i][j]-ff*Am[r][j] for j in range(n)]
            piv.append(cc); r+=1
            if r==d: break
        freec=[cc for cc in range(n) if cc not in piv]
        perp=[]
        for fc in freec:
            v=[Fr(0)]*n; v[fc]=Fr(1)
            for i,pc in enumerate(piv): v[pc]=-Am[i][fc]
            perp.append(v)
        L0=None
        for v in perp:
            a0=mm([v],N)[0]
            if all(x==0 for x in a0): continue
            cand=[v]
            if rk(cand)!=1: continue
            if rk(cand+Cc)!=4: continue
            L0=cand; break
        if L0 is None: continue
        inst+=1
        a0=mm(L0,N)[0]
        # 解 ℓ1: ℓ1 N = 0, ℓ1 A N = a0
        A2m=[]; b2=[]
        for j in range(d):
            A2m.append([N[i][j] for i in range(n)]); b2.append(Fr(0))
        for j in range(d):
            A2m.append([AN[i][j] for i in range(n)]); b2.append(a0[j])
        l1=solve(A2m,b2)
        if l1 is None:
            if inst<=5: print("[%d] ℓ1 无解 ✗ (e=d=2)" % t)
            continue
        yes+=1
        Lam=[L0[0][:], l1[:]]
        M=mm(Lam,N); F=mm(mm(Lam,A),N)
        rho=rk(M)
        K=ker_basis(M)
        ok5a=(not K or not K[0]) or rk(mm(F,K))==0
        ok5b=cond_5b(M,F)
        good = (rho==1 and ok5a and ok5b)
        if good: ok+=1
        if inst<=6:
            print("[%d] rho=%d (5a)=%s (5b)=%s %s" % (t,rho,ok5a,ok5b,"✓" if good else "✗"))
    print()
    print("实例（e=d=2，且找到满足 (ii) 的 L0）：%d" % inst)
    print("其中 ℓ1 有解：%d ；构造出的解满足 (5a)(5b) 且 ρ=1：%d" % (yes,ok))
    if inst>0 and ok==inst:
        print("\n⟹ *** ⇐ 验证通过：e=d 时 (ii) ⟹ ρ=1 的解存在 *** ✓")
        print("   故该族 q_min = 2，而 obs 可任意大")
    elif ok>0:
        print("\n⟹ 部分通过 (%d/%d)" % (ok,inst))

if __name__=="__main__":
    main()
