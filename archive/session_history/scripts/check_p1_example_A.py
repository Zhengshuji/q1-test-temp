# -*- coding: utf-8 -*-
"""验证 P1 §VII 算例：L_{0,0} 与 L_{0,1} 是否满足 (A)（q0=4）"""
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


A_rows = [
    [-14, 3, -4, 5, -1, -1, 1, 0], [-3, 5, 3, -2, -6, 0, 8, 0],
    [22, -17, 1, -9, 8, 3, -11, 0], [9, -11, -2, -6, 7, 1, -5, 0],
    [21, -2, 12, -14, -6, 3, 2, 0], [0, 1, 0, 0, -1, 0, 3, 0],
    [10, -9, 1, -3, 5, 1, -10, 0], [0, 0, 0, 0, 0, 0, 0, -1],
]
C_rows = [[2, -3, 0, 0, 2, 0, -4, 0], [-1, -10, -3, 2, 5, 0, -10, 0]]
L_rows = [[-2, 3, 1, 0, -2, 0, 1, 0], [-7, 8, 3, 0, -6, 0, 2, 0]]

A, C = toF(A_rows), toF(C_rows)
CA = mm(C, A)


def L_ab(a, b):
    a, b = F(a), F(b)
    return toF(L_rows) + [
        [-4 * a - 1, 6 * a + 2, 2 * a, 0, -4 * a - 1, -a, 2 * a + 2, 0],
        [2 - 4 * b, 6 * b + 1, 2 * b, -1, -4 * b, -b, 2 * b + 3, 0],
    ]


def condA(A, C, L):
    LA = mm(L, A)
    lh = rank_exact(LA)                     # rank([LA;L;CA;C]) - rank(L) ...
    W = L + C + mm(C, A)
    left = rank_exact(W + LA)
    right = rank_exact(W)
    return left == right, left, right


print("=" * 76)
print("P1 §VII 算例的 (A) 检验  (q0 = 4, n = 8)")
print("=" * 76)
for (a, b), tag in [((0, 0), "L_{0,0}"), ((0, 1), "L_{0,1}"), ((1, 1), "L_{1,1}"), ((2, 3), "L_{2,3}")]:
    Lx = L_ab(a, b)
    ok, left, right = condA(A, C, Lx)
    print(f"  {tag:10s} rank(L)={rank_exact(Lx)}   "
          f"rank[LA;L;CA;C]={left}  rank[L;CA;C]={right}   (A)={ok}")

# 也检查 L（2 行，未增广）
Lx = toF(L_rows)
ok, left, right = condA(A, C, Lx)
print(f"\n  {'L (2行,未增广)':10s} rank(L)={rank_exact(Lx)}   "
      f"rank[LA;L;CA;C]={left}  rank[L;CA;C]={right}   (A)={ok}")

# 检查 q0 = 4 = sum(eta)？
OC = mm(C, A)
Z = Lx + mm(Lx, A) + OC + mm(OC, A)
print(f"\n  dim Z = {rank_exact(Z)}")
print(f"  P1 说 q0 = 4 (eta = (3,1))")
print(f"  增广后 rank(L_{{a,b}}) = {rank_exact(L_ab(0,1))}")
