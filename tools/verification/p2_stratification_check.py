r"""P2 stratification check (k=3, omega=2, q=3).

Enumerate sigma on the admissible subspace, verify
  dim X_S = omega - (rank[P;Q] - rank Q),  P = B^T Z1, Q = B^T Z2,
and sample the fibre to record good/bad per stratum.

This is a verification, not a proof: only finitely many sigma and sampled fibres.
"""
import itertools
import sys

sys.path.insert(0, 'tools/verification')
sys.path.insert(0, 'tools/exact_linalg')
sys.path.insert(0, 'tools/ledger')

from fractions import Fraction as F
import linalg_q as LQ
import z_generator as ZG
import qmin_scan_pr as QR


def rank(M):
    return LQ.rank([r[:] for r in M])


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def smul(c, v):
    return [c * x for x in v]


def vadd(u, v):
    return [a + b for a, b in zip(u, v)]


def trim(x):
    x = list(x)
    while len(x) > 1 and x[-1] == 0:
        x.pop()
    return x


def pgcd(a, b):
    a, b = trim(a), trim(b)
    while not (len(b) == 1 and b[0] == 0):
        r = list(a)
        while len(r) >= len(b) and not (len(r) == 1 and r[0] == 0):
            d = r[-1] / b[-1]
            sh = len(r) - len(b)
            for i in range(len(b)):
                r[sh + i] -= d * b[i]
            r = trim(r)
        a, b = b, r
    if not (len(a) == 1 and a[0] == 0):
        lead = a[-1]
        a = [x / lead for x in a]
    return a


def gcd_deg(H, HA):
    g = None
    for rows in itertools.combinations(range(len(H)), 2):
        for cols in itertools.combinations(range(len(H[0])), 2):
            e = [[[-HA[i][j], H[i][j]] for j in cols] for i in rows]
            p1 = [e[0][0][0] * e[1][1][0],
                  e[0][0][0] * e[1][1][1] + e[0][0][1] * e[1][1][0],
                  e[0][0][1] * e[1][1][1]]
            p2 = [e[0][1][0] * e[1][0][0],
                  e[0][1][0] * e[1][0][1] + e[0][1][1] * e[1][0][0],
                  e[0][1][1] * e[1][0][1]]
            m = [p1[i] - p2[i] for i in range(3)]
            if not (len(m) == 1 and m[0] == 0):
                g = m if g is None else pgcd(g, m)
    if g is None:
        return -1
    while len(g) > 1 and g[-1] == 0:
        g.pop()
    return len(g) - 1 if not (len(g) == 1 and g[0] == 0) else -1


def data(seed):
    n, p, r, q = 7, 2, 1, 3
    made = QR.make_instance(n, p, r, seed)
    if made is None:
        return None
    A, C, L0 = made
    M = [x[:] for x in C] + LQ.mul(C, A)
    k = n - LQ.rank(M)
    Kc = ZG.ker_cols([x[:] for x in M])
    NK = [row[:] for row in Kc]
    ANK = LQ.mul(A, NK)
    U0 = LQ.mul(L0, NK)
    V0 = LQ.mul(LQ.mul(L0, A), NK)
    T = [[NK[i][j] for j in range(k)] + [ANK[i][j] for j in range(k)] for i in range(n)]
    KT = ZG.ker_cols(T)
    d = len(KT[0]) if KT and KT[0] else 0
    zz = [[KT[i][j] for i in range(2 * k)] for j in range(d)]
    Z1 = [[zz[j][i] for j in range(d)] for i in range(k)]
    Z2 = [[zz[j][k + i] for j in range(d)] for i in range(k)]
    return A, C, L0, k, d, NK, U0, V0, Z1, Z2


