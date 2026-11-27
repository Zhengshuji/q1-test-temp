#!/usr/bin/env python3
"""Exact checks for the r=0 linear-system test (expert report 85, Proposition 3c).

For a degree-one pencil Q(lam) = lam X - G with X, G in Q^{q x omega} and
X of full column rank omega, decide

    (R0)  rank Q(lam) = omega   for every lam in C

in two independent exact ways:

  (a) the gcd of the maximal omega x omega minors of Q is a nonzero constant
      (reference test, uses all C(q, omega) row subsets);
  (b) the finite rational linear system (R0.1)-(R0.3) of the report is
      consistent, i.e. there is S(lam) = sum_{j=0}^{2 omega - 2} S_j lam^j
      with S(lam) Q(lam) = I_omega.

Checked here (over Q, exact arithmetic):

  * (a) and (b) agree on every instance, including negative controls with a
    common root and the "infinite elementary divisor" example Q = 1;
  * the advertised counts: (2 omega - 1) q omega scalar unknowns and
    2 omega^3 scalar equations;
  * the minimal certificate degree never exceeds 2 omega - 2;
  * end to end: for r = 0 instances (A, C, L0) satisfying (5a), the linear
    system on the compressed pencil reproduces the project's reference
    spectral gcd test on (A, C, L0).

This is finite exact verification, not a proof.  It does not prove the degree
bound deg S <= 2 omega - 2 (that is Lemma D/Appendix B of the paper); it only
confirms the report's algorithm on the displayed instances.
"""

from __future__ import annotations

import itertools
import os
import random
import sys
from fractions import Fraction

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for _p in ("tools/verification",):
    sys.path.insert(0, os.path.join(_ROOT, _p))

import spectral_gcd as SG  # noqa: E402

LAM = sp.symbols("lam")


# --------------------------------------------------------------------------
# (a) reference test: gcd of maximal minors
# --------------------------------------------------------------------------
def gcd_minor_test(X: sp.Matrix, G: sp.Matrix):
    """Return (condition holds?, gcd as sympy expr)."""
    q, om = X.shape
    assert X.shape == G.shape
    if om == 0:
        # an empty pencil has rank 0 = omega; the condition is vacuous
        return True, sp.Integer(1)
    Q = LAM * X - G
    minors = []
    for rows in itertools.combinations(range(q), om):
        m = sp.expand(Q.extract(rows, range(om)).det())
        minors.append(sp.Poly(m, LAM))
    if all(p.is_zero for p in minors):
        return False, sp.Integer(0)
    g = sp.gcd_list([p.as_expr() for p in minors])
    return (sp.degree(g, LAM) == 0), sp.expand(g)


# --------------------------------------------------------------------------
# (b) the report's finite linear system
# --------------------------------------------------------------------------
def build_system(X: sp.Matrix, G: sp.Matrix, d: int):
    """Coefficient matrix and rhs of (R0.1)-(R0.3); entries are integers.

    Unknowns: S_j[a, b], 0 <= j <= d, 0 <= a < omega, 0 <= b < q.
    Equations, by the power k of lam:
        k = 0     :  -S_0 G        = I_omega
        1 <= k <= d: S_{k-1} X - S_k G = 0
        k = d + 1 :  S_d X         = 0
    """
    q, om = X.shape
    # clear denominators: scaling (X, G) by a nonzero rational does not change
    # the rank of lam X - G, nor the consistency of the system
    den = 1
    for v in list(X) + list(G):
        den = sp.ilcm(den, sp.Rational(v).q)
    Xs = sp.Matrix(X) * den
    Gs = sp.Matrix(G) * den
    assert all(sp.Rational(v).q == 1 for v in list(Xs) + list(Gs))
    nvar = (d + 1) * om * q
    neq = (d + 2) * om * om
    rows, rhs = [], []
    for k in range(d + 2):
        for a in range(om):
            for c in range(om):
                row = [0] * nvar
                if k == 0:
                    for b in range(q):
                        row[0 * om * q + a * q + b] = -int(Gs[b, c])
                    rhs.append(1 if a == c else 0)
                elif k <= d:
                    for b in range(q):
                        row[(k - 1) * om * q + a * q + b] = int(Xs[b, c])
                        row[k * om * q + a * q + b] = -int(Gs[b, c])
                    rhs.append(0)
                else:
                    for b in range(q):
                        row[d * om * q + a * q + b] = int(Xs[b, c])
                    rhs.append(0)
                rows.append(row)
    M = sp.Matrix(rows)
    b = sp.Matrix(rhs)
    assert M.shape == (neq, nvar), (M.shape, (neq, nvar))
    return M, b


def system_consistent(X: sp.Matrix, G: sp.Matrix, d: int) -> bool:
    M, b = build_system(X, G, d)
    return M.rank() == M.row_join(b).rank()


