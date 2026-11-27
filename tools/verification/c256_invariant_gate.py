"""Exact test: the exact invariant-plane gate fails (5b) (attempt 256).

n=7, p=1, q=3.  S=span{e5,e6,e7}, Q=span{e1,e2,e3,e4}.
A acts on Q as diag(1,1,2,2), on S as e5 -> e5+e7 (so CA=e5), e6 -> 0, e7 -> 0.
A(S) is not contained in S (e5 -> e5+e7 is in S actually; lift offset is zero here).
L0=e6, C=e7, and L=[L0; e1; e3] spans an invariant mixed plane U=span{e1,e3}.

Then (5a) holds, but at lambda=1 or 2 the pencil drops rank, so (5b) fails.

Run: python tools/verification/c256_invariant_gate.py
"""
import sympy as sp

lam = sp.symbols('lam')


def build():
    n = 7
    A = sp.zeros(n, n)
    A[0, 0] = 1
    A[1, 1] = 1
    A[2, 2] = 2
    A[3, 3] = 2
    A[4, 4] = 1
    A[6, 4] = 1          # CA = e5
    C = sp.Matrix([[0, 0, 0, 0, 0, 0, 1]])
    L0 = sp.Matrix([[0, 0, 0, 0, 0, 1, 0]])
    return A, C, L0


def check(L0):
    A, C, _ = build()
    l1 = sp.Matrix([[1, 0, 0, 0, 0, 0, 0]])
    l2 = sp.Matrix([[0, 0, 1, 0, 0, 0, 0]])
    L = sp.Matrix.vstack(L0, l1, l2)
    CA = C * A
    S = sp.Matrix.vstack(L0, CA, C)
    base = sp.Matrix.vstack(L, CA, C)
    full = sp.Matrix.vstack(L * A, L, CA, C)
    print('L0 =', L0)
    print('rank S =', S.rank(), 'rank[LA;L;CA;C] =', full.rank(), 'rank[L;CA;C] =', base.rank())
    assert S.rank() == 3
    assert full.rank() == base.rank(), '(5a) should hold for the invariant plane'

    K = sp.Matrix.vstack(C, CA).nullspace()
    N = sp.Matrix.hstack(*K)
    H = sp.expand(L * N)
    HA = sp.expand(L * A * N)
    P = sp.expand(lam * H - HA)
    print('rank H =', H.rank())
    for t in (0, 1, 2, 3):
        r = P.subs(lam, t).rank()
        print('  rank P(%s) = %s' % (t, r))
        if t in (1, 2):
            assert r < H.rank(), 'expected a drop at eigenvalue %s' % t


def main():
    A, C, L0 = build()
    check(L0)                 # L0=e6: H has rank 3
    print('PASS: exact invariant-plane realisation satisfies (5a) but fails (5b)')


if __name__ == '__main__':
    main()
