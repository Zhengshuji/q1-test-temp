"""delta_scan_22.py —— $(p,r)=(2,2)$ 上按 $\\delta$ 分层的可行性扫描

**背景（B.28b）**：$\\delta(\\mathcal V)=\\dim(\\operatorname{row}(CA)/(\\operatorname{row}(CA)\\cap\\mathcal V))$，$h=q+p+\\delta$；
$\\delta=r_1-p$ 是等号（B.22 杀掉）、$\\delta=0$ 由不变子空间排除，**中间层** $1\\le\\delta<r_1-p$ 未定。
$(2,2)$ 且 $r_1=4$ 时 $\\delta\\in\\{0,1,2\\}$，$\\delta=1$ 是**第一个真正的中间层**。

本脚本：随机 $(2,2)$ 实例（$n=6,7$），对每个阶、每个可容许候选算 $\\delta$ 与 $(5b)$，按 $(\\delta,r_1)$ 分层统计。

用法：python -u tools/verification/delta_scan_22.py
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
    rng = random.Random(20261122)
    per = defaultdict(lambda: [0, 0])   # (r1, delta) -> [samples, feasible]
    for trial in range(900):
        n = rng.choice([6, 7])
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
                for b in (0, 1):
                    Z = DS.Z_from_theta(A, C, L0, q, rows, [F(b)] * (d * (k - d)))
                    if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                        continue
                    try:
                        L = ZG.L_from_Z(A, C, L0, Z, q)
                    except AssertionError:
                        continue
                    if L is None or not LQ.condA(A, C, L):
                        continue
                    # 可容许：算 delta
                    Vl = LQ.rank([list(x) for x in L] + [list(x) for x in C])   # dim V
                    inter = LQ.rank([list(x) for x in L] + [list(x) for x in C] +
                                    [list(x) for x in CA])                     # dim(V + row(CA))
                    delta = (Vl + LQ.rank([list(x) for x in CA])) - inter
                    ok, _w = OT.observability_ok(A, C, L)
                    per[(r1, delta)][0] += 1
                    if ok:
                        per[(r1, delta)][1] += 1
                    break
    print(f'{"r1":>3} {"δ":>2} {"样本":>6} {"可行":>4}')
    for key in sorted(per):
        r1, delta = key
        s_, f_ = per[key]
        print(f'{r1:>3} {delta:>2} {s_:>6} {f_:>4}')


if __name__ == '__main__':
    main()