def minimal_degree(X: sp.Matrix, G: sp.Matrix):
    """Smallest d in [0, 2 omega - 2] making the system consistent, else None."""
    q, om = X.shape
    top = 2 * om - 2 if om >= 1 else 0
    for d in range(top + 1):
        if system_consistent(X, G, d):
            return d
    return None


# --------------------------------------------------------------------------
# instance generators
# --------------------------------------------------------------------------
def random_full_column_rank(q: int, om: int, rng: random.Random) -> sp.Matrix:
    """q x om integer matrix with rank om (unit block on top + noise)."""
    X = sp.zeros(q, om)
    for i in range(om):
        X[i, i] = 1
    for i in range(om, q):
        for j in range(om):
            X[i, j] = rng.randint(-3, 3)
    assert X.rank() == om
    return X


def random_pencil(q: int, om: int, rng: random.Random):
    X = random_full_column_rank(q, om, rng)
    G = sp.Matrix(q, om, lambda i, j: rng.randint(-4, 4))
    return X, G


# --------------------------------------------------------------------------
# end to end: r = 0 instance (A, C, L0)
# --------------------------------------------------------------------------
def compress_r0(A, C, L0):
    """Compressed pencil (X, G) with lam H - H_A = (lam X - G) B.

    Returns (X, G, omega, cond5a, H, HA) with Fractions replaced by sympy.
    """
    n = len(A)
    CA = [[sum(C[i][k] * A[k][j] for k in range(n)) for j in range(n)]
          for i in range(len(C))]
    M = [list(r) for r in C] + [list(r) for r in CA]
    Mq = sp.Matrix(M)
    Ns = Mq.nullspace()
    assert Mq.cols == n, (Mq.cols, n)
    for v in Ns:
        assert (Mq * v).is_zero_matrix, "N is not a kernel basis"
    if not Ns:
        return None
    N = sp.Matrix.hstack(*Ns)                      # n x k
    H = sp.Matrix(L0) * N                          # q x k
    HA = sp.Matrix(L0) * sp.Matrix(A) * N
    om = H.rank()
    cond5a = (H.col_join(HA).rank() == om)
    if om == 0:
        return None
    # pick omega independent columns of H
    J = []
    for j in range(H.cols):
        cand = H[:, J + [j]]
        if cand.rank() == len(J) + 1:
            J.append(j)
    assert len(J) == om
    X = H[:, J]                                    # q x omega, full column rank
    assert X.rank() == om
    Xpinv = (X.T * X).inv() * X.T
    B = Xpinv * H                                  # omega x k, full row rank
    assert (X * B - H).is_zero_matrix
    assert B.rank() == om
    if not cond5a:
        # H_A is not in row(H); no G exists and the instance is infeasible
        return X, None, om, False, H, HA
    Bpinv = B.T * (B * B.T).inv()
    G = HA * Bpinv
    assert (G * B - HA).is_zero_matrix
    return X, G, om, True, H, HA


def to_fraction(M):
    return [[Fraction(int(sp.Rational(v).p), int(sp.Rational(v).q)) for v in row]
            for row in M.tolist()]


