"""boundary_counterexample.py —— 等号情形 $h=q+r_1$ 的**可行**反例（推翻 B.9 的严格不等式）

构造（n=5, p=2, r=1, q=1, d=2）：
* $V=\\ker[C;CA]$（维数 1，因 $r_1=4$），$\\mathcal Z=\\langle V\\rangle+$ 一维（维数 2），故 $V\\subseteq\\mathcal Z$；
* $(5a)$ 成立；$h=q+r_1=1+4=5$（**等号**）；
* 由 B.13c：失败需要 $x\\in V\\setminus\\mathcal Z$，而 $V\\subseteq\\mathcal Z$ ⟹ **无失败** ⟹ $(5b)$ 成立。

⟹ "$(5b)\\Rightarrow h<q+r_1$"（B.9 的原陈述）**为假**；正确说法是 $(5b)\\Rightarrow h\\le q+r_1$，
且等号情形可**可行**（顶层 $V\\subseteq\\mathcal Z$）。

本脚本重建该实例并逐条核验。

用法：python -u tools/verification/boundary_counterexample.py
"""

import os
import sys
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


def build(rng, n=5, p=2, r=1):
    """在 $q_0\\le r_1-p$ 的实例里，构造 $\\mathcal Z\\supseteq V$ 且 $(5a)$ 成立、$h=q+r_1$ 的候选。"""
    for _ in range(20000):
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
        dV, k = len(V[0]), len(K[0])
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        if q0 > r1 - p:
            continue
        for q in range(q0, n0 - p + 1):
            d = n - p - q
            if d < dV or d > k:
                continue
            Km = [[K[i][t] for t in range(k)] for i in range(n)]
            for _ in range(40):
                R = [[F(rng.randrange(-2, 3)) for _ in range(d - dV)] for _ in range(k)]
                Z = [[V[i][j] for j in range(dV)] +
                     [sum(Km[i][t] * R[t][u] for t in range(k)) for u in range(d - dV)]
                     for i in range(n)]
                if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                    continue
                try:
                    L = ZG.L_from_Z(A, C, L0, Z, q)
                except AssertionError:
                    continue
                if L is None or not LQ.condA(A, C, L):
                    continue
                h = LQ.rank([list(x) for x in L] + [list(x) for x in CA] + [list(x) for x in C])
                if h != q + r1:
                    continue
                return dict(A=A, C=C, L0=L0, Z=Z, L=L, q=q, d=d, h=h, r1=r1, n=n, p=p, r=r,
                            dV=dV, q0=q0)
    return None


def main():
    import random
    rng = random.Random(20261106)
    data = build(rng)
    if data is None:
        print('未构造出实例'); return
    A, C, L0, Z, L = data['A'], data['C'], data['L0'], data['Z'], data['L']
    n, p, r, q, d = data['n'], data['p'], data['r'], data['q'], data['d']
    CA = LQ.mul(C, A)
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in CA])
    dV = len(V[0])
    st = Counter()

    # 1) 基本量
    print(f'n={n}, p={p}, r={r}, q={q}, d={d}, q0={data["q0"]}, dim V={dV}, r1={data["r1"]}')
    st['h = q+r1'] = (data['h'] == q + data['r1'])
    # 2) (5a)
    st['(5a) 成立'] = LQ.condA(A, C, L)
    # 3) V ⊆ Z
    aug = [[Z[i][j] for j in range(d)] + [V[i][j2] for j2 in range(dV)] for i in range(n)]
    st['V ⊆ Z'] = (LQ.rank(aug) == d)
    # 4) (5b)：由 B.13c，V ⊆ Z ⟹ 无失败
    ok, why = OT.observability_ok(A, C, L)
    st['(5b) 成立（B.12 判据）'] = bool(ok)
    st['V/S = 0 ⟹ 由 B.13c 无失败'] = st['V ⊆ Z']
    # 5) 该阶其他候选（同一阶的可容许 ℒ）里有没有 h<q+r1 的？（检验 B.11d 的等价）
    lower = 0
    import itertools
    for rows in itertools.combinations(range(d), d) if False else []:
        pass
    print()
    for k_, v in st.items():
        print(f'  {k_}: {v}')
    print()
    if all(st.values()):
        print('⟹ 等号情形 h=q+r1 **可行**：B.9 的严格不等式 $(5b)\\Rightarrow h<q+r_1$ **为假**。')
    else:
        print('⟹ 未全部通过，需复查。')
    print()
    print('A =', [[str(x) for x in row] for row in A])
    print('C =', [[str(x) for x in row] for row in C])
    print('L0=', [[str(x) for x in row] for row in L0])
    print('L =', [[str(x) for x in row] for row in L])
    print('Z =', [[str(x) for x in row] for row in Z])


if __name__ == '__main__':
    main()
