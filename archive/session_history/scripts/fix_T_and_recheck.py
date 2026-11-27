# -*- coding: utf-8 -*-
"""
构造正确的 T（使 P1 闭式解满足 RN_CT = [0|Y]），然后重新检验参数化与 (A)。
"""
from fractions import Fraction as F

import numpy as np


def rref(M):
    M = [row[:] for row in M]
    if not M:
        return M, []
    nrow, ncol = len(M), len(M[0])
    piv, r = [], 0
    for c in range(ncol):
        p = None
        for i in range(r, nrow):
            if M[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(nrow):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c)
        r += 1
        if r == nrow:
            break
    return M, piv


def rank_exact(M):
    if not M or not M[0]:
        return 0
    return len(rref(M)[1])


def mm(X, Y):
    n, k, m = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def toF(M):
    return [[F(int(x)) for x in row] for row in M]


def transpose(M):
    return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]


def inv(M):
    n = len(M)
    R, piv = rref([M[i][:] + [F(1) if i == j else F(0) for j in range(n)] for i in range(n)])
    return [row[n:] for row in R] if len(piv) == n else None


def ker_cols(M):
    if not M:
        return []
    n = len(M[0])
    R, piv = rref(M)
    free = [c for c in range(n) if c not in piv]
    if not free:
        return []
    sols = []
    for fc in free:
        v = [F(0)] * n
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][fc]
        sols.append(v)
    m = len(sols)
    return [[sols[j][i] for j in range(m)] for i in range(n)]


def solve_eq(Des, b):
    m, k = len(Des), len(Des[0])
    R, piv = rref([Des[i][:] + [b[i][0]] for i in range(m)])
    for row in R:
        if all(x == 0 for x in row[:k]) and row[k] != 0:
            return None
    y = [F(0)] * k
    for i, pc in enumerate(piv):
        if pc < k:
            y[pc] = R[i][k]
    ns = []
    free = [c for c in range(k) if c not in piv]
    for fc in free:
        v = [F(0)] * k
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            if pc < k:
                v[pc] = -R[i][fc]
        ns.append(v)
    return y, ns


def solve_coeff(target, basis_rows):
    if not basis_rows:
        return [] if all(x == 0 for x in target) else None
    m, k = len(target), len(basis_rows)
    Aug = [[basis_rows[i][j] for i in range(k)] + [target[j]] for j in range(m)]
    R, piv = rref(Aug)
    for row in R:
        if all(x == 0 for x in row[:k]) and row[k] != 0:
            return None
    phi = [F(0)] * k
    for i, pc in enumerate(piv):
        if pc < k:
            phi[pc] = R[i][k]
    return phi


def times(v, A, q):
    out = v[:]
    for _ in range(q):
        out = mm([out], A)[0]
    return out


def P1_construct(A, C, L0):
    n, p, r = len(A), len(C), len(L0)
    gens = [row[:] for row in C] + [row[:] for row in L0]
    ngen = p + r
    M, M_info, rejected = [], [], {}
    for q in range(n + 1):
        for i in range(ngen):
            if i in rejected:
                continue
            v = times(gens[i], A, q)
            if rank_exact(M + [v]) > rank_exact(M):
                M.append(v); M_info.append((i, q))
            else:
                rejected[i] = q
        if len(rejected) == ngen:
            break
    alpha = [rejected.get(i, n + 1) for i in range(ngen)]
    eta = [alpha[p + j] for j in range(r)]
    R_rows = []
    for j in range(r):
        i = p + j
        a_i = alpha[i]
        if a_i > n:
            continue
        Mminus, Minfo = [], []
        for (ii, qq), row in zip(M_info, M):
            if (qq < a_i) or (qq == a_i and ii < i):
                Mminus.append(row); Minfo.append((ii, qq))
        phi = solve_coeff(times(gens[i], A, a_i), Mminus)
        if phi is None:
            continue
        eta_j = eta[j]
        for t in range(1, eta_j):
            shift = eta_j - t
            row = times(gens[i], A, t)
            for q in range(shift + 1, eta_j + 1):
                for idx, (ii, qq) in enumerate(Minfo):
                    if qq != q or phi[idx] == 0:
                        continue
                    term = times(gens[ii], A, q - shift)
                    row = [row[k] - phi[idx] * term[k] for k in range(n)]
            R_rows.append(row)
    return toF(L0) + R_rows, eta, alpha


