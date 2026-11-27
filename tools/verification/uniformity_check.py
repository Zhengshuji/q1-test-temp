"""uniformity_check.py —— 验证**无条件**不等式 $h\\le s_0+q-r$（替换原来条件性的"整族一致"）

推导（纸面）：$\mathcal Z^\perp=\operatorname{row}C\oplus R$（$R=\operatorname{row}\mathcal L$），
$S=\operatorname{row}[C;L_0]+W$。因 $\operatorname{row}L_0\subseteq R\subseteq\mathcal Z^\perp$，故
$$\mathcal Z^\perp+S=\mathcal Z^\perp+W\quad\Longrightarrow\quad h=\dim(\mathcal Z^\perp+S)=(p+q)+s_0-\dim(\mathcal Z^\perp\cap S).$$
又 $\operatorname{row}C\oplus\operatorname{row}L_0\subseteq\mathcal Z^\perp\cap S$（三者都在 $S$ 里、且和为直和），
故 $\dim(\mathcal Z^\perp\cap S)\ge p+r$，于是
$$\boxed{h\le s_0+q-r},$$
等号 $\iff\mathcal Z^\perp\cap S=\operatorname{row}C\oplus\operatorname{row}L_0$。

**推论**：若 $s_0<r_1+r$，则 $h<s_0+q-r<q+r_1$，即**任何** $\mathcal L$ 都**不是** Type I——
计数障碍在该阶不可能触发（与 $\mathcal L$ 无关）。

本脚本在实例上核验：不等式、等号判据、以及"$s_0<r_1+r$ ⟹ 无 Type I"。

用法：python -u tools/verification/uniformity_check.py
"""

import os
import sys
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import toeplitz_criterion as TC           # noqa: E402


def main():
    stat = Counter()
    for n in (5, 6, 7):
        for p in (1, 2):
            for r in (1, 2):
                if p + r > n:
                    continue
                for seed in range(3000, 3005):
                    made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
                    if made is None:
                        continue
                    A, C, L0 = made
                    O = QR.observability_matrix(A, C)
                    if LQ.rank(O + [list(x) for x in L0]) != LQ.rank(O):
                        continue
                    q0 = Q0.eta_and_q0(A, C, L0)[0]
                    CA = LQ.mul(C, A)
                    W = [list(x) for x in C] + [list(x) for x in CA]
                    r1 = LQ.rank(W)
                    S = [list(x) for x in C] + [list(x) for x in L0] + [list(x) for x in CA]
                    s0 = LQ.rank(S)
                    for L in ZG.sample_L_at_order(A, C, L0, q0, 8, seed * 13 + q0):
                        if not LQ.condA(A, C, L):
                            continue
                        res = TC.analyse(A, C, L)
                        h = res['h']
                        q = len(L)
                        stat['samples'] += 1
                        # (1) 不等式
                        if h <= s0 + q - r:
                            stat['ineq_ok'] += 1
                        else:
                            stat['ineq_fail'] += 1
                        # (2) 等号判据：dim(Z^perp ∩ S) == p + r
                        R = [list(x) for x in L]
                        Zp = [list(x) for x in C] + R            # Z^perp = C ⊕ R
                        dZS = LQ.rank(Zp) + s0 - LQ.rank(Zp + S)   # dim(Z^perp ∩ S)
                        eq = (h == s0 + q - r)
                        if eq == (dZS == p + r):
                            stat['eq_ok'] += 1
                        else:
                            stat['eq_fail'] += 1
                        # (3) s0 < r1+r ⟹ 不可能 Type I
                        if s0 < r1 + r:
                            stat['s0_lt'] += 1
                            if h >= q + r1:
                                stat['s0_lt_but_typeI'] += 1
                        else:
                            stat['s0_ge'] += 1
                            if h >= q + r1:
                                stat['typeI'] += 1
    print('统计：', dict(stat))
    print('\n解读：')
    print('  ineq_ok/ineq_fail —— 不等式 h ≤ s0+q-r 的成立/失败次数')
    print('  eq_ok/eq_fail     —— 等号判据 ⟺ dim(Z^⊥∩S)=p+r 的成立/失败次数')
    print('  s0_lt_but_typeI   —— "s0<r1+r 却仍有 Type I"的次数（应为 0）')


if __name__ == '__main__':
    main()
