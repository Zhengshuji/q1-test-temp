#!/usr/bin/env python3
"""c381 — Can a CHARACTERISTIC layer (omega = k-1) be feasible?

This is the hardness-relevant question.  In the earlier random probes every layer with
omega < k was dead ("non-characteristic layer is always bad"), and the top layer turned out
to be decidable in polynomial time.  The only regime that could still carry hardness is a
*characteristic* layer: one where A acts on K0 with eigenvalues, so that the pencil's
degeneracy is structural rather than accidental.

We build the programmed family
    K0 = span{e1..ek},  C = [0 | I_k],  A = blockdiag(B, D),
so A|K0 = B has eigenvalues by construction, and test layer omega = k-1 exactly
(symbolic fibre parameters, gcd over Q(tau)[lam]).
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


def exact_layer(A, C, L0, W, omega, m_rows):
    """Exact test at layer omega for the subspace W (symbolic fibre parameters)."""
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
    Y = m.ker_basis(sp.Matrix.hstack(N * Wp, AN * Wp).T)
    if Y.cols < 1:
        return "empty fibre", Y.cols, None
    dS = Y.cols
    taus = sp.symbols(f"t0:{m_rows * dS}")
    rowsH, rowsA = [], []
    for a in range(m_rows):
        cf = [taus[a * dS + j] for j in range(dS)]
        yv = [sum(cf[j] * Y[i, j] for j in range(dS)) for i in range(n)]
        rowsH.append(sp.Matrix([[sum(yv[i] * N[i, j] for i in range(n)) for j in range(k)]]))
        rowsA.append(sp.Matrix([[sum(yv[i] * AN[i, j] for i in range(n)) for j in range(k)]]))
    H = sp.Matrix.vstack(sp.Matrix([list(fixed[0, 0:k])]), *rowsH)
    HA = sp.Matrix.vstack(sp.Matrix([list(fixed[0, k:2 * k])]), *rowsA)
    P = sp.Matrix(H.rows, H.cols, lambda i, j: lam * H[i, j] - HA[i, j])
    ms = [x for x in minors_of(P, omega) if sp.simplify(x) != 0]
    if not ms:
        return "no nonzero minor", dS, None
    g = ms[0]
    for x in ms[1:]:
        g = sp.gcd(g, x)
        if sp.simplify(g).is_number:
            g = sp.Integer(1)
            break
    return ("feasible" if (sp.simplify(g).is_number or sp.Poly(g, lam).degree() == 0) else "infeasible",
            dS, sp.factor(g))


def programmed(bvals, dvals):
    k = len(bvals)
    A = sp.diag(sp.diag(*bvals), sp.diag(*dvals))
    n = A.rows
    C = sp.zeros(k, n)
    for i in range(k):
        C[i, k + i] = 1
    return A, C


def main() -> None:
    print("=" * 80)
    print("can a characteristic layer omega = k-1 be feasible?")
    print("=" * 80)
    for bvals, dvals in [((1, 2, 3), (5, 6, 7)), ((1, 2, 3), (1, 2, 3)), ((0, 1, 2), (5, 6, 7))]:
        A, C = programmed(bvals, dvals)
        n = A.rows
        k = len(bvals)
        N = m.ker_basis(sp.Matrix.vstack(C, C * A))
        print(f"\nB = diag{bvals}, D = diag{dvals}: k = {N.cols}")
        rng = random.Random(3)
        L0 = sp.Matrix([[rng.randint(-1, 1) for _ in range(n)]])
        # candidate hyperplanes W = {x : q . x = 0}: q must kill the fixed pair's parts
        fx = L0 * sp.Matrix.hstack(N, A * N)
        h0 = fx[0, 0:k]
        g0 = fx[0, k:2 * k]
        Mq = sp.Matrix.vstack(h0, g0)
        Kq = m.ker_basis(Mq)          # k x (k - d): q's orthogonal to the fixed parts
        qs = [Kq[:, j].T for j in range(Kq.cols)]
        print(f"  (fixed pair: h0={h0.T.tolist()}, g0={g0.T.tolist()}, compatible q's = {len(qs)})")
        for q in qs:
            W = m.ker_basis(q).T          # (k-1) x k
            for m_rows in (2, 3, 4):
                res, dT, g = exact_layer(A, C, L0, W, k - 1, m_rows)
                print(f"  q={q.tolist()}, m={m_rows}: dim T_W={dT}, {res}, gcd={g}")


if __name__ == "__main__":
    main()