def condA(A, C, L):
    LA = mm(L, A)
    W = L + C + mm(C, A)
    return rank_exact(W + LA) == rank_exact(W)


Am = [[1, 0, 2, 0, -1], [-1, -2, -1, -1, -2], [0, 1, -2, -1, 0],
      [-2, -2, 1, -1, 1], [-2, -2, -1, 0, 0]]
Cm = [[2, 0, 0, 0, 0]]
L0m = [[0, 2, 0, 1, 0]]
A, C, L0 = toF(Am), toF(Cm), toF(L0m)
n, p, r = len(A), len(C), len(L0)
NC = ker_cols(C)
dC = len(NC[0])
L0NC = mm(L0, NC)
R = P1_construct(A, C, L0)[0][len(L0):]
RNC = mm(R, NC)

# 构造 T：对 i<=r 取 T_{:,i} = x_i + z_i 使 RNC·T_{:,i}=0
Tcols = []
for i in range(r):
    e = [[F(1) if q == i else F(0)] for q in range(r)]
    Des = [[L0NC[a][j] for j in range(dC)] for a in range(r)]
    xi, nsi = solve_eq(Des, e)
    tgt = mm(RNC, [[xi[j]] for j in range(dC)])[0][0]
    # 在 ker(L0NC) 上解 RNC·z = -tgt
    KN = ker_cols(L0NC)                    # dC × m
    m = len(KN[0]) if (KN and KN[0]) else 0
    Krows = [[KN[a][j] for a in range(dC)] for j in range(m)]
    rncK = [[mm(RNC, [[z[a]] for a in range(dC)])[0][0]] for z in Krows]   # m × 1
    sol = solve_eq([[rncK[j][0]] for j in range(m)], [[-tgt] for _ in range(m)])
    if sol is None:
        print(f"  i={i}: 无法消除，取 z=0")
        Tcols.append(xi)
        continue
    yv, _ = sol
    z = [sum(yv[j] * Krows[j][a] for j in range(m)) for a in range(dC)]
    Tcols.append([xi[a] + z[a] for a in range(dC)])
# 后 dC-r 列：ker(L0NC)
KN = ker_cols(L0NC)
for j in range(len(KN[0])):
    Tcols.append([KN[i][j] for i in range(dC)])
T = [[Tcols[j][i] for j in range(dC)] for i in range(dC)]
Tinv = inv(T)
print("=" * 78)
print(f"  构造的 T 可逆? {Tinv is not None}")
print(f"  L0NC·T = {[[str(x) for x in row] for row in mm(L0NC, T)]}")
RNCT = mm(RNC, T)
print(f"  P1 闭式解的 RN_CT = {[[str(x) for x in row] for row in RNCT]}")
print(f"    => 前 r={r} 列是否全 0? {all(RNCT[0][i] == 0 for i in range(r))}")
print()
print(f"  参数化解的 Y_J = {[str(x) for x in RNCT[0][r:]]}")

# 用这个 T 重新算 Omega*
MC = mm(inv(mm(transpose(NC), NC)), transpose(NC))
Abar = mm(mm(MC, A), NC)
BA = mm(mm(C, A), NC)
AbarT = mm(mm(Tinv, Abar), T)
BAT = mm(BA, T)
s = dC - r
print()
print("  用正确的 T 重新扫描 Omega*_{A,J}（P1 式 (20)，三块 LHS）：")
import itertools
for J in itertools.combinations(range(s), 1):
    hits = []
    rest = [i for i in range(s) if i not in J]
    for a in range(-8, 9):
        th = F(a, 2)
        YJ = [F(0)] * s
        YJ[J[0]] = F(1)
        for pos in rest:
            YJ[pos] = th
        WJ = [[F(1) if j == i else F(0) for j in range(dC)] for i in range(r)]
        WJ.append([F(0)] * r + YJ)
        if rank_exact(WJ + BAT + mm(WJ, AbarT)) == rank_exact(WJ + BAT):
            hits.append(th)
    print(f"    J={J}: 命中 {len(hits)}/17 个 Θ 值: {[str(x) for x in hits][:8]}")
