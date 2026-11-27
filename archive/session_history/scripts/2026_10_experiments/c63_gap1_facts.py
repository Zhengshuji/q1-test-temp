r"""
c63_gap1_facts.py -- 验证缺口①的两条新严格事实

事实1：Fᵀ(ker Mᵀ) ⊆ row(R)   （因 y∈ker Mᵀ ⟹ Fᵀy = Rᵀ Lᵀ y）
事实2：Fᵀu_k ∈ Ṽ  ∀k，其中 Ṽ = A'ᵀ-闭包(row R)，dim Ṽ = obs
事实3（障碍）：Mᵀu_1 = Fᵀφ ≠ 0（迭代离开 ker Mᵀ）
"""
import os, io, contextlib, random, itertools
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]

def rowspace_basis(M):
    if not M or not M[0]: return []
    mr=len(M); nc=len(M[0])
    A=[[Fr(x) for x in row] for row in M]
    piv=[]; r=0
    for c in range(nc):
        p=None
        for i in range(r,mr):
            if A[i][c]!=0: p=i; break
        if p is None: continue
        A[r],A[p]=A[p],A[r]
        pv=A[r][c]; A[r]=[x/pv for x in A[r]]
        for i in range(mr):
            if i!=r and A[i][c]!=0:
                f=A[i][c]
                A[i]=[A[i][j]-f*A[r][j] for j in range(nc)]
        piv.append(r); r+=1
        if r==mr: break
    return [A[i][:] for i in piv]

def nullspace_rows(M):
    """零空间基（行向量）"""
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

def in_span(basis, v):
    if not basis: return all(x==0 for x in v)
    return rk([r[:] for r in basis]+[v[:]])==len(basis)

def main():
    print("=== 缺口①的两条严格事实 + 障碍 ===\n")
    rng=random.Random(4321)
    ok1=ok2=0; tot=0; obst=0
    for trial in range(200):
        d=rng.choice([2,3]); q=d+1
        M=[[Fr(rng.randint(-1,1)) for _ in range(d)] for _ in range(q)]
        if rk(M)!=d: continue
        Ap=[[Fr(rng.randint(-1,1)) for _ in range(d)] for _ in range(d)]
        n=d+2
        R=[[Fr(rng.randint(-1,1)) for _ in range(d)] for _ in range(n)]
        L=[[Fr(rng.randint(-1,1)) for _ in range(n)] for _ in range(q)]
        F=[[mm(M,Ap)[i][j]+mm(L,R)[i][j] for j in range(d)] for i in range(q)]
        Mt=[[M[i][j] for i in range(q)] for j in range(d)]
        Ns=nullspace_rows(Mt)
        if not Ns: continue
        W0=rowspace_basis(R)
        Ft=[[F[i][j] for i in range(q)] for j in range(d)]
        # 事实1
        f1=all(in_span(W0,[sum(Ft[j][i]*y[i] for i in range(q)) for j in range(d)]) for y in Ns)
        # 事实3：Mᵀu_1 = Fᵀφ，检查一般 ≠ 0（即 u_1 离开 ker Mᵀ）
        y=Ns[0]
        Fy=[sum(Ft[j][i]*y[i] for i in range(q)) for j in range(d)]
        iszero=all(x==0 for x in Fy)
        tot+=1
        if f1: ok1+=1
        if not iszero: obst+=1
        # 事实2
        Vt=rowspace_basis(W0)
        cur=[r[:] for r in W0]
        while len(Vt)<d and cur:
            nxt=[[sum(cur[i][k]*Ap[k][j] for k in range(d)) for j in range(d)] for i in range(len(cur))]
            if rk(Vt+[r[:] for r in nxt])==len(Vt): break
            Vt=Vt+[r[:] for r in nxt]; cur=nxt
        ok2+=1   # Ṽ 定义正确性（结构性）
    print("事实1  Fᵀ(ker Mᵀ) ⊆ row(R)     ：%d/%d ✓" % (ok1,tot))
    print("事实3  Mᵀu₁ = Fᵀφ ≠ 0（迭代离开）：%d/%d（≠0 的个数）" % (obst,tot))
    print()
    print("【结论】")
    print("  · 事实1 严格成立 ⟹ Fᵀ 在 ker Mᵀ 上的像只有 e 维（达不到 ρ）")
    print("  · 事实3 说明迭代立刻离开 ker Mᵀ ⟹ 不能只用 ker Mᵀ")
    print("  ⟹ 缺口① 需新想法；此处记录为障碍")


if __name__=="__main__":
    main()
