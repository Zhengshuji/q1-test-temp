# -*- coding: utf-8 -*-
"""
正确构造 T 并用 P1 式 (20)（三块）判定 Omega*_{A,J}。

目标 T：
    L0 N_C T = [I_r | 0]
    R N_C T  = [0   | Y_J]      （对 P1 闭式解的 R）

构造：T_{:,i} = x_i + z_i   (i=1..r)
      x_i: L0 N_C x = e_i 的任一解
      z_i: 取 z_i = K c，使 RNC·(x_i + z_i) = 0   （K = ker(L0 N_C) 的基）
      后 d_C-r 列：K 的列
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


def build_T(A, C, L0, R):
    """构造满足 L0NC T=[I|0] 且 RNC T=[0|Y] 的 T"""
    n, p, r = len(A), len(C), len(L0)
    NC = ker_cols(C)
    dC = len(NC[0])
    L0NC = mm(L0, NC)          # r × dC
    RNC = mm(R, NC)            # k × dC
    K = ker_cols(L0NC)         # dC × (dC-r)
    mK = len(K[0]) if (K and K[0]) else 0
    Krows = [[K[a][j] for a in range(dC)] for j in range(mK)]   # 每个是长度 dC
    # x_i 特解
    Tcols = []
    for i in range(r):
        ei = [F(1) if q == i else F(0) for q in range(r)]
        Aug = [L0NC[a][:] + [ei[a]] for a in range(r)]
        Rr, piv = rref(Aug)
        xi = [F(0)] * dC
        for a, pc in enumerate(piv):
            if pc < dC:
                xi[pc] = Rr[a][dC]
        # 需要 RNC·(xi + K c) = 0
        tgt = mm(RNC, [[xi[j]] for j in range(dC)])[0][0]
        rncK = [mm(RNC, [[Krows[j][a]] for a in range(dC)])[0][0] for j in range(mK)]
        # 取 k 个独立方程（这里是标量）
        c = [F(0)] * mK
        for j in range(mK):
            if rncK[j] != 0:
                c[j] = -tgt / rncK[j]
                break
        z = [sum(c[j] * Krows[j][a] for j in range(mK)) for a in range(dC)]
        Tcols.append([xi[a] + z[a] for a in range(dC)])
    for j in range(mK):
        Tcols.append([Krows[j][a] for a in range(dC)])
    T = [[Tcols[j][i] for j in range(dC)] for i in range(dC)]
    return T, NC, dC, mK


Am = [[1, 0, 2, 0, -1], [-1, -2, -1, -1, -2], [0, 1, -2, -1, 0],
      [-2, -2, 1, -1, 1], [-2, -2, -1, 0, 0]]
Cm = [[2, 0, 0, 0, 0]]
L0m = [[0, 2, 0, 1, 0]]
A, C, L0 = toF(Am), toF(Cm), toF(L0m)
n, p, r = len(A), len(C), len(L0)
Lx, eta, alpha = P1_construct(A, C, L0)
R = Lx[len(L0):]
print("=" * 80)
print(f"  eta={eta} q0={sum(eta)}  P1 闭式解 condA={condA(A, C, Lx)}")
T, NC, dC, mK = build_T(A, C, L0, R)
print(f"  d_C={dC}, ker(L0NC) 维数={mK}")
print(f"  T 可逆? {inv(T) is not None}")
L0NC = mm(L0, NC)
print(f"  L0NC·T = {[[str(x) for x in row] for row in mm(L0NC, T)]}")
RNCT = mm(mm(R, NC), T)
print(f"  RNC·T  = {[[str(x) for x in row] for row in RNCT]}  (应为 [0|Y])")
print(f"    前 r={r} 列全 0? {all(RNCT[0][i] == 0 for i in range(r))}")
if mK and all(RNCT[0][i] == 0 for i in range(r)):
    Y = RNCT[0][r:]
    print(f"    Y_J = {[str(x) for x in Y]}")
    s = dC - r
    ones = [i for i, x in enumerate(Y) if x == 1]
    print(f"    Y 中等于 1 的位置 = {ones}")
    # 重新算 Omega*
    Tinv = inv(T)
    MC = mm(inv(mm(transpose(NC), NC)), transpose(NC))
    Abar = mm(mm(MC, A), NC)
    BA = mm(mm(C, A), NC)
    AbarT = mm(mm(Tinv, Abar), T)
    BAT = mm(BA, T)
    print()
    print("  用三块公式扫描 Omega*_{A,J}：")
    import itertools
    for J in itertools.combinations(range(s), 1):
        hits = []
        rest = [i for i in range(s) if i not in J]
        for a in range(-20, 21):
            th = F(a, 2)
            YJ = [F(0)] * s
            YJ[J[0]] = F(1)
            for pos in rest:
                YJ[pos] = th
            WJ = [[F(1) if j == i else F(0) for j in range(dC)] for i in range(r)]
            WJ.append([F(0)] * r + YJ)
            if rank_exact(WJ + BAT + mm(WJ, AbarT)) == rank_exact(WJ + BAT):
                hits.append(th)
        # 也检验 Y 本身
        okY = None
        if len(ones) == 1:
            YJ = Y[:]
            WJ = [[F(1) if j == i else F(0) for j in range(dC)] for i in range(r)]
            WJ.append([F(0)] * r + YJ)
            okY = (rank_exact(WJ + BAT + mm(WJ, AbarT)) == rank_exact(WJ + BAT))
        print(f"    J={J}: 命中 {len(hits)}/41  Θ;  P1 解对应的 Y 是否满足? {okY}")
