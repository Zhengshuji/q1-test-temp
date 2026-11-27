"""certificate_delta1.py —— 中间层（$\\delta=1$）**可行**的显式证书

结论形式：存在 $(p,r)=(2,2)$、$r_1=4$、阶 $q$、可容许 $\\mathcal L$，使
* $(5a)$ 成立；
* $\\delta(\\mathcal V)=1$（**中间层**，$1\\le\\delta<r_1-p=2$）；
* $(5b)$ **成立**（即该候选**可行**）。

这证明中间层**不是**整层不可行（与两个边界层 $\\delta=0$、$\\delta=r_1-p$ 的"绝不可行"形成对比）。

脚本：搜索一个实例并把完整数据打印成可粘贴的证书；同时逐条断言核验。

用法：python -u tools/verification/certificate_delta1.py
"""

import os
import sys
import itertools
import random
from fractions import Fraction

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


def find(rng):
    for trial in range(3000):
        n = 6
        p = r = 2
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
        if r1 != 4:
            continue
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (K and K[0]):
            continue
        k = len(K[0])
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        for q in range(q0, n0 - p + 1):
            d = n - p - q
            if d <= 0 or d > k:
                continue
            for rows in itertools.combinations(range(k), d):
                Z = DS.Z_from_theta(A, C, L0, q, rows, [F(0)] * (d * (k - d)))
                if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                    continue
                try:
                    L = ZG.L_from_Z(A, C, L0, Z, q)
                except AssertionError:
                    continue
                if L is None or not LQ.condA(A, C, L):
                    continue
                Vl = LQ.rank([list(x) for x in L] + [list(x) for x in C])
                inter = LQ.rank([list(x) for x in L] + [list(x) for x in C] +
                                [list(x) for x in CA])
                delta = (Vl + LQ.rank([list(x) for x in CA])) - inter
                if not (1 <= delta < r1 - p):
                    continue
                ok, why = OT.observability_ok(A, C, L)
                if ok:
                    return dict(n=n, p=p, r=r, q=q, q0=q0, r1=r1, delta=delta,
                                A=A, C=C, L0=L0, Z=Z, L=L, why=why)
    return None


def main():
    rng = random.Random(20261125)
    w = find(rng)
    if w is None:
        print('未找到'); return
    A, C, L0, Z, L = w['A'], w['C'], w['L0'], w['Z'], w['L']
    n, p, r, q = w['n'], w['p'], w['r'], w['q']
    CA = LQ.mul(C, A)
    print(f"实例：n={n}, p={p}, r={r}, q={q}, q0={w['q0']}, r1={w['r1']}, delta={w['delta']}")
    print()
    print('断言核验：')
    print('  (5a) 成立        :', LQ.condA(A, C, L))
    print('  rank[C;L] = p+q  :', LQ.rank([list(x) for x in C] + L), '=', p + q)
    print('  row L0 ⊆ row L   :',
          LQ.rank([list(x) for x in L] + [list(x) for x in L0]) == LQ.rank(L))
    Vl = LQ.rank([list(x) for x in L] + [list(x) for x in C])
    inter = LQ.rank([list(x) for x in L] + [list(x) for x in C] + [list(x) for x in CA])
    delta = (Vl + LQ.rank([list(x) for x in CA])) - inter
    print(f'  delta = {delta}（中间层：1 ≤ δ < r1-p = {w["r1"]-p}）:', 1 <= delta < w['r1'] - p)
    ok, why = OT.observability_ok(A, C, L)
    print('  (5b) 成立        :', ok, '（', why, '）')
    print()
    print('A =', [[str(x) for x in row] for row in A])
    print('C =', [[str(x) for x in row] for row in C])
    print('L0 =', [[str(x) for x in row] for row in L0])
    print('L =', [[str(x) for x in row] for row in L])
    print('Z =', [[str(x) for x in row] for row in Z])


if __name__ == '__main__':
    main()
