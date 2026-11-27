"""proof/rho1_layer/verify_dim.py

Checks Theorem 10.1 of `theorem.md`:

    w != 0, (U,H) fixed:   exists tau in A \\ Bad   <=>   dim Bad < dim A

We compute dim A and dim Bad by linear algebra (both sets are affine) and compare with
the *observed* feasibility: we sample many tau in A and count how many pass (5b).

- if dim Bad < dim A: generic tau in A should be feasible  -> expect many passes
- if dim Bad = dim A (Bad = A):  no tau in A can be feasible -> expect zero passes

Run:  python proof/rho1_layer/verify_dim.py
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
from verify import pick_h, U_with_beta, rows_r  # noqa: E402


def affine_solution(M, rhs):
    """solution set of M x = rhs (affine); returns (None) if inconsistent else (dim, point)"""
    m = len(M)
    cols = len(M[0]) if m else 0
    aug = [list(M[i]) + [rhs[i]] for i in range(m)]
    R, piv = AI.rref(aug)
    if any(pc == cols for pc in piv):
        return None
    pt = [Fr(0)] * cols
    for t, pc in enumerate(piv):
        if pc < cols:
            pt[pc] = R[t][cols]
    return cols - len([p for p in piv if p < cols]), pt



def modB_coords(D, x):
    """coordinates of x modulo B (in a complement of B)"""
    B = D['B']
    if not B:
        return list(x)
    d = D['d']
    from c200_q5_probe import complement
    comp = complement(B, d)
    co = Q.coords_in(B + comp, x) if hasattr(Q, 'coords_in') else None
    if co is None:
        # fall back: coordinate extraction via rref
        base = B + comp
        k = len(base)
        Mx = [[base[t][s] for t in range(k)] + [x[s]] for s in range(d)]
        R, piv = AI.rref(Mx)
        co = [Fr(0)] * k
        for t, pc in enumerate(piv):
            if pc < k:
                co[pc] = R[t][k]
    return co[len(B):]


def Ttilde(D, A, u):
    d = D['d']
    su = [sum(u[k] * D['W'][k][t] for k in range(d)) for t in range(D['n'])]
    return D['pi'](AI.mul([su], A)[0])


def U_closed(D, A, w, rng, target=2, tries=80):
    """a target-dim U containing w with Ttilde(U) <= U + B (closure in X coordinates)"""
    B = D['B']
    def rk(rows):
        return AI.rank(AI.vstack([rows] + [[b] for b in B])) if B else AI.rank(rows)
    for _ in range(tries):
        U = [list(w)]
        ok = True
        for _step in range(8):
            base_rk = rk(U)
            grew = False
            for u in list(U):
                t = Ttilde(D, A, u)
                if rk(U + [t]) > base_rk:
                    if len(U) >= target:
                        ok = False
                        break
                    U = U + [t]
                    grew = True
                    break
            if not ok:
                break
            if not grew:
                if len(U) < target:
                    v = [Fr(rng.randint(-2, 2)) for _ in range(D['d'])]
                    if AI.rank(U + [v]) == len(U) + 1:
                        U = U + [v]
                        continue
                break
        if ok and len(U) == target and rk(U) == AI.rank(U):
            return U
    return None


def main():
    rng = random.Random(31337)
    print("=" * 96)
    print("Theorem 10.1 check:  exists tau in A\\Bad  <=>  dim Bad < dim A   (w != 0)")
    print("=" * 96)
    stat = dict(cases=0, lt=0, eq=0, lt_pass=0, lt_total=0, eq_pass=0, eq_total=0)
    for _ in range(200):
        n = rng.choice([4, 5])
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        p = rng.choice([1, 2])
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        if AI.rank(C) != p:
            continue
        D = Q.build(A, C)
        if D is None or D['d'] < 3 or D['j'] < 1:
            continue
        h, w = pick_h(D, A, rng)
        if h is None:
            continue
        d, j = D['d'], D['j']
        U = U_closed(D, A, w, rng)
        if U is None:
            continue
        # ---- A: tau with r_i(tau) in U  (2j unknowns)
        # U^perp basis
        Umat = U
        up = []
        for a in range(d):
            v = [Fr(1) if t == a else Fr(0) for t in range(d)]
            if AI.rank(Umat + up + [v]) == len(Umat) + len(up) + 1:
                up.append(v)
        # r_i(tau) = Ttilde(u_i) + beta(tau_i);  beta(tau_i)_a = sum_k tau_ik * betaJk[a]
        betaJ = [D['pi'](AI.mul([D['J'][k]], A)[0]) for k in range(j)]
        Tt = []
        for i in range(2):
            su = [sum(U[i][k] * D['W'][k][t] for k in range(d)) for t in range(n)]
            Tt.append(D['pi'](AI.mul([su], A)[0]))
        MA, rA = [], []
        for i in range(2):
            for q in up:
                row = [Fr(0)] * (2 * j)
                for k in range(j):
                    row[i * j + k] = sum(q[a] * betaJ[k][a] for a in range(d))
                MA.append(row)
                rA.append(-sum(q[a] * Tt[i][a] for a in range(d)))
        solA = affine_solution(MA, rA) if MA else (2 * j, [Fr(0)] * (2 * j))
        if solA is None:
            continue
        dimA = solA[0]
        # ---- Bad: unknowns (tau (2j), lam, c1, c2); equations r_i - lam*u_i - c_i*w = 0
        nv = 2 * j + 3
        MB, rB = [], []
        for i in range(2):
            for a in range(d):
                row = [Fr(0)] * nv
                for k in range(j):
                    row[i * j + k] = betaJ[k][a]
                row[2 * j] = -U[i][a]              # lam
                row[2 * j + 1 + i] = -w[a]         # c_i
                MB.append(row)
                rB.append(-Tt[i][a])
        solB = affine_solution(MB, rB)
        if solB is None:
            dimBad = 0
        else:
            dim_sol = solB[0]
            # dim of {delta in ker(MB) : tau-part = 0}
            kM = AI.nullspace(MB) if hasattr(AI, 'nullspace') else None
            if kM is None:
                continue
            # basis vectors: kM is a list of full-length vectors (nullspace of MB)
            tau0 = []
            for v in kM:
                if all(v[c] == 0 for c in range(2 * j)):
                    tau0.append(v)
            dimBad = dim_sol - len(tau0)
        stat['cases'] += 1
        if dimBad < dimA:
            stat['lt'] += 1
        else:
            stat['eq'] += 1
        # ---- observed feasibility: sample tau in A
        sol = solA
        _, pt = sol
        # direction basis of A
        kA = AI.nullspace(MA) if MA else [[Fr(1) if t == c else Fr(0) for c in range(2 * j)] for t in range(2 * j)]
        passes = tot = 0
        for _ in range(6):
            t = list(pt)
            for bi, coeff in enumerate([Fr(rng.randint(-2, 2)) for _ in kA]):
                t = [t[c] + coeff * kA[bi][c] for c in range(2 * j)]
            tau = [t[:j], t[j:]]
            V = Q.make_V(D, A, U, [h], tau)
            if AI.rank(V) != len(V) or not AI.cond_5a_orig(A, C, V):
                continue
            tot += 1
            if AI.cond_5b_orig(A, C, V):
                passes += 1
        if dimBad < dimA:
            stat['lt_total'] += tot; stat['lt_pass'] += passes
        else:
            stat['eq_total'] += tot; stat['eq_pass'] += passes
    print(f"  cases                         : {stat['cases']}")
    print(f"  dim Bad < dim A               : {stat['lt']}   (sampled tau {stat['lt_total']}, (5b) holds {stat['lt_pass']})")
    print(f"  dim Bad = dim A (Bad = A)     : {stat['eq']}   (sampled tau {stat['eq_total']}, (5b) holds {stat['eq_pass']})")
    print()
    print("expected: in the '<' rows most sampled tau pass; in the '=' rows NONE pass.")


if __name__ == '__main__':
    main()
