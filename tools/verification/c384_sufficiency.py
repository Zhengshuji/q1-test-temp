#!/usr/bin/env python3
"""c384 — Sufficiency: if pi_1(T_W) = pi_2(T_W) = W then layer omega is feasible with 2*omega rows.

Construction: take omega admissible pairs (x_1,0),...,(x_omega,0) with x_i a basis of W, and
omega more pairs (0,y_1),...,(0,y_omega) with y_j a basis of W.  The pencil rows are
    lambda x_1, ..., lambda x_omega, -y_1, ..., -y_omega,
so P(lambda) = [lambda X ; -Y] with X, Y invertible, hence rank omega for every lambda.

The script checks this on the scaled shift family, where S = Q^{1 x 2k} and therefore
T_W = W + W for every W.
"""

from __future__ import annotations

import itertools
import os
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import c335_lambda_movement as m  # noqa: E402

lam = sp.symbols("lam")


def minors(P, r):
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


def check(A, C, W, omega, m_rows):
    N = m.ker_basis(sp.Matrix.vstack(C, C * A))
    AN = A * N
    k = N.cols
    n = A.rows
    Wp = m.ker_basis(W)
    Y = m.ker_basis(sp.Matrix.hstack(N * Wp, AN * Wp).T)   # T_W
    if Y.cols < 2 * omega:
        return None, Y.cols, None, "T_W too small"
    # choose 2*omega admissible rows: omega with y-part zero, omega with x-part zero
    basis = [Y[:, j].T for j in range(Y.cols)]
    picks = basis[:2 * omega]
    rowsH, rowsA = [], []
    for y in picks:
        h = (y * N)
        g = (y * AN)
        rowsH.append(sp.Matrix([[h[0, c] for c in range(k)]]))
        rowsA.append(sp.Matrix([[g[0, c] for c in range(k)]]))
    H = sp.Matrix.vstack(*rowsH)
    HA = sp.Matrix.vstack(*rowsA)
    P = sp.Matrix(H.rows, H.cols, lambda i, j: lam * H[i, j] - HA[i, j])
    ms = [x for x in minors(P, omega) if sp.simplify(x) != 0]
    if not ms:
        return None, Y.cols, None, "all minors vanish"
    g = gcd_all(ms)
    ok = sp.simplify(g).is_number or sp.Poly(g, lam).degree() == 0
    return ok, Y.cols, sp.factor(g), ("feasible" if ok else "infeasible")


def shift_family(k, L=3):
    """A: e_i -> e_{i+k}; C = rows e_{2k+1..3k}; then K0 = span{e_1..e_k}, S = row[e_1..e_2k]."""
    n = 3 * k
    A = sp.zeros(n)
    for i in range(2 * k):
        A[i + k, i] = 1
    C = sp.zeros(k, n)
    for i in range(k):
        C[i, 2 * k + i] = 1
    return A, C


def main() -> None:
    print("=" * 80)
    print("sufficiency test: T_W = W + W  =>  layer omega feasible with 2*omega rows")
    print("=" * 80)
    for k in (2, 3):
        A, C = shift_family(k)
        N = m.ker_basis(sp.Matrix.vstack(C, C * A))
        print(f"\nk = {N.cols} (shift family, n = {A.rows})")
        for omega in range(1, N.cols):
            W = sp.zeros(omega, N.cols)
            for i in range(omega):
                W[i, i] = 1
            ok, dT, g, msg = check(A, C, W, omega, 2 * omega)
            print(f"  omega={omega}, dim T_W={dT}: {msg}, gcd={g}")


if __name__ == "__main__":
    main()
