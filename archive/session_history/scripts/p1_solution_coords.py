# -*- coding: utf-8 -*-
"""计算 P1 闭式解在 Z 的基下的坐标，判断解集是否只是"分母大"。"""
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


def rowspace_basis(M):
    if not M:
        return []
    R, piv = rref(M)
    return [row[:] for row in R if any(x != 0 for x in row)]


def P1_construct(A, C, L0):
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
n = len(A)
OC = orbit = None


def orbit_(M, A):
    out, cur = [], M
    for _ in range(len(A)):
        out += cur
        cur = mm(cur, A)
    return out


Z = orbit_(L0, A) + orbit_(C, A)
BZ = rowspace_basis(Z)

Lx, eta, alpha = P1_construct(A, C, L0)
print("=" * 80)
print(f"  eta={eta}  alpha={alpha}  q0={sum(eta)}")
print(f"  P1 闭式解 L* ({len(Lx)} 行), (A)={condA(A, C, Lx)}")
for row in Lx:
    print(f"    {[str(x) for x in row]}")
print()
extra = Lx[len(L0):]
print("  额外行在 Z 的基下的坐标：")
for k, e in enumerate(extra):
    co = solve_coeff(e, BZ)
    print(f"    行{k}: {[str(x) for x in co] if co else '不在 Z 中！'}")
print()
print(f"  Z 的基 ({len(BZ)} 行):")
for b in BZ:
    print(f"    {[str(x) for x in b]}")
