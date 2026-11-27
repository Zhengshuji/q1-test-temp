"""The iterated common-projection core S_* of the subspace reduction.

Construction.  T = row[N | AN] <= R^{2k}.  Put S_0 = R^{1 x k} (all of k-space),
T_0 = T, and
    S_{j+1} = pi_1(T_j) ∩ pi_2(T_j),   T_{j+1} = T ∩ (S_{j+1} x S_{j+1}).
The sequence S_j is decreasing and stabilizes after at most k strict drops.

Claim (to be checked).  Every feasible W satisfies W <= T ∩ (S_* x S_*), where S_*
is the terminal space.  Hence the whole search can be restricted to this core, and
dim S_* <= rank(AN) <= k.

This script builds S_* by exact rational linear algebra on random instances, and
checks the claim on every feasible witness it can find, together with dim S_* <= rank(AN).

NOT a proof: finitely many instances.  Every conclusion is an exact rank computation.
"""

import random

import sympy as sp

import c320_subspace_reduction as S


def rowspace(M):
    return S.rowspace_basis(M)


def proj1(Tb, k):
    """pi_1 of a row space: first k coordinates of a spanning set."""
    if Tb.rows == 0:
        return sp.zeros(0, k)
    return rowspace(Tb[:, 0:k])


def proj2(Tb, k):
    if Tb.rows == 0:
        return sp.zeros(0, k)
    return rowspace(Tb[:, k:2 * k])


def intersect(A, B):
    """Basis of row(A) ∩ row(B)."""
    if A.rows == 0 or B.rows == 0:
        return sp.zeros(0, A.cols)
    # rows x with x = c A = d B  <=>  (c, -d) in kernel of [A^T | -B^T]
    n = A.cols
    M = sp.Matrix.hstack(A.T, -B.T)
    ns = M.nullspace()
    if not ns:
        return sp.zeros(0, n)
    rows = []
    for v in ns:
        c = sp.Matrix(1, A.rows, list(v[:A.rows]))
        rows.append(c * A)
    out = sp.Matrix.vstack(*rows)
    return rowspace(out)


def box(Sb, k):
    """The subspace S x S  <= R^{2k} for a basis Sb of S (rows)."""
    if Sb.rows == 0:
        return sp.zeros(0, 2 * k)
    left = sp.Matrix.hstack(Sb, sp.zeros(Sb.rows, k))
    right = sp.Matrix.hstack(sp.zeros(Sb.rows, k), Sb)
    return rowspace(sp.Matrix.vstack(left, right))


def core(Tb, k, verbose=False):
    Sm = rowspace(sp.eye(k))          # S_0 = R^k
    Tj = Tb
    hist = [Sm.rank()]
    for _ in range(k + 2):
        Snext = intersect(proj1(Tj, k), proj2(Tj, k))
        Tnext = intersect(Tb, box(Snext, k))
        if Snext.rank() == Sm.rank() and Tnext.rank() == Tj.rank():
            Sm, Tj = Snext, Tnext
            break
        Sm, Tj = Snext, Tnext
        hist.append(Sm.rank())
    if verbose:
        print("   dim path:", hist, "-> dim S*=", Sm.rank(), "dim core=", Tj.rank())
    return Sm, Tj


def main():
    rng = random.Random(7311)
    fails = 0
    rows = []
    for _ in range(12):
        n = rng.choice([5, 6, 7])
        p = rng.choice([1, 2])
        r0 = rng.choice([1, 2])
        A = sp.Matrix([[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)])
        C = sp.Matrix([[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)])
        if C.rank() < p:
            continue
        L0 = sp.Matrix([[rng.randint(-2, 2) for _ in range(n)] for _ in range(r0)])
        if L0.rank() < r0:
            continue
        N = S.nullspace_basis(sp.Matrix.vstack(C, C * A))
        k = N.cols
        if k == 0:
            continue
        M = sp.Matrix.hstack(N, A * N)
        Tb = rowspace(M)
        ell = (A * N).rank()
        Sm, Tj = core(Tb, k)
        lst = Sm.rank()
        if lst > ell:
            fails += 1
            print(f"  FAIL dim S*={lst} > rank(AN)={ell}")
        # feasible witnesses: check W <= T ∩ (S* x S*)
        found = 0
        for r in range(1, min(n - r0, 3) + 1):
            for _ in range(40):
                R = sp.Matrix([[rng.randint(-3, 3) for _ in range(n)] for _ in range(r)])
                L = sp.Matrix.vstack(L0, R)
                ok, _why = S.feasible(A, C, L)
                if not ok:
                    continue
                found += 1
                W = rowspace(L * M)
                inside = sp.Matrix.vstack(W, Tj).rank() == Tj.rank()
                if not inside:
                    fails += 1
                    print(f"  FAIL feasible W not inside the core (n={n}, p={p}, r0={r0}, r={r})")
                break
        rows.append((n, p, r0, k, ell, lst, Tj.rank(), found))
    print(" n  p r0  k ell dimS* dimCore  witnesses")
    for t in rows:
        print("  %2d %2d %2d %2d %3d %5d %7d %10d" % t)
    print("\nFAILURES:", fails)


if __name__ == '__main__':
    main()
