"""b26_class_I_only_Z.py —— 核验 B.26：Class I 里 $(5a)$、$h$、$(5b)$ **都只依赖 $\\mathcal Z$**

**B.26（待记录）**：$p=r=1$、$q\\ge1$、$\\mathcal Z\\subseteq K$、$\\dim\\mathcal Z=d$、$\\mathcal V:=\\mathcal Z^\\perp$。则对任何满足
$\\ker[C;\\mathcal L]=\\mathcal Z$ 的 $\\mathcal L$：
1. $\\operatorname{row}[\\mathcal L;c]=\\mathcal V$；
2. $h=\\operatorname{rank}[\\mathcal L;CA;C]=\\dim(\\mathcal V+\\langle cA\\rangle)\\in\\{q+1,q+2\\}$，且 $h=q+2\\iff cA\\notin\\mathcal V$；
3. $(5a)\\iff \\mathcal VA\\subseteq\\mathcal V+\\langle cA\\rangle$；
4. 特别地：若 $cA\\in\\mathcal V$（即 $h=q+1$），则 $(5a)\\iff \\mathcal V$ 是 $A$-不变子空间。

本脚本：随机 Class I 实例与随机 $\\mathcal Z$，验证 1、2、3、4。

用法：python -u tools/verification/b26_class_I_only_Z.py
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

F = Fraction


def rowspace_of(M):
    """矩阵（行堆叠）的行空间基。"""
    keep = []
    for r in [list(x) for x in M]:
        cand = keep + [r]
        if LQ.rank(cand) == len(cand):
            keep = cand
    return keep


def same_space(X, Y, n):
    """两个行空间是否相同。"""
    if not X or not Y:
        return False
    return LQ.rank(X + Y) == len(X) == len(Y)


def main():
    rng = random.Random(20261119)
    st = Counter()
    for trial in range(1500):
        n = rng.choice([5, 6])
        p = r = 1
        A = [[F(rng.randrange(-2, 3)) for _ in range(n)] for _ in range(n)]
        C = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        L0 = [[F(rng.randrange(-2, 3)) for _ in range(n)]]
        if LQ.rank(C) != 1 or LQ.rank(L0) != 1:
            continue
        if LQ.rank([list(x) for x in C] + L0) != 2:
            continue
        O = QR.observability_matrix(A, C)
        n0 = LQ.rank(O)
        if n0 != n or LQ.rank(O + [list(x) for x in L0]) != n:
            continue
        CA = LQ.mul(C, A)
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (K and K[0]):
            continue
        k = len(K[0])
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        for q in range(q0, n0):
            d = n - 1 - q
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
                if L is None:
                    continue
                st['样本'] += 1
                # 𝒱 = 𝒵^⊥ 的基
                Zt = [[Z[i][j] for i in range(n)] for j in range(d)]
                ns = ZG.ker_cols(Zt)
                dZ = len(ns[0]) if (ns and ns[0]) else 0
                Vb = [[ns[i][t] for t in range(dZ)] for i in range(n)]
                Vrows = [[Vb[i][t] for i in range(n)] for t in range(dZ)]   # 行形式
                # 1) row[L; c] = 𝒱 ?
                st['row[L;c] = 𝒱'] += 1 if same_space([list(x) for x in L] + [list(x) for x in C], Vrows, n) else 0
                # 2) h = dim(𝒱 + ⟨cA⟩)
                h = LQ.rank([list(x) for x in L] + [list(x) for x in CA] + [list(x) for x in C])
                dimVcA = LQ.rank(Vrows + [list(x) for x in CA])
                st['h = dim(𝒱+⟨cA⟩)'] += 1 if h == dimVcA else 0
                st['h ∈ {q+1,q+2}'] += 1 if h in (q + 1, q + 2) else 0
                cA_in_V = LQ.rank(Vrows + [list(x) for x in CA]) == dimVcA and LQ.rank(Vrows + [list(x) for x in CA]) == len(Vrows)
                st['h=q+2 ⟺ cA∉𝒱'] += 1 if ((h == q + 2) == (not cA_in_V)) else 0
                # 3) (5a) ⟺ 𝒱A ⊆ 𝒱 + ⟨cA⟩
                VA = [[sum(r[j] * A[j][i] for j in range(n)) for i in range(n)] for r in Vrows]
                lhs = LQ.rank(VA + Vrows + [list(x) for x in CA]) == LQ.rank(Vrows + [list(x) for x in CA])
                rhs = LQ.condA(A, C, L)
                st['(5a) ⟺ 𝒱A⊆𝒱+⟨cA⟩'] += 1 if (lhs == rhs) else 0
                # 4) 若 cA ∈ 𝒱，则 (5a) ⟺ 𝒱 是 A-不变
                if cA_in_V:
                    st['情形 B（cA∈𝒱）'] += 1
                    inv = LQ.rank(VA + Vrows) == LQ.rank(Vrows)
                    st['(5a) ⟺ 𝒱 A-不变'] += 1 if (inv == rhs) else 0
                else:
                    st['情形 A（cA∉𝒱，h=q+2）'] += 1
                break
    print('统计：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')


if __name__ == '__main__':
    main()
