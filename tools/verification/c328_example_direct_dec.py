"""c328_example_direct_dec.py

Direct test of *our* criteria on the order-4 observer matrix of the example of
arXiv:2609.37992 Sec. VII.  No use of that paper's (8a)-(8c), no chart
enumeration, no Z: we simply exhibit L = [L0; R] with 4 rows and check

  (5a)  rank[LA; L; CA; C] = rank[L; CA; C],
  (5b)  rank[lam L - LA; CA; C] = rank[L; CA; C]  for all lam in C,

the second by the gcd of the maximal minors of the pencil (exact, no sampling).
This is what DEC(4) computes on that instance.
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
L0 = sp.Matrix([[-2, -1, -2, -3, -1, 3, 2, 0],
                [1, -1, -2, 1, 0, 2, 0, 1]])

R = sp.Rational
Rrows = sp.Matrix([
    [R(-42919, 32067), R(-55096, 10689), 1, 0, 0, 0, 0, 0],
    [R(3283, 4581), R(118, 1527), 0, 1, 0, 0, 0, 0]])

L = sp.Matrix.vstack(L0, Rrows)      # q = 4 rows, first two are L0
lam = sp.symbols("lam")


def main() -> int:
    n, q = 8, L.rows
    print("q =", q, " rows in L;  first two rows equal L0:", L[:2, :] == L0)

    stacked = sp.Matrix.vstack(C, C * A)          # J
    left = sp.Matrix.vstack(L, C, C * A)          # [L; CA; C]
    left_a = sp.Matrix.vstack(L * A, L, C, C * A)  # [LA; L; CA; C]
    r_ref = left.rank()
    print("(5a): rank[L;CA;C] =", r_ref, " rank[LA;L;CA;C] =", left_a.rank(),
          " equal:", left_a.rank() == r_ref)

    # (5b): pencil  lam * L - L * A  stacked with [CA; C]
    P = sp.Matrix.hstack(lam * L - L * A, sp.zeros(q, 0))
    P = sp.Matrix.vstack(lam * L - L * A, C, C * A)     # (q + 2p) x n
    m, nn = P.shape
    print("pencil block is", m, "x", nn, ";  reference rank", r_ref)
    size = r_ref
    minors = []
    for rows in combinations(range(m), size):
        for cols in combinations(range(nn), size):
            det = sp.expand(P.extract(rows, cols).det())
            if det != 0:
                minors.append(sp.Poly(det, lam))
    print("nonzero", size, "x", size, "minors:", len(minors))
    assert minors, "(5b) fails: every maximal minor vanishes"
    # larger minors must vanish, otherwise the reference rank is not maximal
    for rows in combinations(range(m), min(size + 1, m)):
        for cols in combinations(range(nn), min(size + 1, m)):
            assert sp.expand(P.extract(rows, cols).det()) == 0, \
                "a minor larger than the reference rank survives"
    print("all larger minors vanish, so rank <= ", size)
    g = minors[0]
    for f in minors[1:]:
        g = g.gcd(f)
        if g.degree() <= 0:
            break
    print("gcd =", sp.factor(g.as_expr()), " degree", g.degree())
    ok_b = (g.degree() <= 0)
    print("(5b): no common complex root, hence rank is constant:", ok_b)

    print()
    print("VERDICT: DEC at q =", q, "accepts this instance" if ok_b else "rejects")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
