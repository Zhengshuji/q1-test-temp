"""coordinate_restriction.py —— 专家 §3.2 第 2 项：$\\mathcal L$ 只允许**坐标行**时的组合结构

限制：$\\mathcal L=[L_0;\\{e_i^{\\mathsf T}\\}_{i\\in S}]$，$|S|=q-r$，于是
$$\\mathcal Z=\\ker[C;\\mathcal L]=K\\cap\\{x_i=0,\\ i\\in S\\},\\qquad K=\\ker[C;L_0],$$
固定阶判定退化为**子集选择**：是否存在 $S$（$|S|=q-r$）使 $(5a)$ 与 $(5b)$ 成立。

本脚本：

1. 对每个实例、每个阶 $q$，枚举全部 $S$，记录"好子集"族 $\\mathcal G_q$；
2. 检验**跨阶单调性**：$S\\in\\mathcal G_q$ 且 $i\\notin S$ 时，$S\\cup\\{i\\}\\in\\mathcal G_{q+1}$ 是否总成立？
   （若成立，说明"加一行"是单调的，问题可能是拟阵型；若常有反例，说明存在真正的组合核心。）

用法：python -u tools/verification/coordinate_restriction.py
"""

import os
import sys
import itertools
from collections import Counter, defaultdict
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402

F = Fraction


def good_sets(A, C, L0, n, p, r, q):
    m = q - r
    adm, good = [], []
    if m < 0:
        return adm, good
    for S in itertools.combinations(range(n), m):
        L = [list(x) for x in L0]
        for i in S:
            row = [F(0)] * n
            row[i] = F(1)
            L.append(row)
        if len(L) != q:
            continue
        if LQ.rank([list(x) for x in C] + L) != p + q:
            continue
        if not LQ.condA(A, C, L):
            continue
        adm.append(S)
        if TC.analyse(A, C, L)['five_b']:
            good.append(S)
    return adm, good


def main():
    stats = Counter()
    for n in (5, 6):
        for p in (1, 2):
            for r in (1, 2):
                if p + r > n:
                    continue
                for seed in range(3000, 3008):
                    made = QR.make_instance(n, p, r, seed * 17 + p * 7 + r)
                    if made is None:
                        continue
                    A, C, L0 = made
                    O = QR.observability_matrix(A, C)
                    if LQ.rank(O + [x[:] for x in L0]) != LQ.rank(O):
                        continue
                    q0 = Q0.eta_and_q0(A, C, L0)[0]
                    n0 = LQ.rank(O)
                    fam = defaultdict(list)
                    for q in range(q0, min(n0 - p, n - p) + 1):
                        adm, good = good_sets(A, C, L0, n, p, r, q)
                        fam[q] = good
                        if good:
                            stats['cases_with_good'] += 1
                        stats['cases'] += 1
                    # 跨阶单调性
                    for q in list(fam):
                        if q + 1 not in fam:
                            continue
                        for S in fam[q]:
                            for i in range(n):
                                if i in S:
                                    continue
                                T = tuple(sorted(set(S) | {i}))
                                if len(T) != (q + 1) - r:
                                    continue
                                stats['ext_tests'] += 1
                                if T in fam[q + 1]:
                                    stats['ext_ok'] += 1
                                else:
                                    stats['ext_fail'] += 1
                                    if stats['ext_fail'] <= 6:
                                        print(f'  反例：n={n} p={p} r={r} seed={seed}：'
                                              f'S={S} 在 q={q} 好，但 S∪{{{i}}}={T} 在 q={q + 1} 不好')
                    line = '  '.join(f'q={q}:{len(fam[q])}好/…' for q in sorted(fam))
                    if any(fam.values()):
                        print(f'n={n} p={p} r={r} seed={seed}：{line}')
    print('\n统计：', dict(stats))


if __name__ == '__main__':
    main()
