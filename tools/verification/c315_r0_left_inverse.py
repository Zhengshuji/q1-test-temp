#!/usr/bin/env python3
"""Exact checks for the r=0 rectangular left-inverse construction.

For small random linear pencils Q(lambda) = lambda X - G (q x omega), this
script checks, over Q:

  * the maximal minors have gcd one;
  * Bezout multipliers of degree < omega exist;
  * the rectangular adjugate construction gives S Q = I;
  * deg S <= 2 omega - 2.

This is finite exact verification, not a proof.
"""

from __future__ import annotations

import itertools
import random

import sympy as sp

LAM = sp.symbols("lam")


def poly_degree(p):
    return sp.degree(sp.Poly(p, LAM))


def random_linear_pencil(q: int, omega: int, rng: random.Random):
    Q = sp.Matrix(q, omega, lambda i, j: rng.randint(-3, 3) + rng.randint(-3, 3) * LAM)
    return Q


def main() -> None:
    rng = random.Random(20261110)
    checked = 0
    for trial in range(300):
        q, omega = 4, 2
        Q = random_linear_pencil(q, omega, rng)
        row_sets = list(itertools.combinations(range(q), omega))
        minors = [sp.expand(Q.extract(rows, range(omega)).det()) for rows in row_sets]
        if all(sp.simplify(f) == 0 for f in minors):
            continue
        g = sp.gcd_list(minors)
        if sp.degree(sp.Poly(g, LAM)) != 0:
            continue

        # Unknowns: g_I = sum_{j<omega} c_{I,j} lam^j; equations: coeffs of
        # sum_I g_I f_I - 1, up to degree maxdeg.
        maxdeg = max(poly_degree(f) for f in minors) + omega - 1
        cols = []
        for rows in row_sets:
            f = Q.extract(rows, range(omega)).det()
            f = sp.Poly(sp.expand(f), LAM)
            for j in range(omega):
                p = sp.Poly(sp.expand(f.as_expr() * LAM**j), LAM)
                cols.append([p.coeff_monomial(LAM**k) for k in range(maxdeg + 1)])
        M = sp.Matrix(cols).T
        rhs = sp.Matrix([1] + [0] * maxdeg)
        sol = sp.linsolve((M, rhs))
        if sol is sp.EmptySet:
            print(f"NO BEZOUT at trial {trial}: {Q.tolist()}")
            raise SystemExit(1)
        sol = list(sol)[0]

        S = sp.zeros(omega, q)
        for idx, rows in enumerate(row_sets):
            f = sp.expand(Q.extract(rows, range(omega)).det())
            gI = sum(sol[idx * omega + j] * LAM**j for j in range(omega))
            adj = Q.extract(rows, range(omega)).adjugate()
            for a in range(omega):
                for b in range(omega):
                    S[a, rows[b]] += sp.expand(gI * adj[a, b])

        lhs = sp.expand(S * Q)
        if sp.simplify(lhs - sp.eye(omega)) != sp.zeros(omega, omega):
            print(f"SQ != I at trial {trial}: {Q.tolist()}")
            raise SystemExit(1)
        max_deg = max((poly_degree(sp.expand(S[i, j])) for i in range(omega) for j in range(q)), default=-1)
        if max_deg > 2 * omega - 2:
            print(f"DEGREE BOUND FAILED at trial {trial}: {max_deg}")
            raise SystemExit(1)
        checked += 1

    print(f"PASS: {checked} random full-row-rank pencils; SQ=I and deg S <= 2*omega-2")


if __name__ == "__main__":
    main()
