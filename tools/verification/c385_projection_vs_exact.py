#!/usr/bin/env python3
"""c385 — Cross-check: projection condition  vs  exact gcd feasibility.

Projection condition (438/439):  layer omega is feasible on the fibre of W  <=>
    dim pi_1(T_W) = omega  and  dim pi_2(T_W) = omega      (T_W = S cap (W + W)),
modulo the fixed-row off-by-one.  Equivalently  E_lambda surjective for all lambda.

For random instances and many W we compare this cheap linear-algebraic test with the exact
gcd test (symbolic fibre parameters, gcd over Q(tau)[lam]).
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


def minors(P, r):
    return [sp.expand(P.extract(list(rs), list(cs)).det())
            for rs in itertools.combinations(range(P.rows), r)
            for cs in itertools.combinations(range(P.cols), r)]


def exact_feasible(A, C, L0, W, omega, m_rows, seed=0):
    N = m.ker_basis(sp.Matrix.vstack(C, C * A))
    AN = A * N
    k = N.cols
    n = A.rows
    fixed = L0 * sp.Matrix.hstack(N, AN)
    for i in range(fixed.rows):
        if (sp.Matrix.vstack(W, fixed[i, 0:k]).rank() > omega
                or sp.Matrix.vstack(W, fixed[i, k:2 * k]).rank() > omega):
            return None, None          # incompatible
    Wp = m.ker_basis(W)
    Y = m.ker_basis(sp.Matrix.hstack(N * Wp, AN * Wp).T)
    dT = Y.cols
    if dT < 1:
        return False, dT
    taus = sp.symbols(f"v0:{m_rows * dT}")
    rowsH, rowsA = [], []
    for a in range(m_rows):
        cf = [taus[a * dT + j] for j in range(dT)]
        y = sp.Matrix([sum(cf[j] * Y[i, j] for j in range(dT)) for i in range(n)])
        h = y.T * N
        g = y.T * AN
        rowsH.append(sp.Matrix([[h[0, c] for c in range(k)]]))
        rowsA.append(sp.Matrix([[g[0, c] for c in range(k)]]))
    H = sp.Matrix.vstack(sp.Matrix([[fixed[0, c] for c in range(k)]]), *rowsH)
    HA = sp.Matrix.vstack(sp.Matrix([[fixed[0, k + c] for c in range(k)]]), *rowsA)
    P = sp.Matrix(H.rows, H.cols, lambda i, j: lam * H[i, j] - HA[i, j])
    ms = [x for x in minors(P, omega) if sp.simplify(x) != 0]
    if not ms:
        return False, dT
    g = ms[0]
    for x in ms[1:]:
        g = sp.gcd(g, x)
        if sp.simplify(g).is_number:
            return True, dT
    return bool(sp.simplify(g).is_number or sp.Poly(g, lam).degree() == 0), dT


def projection_condition(A, C, L0, W, omega):
    N = m.ker_basis(sp.Matrix.vstack(C, C * A))
    AN = A * N
    k = N.cols
    fixed = L0 * sp.Matrix.hstack(N, AN)
    for i in range(fixed.rows):
        if (sp.Matrix.vstack(W, fixed[i, 0:k]).rank() > omega
                or sp.Matrix.vstack(W, fixed[i, k:2 * k]).rank() > omega):
            return None
    Wp = m.ker_basis(W)
    Y = m.ker_basis(sp.Matrix.hstack(N * Wp, AN * Wp).T)   # rows = admissible pairs
    if Y.cols == 0:
        return False
    # pair of row j is (N^T Y[:,j], AN^T Y[:,j]); first components = (y^T N), second = (y^T AN)
    X = sp.Matrix([[sum(Y[i, j] * N[i, c] for i in range(N.rows)) for c in range(k)]
                   for j in range(Y.cols)])
    G = sp.Matrix([[sum(Y[i, j] * AN[i, c] for i in range(N.rows)) for c in range(k)]
                   for j in range(Y.cols)])
    return X.rank() == omega and G.rank() == omega


def main() -> None:
    print("=" * 78)
    print("projection condition vs exact gcd feasibility")
    print("=" * 78)
    rng = random.Random(20261121)
    agree = disagree = cases = 0
    for trial in range(6):
        n = 5
        C = sp.zeros(1, n)
        C[0, n - 1] = 1
        A = sp.Matrix(n, n, lambda i, j: rng.randint(-2, 2))
        while sp.Matrix.vstack(C, C * A).rank() != 2:
            A = sp.Matrix(n, n, lambda i, j: rng.randint(-2, 2))
        N = m.ker_basis(sp.Matrix.vstack(C, C * A))
        k = N.cols
        L0 = sp.Matrix([[rng.randint(-1, 1) for _ in range(n)]])
        fixed = L0 * sp.Matrix.hstack(N, A * N)
        h0, g0 = fixed[0, 0:k], fixed[0, k:2 * k]
        Kq = m.ker_basis(sp.Matrix.vstack(h0, g0))
        cand = [Kq[:, j].T for j in range(Kq.cols)]
        if Kq.cols >= 2:
            cand.append((Kq[:, 0] + Kq[:, 1]).T)
            cand.append((Kq[:, 0] - Kq[:, 1]).T)
        for omega in range(1, k):
            for qv in cand:
                W = m.ker_basis(qv).T
                if W.rows != omega:
                    continue
                proj = projection_condition(A, C, L0, W, omega)
                for m_rows in (2, 3, 4, 5):
                    ex, dT = exact_feasible(A, C, L0, W, omega, m_rows, seed=trial)
                    if proj is None or ex is None:
                        continue
                    cases += 1
                    if bool(proj) == bool(ex):
                        agree += 1
                    else:
                        disagree += 1
                        print(f"  DISAGREE trial={trial} omega={omega} m={m_rows}: "
                              f"proj={proj}, exact={ex}")
    print(f"\ncases compared = {cases}, agree = {agree}, disagree = {disagree}")


if __name__ == "__main__":
    main()
