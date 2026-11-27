"""Compressed q=4 rank-one gate with BOTH (5a) and (5b) (attempt 281).

H0 = [e1;e2], Y supported on e3,e4, det(Z)=0 is the gate.
Fixed block HA0 = swap(H0); free block HA = [S | 2Y + T] with
S = I_2 and T = [[0,0],[r11,r12]] (the second row of T is the first row of Y),
so every free HA row lies in row(H).

Checks:
- rank H = 3 on the gate (Z nonzero);
- rank[H;HA] = 3 (so (5a) holds);
- det P = (lam-2)^2(lam-1)(lam+1)*det(Z), hence det P = 0 on the gate;
- gcd of the 3x3 minors of P is 1 (so (5b) holds);
- rank P(lam) = 3 at several sample lambdas.

Run: python tools/verification/c281_q4_gate.py
"""
import itertools

import sympy as sp

lam, r11, r12, r21, r22 = sp.symbols('lam r11 r12 r21 r22')


def main():
    H = sp.Matrix([[1, 0, 0, 0],
                   [0, 1, 0, 0],
                   [0, 0, r11, r12],
                   [0, 0, r21, r22]])
    M = sp.Matrix([[0, 1], [1, 0]])
    Y = sp.Matrix([[r11, r12], [r21, r22]])
    S = sp.eye(2)
    T = sp.Matrix([[0, 0], [r11, r12]])
    H0 = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0]])
    HA = sp.Matrix.vstack(M * H0, sp.Matrix.hstack(S, 2 * Y + T))

    pt = {r11: 1, r12: 2, r21: 3, r22: 6}
    Hp, HAp = H.subs(pt), HA.subs(pt)
    print('rank H =', Hp.rank(), 'rank[H;HA] =', sp.Matrix.vstack(Hp, HAp).rank())
    assert Hp.rank() == 3
    assert sp.Matrix.vstack(Hp, HAp).rank() == 3

    P = sp.expand(lam * H - HA)
    det = sp.factor(P.det())
    print('det P =', det)
    assert sp.factor(sp.expand(det.subs({r11: 1, r22: r12 * r21}))) == 0

    for t in (0, 1, 2, 3, -1):
        r = P.subs(pt).subs(lam, t).rank()
        print('rank P(%s) =' % t, r)
        assert r == 3

    mins = []
    for rs in itertools.combinations(range(4), 3):
        for cs in itertools.combinations(range(4), 3):
            m = sp.expand(P.extract(rs, cs).det())
            if m != 0:
                mins.append(m)
    g = mins[0]
    for m in mins[1:]:
        g = sp.gcd(g, m)
    print('number of nonzero 3x3 minors =', len(mins), '; gcd =', sp.factor(g))
    assert sp.degree(sp.factor(g), lam) == 0
    print('PASS: compressed q=4 gate satisfies (5a) and (5b)')


if __name__ == '__main__':
    main()
