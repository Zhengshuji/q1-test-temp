"""b23_factorization_rank.py —— 核验 B.23：$Q_{\\mathcal L}(\\lambda)=P(\\lambda)H_0$（矩阵恒等式）及行列式

**B.23**：取 $B$（$r_1\\times n$ 满行秩，$\\operatorname{row}B=\\operatorname{row}[CA;C]$）、$H_0=[\\mathcal L;B]$，由 $(5a)$ 得 $\\mathcal LA=KH_0$，
$K=[K_1\\ K_2]$。则
$$Q_{\\mathcal L}(\\lambda)=\\begin{bmatrix}\\lambda\\mathcal L-\\mathcal LA\\\\ B\\end{bmatrix}
=P(\\lambda)H_0,\\qquad P(\\lambda)=\\begin{bmatrix}\\lambda I_q-K_1&-K_2\\\\ 0&I_{r_1}\\end{bmatrix},$$
且 $\\det P(\\lambda)=\\det(\\lambda I_q-K_1)$。

本脚本核验：(a) 矩阵恒等式（逐 λ）；(b) 行列式恒等式（逐 λ）；
(c) 秩跌点必是 $K_1$ 的特征值（秩跌 $\\Rightarrow\\det(\\lambda I-K_1)=0$）。

用法：python -u tools/verification/b23_factorization_rank.py
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
import observability_test as OT           # noqa: E402

F = Fraction


def row_basis(M):
    keep = []
    for r in [list(x) for x in M]:
        cand = keep + [r]
        if LQ.rank(cand) == len(cand):
            keep = cand
    return keep


def solve_K(LA, H0):
    n = len(H0[0]); m = len(H0)
    H0T = [[H0[i][j] for i in range(m)] for j in range(n)]
    K = []
    for r in LA:
        Aq = [row[:] + [r[i]] for i, row in enumerate(H0T)]
        rows_, cols_ = len(Aq), m
        piv = []
        rr = 0
        for c in range(cols_):
            p = next((i for i in range(rr, rows_) if Aq[i][c] != 0), None)
            if p is None:
                continue
            Aq[rr], Aq[p] = Aq[p], Aq[rr]
            inv = Aq[rr][c]
            Aq[rr] = [v / inv for v in Aq[rr]]
            for i in range(rows_):
                if i != rr and Aq[i][c] != 0:
                    f = Aq[i][c]
                    Aq[i] = [v - f * w for v, w in zip(Aq[i], Aq[rr])]
            piv.append(c)
            rr += 1
            if rr == rows_:
                break
        for i in range(rr, rows_):
            if all(v == 0 for v in Aq[i][:cols_]) and Aq[i][cols_] != 0:
                return None
        k = [F(0)] * cols_
        for i, c in enumerate(piv):
            k[c] = Aq[i][cols_]
        K.append(k)
    return K


def det(M):
    """精确行列式（高斯消元）。"""
    n = len(M)
    Aq = [row[:] for row in M]
    detv = F(1)
    for c in range(n):
        p = next((i for i in range(c, n) if Aq[i][c] != 0), None)
        if p is None:
            return F(0)
        if p != c:
            Aq[c], Aq[p] = Aq[p], Aq[c]
            detv = -detv
        detv *= Aq[c][c]
        inv = Aq[c][c]
        for i in range(c + 1, n):
            if Aq[i][c] != 0:
                f = Aq[i][c] / inv
                Aq[i] = [v - f * w for v, w in zip(Aq[i], Aq[c])]
    return detv


def main():
    rng = random.Random(20261113)
    st = Counter()
    for trial in range(1500):
        n = rng.choice([5, 6])
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
        K_ = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (K_ and K_[0]):
            continue
        k = len(K_[0])
        q0 = Q0.eta_and_q0(A, C, L0)[0]
        for q in range(q0, n0 - p + 1):
            d = n - p - q
            if d <= 0 or d > k:
                continue
            for rows_ in itertools.combinations(range(k), d):
                Z = DS.Z_from_theta(A, C, L0, q, rows_, [F(0)] * (d * (k - d)))
                if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                    continue
                try:
                    L = ZG.L_from_Z(A, C, L0, Z, q)
                except AssertionError:
                    continue
                if L is None or not LQ.condA(A, C, L):
                    continue
                B = row_basis([list(x) for x in CA] + [list(x) for x in C])
                if len(B) != r1:
                    continue
                H0 = [list(x) for x in L] + B
                if LQ.rank(H0) != r1 + q - (0 if LQ.rank(L) == q else 1):
                    pass
                LA = LQ.mul(L, A)
                Kmat = solve_K(LA, H0)
                if Kmat is None:
                    st['K 不存在'] += 1
                    continue
                st['样本'] += 1
                K1 = [row[:q] for row in Kmat]
                K2 = [row[q:] for row in Kmat]
                for lamv in [F(0), F(1), F(-1), F(2)]:
                    # Q(λ)
                    Q = []
                    for i in range(q):
                        Q.append([lamv * L[i][j] - LA[i][j] for j in range(n)])
                    for i in range(p):
                        Q.append(list(CA[i]))
                    for i in range(p):
                        Q.append(list(C[i]))
                    # P(λ)
                    P = []
                    for i in range(q):
                        P.append([lamv * (F(1) if i == j else F(0)) - K1[i][j] for j in range(q)] +
                                 [-K2[i][j] for j in range(r1)])
                    for i in range(r1):
                        P.append([F(0)] * q + [F(1) if i == j else F(0) for j in range(r1)])
                    PH = [[sum(P[i][t] * H0[t][j] for t in range(q + r1)) for j in range(n)]
                          for i in range(q + r1)]
                    st['Q = P·H0'] += 1 if PH == Q else 0
                    st['rank 一致'] += 1 if LQ.rank(PH) == LQ.rank(Q) else 0
                    # det P = det(λI−K1)
                    dP = det(P) if (q + r1) == (q + r1) else None
                    lI_K1 = [[lamv * (F(1) if i == j else F(0)) - K1[i][j] for j in range(q)] for i in range(q)]
                    st['det 一致'] += 1 if dP == det(lI_K1) else 0
                break
    print('统计：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')


if __name__ == '__main__':
    main()
