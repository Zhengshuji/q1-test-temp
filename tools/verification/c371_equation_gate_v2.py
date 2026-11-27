#!/usr/bin/env python3
"""c371 — A usable EQUATION gate: feasible <=> t = 0, with only ONE layer available.

Design (n=4):
    C = [0,0,0,1],   A = [[0,0,0,0],
                          [0,0,0,0],
                          [1,1,0,0],
                          [0,0,1,0]],   L0 = [t, 0, 1, 0].
Then
    CA = row 4 of A = e_3^T,   K0 = ker[C;CA] = span{e_1,e_2},   N = [e_1 e_2],
    A N = [A e_1, A e_2] = [e_3, e_3]   =>  dim(A K0) = 1
so by the lambda=0 bound  rank H = rank H_A <= dim(A K0) = 1:  ONLY layer omega = 1 exists.
    H0   = L0 N   = [t, 0]
    HA0  = L0 A N = [1, 1]
and with one free row r:  H = [[t,0],[u1,u2]],  H_A = [[1,1],[w1,w2]].

Prediction:  omega = 1 requires rank H = 1; since H's second column has first coordinate 0 while the
first has t, proportionality forces t = 0.  Then ker H = ker span{(1,-1)} and the kernel lemma needs
HA's columns to be equal, i.e. w1 = w2 -- free.  So feasible  <=>  t = 0.

This is the equation gate WITHOUT the layer-masking problem of 370 (no higher layer exists).
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


def build(t):
    n = 4
    C = sp.zeros(1, n)
    C[0, 3] = 1
    A = sp.zeros(n, n)
    A[2, 0] = 1
    A[2, 1] = 1
    A[3, 2] = 1
    L0 = sp.zeros(1, n)
    L0[0, 0] = t
    L0[0, 2] = 1
    return C, A, L0


def feasible(t, budget=3000):
    C, A, L0 = build(t)
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    if N.cols != 2:
        return None, N.cols
    AN = A * N
    H0 = L0 * N
    HA0 = L0 * AN
    import random
    rng = random.Random(371)
    for _ in range(budget):
        r = sp.Matrix(1, 4, lambda i, j: rng.randint(-2, 2))
        H = sp.Matrix.vstack(H0, r * N)
        HA = sp.Matrix.vstack(HA0, r * AN)
        w = H.rank()
        if w == 0:
            continue
        if sp.Matrix.vstack(H, HA).rank() != w:
            continue
        if layer_good(H, HA, w):
            return True, N.cols
    return False, N.cols


def main() -> None:
    print("=" * 72)
    print("equation gate:  feasible  <=>  t = 0   (only layer 1 exists)")
    print("=" * 72)
    for t in [sp.Rational(-1), sp.Rational(0), sp.Rational(1, 3), sp.Rational(1), sp.Rational(2)]:
        ok, k = feasible(t)
        print(f"  t = {str(t):5s}: feasible = {int(bool(ok))}   (k = {k}, dim(AK0) = 1)")
    print()
    print("  prediction: only t = 0 is feasible")


if __name__ == "__main__":
    main()
