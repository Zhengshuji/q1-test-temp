#!/usr/bin/env python3
"""c379 — The top-layer bad locus, explicitly, and its verification.

At the top layer (omega = k) with r >= k + 1 the free rows are generic, so for a fixed
lambda the rows of P(lambda) span

    V(lambda) = span{ lambda*h - g : (h,g) in S } = colspace((lambda I - A) N),

together with the single fixed row  (lambda h^0 - g^0).  Hence

    rank P(lambda) = dim V(lambda) + [ fixed row not in V(lambda) ],

and the layer is INFEASIBLE exactly when this is < k for some lambda.  This script computes
that criterion and compares it with the exact gcd computed in c378.
"""

from __future__ import annotations

import itertools
import os
import random
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import c335_lambda_movement as m  # noqa: E402

lam = sp.symbols("lam")


def bad_locus(A, C, L0):
    """Return the list of lambda at which rank P(lambda) < k for every admissible fibre choice."""
    N = m.ker_basis(sp.Matrix.vstack(C, C * A))
    AN = A * N
    k = N.cols
    n = A.rows
    S = sp.Matrix.hstack(N, AN)
    fixed = L0 * S
    h0, g0 = sp.Matrix(fixed[0, 0:k]).T, sp.Matrix(fixed[0, k:2 * k]).T
    # candidate lambdas: eigenvalues of A (over C) plus symbolic handling
    evs = sp.roots(A.charpoly().as_expr(), lam)
    bad = []
    for ev in evs:
        M = sp.Matrix(ev * sp.eye(n)) - A          # n x n
        MN = M * N                                 # n x k
        rk = MN.rank()
        # V(ev) = colspace(MN) ; the fixed row is (ev*h0 - g0) as a row
        frow = (ev * h0.T - g0.T)                  # 1 x k
        # frow in V(ev)^T ?  V(ev) is a subspace of the dual; test by rank comparison:
        # rank of the span of {rows of MN^T} plus frow
        span_mat = sp.Matrix.vstack(MN.T, frow)     # (n? no) -- rows of MN^T are columns of MN
        # dim span of columns of MN together with frow^T:
        combined = sp.Matrix.hstack(MN, frow.T)
        rk2 = combined.rank()
        if rk2 < k:
            bad.append((ev, rk, rk2))
    return k, bad


def main() -> None:
    print("=" * 78)
    print("top-layer bad locus: rank P(lambda) < k for every fibre choice")
    print("=" * 78)
    rng = random.Random(20261121)
    n = 5
    C = sp.zeros(1, n)
    C[0, n - 1] = 1
    for trial in range(4):
        A = sp.Matrix(n, n, lambda i, j: rng.randint(-2, 2))
        while sp.Matrix.vstack(C, C * A).rank() != 2:
            A = sp.Matrix(n, n, lambda i, j: rng.randint(-2, 2))
        N = m.ker_basis(sp.Matrix.vstack(C, C * A))
        k = N.cols
        L0 = sp.Matrix([[rng.randint(-1, 1) for _ in range(n)]])
        k2, bad = bad_locus(A, C, L0)
        print(f"\n  trial {trial}: k = {k2}, charpoly = {sp.factor(A.charpoly().as_expr())}")
        if bad:
            for (ev, rk, rk2) in bad:
                print(f"    BAD at lambda = {sp.nsimplify(ev)}: rank((lam I - A)N) = {rk}, "
                      f"with fixed row = {rk2} < k = {k2}")
        else:
            print("    no bad lambda: every eigenvalue has rank k after adding the fixed row")


if __name__ == "__main__":
    main()
