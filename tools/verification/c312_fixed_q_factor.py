"""Fixed-q factorization sanity check (attempt 312).

For a feasible small instance (244 data):
  H = X B with B_J = I, H_A = F H = F X B,
  rank P(lambda) = rank((lambda I - F) X).

Run: python tools/verification/c312_fixed_q_factor.py
"""
import itertools

import sympy as sp

lam = sp.symbols('lam')


def main():
    H = sp.Matrix([[0, 0, 1], [1, 2, 0], [3, 6, 1]])
    HA = sp.Matrix([[0, 0, 0], [3, 6, 1], [3, 6, 3]])
    q, k = H.shape
    omega = H.rank()
    print('q,k,omega =', q, k, omega)
    assert omega == 2

    # choose pivot columns
    J = None
    for cols in itertools.combinations(range(k), omega):
        Xc = H[:, list(cols)]
        if Xc.rank() == omega:
            J = list(cols)
            X = Xc
            break
    print('pivot J =', J)
    B = X.pinv() * H
    print('B =', B)
    print('B_J =', B[:, J])
    assert sp.simplify(B[:, J] - sp.eye(omega)) == sp.zeros(omega, omega)

    # F with HA = F H
    F = HA * H.pinv()
    print('F =', F)
    print('F H - HA =', sp.simplify(F * H - HA))
    assert sp.simplify(F * H - HA) == sp.zeros(q, k)
    assert sp.simplify(X * B - H) == sp.zeros(q, k)

    P = sp.expand(lam * H - HA)
    Q = sp.expand((lam * sp.eye(q) - F) * X)
    for t in (0, 1, 2, 3):
        r1 = P.subs(lam, t).rank()
        r2 = Q.subs(lam, t).rank()
        print('lambda=%s: rank P=%s, rank Q=%s' % (t, r1, r2))
        assert r1 == r2
    print('PASS: H=XB, B_J=I, H_A=FH, rank P = rank((lambda I-F)X)')


if __name__ == '__main__':
    main()
