r"""
c127_fixed.py -- 修正版：验证 "⇐"（e=d 时 (ii) ⟹ ρ=1 的解）

关键修改：去掉不必要的 L0 ⊥ col(C) 筛选。
p=2, n=6；需 d=2 且 e=rank(R0)=2（此时 e=d，条件 (i) 自动成立）。
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

def nullsp(M):
    if not M or not M[0]: return []
    m=len(M); n=len(M[0])
    A=[[Fr(x) for x in row] for row in M]; piv=[]; r=0
    for c in range(n):
        p=None
        for i in range(r,m):
            if A[i][c]!=0: p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]; pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]!=0:
                f=A[i][c]; A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
        piv.append(c); r+=1
        if r==m: break
    free=[c for c in range(n) if c not in piv]
    out=[]
    for fc in free:
        v=[Fr(0)]*n; v[fc]=Fr(1)
        for i,c in enumerate(piv): v[c]=-A[i][fc]
        out.append(v)
    return out

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
    print("=== c127: 验证 e=d 时 (ii) ⟹ ρ=1 的解（p=2, n=6, d=2, e=2）===\n")
    n=6; p=2
    inst=0; yes=0; ok=0
    for t in range(1,200):
        rng=random.Random(9800000+t)
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc)!=p: continue
        CA=mm(Cc,A); Mrows=Cc+CA
        if rk(Mrows)!=4: continue     # => d=2
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
        if e!=2: continue             # 需要 e = d = 2
        # (col AN)^perp 的基
        ANt=[[AN[i][j] for i in range(n)] for j in range(d)]
        perp=nullsp(ANt)
        L0=None
        for v in perp:
            a0=mm([v],N)[0]
            if all(x==0 for x in a0): continue
            L0=[v]; break
        if L0 is None: continue
        inst+=1
        a0=mm(L0,N)[0]
        # 解 ℓ1
        A2m=[]; b2=[]
        for j in range(d):
            A2m.append([N[i][j] for i in range(n)]); b2.append(Fr(0))
        for j in range(d):
            A2m.append([AN[i][j] for i in range(n)]); b2.append(a0[j])
        l1=solve(A2m,b2)
        if l1 is None:
            if inst<=6: print("[%d] ℓ1 无解（意外，因映射是满射）✗" % t)
            continue
        yes+=1
        Lam=[L0[0][:], l1]
        M=mm(Lam,N); F=mm(mm(Lam,A),N)
        rho=rk(M)
        K=ker_basis(M)
        ok5a=(not K or not K[0]) or rk(mm(F,K))==0
        ok5b=cond_5b(M,F)
        good=(rho==1 and ok5a and ok5b)
        if good: ok+=1
        if inst<=8:
            print("[%d] rho=%d (5a)=%s (5b)=%s %s" % (t,rho,ok5a,ok5b,"OK" if good else "FAIL"))
    print()
    print("实例（d=2,e=2 且找到 L0）：%d ；ℓ1 有解：%d ；成功构造 ρ=1 的解：%d" % (inst,yes,ok))
    if inst>0 and ok==inst:
        print("\n⟹ *** ⇐ 验证通过：e=d 时 (ii) ⟹ ρ=1 的解存在 *** ✓")
        print("   故该族 q_min = 2")
    elif ok>0:
        print("\n⟹ 部分通过 (%d/%d)" % (ok,inst))
    elif inst==0:
        print("\n⟹ 未找到 d=2 且 e=2 的实例（需换参数）")

if __name__=="__main__":
    main()
