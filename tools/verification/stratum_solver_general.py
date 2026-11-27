"""General-r stratum solver (r = number of fixed rows L0).

The rank condition is: the bottom (q-r) rows span Ann(V)/row(L0 N), i.e. their
coefficient matrix on the quotient directions has rank omega - rho0, where
rho0 = rank(L0 N).  This is the r>1 correction of attempts/186 (expert 61).

Run: python tools/verification/stratum_solver_general.py
"""
import sys
import random
import itertools
sys.path.insert(0, '.')
sys.path.insert(0, 'tools/verification')
sys.path.insert(0, 'tools/exact_linalg')
sys.path.insert(0, 'tools/ledger')
from fractions import Fraction as F
import linalg_q as LQ
import z_generator as ZG
from tools.verification.consistency_checks import check_candidate
from tools.verification.stratum_solver import prepare, planes, gcd_minors



def lift_data(A, C, L0, H, HA):
    """Lift layer (expert 61, four-layer architecture).

    Returns realizability of each pair (h_i, hA_i) = (gN, gAN), the dimension
    d'_C = dim E'_C, and dim ker Z_pair; the pair-preserving criterion is
    d'_C >= dim ker Z_pair (with all pairs realizable).
    """
    N, k, AN, L0N1, L0AN1, RD, G, n = prepare(A, C, L0)
    q = len(H)
    # realizability: solve g [N; AN] = (h, hA) for g in C^n
    Des = [[N[t][j] for t in range(n)] for j in range(k)] + [[AN[t][j] for t in range(n)] for j in range(k)]
    realizable = True
    for i in range(q):
        b = [H[i][j] for j in range(k)] + [HA[i][j] for j in range(k)]
        if LQ.solve(Des, [[x] for x in b]) is None:
            realizable = False
    # d'_C = dim(ker g -> gAN on row[C;CA]) - rank C
    m = len(RD)
    Gam = [[sum(F(r[u]) * F(AN[u][t]) for u in range(n)) for t in range(k)] for r in RD]
    dC = m - LQ.rank(Gam) - LQ.rank([r[:] for r in C])
    # ker Z_pair: alpha in C^q with sum alpha_i (h_i,hA_i) = 0
    pairs = [[H[i][j] for j in range(k)] + [HA[i][j] for j in range(k)] for i in range(q)]
    kz = q - LQ.rank(pairs)
    return {'realizable': realizable, 'dC': dC, 'kerZ': kz, 'ok': realizable and kz <= dC}


