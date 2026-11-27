"""class_I_low_orders.py —— Class I 的低阶（$d\\ge2$）到底有没有**可容许**增广？

对 $p=r=1$ 的可观测实例，在每一阶 $q$（$d=n-1-q\\ge2$）上扫图卡，只统计 $(5a)$ 是否成立
（谱条件另论）。问题：$(5a)$ 本身在低阶是否可满足？

若所有 $d\\ge2$ 的阶都**没有**可容许候选，则 $q_{\\min}=n-1$ 由 $(5a)$ 单独给出（配合 $d=1$ 的 B.18e）。

用法：python -u tools/verification/class_I_low_orders.py
"""

import os
import sys
import itertools
import random
from fractions import Fraction
from collections import Counter

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import decide_symbolic as DS
import observability_test as OT              # noqa: E402

F = Fraction


def main():
    rng = random.Random(20261114)
    st = Counter()
    for trial in range(400):
        n = rng.choice([4, 5, 6])
        p = r = 1
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        if LQ.rank(C) != 1 or LQ.rank(L0) != 1:
            continue
        if LQ.rank([list(x) for x in C] + L0) != 2:
            continue
        O = QR.observability_matrix(A, C)
        n0 = LQ.rank(O)
        if n0 != n or LQ.rank(O + [list(x) for x in L0]) != n:
            continue
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (K and K[0]):
            continue
        k = len(K[0])
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        for q in range(q0, n0):           # q ≤ n-1；d = n-1-q
            d = n - 1 - q
            if d < 2 or d > k:
                continue
            st[f'阶 d={d}:实例'] += 1
            found = False
            for rows in itertools.combinations(range(k), d):
                for b in range(0, 3):
                    Z = DS.Z_from_theta(A, C, L0, q, rows, [F(b)] * (d * (k - d)))
                    if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                        continue
                    try:
                        L = ZG.L_from_Z(A, C, L0, Z, q)
                    except AssertionError:
                        continue
                    if L is None:
                        continue
                    if LQ.condA(A, C, L):
                        st[f'阶 d={d}:有可容许'] += 1
                        ok, why = OT.observability_ok(A, C, L)
                        st[f'阶 d={d}:可容许且 (5b) 成立' if ok else f'阶 d={d}:可容许但 (5b) 失败'] += 1
                        found = True
                        break
                if found:
                    break
    print('统计：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')


if __name__ == '__main__':
    main()
