# -*- coding: utf-8 -*-
"""
计算 P1 闭式解对应的 (J, Θ)，从而给出 Omega*_{A,J} 的一个精确点。
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


def solve_exact(Des, b):
    m, k = len(Des), len(Des[0])
    R, piv = rref([Des[i][:] + [b[i][0]] for i in range(m)])
    for row in R:
        if all(x == 0 for x in row[:k]) and row[k] != 0:
            return None
    y = [F(0)] * k
    for i, pc in enumerate(piv):
        if pc < k:
            y[pc] = R[i][k]
    return y


def condA(A, C, L):
    LA = mm(L, A)
    W = L + C + mm(C, A)
    return rank_exact(W + LA) == rank_exact(W)


def solve_coeff(target, basis_rows):
    """解 target = phi * basis_rows（行组合）"""
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


Am = [[1, 0, 2, 0, -1], [-1, -2, -1, -1, -2], [0, 1, -2, -1, 0],
      [-2, -2, 1, -1, 1], [-2, -2, -1, 0, 0]]
Cm = [[2, 0, 0, 0, 0]]
L0m = [[0, 2, 0, 1, 0]]
A, C, L0 = toF(Am), toF(Cm), toF(L0m)
n, p, r = len(A), len(C), len(L0)
NC = ker_cols(C)
dC = len(NC[0])
MC = mm(inv(mm(transpose(NC), NC)), transpose(NC))
L0NC = mm(L0, NC)
Tcols = []
for i in range(r):
    e = [F(1) if q == i else F(0) for q in range(r)]
    Tcols.append(solve_exact([[L0NC[i2][j] for j in range(dC)] for i2 in range(r)],
                             [[e[i2]] for i2 in range(r)]))
KN = ker_cols(L0NC)
for j in range(len(KN[0])):
    Tcols.append([KN[i][j] for i in range(dC)])
T = [[Tcols[j][i] for j in range(dC)] for i in range(dC)]
Tinv = inv(T)

Lx, eta, alpha = P1_construct(A, C, L0)
print("=" * 80)
print(f"  eta={eta} q0={sum(eta)}  P1 闭式解 condA={condA(A, C, Lx)}")
R = Lx[len(L0):]
RNCT = mm(mm(R, NC), T)
print(f"  RN_CT = {[[str(x) for x in row] for row in RNCT]}")
s = dC - r
Y = RNCT[0][r:]
print(f"  Y_J (后 s={s} 个分量) = {[str(x) for x in Y]}")
# 找值为 1 的位置 -> J
ones = [i for i, x in enumerate(Y) if x == 1]
print(f"  值为 1 的位置: {ones}")
if len(ones) == 1:
    J = (ones[0],)
    rest = [i for i in range(s) if i != J[0]]
    Theta = [Y[i] for i in rest]
    print(f"  => J = {J},  Theta = {[str(x) for x in Theta]}")
    print()
    print("  用该 (J,Θ) 走参数化路径，检验约化 (A) 与 condA：")
    Abar = mm(mm(MC, A), NC)
    BA = mm(mm(C, A), NC)
    AbarT = mm(mm(Tinv, Abar), T)
    BAT = mm(BA, T)
    YJ = [F(0)] * s
    YJ[J[0]] = F(1)
    for pos, val in zip(rest, Theta):
        YJ[pos] = val
    WJ = [[F(1) if j == i else F(0) for j in range(dC)] for i in range(r)]
    WJ.append([F(0)] * r + YJ)
    LHS = WJ + BAT + mm(WJ, AbarT)
    RHS = WJ + BAT
    print(f"    rank[W;B;W·Abar_T] = {rank_exact(LHS)}, rank[W;B] = {rank_exact(RHS)}"
          f"  => 约化(A)={rank_exact(LHS) == rank_exact(RHS)}")
    XJ = mm(WJ, Tinv)
    R2 = mm(XJ[r:], MC)
    Lx2 = toF(L0) + R2
    print(f"    从参数化恢复的 L 的 condA = {condA(A, C, Lx2)}")
    print(f"    (P1 闭式解的 condA = {condA(A, C, Lx)})")