def analyse(seed):
    dat = data(seed)
    if dat is None:
        print(f'seed {seed}: no instance')
        return
    A, C, L0, k, d, NK, U0, V0, Z1, Z2 = dat
    if k != 3 or d != 1:
        print(f'seed {seed}: skip k={k}, d={d}')
        return
    E = U0[0] if U0 else [F(0)] * k
    Fv = V0[0] if V0 else [F(0)] * k
    rows0 = [r for r in (E, Fv) if any(x != 0 for x in r)]
    if rows0:
        Bs = ZG.ker_cols(rows0)
        m = len(Bs[0]) if Bs and Bs[0] else 0
        basis = [[Bs[i][j] for i in range(3)] for j in range(m)]
    else:
        basis = [[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(1)]]
    sigmas = []
    for coef in itertools.product([-2, -1, 0, 1, 2], repeat=len(basis)):
        if all(c == 0 for c in coef):
            continue
        sig = [sum(coef[j] * basis[j][i] for j in range(len(basis))) for i in range(3)]
        first = next(x for x in sig if x != 0)
        sig = tuple(x / first for x in sig)
        if sig not in sigmas:
            sigmas.append(sig)
    stats = {}
    bad_formula = []
    for sig in sigmas:
        B = ZG.ker_cols([sig])
        if not B or not B[0]:
            continue
        p = [sum(B[t][i] * Z1[t][0] for t in range(3)) for i in range(2)]
        q = [sum(B[t][i] * Z2[t][0] for t in range(3)) for i in range(2)]
        rQ = 1 if q != [F(0), F(0)] else 0
        rPQ = 1 if (p != [F(0), F(0)] or q != [F(0), F(0)]) else 0
        dim_formula = 2 - (rPQ - rQ)
        if rQ == 1:
            dim_direct = 2
        elif p != [F(0), F(0)]:
            dim_direct = 1
        else:
            dim_direct = 2
        if dim_formula != dim_direct:
            bad_formula.append((sig, dim_formula, dim_direct))
        if dim_direct == 2:
            Xbasis = [[B[t][i] for t in range(3)] for i in range(2)]
        else:
            a0 = [-p[1], p[0]]
            Xbasis = [[sum(a0[j] * B[t][j] for j in range(2)) for t in range(3)]]
        spanX = rank(Xbasis + ([E] if any(x != 0 for x in E) else []))
        ok_span = (spanX == 2)
        nq = [-q[1], q[0]] if rQ == 1 else None
        qq = dot(q, q) if nq else F(0)
        found = None
        for a1 in itertools.product([-1, 0, 1], repeat=2):
            for a2 in itertools.product([-1, 0, 1], repeat=2):
                a1 = [F(x) for x in a1]
                a2 = [F(x) for x in a2]
                x1 = [sum(a1[j] * B[t][j] for j in range(2)) for t in range(3)]
                x2 = [sum(a2[j] * B[t][j] for j in range(2)) for t in range(3)]
                H = [E[:], x1, x2]
                if rank(H) != 2:
                    continue
                if nq:
                    b10 = smul(-dot(a1, p) / qq, q)
                    b20 = smul(-dot(a2, p) / qq, q)
                    trials = [(vadd(b10, smul(F(t1), nq)), vadd(b20, smul(F(t2), nq)))
                              for t1 in (-1, 0, 1) for t2 in (-1, 0, 1)]
                else:
                    if dot(a1, p) != 0 or dot(a2, p) != 0:
                        continue
                    trials = [([F(b1), F(b2)], [F(c1), F(c2)])
                              for b1 in (-1, 0, 1) for b2 in (-1, 0, 1)
                              for c1 in (-1, 0, 1) for c2 in (-1, 0, 1)]
                for b1, b2 in trials:
                    y1 = [sum(b1[j] * B[t][j] for j in range(2)) for t in range(3)]
                    y2 = [sum(b2[j] * B[t][j] for j in range(2)) for t in range(3)]
                    HA = [Fv[:], y1, y2]
                    if rank([r[:] for r in H] + [r[:] for r in HA]) != 2:
                        continue
                    dg = gcd_deg(H, HA)
                    if dg == 0:
                        found = 'good'
                        break
                    elif found is None:
                        found = 'bad'
                if found == 'good':
                    break
            if found == 'good':
                break
        key = (rQ, rPQ, dim_direct, ok_span)
        stats.setdefault(key, {'good': 0, 'bad': 0, 'none': 0})
        stats[key][found or 'none'] += 1
    print(f'seed {seed}: strata (rQ, rPQ, dim X_S, E+X_S=S) -> verdicts')
    for key in sorted(stats):
        print('  ', key, stats[key])
    print('  dim formula mismatches:', len(bad_formula), bad_formula[:3])


if __name__ == '__main__':
    for s in [179, 589, 794]:
        analyse(s)
