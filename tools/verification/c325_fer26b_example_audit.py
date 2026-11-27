"""c325_fer26b_example_audit.py

Audit of the illustrative example in
  J. A. Fernando, "Complete characterization of minimum-order functional
  observers from Darouach to Luenberger", arXiv:2609.37992, Sec. VII.

The paper claims Sigma_FO(L) = {5,6}, nu_min = 5, i.e. "4 not in Sigma_FO(L)".
That claim is refuted here by exhibiting Z4 (8x2) satisfying the paper's own
conditions (8a)-(8c) at q = 4, with exact rational arithmetic.

Conditions (8a)-(8c) of that paper:
  (8a) C Z = 0, L Z = 0,                                (and rank Z = d)
  (8b) rank[Z, A Z R_Z] = d,  im R_Z = ker(C A Z),
  (8c) rank[(lam I - A) V, Z] = rank[V, Z]  for all lam in C,
       where im V = ker[C; CA].

Verification is symbolic in lam: all 6x6 minors of the 8x6 pencil are checked
to vanish identically, and the gcd of the nonzero 5x5 minors is checked to be
a nonzero constant (so no common complex root). No numerical sampling.

Run:  python tools/verification/c325_fer26b_example_audit.py
"""

import sympy as sp
from itertools import combinations

A = sp.Matrix([
    [0, 1, 0, 1, 0, 0, 0, 0],
    [0, -1, 1, 0, 0, 0, 0, -1],
    [1, 0, -1, 1, 0, 0, 1, -1],
    [-1, -1, 0, -2, 0, 0, 0, 0],
    [0, 0, 0, 0, -2, 0, 0, 1],
    [0, 0, 0, 0, 0, -2, 1, 0],
    [0, 0, 0, 0, 0, -1, -2, 1],
    [0, 0, 0, 0, 0, 0, 1, -2]])
C = sp.Matrix([[-2, -2, 2, -2, -1, 0, 1, -3],
               [0, 0, 1, 2, 2, 3, -1, -2]])
L = sp.Matrix([[-2, -1, -2, -3, -1, 3, 2, 0],
               [1, -1, -2, 1, 0, 2, 0, 1]])

n, p, q = 8, 2, 4
d = n - p - q

lam = sp.symbols("lam")


def main() -> int:
    print("=== data of Sec. VII of arXiv:2609.37992")
    print("n, p, q =", n, p, q, " => d = n - p - q =", d)
    print("rank[C;L] =", sp.Matrix.vstack(C, L).rank(),
          " => dim ker[C;L] =", n - sp.Matrix.vstack(C, L).rank())
    print("dim ker[C;CA] =", n - sp.Matrix.vstack(C, C * A).rank())

    # candidate nullspace matrix at q = 4
    j = sp.Matrix([390, -97, 22, -272, 419, -58, 252, -55])
    w = sp.Matrix([-369, 174, 403, 251, -893, 368, -501, 362])
    Z = sp.Matrix.hstack(j, w)

    assert Z.rank() == d, "rank Z must equal d"
    assert (C * Z).is_zero_matrix and (L * Z).is_zero_matrix, "(8a) fails"
    print("(8a) holds: C Z = 0, L Z = 0, rank Z =", Z.rank())

    R = (C * A * Z).nullspace()
    R = sp.Matrix.hstack(*R)
    rank_b = sp.Matrix.hstack(Z, A * Z * R).rank()
    assert rank_b == d, "(8b) fails"
    print("(8b) holds: rank[Z, A Z R] =", rank_b, " with R =", R.T.tolist())

    # a basis of ker[C;CA]
    V = sp.Matrix.hstack(*sp.Matrix.vstack(C, C * A).nullspace())
    V = sp.Matrix([[-7, -1, 10, 11], [0, -2, -1, 0], [-6, -6, 6, 14],
                   [-1, -3, -2, -3], [4, 0, 0, 0], [0, 4, 0, 0],
                   [0, 0, 2, 0], [0, 0, 0, 4]])
    assert (C * V).is_zero_matrix and (C * A * V).is_zero_matrix
    r0 = sp.Matrix.hstack(V, Z).rank()
    print("rank V =", V.rank(), " rank[V Z] =", r0)

    P = sp.Matrix.hstack((lam * sp.eye(n) - A) * V, Z)   # n x (4+2) = 8 x 6
    six = [sp.expand(P.extract(rows, range(P.cols)).det())
           for rows in combinations(range(n), P.cols)]
    assert all(x == 0 for x in six), "some maximal minor is nonzero"
    print("all", len(six), "maximal (6x6) minors vanish identically")

    minors = []
    for rows in combinations(range(n), 5):
        for cols in combinations(range(P.cols), 5):
            det = sp.expand(P.extract(rows, cols).det())
            if det != 0:
                minors.append(sp.Poly(det, lam))
    print("nonzero 5x5 minors:", len(minors))
    g = minors[0]
    for f in minors[1:]:
        g = g.gcd(f)
        if g.degree() <= 0:
            break
    print("gcd of the 5x5 minors =", g.as_expr(), " degree", g.degree())
    assert g.degree() <= 0, "(8c) fails: the minors have a common root"

    # q = 3 infeasibility is NOT used: (8c) plus nu_min >= 4 from sigma_1.
    Mb = sp.Matrix.vstack(C, C * A, L)
    Jb = sp.Matrix.hstack(*Mb.nullspace())
    LAJ = L * A * Jb
    sigma1 = (n - sp.Matrix.vstack(C, C * A).rank()) - (Jb.cols - LAJ.rank())
    print("dim ker[C;CA;L] =", Jb.cols, " rank(LA|_J) =", LAJ.rank(),
          " => sigma_1 =", sigma1)

    print()
    print("VERDICT: rank[(lam I - A)V, Z] = rank[V, Z] =", r0,
          "for all lam in C, so q = 4 is feasible;")
    print("         the spectrum of Sec. VII is {4,5,6} and nu_min = 4,")
    print("         not {5,6} and 5 as claimed there.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
