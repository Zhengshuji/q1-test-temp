"""delta_general.py —— 中间层是否**总是**可行？跨 $(p,r,r_1)$ 的 $\delta$ 分层扫描

**问题**：B.30 的"中间层可行"目前只有 $(2,2),r_1=4,\\delta=1$ 的 2248/2248 证据。
本项目早期（attempts/77–78）在 $s$-分层（$s=\\dim(V\\cap\\mathcal Z)$）下曾找到**中间层失败**的例子，
而 $s+\\delta=n-q-p$（由 $s=n-h$ 与 $h=q+p+\\delta$），故两种分层是**同一分层**的不同坐标。
本脚本跨参数扫描，看中间层（$1\\le\\delta<r_1-p$）里有没有**失败**的候选。

用法：python -u tools/verification/delta_general.py
"""

import os
import sys
import itertools
import random
from fractions import Fraction
from collections import Counter, defaultdict

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
    rng = random.Random(20261124)
    per = defaultdict(lambda: [0, 0])
    for trial in range(1500):
        n = rng.choice([6, 7])
        p = rng.choice([2, 3])
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
                Vchk = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
                if not (Vchk and Vchk[0]):
                    ok = True          # V=0 ⟹ 无失败见证
                else:
                    ok, _w = OT.observability_ok(A, C, L)
                tag = ('δ=r1-p' if delta == r1 - p else ('中间层' if 1 <= delta < r1 - p else 'δ=0'))
                per[(p, r, r1, tag)][0] += 1
                if ok:
                    per[(p, r, r1, tag)][1] += 1
                break
    print(f'{"p":>2} {"r":>2} {"r1":>3} {"层":>8} {"样本":>6} {"可行":>5}')
    for key in sorted(per):
        p_, r_, r1_, tag = key
        s_, f_ = per[key]
        print(f'{p_:>2} {r_:>2} {r1_:>3} {tag:>8} {s_:>6} {f_:>5}')


if __name__ == '__main__':
    main()
