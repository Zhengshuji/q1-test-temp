"""c=2, q=3 feasibility (general W_L) — exact rational arithmetic. For each 2-plane V in W_L:
  Ann(V) = span(h0, u1), h0 = L0 N; bottom rows h_i = a_i h0 + b_i u1;
  admissibility H_{A,i}|_V = 0 is linear in (a_i,b_i,c_i);
  if some b_i is not forced to zero, build a rank-2 H and test (5a),(5b).
Exact rational arithmetic. This is the generalisation of attempts/165.
"""
import sys, itertools
sys.path.insert(0, '.')
sys.path.insert(0, 'tools/verification')
sys.path.insert(0, 'tools/exact_linalg')
sys.path.insert(0, 'tools/ledger')
from fractions import Fraction as F
import linalg_q as LQ
import z_generator as ZG
from tools.verification.p2_stratification_check import data
from tools.verification.consistency_checks import check_candidate


def planes_in(WL, k, maxn=400):
    d = len(WL[0]) if WL and WL[0] else 0
    B = [[WL[i][j] for i in range(k)] for j in range(d)]
    if d < 2:
        return []
    if d == 2:
        return [[B[0][:], B[1][:]]]
    out, seen = [], set()
    for coeff in itertools.product([-1, 0, 1, 2], repeat=d):
        if all(c == 0 for c in coeff):
            continue
        first = next(c for c in coeff if c != 0)
        if first < 0:
            continue
        Nphi = ZG.ker_cols([[F(c) for c in coeff]])
        if not Nphi or not Nphi[0] or len(Nphi[0]) < 2:
            continue
        Vc = [[sum(Nphi[i][j] * B[i][t] for i in range(d)) for t in range(k)] for j in range(len(Nphi[0]))]
        V = [Vc[0][:], Vc[1][:]]
        R, _ = LQ.rref([r[:] for r in V])
        R = [r[:] for r in R if any(x != 0 for x in r)]
        if len(R) != 2:
            continue
        key = tuple(tuple(x for x in r) for r in R)
        if key in seen:
            continue
        seen.add(key)
        out.append(R)
        if len(out) >= maxn:
            break
    return out


