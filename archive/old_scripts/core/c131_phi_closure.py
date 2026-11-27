r"""
c131_phi_closure.py -- 检验 Φ-闭包猜测：ρ_min = dim(Φ-闭包 of span{α0})

Φ(A) = { ℓ N : ℓ N ∈ A 且 ℓ A N ∈ A }
"""
import os, io, contextlib, random, sys, itertools
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

def Phi(Nmat, ANmat, Abasis, n, d):
    """Phi(A) = { ℓN : ℓN ∈ A, ℓAN ∈ A }"""
    k=len(Abasis)
    if k==0: return []
    # 未知：ℓ (n), c (k), e (k)
    # 方程：ℓN - Σc_i a_i = 0  (d 个)
    #       ℓAN - Σe_i a_i = 0 (d 个)
    nv=n+2*k
    Amat=[]
    for t in range(d):
        row=[Nmat[t][i] for i in range(n)] + [-Abasis[i][t] for i in range(k)] + [Fr(0)]*k
        Amat.append(row)
    for t in range(d):
        row=[ANmat[t][i] for i in range(n)] + [Fr(0)]*k + [-Abasis[i][t] for i in range(k)]
        Amat.append(row)
    sols=nullsp(Amat)
    out=[]
    for s in sols:
        l=s[:n]
        v=mm([l],Nmat)  # 1×d ? 需要转置
    # Nmat 是 d×n，ℓ 是 1×n → ℓ·Nᵀ? 这里 Nmat[t][i] 表示第 t 行第 i 列 = N[i][t]
    # 所以 (ℓN)_t = Σ_i ℓ_i N[i][t] = Σ_i Nmat[t][i] ℓ_i  ✓
    out=[]
    for s in sols:
        l=s[:n]
        val=[sum(Nmat[t][i]*l[i] for i in range(n)) for t in range(d)]
        if any(v!=0 for v in val): out.append(val)
    return rb(out)

def main():
    print("=== 检验 Φ-闭包猜测 ===\n")
    n=6; p=2
    for t in range(1,4):
        rng=random.Random(9990000+t)
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc)!=p: continue
        CA=mm(Cc,A); Mr=Cc+CA
        if rk(Mr)!=4: continue
        N=ker_basis(Mr); d=len(N[0]); AN=mm(A,N)
        Nt=[[N[i][j] for i in range(n)] for j in range(d)]
        iN=minv(mm(Nt,N)); Ap=mm(mm(iN,Nt),AN)
        R0=[[AN[i][j]-mm(N,Ap)[i][j] for j in range(d)] for i in range(n)]
        # 取 L0 满足 alpha0 != 0
        L0=None
        for _ in range(200):
            cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            if rk(cand)!=1: continue
            a=mm(cand,N)[0]
            if all(x==0 for x in a): continue
            L0=cand; break
        if L0 is None: continue
        a0=mm(L0,N)[0]
        # Φ-闭包
        Ab=rb([a0])
        seq=[len(Ab)]
        for it in range(20):
            Nb=Phi(Nt,[[AN[i][j] for i in range(n)] for j in range(d)],Ab,n,d)
            newb=rb(Ab+Nb)
            seq.append(len(newb))
            if len(newb)==len(Ab): break
            Ab=newb
        print("[%d] d=%d  ;  Φ-闭包维数序列 = %s  最终 = %d" % (t,d,seq,len(Ab)))
        # 检查是否有 ρ=dim(闭包) 的解（用 c121 式搜索粗略验证）
        a0_ = a0
        print("     alpha0 =", [str(x) for x in a0_], " 闭包基:", [[str(x) for x in r] for r in Ab])

if __name__=="__main__":
    main()
