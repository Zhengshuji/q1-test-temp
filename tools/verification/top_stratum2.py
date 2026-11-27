"""top_stratum2.py —— 正确版本的"顶层"搜索：$V\\subseteq\\mathcal Z\\subseteq K$

前一版（`top_stratum.py`）有构造错误：把 $V$ 的列直接拼进 $Z$，于是 $Z\\not\\subseteq K$，它不可能是
$\\ker[C;\\mathcal L]$；而那些样本其实只是 $\\mathcal L=L_0$ 的普通候选。

正确做法：
1. 先筛出 $V\\subseteq K=\\ker[C;L_0]$ 的实例（这是 $V\\subseteq\\mathcal Z$ 的必要条件，因 $\\mathcal Z\\subseteq K$）；
2. 在阶 $q$ 上要求 $d=n-p-q\\ge\\dim V$ 且 $d\\le\\dim K$；
3. 取 $\\mathcal Z$ 为 $K$ 内含 $V$ 的 $d$ 维子空间，构造 $\\mathcal L$，检查 $(5a)$、$h$、$(5b)$。

若存在 $(5a)$ 成立、$h=q+r_1$、$(5b)$ 成立的样本 ⟹ **B.9 的严格不等式被推翻**。

用法：python -u tools/verification/top_stratum2.py
"""

import os
import sys
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

F = Fraction


def main():
    rng = random.Random(20261107)
    st = Counter()
    wit = []
    for trial in range(6000):
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
        if n0 != n or LQ.rank(O + [list(x) for x in L0]) != n:
            continue
        CA = LQ.mul(C, A)
        r1 = LQ.rank([list(x) for x in CA] + [list(x) for x in C])
        V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (V and V[0] and K and K[0]):
            continue
        dV, dK = len(V[0]), len(K[0])
        # 必要条件 V ⊆ K
        if LQ.rank([[K[i][j] for j in range(dK)] + [V[i][j2] for j2 in range(dV)]
                    for i in range(n)]) != dK:
            st['V ⊄ K（顶层不可能）'] += 1
            continue
        st['V ⊆ K'] += 1
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        for q in range(q0, n0 - p + 1):
            d = n - p - q
            if d < dV or d > dK:
                continue
            # Z = span(V 的基 + K 中随机的 (d-dV) 个组合)，且必须在 K 内
            for _ in range(30):
                extra = d - dV
                coef = [[F(rng.randrange(-2, 3)) for _ in range(extra)] for _ in range(dK)]
                Z = [[V[i][j] for j in range(dV)] +
                     [sum(K[i][t] * coef[t][u] for t in range(dK)) for u in range(extra)]
                     for i in range(n)]
                if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                    continue
                # 确认 Z ⊆ K
                if LQ.rank([[K[i][j] for j in range(dK)] + [Z[i][j2] for j2 in range(d)]
                            for i in range(n)]) != dK:
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
                ok, why = OT.observability_ok(A, C, L)
                st['顶层可容许 ' + key] += 1
                if ok:
                    st['顶层可容许 ' + key + ' ∧ (5b) 成立'] += 1
                    if len(wit) < 4:
                        wit.append((n, p, r, q, d, h, r1, A, C, L0, Z, L))
                break
    print('统计：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')
    print()
    if wit:
        print('★ 候选反例（n,p,r,q,d,h,r1）=', [w[:7] for w in wit])
    else:
        print('未找到"顶层可容许 ∧ h=q+r1 ∧ (5b) 成立"的样本')


if __name__ == '__main__':
    main()
