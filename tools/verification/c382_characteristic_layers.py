#!/usr/bin/env python3
"""c382 — Characteristic middle layers: exact feasibility test on a programmed family.

Family:  K0 = span{e1..ek},  C = [0 | I_k],  A = blockdiag(B, D).
Then A acts on K0 by B, so K0 contains eigenvectors of A (characteristic), and layer omega
is subject to the drop criterion  dim(K0 cap ker(lam I - A)) <= k - omega.

For each layer omega < k and each compatible W we build the generic pencil over the
function field Q(tau) and compute the gcd of its omega-minors exactly (no sampling).
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


def gcd_list(polys):
    g = polys[0]
    for p in polys[1:]:
        g = sp.gcd(g, p)
        if sp.simplify(g).is_number:
            return sp.Integer(1)
    return g


def layer_exact(A, C, L0, W, omega, m_rows):
    """Exact: is layer omega feasible on the fibre of W?  (symbolic tau)"""
    N = m.ker_basis(sp.Matrix.vstack(C, C * A))
    AN = A * N
    k = N.cols
    n = A.rows
    fixed = L0 * sp.Matrix.hstack(N, AN)
    for i in range(fixed.rows):
        if (sp.Matrix.vstack(W, fixed[i, 0:k]).rank() > omega
                or sp.Matrix.vstack(W, fixed[i, k:2 * k]).rank() > omega):
            return "incompatible", None, None
    Wp = m.ker_basis(W)
    Y = m.ker_basis(sp.Matrix.hstack(N * Wp, AN * Wp).T)   # left null space = T_W
    if Y.cols < 1:
        return "empty fibre", 0, None
    dS = Y.cols
    taus = sp.symbols(f"u0:{m_rows * dS}")
    rowsH, rowsA = [], []
    for a in range(m_rows):
        cf = [taus[a * dS + j] for j in range(dS)]
        y = sp.Matrix([sum(cf[j] * Y[i, j] for j in range(dS)) for i in range(n)])
        h = (y.T * N)
        g = (y.T * AN)
        rowsH.append(sp.Matrix([[h[0, j] for j in range(k)]]))
        rowsA.append(sp.Matrix([[g[0, j] for j in range(k)]]))
    H = sp.Matrix.vstack(sp.Matrix([[fixed[0, j] for j in range(k)]]), *rowsH)
    HA = sp.Matrix.vstack(sp.Matrix([[fixed[0, k + j] for j in range(k)]]), *rowsA)
    P = sp.Matrix(H.rows, H.cols, lambda i, j: lam * H[i, j] - HA[i, j])
    ms = [x for x in minors(P, omega) if sp.simplify(x) != 0]
    if not ms:
        return "all minors vanish", dS, None
    g = gcd_list(ms)
    ok = bool(sp.simplify(g).is_number or sp.Poly(g, lam).degree() == 0)
    return ("feasible" if ok else "infeasible"), dS, sp.factor(g)


def main() -> None:
    print("=" * 80)
    print("characteristic middle layers, exact test")
    print("=" * 80)
    cases = [((1, 2, 3), (5, 6, 7)), ((1, 1, 2), (5, 6, 7)), ((0, 1, 2), (5, 6, 7))]
    for bvals, dvals in cases:
        k = len(bvals)
        A = sp.diag(sp.diag(*bvals), sp.diag(*dvals))
        n = A.rows
        C = sp.zeros(k, n)
        for i in range(k):
            C[i, k + i] = 1
        N = m.ker_basis(sp.Matrix.vstack(C, C * A))
        rng = random.Random(5)
        L0 = sp.Matrix([[rng.randint(-1, 1) for _ in range(n)]])
        fixed = L0 * sp.Matrix.hstack(N, A * N)
        h0, g0 = fixed[0, 0:N.cols], fixed[0, N.cols:2 * N.cols]
        Kq = m.ker_basis(sp.Matrix.vstack(h0, g0))
        print(f"\nB = diag{bvals}, D = diag{dvals}: k = {N.cols}, "
              f"compatible q-space dim = {Kq.cols}")
        qs = [Kq[:, j].T for j in range(Kq.cols)]
        if not qs:
            print("  no compatible hyperplane (fixed pair spans all of V)")
            continue
        for omega in range(1, N.cols):
            for q in qs[:3]:
                W = m.ker_basis(q).T
                if W.rows != omega:
                    continue
                for m_rows in (2, 3):
                    res, dT, g = layer_exact(A, C, L0, W, omega, m_rows)
                    print(f"  omega={omega}, q={q.tolist()}, m={m_rows}: "
                          f"dim T_W={dT}, {res}, gcd={g}")


if __name__ == "__main__":
    main()
