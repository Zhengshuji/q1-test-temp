"""nullspace_vs_toeplitz.py —— 交叉核对专家式 (12) 与 Toeplitz 判据

**零空间判据**（专家答复式 (12)）：
$$(5b)\\iff \\operatorname{rank}\\bigl[(\\lambda I-A)V\\ |\\ Z\\bigr]=\\operatorname{rank}\\bigl[V\\ |\\ Z\\bigr]\\quad\\forall\\lambda,$$
其中 $V$ 张成 $\\ker[C;CA]$、$Z$ 张成 $\\ker[C;\\mathcal L]$。实现用极大子式的 gcd（`spectral_gcd_Z`），
非平凡 gcd ⟺ 有公共复根 ⟺ 失败。

本脚本在若干 $(5a)$-可行样本上，把该判据与 [Toeplitz 判据](toeplitz_criterion.py) 的结论逐点比较。

用法：python -u tools/verification/nullspace_vs_toeplitz.py
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import spectral_gcd as SG                 # noqa: E402
import z_generator as ZG                  # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
from fractions import Fraction            # noqa: E402

F = Fraction


def main():
    agree = disagree = 0
    checked = 0
    for n in (5, 6):
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
                    cands = ZG.sample_L_at_order(A, C, L0, q0, 3, seed * 13 + q0)
                    for L in cands:
                        checked += 1
                        toe = TC.analyse(A, C, L)['five_b']
                        Zc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L])
                        if not Zc or not Zc[0]:
                            continue
                        g, h, nmin = SG.spectral_gcd_Z(A, C, Zc)
                        deg = SG.pdeg(g)
                        null_ok = (deg == 0)               # gcd 为常数 ⟹ 无有限公共根 ⟹ (5b) 成立
                        if null_ok == toe:
                            agree += 1
                        else:
                            disagree += 1
                            print(f'  **不一致**: n={n} p={p} r={r} seed={seed} toeplitz={toe} '
                                  f'nullspace={null_ok} (gcd 次数={deg}, h={h}, 子式={nmin})')
    print(f'\n检查 {checked} 个铅笔：一致 {agree}，不一致 {disagree}')
    assert disagree == 0, '两个判据在样本上不一致'


if __name__ == '__main__':
    main()
