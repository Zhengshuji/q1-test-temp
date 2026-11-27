"""Spectral polarity checks for Route B (attempt 269).

1. q=2, omega=1: H rank 1 => P(lambda)=(lambda I - F)H has rank <=1 for every
   lambda, so (5b) is automatic regardless of F.
2. q=3, omega=2: (5b) fails at an eigenvalue lambda0 iff im H contains an
   eigenvector of F for lambda0.

Run: python tools/verification/c269_spectral_polarity.py
"""
import random

import sympy as sp

lam = sp.symbols('lam')


def random_matrix(rng, rows, cols):
    return sp.Matrix([[rng.randint(-2, 2) for _ in range(cols)] for _ in range(rows)])


def main():
    rng = random.Random(269)

    # q=2, omega=1: automatic
    for trial in range(5):
        F = random_matrix(rng, 2, 2)
        u = random_matrix(rng, 2, 1)
        v = random_matrix(rng, 1, 3)
        H = u * v
        assert H.rank() <= 1
        P = sp.expand(lam * H - F * H)
        ranks = [P.subs(lam, t).rank() for t in range(-3, 4)]
        print('q=2 trial', trial, 'rank H', H.rank(), 'P ranks', ranks)
        assert max(ranks) <= 1

    # q=3, omega=2: drop iff eigenvector in im H
    for trial in range(5):
        F = sp.diag(0, 1, 2)  # distinct eigenvalues
        # plane im H = span{e1, e2}: contains e1,e2 -> drops at 0,1
        H = sp.Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
        P = sp.expand(lam * H - F * H)
        ranks = [P.subs(lam, t).rank() for t in (0, 1, 2, 3)]
        print('q=3 trial', trial, 'im H=e1,e2; P ranks at 0,1,2,3 =', ranks)
        assert ranks[0] < 2 and ranks[1] < 2 and ranks[3] == 2

        # plane avoiding all three eigenlines: span{e1+e3, e2+e3}
        # im H = column space of H
        H2 = sp.Matrix([[1, 0], [0, 1], [1, 1]])
        P2 = sp.expand(lam * H2 - F * H2)
        ranks2 = [P2.subs(lam, t).rank() for t in (0, 1, 2, 3)]
        print('  avoiding plane; P ranks =', ranks2)
        assert all(r == 2 for r in ranks2)

    print('PASS: q=2 omega=1 is automatic; q=3 drop is eigenvector containment')


if __name__ == '__main__':
    main()
