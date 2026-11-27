"""verify_b32_33.py —— 核验 B.32（$r_1\\le p+1$ ⟹ $q_{\\min}=n-p$）与 B.33（铅笔尺寸 $(p+q)\\times(q+\\delta-\\rho)$）

用法：python -u tools/verification/verify_b32_33.py
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
    rng = random.Random(20261126)
    st = Counter()
    for trial in range(1200):
        n = rng.choice([6, 7])
        p = rng.choice([1, 2, 3])
        r = rng.choice([1, 2])
        if p + r >= n:
            continue
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(p)]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(r)]
        if LQ.rank(C) != p or LQ.rank(L0) != r:
            continue
        if LQ.rank([list(x) for x in C] + L0) != p + r:
            continue
        O = QR.observability_matrix(A, C)
        n0 = LQ.rank(O)
        if n0 != n or LQ.rank(O + [list(x) for x in L0]) != n:
            continue
        CA = LQ.mul(C, A)
        r1 = LQ.rank([list(x) for x in CA] + [list(x) for x in C])
        rho = r1 - p
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (K and K[0]):
            continue
        k = len(K[0])
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        qmin = None
        for q in range(q0, n0 - p + 1):
            d = n - p - q
            if d < 0 or d > k:
                continue
            found = False
            if d == 0:
                cands = [None]
            else:
                cands = [DS.Z_from_theta(A, C, L0, q, rows, [F(0)] * (d * (k - d)))
                         for rows in itertools.combinations(range(k), d)]
            for Z in cands:
                if Z is not None and ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                    continue
                try:
                    L = ZG.L_from_Z(A, C, L0, Z if Z is not None else [[] for _ in range(n)], q)
                except AssertionError:
                    continue
                if L is None or not LQ.condA(A, C, L):
                    continue
                Vchk = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
                if not (Vchk and Vchk[0]):
                    ok = True
                else:
                    ok, _w = OT.observability_ok(A, C, L)
                # B.33 核验
                h = LQ.rank([list(x) for x in L] + [list(x) for x in CA] + [list(x) for x in C])
                Vl = LQ.rank([list(x) for x in L] + [list(x) for x in C])
                inter = LQ.rank([list(x) for x in L] + [list(x) for x in C] + [list(x) for x in CA])
                delta = (Vl + LQ.rank([list(x) for x in CA])) - inter
                s = n - h
                if h - r1 == q + delta - rho:
                    st['B.33 成立'] += 1
                else:
                    st['B.33 不成立'] += 1
                if ok:
                    found = True
                    break
            if found:
                qmin = q
                break
        if rho <= 1:
            st['rho≤1 实例'] += 1
            if qmin == n - p:
                st['rho≤1 且 qmin=n-p'] += 1
            elif qmin is None:
                st['rho≤1 但未找到可行'] += 1
            else:
                st[f'rho≤1 但 qmin={qmin}≠n-p'] += 1
        else:
            st['rho≥2 实例'] += 1
            if qmin is not None and qmin < n - p:
                st['rho≥2 且 qmin<n-p'] += 1
    print('统计：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')


if __name__ == '__main__':
    main()
