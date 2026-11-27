"""proof/rho1_layer/strat_d3.py

The d = 3 stratification experiment.

For each random instance with d = 3 we sample many classes [v] in P(X/B) (v not in B),
build U = <w, v>, solve for admissible tau, and record

    (dim(B cap U), dim A, dim Bad, feasible?)

The point: (dim A, dim Bad) take only FINITELY many values as [v] varies -- these values
are the strata of Theorem 10.1/§10.3 -- and feasibility is exactly "dim Bad < dim A"
on each stratum.  We report the strata and whether any of them is feasible.

Run:  python proof/rho1_layer/strat_d3.py
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
from verify_dim import Ttilde  # noqa: E402


def dim_A_and_bad(D, A, U, w):
    """(dim A, dim Bad) for this (U, w) -- both by linear algebra"""
    j, d = D['j'], D['d']
    betaJ = [D['pi'](AI.mul([D['J'][k]], A)[0]) for k in range(j)]
    Tt = []
    for i in range(2):
        su = [sum(U[i][k] * D['W'][k][t] for k in range(d)) for t in range(D['n'])]
        Tt.append(D['pi'](AI.mul([su], A)[0]))
    # U^perp
    # annihilator of U (NOT a complement of U!)
    up = AI.nullspace(U)
    # A: r_i(tau) in U
    MA, rA = [], []
    for i in range(2):
        for q in up:
            row = [Fr(0)] * (2 * j)
            for k in range(j):
                row[i * j + k] = sum(q[a] * betaJ[k][a] for a in range(d))
            MA.append(row)
            rA.append(-sum(q[a] * Tt[i][a] for a in range(d)))
    if MA:
        aug = [list(MA[i]) + [rA[i]] for i in range(len(MA))]
        R, piv = AI.rref(aug)
        cols = len(MA[0])
        if any(pc == cols for pc in piv):
            return None, None
        dimA = cols - len([p for p in piv if p < cols])
    else:
        dimA = 2 * j
    # Bad
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
        return dimA, 0
    dim_sol = cols - len([p for p in piv if p < cols])
    kM = AI.nullspace(MB)
    tau0 = [v for v in kM if all(v[c] == 0 for c in range(2 * j))]
    return dimA, dim_sol - len(tau0)


def main():
    rng = random.Random(777)
    print("=" * 100)
    print("d = 3 stratification:  (dim(B cap U), dim A, dim Bad) as [v] varies")
    print("=" * 100)
    strata_all = {}
    any_feasible = 0
    inst = 0
    for _ in range(120):
        n = 5
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        p = rng.choice([1, 2])
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        if AI.rank(C) != p:
            continue
        D = Q.build(A, C)
        if D is None or D['d'] != 3 or D['j'] < 1:
            continue
        # h with w != 0
        h = w = None
        for _t in range(30):
            hh = [Fr(rng.randint(-2, 2)) for _ in range(D['j'])]
            if all(x == 0 for x in hh):
                continue
            vec = [sum(hh[k] * D['J'][k][t] for k in range(D['j'])) for t in range(n)]
            ww = D['pi'](AI.mul([vec], A)[0])
            if any(x != 0 for x in ww):
                h, w = hh, ww
                break
        if h is None:
            continue
        inst += 1
        local = {}
        for _v in range(25):                       # sample the projective parameter [v]
            v = [Fr(rng.randint(-3, 3)) for _ in range(D['d'])]
            if AI.rank(AI.vstack([D['B'], [v]])) != len(D['B']) + 1:
                continue
            U = [list(w), list(v)]
            if AI.rank(U) != 2:
                continue
            kB = (len(D['B']) + len(U) - AI.rank(D['B'] + U)) if D['B'] else 0
            dimA, dimBad = dim_A_and_bad(D, A, U, w)
            if dimA is None:
                continue
            tau = Q.solve_tau(D, A, U, [h])
            feas = False
            if tau is not None:
                V = Q.make_V(D, A, U, [h], tau)
                if AI.rank(V) == len(V) and AI.cond_5a_orig(A, C, V) and AI.cond_5b_orig(A, C, V):
                    feas = True
            key = (kB, dimA, dimBad)
            local[key] = local.get(key, 0) + (1 if feas else 0)
            strata_all[key] = strata_all.get(key, 0) + 1
            if feas:
                any_feasible += 1
        if local:
            sig = ', '.join(f'{k}->{v}feas' for k, v in sorted(local.items()))
            print(f'  inst {inst}: d=3 j={D["j"]} |B|={len(D["B"])}  strata: {sig}')
    print()
    print(f'  instances with d=3 : {inst}')
    print(f'  distinct strata (kB, dimA, dimBad): {len(strata_all)}')
    for k, cnt in sorted(strata_all.items()):
        print(f'    {k}: {cnt} samples')
    print(f'  feasible samples    : {any_feasible}')
    print()
    print('reading: the strata are the finitely many values of (kB, dimA, dimBad);')
    print('         feasibility happens exactly on the strata with dimBad < dimA.')


if __name__ == '__main__':
    main()
