r"""
c138_S_extension.py -- 新候选：A = A_* + <s>（A_* = A'-闭包 of alpha0，s ∈ S）

关键：这个 A **不是** A'-不变的（因为 sA' ∈ A_* + S 但一般 ∉ A_* + <s>），
      所以 P6b 的障碍（A'-不变 ⟹ (b) 必败）不适用。
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
    if not Amat: return None
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

def Aclosure(seed,Ap,d):
    B=rb(seed)
    while True:
        newB=rb(B+mm(B,Ap))
        if len(newB)==len(B): return B
        B=newB

def try_A(As,Ap,S,Nt,ANt,A,N,n,d):
    """给定 A（行基），检查 admissible + 交非零 + lift + (a)(b)"""
    k=len(As)
    if k==0: return None
    # admissible: A A' ⊆ A + S
    lhs=rb([r[:] for r in As]+[r[:] for r in mm(As,Ap)]+[r[:] for r in S])
    rhs=rb([r[:] for r in As]+[r[:] for r in S])
    if len(lhs)!=len(rhs): return None
    # A ∩ S ≠ 0
    if not rb([v for v in As if rk(S+[v])==len(S)]): return None
    # lift
    rows=[]; ok=True
    for a in As:
        Amat=[]; bv=[]
        for tt in range(d):
            Amat.append([Nt[tt][i] for i in range(n)]+[Fr(0)]*k); bv.append(a[tt])
        for tt in range(d):
            Amat.append([ANt[tt][i] for i in range(n)]+[-As[i][tt] for i in range(k)]); bv.append(Fr(0))
        sp=solve(Amat,bv)
        if sp is None: ok=False; break
        rows.append(sp[:n])
    if not ok: return None
    q=len(rows)
    M=[[sum([rows[i][j]*Nt[k2][j] for j in range(n)],Fr(0)) for k2 in range(d)] for i in range(q)]
    LA=[[sum([rows[i][j]*A[j][k2] for j in range(n)],Fr(0)) for k2 in range(n)] for i in range(q)]
    F=[[sum([LA[i][j]*Nt[k2][j] for j in range(n)],Fr(0)) for k2 in range(d)] for i in range(q)]
    K=ker_basis(M)
    ok5a=(not K or not K[0]) or rk(mm(F,K))==0
    if not ok5a: return None
    if cond_5b(M,F): return (len(As), M, F)
    return None

def main():
    print("=== 新候选：A = A_*(alpha0) + <s>,  s ∈ S ===\n")
    n=6; p=2
    tested=0; ok_cand=0; sols=0
    for t in range(1,90):
        rng=random.Random(7788000+t)
        A=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc)!=p: continue
        CA=mm(Cc,A); Mr=Cc+CA
        if rk(Mr)!=4: continue
        N=ker_basis(Mr); d=len(N[0]); AN=mm(A,N)
        Nt=[[N[i][j] for i in range(n)] for j in range(d)]
        ANt=[[AN[i][j] for i in range(n)] for j in range(d)]
        iN=minv(mm(Nt,N))
        if iN is None: continue
        Ap=mm(mm(iN,Nt),AN)
        R0=[[AN[i][j]-mm(N,Ap)[i][j] for j in range(d)] for i in range(n)]
        S=rb(R0)
        if not S: continue
        L0=None
        for _ in range(60):
            cand=[[Fr(rng.randint(-1,1)) for _ in range(n)]]
            a0=mm(cand,N)[0]
            if all(x==0 for x in a0): continue
            L0=cand; break
        if L0 is None: continue
        a0=mm(L0,N)[0]
        tested+=1
        Astar=Aclosure([a0],Ap,d)
        got=None
        # 解线性系统：s ∈ S 使 sA' ∈ A_* + S
        # s = Σ c_j S_j ; 条件 (sA') mod (A_*+S) = 0
        basis_AS=rb([r[:] for r in Astar]+[r[:] for r in S])
        # 对每个 j：计算 S_j A' 在 basis_AS 下的坐标残差
        # 用零空间法：构造矩阵 [S_j A'] 与 basis_AS 的行关系
        # 未知 c=(c_j)：(Σ c_j S_j)A' = Σ p_l basis_AS_l ⟹ 线性系统
        nS=len(S); nAS=len(basis_AS)
        Amat=[]
        for tt in range(d):
            # 第 tt 个坐标：Σ_j c_j (S_j A')_tt - Σ_l p_l basis_AS[l][tt] = 0
            row=[sum([S[j][k]*Ap[k][tt] for k in range(d)],Fr(0)) for j in range(nS)]
            row=row+[-basis_AS[l][tt] for l in range(nAS)]
            Amat.append(row)
        nsols=nullsp(Amat)
        for sol in nsols:
            cs=sol[:nS]
            s=[sum([cs[j]*S[j][i] for j in range(nS)],Fr(0)) for i in range(d)]
            if all(v==0 for v in s): continue
            As=rb([r[:] for r in Astar]+[s[:]])
            if len(As)!=len(Astar)+1: continue
            r=try_A(As,Ap,S,Nt,ANt,A,N,n,d)
            if r is not None:
                ok_cand+=1
                if got is None or r[0]<got: got=r[0]
        if got is not None:
            sols+=1
    print("检验 %d 个实例" % tested)
    print("  合格候选数：%d" % ok_cand)
    print("  **成功构造 (a)∧(b) 的实例：%d**" % sols)

if __name__=="__main__":
    main()
