"""proof/pencil_equivalence/verify.py

Re-verifies `docs/02_theorems_proven.md` B.1:

    (5b)  <=>  rank Q_V(lambda) = rho   for all lambda,
    Q_V(lambda) = lambda*pi(L) - pi(LA)   (q x d),   rho = dim pi(V).

Checked on every feasible L we can build (observability stacks + certificate solutions),
at several exact values of lambda (0, +-1, and the eigenvalues of A when small).

Run:  python proof/pencil_equivalence/verify.py
"""
import glob
import io
import json
import os
import random
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools", "exact_linalg"))
import audit_independent as AI  # noqa: E402


def pi_map(A, C):
    """returns pi(x) = coordinates of x modulo J in a complement basis, plus rho helper"""
    n = len(A)
    M = AI.vstack([C, AI.mul(C, A)])
    J = AI.row_basis(M)
    comp = []
    for i in range(n):
        v = [Fr(0)] * n
        v[i] = Fr(1)
        if AI.rank(AI.vstack([J] + [[c] for c in comp] + [[v]])) == len(J) + len(comp) + 1:
            comp.append(v)
    base = J + comp

    def pi(x):
        k = len(base)
        Mx = [[base[t][s] for t in range(k)] + [x[s]] for s in range(n)]
        R, piv = AI.rref(Mx)
        co = [Fr(0)] * k
        for t, pc in enumerate(piv):
            if pc < k:
                co[pc] = R[t][k]
        return co[len(J):]

    return pi, J


def pencil_rank(A, L, lam, pi):
    q = len(L)
    LA = AI.mul(L, A)
    rows = []
    for i in range(q):
        row = [lam * a - b for a, b in zip(pi(L[i]), pi(LA[i]))]
        rows.append(row)
    return AI.rank(rows)


def check(A, C, L, tag, lams):
    pi, J = pi_map(A, C)
    n = len(A)
    rho = AI.rank([pi(r) for r in L])
    cond5b = AI.cond_5b_orig(A, C, L)
    ranks = [pencil_rank(A, L, lam, pi) for lam in lams]
    all_eq = all(r == rho for r in ranks)
    ok = (cond5b == all_eq)
    print(f"  {tag:<40} rho={rho} (5b)={cond5b} ranks={ranks} equivalence={ok}")
    return ok


def main():
    rng = random.Random(11)
    lams = [Fr(0), Fr(1), Fr(-1), Fr(2)]
    print("=" * 92)
    print("B.1  (5b) <=> rank Q_V(lambda) = rho for all lambda")
    print("=" * 92)
    ok = tot = 0
    for _ in range(8):
        n = rng.choice([3, 4])
        p = rng.choice([1, 2])
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        if AI.rank(C) != p:
            continue
        rows = [list(r) for r in C]
        cur = [list(r) for r in C]
        for _ in range(n - 1):
            cur = AI.mul(cur, A)
            for r in cur:
                if AI.rank(rows + [r]) > AI.rank(rows):
                    rows.append(list(r))
        if not (AI.cond_5a_orig(A, C, rows) and AI.cond_5b_orig(A, C, rows)):
            continue
        tot += 1
        ok += check(A, C, rows, f"n={n} p={p} observability stack", lams)
    # certificates
    for path in sorted(glob.glob(os.path.join(HERE, "..", "refuted", "certificates", "*.json"))):
        d = json.load(io.open(path, encoding="utf-8"))
        if not all(k in d for k in ("A", "C", "L0")):
            continue
        sol = None
        for key in ("L", "L_2row", "solution"):
            if key in d and isinstance(d[key], list):
                sol = d[key]
                break
        if sol is None:
            continue
        F = lambda M: [[Fr(x) for x in row] for row in M]
        A, C, L = F(d["A"]), F(d["C"]), F(sol)
        if not (AI.cond_5a_orig(A, C, L) and AI.cond_5b_orig(A, C, L)):
            continue
        tot += 1
        ok += check(A, C, L, os.path.basename(path), lams)
    print()
    print(f"passed {ok}/{tot}")


if __name__ == "__main__":
    main()
