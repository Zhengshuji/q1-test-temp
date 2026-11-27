"""A liftable q=5 compressed gate at a sample point (attempt 289).

Sample x=2, y=3, z=6 (so z=xy).  H0=[e1;e1], Y=[e1;(0,0,1,x);(0,0,y,z)].
The free H_A rows are Y_i M + o_i with o_i in span(u,v), matching the
liftability form r_i AN = Y_i M + r_i E with E's rows spanning u,v.

Run: python tools/verification/c289_liftable_gate.py
"""
import sympy as sp

lam = sp.symbols('lam')
x, y, z = 2, 3, 6


def main():
    M = sp.Matrix([[0, -1, -2, 1],
                   [-2, -2, 1, 1],
                   [-2, 1, 1, -2],
                   [1, -2, 2, 1]])
    u = sp.Matrix([[-1, -2, -1, -2]])
    v = sp.Matrix([[-2, -2, -1, 2]])
    H = sp.Matrix([[1, 0, 0, 0],
                   [1, 0, 0, 0],
                   [1, 0, 0, 0],
                   [0, 0, 1, x],
                   [0, 0, y, z]])
    HA = sp.Matrix([[1, 0, 0, 0],
                    [1, 0, 0, 0],
                    [sp.Rational(7, 4), 0, sp.Rational(-3, 2), -3],
                    [-1, 0, sp.Rational(13, 2), 13],
                    [-3, 0, sp.Rational(39, 2), 39]])
    print('rank H =', H.rank(), 'rank[H;HA] =', sp.Matrix.vstack(H, HA).rank())
    assert H.rank() == 2
    assert sp.Matrix.vstack(H, HA).rank() == 2

    # liftability: each free H_A row minus Y_i M lies in span(u,v)
    Yrows = [sp.Matrix([[1, 0, 0, 0]]),
             sp.Matrix([[0, 0, 1, x]]),
             sp.Matrix([[0, 0, y, z]])]
    for i, Yrow in enumerate(Yrows):
        off = HA[2 + i, :] - Yrow * M
        print('offset', i, '=', off, '; in span(u,v):',
              sp.Matrix.hstack(u.T, v.T).rank() ==
              sp.Matrix.hstack(u.T, v.T, off.T).rank())
        assert sp.Matrix.hstack(u.T, v.T).rank() == \
            sp.Matrix.hstack(u.T, v.T, off.T).rank()

    P = sp.expand(lam * H - HA)
    ranks = [P.subs(lam, t).rank() for t in (0, 1, 2, 3, -1)]
    print('ranks P at 0,1,2,3,-1 =', ranks)
    assert all(r == 2 for r in ranks)

    # check all minors are not identically zero? print gcd of 2x2 minors
    import itertools
    mins = []
    for rs in itertools.combinations(range(5), 2):
        for cs in itertools.combinations(range(4), 2):
            m = sp.expand(P.extract(rs, cs).det())
            if m != 0:
                mins.append(m)
    g = mins[0]
    for m in mins[1:]:
        g = sp.gcd(g, m)
    print('gcd of 2x2 minors =', sp.factor(g))
    assert sp.degree(sp.factor(g), lam) == 0
    print('PASS: sample-level liftable q=5 gate')


if __name__ == '__main__':
    main()
