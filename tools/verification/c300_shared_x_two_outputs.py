"""Shared-x two-output mixed block (attempt 300).

H = [[1,0,0],[0,1,x],[0,0,0],[0,0,0]]
HA= [[1,0,0],[0,y1,z1],[0,y2,z2],[1,1,x]]
On the gate z1=x*y1, z2=x*y2: rank H=2, gcd of 2x2 minors of P is 1.

Run: python tools/verification/c300_shared_x_two_outputs.py
"""
import itertools

import sympy as sp

lam, x, y1, y2, z1, z2 = sp.symbols('lam x y1 y2 z1 z2')


def main():
    H = sp.Matrix([[1, 0, 0], [0, 1, x], [0, 0, 0], [0, 0, 0]])
    HA = sp.Matrix([[1, 0, 0], [0, y1, z1], [0, y2, z2], [1, 1, x]])
    assert H.rank() == 2

    gate = {z1: x * y1, z2: x * y2}
    print('rank[H;HA] on gate =', sp.Matrix.vstack(H, HA).subs(gate).rank())
    assert sp.Matrix.vstack(H, HA).subs(gate).rank() == 2

    off = {z1: x * y1 + 1, z2: x * y2}
    print('rank[H;HA] off gate =', sp.Matrix.vstack(H, HA).subs(off).rank())
    assert sp.Matrix.vstack(H, HA).subs(off).rank() == 3

    P = sp.expand(lam * H - HA).subs(gate)
    mins = []
    for rs in itertools.combinations(range(4), 2):
        for cs in itertools.combinations(range(3), 2):
            m = sp.expand(P.extract(rs, cs).det())
            if m != 0:
                mins.append(m)
    g = mins[0]
    for m in mins[1:]:
        g = sp.gcd(g, m)
    print('gcd of 2x2 minors on gate =', sp.factor(g))
    assert sp.degree(sp.factor(g), lam) == 0

    pt = {x: 2, y1: 3, y2: 5, z1: 6, z2: 10}
    for t in (0, 1, 2, 3, 5, -1):
        print('rank P(%s) =' % t, P.subs(pt).subs(lam, t).rank())
        assert P.subs(pt).subs(lam, t).rank() == 2
    print('PASS: shared-x two-output block')


if __name__ == '__main__':
    main()
