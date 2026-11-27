"""equality_search.py —— 为"等号情形必失败"寻找**反例**（专家 §Direction A 第 5 步）

问题：$h=q+r_1$ 时 $(5b)$ 是否**总**失败？（我们的 22877 个样本都在等号处失败，但那些样本的 $d\\ge1$。）
本轮扩大搜索面：
* 阶的范围扩到**全体** $q_0\\le q\\le n_0-p$（含 $d=0$ 的终阶）；
* $(p,r)$ 取 $(1,1),(1,2),(2,1),(2,2)$；
* 图卡在 $\\binom{k}{d}$ 上扫，$\\theta$ 取若干值；
记录每个可容许 $(\\mathcal L,q)$ 的 $(h-(q+r_1),\\ (5b))$，专门找 **等号 $\\wedge$ $(5b)$ 成立** 的样本。

用法：python -u tools/verification/equality_search.py
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
    witnesses = []
    for trial in range(1200):
        n = rng.choice([4, 5, 6])
        p = rng.choice([1, 2])
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
        if n0 != n:
            continue
        if LQ.rank(O + [list(x) for x in L0]) != n:
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
            if d < 0 or d > k:
                continue
            if d == 0:
                cands = [([[] for _ in range(n)], None)]
            else:
                cands = []
                for rows in itertools.combinations(range(k), d):
                    for b in range(0, 2):
                        cands.append((DS.Z_from_theta(A, C, L0, q, rows,
                                                      [F(b)] * (d * (k - d))), rows))
            for Z, _ in cands:
                if d > 0 and ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                    continue
                try:
                    L = ZG.L_from_Z(A, C, L0, Z, q)
                except AssertionError:
                    st['构造失败'] += 1
                    continue
                if L is None or not LQ.condA(A, C, L):
                    continue
                h = LQ.rank([list(x) for x in L] + [list(x) for x in CA] + [list(x) for x in C])
                gap = h - (q + r1)
                key = 'h<q+r1' if gap < 0 else ('h=q+r1' if gap == 0 else 'h>q+r1')
                st[key + ' 样本'] += 1
                Vchk = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
                if not (Vchk and Vchk[0]):
                    ok, why = True, 'V=0：无失败见证（B.13c）'
                else:
                    ok, why = OT.observability_ok(A, C, L)
                if ok:
                    st[key + ' ∧ (5b) 成立'] += 1
                    if key == 'h=q+r1' and len(witnesses) < 5:
                        witnesses.append((n, p, r, q, h, r1, d))
    print('统计：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')
    if witnesses:
        print('\n★ 等号且 (5b) 成立的反例：', witnesses)
    else:
        print('\n未找到"等号 ∧ (5b) 成立"的样本')


if __name__ == '__main__':
    main()
