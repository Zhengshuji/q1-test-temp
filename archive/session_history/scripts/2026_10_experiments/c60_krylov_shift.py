r"""
c60_krylov_shift.py -- 关键检验：Λ 的自由度是否使 Krylov 维数变化？

【推理】
   约束 Λ_i· M = F_i· （每行 1 个方程）⟹ 每行有 (q − rank M) = 1 个自由参数
   ⟹ 全局自由度 = q 维 ⟹ Λ → Λ + φ cᵀ 对**任意** c ∈ ℝ^q
   ⟹ Λᵀφ → Λᵀφ + c‖φ‖²  ⟹ **Krylov 空间可能变** ✗

【检验】随机 c（不只 e₁ 方向），看 Krylov 维数是否变
"""
import os, io, contextlib, random
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]

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
    Mt=[[M[i][j] for i in range(q)] for j in range(d)]
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
        for ii in range(r,nr):
            if all(m[ii][j]==0 for j in range(q)) and m[ii][q]!=0: return None
        y=[Fr(0)]*q
        for ii,c in enumerate(piv): y[c]=m[ii][q]
        parts.append(y)
    return parts

def krylov_dim(Lam, phi, q):
    u=phi[:]; basis=[]
    for _ in range(q+1):
        if not any(x!=0 for x in u): break
        if rk(basis+[u[:]])>len(basis): basis.append(u[:])
        else: break
        u=[sum(Lam[i][j]*u[i] for i in range(q)) for j in range(q)]
    return len(basis)

def main():
    print("=== Λ 的自由度是否改变 Krylov 维数？ ===\n")
    rng=random.Random(611)
    q=3; d=2
    changed=0; tot=0
    for trial in range(200):
        M=[[Fr(rng.randint(-1,1)) for _ in range(d)] for _ in range(q)]
        if rk(M)!=d: continue
        F=[[Fr(rng.randint(-1,1)) for _ in range(d)] for _ in range(q)]
        Mt=[[M[i][j] for i in range(q)] for j in range(d)]
        ns=nullspace(Mt)
        if not ns: continue
        phi=ns[0]
        Lam0=solve_lambda(M,F,q,d)
        if Lam0 is None: continue
        k0=krylov_dim(Lam0,phi,q)
        # Λ_t = Λ0 + φ cᵀ，随机 c
        kdims=set([k0])
        for _ in range(6):
            c=[Fr(rng.randint(-2,2)) for _ in range(q)]
            Lam1=[[Lam0[i][j]+phi[i]*c[j] for j in range(q)] for i in range(q)]
            # 检查 Λ1 M = F
            ok=all(all(sum(Lam1[i][k]*M[k][j] for k in range(q))==F[i][j] for j in range(d)) for i in range(q))
            if not ok: continue
            kdims.add(krylov_dim(Lam1,phi,q))
        tot+=1
        if len(kdims)>1:
            changed+=1
            if changed<=5:
                print("trial=%d: Krylov 维数集合 = %s  **变化！**" % (trial, sorted(kdims)))
    print()
    print("共 %d 个 (M,F)；Krylov 维数随 c 变化的 %d 个" % (tot,changed))
    if changed>0:
        print("\n⟹ **Krylov 判据不是良定义的** ✗（第 32 处更正）")
        print("   正确且良定义的判据是 E_∞ = 0（只用 Λ 在 im(M) 上的作用）")
    else:
        print("\n⟹ 未观察到变化（需更多样本确认）")


if __name__=="__main__":
    main()
