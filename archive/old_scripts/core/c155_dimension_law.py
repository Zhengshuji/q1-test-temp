r"""
c155_dimension_law.py -- 验证维数下界定理（[proof/S](../proof/S_维数下界定理_2026-10-21.md)）

定理：
  $$\dim\{\ell N:\ \ell\in V_{\mathcal A}\}=2\rho-d+p-|\mathcal A\cap S|$$
  $$\Longrightarrow\ \text{任何解满足}\ \rho\ge d-p+|\mathcal A\cap S|$$

本脚本对若干 $\mathcal A$（含 $S$ 的、与 $S$ 交一维的、$\rho=4$ 的、$\rho=2$ 的）
逐个算出左边（实测）与右边（公式），比较。

跑法：python scripts/core/c155_dimension_law.py
"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fractions import Fraction as Fr

import audit_independent as AI
import c141_invariant_family as F

mul = AI.mul


def make_instance(rng, n=8, d_t=4, p=2):
    for _ in range(80):
        A_ = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if AI.rank(C) != p:
            continue
        if AI.rank(AI.vstack([C, mul(C, A_)])) != n - d_t:
            continue
        return A_, C
    return None


def dim_image(Ar, A_, D, n):
    """dim{ell N : ell in V_A}"""
    d = D["d"]
    N, AN = D["N"], mul(A_, D["N"])
    ann = F.annihilator(Ar)
    rows = []
    for w in ann:
        rows.append([sum(N[j][k] * w[k] for k in range(d)) for j in range(n)])
        rows.append([sum(AN[j][k] * w[k] for k in range(d)) for j in range(n)])
    if not rows:
        ker = [[Fr(1) if i == j else Fr(0) for i in range(n)] for j in range(n)]
    else:
        sol = F.solve_affine(rows, [Fr(0)] * len(rows), n)
        if sol is None:
            return 0
        x0, ker = sol
    imgs = [mul([v], N)[0] for v in ker]
    return AI.rank(imgs) if imgs else 0


def main():
    print("=" * 78)
    print("维数下界定理：dim{ellN : ell in V_A} = 2*rho - d + p - |A∩S|")
    print("=" * 78)
    tot = bad = 0
    for seed in range(4):
        rng = random.Random(seed)
        got = make_instance(rng)
        if got is None:
            continue
        A_, C = got
        d, n = 4, 8
        D0 = AI.build_data(A_, C, [[Fr(1)] + [Fr(0)] * (n - 1)])
        N, R0 = D0["N"], D0["R0"]
        S = AI.row_basis(R0)
        AN = mul(A_, N)
        s0 = S[0]
        NtN = mul(AI.tr(N), N)
        L0 = mul([s0], mul(AI.inv(NtN), AI.tr(N)))
        D = AI.build_data(A_, C, L0)
        al = D["alpha0"]
        be = mul(L0, mul(A_, N))[0]
        cands = [
            ("含S  ", AI.row_basis([al, be] + S)),
            ("交1维", AI.row_basis([al, be, [Fr(1), Fr(0), Fr(0), Fr(0)]])),
            ("rho=4", AI.row_basis([al, be] + S + [[Fr(0), Fr(1), Fr(0), Fr(0)]])),
            ("rho=2", AI.row_basis([al, be])),
        ]
        for tag, Ar in cands:
            rho = len(Ar)
            if rho > d:
                continue
            inter = rho + len(S) - AI.rank(AI.row_basis(Ar + S))
            if inter < 0:
                continue
            got_img = dim_image(Ar, A_, D, n)
            pred = 2 * rho - d + len(S) - inter
            tot += 1
            ok = (pred == got_img)
            bad += (not ok)
            print(f"  seed{seed} {tag}: rho={rho} |A∩S|={inter} "
                  f"实测={got_img} 公式={pred} {'✓' if ok else '✗'}")
    print("-" * 78)
    print(f"合计 {tot}，不符 {bad}")
    print("结论：公式成立 ⟹ ρ ≥ d-p+|A∩S| ≥ d-p+1 ⟹ q_min ≥ d+2-p")


if __name__ == "__main__":
    main()
