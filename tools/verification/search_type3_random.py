"""search_type3_random.py —— 在更大的随机实例里搜索 $q_0$ 阶的 Type III

目的：检验"一般实例在谱区（整数障碍不适用）里 $(5b)$ 总成立"的说法是否在更大规模上仍成立。

对每个实例：

1. 算 $s_0=\\dim(\\operatorname{row}[C;L_0]+W)$、$r_1$、$q_0$、$t=q_0-r$、$h_{\\max}=s_0+\\min(t,n-s_0)$；
2. 若 $h_{\\max}\\ge q_0+r_1$（整数区）跳过；
3. 谱区：在 $q_0$ 阶抽 40 个 $Z$-参数化候选，筛 $(5a)$，判 $(5b)$；
4. 报告任何"有候选但全失败"（Type III）的实例。

用法：python -u tools/verification/search_type3_random.py
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
    for r0 in rows:
        if LQ.rank(out + [r0]) > len(out):
            out.append(list(r0))
    return out


def main():
    import random
    stats = Counter()
    for n in (7, 8, 9):
        for p in (2, 3):
            for r in (1, 2, 3):
                if p + r > n - 1:
                    continue
                for seed in range(4000, 4006):
                    made = QR.make_instance(n, p, r, seed * 23 + p * 11 + r)
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
                    t = q0 - r
                    if t < 0:
                        continue
                    h_max = s0 + min(t, n - s0)
                    stats['inst'] += 1
                    if h_max >= q0 + r1:
                        stats['integer_zone'] += 1
                        continue
                    stats['spectral_zone'] += 1
                    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
                    mm = len(K[0])
                    d = n - p - q0
                    if d <= 0:
                        stats['d0'] += 1
                        continue
                    rng = random.Random(seed * 31 + q0)
                    adm = succ = 0
                    for _ in range(40):
                        Wm = [[F(rng.randrange(-3, 4)) for _ in range(d)] for _ in range(mm)]
                        Z = [[sum(K[i][tt] * Wm[tt][j] for tt in range(mm)) for j in range(d)]
                             for i in range(n)]
                        if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                            continue
                        L = ZG.L_from_Z(A, C, L0, Z, q0)
                        if L is None or not LQ.condA(A, C, L):
                            continue
                        adm += 1
                        h, s, m, d_fin = T3.fast_dfin(A, C, L)
                        if d_fin == 0:
                            succ += 1
                    stats['adm'] += adm
                    if adm and succ == 0:
                        stats['typeIII'] += 1
                        print(f'  ** Type III：n={n} p={p} r={r} seed={seed} q0={q0} '
                              f'r1={r1} p+r={p + r} s0={s0} t={t} 样本={adm}')
                    elif succ:
                        stats['feasible'] += 1
    print('\n统计：', dict(stats))


if __name__ == '__main__':
    main()
