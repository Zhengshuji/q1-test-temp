"""Direct sum of two nonzero gadgets (attempt 297).

Block diagonal of two copies of the 296 gadget:
  q=4, n=6, p=2, k=2, omega=2.
  (5b) <=> f1 != 0 AND f2 != 0.

Run: python tools/verification/c297_direct_sum_gadgets.py
"""
import sympy as sp

lam, f1, f2 = sp.symbols('lam f1 f2')


def block_diag(*blocks):
    return sp.diag(*blocks)


def main():
    A1 = sp.Matrix([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
    C1 = sp.Matrix([[0, 0, 1]])
    L01 = sp.Matrix([[1, 0, 0]])

    A = block_diag(A1, A1)
    C = block_diag(C1, C1)
    L0 = block_diag(L01, L01)
    R = block_diag(sp.Matrix([[0, f1, 0]]), sp.Matrix([[0, f2, 0]]))
    N = block_diag(sp.Matrix([[1], [0], [0]]), sp.Matrix([[1], [0], [0]]))

    CA = C * A
    print('C =', C)
    print('CA =', CA)
    # kernel of [C;CA] = span(e1, e4)
    x = sp.Matrix(sp.symbols('x1:7'))
    eqs = list(C * x) + list(CA * x)
    sol = sp.solve(eqs, list(x), dict=True)
    print('K0 solution =', sol)
    # expected basis
    Nexp = sp.zeros(6, 2)
    Nexp[0, 0] = 1
    Nexp[3, 1] = 1
    assert sp.Matrix.hstack(N, Nexp).rank() == 2

    L = sp.Matrix.vstack(L0, R)
    H = sp.expand(L * N)
    HA = sp.expand(L * A * N)
    print('H =', H, '; rank H =', H.rank())
    print('HA =', HA)
    assert H.rank() == 2

    # (5a) for all combos
    for v1 in (0, 1, 2):
        for v2 in (0, 1):
            Hv = H.subs({f1: v1, f2: v2})
            HAv = HA.subs({f1: v1, f2: v2})
            assert sp.Matrix.vstack(Hv, HAv).rank() == Hv.rank() == 2
    print('(5a): rank[H;HA] = rank H = 2 for all f1,f2')

    P = sp.expand(lam * H - HA)
    print('P =', P)
    for v1, v2 in ((0, 0), (1, 0), (0, 1), (1, 1), (2, 3)):
        ranks = [P.subs({f1: v1, f2: v2, lam: t}).rank() for t in (0, 1, 2, -1)]
        print('f=(%s,%s): ranks =' % (v1, v2), ranks)
        if v1 != 0 and v2 != 0:
            assert all(r == 2 for r in ranks)
        else:
            assert min(ranks) < 2
    print('PASS: direct sum gives (5b) <=> f1 != 0 AND f2 != 0')


if __name__ == '__main__':
    main()
