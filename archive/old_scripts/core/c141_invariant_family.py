r"""
c141_invariant_family.py -- 检验新假设：$A'$-不变族里是否总有解？

背景（2026-10-20）：
  P6b（$\mathcal AA'\subseteq\mathcal A\Rightarrow(5b)$ 必败）已被反例推翻（proof/I、c140）。
  于是被它排除掉的一整族——**$A'$-不变**的 $\mathcal A$——重新进入搜索范围。
  本脚本检验最自然的一个候选：

      $$\mathcal A=\big\langle\,\alpha_0,\ \beta_0,\ S\,\big\rangle_{A'}\quad(A'\text{-闭包})$$

  在 $q=\rho+1$（P4b 允许的最小行数）处是否 liftable。

判定方式（与 c139 相同的思路，但 $\mathcal A$ 任意）：
  * 未知量 $\ell_2,\dots,\ell_q$；约束 $\ell_iN\in\mathcal A$、$\ell_iAN\in\mathcal A$ 都是**线性**的
    （用 $\mathcal A$ 的零化子 $\mathcal A^\perp$ 表示：$v\in\mathcal A\iff v\perp\mathcal A^\perp$）；
  * 在解空间上取样，检验 (b)；命中的点用**原始** (5a)/(5b) 复核。

跑法：python scripts/core/c141_invariant_family.py
"""
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr

import audit_independent as AI

mul, tr, rank, rref = AI.mul, AI.tr, AI.rank, AI.rref
vstack, row_basis, in_span = AI.vstack, AI.row_basis, AI.in_span
cond_5a_orig, cond_5b_orig = AI.cond_5a_orig, AI.cond_5b_orig


def annihilator(basis):
    r"""$\mathcal A^\perp$ 的基（行向量，长度 d）"""
    if not basis: return []
    return AI.nullspace(basis)          # {w : basis · w = 0}，返回的是列向量


def closure(rows0, Ap):
    r"""$\langle rows0\rangle_{A'}$：对右乘 $A'$ 取闭包"""
    B = row_basis(rows0) if rows0 else []
    while True:
        if not B: return []
        B2 = row_basis(vstack([B, mul(B, Ap)]))
        if len(B2) == len(B): return B
        B = B2


def solve_affine(rows_eq, rhs, n):
    A = [list(rows_eq[i]) + [rhs[i]] for i in range(len(rows_eq))]
    R, piv = rref(A)
    if n in piv: return None
    x0 = [Fr(0)] * n
    for i, p in enumerate(piv): x0[p] = R[i][n]
    free = [c for c in range(n) if c not in piv]
    basis = []
    for f in free:
        v = [Fr(0)] * n; v[f] = Fr(1)
        for i, p in enumerate(piv): v[p] = -R[i][f]
        basis.append(v)
    return x0, basis


def try_A(Arows, A_, C, L0, D, q, rng, n_trials=10):
    r"""给定 $\mathcal A$（行基 Arows，首行须为 $\alpha_0$）与 $q$，判定是否 liftable"""
    N, AN = D["N"], mul(A_, D["N"])
    n, d, rho = AI.cols(A_), D["d"], len(Arows)
    W = annihilator(Arows)                     # (d-rho) 个行向量
    rows_eq, rhs = [], []
    m = q - 1
    for i in range(m):
        for w in W:
            e = [Fr(0)] * (m * n)
            for j in range(n):
                e[i * n + j] = sum(N[j][k] * w[k] for k in range(d))
            rows_eq.append(e); rhs.append(Fr(0))
            e = [Fr(0)] * (m * n)
            for j in range(n):
                e[i * n + j] = sum(AN[j][k] * w[k] for k in range(d))
            rows_eq.append(e); rhs.append(Fr(0))
    if not rows_eq:                      # A = R^d：无约束
        x0, ker = [Fr(0)] * (m * n), [[Fr(1) if i == j else Fr(0) for i in range(m * n)] for j in range(m * n)]
    else:
        sol = solve_affine(rows_eq, rhs, m * n)
        if sol is None: return None, 0
        x0, ker = sol
    for _ in range(n_trials):
        x = list(x0)
        for v in ker:
            c = Fr(rng.randint(-2, 2))
            x = [x[j] + c * v[j] for j in range(m * n)]
        L = [list(L0[0])] + [x[i * n:(i + 1) * n] for i in range(m)]
        if rank(mul(L, N)) != rho: continue
        if cond_5a_orig(A_, C, L) and cond_5b_orig(A_, C, L):
            return L, len(ker)
    return None, len(ker)


def run(seed, n=5, n_trials=10):
    rng = random.Random(seed)
    A_, C, L0, D = AI.rand_instance(rng, n)
    al, be = D["alpha0"], mul(L0, mul(A_, D["N"]))[0]
    S = AI.row_basis(D["R0"]) if rank(D["R0"]) > 0 else []
    rows0 = [al, be] + ([list(r) for r in S] if S else [])
    Arows = closure(rows0, D["Ap"])
    rho = len(Arows)
    out = dict(seed=seed, d=D["d"], rho=rho, obs=D["obs"], dimS=len(S) if S else 0,
               inA_S=None, lift=None, q=None, ker=None, inV=D["inV"])
    if rho == 0: return out
    # A ∩ S 的维数
    out["inA_S"] = rho + (len(S) if S else 0) - rank(Arows + (S if S else []))
    q = rho + 1
    out["q"] = q
    wit, ker = try_A(Arows, A_, C, L0, D, q, random.Random(seed + 1000), n_trials)
    out["lift"] = wit is not None
    out["ker"] = ker
    return out


if __name__ == "__main__":
    print("=" * 84)
    print("假设检验： A = <a0, b0, S>_{A'}  （A'-不变），在 q = rho+1 处 liftable ?")
    print("=" * 84)
    print(f"{'seed':>4} {'d':>2} {'rho':>3} {'obs':>3} {'inV':>5} {'dimS':>4} {'A∩S':>4} {'q':>2} {'liftable':>8} {'解空间维':>7}")
    stats = dict(inst=0, lift=0, byrho={})
    for seed in range(20):
        o = run(seed)
        if o["rho"] == 0: continue
        stats["inst"] += 1
        stats["lift"] += bool(o["lift"])
        stats["byrho"][o["rho"]] = stats["byrho"].get(o["rho"], 0) + (1 if o["lift"] else 0)
        print(f"{o['seed']:>4} {o['d']:>2} {o['rho']:>3} {o['obs']:>3} {str(o['inV']):>5} {o['dimS']:>4} "
              f"{o['inA_S']:>4} {o['q']:>2} {str(o['lift']):>8} {o['ker']:>7}")
    print("-" * 84)
    print(f"实例 {stats['inst']}；liftable {stats['lift']}；按 rho 的 lift 数 {stats['byrho']}")
    print("⚠️ P1 必要性自检：任何 liftable=True 都必须 inV=True（否则 P1 被违反）")
