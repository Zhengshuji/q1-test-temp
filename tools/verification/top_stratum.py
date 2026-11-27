"""top_stratum.py —— 专查"顶层"($V\\subseteq\\mathcal Z$) 能否给出等号可行反例

若 $V\\subseteq\\mathcal Z$，则 $\\mathcal LV=0$，商铅笔定义域 $V/S=V/\\mathcal Z=0$，$(5b)$ **自动成立**
（B.16(a)）。于是"等号 $h=q+r_1$ 处必失败"的断言只可能被这种候选推翻。
本轮专查：可容许（$(5a)$）、$V\\subseteq\\mathcal Z$、且 $h=q+r_1$ 的候选是否存在。

用法：python -u tools/verification/top_stratum.py
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
    rng = random.Random(20261106)
    st = Counter()
    for trial in range(3000):
        n = rng.choice([4, 5, 6, 7])
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
        V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (K and K[0]):
            continue
        dV = len(V[0]) if (V and V[0]) else 0
        k = len(K[0])
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        st['实例'] += 1
        if q0 > r1 - p:
            st['q0 > r1-p（顶层不可达）'] += 1
            continue
        st['q0 ≤ r1-p（可能可达）'] += 1
        # 试 q = q0 附近的阶，找 Z ⊇ V 且 dim d
        for q in range(q0, n0 - p + 1):
            d = n - p - q
            if d < dV or d > k:
                continue
            # 构造 Z ⊇ V：取 V 的基，扩成 d 维（在 K 内）
            VK = [[V[i][j] for j in range(dV)] + [K[i][t] for t in range(k)] for i in range(n)]
            # 求 ker(K) ∩ ... 简化：直接在 span(K) 里随机取 d 维并检查含 V
            for _ in range(20):
                R = [[F(rng.randrange(-2, 3)) for _ in range(d - dV)] for _ in range(k)]
                if d > dV:
                    Km = [[K[i][t] for t in range(k)] for i in range(n)]
                    Z = [[V[i][j] for j in range(dV)] +
                         [sum(Km[i][t] * R[t][u] for t in range(k)) for u in range(d - dV)]
                         for i in range(n)]
                else:
                    Z = [[V[i][j] for j in range(dV)] for i in range(n)]
                if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                    continue
                # 确认 V ⊆ Z
                if LQ.rank([[Z[i][j] for j in range(d)] + [V[i][j2] for j2 in range(dV)]
                            for i in range(n)]) != d:
                    continue
                try:
                    L = ZG.L_from_Z(A, C, L0, Z, q)
                except AssertionError:
                    continue
                if L is None or not LQ.condA(A, C, L):
                    continue
                h = LQ.rank([list(x) for x in L] + [list(x) for x in CA] + [list(x) for x in C])
                gap = h - (q + r1)
                key = 'h<q+r1' if gap < 0 else ('h=q+r1' if gap == 0 else 'h>q+r1')
                st['顶层可容许 ' + key] += 1
                break
    print('统计：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')
    print('\n若"顶层可容许 h=q+r1"为 0，则顶层路线不能给出等号反例。')


if __name__ == '__main__':
    main()
