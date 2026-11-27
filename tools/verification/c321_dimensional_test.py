"""Is feasibility determined by the dimensions (k, d, s, r) alone?

The subspace reduction turns DEC into a question about a subspace W of
T = row[N | AN] with W_0 <= W <= T and dim(W/W_0) <= r.  The parameters are

  k = dim ker[C; CA],  d = rank[N | AN],  s = dim W_0,  r = q - r_0.

If feasibility depended only on (k, d, s, r), q1 would reduce to a finite
combinatorial question.  This script looks for counterexamples: instances with
equal (k, d, s, r) but different feasibility.

Exact (5a)/(5b) test, random search.  NOT a proof.
"""

import random

import sympy as sp

import c320_subspace_reduction as S


def params_and_feasibility(A, C, L0, q, rng, tries=25):
    n = A.shape[0]
    r0 = L0.rows
    r = q - r0
    CA = C * A
    N = S.nullspace_basis(sp.Matrix.vstack(C, CA))
    k = N.cols
    M = sp.Matrix.hstack(N, A * N)
    T = S.rowspace_basis(M)
    d = T.rank()
    W0 = S.rowspace_basis(L0 * M)
    s = W0.rank()
    if r < 0:
        return (k, d, s, r), None
    for _ in range(tries):
        R = sp.Matrix([[rng.randint(-3, 3) for _ in range(n)] for _ in range(r)])
        ok, _why = S.feasible(A, C, sp.Matrix.vstack(L0, R))
        if ok:
            return (k, d, s, r), True
    return (k, d, s, r), False


def main():
    rng = random.Random(424242)
    groups = {}
    for _ in range(40):
        n = rng.choice([5, 6])
        p = rng.choice([1, 2])
        r0 = rng.choice([1, 2])
        A = sp.Matrix([[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)])
        C = sp.Matrix([[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)])
        if C.rank() < p:
            continue
        L0 = sp.Matrix([[rng.randint(-2, 2) for _ in range(n)] for _ in range(r0)])
        if L0.rank() < r0:
            continue
        for r in (1, 2):
            q = r0 + r
            if q > n:
                continue
            key, feas = params_and_feasibility(A, C, L0, q, rng)
            if feas is None:
                continue
            groups.setdefault(key, set()).add(feas)
    mixed = {k: v for k, v in groups.items() if len(v) > 1}
    print(f"parameter groups: {len(groups)}; groups with both outcomes: {len(mixed)}")
    for key, vals in sorted(mixed.items())[:8]:
        print(f"  (k,d,s,r)={key}: outcomes {sorted(vals)}")
    pure = {k: v for k, v in groups.items() if len(v) == 1}
    print(f"groups with a single outcome: {len(pure)}")
    for key, vals in sorted(pure.items())[:8]:
        print(f"  (k,d,s,r)={key}: {sorted(vals)}")


if __name__ == '__main__':
    main()
