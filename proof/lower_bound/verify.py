"""proof/lower_bound/verify.py

Re-verifies the statements of `docs/02_theorems_proven.md` section A:

    A.1  q = rho + c
    A.2  c >= max(c0, 1)
    A.3  q >= max(r + eps,  rho + max(c0, 1))

for EVERY feasible L we can construct.  The inequalities are asserted for all feasible
solutions, so a single feasible L per instance suffices; we use the observability stack
L = [C; CA; ...; CA^{n-1}], which is always feasible (its row space is A-invariant, hence
(5a) holds, and (5b) holds by Cayley-Hamilton).

Run:  python proof/lower_bound/verify.py
"""
import io
import os
import random
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools", "exact_linalg"))
import audit_independent as AI  # noqa: E402


def observability_stack(A, C):
    rows = [list(r) for r in C]
    cur = [list(r) for r in C]
    for _ in range(len(A) - 1):
        cur = AI.mul(cur, A)
        for r in cur:
            if AI.rank(rows + [r]) > AI.rank(rows):
                rows.append(list(r))
    return rows


def invariants(A, C, L):
    n = len(A)
    J = AI.row_basis(AI.vstack([C, AI.mul(C, A)]))
    j = AI.rank(J)
    Nv = AI.nullspace(AI.vstack([C, AI.mul(C, A)]))
    N = [[Nv[k][i] for k in range(len(Nv))] for i in range(n)]
    q = AI.rank(L)
    rho = AI.rank(AI.mul(L, N))
    c = q + j - AI.rank(AI.vstack([L, J]))
    return q, rho, c, j


def main():
    rng = random.Random(2027)
    ok = tot = 0
    print("=" * 88)
    print("A.1  q = rho + c      A.2  c >= max(c0,1)      A.3  q >= max(r+eps, rho+max(c0,1))")
    print("=" * 88)
    for t in range(12):
        n = rng.choice([3, 4, 5])
        p = rng.choice([1, 2])
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        if AI.rank(C) != p:
            continue
        L = observability_stack(A, C)
        if AI.rank(L) != len(L):
            continue
        if not (AI.cond_5a_orig(A, C, L) and AI.cond_5b_orig(A, C, L)):
            continue
        # choose L0 = first row of L  (so that L is a feasible extension of L0)
        L0 = [L[0]]
        r = len(L0)
        J = AI.row_basis(AI.vstack([C, AI.mul(C, A)]))
        j = AI.rank(J)
        S = AI.row_basis(L0)
        c0 = len(S) + j - AI.rank(AI.vstack([S, J]))
        eps = 0 if (AI.cond_5a_orig(A, C, L0) and AI.cond_5b_orig(A, C, L0)) else 1
        q, rho, c, _ = invariants(A, C, L)
        tot += 1
        a1 = (q == rho + c)
        a2 = (c >= max(c0, 1))
        a3 = (q >= max(r + eps, rho + max(c0, 1)))
        ok += (a1 and a2 and a3)
        print(f"  n={n} p={p} q={q} rho={rho} c={c} c0={c0} eps={eps} "
              f"| A.1 {a1}  A.2 {a2}  A.3 {a3}")
    print()
    print(f"passed {ok}/{tot} feasible observability stacks")
    print("note: each row is ONE feasible L; A.1-A.3 are asserted for every feasible L,")
    print("      so this checks the identities on a sample of exact feasible solutions.")


def check_certificates():
    """also check A.1-A.3 on the exact certificates that carry an explicit solution"""
    import glob
    import json
    cert_dir = os.path.join(HERE, '..', 'refuted', 'certificates')
    ok = tot = 0
    print()
    print('=' * 88)
    print('A.1-A.3 on certificate solutions (these have eps = 1 typically)')
    print('=' * 88)
    for path in sorted(glob.glob(os.path.join(cert_dir, '*.json'))):
        d = json.load(io.open(path, encoding='utf-8'))
        if not all(k in d for k in ('A', 'C', 'L0')):
            continue
        sol = None
        for key in ('L', 'L_2row', 'solution'):
            if key in d and isinstance(d[key], list):
                sol = d[key]; break
        if sol is None:
            continue
        F = lambda M: [[Fr(x) for x in row] for row in M]
        A, C, L0, L = F(d['A']), F(d['C']), F(d['L0']), F(sol)
        n = len(A)
        J = AI.row_basis(AI.vstack([C, AI.mul(C, A)]))
        j = AI.rank(J)
        S = AI.row_basis(L0)
        r = len(L0)
        c0 = len(S) + j - AI.rank(AI.vstack([S, J]))
        eps = 0 if (AI.cond_5a_orig(A, C, L0) and AI.cond_5b_orig(A, C, L0)) else 1
        feas = AI.cond_5a_orig(A, C, L) and AI.cond_5b_orig(A, C, L)
        if not feas:
            print('  skip (solution not feasible):', os.path.basename(path)); continue
        q, rho, c, _ = invariants(A, C, L)
        tot += 1
        a1 = (q == rho + c); a2 = (c >= max(c0, 1)); a3 = (q >= max(r + eps, rho + max(c0, 1)))
        ok += (a1 and a2 and a3)
        print(f'  {os.path.basename(path):<48} q={q} rho={rho} c={c} c0={c0} eps={eps} '
              f'| A.1 {a1} A.2 {a2} A.3 {a3}')
    print()
    print(f'passed {ok}/{tot} certificate solutions')


if __name__ == '__main__':
    main()
    check_certificates()
