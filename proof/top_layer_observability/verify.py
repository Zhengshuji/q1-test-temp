"""proof/top_layer_observability/verify.py

Re-verifies `docs/02_theorems_proven.md` B.4:

    V = C^n satisfies (5b)  <=>  A^T has no eigenvector lying in K = ker[C;CA].

For A diagonal with distinct eigenvalues the left eigenvectors are e_i, so the criterion
becomes:  every column of [C;CA] is nonzero.  This is checked exactly against the raw
(5b) condition.

Run:  python proof/top_layer_observability/verify.py
"""
import os
import random
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools", "exact_linalg"))
import audit_independent as AI  # noqa: E402


def main():
    rng = random.Random(31)
    print("=" * 96)
    print("B.5  V=C^n feasible  <=>  no left eigenvector of A in K  (A diagonal, distinct)")
    print("=" * 96)
    ok = tot = 0
    for _ in range(12):
        n = rng.choice([3, 4, 5])
        p = rng.choice([1, 2])
        lam = rng.sample(range(1, 40), n)                      # distinct eigenvalues
        A = [[Fr(lam[i]) if i == j else Fr(0) for j in range(n)] for i in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        if AI.rank(C) != p:
            continue
        M = AI.vstack([C, AI.mul(C, A)])
        # criterion: every column of [C;CA] nonzero  <=> no e_i with e_i C = e_i CA = 0
        cols = [[M[k][i] for k in range(len(M))] for i in range(n)]
        crit = all(any(x != 0 for x in col) for col in cols)
        I = AI.identity(n) if hasattr(AI, "identity") else [[Fr(1) if i == j else Fr(0) for j in range(n)] for i in range(n)]
        raw = AI.cond_5b_orig(A, C, I)
        tot += 1
        good = (crit == raw)
        ok += good
        print(f"  n={n} p={p} lambdas={lam[:4]}... criterion={crit} raw(5b)={raw} "
              f"{'OK' if good else 'MISMATCH'}")
    print()
    print(f"passed {ok}/{tot}")


if __name__ == "__main__":
    main()
