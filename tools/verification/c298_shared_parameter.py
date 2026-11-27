"""Shared-parameter direct sum (attempt 298).

Two 296 gadgets with f1=f2=f: (5b) <=> f != 0 (same as one gadget).

Run: python tools/verification/c298_shared_parameter.py
"""
import sympy as sp

lam, f = sp.symbols('lam f')


def main():
    A1 = sp.Matrix([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
    C1 = sp.Matrix([[0, 0, 1]])
    L01 = sp.Matrix([[1, 0, 0]])
    A = sp.diag(A1, A1)
    C = sp.diag(C1, C1)
    L0 = sp.diag(L01, L01)
    R = sp.diag(sp.Matrix([[0, f, 0]]), sp.Matrix([[0, f, 0]]))
    N = sp.diag(sp.Matrix([[1], [0], [0]]), sp.Matrix([[1], [0], [0]]))
    L = sp.Matrix.vstack(L0, R)
    H = sp.expand(L * N)
    HA = sp.expand(L * A * N)
    print('H =', H, '; HA =', HA)
    assert H.rank() == 2
    for val in (0, 1, 2):
        Hv, HAv = H.subs(f, val), HA.subs(f, val)
        assert sp.Matrix.vstack(Hv, HAv).rank() == 2
    P = sp.expand(lam * H - HA)
    for val in (0, 1, 2):
        ranks = [P.subs(f, val).subs(lam, t).rank() for t in (0, 1, 2, -1)]
        print('f=%s ranks =' % val, ranks)
        if val == 0:
            assert min(ranks) < 2
        else:
            assert all(r == 2 for r in ranks)
    print('PASS: shared-parameter direct sum is just a copy; (5b) <=> f != 0')


if __name__ == '__main__':
    main()