def solve_general(A, C, L0, q, omega=None, seed=0, mode='random'):
    N, k, AN, L0N1, L0AN1, RD, G, n = prepare(A, C, L0)
    r = len(L0)
    L0N = [[sum(F(L0[i][u]) * F(N[u][t]) for u in range(n)) for t in range(k)] for i in range(r)]
    L0AN = [[sum(F(L0[i][u]) * F(AN[u][t]) for u in range(n)) for t in range(k)] for i in range(r)]
    rho0 = LQ.rank([row[:] for row in L0N])
    m = len(RD)
    if omega == 0:
        # V = K0, H = 0: every row of L must lie in row[C;CA] = K0^perp.
        RD0 = LQ.rowspace([r[:] for r in C] + [r[:] for r in LQ.mul(C, A)])
        L0N = [[sum(F(L0[i][u]) * F(N[u][t]) for u in range(n)) for t in range(k)] for i in range(r)]
        if any(x != 0 for row in L0N for x in row):
            return None, {'status': 'omega=0 but L0N != 0', 'omega': 0}
        # start with L0 rows, add rows from RD0 keeping independence mod C
        Lrows = [L0[i][:] for i in range(r)]
        for g in RD0:
            if LQ.rank([x[:] for x in C] + Lrows) == LQ.rank([x[:] for x in C]) + len(Lrows):
                if len(Lrows) == q:
                    break
                Lrows.append(g[:])
        if len(Lrows) != q:
            return None, {'status': 'omega=0: not enough independent rows in row[C;CA]', 'omega': 0}
        if LQ.rank([x[:] for x in C] + Lrows) != LQ.rank([x[:] for x in C]) + q:
            return None, {'status': 'omega=0: rank[C;L] != rank C + q', 'omega': 0}
        try:
            res = check_candidate(A, C, L0, Lrows, tag='omega0', verbose=False)
        except AssertionError:
            return None, {'status': 'omega=0: check failed', 'omega': 0}
        if res['cond'] and res['five_b']:
            return Lrows, {'status': 'feasible', 'omega': 0, 'c': k}
        return None, {'status': 'omega=0: checks failed', 'omega': 0}

    rng = random.Random(seed)
    if omega is None:
        omega = q - r
    c = k - omega
    if c < 0 or omega <= 0 or omega > q:
        return None, {'status': 'bad parameters'}
    WL = ZG.ker_cols([L0N[i][:] for i in range(r)] + [L0AN[i][:] for i in range(r)])
    dWL = len(WL[0]) if WL and WL[0] else 0
    if dWL < c:
        return None, {'status': f'dim W_L={dWL} < c={c}'}
    S0 = LQ.rowspace([row[:] for row in L0N])
    for V in planes(WL, k, c, rng, mode=mode):
        Ann = ZG.ker_cols([V[i][:] for i in range(c)])
        acols = [[F(Ann[i][j]) for i in range(k)] for j in range(len(Ann[0]) if Ann and Ann[0] else 0)]
        if len(acols) < omega:
            continue
        if any(sum(F(L0N[i][t]) * F(V[j][t]) for t in range(k)) != 0 for i in range(r) for j in range(c)):
            continue
        basis = [row[:] for row in S0]
        for u in acols:
            if len(basis) == omega:
                break
            if LQ.rank(basis + [u]) > len(basis):
                basis.append(u)
        if len(basis) != omega:
            continue
        us = basis[rho0:]
        lifts = []
        for h in basis:
            lifts.append(LQ.solve([[N[t][j] for t in range(n)] for j in range(k)], [[h[j]] for j in range(k)])[0])
        Abase = [[sum(F(l[u]) * F(AN[u][t]) for u in range(n)) for t in range(k)] for l in lifts]
        sols = []
        forced = []
        ok = True
        for i in range(q - r):
            rows = []
            for rv in range(c):
                row = [sum(F(Abase[j][t]) * F(V[rv][t]) for t in range(k)) for j in range(rho0)]
                row += [sum(F(Abase[rho0 + j][t]) * F(V[rv][t]) for t in range(k)) for j in range(omega - rho0)]
                row += [sum(F(G[j][t]) * F(V[rv][t]) for t in range(k)) for j in range(m)]
                rows.append(row)
            if omega == rho0:
                is_forced = False
            else:
                is_forced = True
                for z in range(omega - rho0):
                    eb = [F(0)] * (rho0 + (omega - rho0) + m)
                    eb[rho0 + z] = F(1)
                    if LQ.rank(rows + [eb]) > LQ.rank(rows):
                        is_forced = False
            forced.append(is_forced)
            if is_forced:
                sols.append(None)
            else:
                s = LQ.solve(rows, [[F(0)] for _ in range(c)])
                if s is None:
                    ok = False
                    break
                sols.append(s)
        if not ok or all(forced):
            continue
        free_dims = [len(sols[i][1]) if sols[i] is not None else 0 for i in range(q - r)]
        total_free = sum(free_dims)
        if mode == 'grid' and total_free <= 6:
            trials = list(itertools.product([-1, 0, 1], repeat=total_free))[:400]
        elif mode == 'grid':
            trials = [tuple(0 for _ in range(total_free))]
            for i in range(total_free):
                for sgn in (1, -1):
                    tv = [0] * total_free; tv[i] = sgn; trials.append(tuple(tv))
        else:
            trials = [None] * 200
        for trial in trials:
            coefs = []
            idx = 0
            for i in range(q - r):
                if sols[i] is None:
                    co = [F(0)] * (omega + m)
                else:
                    co = [F(x) for x in sols[i][0]]
                    for z in range(len(sols[i][1])):
                        if mode == 'grid':
                            rv = trial[idx]; idx += 1
                        else:
                            rv = rng.randint(-2, 2)
                        if rv:
                            co = [co[j] + F(rv) * F(sols[i][1][z][j]) for j in range(len(co))]
                coefs.append(co)
            if omega - rho0 > 0:
                Bmat = [[coefs[i][rho0 + j] for j in range(omega - rho0)] for i in range(q - r)]
                if LQ.rank(Bmat) != omega - rho0:
                    continue
            H = [row[:] for row in L0N]
            HA = [row[:] for row in L0AN]
            for co in coefs:
                cs = co[:rho0]; bs = co[rho0:omega]; g = co[omega:]
                H.append([sum(cs[j] * basis[j][t] for j in range(rho0)) +
                          sum(bs[j] * us[j][t] for j in range(omega - rho0)) for t in range(k)])
                HA.append([sum(cs[j] * Abase[j][t] for j in range(rho0)) +
                           sum(bs[j] * Abase[rho0 + j][t] for j in range(omega - rho0)) +
                           sum(g[j] * G[j][t] for j in range(m)) for t in range(k)])
            if LQ.rank(H) != omega:
                continue
            if any(sum(HA[i][t] * V[j][t] for t in range(k)) != 0 for i in range(q) for j in range(c)):
                continue
            ld = lift_data(A, C, L0, H, HA)
            if not ld['ok']:
                continue
            P = [[(-HA[i][t], H[i][t]) for t in range(k)] for i in range(q)]
            g = gcd_minors(P, q, k, omega)
            if not (len(g) == 1 and g[0] != 0):
                continue
            Lrows = [L0[i][:] for i in range(r)]
            for co in coefs:
                cs = co[:rho0]; bs = co[rho0:omega]; g = co[omega:]
                Lrows.append([sum(cs[j] * F(lifts[j][u]) for j in range(rho0)) +
                              sum(bs[j] * F(lifts[rho0 + j][u]) for j in range(omega - rho0)) +
                              sum(g[j] * F(RD[j][u]) for j in range(m)) for u in range(n)])
            if LQ.rank([x[:] for x in C] + Lrows) != len(C) + len(Lrows):
                continue
            try:
                res = check_candidate(A, C, L0, Lrows, tag='general', verbose=False)
            except AssertionError:
                continue
            if res['cond'] and res['five_b']:
                return Lrows, {'status': 'feasible', 'r': r, 'rho0': rho0}
    return None, {'status': 'none in search', 'r': r, 'rho0': rho0}


if __name__ == '__main__':
    from tools.verification.p2_stratification_check import data
    for seed in (10, 16, 21):
        A, C, L0, k, d, NK, U0, V0, Z1, Z2 = data(seed)
        L, info = solve_general(A, C, [r[:] for r in L0], q=3, omega=2, seed=seed)
        print(seed, 'FOUND' if L else 'none', info)
