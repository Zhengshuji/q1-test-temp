"""Explicit compact certificate QPR = I for the q=3 instance (attempt 252).

For the 244 pencil P (3x3 rank 2), choose
    Q = [[1,2,-1],[-2,2,2]]
so that (Q P) has the constant 2x2 minor 36 on columns 0 and 2.  Invert that
constant 2x2 block to build a polynomial R (3x2) with Q P R = I_2.

Run: python tools/verification/c252_compact_cert.py
"""
import sympy as sp

lam = sp.symbols('lam')


def main():
    P = sp.Matrix([[0, 0, lam],
                   [lam - 3, 2 * lam - 6, -1],
                   [3 * lam - 3, 6 * lam - 6, lam - 3]])
    Q = sp.Matrix([[1, 2, -1], [-2, 2, 2]])
    print('rank P =', P.rank(), 'det P =', sp.factor(P.det()))
    assert P.rank() == 2 and sp.expand(P.det()) == 0

    M = sp.expand(Q * P)
    S = M[:, [0, 2]]
    detS = sp.factor(S.det())
    print('M =', M)
    print('S =', S, 'det S =', detS)
    assert detS == 36

    Sinv = S.inv()
    R = sp.zeros(3, 2)
    R[0, 0] = Sinv[0, 0]
    R[0, 1] = Sinv[0, 1]
    R[2, 0] = Sinv[1, 0]
    R[2, 1] = Sinv[1, 1]
    print('R =', sp.simplify(R))
    prod = sp.simplify(sp.expand(Q * P * R))
    print('Q P R =', prod)
    assert prod == sp.eye(2)

    # the three maximal minors of P have gcd 1 (so (5b) holds)
    import itertools
    mins = []
    for rs in itertools.combinations(range(3), 2):
        for cs in itertools.combinations(range(3), 2):
            mins.append(sp.expand(P.extract(rs, cs).det()))
    g = mins[0]
    for m in mins[1:]:
        g = sp.gcd(g, m)
    print('maximal minors =', [sp.factor(m) for m in mins], 'gcd =', sp.factor(g))
    assert sp.degree(sp.factor(g), lam) == 0
    print('PASS: explicit compact certificate Q P R = I_2 for the 244 pencil')


if __name__ == '__main__':
    main()
