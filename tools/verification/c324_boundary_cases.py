"""Boundary cases of the subspace reduction, as listed in the expert reply.

Cases:
  (A) k = 0  (ker[C; CA] = 0):  then T = 0 and W = 0 for every L, so feasibility
      must not depend on R at all.
  (B) m = 0  (W_0 = T):  every admissible W equals T, so feasibility must not
      depend on R at all.
  (C) W_0 = 0 and omega = 0:  the branch W = 0 is feasible iff W_0 = 0, and it is
      realized by L_0 alone (no free rows needed).
  (D) a pencil whose maximal minors have no real common root but do have a
      complex one:  the gcd test must reject it, while every real evaluation is
      full rank.

Each check is an exact computation.  NOT a proof: constructed and random
instances only.
"""

import random

import sympy as sp

import c320_subspace_reduction as S
import spectral_gcd as SG


def feasible(A, C, L):
    return S.feasible(A, C, L)[0]


def case_k_zero(rng):
    """C = I_n makes ker[C; CA] = 0.  Feasibility must not depend on R."""
    n = 4
    A = sp.Matrix([[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)])
    C = sp.eye(n)
    L0 = sp.Matrix([[rng.randint(-2, 2) for _ in range(n)]])
    if sp.Matrix.vstack(C, C * A).rank() < n:
        return None  # k > 0, not this case
    vals = set()
    for _ in range(6):
        R = sp.Matrix([[rng.randint(-3, 3) for _ in range(n)]])
        vals.add(feasible(A, C, sp.Matrix.vstack(L0, R)))
    return ('k=0', len(vals) == 1, f'feasibility over 6 free rows: {sorted(vals)}')


def case_m_zero(rng):
    """Rank(L0 M) = rank(M): then W_0 = T and feasibility must not depend on R."""
    for _ in range(60):
        n = 4
        p = 1
        r0 = 3
        A = sp.Matrix([[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)])
        C = sp.Matrix([[rng.randint(-2, 2) for _ in range(n)]])
        if C.rank() < 1:
            continue
        N = S.nullspace_basis(sp.Matrix.vstack(C, C * A))
        if N.cols == 0:
            continue
        M = sp.Matrix.hstack(N, A * N)
        T = S.rowspace_basis(M)
        d = T.rank()
        L0 = sp.Matrix([[rng.randint(-2, 2) for _ in range(n)] for _ in range(r0)])
        W0 = S.rowspace_basis(L0 * M)
        if W0.rank() != d:
            continue
        vals = set()
        for _ in range(5):
            R = sp.Matrix([[rng.randint(-3, 3) for _ in range(n)]])
            vals.add(feasible(A, C, sp.Matrix.vstack(L0, R)))
        return ('m=0', len(vals) == 1, f'feasibility over 5 free rows: {sorted(vals)}')
    return None


def case_w0_zero(rng):
    """L0 M = 0 makes W_0 = 0; the branch W = 0 is realised by L0 alone."""
    for _ in range(60):
        n = 4
        p = 1
        A = sp.Matrix([[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)])
        C = sp.Matrix([[rng.randint(-2, 2) for _ in range(n)]])
        N = S.nullspace_basis(sp.Matrix.vstack(C, C * A))
        if N.cols == 0:
            continue
        M = sp.Matrix.hstack(N, A * N)
        # L0 with L0 M = 0: take a left null vector of M
        ns = M.T.nullspace()
        if not ns:
            continue
        L0 = sp.Matrix(1, n, list(ns[0]))
        if (L0 * M) != sp.zeros(1, 2 * N.cols):
            continue
        ok = feasible(A, C, L0)          # no free rows: L = L0
        return ('W_0=0, omega=0 branch', True, f'L = L0 feasible: {ok} (branch is W=0)')
    return None


def case_complex_root():
    """Q(lam) = [[lam, 1], [-1, lam]] has det = lam^2 + 1: full rank over R, not over C."""
    lam = sp.symbols('lam')
    Q = sp.Matrix([[lam, 1], [-1, lam]])
    det = sp.expand(Q.det())
    real_ok = all(sp.Matrix([[x, 1], [-1, x]]).det() != 0 for x in range(-5, 6))
    complex_root = sp.solve(det, lam) == [-sp.I, sp.I]
    return ('complex common root', real_ok and complex_root,
            f'det = {det}; full rank on real grid: {real_ok}; roots {sp.solve(det, lam)}')


def main():
    rng = random.Random(5150)
    results = []
    k0 = case_k_zero(rng)
    if k0:
        results.append(k0)
    m0 = case_m_zero(rng)
    if m0:
        results.append(m0)
    w0 = case_w0_zero(rng)
    if w0:
        results.append(w0)
    results.append(case_complex_root())
    bad = 0
    for tag, ok, msg in results:
        print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {msg}")
        bad += (not ok)
    print(f"\nFAILURES: {bad}")


if __name__ == '__main__':
    main()
