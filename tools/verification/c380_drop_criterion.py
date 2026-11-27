#!/usr/bin/env python3
"""c380 — The eigenvalue-drop criterion, and a construction that programs it.

Necessary condition for feasibility at layer omega (any omega):

    rank P(lambda) <= rank((lambda I - A) N)  =>  need rank((lambda I - A) N) >= omega
    <=>  dim( K0 cap ker(lambda I - A) ) <= k - omega    for every lambda.

This script
  (a) computes that dimension for the instances where layer omega = k-1 was found dead;
  (b) builds a family (A,C,L0) where the drops are *programmed*, and checks the criterion.
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


def drops(A, C):
    """max over lambda of dim(K0 cap ker(lambda I - A)) = k - min rank((lambda I-A)N)."""
    N = m.ker_basis(sp.Matrix.vstack(C, C * A))
    k = N.cols
    n = A.rows
    MN = (sp.Matrix(lam * sp.eye(n)) - A) * N
    # rank of a polynomial matrix = max over lambda of the rank; use generic lambda value
    ms = [x for x in _kminors(MN, k) if sp.simplify(x) != 0] if k <= MN.rows else []
    g = ms[0] if ms else sp.Integer(0)
    for x in ms[1:]:
        g = sp.gcd(g, x)
    # the rank drops exactly where the gcd of the k-minors vanishes; compute the drop at each root
    info = []
    evs = sp.roots(sp.factor(g), lam) if g != 0 else {}
    for ev, mult in evs.items():
        rk = ((sp.Matrix(ev * sp.eye(n)) - A) * N).rank()
        info.append((ev, k - rk))
    return k, sp.factor(g), info


def _kminors(M, k):
    return [sp.expand(M.extract(list(rs), list(cs)).det())
            for rs in itertools.combinations(range(M.rows), k)
            for cs in itertools.combinations(range(M.cols), k)]


def programmed(bvals, dvals=None):
    """K0 = span{first k coords}, A = blockdiag(B, D): then A acts on K0 by B, and the drops are
    exactly the eigenspaces of B."""
    k = len(bvals)
    B = sp.diag(*bvals)
    D = sp.diag(*dvals) if dvals else sp.eye(k)
    A = sp.diag(B, D)
    n = A.rows
    C = sp.zeros(k, n)
    for i in range(k):
        C[i, k + i] = 1
    return A, C


def main() -> None:
    print("=" * 78)
    print("eigenvalue-drop criterion")
    print("=" * 78)
    rng = random.Random(20261121)
    n = 5
    C0 = sp.zeros(1, n)
    C0[0, n - 1] = 1
    print("\n(a) instances where layer omega = k-1 was dead:")
    for trial in range(3):
        A = sp.Matrix(n, n, lambda i, j: rng.randint(-2, 2))
        while sp.Matrix.vstack(C0, C0 * A).rank() != 2:
            A = sp.Matrix(n, n, lambda i, j: rng.randint(-2, 2))
        N = m.ker_basis(sp.Matrix.vstack(C0, C0 * A))
        k = N.cols
        MN = (sp.Matrix(lam * sp.eye(n)) - A) * N
        ms = [x for x in _kminors(MN, k) if sp.simplify(x) != 0]
        g = ms[0] if ms else sp.Integer(0)
        for x in ms[1:]:
            g = sp.gcd(g, x)
        print(f"  trial {trial}: k={k}, gcd of k-minors of (lamI-A)N = {sp.factor(g)} "
              f"-> drop = {k - ((sp.Matrix(-A)) * N).rank() if g == lam else 'see below'}")
    print("\n(b) programmed construction: A = blockdiag(B, D), K0 = first k coords")
    for bvals, dvals in [((1, 2), (3, 4)), ((1, 1), (2, 3)), ((0, 2), (1, 3))]:
        A, C = programmed(bvals, dvals)
        k, g, info = drops(A, C)
        print(f"  B = diag{bvals}: k={k}, gcd of k-minors of (lamI-A)N = {g}, drops = {info}")


if __name__ == "__main__":
    main()
