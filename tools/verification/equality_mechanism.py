"""equality_mechanism.py —— 等号情形 $h=q+r_1$ 的**失败机制**：秩在哪些 $\\lambda$ 处跌破？

对 $h=q+r_1$ 的可容许样本，计算 $Q_{\\mathcal L}(\\lambda)$ 的极大子式 gcd 的根，并与
$\\operatorname{spec}(A)$、$\\operatorname{spec}(\\Lambda)$ 对照。问题：跌破点总是 $A$ 的特征值吗？
还是总与 $\\Lambda$ 的特征值相关？

用法：python -u tools/verification/equality_mechanism.py
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
import observability_test as OT           # noqa: E402
import decide_symbolic as DS              # noqa: E402

F = Fraction
lam = sp.symbols('lam')


def gcd_of_minors(A, C, L):
    """$Q_{\\mathcal L}(\\lambda)$ 的 $h$ 阶极大子式 gcd（符号 λ）。"""
    n, p, q = len(A), len(C), len(L)
    CA = LQ.mul(C, A)
    LA = LQ.mul(L, A)
    # Q(λ) = [λL − LA; CA; C]，行数 q+2p
    rows = q + 2 * p
    h = LQ.rank([list(x) for x in L] + [list(x) for x in CA] + [list(x) for x in C])
    As = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in A])
    Cs = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in C])
    Ls = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in L])
    Q = sp.zeros(rows, n)
    QL = lam * Ls - Ls * As
    for i in range(q):
        for j in range(n):
            Q[i, j] = sp.expand(QL[i, j])
    CAs = Cs * As
    for i in range(p):
        for j in range(n):
            Q[q + i, j] = CAs[i, j]
            Q[q + p + i, j] = Cs[i, j]
    mins = []
    for rs in itertools.combinations(range(rows), h):
        m = sp.expand(Q[list(rs), :].det())
        if m != 0:
            mins.append(sp.Poly(m, lam))
    if not mins:
        return None, h
    g = mins[0]
    for mm in mins[1:]:
        g = sp.gcd(g, mm)
    return g, h


def main():
    rng = random.Random(20261108)
    st = Counter()
    shown = 0
    for trial in range(2000):
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
                    L = ZG.L_from_Z(A, C, L0, Z, q)
                except AssertionError:
                    continue
                if L is None or not LQ.condA(A, C, L):
                    continue
                h = LQ.rank([list(x) for x in L] + [list(x) for x in CA] + [list(x) for x in C])
                if h != q + r1:
                    continue
                g, hh = gcd_of_minors(A, C, L)
                if g is None:
                    st['gcd 全零'] += 1
                    continue
                roots = sp.roots(g.as_expr(), lam)
                deg = sp.degree(g.as_expr(), lam)
                st['等号样本'] += 1
                st[f'gcd 次数 = {deg}'] += 1
                # A 的特征值
                evA = [sp.nsimplify(e) for e in sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in A]).eigenvals()]
                # 根是否都在 spec(A) 里（数值比对）
                allin = True
                for rt, mult in roots.items():
                    rv = complex(sp.N(rt))
                    if not any(abs(rv - complex(sp.N(e))) < 1e-8 for e in evA):
                        allin = False
                st['根全在 spec(A)' if allin else '根不全在 spec(A)'] += 1
                if shown < 3:
                    print(f'  n={n},p={p},r={r},q={q},d={d},h={h}：gcd 次数={deg}，'
                          f'根={list(roots.keys())}，spec(A)={[sp.N(e) for e in evA]}')
                    shown += 1
                break
    print('\n统计：')
    for k_ in sorted(st):
        print(f'  {k_}: {st[k_]}')


if __name__ == '__main__':
    main()
