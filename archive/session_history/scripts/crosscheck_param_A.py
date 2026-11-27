# -*- coding: utf-8 -*-
"""
交叉验证：从 P1 参数化 W_J(Θ) 恢复 R，检验原始 (A)（condA）。

若 condA = True：参数化族中 (A) 恒成立 => (A)-解集正维数
   => 之前"随机采样 0/400"是因为采样的 R 不在参数化族中（缺 RN_CT 前 r 列为 0 的约束）
若 condA = False：参数化实现的约化 (A) 与原始 (A) 不等价（实现有误）
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
    if not X or not Y:
        return []
    n, k, m = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def toF(M):
    return [[F(int(x)) for x in row] for row in M]


def transpose(M):
    return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]


def inv(M):
    n = len(M)
    A = [M[i][:] + [F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    R, piv = rref(A)
    if len(piv) != n:
        return None
    return [row[n:] for row in R]


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


Am = [[1, 0, 2, 0, -1], [-1, -2, -1, -1, -2], [0, 1, -2, -1, 0],
      [-2, -2, 1, -1, 1], [-2, -2, -1, 0, 0]]
Cm = [[2, 0, 0, 0, 0]]
L0m = [[0, 2, 0, 1, 0]]
A, C, L0 = toF(Am), toF(Cm), toF(L0m)
n, p, r = len(A), len(C), len(L0)
k = 1
NC = ker_cols(C)
dC = len(NC[0])
NCt = transpose(NC)
MC = mm(inv(mm(NCt, NC)), NCt)

# T: 使 L0NC T = [I_r | 0]
L0NC = mm(L0, NC)
Tcols = []
for i in range(r):
    e = [F(1) if q == i else F(0) for q in range(r)]
    x = solve_exact([[L0NC[i2][j] for j in range(dC)] for i2 in range(r)],
                    [[e[i2]] for i2 in range(r)])
    Tcols.append(x)
KN = ker_cols(L0NC)
for j in range(len(KN[0])):
    Tcols.append([KN[i][j] for i in range(dC)])
T = [[Tcols[j][i] for j in range(dC)] for i in range(dC)]
Tinv = inv(T)
print(f"  T 可逆? {Tinv is not None},  L0NC·T = "
      f"{[[str(x) for x in row] for row in mm(L0NC, T)]}")

s = dC - r
print(f"  s = {s}, k = {k}")
print()
print("  从参数化生成 R 并检验原始 (A)：")
print(f"  {'J':>6} {'Θ':>14} {'condA':>8}   RN_CT 前 r 列")
for J in [(0,), (1,), (2,)]:
    rest = [i for i in range(s) if i not in J]
    for th in [F(0), F(1), F(-3, 2), F(5)]:
        Y = [F(0)] * s
        Y[J[0]] = F(1)
        for pos in rest:
            Y[pos] = th
        WJ = []
        for i in range(r):
            WJ.append([F(1) if j == i else F(0) for j in range(dC)])
        WJ.append([F(0)] * r + Y)
        XJ = mm(WJ, Tinv)          # (r+k) × dC
        Xlow = XJ[r:]              # k × dC
        R = mm(Xlow, MC)           # k × n  (K=0)
        Lx = toF(L0) + R
        ok = condA(A, C, Lx)
        RNCT = mm(mm(R, NC), T)
        print(f"  {str(J):>6} {str(th):>14} {str(ok):>8}   "
              f"{[str(x) for x in RNCT[0][:r]]}")
print()
print("  判读：")
print("    若 condA 全为 True => 参数化族中 (A) 恒成立 => 解集正维数")
print("       => 之前随机采样 0/400 是因为采样点不满足 RN_CT 前 r 列为 0 的约束")
print("    若 condA 全为 False => 约化 (A) 与原始 (A) 不等价，实现有误")
