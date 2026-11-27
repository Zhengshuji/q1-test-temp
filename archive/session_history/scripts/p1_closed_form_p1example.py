# -*- coding: utf-8 -*-
"""用 P1 §VII 算例（n=8, q0=4）校准 P1 闭式实现"""
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
    if not X or not Y:
        return []
    n, k, m = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def toF(M):
    return [[F(int(x)) for x in row] for row in M]


def times(v, A, q):
    out = v[:]
    for _ in range(q):
        out = mm([out], A)[0]
    return out


def condA(A, C, L):
    LA = mm(L, A)
    W = L + C + mm(C, A)
    return rank_exact(W + LA) == rank_exact(W)


def solve_coeff(target, basis_rows):
    if not basis_rows:
        return [] if all(x == 0 for x in target) else None
    n, k = len(target), len(basis_rows)
    Aug = [[basis_rows[i][j] for i in range(k)] + [target[j]] for j in range(n)]
    R, piv = rref(Aug)
    for row in R:
        if all(x == 0 for x in row[:k]) and row[k] != 0:
            return None
    phi = [F(0)] * k
    for i, pc in enumerate(piv):
        if pc < k:
            phi[pc] = R[i][k]
    return phi


def P1_construct(A, C, L0, verbose=False):
    n, p, r = len(A), len(C), len(L0)
    gens = [row[:] for row in C] + [row[:] for row in L0]
    ngen = p + r
    M, M_info = [], []
    rejected = {}
    for q in range(n + 1):
        for i in range(ngen):
            if i in rejected:
                continue
            v = times(gens[i], A, q)
            if rank_exact(M + [v]) > rank_exact(M):
                M.append(v)
                M_info.append((i, q))
            else:
                rejected[i] = q
        if len(rejected) == ngen:
            break
    alpha = [rejected.get(i, n + 1) for i in range(ngen)]
    eta = [alpha[p + j] for j in range(r)]
    if verbose:
        print(f"    M 的行 (i,q): {M_info}")
        print(f"    alpha={alpha}  eta={eta}  q0={sum(eta)}")
    R_rows = []
    for j in range(r):
        i = p + j
        a_i = alpha[i]
        if a_i > n:
            continue
        Mminus, Minfo_minus = [], []
        for (ii, qq), row in zip(M_info, M):
            if (qq < a_i) or (qq == a_i and ii < i):
                Mminus.append(row)
                Minfo_minus.append((ii, qq))
        phi = solve_coeff(times(gens[i], A, a_i), Mminus)
        if phi is None:
            continue
        eta_j = eta[j]
        for t in range(1, eta_j):
            shift = eta_j - t
            row = times(gens[i], A, t)
            for q in range(shift + 1, eta_j + 1):
                for idx, (ii, qq) in enumerate(Minfo_minus):
                    if qq != q or phi[idx] == 0:
                        continue
                    term = times(gens[ii], A, q - shift)
                    row = [row[k] - phi[idx] * term[k] for k in range(n)]
            R_rows.append(row)
    return toF(L0) + R_rows, eta, alpha


A_rows = [
    [-14, 3, -4, 5, -1, -1, 1, 0], [-3, 5, 3, -2, -6, 0, 8, 0],
    [22, -17, 1, -9, 8, 3, -11, 0], [9, -11, -2, -6, 7, 1, -5, 0],
    [21, -2, 12, -14, -6, 3, 2, 0], [0, 1, 0, 0, -1, 0, 3, 0],
    [10, -9, 1, -3, 5, 1, -10, 0], [0, 0, 0, 0, 0, 0, 0, -1],
]
C_rows = [[2, -3, 0, 0, 2, 0, -4, 0], [-1, -10, -3, 2, 5, 0, -10, 0]]
L_rows = [[-2, 3, 1, 0, -2, 0, 1, 0], [-7, 8, 3, 0, -6, 0, 2, 0]]

A, C, L0 = toF(A_rows), toF(C_rows), toF(L_rows)
print("=" * 80)
print("P1 §VII 算例 (n=8, p=2, r=2, 已知 q0=4, eta=(3,1)) 的闭式构造")
print("=" * 80)
Lx, eta, alpha = P1_construct(A, C, L0, verbose=True)
print(f"    构造 L*: {len(Lx)} 行 (期望 q0={sum(eta)})")
print(f"    rank(L*) = {rank_exact(Lx)}")
print(f"    (A) 成立? {condA(A, C, Lx)}")
print()
for row in Lx:
    print("      ", [str(x) for x in row])
