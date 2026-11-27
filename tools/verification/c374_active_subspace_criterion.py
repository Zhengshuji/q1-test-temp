#!/usr/bin/env python3
"""c374 — Milestone 1-2 check: the active-subspace criterion on a known instance.

Expert 104's criterion.  With Phi(r) = (rN, rAN), S = im Phi = row[N AN], and for an
omega-dimensional W:
    T_W = S cap (W + W)          (pairs of compressed rows admissible inside W)
    (i)   compatibility: every fixed pair (h_i^0, g_i^0) lies in W + W
    (ii)  rank completion: span({h_i^0} cup pi_1(T_W)) = W
    (iii) generic spectral feasibility of the pencil built from T_W
Feasibility  <=>  some W in Gr(omega,k) satisfies (i)(ii)(iii).

This script checks the criterion against brute-force feasibility on the Booleanity gate
(where the answer is known: feasible  <=>  x in {0,1}).

For k = 2, omega = 1, Gr(1,2) = P^1: we enumerate W_t = span{(1,t)} for several rational t
plus W_inf = span{(0,1)}.  The generic gcd test is performed by sampling admissible pairs
from T_W: if ANY sampled pencil has gcd 1, the generic gcd is 1 (specialisation can only
enlarge the gcd).
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


def layer_good(H, HA, w):
    P = sp.Matrix(H.rows, H.cols, lambda i, j: lam * H[i, j] - HA[i, j])
    if w + 1 <= min(P.rows, P.cols):
        for d in minors(P, w + 1):
            if sp.simplify(d) != 0:
                return False
    ms = [d for d in minors(P, w) if sp.simplify(d) != 0]
    if not ms:
        return False
    g = ms[0]
    for d in ms[1:]:
        g = sp.gcd(g, d)
    return sp.simplify(g).is_number or sp.Poly(g, lam).degree() == 0


def build(x):
    """Booleanity gate: k=2, r0=1, parameters in L0 and A."""
    n = 6
    C = sp.zeros(2, n)
    A = sp.zeros(n)
    L0 = sp.zeros(1, n)
    C[0, 2] = 1
    A[1, 0] = 1
    A[2, 1] = 1
    L0[0, 0] = x
    C[1, 5] = 1
    A[4, 3] = x - 1
    A[5, 4] = 1
    L0[0, 4] = 1
    return C, A, L0


def criterion(x, ws, n_z=8, seed=374):
    C, A, L0 = build(x)
    Wm = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(Wm)
    AN = A * N
    k = N.cols
    # S = row[N AN] as a subspace of C^{2k}; build a basis (2k x d)
    S = sp.Matrix.hstack(N, AN)          # n x 2k, its row space is S
    dS = S.rank()
    fixed = L0 * sp.Matrix.hstack(N, AN) # fixed rows' pairs (1 x 2k)
    passing = []
    for W in ws:
        # W given as list of row vectors in C^{1 x k}
        Wm_ = sp.Matrix(W)               # (#gens x k)
        if Wm_.rank() != Wm_.rows:
            continue
        r = Wm_.rows
        # compatibility: the fixed pairs lie in W + W
        ok_i = True
        for i in range(fixed.rows):
            h0 = fixed[i, 0:k]
            g0 = fixed[i, k:2 * k]
            if sp.Matrix.vstack(Wm_, h0).rank() > r or sp.Matrix.vstack(Wm_, g0).rank() > r:
                ok_i = False
                break
        if not ok_i:
            continue
        # T_W = S cap (W + W): solve for pairs (h,g) in W+W with the pair in S.
        # S is the row space of S (n x 2k); a pair p in S iff p = y^T S^T for some y.
        # Work with the orthogonal complement instead: p in S iff p is orthogonal to ker(S^T)... use rank test.
        # We sample admissible pairs directly: choose u, v as free rows and project.
        # A pair (rN, rAN) is admissible inside W iff both parts lie in W.
        # Solve: find the space of r with rN in W and rAN in W.
        # rN in W  <=>  each coordinate functional of N's orthogonal complement kills r.
        # Simpler: sample random r and keep those whose pair lies in W + W (gives pi_1 image samples).
        rng = random.Random(seed)
        pi1_samples = []
        pair_samples = []
        for _ in range(400):
            rr = sp.Matrix(1, A.rows, lambda i, j: rng.randint(-3, 3))
            p = rr * sp.Matrix.hstack(N, AN)   # 1 x 2k
            hh = p[:, 0:k]
            gg = p[:, k:2 * k]
            if sp.Matrix.vstack(Wm_, hh).rank() == r and sp.Matrix.vstack(Wm_, gg).rank() == r:
                pi1_samples.append(hh)
                pair_samples.append((hh, gg))
        if not pair_samples:
            continue
        # (ii) rank completion
        rows = [fixed[i, 0:k] for i in range(fixed.rows)] + pi1_samples
        d0 = sp.Matrix.hstack(*[sp.Matrix(r2) for r2 in [fixed[:, 0:k]]]).T.rank() if fixed.rows else 0
        comp = sp.Matrix.vstack(*[sp.Matrix(r2) for r2 in rows]) if rows else sp.zeros(0, k)
        ranks = comp.rank()
        ok_ii = (ranks >= r)
        if not ok_ii:
            continue
        # (iii) generic spectral feasibility: build pencils from sampled admissible pairs
        ok_iii = False
        for (hh, gg) in pair_samples[:60]:
            H = sp.Matrix.vstack(fixed[:, 0:k], hh)
            HA = sp.Matrix.vstack(fixed[:, k:2 * k], gg)
            w = H.rank()
            if w != r:
                continue
            if sp.Matrix.vstack(H, HA).rank() != w:
                continue
            if layer_good(H, HA, w):
                ok_iii = True
                break
        if ok_iii:
            passing.append(W)
    return dS, passing, k


def main() -> None:
    print("=" * 74)
    print("active-subspace criterion vs brute force, on the Booleanity gate")
    print("=" * 74)
    ws = []
    for t in [0, 1, 2, -1, sp.Rational(1, 2)]:
        ws.append([sp.Matrix([[1, t]])])
    ws.append([sp.Matrix([[0, 1]])])          # W_inf
    for x in [sp.Rational(0), sp.Rational(1, 2), sp.Rational(1)]:
        dS, passing, k = criterion(x, ws)
        print(f"  x = {str(x):5s}: dim S = {dS}, k = {k}, W's passing (i)(ii)(iii) = "
              f"{[sp.sstr(w[0]) for w in passing]}")
        print(f"             (brute force says feasible = {int(x == 0 or x == 1)})")


if __name__ == "__main__":
    main()
