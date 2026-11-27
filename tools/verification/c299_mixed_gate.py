"""Mixed block: (5a) forces z=xy, (5b) automatic (attempt 299).

H = [[1,0,0],[0,1,x],[0,0,0]]
HA= [[1,0,0],[0,y,z],[1,1,w]]
On the gate z=x*y, w=x: rank[H;HA]=2, det P=0, gcd of 2x2 minors=1.

Run: python tools/verification/c299_mixed_gate.py
"""
import itertools

import sympy as sp

lam, x, y, z, w = sp.symbols('lam x y z w')


def main():
    H = sp.Matrix([[1, 0, 0], [0, 1, x], [0, 0, 0]])
    HA = sp.Matrix([[1, 0, 0], [0, y, z], [1, 1, w]])

    assert H.rank() == 2
    # (5a) on the gate
    gate = {z: x * y, w: x}
    print('rank[H;HA] on gate =', sp.Matrix.vstack(H, HA).subs(gate).rank())
    assert sp.Matrix.vstack(H, HA).subs(gate).rank() == 2

    # off gate, e.g. z != xy, the rank is 3
    off = {z: x * y + 1, w: x}
    print('rank[H;HA] off gate =', sp.Matrix.vstack(H, HA).subs(off).rank())
    assert sp.Matrix.vstack(H, HA).subs(off).rank() == 3

    P = sp.expand(lam * H - HA)
    Pg = sp.expand(P.subs(gate))
    print('det P on gate =', sp.factor(Pg.det()))
    assert sp.factor(Pg.det()) == 0

    mins = []
    for rs in itertools.combinations(range(3), 2):
        for cs in itertools.combinations(range(3), 2):
            m = sp.expand(Pg.extract(rs, cs).det())
            if m != 0:
                mins.append(m)
    g = mins[0]
    for m in mins[1:]:
        g = sp.gcd(g, m)
    print('gcd of 2x2 minors on gate =', sp.factor(g))
    assert sp.degree(sp.factor(g), lam) == 0

    pt = {x: 2, y: 3, z: 6, w: 2}
    for t in (0, 1, 2, 3, -1):
        print('rank P(%s) =' % t, P.subs(pt).subs(lam, t).rank())
        assert P.subs(pt).subs(lam, t).rank() == 2
    print('PASS: mixed block (5a) forces z=xy, (5b) holds on the gate')


if __name__ == '__main__':
    main()
