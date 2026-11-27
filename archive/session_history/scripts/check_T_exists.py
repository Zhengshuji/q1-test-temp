# -*- coding: utf-8 -*-
"""
关键验证：是否存在 T（满足 L0NC·T = [I_r|0]）使 P1 闭式解满足 RN_CT = [0|Y]？

T 的列: T_{:,i} = x_i + z_i,  L0NC x_i = e_i,  z_i ∈ ker(L0NC)
需要: RN_C T_{:,i} = RN_C x_i + RN_C z_i = 0
即:   -RN_C x_i ∈ { RN_C z : z ∈ ker(L0NC) }
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
    """解 Des y = b（Des: m×k, b: m×1）"""
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
RNC = mm(R, NC)                      # 1 × dC
print("=" * 76)
print(f"  P1 闭式解的 R·N_C = {[[str(x) for x in row] for row in RNC]}")
print(f"  L0·N_C = {[[str(x) for x in row] for row in L0NC]}")
print()

# 对每个 i <= r，检验 -RNC·x_i 是否属于 {RNC·z : z ∈ ker(L0NC)}
K = ker_cols(L0NC)                   # dC × (dC - r)
Krows = [[K[i][j] for i in range(dC)] for j in range(len(K[0]))]
print(f"  ker(L0·N_C) 的维数 = {len(Krows)}")
img = [mm(RNC, [[z[i]] for i in range(dC)])[0][0] for z in Krows] if Krows else []
print(f"  RNC(K) 的生成元 = {[str(x) for x in img]}")
print()

for i in range(r):
    e = [[F(1) if q == i else F(0)] for q in range(r)]
    Des = [[L0NC[a][j] for j in range(dC)] for a in range(r)]
    xi = solve_eq(Des, e)
    if xi is None:
        print(f"  i={i}: 无特解")
        continue
    tgt = mm(RNC, [[xi[j]] for j in range(dC)])[0][0]
    # -tgt 是否在 img 的张成中
    cands = [[-tgt] + img] if img else [[-tgt]]
    in_span = (rank_exact([[v] for v in cands[0]]) == rank_exact([[v] for v in img])) if img else (tgt == 0)
    print(f"  i={i}: RNC·x_i = {tgt};  -RNC·x_i ∈ span(RNC(K))? {in_span}")
    if not in_span:
        print(f"       => 不存在 T 使 RNC·T_{{[{i}]}} = 0")
        print(f"       => P1 闭式解**不在**参数化族 {{W_J(Θ)}} 中")
