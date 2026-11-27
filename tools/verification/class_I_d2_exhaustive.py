"""class_I_d2_exhaustive.py —— $d=2$ 的**穷举式**检查：把可容许候选扫干净，看有没有可行的

思路：$d\\ge2$ 的可容许候选很稀有（上一轮 5/266）。所以先筛出"有可容许候选"的实例，
再在这些实例上把图卡 × $\\theta\\in\\{-2,\\dots,2\\}$ 全扫一遍，对**每个**可容许 $\\mathcal L$ 检查 $(5b)$。

若出现"可容许且 $(5b)$ 成立" ⟹ $q_{\\min}<n-1$（本类结论被推翻）；
若全失败 ⟹ 支持 $q_{\\min}=n-1$。

用法：python -u tools/verification/class_I_d2_exhaustive.py
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
import decide_symbolic as DS              # noqa: E402
import observability_test as OT           # noqa: E402

F = Fraction


def main():
    rng = random.Random(20261115)
    st = Counter()
    hits = []
    for trial in range(4000):
        n = rng.choice([5, 6])
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
        for q in range(q0, n0):            # d = n-1-q ≥ 2
            d = n - 1 - q
            if d < 2 or d > k:
                continue
            adm = 0
            feas = 0
            for rows in itertools.combinations(range(k), d):
                nv = d * (k - d)
                ths = [[F(b)] * nv for b in range(-2, 3)]
                for _ in range(4):
                    ths.append([F(rng.randrange(-3, 4)) for _ in range(nv)])
                for th in ths:
                    Z = DS.Z_from_theta(A, C, L0, q, rows, th)
                    if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                        continue
                    try:
                        L = ZG.L_from_Z(A, C, L0, Z, q)
                    except AssertionError:
                        continue
                    if L is None or not LQ.condA(A, C, L):
                        continue
                    adm += 1
                    ok, why = OT.observability_ok(A, C, L)
                    if ok:
                        feas += 1
                        if len(hits) < 5:
                            hits.append((n, q, d, A, C, L0, L))
            st[f'd={d}:实例'] += 1
            st[f'd={d}:可容许候选总数'] += adm
            st[f'd={d}:可行候选'] += feas
            if adm > 0:
                st[f'd={d}:有可容许的实例'] += 1
    print('统计：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')
    print()
    if hits:
        print('★ 找到可行候选（q_min < n-1 的反例）=', [(h[0], h[1], h[2]) for h in hits])
    else:
        print('未找到 d≥2 的可行候选')


if __name__ == '__main__':
    main()
