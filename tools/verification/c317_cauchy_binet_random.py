#!/usr/bin/env python3
"""Exact checks for the Cauchy-Binet / shifted-index compression.

For random linear pencils P(lambda) = lambda H - H_A this script checks:

  * K(lambda,mu) = sum_{|J|=omega} det(P(lambda)[:,J]^T P(mu)[:,J])
    equals sum_i f_i(lambda) f_i(mu), where f_i are the maximal minors;
  * the coefficient identity
    (B^T B)_{t,t'} = sum_j S_{t-j,t'-j}.

This is finite exact verification, not a proof.
"""

from __future__ import annotations

import itertools
import random

import sympy as sp

LAM, MU = sp.symbols("lam mu")


def random_pencil(q: int, k: int, rng: random.Random):
    return sp.Matrix(q, k, lambda i, j: rng.randint(-2, 2) + rng.randint(-2, 2) * LAM)


def coeff_matrix(poly, var, n):
    p = sp.Poly(sp.expand(poly), var)
    return [p.coeff_monomial(var**i) for i in range(n)]


def main() -> None:
    rng = random.Random(20261112)
    checks = 0
    for trial in range(200):
        q, k = rng.choice([(3, 4), (4, 3), (4, 4), (5, 3)])
        omega = rng.choice([1, 2, 3])
        if omega > min(q, k):
            continue
        P = random_pencil(q, k, rng)
        cols_sets = list(itertools.combinations(range(k), omega))
        rows_sets = list(itertools.combinations(range(q), omega))

        # K(lambda,mu) via rectangular Cauchy-Binet (sum over column sets).
        K = 0
        for cols in cols_sets:
            A = P[:, cols]
            K += sp.expand((A.subs(LAM, LAM).T * A.subs(LAM, MU)).det())
        K = sp.expand(K)

        # sum over all maximal minors f_{I,J}(lambda) f_{I,J}(mu).
        R = 0
        minors = []
        for rows in rows_sets:
            for cols in cols_sets:
                f = sp.expand(P.extract(rows, cols).det())
                minors.append(f)
                R += sp.expand(f.subs(LAM, LAM) * f.subs(LAM, MU))
        R = sp.expand(R)
        if sp.simplify(K - R) != 0:
            print(f"CAUCHY-BINET FAILED trial {trial}")
            raise SystemExit(1)

        # B matrix by shifted coefficients.
        B = sp.zeros(omega * len(minors), 2 * omega)
        for i, f_expr in enumerate(minors):
            f = sp.Poly(sp.expand(f_expr), LAM)
            coeff = [f.coeff_monomial(LAM**a) for a in range(2 * omega + 1)]
            for j in range(omega):
                for t in range(2 * omega):
                    B[i * omega + j, t] = coeff[t - j] if 0 <= t - j < len(coeff) else 0

        # S_{a,b} coefficients of K.
        S = {}
        Kpoly = sp.Poly(K, LAM, MU)
        for a in range(2 * omega + 1):
            for b in range(2 * omega + 1):
                S[(a, b)] = Kpoly.coeff_monomial(LAM**a * MU**b)

        G = B.T * B
        for t in range(2 * omega):
            for tp in range(2 * omega):
                val = sum(S.get((t - j, tp - j), 0) for j in range(omega))
                if sp.simplify(G[t, tp] - val) != 0:
                    print(f"INDEX FAILED trial {trial} at ({t},{tp})")
                    raise SystemExit(1)
        checks += 1

    print(f"PASS: {checks} random pencils; Cauchy-Binet and shifted index both hold")


if __name__ == "__main__":
    main()
