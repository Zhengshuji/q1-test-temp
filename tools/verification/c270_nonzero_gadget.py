"""Compressed nonzero gadget for Route B (attempt 270).

q=3, omega=2, k=3.  With f a scalar parameter:
    H  = [ f e1 ; f e2 ; e1+e2 ]
    HA = -[ f b1 ; f b2 ; b3 ]
    b1=(-1,0,0), b2=(-2,2,0), b3=(0,-2,0)
Then P(lambda)=lambda H - HA has gcd of its 2x2 minors equal to f.
At f=0, rank P < 2 (so (5b) fails); at f=1, rank P = 2 and gcd is constant.

Run: python tools/verification/c270_nonzero_gadget.py
"""
import itertools
import sympy as sp

lam, f = sp.symbols('lam f')


def main():
    e1 = sp.Matrix([[1, 0, 0]])
    e2 = sp.Matrix([[0, 1, 0]])
    b1 = sp.Matrix([[-1, 0, 0]])
    b2 = sp.Matrix([[-2, 2, 0]])
    b3 = sp.Matrix([[0, -2, 0]])

    H = sp.Matrix.vstack(f * e1, f * e2, e1 + e2)
    HA = -sp.Matrix.vstack(f * b1, f * b2, b3)
    P = sp.expand(lam * H - HA)
    print('H =', H)
    print('HA =', HA)
    print('P =', P)
    print('rank H at f=1:', H.subs(f, 1).rank(), '; at f=0:', H.subs(f, 0).rank())

    mins = []
    for rs in itertools.combinations(range(3), 2):
        for cs in itertools.combinations(range(3), 2):
            mins.append(sp.expand(P.extract(rs, cs).det()))
    g = mins[0]
    for m in mins[1:]:
        g = sp.gcd(g, m)
    g = sp.factor(g)
    print('2x2 minors =', [sp.factor(m) for m in mins])
    print('gcd =', g)
    assert sp.simplify(g - f) == 0, 'expected gcd = f'

    for val in (0, 1, 2):
        Pv = P.subs(f, val)
        r = Pv.subs(lam, 3).rank()
        print('f=%s, rank P(3) =' % val, r)
        if val == 0:
            assert r < 2
        else:
            assert r == 2
    print('PASS: compressed nonzero gadget with gcd = f')


if __name__ == '__main__':
    main()
