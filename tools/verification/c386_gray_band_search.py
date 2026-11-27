#!/usr/bin/env python3
"""c386 — Directed search in the gray band: (E) true, (Z) false — can (F) still hold?

(E): E_lambda surjective for all lambda   (necessary, 437)
(Z): zero-partner condition                (sufficient, 441)
(F): layer feasible on that fibre

We look for (E) & !(Z) with a large T_W and many free rows, and test (F) exactly.
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


def data(A, C, L0, W, omega):
    N = m.ker_basis(sp.Matrix.vstack(C, C * A))
    AN = A * N
    k = N.cols
    n = A.rows
    Wp = m.ker_basis(W)
    Y = m.ker_basis(sp.Matrix.hstack(N * Wp, AN * Wp).T)
    return N, AN, k, n, Y


def cond_E(Y, N, AN, k, omega):
    if Y.cols == 0:
        return False
    X = sp.Matrix([[sum(Y[i, j] * N[i, c] for i in range(N.rows)) for c in range(k)] for j in range(Y.cols)])
    G = sp.Matrix([[sum(Y[i, j] * AN[i, c] for i in range(N.rows)) for c in range(k)] for j in range(Y.cols)])
    if X.rank() < omega or G.rank() < omega:
        return False
    # E_lambda surjective for all lambda <=> the omega-minors of M(lambda) are coprime
    M = sp.Matrix([[sp.expand(lam * X[j, c] - G[j, c]) for c in range(k)] for j in range(Y.cols)])
    ms = [x for x in minors(M, omega) if sp.simplify(x) != 0]
    if not ms:
        return False
    g = ms[0]
    for x in ms[1:]:
        g = sp.gcd(g, x)
        if sp.simplify(g).is_number:
            return True
    return bool(sp.simplify(g).is_number or sp.Poly(g, lam).degree() == 0)


def cond_Z(Y, N, AN, k, omega):
    # (x,0) in T_W: the admissible row y has (y^T AN) = 0 ; similarly (0,y): y^T N = 0
    rows = []
    rowsH, rowsA = [], []
    for j in range(Y.cols):
        y = Y[:, j].T
        rowsH.append([sum(y[0, i] * N[i, c] for i in range(N.rows)) for c in range(k)])
        rowsA.append([sum(y[0, i] * AN[i, c] for i in range(N.rows)) for c in range(k)])
    Hm = sp.Matrix(rowsH)
    Am = sp.Matrix(rowsA)
    # zero-partner: rows of Am span W AND rows of Hm span W (as vectors in W)
    return Hm.rank() == omega and Am.rank() == omega and False   # placeholder replaced below


def cond_Z_true(Y, N, AN, k, omega):
    """(Z): among rows with g-part 0 there are omega independent h-parts, and vice versa."""
    Hm = sp.Matrix([[sum(Y[i, j] * N[i, c] for i in range(N.rows)) for c in range(k)] for j in range(Y.cols)])
    Am = sp.Matrix([[sum(Y[i, j] * AN[i, c] for i in range(N.rows)) for c in range(k)] for j in range(Y.cols)])
    # select rows of Am that vanish -> corresponding Hm rows give candidates for (x,0)
    zero_g = [j for j in range(Y.cols) if Am.row(j).norm() == 0]
    zero_h = [j for j in range(Y.cols) if Hm.row(j).norm() == 0]
    if not zero_g or not zero_h:
        return False
    return sp.Matrix([Hm.row(j) for j in zero_g]).rank() == omega and \
        sp.Matrix([Am.row(j) for j in zero_h]).rank() == omega


def cond_F(A, C, L0, W, omega, m_rows, tries=6, seed=0):
    N, AN, k, n, Y = data(A, C, L0, W, omega)
    fixed = L0 * sp.Matrix.hstack(N, AN)
    for i in range(fixed.rows):
        if (sp.Matrix.vstack(W, fixed[i, 0:k]).rank() > omega
                or sp.Matrix.vstack(W, fixed[i, k:2 * k]).rank() > omega):
            return None
    rng = random.Random(seed)
    taus = sp.symbols(f"w0:{m_rows * Y.cols}")
    for t in range(tries):
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
        ms = [x for x in minors(P, omega) if sp.simplify(x) != 0]
        if not ms:
            continue
        g = ms[0]
        for x in ms[1:]:
            g = sp.gcd(g, x)
            if sp.simplify(g).is_number:
                return True
        if sp.simplify(g).is_number or sp.Poly(g, lam).degree() == 0:
            return True
    return False


def main() -> None:
    print("=" * 78)
    print("gray-band search: (E) true, (Z) false  ->  is (F) possible?")
    print("=" * 78)
    rng = random.Random(77)
    gray = feasible = 0
    for trial in range(8):
        n, k_target = (6, 3), 3
        n = 6
        C = sp.zeros(2, n)
        C[0, n - 2] = 1
        C[1, n - 1] = 1
        A = sp.Matrix(n, n, lambda i, j: rng.randint(-2, 2))
        if sp.Matrix.vstack(C, C * A).rank() != 4:
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
                N2, AN2, k2, n2, Y = data(A, C, L0, W, omega)
                E = cond_E(Y, N2, AN2, k2, omega)
                Z = cond_Z_true(Y, N2, AN2, k2, omega)
                if E and not Z:
                    gray += 1
                    f = cond_F(A, C, L0, W, omega, m_rows=4, tries=4, seed=trial)
                    print(f"  trial={trial} omega={omega}: dim T_W={Y.cols}, E=True Z=False, "
                          f"F={f}")
                    if f:
                        feasible += 1
    print(f"\ngray-band cases = {gray}, among them feasible = {feasible}")


if __name__ == "__main__":
    main()