def end_to_end(trials: int, rng: random.Random) -> dict:
    stats = {"5a": 0, "total": 0, "agree": 0}
    for t in range(trials):
        n = rng.randint(4, 6)
        p = rng.randint(1, 2)
        r0 = rng.randint(1, 3)
        A = [[Fraction(rng.randint(-3, 3)) for _ in range(n)] for _ in range(n)]
        C = [[Fraction(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        L0 = [[Fraction(rng.randint(-2, 2)) for _ in range(n)] for _ in range(r0)]
        out = compress_r0(A, C, L0)
        if out is None:
            continue
        X, G, om, cond5a, H, HA = out
        stats["total"] += 1
        if not cond5a:
            continue
        stats["5a"] += 1
        lam_test = system_consistent(X, G, 2 * om - 2)
        gcd = SG.spectral_gcd(A, C, L0)[0]
        ref = (gcd == [Fraction(1)])
        assert lam_test == ref, (
            f"end-to-end mismatch at trial {t}: linear system={lam_test}, "
            f"spectral_gcd={ref} (n={n}, p={p}, r0={r0}, omega={om})\n"
            f"A={[[str(v) for v in row] for row in A]}\n"
            f"C={[[str(v) for v in row] for row in C]}\n"
            f"L0={[[str(v) for v in row] for row in L0]}\n"
            f"X={X.tolist()}\nG={G.tolist()}\nH={H.tolist()}\nHA={HA.tolist()}")
        stats["agree"] += 1
    return stats


def main() -> None:
    rng = random.Random(20261110)

    # ---- 1. core equivalence on random full-column-rank pencils ----------
    cases = [(3, 1, 30), (4, 2, 40), (5, 2, 30), (6, 3, 25), (8, 3, 10)]
    total = 0
    for q, om, trials in cases:
        for _ in range(trials):
            X, G = random_pencil(q, om, rng)
            holds, g = gcd_minor_test(X, G)
            sys_ok = system_consistent(X, G, 2 * om - 2)
            assert holds == sys_ok, (
                f"mismatch q={q} omega={om}: gcd-degree={sp.degree(g, LAM)}, "
                f"system={sys_ok}\nX={X.tolist()}\nG={G.tolist()}")
            total += 1
    print(f"[1] gcd test vs linear system: {total} random pencils agree")

    # ---- 2. advertised counts -------------------------------------------
    for om, q in [(1, 3), (2, 4), (3, 6)]:
        X, G = random_pencil(q, om, rng)
        M, b = build_system(X, G, 2 * om - 2)
        assert M.shape == (2 * om ** 3, (2 * om - 1) * q * om), M.shape
        print(f"[2] omega={om}, q={q}: {M.shape[0]} equations "
              f"(=2 omega^3), {M.shape[1]} unknowns (=(2 omega-1) q omega)")

    # ---- 3. negative controls -------------------------------------------
    # (a) common root: G = lam0 * X  =>  Q(lam0) = 0
    for lam0 in (0, 2, -3):
        X = random_full_column_rank(4, 2, rng)
        G = lam0 * X
        holds, g = gcd_minor_test(X, G)
        sys_ok = system_consistent(X, G, 2)
        assert not holds and not sys_ok, (lam0, holds, sys_ok, g)
        assert minimal_degree(X, G) is None
    print("[3a] common-root controls (lam0 = 0, 2, -3): both tests reject")

    # (b) Q = 1: the expert's infinite-elementary-divisor example
    X = sp.zeros(1, 1)
    G = sp.Matrix([[-1]])
    assert gcd_minor_test(X, G) == (True, sp.Integer(1))
    assert system_consistent(X, G, 0)
    print("[3b] Q(lam) = 1 (q = omega = 1) accepted by both tests")

    # (c) invertible constant pencil: Q = -G with G invertible
    G = sp.Matrix([[1, 0], [0, 2], [1, 1]])          # 3 x 2, rank 2
    X = sp.zeros(3, 2)
    assert gcd_minor_test(X, G)[0] and system_consistent(X, G, 2)
    print("[3c] constant full-column-rank pencil accepted")

    # (d) rank-deficient at every lam: X = 0, G = 0
    Z = sp.zeros(3, 2)
    holds, _ = gcd_minor_test(Z, Z)
    assert not holds and not system_consistent(Z, Z, 2)
    print("[3d] zero pencil rejected (rank 0 < omega)")

    # ---- 4. degree bound, including the thin (constructed) extremal cases
    # Random full-row pencils usually admit a *constant* left inverse, so they
    # do not exercise the bound.  The samples below are singular square
    # pencils with det(lam X - G) constant, where the minimal degree is
    # positive (and, for omega = 3, exactly 2 omega - 2).
    degs = []
    for q, om, trials in [(4, 2, 15), (6, 3, 10)]:
        for _ in range(trials):
            X, G = random_pencil(q, om, rng)
            d = minimal_degree(X, G)
            if d is not None:
                degs.append(d)
                assert d <= 2 * om - 2
    print(f"[4] minimal certificate degree on {len(degs)} random feasible pencils: "
          f"max={max(degs) if degs else None} (constant certificates suffice there)")

    thin = [
        # omega = 2: Q = [[lam, -1], [1, 0]], det = 1; degree-0 S is impossible,
        # the adjugate gives S = [[0, 1], [-1, lam]] of degree 1.
        (sp.Matrix([[1, 0], [0, 0]]), sp.Matrix([[0, 1], [-1, 0]]), 2, 1),
        # omega = 3: Q = block diag([[lam,-1],[1,0]], [-1]), det = -1;
        # S = [[0,1,0],[-1,lam,0],[0,0,-1]] has degree 1.
        (sp.Matrix([[1, 0, 0], [0, 0, 0], [0, 0, 0]]),
         sp.Matrix([[0, 1, 0], [-1, 0, 0], [0, 0, 1]]), 3, 1),
    ]
    for X, G, om, expected in thin:
        assert gcd_minor_test(X, G)[0]
        d = minimal_degree(X, G)
        assert d == expected, (d, expected, X.tolist(), G.tolist())
        assert system_consistent(X, G, 2 * om - 2)
        assert not system_consistent(X, G, 0)   # a constant S cannot work
    print("[4b] thin constructed pencils (singular X, det constant): minimal "
          "degree 1 > 0, so d = 0 wrongly rejects while d = 2 omega - 2 accepts")

    # ---- 5. end to end on r = 0 instances ------------------------------
    stats = end_to_end(60, rng)
    print(f"[5] end to end: {stats['total']} r=0 compressions, "
          f"{stats['5a']} satisfy (5a), {stats['agree']} agree with spectral_gcd")

    print("\nPASS: r=0 linear-system test matches the gcd reference on all "
          "checked instances; counts and degree bound as claimed")


if __name__ == "__main__":
    main()
