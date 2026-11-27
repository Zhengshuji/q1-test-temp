#!/usr/bin/env python3
"""c376 — k=2, omega=1: the active set is empty, a single point, or (d=0) open.

Verifies the classification of the P^1 case.  With W_z = span{(1,z)} and the expert's
scalar reduction, spectral regularity of the pencil is equivalent to

    dim span{ (alpha_j, beta_j) : nonzero } >= 2

where h_j = alpha_j (1,z) and g_j = beta_j (1,z).  The span of the fixed pairs is
U (dimension d), and the free rows contribute the image F(z) of the left-null-space
parametrisation of T_z.  Hence:

    d = 2  ->  no compatible W            (active set empty)
    d = 1  ->  one compatible W           (active set is at most one point)
    d = 0  ->  every W compatible         (active set = {z : dim F(z) >= 2}, open)

The script checks this against a direct feasibility test on a grid of z.
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


def direct_test(H, HA, w):
    P = sp.Matrix(H.rows, H.cols, lambda i, j: lam * H[i, j] - HA[i, j])
    ms = [d for d in minors(P, w) if sp.simplify(d) != 0]
    if not ms:
        return False
    g = ms[0]
    for d in ms[1:]:
        g = sp.gcd(g, d)
    return sp.simplify(g).is_number or sp.Poly(g, lam).degree() == 0


def setup(A, C, L0):
    N = m.ker_basis(sp.Matrix.vstack(C, C * A))
    AN = A * N
    S = sp.Matrix.hstack(N, AN)
    fixed = L0 * S
    return N, AN, S, fixed, N.cols


def criterion(A, C, L0, z, m_rows, seed=7):
    """Return (compatible, active) for W_z at layer omega = 1, using the scalar criterion."""
    N, AN, S, fixed, k = setup(A, C, L0)
    if k != 2:
        return None, None
    W = sp.Matrix([[1, z]]) if z is not None else sp.Matrix([[0, 1]])
    h0, g0 = fixed[0, 0:2], fixed[0, 2:4]
    if sp.Matrix.vstack(W, h0).rank() > 1 or sp.Matrix.vstack(W, g0).rank() > 1:
        return False, None
    Wp = m.ker_basis(W)                       # 2 x 1
    Mall = sp.Matrix.hstack(N * Wp, AN * Wp)  # n x 2
    Y = m.ker_basis(Mall.T)                   # left null space
    idx = 0 if z is not None else 1
    pairs = []
    for j in range(Y.cols):
        y = Y[:, j].T
        pairs.append((sp.simplify((y * N)[idx]), sp.simplify((y * AN)[idx])))
    if z is not None:
        pairs += [(h0[0], g0[0])] if (h0[0] != 0 or g0[0] != 0) else []
    else:
        pairs += [(h0[1], g0[1])] if (h0[1] != 0 or g0[1] != 0) else []
    M = sp.Matrix([list(p) for p in pairs if p != (0, 0)])
    active = M.rows >= 2 and M.rank() >= 2 if M.rows else False
    return True, active


def direct(A, C, L0, z, m_rows, seed=7):
    """Direct (sampled) feasibility test inside T_z, for cross-checking."""
    N, AN, S, fixed, k = setup(A, C, L0)
    W = sp.Matrix([[1, z]]) if z is not None else sp.Matrix([[0, 1]])
    h0, g0 = fixed[0, 0:2], fixed[0, 2:4]
    if sp.Matrix.vstack(W, h0).rank() > 1 or sp.Matrix.vstack(W, g0).rank() > 1:
        return False
    Wp = m.ker_basis(W)
    Y = m.ker_basis(sp.Matrix.hstack(N * Wp, AN * Wp).T)
    if Y.cols < 1:
        return False
    rng = random.Random(seed)
    for _ in range(30):
        rows = [Y * sp.Matrix([rng.randint(-3, 3) for _ in range(Y.cols)]) for _ in range(m_rows)]
        H = sp.Matrix.vstack(fixed[:, 0:2], *[r.T * N for r in rows])
        HA = sp.Matrix.vstack(fixed[:, 2:4], *[r.T * AN for r in rows])
        if H.rank() != 1:
            continue
        if sp.Matrix.vstack(H, HA).rank() != 1:
            continue
        if direct_test(H, HA, 1):
            return True
    return False


def build(case, seed=0):
    rng = random.Random(seed)
    n = 4
    C = sp.zeros(1, n)
    C[0, 3] = 1
    A = sp.zeros(n)
    if case == "d1":
        A[0, 0] = 2
        A[1, 0] = 1
        A[2, 1] = 1
        A[3, 2] = 1
    else:
        A[0, 0] = 2
        A[1, 0] = 1
        A[2, 1] = 1
        A[3, 2] = 1
    L0 = sp.zeros(1, n)
    if case == "d1":
        L0[0, 0] = 1          # gives a nonzero fixed pair
    else:
        L0[0, 1] = 0          # zero fixed pair
    return A, C, L0


def main() -> None:
    print("=" * 74)
    print("k=2, omega=1: classification check (criterion vs direct test)")
    print("=" * 74)
    zs = [None, 0, 1, 2, -1, sp.Rational(1, 2), -2]
    for case in ["d1", "d0"]:
        A, C, L0 = build(case)
        N, AN, S, fixed, k = setup(A, C, L0)
        d = sp.Matrix.vstack(fixed[:, 0:k], fixed[:, k:2 * k]).rank()
        print(f"\ncase {case}: k = {k}, d = {d}")
        for z in zs:
            comp, act = criterion(A, C, L0, z, 1)
            dfeas = direct(A, C, L0, z, 1) if comp else None
            zz = "inf" if z is None else str(z)
            flag = "" if (act is None or dfeas is None or act == dfeas) else "   <-- MISMATCH"
            print(f"  z={zz:5s}: compatible={comp}, criterion={act}, direct={dfeas}{flag}")


if __name__ == "__main__":
    main()
