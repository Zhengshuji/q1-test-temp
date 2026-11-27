#!/usr/bin/env python3
"""c387 — Threshold experiment: how large must dim T_W be for feasibility?

For random instances we collect (omega, dim T_W, cond_E, cond_F) and look for the smallest
dim T_W at which (F) holds.
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


def analyse(A, C, L0, W, omega, m_rows, seed=0):
    N = m.ker_basis(sp.Matrix.vstack(C, C * A))
    AN = A * N
    k = N.cols
    n = A.rows
    fixed = L0 * sp.Matrix.hstack(N, AN)
    for i in range(fixed.rows):
        if (sp.Matrix.vstack(W, fixed[i, 0:k]).rank() > omega
                or sp.Matrix.vstack(W, fixed[i, k:2 * k]).rank() > omega):
            return None
    Wp = m.ker_basis(W)
    Y = m.ker_basis(sp.Matrix.hstack(N * Wp, AN * Wp).T)
    if Y.cols == 0:
        return (0, False, False)
    X = sp.Matrix([[sum(Y[i, j] * N[i, c] for i in range(n)) for c in range(k)] for j in range(Y.cols)])
    G = sp.Matrix([[sum(Y[i, j] * AN[i, c] for i in range(n)) for c in range(k)] for j in range(Y.cols)])
    M = sp.Matrix([[sp.expand(lam * X[j, c] - G[j, c]) for c in range(k)] for j in range(Y.cols)])
    ms = [x for x in minors(M, omega) if sp.simplify(x) != 0]
    E = False
    if ms:
        g = ms[0]
        for x in ms[1:]:
            g = sp.gcd(g, x)
            if sp.simplify(g).is_number:
                break
        E = bool(sp.simplify(g).is_number or sp.Poly(g, lam).degree() == 0)
    # (F) with several random choices
    rng = random.Random(seed)
    F = False
    for _ in range(4):
        rowsH, rowsA = [], []
        for a in range(m_rows):
            cf = [rng.randint(-2, 2) for _ in range(Y.cols)]
            y = sp.Matrix([sum(cf[j] * Y[i, j] for j in range(Y.cols)) for i in range(n)])
            h = y.T * N
            g = y.T * AN
            rowsH.append(sp.Matrix([[h[0, c] for c in range(k)]]))
            rowsA.append(sp.Matrix([[g[0, c] for c in range(k)]]))
        H = sp.Matrix.vstack(sp.Matrix([[fixed[0, c] for c in range(k)]]), *rowsH)
        HA = sp.Matrix.vstack(sp.Matrix([[fixed[0, k + c] for c in range(k)]]), *rowsA)
        P = sp.Matrix(H.rows, H.cols, lambda i, j: lam * H[i, j] - HA[i, j])
        ms2 = [x for x in minors(P, omega) if sp.simplify(x) != 0]
        if not ms2:
            continue
        g = ms2[0]
        for x in ms2[1:]:
            g = sp.gcd(g, x)
            if sp.simplify(g).is_number:
                break
        if sp.simplify(g).is_number or sp.Poly(g, lam).degree() == 0:
            F = True
            break
    return (Y.cols, E, F)


def main() -> None:
    print("=" * 78)
    print("threshold: (omega, dim T_W, E, F)")
    print("=" * 78)
    rng = random.Random(1234)
    rows = []
    for trial in range(10):
        n = 5
        C = sp.zeros(1, n)
        C[0, n - 1] = 1
        A = sp.Matrix(n, n, lambda i, j: rng.randint(-2, 2))
        if sp.Matrix.vstack(C, C * A).rank() != 2:
            continue
        N = m.ker_basis(sp.Matrix.vstack(C, C * A))
        k = N.cols
        L0 = sp.Matrix([[rng.randint(-1, 1) for _ in range(n)]])
        fixed = L0 * sp.Matrix.hstack(N, A * N)
        h0, g0 = fixed[0, 0:k], fixed[0, k:2 * k]
        Kq = m.ker_basis(sp.Matrix.vstack(h0, g0))
        cand = [Kq[:, j].T for j in range(Kq.cols)]
        for omega in range(1, k):
            for q in cand:
                W = m.ker_basis(q).T
                if W.rows != omega:
                    continue
                res = analyse(A, C, L0, W, omega, m_rows=2 * omega, seed=trial)
                if res is None:
                    continue
                dT, E, F = res
                rows.append((omega, dT, E, F))
    for (omega, dT, E, F) in sorted(rows):
        print(f"  omega={omega}  dim T_W={dT}  2*omega={2*omega}  E={E}  F={F}")
    feas = [r for r in rows if r[3]]
    print(f"\ntotal = {len(rows)}, feasible = {len(feas)}")
    if feas:
        print("feasible cases (omega, dim T_W):", sorted({(r[0], r[1]) for r in feas}))


if __name__ == "__main__":
    main()
