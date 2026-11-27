#!/usr/bin/env python3
"""c372 — Booleanity gate: feasible  <=>  x(x-1) = 0,  i.e. x in {0,1}.

Derivation (k = 2, layer omega = 1, m = 1 free row so r = r0 + m = 2 = k):
  Per block i: C_i=[0,0,1], A_i(t_i)=[[0,0,0],[t_i,0,0],[0,1,0]], L0 part [a_i b_i c_i].
  Contributions:  H's column i = (a_i; u_i),   H_A's column i = t_i (b_i; w_i).

  At layer 1 the two columns of H are proportional, so ker H = span{v} with
        v_1 H_1 + v_2 H_2 = 0.
  The fixed part of that vector equation gives a LINEAR condition on v:
        v_1 a_1 + v_2 a_2 = 0,        (row 0 of H)
  and the kernel lemma (ker H = ker H_A) gives
        v_1 t_1 b_1 + v_2 t_2 b_2 = 0.  (row 0 of H_A)
  Such a nonzero v exists iff  det [[a_1, a_2], [t_1 b_1, t_2 b_2]] = 0.
  (The free parts u_i, w_i can then always be chosen; the pencil stays rank 1 as long as
   we avoid one proportionality, which is a free choice.)

  Choose  a_1 = x, a_2 = 0, b_1 = b_2 = 1, t_1 = 1, t_2 = x - 1:
        det = x * (x-1) * 1 - 0 * ... = x(x-1)
  so layer 1 is feasible  <=>  x(x-1) = 0  <=>  x in {0,1}:  BOOLEANITY.

  Higher layers: dim(A K0) = 2, but r = 2 = k, so layer 2 is a SQUARE pencil and is
  infeasible for every x (square-pencil obstruction).  No masking.
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
    n = 6
    C = sp.zeros(2, n)
    A = sp.zeros(n)
    L0 = sp.zeros(1, n)
    # block 1: parameter t1 = 1, L0 part (x, 1, 0)
    C[0, 2] = 1
    A[1, 0] = 1
    A[2, 1] = 1
    L0[0, 0] = x
    # block 2: parameter t2 = x - 1, L0 part (0, 1, 0)
    C[1, 5] = 1
    A[4, 3] = x - 1
    A[5, 4] = 1
    L0[0, 4] = 1
    return C, A, L0


def feasible(x, budget=4000):
    C, A, L0 = build(x)
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    AN = A * N
    H0 = L0 * N
    HA0 = L0 * AN
    rng = random.Random(372)
    for _ in range(budget):
        R = sp.Matrix(1, 6, lambda i, j: rng.randint(-3, 3))
        H = sp.Matrix.vstack(H0, R * N)
        HA = sp.Matrix.vstack(HA0, R * AN)
        w = H.rank()
        if w == 0:
            continue
        if sp.Matrix.vstack(H, HA).rank() != w:
            continue
        if layer_good(H, HA, w):
            return True, w
    return False, None


def main() -> None:
    print("=" * 72)
    print("Booleanity gate:  feasible  <=>  x(x-1) = 0")
    print("=" * 72)
    for x in [sp.Rational(-1), sp.Rational(0), sp.Rational(1, 2), sp.Rational(1), sp.Rational(2)]:
        ok, w = feasible(x)
        pred = (x == 0) or (x == 1)
        print(f"  x = {str(x):5s}: feasible = {int(ok)}  (predicted {int(pred)}, omega = {w})")


if __name__ == "__main__":
    main()
