"""equality_case.py —— 检验专家指出的边界情形 $h=q+r_1$（B.11d 的缺口）

**问题**：$h>q+r_1$ 时 $(5b)$ 不可能（Rank $Q\\le q+r_1<h$）；但 $h=q+r_1$ 时 $(5b)$
只要求 $Q_{\\mathcal L}(\\lambda)$ 对一切有限 $\\lambda$ 满行秩——**原则上可能**。
故"Type I（$h\\ge q+r_1$）杀掉 $(5b)$"在等号处需要单独论证。

本脚本：在随机实例的可容许增广中，找 $h=q+r_1$ 的样本，逐一检验 $(5b)$（B.12 判据）。
若存在 $h=q+r_1$ 且 $(5b)$ 成立 ⟹ 专家的担心成立，B.11d 必须按"严格不等式"改写。

用法：python -u tools/verification/equality_case.py
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
import observability_test as OT           # noqa: E402
import decide_symbolic as DS              # noqa: E402

F = Fraction


def main():
    rng = random.Random(20261105)
    st = Counter()
    examples = []
    for trial in range(4000):
        n = rng.choice([5, 6, 7])
        p = rng.choice([1, 2])
        r = rng.choice([1, 2])
        if p + r >= n:
            continue
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(p)]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(r)]
        if LQ.rank(C) != p or LQ.rank(L0) != r:
            continue
        O = QR.observability_matrix(A, C)
        n0 = LQ.rank(O)
        if n0 != n:
            continue
        if LQ.rank(O + [list(x) for x in L0]) != n:
            continue
        CA = LQ.mul(C, A)
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
                        st['构造失败（跳过）'] += 1
                        continue
                    if L is None or not LQ.condA(A, C, L):
                        continue
                    h = LQ.rank([list(x) for x in L] + [list(x) for x in CA] + [list(x) for x in C])
                    r1 = LQ.rank([list(x) for x in CA] + [list(x) for x in C])
                    if h == q + r1:
                        st['h=q+r1 样本'] += 1
                        ok, why = OT.observability_ok(A, C, L)
                        if ok:
                            st['h=q+r1 且 (5b) 成立'] += 1
                            if len(examples) < 3:
                                examples.append((n, p, r, q, h, r1, why))
                        else:
                            st['h=q+r1 且 (5b) 失败'] += 1
                    elif h > q + r1:
                        st['h>q+r1 样本'] += 1
                    else:
                        st['h<q+r1 样本'] += 1
    print('统计：', dict(st))
    for e in examples:
        print('  ★ h=q+r1 且可行：n,p,r,q,h,r1 =', e[:6])
    print('\n结论：若 "h=q+r1 且 (5b) 成立" 为 0，则等号处在本样本里总是失败；'
          '但这不是证明（专家要求的是定理）。')


if __name__ == '__main__':
    main()
