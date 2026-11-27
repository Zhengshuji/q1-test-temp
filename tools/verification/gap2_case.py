"""gap2_case.py —— 自有阶差 2 实例的细查

实例：`diag-distinct-n7`、$n=7$、$p=2$、$r=1$、$q_0=2$；扫描给出 $q=2,3$ 全失败、$q=4$ 全成功
（[gap_scan.py](gap_scan.py)）。本脚本：

1. 对 $q=2,3$ 的候选记录 $h,r_1,d_{\\rm fin}$，并按 Type I/II/III 分类；
2. 把 $q=3$ 的样本数加大到 300（更强的"不是抽样不足"证据）；
3. 对 $q=4$ 确认可行比例。

用法：python -u tools/verification/gap2_case.py
"""

import os
import sys
from collections import Counter
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p))

import linalg_q as LQ                     # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import z_generator as ZG                  # noqa: E402
import type3_structured as T3             # noqa: E402

F = Fraction


def build():
    name = 'diag-distinct-n7'
    A = T3.diag_family(7, [0, 1, 2, 3])
    n, p, r = 7, 2, 1
    import random
    rngC = random.Random(sum(ord(ch) for ch in name) * 13 + p * 17)
    C = None
    for _try in range(60):
        cand = [[F(rngC.randrange(2)) for _ in range(n)] for _ in range(p)]
        if LQ.rank(cand) != p:
            continue
        if LQ.rank(T3.obs_matrix(A, cand)) != n:
            continue
        C = cand
        break
    assert C is not None
    L0 = T3.pick_L0(A, C, r, seed=sum(ord(ch) for ch in name) * 7 + p * 31 + r)
    assert L0 is not None
    return A, C, L0


def main():
    A, C, L0 = build()
    q0 = Q0.eta_and_q0(A, C, L0)[0]
    CA = LQ.mul(C, A)
    r1 = LQ.rank([x[:] for x in C] + [x[:] for x in CA])
    n, p = len(A), len(C)
    print('A =', [[str(x) for x in row] for row in A])
    print('C =', [[str(x) for x in row] for row in C])
    print('L0=', [[str(x) for x in row] for row in L0])
    print(f'n={n} p={p} r={len(L0)} q0={q0} r1={r1}  n-p={n - p}')
    for q, ns in ((q0, 120), (q0 + 1, 300), (q0 + 2, 60)):
        cands = ZG.sample_L_at_order(A, C, L0, q, ns, seed=q * 101 + q0 * 37)
        types = Counter()
        info = []
        for L in cands:
            h, s, m, d_fin = T3.fast_dfin(A, C, L)
            if d_fin == 0:
                types['ok'] += 1
            elif h >= q + r1:
                types['I'] += 1
            elif q + r1 - h > s:
                types['II'] += 1
            else:
                types['III'] += 1
                info.append((h, s, d_fin))
        print(f'q={q}: 样本 {len(cands)}，分类 {dict(types)}'
              + (f'；Type III 的 (h,s,d_fin) 例：{info[:3]}' if info else ''))


if __name__ == '__main__':
    main()
