# -*- coding: utf-8 -*-
"""
判定 (A)-解集的局部维数：从 P1 的精确解出发做扰动。
若邻域内其他点也满足 (A) => 正维数；否则 => 孤立点。
"""
from fractions import Fraction as F

import numpy as np

rng = np.random.default_rng(20260128)


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


def condA(A, C, L):
    LA = mm(L, A)
    W = L + C + mm(C, A)
    return rank_exact(W + LA) == rank_exact(W)


Am = [[1, 0, 2, 0, -1], [-1, -2, -1, -1, -2], [0, 1, -2, -1, 0],
      [-2, -2, 1, -1, 1], [-2, -2, -1, 0, 0]]
Cm = [[2, 0, 0, 0, 0]]
L0m = [[0, 2, 0, 1, 0]]
A, C, L0 = toF(Am), toF(Cm), toF(L0m)
n = len(A)

v0 = [F(-35, 8), F(-6), F(-7, 4), F(-3), F(-21, 8)]
print("=" * 82)
print("(A)-解集的局部结构：从 P1 精确解出发扰动")
print("=" * 82)
print(f"  v0 = {[str(x) for x in v0]}")
print(f"  检验 (A): {condA(A, C, L0 + [v0])}")
print()

# 1) 沿随机方向的线性扰动
print("  [1] 沿随机方向的线性扰动  v = v0 + t*u :")
for scale in ["1", "1/10", "1/100", "1/1000"]:
    sc = F(scale)
    hits = 0
    trials = 60
    for _ in range(trials):
        u = [F(int(rng.integers(-3, 4))) for _ in range(n)]
        if all(x == 0 for x in u):
            continue
        v = [v0[k] + sc * u[k] for k in range(n)]
        if condA(A, C, L0 + [v]):
            hits += 1
    print(f"      t={scale:>6s}: (A) 命中 {hits}/{trials}")

print()
# 2) 只在一个坐标上扰动
print("  [2] 单坐标扰动 v0 + t*e_k :")
for k in range(n):
    hits = []
    for t in [F(1, 100), F(1, 1000), F(1, 10000)]:
        v = v0[:]
        v[k] = v0[k] + t
        hits.append("Y" if condA(A, C, L0 + [v]) else ".")
    print(f"      e_{k}: {''.join(hits)}  (t=1e-2,1e-3,1e-4)")

print()
# 3) 精确的有理扰动：v0 + (p/q) * basis  （小分母）
print("  [3] 用分母 <= 4 的有理扰动（坐标级）:")
hits = 0
trials = 0
for _ in range(400):
    v = []
    for k in range(n):
        num = int(rng.integers(-4, 5))
        den = int(rng.integers(1, 5))
        v.append(v0[k] + F(num, den))
    trials += 1
    if condA(A, C, L0 + [v]):
        hits += 1
print(f"      (A) 命中 {hits}/{trials}")

print()
print("  判读：")
print("    若上述扰动命中率均为 0 => (A)-解集在 v0 附近是**孤立点**")
print("    若有大量命中        => 解集**正维数**（随机采样本应命中，与 0/400 矛盾）")
