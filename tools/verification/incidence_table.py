r"""Incidence table for k=3, omega=2, q=3 (d=1 and d=2).

For each instance: enumerate the projective base sigma with E+F0 in S, compute
  rank Q, rank [P;Q], dim X_S, t = dim(E cap X_S), e = dim E,
check the exact admissibility e + dim X_S - t = omega and m >= omega - e,
sample the compatibility fibre, record good/bad, and test a full-row-rank lift.

Verification only: finitely many sigma and sampled fibres.
"""
import itertools
import sys

sys.path.insert(0, '.')
sys.path.insert(0, 'tools/verification')
sys.path.insert(0, 'tools/exact_linalg')
sys.path.insert(0, 'tools/ledger')

from fractions import Fraction as F
import linalg_q as LQ
import z_generator as ZG
from tools.verification.p2_stratification_check import data, gcd_deg, rank


def matT(M):
    return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]


def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
            for i in range(len(A))]


def solve_linear(A, b):
    M = [list(map(F, row)) + [F(b[i])] for i, row in enumerate(A)]
    m, n = len(M), len(M[0]) - 1
    piv, r = [], 0
    for c in range(n):
        p = next((i for i in range(r, m) if M[i][c] != 0), None)
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[r][j] for j in range(n + 1)]
        piv.append(c)
        r += 1
    for i in range(r, m):
        if all(M[i][j] == 0 for j in range(n)) and M[i][n] != 0:
            return None
    x = [F(0)] * n
    for i, c in enumerate(piv):
        x[c] = M[i][n]
    return x


def analyse(seed):
    dat = data(seed)
    if dat is None:
        print(seed, 'no instance')
        return
    A, C, L0, k, d, NK, U0, V0, Z1, Z2 = dat
    if k != 3:
        print(seed, 'skip k', k)
        return
    t = len(NK[0]) if NK and NK[0] else 0
    E = U0[0] if U0 else [F(0)] * t
    Fv = V0[0] if V0 else [F(0)] * t
    e = 1 if any(x != 0 for x in E) else 0
    rows0 = [r for r in (E, Fv) if any(x != 0 for x in r)]
    if rows0:
        Bs = ZG.ker_cols(rows0)
        basis = [[Bs[i][j] for i in range(3)] for j in range(len(Bs[0]) if Bs and Bs[0] else 0)]
    else:
        basis = [[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(1)]]
    sigmas = []
    for coef in itertools.product([-1, 0, 1], repeat=len(basis)):
        if all(c == 0 for c in coef):
            continue
        sig = [sum(coef[j] * basis[j][i] for j in range(len(basis))) for i in range(3)]
        first = next(x for x in sig if x != 0)
        sig = tuple(x / first for x in sig)
        if sig not in sigmas:
            sigmas.append(sig)
    table = {}
    for sig in sigmas:
        B = ZG.ker_cols([sig])
        P = mul(matT(B), Z1)
        Q = mul(matT(B), Z2)
        rQ = rank(Q)
        rPQ = rank([[P[i][j] for j in range(d)] for i in range(2)] + [[Q[i][j] for j in range(d)] for i in range(2)])
        dim = 2 - (rPQ - rQ)
        Qrows = [[Q[i][j] for j in range(d)] for i in range(2)]
        Xb = []
        for a in ([F(1), F(0)], [F(0), F(1)]):
            aP = [sum(a[i] * P[i][j] for i in range(2)) for j in range(d)]
            if rank([aP] + Qrows) == rQ:
                Xb.append([sum(a[i] * B[t2][i] for i in range(2)) for t2 in range(3)])
        tin = 1 if e and rank(Xb + [E]) == rank(Xb) else 0
        adm = (e + dim - tin == 2) and (2 >= 2 - e)
        key = (rQ, rPQ, dim, tin, adm)
        table.setdefault(key, {'n': 0, 'good': 0, 'bad': 0, 'lift': 0})
        table[key]['n'] += 1
        if not adm:
            continue
        # fibre: left nullspace of M=[P;Q] (4 x d)
        M = [[P[i][j] for j in range(d)] for i in range(2)] + [[Q[i][j] for j in range(d)] for i in range(2)]
        KT = ZG.ker_cols(matT(M))
        m = len(KT[0]) if KT and KT[0] else 0
        vecs = [[KT[i][j] for i in range(4)] for j in range(m)]
        found = None
        for c1 in itertools.product([-1, 0, 1], repeat=m):
            for c2 in itertools.product([-1, 0, 1], repeat=m):
                v1 = [sum(c1[j] * vecs[j][i] for j in range(m)) for i in range(4)]
                v2 = [sum(c2[j] * vecs[j][i] for j in range(m)) for i in range(4)]
                if all(x == 0 for x in v1) or all(x == 0 for x in v2):
                    continue
                x1 = [sum(v1[j] * B[t2][j] for j in range(2)) for t2 in range(3)]
                x2 = [sum(v2[j] * B[t2][j] for j in range(2)) for t2 in range(3)]
                H = [E[:], x1, x2]
                if rank(H) != 2:
                    continue
                y1 = [sum(v1[2 + j] * B[t2][j] for j in range(2)) for t2 in range(3)]
                y2 = [sum(v2[2 + j] * B[t2][j] for j in range(2)) for t2 in range(3)]
                HA = [Fv[:], y1, y2]
                if rank(H + HA) != 2:
                    continue
                dg = gcd_deg(H, HA)
                if dg == 0:
                    found = ('good', H, HA)
                    break
                elif found is None:
                    found = ('bad', H, HA)
            if found and found[0] == 'good':
                break
        if found is None:
            continue
        table[key][found[0]] += 1
        if found[0] == 'good':
            H, HA = found[1], found[2]
            # recover R: R NK = H[1:], R ANK = HA[1:]
            rows, rhs = [], []
            for i in range(2):
                for j in range(3):
                    row = [F(0)] * 14
                    for tt in range(7):
                        row[i * 7 + tt] = NK[tt][j]
                    rows.append(row)
                    rhs.append(H[1 + i][j])
            for i in range(2):
                for j in range(3):
                    row = [F(0)] * 14
                    for tt in range(7):
                        row[i * 7 + tt] = LQ.mul(A, NK)[tt][j]
                    rows.append(row)
                    rhs.append(HA[1 + i][j])
            sol = solve_linear(rows, rhs)
            if sol is not None:
                R = [sol[i * 7:(i + 1) * 7] for i in range(2)]
                L = [L0[0][:]] + R
                if rank(L) == 3:
                    table[key]['lift'] += 1
    print(f'seed {seed}: d={d}, e={e}')
    print('  (rQ, rPQ, dimX, t, adm) : n, good, bad, lift')
    for key in sorted(table):
        v = table[key]
        print('  ', key, ':', v['n'], v['good'], v['bad'], v['lift'])


for s in [179, 589, 794, 138, 261, 1163, 753, 1081, 1327, 302, 1491]:
    analyse(s)
