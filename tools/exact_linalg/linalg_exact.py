# -*- coding: utf-8 -*-
"""
linalg_exact.py —— **独立**的精确线性代数例程（用于交叉验证库的 solve/rk）

动机（CLAUDE.md §10）：库的 `solve(Des,b)` 出现"秩条件保证可解、却报不相容"的现象 ✗。
本模块用**标准 RREF**（Gauss-Jordan）重新实现，算法显然正确 ✓，作为**裁判**。

约定：
  Des : m 行 k 列的系数矩阵（行列表）
  b   : m 行 1 列的右端
  返回 (y, ns) 或 None；y 为特解（长度 k），ns 为零空间基（每个长度 k）
"""
from fractions import Fraction

F = Fraction


def rref_aug(Des, b, k):
    """把 [Des | b] 化成 RREF。返回 (M, piv_cols)，M 是 m x (k+1)。"""
    m = len(Des)
    M = [[F(Des[i][j]) for j in range(k)] + [F(b[i][0])] for i in range(m)]
    piv = []
    r = 0
    for c in range(k):
        # 选主元（第一个非零）
        sel = None
        for i in range(r, m):
            if M[i][c] != 0:
                sel = i
                break
        if sel is None:
            continue
        M[r], M[sel] = M[sel], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[r][j] for j in range(k + 1)]
        piv.append(c)
        r += 1
        if r == m:
            break
    return M, piv


def solve_exact(Des, b):
    """解 Des·x = b。返回 (y, ns) 或 None（不相容）。"""
    if not Des:
        return None
    k = len(Des[0])
    M, piv = rref_aug(Des, b, k)
    m = len(Des)
    for i in range(m):
        if all(M[i][j] == 0 for j in range(k)) and M[i][k] != 0:
            return None
    y = [F(0)] * k
    for i, c in enumerate(piv):
        y[c] = M[i][k]
    free = [c for c in range(k) if c not in piv]
    ns = []
    for fc in free:
        v = [F(0)] * k
        v[fc] = F(1)
        for i, c in enumerate(piv):
            v[c] = -M[i][fc]
        ns.append(v)
    return y, ns


def rank_exact(M):
    """矩阵的秩（用 RREF，不依赖库）。"""
    if not M or not M[0]:
        return 0
    m, k = len(M), len(M[0])
    A = [row[:] for row in M]
    r = 0
    for c in range(k):
        sel = None
        for i in range(r, m):
            if A[i][c] != 0:
                sel = i
                break
        if sel is None:
            continue
        A[r], A[sel] = A[sel], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(k)]
        r += 1
        if r == m:
            break
    return r


def matmul(X, Y):
    """标准矩阵乘法（带维数断言，杜绝库 mm 的静默错配）。"""
    assert X and Y, "空矩阵"
    assert len(X[0]) == len(Y), "维数不匹配: %d vs %d" % (len(X[0]), len(Y))
    n, k, p = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(p)] for i in range(n)]
