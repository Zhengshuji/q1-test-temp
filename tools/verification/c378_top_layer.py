#!/usr/bin/env python3
"""c378 — The top layer omega = k, decided exactly.

At the top layer W = V (the whole compressed row space), so
    T_V = S,  compatibility is automatic,  rank completion is automatic for m >= 1,
and feasibility reduces to: the generic pencil built from the fixed pairs plus m generic
pairs from S has all its k x k minors coprime.

The test here is exact in the fibre parameters tau: the minors are formed symbolically and
their gcd is computed over Q(tau)[lam].  gcd = 1 means the top layer is active.
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


def minors_of(P, r):
    return [sp.expand(P.extract(list(rs), list(cs)).det())
            for rs in itertools.combinations(range(P.rows), r)
            for cs in itertools.combinations(range(P.cols), r)]


def gcd_all(polys):
    g = polys[0]
    for p in polys[1:]:
        g = sp.gcd(g, p)
        if sp.simplify(g).is_number:
            return sp.Integer(1)
    return g


def top_layer(A, C, L0, m_rows):
    """Exact: is the top layer (omega = k) active?  Returns (k, dim S, gcd, active)."""
    N = m.ker_basis(sp.Matrix.vstack(C, C * A))
    AN = A * N
    k = N.cols
    n = A.rows
    S = sp.Matrix.hstack(N, AN)
    # a basis of the row space S: rows of S span it; take independent rows
    basis = []
    cur = sp.zeros(0, 2 * k)
    for i in range(S.rows):
        cand = sp.Matrix.vstack(cur, S.row(i))
        if cand.rank() > cur.rank():
            cur = cand
            basis.append(S.row(i).T)
    Sbas = sp.Matrix.hstack(*basis) if basis else sp.zeros(2 * k, 0)   # 2k x dS
    dS = Sbas.cols
    fixed = L0 * S                                          # 1 x 2k
    taus = sp.symbols(f"t0:{m_rows * dS}")
    rowsH, rowsA = [], []
    for a in range(m_rows):
        coeff = [taus[a * dS + j] for j in range(dS)]
        vals = [sum(coeff[j] * Sbas[i, j] for j in range(dS)) for i in range(2 * k)]
        rowsH.append(sp.Matrix([vals[0:k]]))
        rowsA.append(sp.Matrix([vals[k:2 * k]]))
    H = sp.Matrix.vstack(sp.Matrix([list(fixed[0, 0:k])]), *rowsH)
    HA = sp.Matrix.vstack(sp.Matrix([list(fixed[0, k:2 * k])]), *rowsA)
    P = sp.Matrix(H.rows, H.cols, lambda i, j: lam * H[i, j] - HA[i, j])
    ms = [x for x in minors_of(P, k) if sp.simplify(x) != 0]
    if not ms:
        return k, dS, None, False
    g = gcd_all(ms)
    active = bool(sp.simplify(g).is_number or sp.Poly(g, lam).degree() == 0)
    return k, dS, sp.factor(g), active


def main() -> None:
    print("=" * 78)
    print("top layer omega = k: exact activity test (gcd over Q(tau)[lam])")
    print("=" * 78)
    rng = random.Random(20261121)
    for n, p in [(5, 1), (6, 1)]:
        C = sp.zeros(p, n)
        C[p - 1, n - 1] = 1
        for trial in range(4):
            A = sp.Matrix(n, n, lambda i, j: rng.randint(-2, 2))
            while sp.Matrix.vstack(C, C * A).rank() != 2 * p:
                A = sp.Matrix(n, n, lambda i, j: rng.randint(-2, 2))
            N = m.ker_basis(sp.Matrix.vstack(C, C * A))
            k = N.cols
            L0 = sp.Matrix([[rng.randint(-1, 1) for _ in range(n)]])
            for m_rows in (1, 2, 3):
                k2, dS, g, act = top_layer(A, C, L0, m_rows)
                tag = "ACTIVE" if act else "inactive"
                if g is None:
                    desc = "none (no nonzero k x k minor)"
                elif sp.simplify(g).is_number:
                    desc = "1 (coprime)"
                else:
                    desc = f"nonconstant of degree {sp.Poly(g, lam).degree(law) if False else sp.degree(g, lam)}"
                print(f"  n={n}, k={k2}, dim S={dS}, r={1+m_rows}: gcd={desc}  ->  {tag}")


if __name__ == "__main__":
    main()