def try_instance(A, C, L0, N, tag='c2'):
    n = len(A); k = len(N[0])
    AN = LQ.mul(A, N)
    L0N = [F(x) for x in LQ.mul(L0, N)[0]]
    L0AN = [F(x) for x in LQ.mul(LQ.mul(L0, A), N)[0]]
    WL = ZG.ker_cols([L0N[:], L0AN[:]])
    dWL = len(WL[0]) if WL and WL[0] else 0
    if dWL < 2:
        return None, f'dim W_L={dWL} < 2'
    RD = LQ.rowspace([r[:] for r in C] + [r[:] for r in LQ.mul(C, A)])
    G = [[sum(F(r[u]) * F(AN[u][t]) for u in range(n)) for t in range(k)] for r in RD]
    m = len(RD)
    stats = {'V': 0, 'forced': 0, 'good': 0, 'fail': 0}
    for V in planes_in(WL, k):
        stats['V'] += 1
        V0v, V1v = V[0], V[1]
        # ann(V): kernel of the 2xk matrix V
        Ann = ZG.ker_cols([V0v[:], V1v[:]])
        us = [[F(Ann[i][j]) for i in range(k)] for j in range(len(Ann[0]))]
        # h0 must be in ann(V)
        if any(sum(L0N[t] * Vc[t] for t in range(k)) != 0 for Vc in (V0v, V1v)):
            continue
        u1 = next((u for u in us if LQ.rank([L0N, u]) == 2), None)
        if u1 is None:
            continue
        p0 = LQ.solve([[N[t][j] for t in range(n)] for j in range(k)], [[L0N[j]] for j in range(k)])[0]
        p1 = LQ.solve([[N[t][j] for t in range(n)] for j in range(k)], [[u1[j]] for j in range(k)])[0]
        A0 = [sum(F(p0[u]) * F(AN[u][t]) for u in range(n)) for t in range(k)]
        A1 = [sum(F(p1[u]) * F(AN[u][t]) for u in range(n)) for t in range(k)]
        forced = []
        sols = []
        for i in range(2):
            Des = []
            for Vc in (V0v, V1v):
                Des.append([sum(F(A0[t]) * F(Vc[t]) for t in range(k)),
                            sum(F(A1[t]) * F(Vc[t]) for t in range(k))] +
                           [sum(F(G[j][t]) * F(Vc[t]) for t in range(k)) for j in range(m)])
            r0 = LQ.rank(Des)
            rb = LQ.rank(Des + [[F(0), F(1)] + [F(0)] * m])
            forced.append(rb == r0)
            if not forced[-1]:
                s = LQ.solve(Des + [[F(0), F(1)] + [F(0)] * m], [[F(0)], [F(0)], [F(1)]])
                sols.append(s)
            else:
                sols.append(None)
        if all(forced):
            stats['forced'] += 1
            continue
        # search over the free parameters (nullspace) of the non-forced rows
        import random
        rng = random.Random(1234 + len(stats))
        for trial in range(300):
            H = [L0N]; HA = [L0AN]
            coefs = []
            for i in range(2):
                if sols[i] is None:
                    co = [F(0)] * (2 + m)
                else:
                    co = [F(x) for x in sols[i][0]]
                    for z in range(len(sols[i][1])):
                        r = rng.randint(-2, 2)
                        if r:
                            co = [co[j] + F(r) * F(sols[i][1][z][j]) for j in range(len(co))]
                coefs.append(co)
                a, b = co[0], co[1]; c = co[2:]
                H.append([a * L0N[t] + b * u1[t] for t in range(k)])
                HA.append([a * A0[t] + b * A1[t] + sum(c[j] * G[j][t] for j in range(m)) for t in range(k)])
            if LQ.rank(H) != 2:
                continue
            if any(sum(HA[i][t] * Vc[t] for t in range(k)) != 0 for i in range(3) for Vc in (V0v, V1v)):
                continue
            Lrows = [L0[0][:]]
            for i in range(2):
                co = coefs[i]; a, b = co[0], co[1]; c = co[2:]
                l = [a * F(p0[u]) + b * F(p1[u]) + sum(c[j] * F(RD[j][u]) for j in range(m)) for u in range(n)]
                Lrows.append(l)
            if LQ.rank([x[:] for x in C] + Lrows) != len(C) + len(Lrows):
                continue
            try:
                res = check_candidate(A, C, L0, Lrows, tag=tag, verbose=False)
            except AssertionError:
                continue
            if res['cond'] and res['five_b']:
                stats['good'] += 1
                return Lrows, stats
        stats['fail'] += 1
    return None, stats


def run_from_data(A, C, L0):
    N = [r[:] for r in ZG.ker_cols([C[0][:], LQ.mul(C, A)[0]])]
    return try_instance(A, C, [r[:] for r in L0], N, 'instance')


if __name__ == '__main__':
    for seed in (10, 16, 21):
        A, C, L0, k, d, NK, U0, V0, Z1, Z2 = data(seed)
        L, info = try_instance(A, C, [r[:] for r in L0], [r[:] for r in NK], f'seed{seed}')
        print(seed, 'FOUND' if L else 'none', info)
    # the dim W_L=3 witness instance (attempts/168)
    n = 6
    cols = {
        1: [F(0), F(1), F(0), F(0), F(0), F(0)],
        2: [F(1), F(0), F(0), F(0), F(0), F(0)],
        3: [F(0), F(1), F(1), F(0), F(0), F(0)],
        4: [F(0), F(0), F(0), F(1), F(0), F(0)],
        5: [F(0), F(0), F(0), F(0), F(1), F(0)],
        6: [F(0), F(1), F(0), F(0), F(0), F(3)],
    }
    A = [[cols[j + 1][i] for j in range(n)] for i in range(n)]
    C = [[F(1), F(0), F(0), F(0), F(0), F(0)]]
    L0 = [[F(0), F(0), F(1), F(0), F(0), F(0)]]
    L, info = run_from_data(A, C, L0)
    print('dimWL3', 'FOUND' if L else 'none', info)
