"""Full observer realization of the 2x1 nonzero gadget (attempt 296).

n=3, p=1, q=2, r0=1, r=1, k=1, omega=1.
A e1=e2, A e2=e3, A e3=0; C=e3^T; L0=e1^T; R(f)=(0,f,0).
Then H=(1,0)^T, HA=(0,f)^T, and (5b) <=> f != 0.

Run: python tools/verification/c296_nonzero_gadget_observer.py
"""
import sympy as sp

lam, f = sp.symbols('lam f')


def main():
    A = sp.Matrix([[0, 0, 0], [1, 0, 0], [0, 1, 0]])
    C = sp.Matrix([[0, 0, 1]])
    L0 = sp.Matrix([[1, 0, 0]])
    R = sp.Matrix([[0, f, 0]])
    N = sp.Matrix([[1], [0], [0]])

    # kernel of [C; CA]
    CA = C * A
    print('C =', C, '; CA =', CA, '; C*N =', C * N, '; CA*N =', CA * N)
    assert C * N == sp.zeros(1, 1)
    assert CA * N == sp.zeros(1, 1)
    # K0 = span(e1)
    x1, x2, x3 = sp.symbols('x1 x2 x3')
    x = sp.Matrix([[x1], [x2], [x3]])
    sol = sp.solve(list(C * x) + list(CA * x), [x1, x2, x3], dict=True)
    print('K0 equations solution =', sol)

    L = sp.Matrix.vstack(L0, R)
    H = sp.expand(L * N)
    HA = sp.expand(L * A * N)
    print('H =', H, '; HA =', HA)
    assert sp.simplify(H - sp.Matrix([[1], [0]])) == sp.zeros(2, 1)
    assert sp.simplify(HA - sp.Matrix([[0], [f]])) == sp.zeros(2, 1)

    # (5a): row(HA) subset row(H)
    for val in (0, 1, 2):
        Hv = H.subs(f, val)
        HAv = HA.subs(f, val)
        rH = Hv.rank()
        rS = sp.Matrix.vstack(Hv, HAv).rank()
        print('f=%s: rank H=%s, rank[H;HA]=%s' % (val, rH, rS))
        assert rH == 1 and rS == 1

    P = sp.expand(lam * H - HA)
    print('P =', P)
    for val in (0, 1, 2):
        ranks = [P.subs(f, val).subs(lam, t).rank() for t in (0, 1, 2, -1)]
        print('f=%s: ranks P at 0,1,2,-1 =' % val, ranks)
        if val == 0:
            assert ranks[0] == 0
        else:
            assert all(r == 1 for r in ranks)

    # per-row liftability: (H_i, HA_i) = row_i [N AN]
    AN = A * N
    M = sp.Matrix.hstack(N, AN)
    print('N =', N.T, '; AN =', AN.T, '; [N AN] =', M)
    for rowL, Hrow, HArow in ((L0, H[0, :], HA[0, :]), (R, H[1, :], HA[1, :])):
        pair = sp.Matrix.hstack(Hrow, HArow)
        assert sp.Matrix.vstack(M, pair).rank() == M.rank()
    print('PASS: full observer realization, (5b) <=> f != 0')


if __name__ == '__main__':
    main()
