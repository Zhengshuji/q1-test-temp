"""equality_drop_point.py —— 等号情形下秩**在哪个 λ 跌**（数值诊断，不算证明）

对 $h=q+r_1$ 的可容许样本，在若干 $\\lambda$ 处算 $Q_{\\mathcal L}(\\lambda)$ 的秩：
* 有理 $\\lambda$（0, ±1, ±2, 3）；
* $A$ 的特征值（浮点）。
看跌破点是否总落在 $\\operatorname{spec}(A)$。仅作诊断。

用法：python -u tools/verification/equality_drop_point.py
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

import sympy as sp                        # noqa: E402
import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import qmin_scan_pr as QR                 # noqa: E402
import c208_q0_lower_bound as Q0          # noqa: E402
import decide_symbolic as DS              # noqa: E402

F = Fraction


def Q_matrix(A, C, L, cplx=False):
    n, p, q = len(A), len(C), len(L)
    CA = LQ.mul(C, A)
    LA = LQ.mul(L, A)
    rows = q + 2 * p
    ent = (lambda f: complex(sp.N(f))) if cplx else (lambda f: f)
    Q = []
    for i in range(q):
        Q.append([ent(('LAM', L[i][j], LA[i][j])) for j in range(n)])
    for i in range(p):
        Q.append([ent(CA[i][j]) for j in range(n)])
    for i in range(p):
        Q.append([ent(C[i][j]) for j in range(n)])
    return Q


def rank_at(Q, lam):
    """rank Q(λ)（λ 为复数或浮点）。"""
    M = sp.Matrix(Q)
    M = M.subs(sp.Symbol('LAMSYM'), 0)  # 占位
    return M.rank()


def main():
    rng = random.Random(20261110)
    st = Counter()
    shown = 0
    for trial in range(3000):
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
        K = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
        if not (K and K[0]):
            continue
        k = len(K[0])
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
                    L = ZG.L_from_basis(A, C, L0, Z, q) if hasattr(ZG, 'L_from_basis') else ZG.L_from_Z(A, C, L0, Z, q)
                except AssertionError:
                    continue
                if L is None or not LQ.condA(A, C, L):
                    continue
                h = LQ.rank([list(x) for x in L] + [list(x) for x in CA] + [list(x) for x in C])
                if h != q + r1:
                    continue
                # 数值诊断：Q(λ) 在各 λ 处的秩
                As = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in A])
                evs = [complex(e) for e in As.eigenvals()]
                lam = sp.Symbol('LAM')
                CA_s = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in CA])
                L_s = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in L])
                LA_s = L_s * As
                Q = sp.zeros(q + 2 * p, n)
                for i in range(q):
                    for j in range(n):
                        Q[i, j] = lam * L_s[i, j] - LA_s[i, j]
                for i in range(p):
                    for j in range(n):
                        Q[q + i, j] = CA_s[i, j]
                        Q[q + p + i, j] = sp.Rational(C[i][j].numerator, C[i][j].denominator)
                deg = sp.degree(sp.expand(Q.det()), lam) if Q.rows == Q.cols else None
                st['等号样本'] += 1
                if deg is not None:
                    st[f'deg det = {deg}'] += 1
                else:
                    st['非方阵'] += 1
                if shown < 4:
                    ranks = []
                    for lamv in [F(0), F(1), F(-1), F(2)]:
                        ranks.append(Q.subs(lam, sp.Rational(lamv.numerator, lamv.denominator)).rank())
                    print(f'  n={n},p={p},r={r},q={q},d={d},h={h}：deg det={deg}；'
                          f'λ=0,±1,2 处 rank={ranks}（h={h}）')
                    shown += 1
                break
    print('\n统计：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')


if __name__ == '__main__':
    main()
