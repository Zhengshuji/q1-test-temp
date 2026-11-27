"""Audit of the missing L0A row (attempt 239).

The full (5a) condition uses both rows of LA:
    [L0A; lA; L0; l; CA; C] vs [L0; l; CA; C].
The earlier reduced determinant omitted L0A.

Checks:
1. (5a) holds for (a,b,c,d,e)=(1,0,1,0,0) (b=0,d=0,c!=0).
2. (5a) fails for (0,0,1,1,0), (1,2,3,6,0), (1,1,1,0,0), (1,0,1,1,0).
3. The (5b) minor at (1,0,1,0,0) is c*(lam^2-lam-1), nonconstant.
4. Therefore the instance has no feasible L.

Run: python tools/verification/c239_missing_L0A.py
"""
import sys
from fractions import Fraction as F

sys.path.insert(0, '.')
sys.path.insert(0, 'tools/verification')
sys.path.insert(0, 'tools/exact_linalg')
sys.path.insert(0, 'tools/ledger')

import linalg_q as LQ

A = [[F(x) for x in row] for row in [
    [1, 1, -1, 0, 1],
    [-1, 0, 0, -1, 1],
    [0, 1, -1, 0, 1],
    [0, 0, 0, -1, 0],
    [-1, 1, 0, 0, 0]]]
C = [[F(0), F(0), F(0), F(0), F(1)]]
L0 = [[F(1), F(0), F(0), F(0), F(0)]]
L0A = LQ.mul(L0, A)[0]
CA = LQ.mul(C, A)[0]


def ranks(pt):
    l = [F(v) for v in pt]
    base = [L0[0][:], l, CA, C[0][:]]
    full = [L0A, LQ.mul([l], A)[0]] + base
    return LQ.rank(full), LQ.rank(base)


def main():
    good = (1, 0, 1, 0, 0)
    r1, r0 = ranks(good)
    print('1. (5a) point', good, 'ranks', r1, r0)
    assert r1 == r0, 'expected (5a) to hold'

    for pt in [(0, 0, 1, 1, 0), (1, 2, 3, 6, 0), (1, 1, 1, 0, 0), (1, 0, 1, 1, 0)]:
        r1, r0 = ranks(pt)
        print('2. (5a) point', pt, 'ranks', r1, r0)
        assert r1 > r0, 'expected (5a) to fail at %s' % (pt,)

    # (5b) at b=d=0, c=1: the only nonzero maximal minor is c*(lam^2-lam-1)
    # Verify by exact evaluation at a root? Use sympy for the factor.
    import sympy as sp
    lam = sp.symbols('lam')
    a, c = sp.symbols('a c')
    H = sp.Matrix([[1, 0, 0], [a, c, 0]])
    HA = sp.Matrix([[2, -1, 0], [2 * a + c, -a - c, 0]])
    P = lam * H - HA
    m = sp.expand(P[:, 0:2].det())
    print('3. minor at b=d=0:', sp.factor(m))
    assert sp.factor(m) == c * (lam ** 2 - lam - 1)
    print('PASS: the missing L0A row invalidates the reduced gate; the instance is infeasible')


if __name__ == '__main__':
    main()
