"""proof/rho0_layer/verify.py

Re-verifies `docs/02_theorems_proven.md` B.3:

    rho = 0  <=>  V subset J
    and then   (5a) <=> S subset J and SA subset J,   and (5b) holds automatically.

Run:  python proof/rho0_layer/verify.py
"""
import os
import random
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools", "exact_linalg"))
import audit_independent as AI  # noqa: E402


def J_of(A, C):
    return AI.row_basis(AI.vstack([C, AI.mul(C, A)]))


def main():
    rng = random.Random(5)
    print("=" * 92)
    print("B.4  rho = 0  <=>  V subset J ;  and then (5b) is automatic")
    print("=" * 92)
    ok = tot = 0
    for _ in range(10):
        n = rng.choice([3, 4])
        p = rng.choice([1, 2])
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        if AI.rank(C) != p:
            continue
        J = J_of(A, C)
        j = AI.rank(J)
        # T = a random combination of rows of J, i.e. an S inside J
        r = rng.choice([1, 2])
        coeffs = [[Fr(rng.randint(-2, 2)) for _ in range(j)] for _ in range(r)]
        S = [[sum(coeffs[i][k] * J[k][t] for k in range(j)) for t in range(n)] for i in range(r)]
        S = AI.row_basis(S)
        r = len(S)
        if r == 0:
            continue
        sa_in_j = (AI.rank(AI.vstack([J, AI.mul(S, A)])) == j)
        # L0 = S
        L0 = S
        cond5a = AI.cond_5a_orig(A, C, L0)
        cond5b = AI.cond_5b_orig(A, C, L0)
        q = AI.rank(L0)
        # rho of V = row(S): should be 0 since S subset J
        Nv = AI.nullspace(AI.vstack([C, AI.mul(C, A)]))
        N = [[Nv[k][i] for k in range(len(Nv))] for i in range(n)]
        rho = AI.rank(AI.mul(L0, N))
        tot += 1
        good = (rho == 0) and (cond5b is True) and (cond5a == sa_in_j)
        ok += good
        print(f"  n={n} p={p} r={r} rho={rho} (5a)={cond5a} SA in J={sa_in_j} "
              f"(5b)={cond5b}  {'OK' if good else 'MISMATCH'}")
    print()
    print(f"passed {ok}/{tot}")
    print("note: rho=0 <=> V subset J is immediate; the content here is that (5b) is")
    print("      automatic once S and SA sit inside J, and that (5a) is exactly SA subset J.")


if __name__ == "__main__":
    main()
