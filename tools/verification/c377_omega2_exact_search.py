#!/usr/bin/env python3
"""c377 — Exact search for an ACTIVE layer omega = 2 (k = 3).

For a fixed W, the fibre is parametrised exactly (symbolic parameters tau), the pencil
P(lam) = lam H(tau) - H_A(tau) is formed, and the gcd of its 2x2 minors is computed over
Q(tau)[lam].  Activity is decided by whether that gcd is 1 (no common root) — this is an
exact test in tau, not a sampling test.

The script scans a small set of instances and subspaces W, and reports whether any is active.
"""

from __future__ import annotations

import itertools
import os
import random
import sys
import time

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
        if g.is_number:
            return sp.Integer(1)
    return g


def active_exact(A, C, L0, W, omega, m_rows):
    """Exact test: gcd over Q(tau)[lam] of the omega-minors; returns (active, gcd, dim T_W)."""
    N = m.ker_basis(sp.Matrix.vstack(C, C * A))
    AN = A * N
    k = N.cols
    n = A.rows
    fixed = L0 * sp.Matrix.hstack(N, AN)
    # compatibility
    for i in range(fixed.rows):
        if (sp.Matrix.vstack(W, fixed[i, 0:k]).rank() > omega
                or sp.Matrix.vstack(W, fixed[i, k:2 * k]).rank() > omega):
            return None, None, None
    Wp = m.ker_basis(W)                       # k x (k - omega)
    Y = m.ker_basis(sp.Matrix.hstack(N * Wp, AN * Wp).T)   # left null space: dim T_W
    dT = Y.cols
    if dT < 1:
        return False, None, dT
    taus = sp.symbols(f"t0:{m_rows * dT}")
    rowsH, rowsA = [], []
    for a in range(m_rows):
        coeff = [taus[a * dT + j] for j in range(dT)]
        y = sp.Matrix([sum(coeff[j] * Y[i, j] for j in range(dT)) for i in range(n)])
        rowsH.append((y.T * N))
        rowsA.append((y.T * AN))
    H = sp.Matrix.vstack(fixed[:, 0:k], *rowsH)
    HA = sp.Matrix.vstack(fixed[:, k:2 * k], *rowsA)
    P = sp.Matrix(H.rows, H.cols, lambda i, j: lam * H[i, j] - HA[i, j])
    ms = [x for x in minors_of(P, omega) if sp.simplify(x) != 0]
    if not ms:
        return False, None, dT
    g = gcd_all(ms)
    return (sp.simplify(g).is_number or sp.Poly(g, lam).degree() == 0), g, dT


def main() -> None:
    print("=" * 78)
    print("exact search for an active omega = 2 layer (k = 3)")
    print("=" * 78)
    n = 5
    C = sp.Matrix([[0, 0, 0, 0, 1]])
    rng = random.Random(20261118)
    subspaces = [
        sp.Matrix([[1, 0, 0], [0, 1, 0]]),
        sp.Matrix([[1, 0, 0], [0, 0, 1]]),
        sp.Matrix([[0, 1, 0], [0, 0, 1]]),
        sp.Matrix([[1, 0, 0], [0, 1, 1]]),
        sp.Matrix([[1, 0, 0], [0, 1, -1]]),
    ]
    found = 0
    t0 = time.time()
    for trial in range(8):
        A = sp.Matrix(n, n, lambda i, j: rng.randint(-2, 2))
        if sp.Matrix.vstack(C, C * A).rank() != 2:
            continue
        N = m.ker_basis(sp.Matrix.vstack(C, C * A))
        if N.cols != 3:
            continue
        L0 = sp.Matrix([[rng.randint(-1, 1) for _ in range(n)]])
        if L0 * sp.Matrix.hstack(N, A * N) == sp.zeros(1, 6):
            continue      # trivial (omega = 0 layer available)
        for W in subspaces:
            act, g, dT = active_exact(A, C, L0, W, 2, 2)
            if act is True:
                found += 1
                print(f"  ACTIVE: trial={trial}, W={W.tolist()}, dim T_W={dT}, gcd={sp.factor(g)}")
                print(f"    A={A.tolist()}")
                print(f"    L0={L0.tolist()}")
            elif act is False and g is not None:
                print(f"  trial={trial}, W={W.tolist()}: dim T_W={dT}, gcd={sp.factor(g)}  (inactive)")
        if found:
            break
    print(f"\nactive instances found: {found}   ({time.time()-t0:.1f}s)")


if __name__ == "__main__":
    main()
