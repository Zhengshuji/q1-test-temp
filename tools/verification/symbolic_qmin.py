"""symbolic_qmin.py —— 用**符号判定**重算 $q_0$ 阶（把网格统计升级为证书）

对每个实例，只在小图卡（参数 $d(k-d)\\le2$）上做符号判定（[decide_symbolic.py](decide_symbolic.py)）：

* `FEASIBLE` ⟹ $q_{\\min}=q_0$（带见证 + 七条一致性检查）；
* `INFEASIBLE` ⟹ $q_{\\min}>q_0$（gcd 证书）；
* `UNKNOWN` ⟹ 记录未决（并注明原因）。

与网格版（`q0_scan_gz.py` 等）对照，统计"网格说没有/符号说有"这类差异。

用法：python -u tools/verification/symbolic_qmin.py [--max N] [--param-cap 2]
"""

import os
import sys
import time
import itertools

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import toeplitz_criterion as TC           # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import decide_symbolic as DS              # noqa: E402

from collections import Counter


def grid_verdict(A, C, L0, q, samples=40):
    """网格版：返回 ('yes'/'no'/'none', 命中数)。"""
    import random
    from fractions import Fraction as F
    n, p, r = len(A), len(C), len(L0)
    d = n - p - q
    if d <= 0:
        return 'degenerate', 0
    K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    mm = len(K[0])
    rng = random.Random(q * 7919 + 13)
    hits = adm = 0
    for _ in range(samples):
        Wm = [[F(rng.randrange(-3, 4)) for _ in range(d)] for _ in range(mm)]
        Z = [[sum(K[i][t] * Wm[t][j] for t in range(mm)) for j in range(d)] for i in range(n)]
        if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
            continue
        L = ZG.L_from_Z(A, C, L0, Z, q)
        if L is None or not LQ.condA(A, C, L):
            continue
        adm += 1
        if TC.analyse(A, C, L)['five_b']:
            hits += 1
    if hits:
        return 'yes', hits
    return ('no' if adm else 'none'), adm


def main():
    cap = 2
    maxn = 12
    args = sys.argv[1:]
    if '--param-cap' in args:
        cap = int(args[args.index('--param-cap') + 1])
    if '--max' in args:
        maxn = int(args[args.index('--max') + 1])
    stats = Counter()
    rows = []
    t0 = time.time()
    done = 0
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
                    q0 = Q0.eta_and_q0(A, C, L0)[0]
                    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
                    k = len(Kc[0])
                    d = n - p - q0
                    if d <= 0 or d >= k or d * (k - d) > cap:
                        continue
                    tt = time.time()
                    v, why, w = DS.decide(A, C, L0, q0, verbose=False)
                    el = time.time() - tt
                    g, hits = grid_verdict(A, C, L0, q0)
                    stats['inst'] += 1
                    stats[v] += 1
                    consistent = ((v == 'FEASIBLE' and g == 'yes') or
                                  (v == 'INFEASIBLE' and g in ('no', 'none')) or
                                  (v == 'UNKNOWN'))
                    if not consistent:
                        stats['mismatch'] += 1
                    rows.append((n, p, r, seed, q0, d, k, v, g, hits, round(el, 1)))
                    print(f'n={n} p={p} r={r} seed={seed} q0={q0} d={d} k={k}: 符号={v}'
                          f'（{el:.1f}s）；网格={g}(命中{hits})'
                          + ('' if consistent else '  ← **不一致**'))
                    done += 1
                    if done >= maxn:
                        print(f'\n统计：{dict(stats)}；总耗时 {time.time() - t0:.0f}s')
                        return
    print(f'\n统计：{dict(stats)}；总耗时 {time.time() - t0:.0f}s')


if __name__ == '__main__':
    main()
