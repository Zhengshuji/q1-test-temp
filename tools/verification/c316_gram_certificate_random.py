#!/usr/bin/env python3
"""Exact checks for the Gram-Bezout certificate on random polynomial families.

For random real polynomials f_i of degree <= omega this script checks:

  * if the f_i have no common complex root, then e0 is in row(B) and the
    system B^T B x = e0 is consistent;
  * if the f_i have a common root, then e0 is not in row(B).

The matrix B is built by the shifted-coefficient indexing used in the paper.
This is finite exact verification, not a proof.
"""

from __future__ import annotations

import random

import sympy as sp

LAM = sp.symbols("lam")


def random_poly(omega: int, rng: random.Random):
    deg = rng.randint(1, omega)
    coeffs = [rng.randint(-3, 3) for _ in range(deg)] + [rng.choice([-2, -1, 1, 2])]
    return sum(c * LAM**k for k, c in enumerate(coeffs))


def certificate_matrix(fs, omega: int):
    rows = []
    for f in fs:
        p = sp.Poly(sp.expand(f), LAM)
        coeff = [p.coeff_monomial(LAM**k) for k in range(2 * omega + 1)]
        for j in range(omega):
            rows.append([coeff[t - j] if 0 <= t - j < len(coeff) else 0 for t in range(2 * omega)])
    return sp.Matrix(rows)


def rank(M):
    return M.rank()


def main() -> None:
    rng = random.Random(20261111)
    positive = 0
    negative = 0
    for trial in range(500):
        omega = rng.choice([2, 3])
        s = rng.randint(2, 5)
        fs = [random_poly(omega, rng) for _ in range(s)]
        g = sp.gcd_list(fs)
        B = certificate_matrix(fs, omega)
        e0 = sp.Matrix([1] + [0] * (2 * omega - 1))
        aug = B.T.row_join(e0)
        in_row = rank(aug) == rank(B.T)

        if sp.degree(sp.Poly(g, LAM)) == 0:
            if not in_row:
                print(f"FALSE NEGATIVE trial {trial}: {fs}")
                raise SystemExit(1)
            gram = B.T * B
            sol = sp.linsolve((gram, e0))
            if sol is sp.EmptySet:
                print(f"GRAM SYSTEM FAILED trial {trial}: {fs}")
                raise SystemExit(1)
            positive += 1
        else:
            if in_row:
                print(f"FALSE POSITIVE trial {trial}: {fs}, gcd={g}")
                raise SystemExit(1)
            negative += 1

    print(f"PASS: {positive} coprime families (certificate exists), {negative} common-root families (no certificate)")


if __name__ == "__main__":
    main()
