r"""
c159_admissibility_equivalence.py -- 验证 §1.5 的核心等价（单条命令）

命题（[proof/S](../proof/S_维数下界定理_2026-10-21.md) §1.3–1.5）：

  对 **admissible** 的 A（即 $\mathcal A\mathcal A'\subseteq\mathcal A+S$）：

  $$(L\text{-}1):\ \dim V_{\mathcal A}=n-2(d-\rho)\qquad\Longleftrightarrow\qquad \mathcal A+S=\mathbb{R}^d$$

  * "饱和 ⟹ (L-1)" 在 §1.3 已证；
  * "非饱和 ⟹ (L-1) 失效" 在 §1.5 已证。

本脚本对随机 A 与 P7 型 A 逐组计算：

  adm = (A A' ⊆ A + S);  sat = (dim(A+S) == d);  L1 = (dim V_A == n-2(d-rho))

并检查：adm ⟹ (L1 ⟺ sat)。

跑法：python scripts/core/c159_admissibility_equivalence.py
"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr

import audit_independent as AI
import c141_invariant_family as F

mul = AI.mul


def make_instance(rng, n, d_t, p):
    for _ in range(60):
        A_ = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if AI.rank(C) != p:
            continue
        if AI.rank(AI.vstack([C, mul(C, A_)])) != n - d_t:
            continue
        L0 = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        D = AI.build_data(A_, C, L0)
        if D["d"] != d_t:
            continue
        return A_, C, L0, D
    return None


def probe(Ar, A_, D, n):
    d = D["d"]
    N, AN, Ap = D["N"], mul(A_, D["N"]), D["Ap"]
    S = AI.row_basis(D["R0"])
    AS = AI.row_basis(Ar + S)
    sat = (len(AS) == d)
    adm = all(AI.in_span(mul([v], Ap)[0], AS) for v in Ar)
    ann = F.annihilator(Ar)
    rows = []
    for w in ann:
        rows.append([sum(N[j][k] * w[k] for k in range(d)) for j in range(n)])
        rows.append([sum(AN[j][k] * w[k] for k in range(d)) for j in range(n)])
    if not rows:
        L1 = True
    else:
        sol = F.solve_affine(rows, [Fr(0)] * len(rows), n)
        dimV = len(sol[1]) if sol else 0
        L1 = (dimV == n - 2 * (d - len(Ar)))
    return adm, sat, L1


def main():
    print("=" * 72)
    print("§1.5 等价验证：admissible ⟹ (L-1) ⟺ A+S=R^d")
    print("=" * 72)
    tab = {}

    def bump(t):
        tab[t] = tab.get(t, 0) + 1

    for (n, d_t, p) in ((6, 4, 1), (5, 3, 1), (8, 4, 2), (7, 3, 2), (10, 4, 3)):
        got = make_instance(random.Random(1), n, d_t, p)
        if got is None:
            continue
        A_, C, L0, D = got
        for trial in range(12):
            rr = random.Random(d_t * 1000 + trial)
            rho = rr.randint(1, d_t)
            Ar = [[Fr(rr.randint(-2, 2)) for _ in range(d_t)] for _ in range(rho)]
            Ar = AI.row_basis(Ar)
            if len(Ar) != rho:
                continue
            bump(probe(Ar, A_, D, n))

    try:
        import c142_rho1_family as R1
        for seed in range(6):
            rng = random.Random(seed)
            try:
                A_, C, L0, D, c = R1.make_instance(rng, n=6)
            except AssertionError:
                continue
            if D["d"] != 4:
                continue
            be = mul(L0, mul(A_, D["N"]))[0]
            if not AI.in_span(be, [D["alpha0"]]):
                continue
            bump(probe([D["alpha0"]], A_, D, 6))
    except Exception as ex:
        print("  （P7 型构造跳过：", ex, "）")

    print("(adm, sat, L1) → 计数")
    for k in sorted(tab):
        print("   ", k, tab[k])
    viol = sum(tab[k] for k in tab if k[0] and not k[1] and k[2])
    viol2 = sum(tab[k] for k in tab if k[0] and k[1] and not k[2])
    tot_adm = sum(tab[k] for k in tab if k[0])
    print("-" * 72)
    print(f"admissible 组：{tot_adm}；违反等价：{viol + viol2}")
    print("  · adm ∧ ¬sat ∧ L1（应为 0）:", viol)
    print("  · adm ∧ sat ∧ ¬L1（应为 0）:", viol2)


if __name__ == "__main__":
    main()
