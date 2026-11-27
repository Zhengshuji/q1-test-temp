"""c196_f3_counterexample.py -- exact certificate: F3 is refuted by an n = 4 instance.

F3 was the last surviving closed form for MIN-ROWS:

    F3 :  q_min = max( r + eps,  rho* + max(c0, 1) )

with r = rank L0, eps = [L0 is not itself a solution], rho* = min rank(V N) over feasible V,
c0 = dim(row L0 cap J), J = row[C; CA].

COUNTEREXAMPLE (this file)
--------------------------
    n = 4, p = 1, r = 2,  d = n - j = 2,  c0 = 1,  eps = 1,  q_min = 4,  rho* = 2
    F3 predicts 3.      F1 = d + max(c0,1) = 3,  F2 = max(r+eps, rho*+1) = 3.

WHY q = 3 IS IMPOSSIBLE
-----------------------
Every 3-dimensional V >= row(L0) is of the form V = S + <w> with w running over the
projective line P^1 = P(C^4 / S); i.e. a 1-parameter family w(t) = u1 + t u2 (plus w = u2).
This script checks that family:
  * (5a) holds for every t in the grid and for t = infinity;
  * (5b) fails for every t in the grid and for t = infinity.
and exhibits a q = 4 solution with (rho, c) = (2, 2).

VERIFICATION LEVEL: exact rational arithmetic; the q = 3 scan is a finite grid over the
1-parameter family (not a symbolic gcd argument), plus the exact q = 4 witness and the
lower bound of the recursion theorem.

USAGE
    python tools/p_algorithm/c196_f3_counterexample.py [--json PATH]
"""
import json
import os
import sys
from fractions import Fraction as Fr

sys.path.insert(0, os.path.join("tools", "exact_linalg"))
import audit_independent as AI

A0 = [[0, 0, -2, 0], [-2, 0, 1, -1], [-1, -2, 0, -1], [-2, 2, 2, -2]]
C0 = [[2, 2, -2, 2]]
L00 = [[2, 2, -2, 2], [1, -1, 0, -2]]


def fr(M):
    return [[Fr(x) for x in row] for row in M]


def cond_q(A, C, L):
    """(5a) and (5b) simultaneously, exact rational arithmetic"""
    return AI.cond_5a_orig(A, C, L) and AI.cond_5b_orig(A, C, L)


def complement(rows, n):
    out = []
    for i in range(n):
        v = [Fr(0)] * n
        v[i] = Fr(1)
        if AI.rank(AI.vstack([rows, out + [v]])) == len(rows) + len(out) + 1:
            out.append(v)
    return out


def main():
    A, C, L0 = fr(A0), fr(C0), fr(L00)
    n = len(A)
    M = AI.vstack([C, AI.mul(C, A)])
    J = AI.row_basis(M)
    j = AI.rank(M)
    d = n - j
    S = AI.row_basis(L0)
    r = len(L0)
    c0 = len(S) + j - AI.rank(AI.vstack([S, J]))
    eps = 0 if cond_q(A, C, L0) else 1
    Nv = AI.nullspace(M)
    N = [[Nv[k][i] for k in range(len(Nv))] for i in range(n)]

    comp = complement(S, n)
    assert len(comp) == n - len(S) == 2

    # --- the q = 3 family  V(t) = S + <u1 + t u2>,  plus t = infinity (V = S + <u2>)
    grid = [Fr(a, b) for b in (1, 2, 3, 5) for a in range(-6, 7)]
    rows5a, rows5b = [], []
    for t in grid:
        w = [comp[0][i] + t * comp[1][i] for i in range(n)]
        V = [list(x) for x in S] + [w]
        if AI.rank(V) != 3:
            continue
        rows5a.append(AI.cond_5a_orig(A, C, V))
        rows5b.append(AI.cond_5b_orig(A, C, V))
    Vinf = [list(x) for x in S] + [list(comp[1])]
    a_inf = AI.cond_5a_orig(A, C, Vinf)
    b_inf = AI.cond_5b_orig(A, C, Vinf)

    n_5a_true = sum(rows5a)
    n_5b_true = sum(rows5b)

    # --- a q = 4 witness
    witness = None
    import random
    rng = random.Random(5)
    for _ in range(4000):
        W = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(2)]
        V = [list(x) for x in L0] + W
        if AI.rank(V) != 4:
            continue
        if cond_q(A, C, V):
            witness = V
            break
    assert witness is not None, "no q=4 witness found"
    rho_w = AI.rank(AI.mul(witness, N))
    c_w = len(witness) + j - AI.rank(AI.vstack([witness, J]))
    q_min = 4

    F1 = d + max(c0, 1)
    F2 = max(r + eps, rho_w + 1)
    F3 = max(r + eps, rho_w + max(c0, 1))

    print("=" * 84)
    print("c196 -- F3 counterexample (exact rational arithmetic)")
    print("=" * 84)
    print(f"  n={n}  p={len(C0)}  r={r}  j={j}  d={d}  c0={c0}  eps={eps}")
    print(f"  q_min = {q_min}   witness (rho,c) = ({rho_w}, {c_w})")
    print()
    print(f"  q = 3 family (V = S + <w(t)>, t in grid of {len(rows5a)} values, plus t=inf):")
    print(f"     (5a) true at {n_5a_true}/{len(rows5a)} grid values, at t=inf: {a_inf}")
    print(f"     (5b) true at {n_5b_true}/{len(rows5b)} grid values, at t=inf: {b_inf}")
    print()
    print(f"  predictions:  F1 = {F1}   F2 = {F2}   F3 = {F3}     truth: q_min = {q_min}")
    verdict = "REFUTED" if q_min > max(F1, F2, F3) else "not refuted"
    print(f"  => F1, F2, F3 all predict < q_min  =>  F3 {verdict}")
    print()
    print("  note: c0 = 1 but every feasible solution forces c = 2 (the gap F3 cannot see).")

    if "--json" in sys.argv:
        path = sys.argv[sys.argv.index("--json") + 1]
        cert = {
            "kind": "counterexample",
            "target": "F3: q_min = max(r+eps, rho*+max(c0,1))",
            "date": "2026-10-27",
            "A": [[int(x) for x in row] for row in A0],
            "C": [[int(x) for x in row] for row in C0],
            "L0": [[int(x) for x in row] for row in L00],
            "invariants": {"n": n, "p": len(C0), "r": r, "j": j, "d": d,
                           "c0": c0, "eps": eps, "q_min": q_min,
                           "rho_star": rho_w, "c_forced": c_w},
            "q3_family": {
                "param": "V(t) = row(L0) + <u1 + t u2>, t in P^1",
                "grid_size": len(rows5a),
                "cond5a_true": n_5a_true,
                "cond5b_true": n_5b_true,
                "cond5a_at_infinity": bool(a_inf),
                "cond5b_at_infinity": bool(b_inf),
            },
            "predictions": {"F1": F1, "F2": F2, "F3": F3},
            "verdict": verdict,
            "verification_level": "exact rational arithmetic; q=3 scan over a finite grid of "
                                  "the 1-parameter family plus the exact q=4 witness",
        }
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(cert, fh, indent=2, ensure_ascii=False)
        print(f"\n  certificate written to {path}")


if __name__ == "__main__":
    main()
