"""proof/rho1_layer/verify_conv114.py

Tests Conjecture 11.4 of `theorem.md` on CONSTRUCTED instances (not sampled):

    if there is a mod-B eigenvector v (T v in <v>+B) and A(tau) is non-empty,
    then dim Bad < dim A  (i.e. the layer has no further obstruction).

Construction: n = 4, C = e1, and A is built so that

    J = row[C; CA] = span{e1, e2},   d = 2,   dim B = dim pi(JA) = 1,

so X/B is 1-dimensional and EVERY v not in B is a mod-B eigenvector --
the necessary condition of Thm 11.1' holds automatically.  The remaining
rows of A carry random noise, so the instance is still generic in its other data.

Run:  python proof/rho1_layer/verify_conv114.py
"""
import os
import random
import sys
from fractions import Fraction as Fr

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools", "layer_search"))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools", "exact_linalg"))
import audit_independent as AI  # noqa: E402
import c200_q5_probe as Q  # noqa: E402
from verify_dim import U_closed  # noqa: E402


def build_designed(rng, n=4):
    """C = e1, A e1 = e2, A e2 = e1+e3, last rows random (keeps J = span{e1,e2})"""
    A = [[Fr(0)] * n for _ in range(n)]
    A[0] = [Fr(0), Fr(1), Fr(0), Fr(0)]            # row 0: e1 A = e2
    A[1] = [Fr(1), Fr(0), Fr(1), Fr(0)]            # row 1: e2 A = e1 + e3
    for i in range(2, n):                          # rows 2,3: noise (avoid exact degeneracy)
        A[i] = [Fr(rng.randint(-2, 2)) for _ in range(n)]
        if all(x == 0 for x in A[i]):
            A[i][i % n] = Fr(1)
    C = [[Fr(1)] + [Fr(0)] * (n - 1)]
    return A, C


def bad_dim(D, A, U, w):
    """dim Bad (projection onto tau of the (5a)+eigen equations) -- see Thm 10.1"""
    d, j = D['d'], D['j']
    betaJ = [D['pi'](AI.mul([D['J'][k]], A)[0]) for k in range(j)]
    Tt = []
    for i in range(2):
        su = [sum(U[i][k] * D['W'][k][t] for k in range(d)) for t in range(D['n'])]
        Tt.append(D['pi'](AI.mul([su], A)[0]))
    nv = 2 * j + 3
    MB, rB = [], []
    for i in range(2):
        for a in range(d):
            row = [Fr(0)] * nv
            for k in range(j):
                row[i * j + k] = betaJ[k][a]
            row[2 * j] = -U[i][a]
            row[2 * j + 1 + i] = -w[a]
            MB.append(row)
            rB.append(-Tt[i][a])
    aug = [list(MB[i]) + [rB[i]] for i in range(len(MB))]
    R, piv = AI.rref(aug)
    cols = len(MB[0])
    if any(pc == cols for pc in piv):
        return None
    dim_sol = cols - len([p for p in piv if p < cols])
    kM = AI.nullspace(MB)
    tau0 = [v for v in kM if all(v[c] == 0 for c in range(2 * j))]
    return dim_sol - len(tau0)


def main():
    rng = random.Random(5)
    print("=" * 96)
    print("Conjecture 11.4 on CONSTRUCTED instances (mod-B eigenvector exists by design)")
    print("=" * 96)
    ok = tot = 0
    for _ in range(40):
        A, C = build_designed(rng)
        D = Q.build(A, C)
        if D is None:
            continue
        if not (D['j'] == 2 and D['d'] == 2 and len(D['B']) == 1):
            print(f"  skip: j={D['j']} d={D['d']} |B|={len(D['B'])}")
            continue
        # h: pick a J-combination with beta(h) != 0
        h = w = None
        for _t in range(30):
            hh = [Fr(rng.randint(-2, 2)), Fr(rng.randint(-2, 2))]
            if all(x == 0 for x in hh):
                continue
            vec = [sum(hh[k] * D['J'][k][t] for k in range(2)) for t in range(D['n'])]
            ww = D['pi'](AI.mul([vec], A)[0])
            if any(x != 0 for x in ww):
                h, w = hh, ww
                break
        if h is None:
            continue
        # v: any vector not in B
        v = [Fr(rng.randint(-2, 2)) for _ in range(D['d'])]
        if AI.rank(AI.vstack([D['B'], [v]])) != len(D['B']) + 1:
            continue
        U = [list(w), list(v)]
        if AI.rank(U) != 2:
            continue
        tau = Q.solve_tau(D, A, U, [h])
        if tau is None:
            continue
        V = Q.make_V(D, A, U, [h], tau)
        if AI.rank(V) != len(V) or not AI.cond_5a_orig(A, C, V):
            continue
        # dim A
        up = []
        for a in range(D['d']):
            e = [Fr(1) if t == a else Fr(0) for t in range(D['d'])]
            if AI.rank(U + up + [e]) == len(U) + len(up) + 1:
                up.append(e)
        betaJ = [D['pi'](AI.mul([D['J'][k]], A)[0]) for k in range(D['j'])]
        Tt = []
        for i in range(2):
            su = [sum(U[i][k] * D['W'][k][t] for k in range(D['d'])) for t in range(D['n'])]
            Tt.append(D['pi'](AI.mul([su], A)[0]))
        MA, rA = [], []
        for i in range(2):
            for q in up:
                row = [Fr(0)] * (2 * D['j'])
                for k in range(D['j']):
                    row[i * D['j'] + k] = sum(q[a] * betaJ[k][a] for a in range(D['d']))
                MA.append(row)
                rA.append(-sum(q[a] * Tt[i][a] for a in range(D['d'])))
        augA = [list(MA[i]) + [rA[i]] for i in range(len(MA))] if MA else []
        if MA:
            RA, pivA = AI.rref(augA)
            colsA = len(MA[0])
            if any(pc == colsA for pc in pivA):
                continue
            dimA = colsA - len([p for p in pivA if p < colsA])
        else:
            dimA = 2 * D['j']
        dBad = bad_dim(D, A, U, w)
        if dBad is None:
            continue
        tot += 1
        good = (dBad < dimA)
        ok += good
        print(f"  d={D['d']} j={D['j']} |B|={len(D['B'])}: dim A={dimA}, dim Bad={dBad}, "
              f"dimBad<dimA={good}, (5b)={AI.cond_5b_orig(A, C, V)}")
    print()
    print(f"  constructed instances checked: {tot};  dim Bad < dim A: {ok}")
    print("  (Conjecture 11.4 predicts ALL of them satisfy dim Bad < dim A and hence are feasible)")


if __name__ == "__main__":
    main()
