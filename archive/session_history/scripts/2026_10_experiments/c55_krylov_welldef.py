r"""
c55_krylov_welldef.py -- 检验 Krylov 判据是否良定义

【疑问】Λ 只被 "Λ M = F" 确定到 Λ → Λ + φ wᵀ（行空间在 span φ 内的秩 1 扰动）
   而 Krylov 维数用 Λᵀ 与 φ ⟹ 可能依赖 w ⟹ **判据不好定义**

【检验】对同一 (M,F)：取两个不同的 Λ（不同 w），比较
   · (5b)（应不变，因它只依赖 Λ 在 im(M) 上的作用）
   · Krylov 维数（若变化 ⟹ 判据不好定义 ✗）
"""
import os, io, contextlib, random, itertools
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]

def nullspace(M):
    if not M or not M[0]: return []
    m=len(M); n=len(M[0])
    A=[[Fr(x) for x in row] for row in M]
    piv=[]; r=0
    for c in range(n):
        p=None
        for i in range(r,m):
            if A[i][c]!=0: p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]!=0:
                f=A[i][c]
                A[i]=[A[i][j]-f*A[r][j] for j in range(n)]
        piv.append(c); r+=1
        if r==m: break
    free=[c for c in range(n) if c not in piv]
    out=[]
    for fc in free:
        v=[Fr(0)]*n; v[fc]=Fr(1)
        for i,c in enumerate(piv): v[c]=-A[i][fc]
        out.append(v)
    return out

def solve_lambda(M,F,q,d):
    """求 Λ（q×q）满足 Λ M = F；返回 (特解, 齐次生成元列表 as q×q)"""
    # 逐行：Λ_iᵀ M = F_i  ⟺  Mᵀ Λ_i = F_iᵀ
    Mt=[[M[i][j] for i in range(q)] for j in range(d)]     # d×q
    homo_rows=nullspace(Mt)        # {y ∈ ℝ^q : yᵀM = 0}
    parts=[]
    for i in range(q):
        rhs=[F[i][j] for j in range(d)]
        m=[[Mt[r][c] for c in range(q)]+[rhs[r]] for r in range(d)]
        nr=len(m); piv=[]; r=0
        for c in range(q):
            p=None
            for ii in range(r,nr):
                if m[ii][c]!=0: p=ii; break
            if p is None: continue
            m[r],m[p]=m[p],m[r]
            pv=m[r][c]; m[r]=[x/pv for x in m[r]]
            for ii in range(nr):
                if ii!=r and m[ii][c]!=0:
                    f=m[ii][c]
                    m[ii]=[m[ii][j]-f*m[r][j] for j in range(q+1)]
            piv.append(c); r+=1
            if r==nr: break
        ok=True
        for ii in range(r,nr):
            if all(m[ii][j]==0 for j in range(q)) and m[ii][q]!=0: ok=False
        if not ok: return None,None
        y=[Fr(0)]*q
        for ii,c in enumerate(piv): y[c]=m[ii][q]
        parts.append(y)
    return parts, homo_rows

def krylov_dim(Lam, phi, q):
    """dim span{φ, Λᵀφ, ...}"""
    u=phi[:]
    basis=[]
    for _ in range(q+1):
        if not any(x!=0 for x in u): break
        cand=basis+[u[:]]
        if rk(cand)>len(basis):
            basis.append(u[:])
        else:
            break
        # u ← Λᵀ u
        u=[sum(Lam[i][j]*u[i] for i in range(q)) for j in range(q)]
    return len(basis)

def main():
    print("=== Krylov 判据是否良定义？ ===\n")
    rng=random.Random(777)
    q=3; d=2
    nfound=0
    for trial in range(300):
        M=[[Fr(rng.randint(-1,1)) for _ in range(d)] for _ in range(q)]
        if rk(M)!=d: continue
        # 任取 F 使 Λ 存在（自动，因 row(M)=ℝ^d）
        F=[[Fr(rng.randint(-1,1)) for _ in range(d)] for _ in range(q)]
        parts,homo=solve_lambda(M,F,q,d)
        if parts is None: continue
        if not homo: continue
        # φ = 左零向量
        phi=[] 
        # 找 Mᵀ 的零空间（q 维向量）
        Mt=[[M[i][j] for i in range(q)] for j in range(d)]
        ns=nullspace(Mt)
        if not ns: continue
        phi=ns[0]
        Lam1=[p[:] for p in parts]
        # 第二个 Λ：给某一行加 c·h
        Lam2=[p[:] for p in parts]
        c=Fr(rng.choice([-2,-1,1,2]))
        h=homo[0]
        Lam2[0]=[Lam2[0][j]+c*h[j] for j in range(q)]
        # 验证两者都满足 ΛM=F
        ok1=all(all(sum(Lam1[i][k]*M[k][j] for k in range(q))==F[i][j] for j in range(d)) for i in range(q))
        ok2=all(all(sum(Lam2[i][k]*M[k][j] for k in range(q))==F[i][j] for j in range(d)) for i in range(q))
        k1=krylov_dim(Lam1,phi,q); k2=krylov_dim(Lam2,phi,q)
        print("trial=%d: Λ₁,Λ₂ 都满足 ΛM=F? %s/%s ; Krylov 维数: %d vs %d  %s" %
              (trial, ok1, ok2, k1, k2, "**不同 ⟹ 判据不好定义** ✗" if k1!=k2 else "相同"))
        nfound+=1
        if nfound>=6: break
    print()
    print("【结论】若出现『不同』⟹ Krylov 判据 **不是良定义的** ✗（第 32 处更正）")
    print("        正确的、良定义的判据是 E_∞ = 0（即 H_∞=0，只用 Λ 在 im(M) 上的作用）")


if __name__=="__main__":
    main()
