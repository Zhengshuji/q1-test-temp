"""proof/cyclic_vector_criterion/verify.py

Proposition (Q1_FOR_EXPERT_9 §4, paper-proved there):

    Assume c0 = 1: S = span{j0}, j0 in J.  Take a complement W of J (dim W = d, W cap J = 0)
    and V = span{j0} + W   (so V + J = C^n and (5a) holds automatically).
    Let T_W : W -> W be the compression of A along J (T_W w = pi_W(wA)) and v_W = pi_W(j0 A).

        V fails (5b)  <=>  v_W lies in a T_W-invariant proper subspace of W
                      <=>  v_W is NOT a cyclic vector of T_W
                      <=>  rank[v_W; v_W T_W; ...; v_W T_W^{d-1}] < d .

For d = 2 the criterion is simply: v_W is an eigenvector of T_W.

Checked exactly (Fractions) against the raw (5b) test, over several complements W per instance
(different W give different v_W and T_W, hence both feasible and infeasible cases).

Run:  python proof/cyclic_vector_criterion/verify.py
"""
import os
import random
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools", "exact_linalg"))
import audit_independent as AI  # noqa: E402


def complements(J, n, rng, trials=5):
    """several complements of J in C^n: lists of d rows, independent mod J"""
    j = len(J)
    d = n - j
    out = []
    for _ in range(trials):
        W = []
        guard = 0
        while len(W) < d and guard < 300:
            guard += 1
            v = [Fr(rng.randint(-3, 3)) for _ in range(n)]
            if AI.rank(AI.vstack([J] + [[w] for w in W] + [[v]])) == j + len(W) + 1:
                W.append(v)
        if len(W) == d:
            out.append(W)
    return out


def coords_in(base, x):
    k = len(base)
    Mx = [[base[t][s] for t in range(k)] + [x[s]] for s in range(len(x))]
    R, piv = AI.rref(Mx)
    co = [Fr(0)] * k
    for t, pc in enumerate(piv):
        if pc < k:
            co[pc] = R[t][k]
    chk = [sum(co[t] * base[t][s] for t in range(k)) for s in range(len(x))]
    return co if chk == list(x) else None


def main():
    rng = random.Random(11)
    print("=" * 100)
    print("c0 = 1, rho = d:   (5b) holds  <=>  v_W is a cyclic vector of T_W")
    print("=" * 100)
    ok = tot = infeas = 0
    for t in range(10):
        n = rng.choice([4, 5, 6])
        p = rng.choice([1, 2])
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        if AI.rank(C) != p:
            continue
        J = AI.row_basis(AI.vstack([C, AI.mul(C, A)]))
        j, d = len(J), n - len(J)
        if d < 2 or j < 1:
            continue
        for j0 in (list(J[0]), [x + y for x, y in zip(J[0], J[-1])]):
            if all(x == 0 for x in j0):
                continue
            j0A = AI.mul([j0], A)[0]
            if AI.rank(AI.vstack([J, [j0A]])) == j:      # v_W = 0 for every W
                continue
            for W in complements(J, n, rng):
                base = W + J

                def piW(x):
                    co = coords_in(base, x)
                    return co[:d] if co is not None else None

                TW = [piW(AI.mul([w], A)[0]) for w in W]
                vW = piW(j0A)
                if vW is None or any(x is None for x in TW):
                    continue
                rows = [list(vW)]
                cur = list(vW)
                for _ in range(d - 1):
                    cur = [sum(cur[i] * TW[i][k] for i in range(d)) for k in range(d)]
                    rows.append(list(cur))
                cyclic = (AI.rank(rows) == d)
                V = [list(j0)] + [list(w) for w in W]
                c5a = AI.cond_5a_orig(A, C, V)
                c5b = AI.cond_5b_orig(A, C, V)
                good = c5a and (c5b == cyclic)
                tot += 1
                ok += good
                infeas += (not c5b)
                print(f"  n={n} p={p} j={j} d={d}  cyclic={cyclic}  (5b)={c5b}  (5a)={c5a}  "
                      f"{'OK' if good else 'MISMATCH'}")
    print()
    print(f"passed {ok}/{tot}   (infeasible cases seen: {infeas})")
    if infeas == 0:
        print("WARNING: no infeasible case in this sample -- the criterion was only tested on its")
        print("         positive side; widen the sample (more complements / larger n) to test it.")


def constructed_negative_case():
    """A hand-built instance where v_W is NOT cyclic -- so (5b) must fail.

    n=4, C=e1, A e1 = e3+e2, A e2 = A e3 = 0, A e4 = e4.
    J = span{e1, e2+e3}, d=2, W = span{e2, e4}, j0 = e1.
    Then T_W = [[0,0],[0,1]], v_W = (1,0):  rank[v_W; v_W T_W] = 1 < 2  -> not cyclic.
    """
    n = 4
    e = [[Fr(1) if i == k else Fr(0) for k in range(n)] for i in range(n)]
    A = [[Fr(0)] * n for _ in range(n)]
    for i in range(n):
        A[i] = list(e[0]) if False else A[i]
    # columns: A e1 = e3+e2 ; A e2 = 0 ; A e3 = 0 ; A e4 = e4
    cols = [[Fr(0)] * n for _ in range(n)]
    cols[0] = [x + y for x, y in zip(e[2], e[1])]
    cols[3] = list(e[3])
    A = [[cols[j][i] for j in range(n)] for i in range(n)]     # A[i][j] = (A e_j)_i
    C = [list(e[0])]
    J = AI.row_basis(AI.vstack([C, AI.mul(C, A)]))
    print('constructed case: j =', len(J), ' d =', n - len(J), ' J =', [[str(x) for x in r] for r in J])
    W = [list(e[1]), list(e[3])]
    j0 = list(e[0])
    j0A = AI.mul([j0], A)[0]
    base = W + J
    def piW(x):
        co = coords_in(base, x)
        return co[:n - len(J)] if co is not None else None
    TW = [piW(AI.mul([w], A)[0]) for w in W]
    vW = piW(j0A)
    d = n - len(J)
    rows = [list(vW)]
    cur = list(vW)
    for _ in range(d - 1):
        cur = [sum(cur[i] * TW[i][k] for i in range(d)) for k in range(d)]
        rows.append(list(cur))
    cyclic = (AI.rank(rows) == d)
    V = [list(j0)] + [list(w) for w in W]
    c5a = AI.cond_5a_orig(A, C, V)
    c5b = AI.cond_5b_orig(A, C, V)
    print(f'  T_W={[[str(x) for x in r] for r in TW]}  v_W={[str(x) for x in vW]}')
    print(f'  cyclic={cyclic}  (5b)={c5b}  (5a)={c5a}   '
          f"{'OK' if (c5a and c5b == cyclic) else 'MISMATCH'}")
    return c5a and (c5b == cyclic)


if __name__ == '__main__':
    main()
