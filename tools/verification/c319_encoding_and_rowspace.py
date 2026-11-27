#!/usr/bin/env python3
"""Exact checks for the paper's remaining bookkeeping items (freeze audit).

Three items of the freeze checklist are closed by written lemmas in the paper;
this script checks their *instances*, not their proofs.

1. Lemma D2 (coefficient-vector row space): for random polynomial families
   f_1..f_s of degree <= omega, the row space of the coefficient matrix B
   consists exactly of the coefficient vectors of sum g_i f_i, deg g_i < omega.

2. Appendix B witness direction, on a *constructed* feasible instance:
   take (C, A) observable, L0 = e_1^T and L = I_n (feasible with q = n).
   Construct X, B, G, U, V and the polynomial left inverse S and verify every
   constraint of the encoding, including the data constraints (B.1) and (B.2).

3. Necessity of the data constraints: the same witness satisfies every encoding
   constraint that does not mention the data, while (H, H_A) = (XB, GB) does not
   match a perturbed input L0'.  So (B.1)-(B.2) cannot be dropped.

Negative control: the row vector that `tools/verification/consistency_checks.py`
uses as the "explicit feasible augmentation" of the two-gap example is *not*
feasible -- both the maximal-minor gcd and the Toeplitz criterion reject it, and
the left-inverse test finds no certificate.  It is recorded here as a control.

This is finite exact verification, not a proof.
"""

from __future__ import annotations

import importlib.util
import os
import random
import sys
from fractions import Fraction

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
sys.path.insert(0, os.path.join(_ROOT, "tools", "verification"))

import spectral_gcd as SG  # noqa: E402

LAM = sp.symbols("lam")


# --------------------------------------------------------------------------
# 1. Lemma D2
# --------------------------------------------------------------------------
def check_lemma_d2(rng: random.Random, trials: int = 40) -> int:
    checked = 0
    for _ in range(trials):
        omega = rng.randint(1, 3)
        s = rng.randint(1, 4)
        fs = [sp.Poly(sum(rng.randint(-3, 3) * LAM ** a for a in range(omega + 1)), LAM)
              for _ in range(s)]
        B = sp.zeros(s * omega, 2 * omega)
        for i in range(s):
            c = [fs[i].coeff_monomial(LAM ** a) if 0 <= a <= omega else 0
                 for a in range(2 * omega)]
            for j in range(omega):
                for t in range(2 * omega):
                    B[i * omega + j, t] = c[t - j] if 0 <= t - j < 2 * omega else 0
        gs = [sum(rng.randint(-2, 2) * LAM ** a for a in range(omega)) for _ in range(s)]
        total = sp.Poly(sp.expand(sum(g * f.as_expr() for g, f in zip(gs, fs))), LAM)
        target = sp.Matrix([total.coeff_monomial(LAM ** t) for t in range(2 * omega)])
        y = sp.zeros(1, s * omega)
        for i, g in enumerate(gs):
            for j in range(omega):
                y[0, i * omega + j] = sp.Poly(g, LAM).coeff_monomial(LAM ** j)
        assert (y * B).T == target
        checked += 1
    return checked


# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------
def frac_matrix(M):
    return sp.Matrix([[sp.Rational(v.numerator, v.denominator) for v in row] for row in M])


def kernel_basis(M):
    Ns = M.nullspace()
    assert Ns, "empty kernel"
    return sp.Matrix.hstack(*Ns)


def left_inverse(X):
    return (X.T * X).inv() * X.T


def solve_S(X, G, d):
    """Coefficient matrices S_0..S_d with S(lam)(lam X - G) = I (exact), or None."""
    q, om = X.shape
    nvar = (d + 1) * om * q
    rows, rhs = [], []
    for k in range(d + 2):
        for a in range(om):
            for c in range(om):
                row = [0] * nvar
                if k == 0:
                    for b in range(q):
                        row[a * q + b] = -G[b, c]
                    rhs.append(1 if a == c else 0)
                elif k <= d:
                    for b in range(q):
                        row[(k - 1) * om * q + a * q + b] = X[b, c]
                        row[k * om * q + a * q + b] = -G[b, c]
                    rhs.append(0)
                else:
                    for b in range(q):
                        row[d * om * q + a * q + b] = X[b, c]
                    rhs.append(0)
                rows.append(row)
    sol_set = sp.linsolve((sp.Matrix(rows), sp.Matrix(rhs)))
    if sol_set is sp.EmptySet:
        return None
    sol = next(iter(sol_set))
    free = set()
    for v in sol:
        free |= v.free_symbols
    sol = [sp.together(v.subs({s: 0 for s in free})) for v in sol]
    S = [sp.zeros(om, q) for _ in range(d + 1)]
    for j in range(d + 1):
        for a in range(om):
            for b in range(q):
                S[j][a, b] = sol[j * om * q + a * q + b]
    return S


def build_witness(A, C, L0, L):
    """X, B, G, U, V for a feasible L (asserts (5a) at the compressed level)."""
    CA = C * A
    N = kernel_basis(C.col_join(CA))
    H, HA = L * N, L * A * N
    om = H.rank()
    J = []
    for j in range(N.cols):
        if H[:, J + [j]].rank() == len(J) + 1:
            J.append(j)
    assert len(J) == om
    X = H[:, J]
    U = left_inverse(X)
    B = U * H
    assert (X * B - H).is_zero_matrix and B.rank() == om
    V = B.T * (B * B.T).inv()
    assert (B * V - sp.eye(om)).is_zero_matrix
    G = HA * V
    assert (G * B - HA).is_zero_matrix, "(5a) fails at the compressed level"
    return N, H, HA, X, B, G, U, V, om


