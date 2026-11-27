#!/usr/bin/env python3
"""c373 — Conjunction of equations: feasible  <=>  (x = 0 AND y = 0).

Single block with k = 2 compressed columns and r0 = 2 fixed rows:
    n = 4,  C = [0,0,0,1],
    A = [[0,0,0,0],[0,0,0,0],[1,1,0,0],[0,0,1,0]],
    L0 = [[x, 0, 1, 0],
          [y, 0, 1, 0]].
Then  K0 = ker[C;CA] = span{e1,e2},  N = [e1 e2],  A N = [e3, e3]  =>  dim(AK0) = 1,
so by the lambda=0 bound ONLY layer omega = 1 can be feasible (no masking).

    H0  = L0 N   = [[x, 0],
                    [y, 0]]
    HA0 = L0 A N = [[1, 1],
                    [1, 1]]

Layer 1 requires a nonzero v with  v^T H0 = 0  and  v^T HA0 = 0  (the fixed-row parts of the
kernel equality; the free-row parts can then always be chosen).  The second gives
v1 + v2 = 0, so v = (1,-1); the first then gives  x = 0  and  y = 0.

    feasible  <=>  (x = 0 and y = 0):  a CONJUNCTION OF EQUATIONS.
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


def build(x, y):
    n = 4
    C = sp.zeros(1, n)
    C[0, 3] = 1
    A = sp.zeros(n, n)
    A[2, 0] = 1
    A[2, 1] = 1
    A[3, 2] = 1
    L0 = sp.zeros(2, n)
    L0[0, 0] = x
    L0[0, 2] = 1
    L0[1, 0] = y
    L0[1, 2] = 1
    return C, A, L0


def feasible(x, y, budget=4000):
    C, A, L0 = build(x, y)
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    if N.cols != 2:
        return False, N.cols
    AN = A * N
    H0 = L0 * N
    HA0 = L0 * AN
    rng = random.Random(373)
    for _ in range(budget):
        R = sp.Matrix(1, 4, lambda i, j: rng.randint(-3, 3))
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
    print("conjunction of equations:  feasible  <=>  (x = 0 AND y = 0)")
    print("=" * 72)
    for x in [sp.Rational(0), sp.Rational(1)]:
        for y in [sp.Rational(0), sp.Rational(1)]:
            ok, w = feasible(x, y)
            pred = (x == 0) and (y == 0)
            print(f"  (x,y) = ({x},{y}): feasible = {int(ok)}  (predicted {int(pred)}, omega = {w})")


if __name__ == "__main__":
    main()
