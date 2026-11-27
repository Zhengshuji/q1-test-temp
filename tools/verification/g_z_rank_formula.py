"""g_z_rank_formula.py —— $G_{\\mathcal Z}$ 的秩公式与"$(5a)$ 自动成立"的条件

设 $\\mathcal Z=\\ker[C;\\mathcal L]$、$\\mathcal Z^{\\perp}=\\operatorname{row}[C;\\mathcal L]$（$\\dim=p+q$）、$W=\\operatorname{row}[C;CA]$。
定义
$$\\varphi:\\ \\mathcal Z^{\\perp}\\longrightarrow \\mathbb C^{n}/(\\mathcal Z^{\\perp}+W),\\qquad \\ell\\longmapsto \\ell A\\ \\bmod\\ (\\mathcal Z^{\\perp}+W).$$
则

* $G_{\\mathcal Z}=\\ker\\varphi$，故 $\\dim G_{\\mathcal Z}=(p+q)-\\operatorname{rank}\\varphi$；
* **必要条件** $\\dim G_{\\mathcal Z}\\ge q\\iff\\operatorname{rank}\\varphi\\le p$；
* **自动成立**：若 $\\dim(\\mathcal Z^{\\perp}+W)=n$（即 $h=n$，由 B.11），则 $\\varphi=0$、$G_{\\mathcal Z}=\\mathcal Z^{\\perp}$，
  于是 $(5a)$ 对**每个**补都成立。

本脚本核验这三条。

用法：python -u tools/verification/g_z_rank_formula.py
"""

import os
import sys
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import type3_structured as T3             # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import g_z_criterion as GZc               # noqa: E402

F = Fraction


def rank_phi(A, C, Z):
    """$\\operatorname{rank}\\varphi$：$\\ell\\mapsto\\ell A$ 模 $\\mathcal Z^{\\perp}+W$ 的秩。"""
    n = len(A)
    CA = LQ.mul(C, A)
    W = [x[:] for x in C] + [x[:] for x in CA]
    ZT = [[Z[i][j] for i in range(n)] for j in range(len(Z[0]))]
    B = [list(x) for x in LQ.nullspace(ZT)]
    S = [x[:] for x in B] + [x[:] for x in W]
    rS = LQ.rank(S)
    # φ 的秩 = 把所有 ℓA 并到 S 上增加的秩
    gens = [LQ.mul([b], A)[0] for b in B]
    return LQ.rank(S + gens) - rS


def main():
    import random
    checked = bad1 = bad2 = bad3 = 0
    auto_cases = 0
    for n in (5, 6, 7):
        for p in (1, 2):
            for r in (1, 2):
                if p + r > n:
                    continue
                for seed in range(3000, 3006):
                    made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
                    if made is None:
                        continue
                    A, C, L0 = made
                    O = QR.observability_matrix(A, C)
                    if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
                        continue
                    q0 = Q0.eta_and_q0(A, C, L0)[0]
                    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
                    mm = len(K[0])
                    d = n - p - q0
                    if d <= 0:
                        continue
                    rng = random.Random(seed * 3 + q0)
                    for _ in range(30):
                        Wm = [[F(rng.randrange(-3, 4)) for _ in range(d)] for _ in range(mm)]
                        Z = [[sum(K[i][t] * Wm[t][j] for t in range(mm)) for j in range(d)]
                             for i in range(n)]
                        if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                            continue
                        G, B, rS = GZc.G_of(A, C, Z)
                        dimG = LQ.rank(G)
                        rphi = rank_phi(A, C, Z)
                        dimZp = len(B)
                        h = rS                                   # = dim(Z⊥+W)（B.11）
                        checked += 1
                        if dimG != dimZp - rphi:
                            bad1 += 1
                        if (dimG >= q0) != (rphi <= p):
                            bad2 += 1
                        if h == n:
                            auto_cases += 1
                            # 自动成立：任取一个补都应满足 (5a)
                            L = ZG.L_from_Z(A, C, L0, Z, q0)
                            if L is None or not LQ.condA(A, C, L):
                                bad3 += 1
    print(f'检查 {checked} 个 (Z, 实例)：')
    print(f'  dim G_Z = (p+q) - rank φ 失败 {bad1}')
    print(f'  (dim G_Z ≥ q0) ⟺ (rank φ ≤ p) 失败 {bad2}')
    print(f'  h=n 的 {auto_cases} 个中，(5a) 自动成立失败 {bad3}')
    assert bad1 == 0 and bad2 == 0 and bad3 == 0
    print('✓ 三条全部通过')


if __name__ == '__main__':
    main()
