"""spectral_regime.py —— 只在"整数障碍不适用"的阶上做谱判定

上一轮得到：$h=s_0+\\dim\\pi(V)$（$s_0=\\dim(\\operatorname{row}[C;L_0]+W)$），故
$$\\dim\\pi(V)\\le\\min(t,\\,n-s_0),\\qquad t=q-r,$$
于是 **Type I 不可能**当且仅当
$$s_0+\\min(t,\\,n-s_0)<q+r_1 .$$
本脚本筛出这类"谱区"的 $(\\text{实例},q)$ 对，在 $q_0$ 阶抽样判 $(5b)$，并区分：

* 成功（$q_{\\min}=q_0$）；
* Type III 失败（$h<q+r_1$ 但 $d_{\\rm fin}>0$）。

用法：python -u tools/verification/spectral_regime.py
"""

import os
import sys
from collections import Counter
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

F = Fraction


def rowspace(rows):
    out = []
    for r in rows:
        if LQ.rank(out + [r]) > len(out):
            out.append(list(r))
    return out


def main():
    import random
    stats = Counter()
    rows = []
    for n in (5, 6, 7):
        for p in (1, 2):
            for r in (1, 2):
                if p + r > n:
                    continue
                for seed in range(3000, 3010):
                    made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
                    if made is None:
                        continue
                    A, C, L0 = made
                    O = QR.observability_matrix(A, C)
                    if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
                        continue
                    CA = LQ.mul(C, A)
                    W = [x[:] for x in C] + [x[:] for x in CA]
                    r1 = LQ.rank(W)
                    s0 = len(rowspace([x[:] for x in C] + [x[:] for x in L0]
                                      + [x[:] for x in W]))
                    q0 = Q0.eta_and_q0(A, C, L0)[0]
                    q = q0
                    t = q - r
                    if t < 0:
                        continue
                    h_max = s0 + min(t, n - s0)
                    typeI_possible = (h_max >= q + r1)
                    stats['inst'] += 1
                    if typeI_possible:
                        stats['typeI_possible'] += 1
                        continue                       # 整数区内，无需谱判定
                    stats['spectral_regime'] += 1
                    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
                    mm = len(K[0])
                    d = n - p - q
                    if d <= 0:
                        continue
                    rng = random.Random(seed * 11 + q)
                    adm = succ = fail = 0
                    for _ in range(60):
                        Wm = [[F(rng.randrange(-3, 4)) for _ in range(d)] for _ in range(mm)]
                        Z = [[sum(K[i][tt] * Wm[tt][j] for tt in range(mm)) for j in range(d)]
                             for i in range(n)]
                        if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                            continue
                        L = ZG.L_from_Z(A, C, L0, Z, q)
                        if L is None or not LQ.condA(A, C, L):
                            continue
                        adm += 1
                        h, s, m, d_fin = T3.fast_dfin(A, C, L)
                        if d_fin == 0:
                            succ += 1
                        elif h < q + r1:
                            fail += 1
                    stats['adm'] += adm
                    stats['succ'] += succ
                    stats['typeIII'] += fail
                    rows.append((n, p, r, seed, q0, s0, r1, t, h_max, adm, succ, fail))
                    print(f'n={n} p={p} r={r} seed={seed} q0={q0}: s0={s0} r1={r1} t={t} '
                          f'h_max={h_max} q+r1={q + r1}｜样本 {adm}，成功 {succ}，TypeIII {fail}')
    print(f"\n实例 {stats['inst']}：整数区 {stats['typeI_possible']}，谱区 {stats['spectral_regime']}")
    print(f"谱区样本 {stats['adm']}：成功 {stats['succ']}，Type III {stats['typeIII']}")


if __name__ == '__main__':
    main()