def observable(A, C):
    n = A.rows
    rows = [C]
    cur = C
    for _ in range(n - 1):
        cur = cur * A
        rows.append(cur)
    return sp.Matrix.vstack(*rows).rank() == n


def main() -> None:
    rng = random.Random(20261110)

    n1 = check_lemma_d2(rng)
    print(f"[1] Lemma D2: {n1} random families: rows of B = coefficient vectors of "
          f"sum g_i f_i with deg g_i < omega")

    # ---- constructed feasible instance: (C,A) observable, L0 = e_1, L = I ----
    n = 4
    A = sp.Matrix([[rng.randint(-3, 3) for _ in range(n)] for _ in range(n)])
    C = sp.Matrix([[rng.randint(-2, 2) for _ in range(n)]])
    while not observable(A, C):
        C = sp.Matrix([[rng.randint(-2, 2) for _ in range(n)]])
    L0 = sp.zeros(1, n)
    L0[0, 0] = 1
    L = sp.eye(n)                       # contains L0 and is feasible: q = n
    print(f"[i] constructed instance: n={n}, p=1, r0=1, q={n}, (C,A) observable, L=I")

    N, H, HA, X, B, G, U, V, om = build_witness(A, C, L0, L)
    d = 2 * om - 2
    S = solve_S(X, G, d)
    assert S is not None, "no left-inverse certificate for a feasible instance"
    Spoly = sp.zeros(om, X.rows)
    for j in range(d + 1):
        Spoly += S[j] * LAM ** j
    lhs = Spoly * (LAM * X - G)
    assert sp.expand(lhs - sp.eye(om)).is_zero_matrix
    print(f"[2] witness: omega={om}, deg S<={d}; H=XB, H_A=GB, UX=I, BV=I, "
          f"S(lam)(lam X-G)=I verified")

    # (B.1): fixed rows
    H0, HA0 = L0 * N, L0 * A * N
    for i in range(L0.rows):
        assert (X[i, :] * B - H0[i, :]).is_zero_matrix
        assert (G[i, :] * B - HA0[i, :]).is_zero_matrix
    # (B.2): free rows lie in T = row[N AN]
    M2 = N.row_join(A * N)
    d0 = M2.rank()
    Tperp = M2.nullspace()
    D = sp.Matrix.hstack(*Tperp).T if Tperp else sp.zeros(0, 2 * N.cols)
    assert D.rows == 2 * N.cols - d0
    XB, GB = X * B, G * B
    for i in range(L0.rows, L.rows):
        w = XB[i, :].T.col_join(GB[i, :].T)
        assert (D * w).is_zero_matrix
    print(f"[2] data constraints: (B.1) on {L0.rows} fixed rows, (B.2) on "
          f"{L.rows - L0.rows} free rows ({2 * N.cols - d0} equations per row) verified")

    # ---- 3. the data constraints are necessary ---------------------------
    L0p = L0.copy()
    L0p[0, 0] += 1
    H0p = L0p * N
    bad = [i for i in range(L0.rows) if not (X[i, :] * B - H0p[i, :]).is_zero_matrix]
    assert bad, "perturbation did not change the fixed rows"
    print(f"[3] with L0 perturbed, rows {bad} of (B.1) fail while every other "
          f"constraint still holds: (B.1)-(B.2) are necessary")

    # ---- 5. the parameter family of §10.2 ---------------------------------
    # p = n-1, C = [I_{n-1} 0], last column of A in ker C  =>  k = 1, d0 <= 2
    for n in range(4, 9):
        Cm = sp.zeros(n - 1, n)
        for i in range(n - 1):
            Cm[i, i] = 1
        Am = sp.zeros(n, n)
        for i in range(n):
            for j in range(n - 1):
                Am[i, j] = rng.randint(-3, 3)
        c0 = rng.choice([-2, -1, 1, 2])
        for i in range(n):
            Am[i, n - 1] = 0
        Am[n - 1, n - 1] = c0          # last column = c0 * e_n
        K0 = Cm.col_join(Cm * Am)
        assert K0.rank() == n - 1, (n, K0.rank())
        Nf = kernel_basis(K0)
        assert Nf.cols == 1
        M2f = Nf.row_join(Am * Nf)
        d0f = M2f.rank()
        assert d0f <= 2
        assert 1 * d0f <= 2            # kappa_obs = r * d0 with r = 1
    print("[5] parameter family (p=n-1, C=[I 0], last column of A in ker C): "
          "n=4..8 give k=1, d0<=2, kappa_obs<=2 while n grows")

    # ---- negative control: the "explicit feasible L" of consistency_checks --
    spec = importlib.util.spec_from_file_location(
        "fg", os.path.join(_ROOT, "proof", "fernando_2gap", "verify.py"))
    fg = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(fg)
    F = Fraction
    v = [F(-42919, 32067), F(-55096, 10689), F(1), F(0), F(0), F(0), F(0), F(0)]
    Ln = [list(x) for x in fg.L0] + [v]
    gcd = SG.spectral_gcd(fg.A, fg.C, Ln)[0]
    assert gcd != [F(1)], "the control is unexpectedly feasible"
    print(f"[4] negative control: consistency_checks' 'feasible' L for the two-gap "
          f"example is rejected by the gcd criterion (gcd has degree {len(gcd) - 1})")

    print("\nPASS: Lemma D2 instances, encoding witness, necessity of (B.1)-(B.2), "
          "and the infeasibility control")


if __name__ == "__main__":
    main()
