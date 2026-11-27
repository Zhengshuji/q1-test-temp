r"""
c161_R_family.py -- 构造落在 R 里的实例：r 的 Krylov 维数 = 2（即 rA'^2 ∈ span{r, rA'}）

**背景**（[GAP1](../GAP1_非饱和lift_详细.md) §4.6）：
$p=1,d=3$ 时非饱和候选唯一：$\mathcal A=\operatorname{span}\{\alpha_0,r\}$。
admissibility（lift 的必要条件）要求
$$rA'\in\operatorname{span}\{\alpha_0,r\}$$
而随机的 $(A,C)$ 几乎总给 $r$ 的 Krylov 维数 $=d=3$（10/10），于是 admissibility 自动失败。
要测"$\mathcal R$（Krylov 维数 $=2$）里能否 $\rho=2$ lift"，必须**专门构造**。

**构造**（从约化数据反推）：
1. 取 $n=4,d=3,p=1$，$K=\operatorname{span}\{e_1,e_2,e_3\}$，$N=[I_3;0]$；
2. 取 $A'$ 使 $r=e_1$ 的 Krylov 维数 $=2$：$rA'=e_2,\ rA'^2=0$；
3. 取 $R_0=u\otimes r$（秩 1，$\operatorname{row}R_0=\operatorname{span}\{r\}$），$u_4=0$；
4. 令 $AN:=NA'+R_0$（定义 $A$ 在 $K$ 上），$A e_4:=e_4$；
5. $C:=e_4^{\mathsf T}$ ⟹ $\ker[C;CA]=K$ ✓；
6. 取 $L_0=\ell$ 解 $\ell(AN-cN)=0$ ⟹ $\beta_0=c\,\alpha_0$ ✓（同 `c142`）。

跑法：python scripts/core/c161_R_family.py
"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr

import audit_independent as AI
import c141_invariant_family as F

mul, tr, rank = AI.mul, AI.tr, AI.rank


def build(n=4, d=3, blk=None, u=None):
    """按 §构造 建 (A, C)，返回 (A, C) 或 None"""
    if blk is None:
        # A' = [[0,1,0],[0,0,0],[0,0,2]]：e1 --A'--> e2 --> 0，Krylov=2
        blk = [[Fr(0), Fr(1), Fr(0)],
               [Fr(0), Fr(0), Fr(0)],
               [Fr(0), Fr(0), Fr(2)]]
    Ap = [row[:] for row in blk]
    N = [[Fr(1) if i == j else Fr(0) for j in range(d)] for i in range(n)]  # [I;0]
    if u is None:
        u = [Fr(1), Fr(1), Fr(0), Fr(0)]
    r = [Fr(1), Fr(0), Fr(0)]          # v = e1
    R0 = [[u[i] * r[j] for j in range(d)] for i in range(n)]   # u ⊗ r
    NA = mul(N, Ap)                    # n×d
    AN = [[NA[i][j] + R0[i][j] for j in range(d)] for i in range(n)]
    # A 的列：前 d 列 = AN 的列；第 n 列 = e_n
    A_ = [[AN[i][j] for j in range(d)] for i in range(n)]
    last = [Fr(0)] * n
    last[n - 1] = Fr(1)
    for i in range(n):
        A_[i].append(last[i])
    C = [[Fr(0)] * (n - 1) + [Fr(1)]]  # e_n^T
    return A_, C


def make_instance(seed=0, n=4):
    A_, C = build(n=n)
    # 校验 K = ker[C;CA]
    try:
        Nc = AI.nullspace(AI.vstack([C, mul(C, A_)]))
    except AssertionError:
        return None
    d = len(Nc)
    if d != 3:
        return None
    N = [[Nc[j][i] for j in range(d)] for i in range(n)]
    AN = mul(A_, N)
    rng = random.Random(seed)
    cc = Fr(rng.randint(-2, 2))
    M = [[AN[j][k] - cc * N[j][k] for k in range(d)] for j in range(n)]
    sols = AI.nullspace(tr(M))
    if not sols:
        return None
    L0 = [list(sols[0])]
    D = AI.build_data(A_, C, L0)
    if D["d"] != 3 or all(x == 0 for x in D["alpha0"]):
        return None
    return A_, C, L0, D, cc


def krylov_dim(r, Ap, d):
    K = [r]
    v = r
    for _ in range(d):
        v = mul([v], Ap)[0]
        K.append(v)
    dims = []
    KK = []
    for v2 in K:
        KK.append(v2)
        dims.append(rank(KK))
    return dims


def main():
    print("=" * 76)
    print("构造 R 族：r 的 Krylov 维数 = 2，再检验 A = span{al, r} 能否 rho=2 lift")
    print("=" * 76)
    got = make_instance(0)
    if got is None:
        print("构造失败")
        return
    A_, C, L0, D, cc = got
    n, d = 4, D["d"]
    N, Ap, R0 = D["N"], D["Ap"], D["R0"]
    AN = mul(A_, N)
    al, be = D["alpha0"], mul(L0, AN)[0]
    S = AI.row_basis(R0)
    print(f"d={d} dimS={len(S)}  beta0 ∥ alpha0 ? {AI.in_span(be,[al])}")
    r = S[0]
    print(f"r = {[str(x) for x in r]}")
    print(f"alpha0 = {[str(x) for x in al]}")
    print(f"r 的 Krylov 维数序列 = {krylov_dim(r, Ap, d)}   (期望 1,2,2,...)")
    rAp = mul([r], Ap)[0]
    print(f"rA' ∈ span{{alpha0, r}} ? {AI.in_span(rAp, AI.row_basis([al, r]))}")
    A2 = AI.row_basis([al, r])
    AS = AI.row_basis(A2 + S)
    print(f"dimA={len(A2)}  |A∩S|={len(A2)+len(S)-len(AS)}  dim(A+S)={len(AS)}  (d={d})")
    adm = all(AI.in_span(mul([v], Ap)[0], AS) for v in A2)
    print(f"admissible ? {adm}")
    for q in (3, 4):
        w, _ = F.try_A(A2, A_, C, L0, D, q, random.Random(0), n_trials=6)
        print(f"  q={q}: liftable = {w is not None}")


if __name__ == "__main__":
    main()

# ============================================================================
# 2026-10-22 构造失败两次后记下的**设计约束**（下次从这里开始）
#
# 构造 R 族要同时满足三条：
#
#   (D1) α0 = ℓN 必须是 A' 关于 c 的**左特征向量**
#        （因为 ℓ 满足 ℓ(AN − cN) = 0，且 ℓN = α0 ⟹ α0A' = cα0 mod row(R0)，
#         在 row(R0) ⊥ 的方向上就是左特征向量条件）
#
#   (D2) α0 ∈ V = <row R0>_{A'}（否则**不可行**，见 P1；第一次尝试 α0=e3 ∉ span{e1,e2} 就死在这）
#
#   (D3) β0 ≠ 0（否则 f_1 = 0，λ=0 处 rank F ≤ ρ−1，(b) **平凡失败**，不能测任何东西）
#        —— 第二次尝试取 u=−e2 会让 R0 首列为 0、β0=0，死在这
#
# 同时还要 r 的 Krylov 维数 = 2（这是进 R 的定义）。
#
# **已知可行的方向**：取 A' 有 2 维 Krylov 的 r、一个**非零**左特征向量落在 span{r, rA'} 里，
# 且 R0 的 u 不破坏 (D2)(D3)。需要先解出 u 的自由度（u ∈ R^n，n=4）。
# ============================================================================