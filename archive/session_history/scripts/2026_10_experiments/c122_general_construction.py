r"""
c122_general_construction.py -- 推广反例：α0 ∈ im R0ᵀ ⟹ q=2, ρ=1 的解存在

构造：row0 = L0, row1 = ℓ1 满足 ℓ1 N = 0 且 ℓ1 A N = L0 N
      Λ = [[0,0],[1,0]] （幂零）
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

def solve(Amat, bvec):
    """解 Amat x = bvec（Amat: m×n, bvec: 长 m）；返回一个解或 None"""
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
    # 相容性
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
    print("=== 推广检验：α0 ∈ im R0ᵀ ⟹ q=2, ρ=1 的解 ===\n")
    n=6; p=1
    tested=0; ok=0; fail=0; skipped=0
    obs_hist={}
    for t in range(1,120):
        rng=random.Random(9300000+t)
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
        Vb=invcl(R0,Ap,d); obs=len(Vb)
        # 取 L0
        L0=None
        for _ in range(200):
            cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(cand)!=1: continue
            if rk(cand+Cc)!=2: continue
            if rk(mm(cand,N))==0: continue
            L0=cand; break
        if L0 is None: continue
        a0=mm(L0,N)[0]
        # 检查 a0 ∈ im R0ᵀ ？
        R0t=[[R0[i][j] for i in range(n)] for j in range(d)]   # d×n
        # im R0ᵀ = 行空间 of R0 = 列空间 of R0t
        R0row = rb(R0)
        if rk([r[:] for r in R0row]+[a0[:]])!=rk(R0row):
            skipped+=1; continue
        # 解 ℓ1: ℓ1 N = 0 且 ℓ1 A N = a0
        # 未知量 ℓ1 ∈ R^n；方程：Nᵀ ℓ1ᵀ = 0 (d 个), (AN)ᵀ ℓ1ᵀ = a0ᵀ (d 个)
        Amat=[]; bvec=[]
        for j in range(d):
            Amat.append([N[i][j] for i in range(n)]); bvec.append(Fr(0))
        for j in range(d):
            Amat.append([AN[i][j] for i in range(n)]); bvec.append(a0[j])
        sol=solve(Amat,bvec)
        tested+=1
        if sol is None:
            fail+=1; print("[%d] 线性系统无解 ✗ (obs=%d)" % (t,obs)); continue
        Lam=[L0[0][:], sol[:]]
        M=mm(Lam,N); F=mm(mm(Lam,A),N)
        rho=rk(M)
        K=ker_basis(M)
        ok5a = (not K or not K[0]) or rk(mm(F,K))==0
        ok5b = cond_5b(M,F)
        if rho==1 and ok5a and ok5b:
            ok+=1
            obs_hist[obs]=obs_hist.get(obs,0)+1
        else:
            fail+=1
            if fail<=3: print("[%d] rho=%d (5a)=%s (5b)=%s ✗" % (t,rho,ok5a,ok5b))
    print()
    print("检验 %d 个（α0 ∈ im R0ᵀ 的实例）；成功 %d ；失败 %d ；跳过 %d（α0 ∉ im R0ᵀ）" % (tested,ok,fail,skipped))
    print("成功实例的 obs 分布：", sorted(obs_hist.items()))
    if tested>0 and ok==tested:
        print()
        print("⟹ *** 推广成立：α0 ∈ im R0ᵀ ⟹ q=2, ρ=1 的解存在 ***")
        print("   ⟹ 每当 α0 ∈ im R0ᵀ，都有 ρ=1 < obs（若 obs≥2）")
    elif ok>0:
        print("\n⟹ 部分成立（%d/%d）" % (ok,tested))

if __name__=="__main__":
    main()
