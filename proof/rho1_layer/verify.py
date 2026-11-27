"""proof/rho1_layer/verify.py

Re-verifies Theorem 9.10 of `theorem.md`:

    rho = 2, c = 1, H = <h>, w := beta(h) != 0, (U,H) fixed, tau admissible.
    Then   V fails (5b) at tau  <=>  exists lam with lam*u_i - r_i(tau) in <w>  (i = 1,2),
    and the set of such (tau,lam) is AFFINE in (tau,lam), so the bad set in tau is affine.

The test is pointwise: for every admissible tau we compare the exact (5b) with the
linear-system consistency test.  We also report how often the affine structure is
non-trivial (dim Bad > 0 or Bad = empty).

Generation is TARGETED: we first pick h in J with beta(h) != 0 (so w != 0), then U >= <beta(h)>,
then solve for an admissible tau.  (The naive generator rarely produces w != 0 AND (5a)-feasible.)

Run:  python proof/rho1_layer/verify.py
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


def pick_h(D, A, rng, tries=40):
    """h in J (J-coords) with beta(h) = pi(h A) != 0"""
    j = D['j']
    for _ in range(tries):
        h = [Fr(rng.randint(-2, 2)) for _ in range(j)]
        if all(x == 0 for x in h):
            continue
        vec = [sum(h[k] * D['J'][k][t] for k in range(j)) for t in range(D['n'])]
        w = D['pi'](AI.mul([vec], A)[0])
        if any(x != 0 for x in w):
            return h, w
    return None, None


def U_with_beta(D, w, rng, tries=40):
    """a 2-dim U containing w (w in X-coords)"""
    rho = 2
    for _ in range(tries):
        U = [list(w)]
        for _ in range(tries):
            v = [Fr(rng.randint(-2, 2)) for _ in range(D['d'])]
            if AI.rank(U + [v]) == len(U) + 1:
                U.append(v)
                break
        if len(U) == rho:
            return U
    return None


def bad_consistent(D, w, U, r):
    """does there exist lam with lam*u_i - r_i in <w> for i = 1,2 ?  (linear system, w != 0)"""
    d = D['d']
    rows, rhs = [], []
    for i in range(2):
        for a in range(d):
            row = [U[i][a]]
            for k in range(2):
                row.append(-w[a] if k == i else Fr(0))
            rows.append(row)
            rhs.append(r[i][a])
    M = [rows[i] + [rhs[i]] for i in range(len(rows))]
    R, piv = AI.rref(M)
    k = 3
    return not any(pc == k for pc in piv)


def rows_r(D, A, U, tau):
    d, n, j = D['d'], D['n'], D['j']
    out = []
    for i in range(2):
        su = [sum(U[i][k] * D['W'][k][t] for k in range(d)) for t in range(n)]
        Ti = D['pi'](AI.mul([su], A)[0])
        tvec = [sum(tau[i][k] * D['J'][k][t] for k in range(j)) for t in range(n)]
        bi = D['pi'](AI.mul([tvec], A)[0])
        out.append([Ti[q] + bi[q] for q in range(d)])
    return out


def main():
    rng = random.Random(2027)
    print("=" * 96)
    print("Theorem 9.10 check:  (5b) fails at tau  <=>  exists lam, lam*u_i - r_i in <w>   (w != 0)")
    print("=" * 96)
    stat = dict(inst=0, w_ok=0, U_ok=0, tau_ok=0, tests=0, ok=0, bad=0, infeas=0, feas=0)
    for _ in range(400):
        n = rng.choice([4, 5])
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        p = rng.choice([1, 2])
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        if AI.rank(C) != p:
            continue
        D = Q.build(A, C)
        if D is None or D['d'] < 2 or D['j'] < 1:
            continue
        stat['inst'] += 1
        h, w = pick_h(D, A, rng)
        if h is None:
            continue
        stat['w_ok'] += 1
        for _rep in range(3):
            U = U_with_beta(D, w, rng)
            if U is None:
                continue
            H = [h]
            tau = Q.solve_tau(D, A, U, H)
            if tau is None:
                continue
            V = Q.make_V(D, A, U, H, tau)
            if AI.rank(V) != len(V) or not AI.cond_5a_orig(A, C, V):
                continue
            stat['tau_ok'] += 1
            # the particular tau, plus random homogeneous perturbations that keep (5a)
            cands = [tau]
            for _ in range(4):
                t2 = [[tau[i][k] + Fr(rng.randint(-1, 1)) for k in range(D['j'])] for i in range(2)]
                V2 = Q.make_V(D, A, U, H, t2)
                if AI.rank(V2) == len(V2) and AI.cond_5a_orig(A, C, V2):
                    cands.append(t2)
            for t in cands:
                V = Q.make_V(D, A, U, H, t)
                if AI.rank(V) != len(V) or not AI.cond_5a_orig(A, C, V):
                    continue
                r = rows_r(D, A, U, t)
                fails = not AI.cond_5b_orig(A, C, V)
                pred = bad_consistent(D, w, U, r)
                stat['tests'] += 1
                if fails:
                    stat['infeas'] += 1
                else:
                    stat['feas'] += 1
                if pred == fails:
                    stat['ok'] += 1
                else:
                    stat['bad'] += 1
                    if stat['bad'] <= 3:
                        print('  MISMATCH: predicted fails =', pred, ' actual fails =', fails,
                              ' d =', D['d'], ' j =', D['j'])
    print(f"  instances            : {stat['inst']}")
    print(f"  with w != 0          : {stat['w_ok']}")
    print(f"  with admissible tau  : {stat['tau_ok']}")
    print(f"  pointwise tests      : {stat['tests']}  (feasible {stat['feas']} / infeasible {stat['infeas']})")
    print(f"  criterion agrees     : {stat['ok']}   mismatches: {stat['bad']}")
    print()
    print("note: this only validates the POINTWISE part of Thm 9.10 (and hence the affine-ness")
    print("      of the bad set, since the test is a linear system in (tau,lam)).")


if __name__ == '__main__':
    main()
