"""Exact check of the q=3, n=7, p=2 feasible instance (attempt 244).

Layout (0-based):
    A[2][0]=1 (col1=e3), A[3][1]=1 (col2=e4),
    A[4][2]=1 (row5=e3), A[5][3]=1 (row6=e4),
    A[0][6]=1 (A[1][7]=1), row7=0.
    C = rows e5,e6; L0=e7; l1,l2 as in attempt 244.

Checks:
1. rank S = 5, Q dim = 2.
2. (5a): rank[LA;L;CA;C] = rank[L;CA;C].
3. (5b): rank H = 2, det P = 0, gcd of all 2x2 minors of P is 1.
4. Absorption: v1 is proportional to x1, and x2=v1, v2=x2.

Run: python tools/verification/c244_q3_feasible.py
"""
import itertools
import sys

import sympy as sp

lam = sp.symbols('lam')


def main():
    A = sp.zeros(7, 7)
    A[2, 0] = 1
    A[3, 1] = 1
    A[4, 2] = 1
    A[5, 3] = 1
    A[0, 6] = 1

    C = sp.Matrix([[0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0]])
    L0 = sp.Matrix([[0, 0, 0, 0, 0, 0, 1]])
    l1 = sp.Matrix([[1, 2, 3, 6, 0, 0, 0]])
    l2 = sp.Matrix([[3, 6, 3, 6, 0, 0, 1]])
    L = sp.Matrix.vstack(L0, l1, l2)
    CA = C * A
    S = sp.Matrix.vstack(L0, CA, C)
    print('rank C =', C.rank(), 'rank CA =', CA.rank(), 'rank S =', S.rank())
    assert S.rank() == 5
    assert 7 - S.rank() == 2

    base = sp.Matrix.vstack(L, CA, C)
    full = sp.Matrix.vstack(L * A, L, CA, C)
    print('rank full / base =', full.rank(), base.rank())
    assert full.rank() == base.rank() == 6

    K = sp.Matrix.vstack(C, CA).nullspace()
    N = sp.Matrix.hstack(*K)
    print('dim K0 =', N.cols)
    assert N.cols == 3
    H = sp.expand(L * N)
    HA = sp.expand(L * A * N)
    P = sp.expand(lam * H - HA)
    print('H =', H)
    print('HA =', HA)
    print('rank H =', H.rank())
    assert H.rank() == 2

    print('det P =', sp.factor(sp.expand(P.det())))
    assert sp.expand(P.det()) == 0

    mins = []
    for rs in itertools.combinations(range(3), 2):
        for cs in itertools.combinations(range(3), 2):
            mins.append(sp.expand(P.extract(rs, cs).det()))
    g = mins[0]
    for m in mins[1:]:
        g = sp.gcd(g, m)
    print('gcd of 2x2 minors =', sp.factor(g))
    assert sp.degree(sp.factor(g), lam) == 0, 'expected (5b) to hold'

    # Absorption data: x1=[l1], x2=[l2], v1=[l1A], v2=[l2A] in Q (coords e1,e2)
    def q_coords(row):
        return sp.Matrix([[row[0, 0]], [row[0, 1]]])

    x1, x2 = q_coords(l1), q_coords(l2)
    v1, v2 = q_coords(l1 * A), q_coords(l2 * A)
    print('x1,x2,v1,v2 =', list(x1), list(x2), list(v1), list(v2))
    # v1 is proportional to x1 (cross product zero)
    assert sp.expand(x1[0, 0] * v1[1, 0] - x1[1, 0] * v1[0, 0]) == 0
    assert v1 == x2 and v2 == x2
    print('PASS: q=3 instance satisfies (5a) and (5b); v1 is absorbed by x2')


if __name__ == '__main__':
    main()
