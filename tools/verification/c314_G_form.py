"""G = FX formulation check (attempt 314).

For 244 data: H=XB, HA=FH, G=FX => HA=GB and
rank P(lambda) = rank((lambda X - G) B).

Run: python tools/verification/c314_G_form.py
"""
import sympy as sp

lam = sp.symbols('lam')


def main():
    H = sp.Matrix([[0, 0, 1], [1, 2, 0], [3, 6, 1]])
    HA = sp.Matrix([[0, 0, 0], [3, 6, 1], [3, 6, 3]])
    omega = 2
    X = H[:, [0, 2]]
    B = X.pinv() * H
    F = HA * H.pinv()
    G = sp.simplify(F * X)
    print('G =', G)
    assert sp.simplify(G * B - HA) == sp.zeros(*HA.shape)
    assert sp.simplify(F * H - HA) == sp.zeros(*HA.shape)

    P = sp.expand(lam * H - HA)
    Q = sp.expand((lam * X - G) * B)
    for t in (0, 1, 2, 3):
        r1 = P.subs(lam, t).rank()
        r2 = Q.subs(lam, t).rank()
        print('lambda=%s: rank P=%s, rank Q=%s' % (t, r1, r2))
        assert r1 == r2
    print('PASS: G=FX, HA=GB, rank P = rank((lambda X - G)B)')


if __name__ == '__main__':
    main()
