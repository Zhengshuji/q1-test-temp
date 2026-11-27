# -*- coding: utf-8 -*-
"""
判定 (A)-解集的结构：有限点集 还是 正维数？

方法：在 Z 的精确基下，枚举 v（射影归一化），构造 R = span(L0, v)，检验 (A)。
      统计解的数量与分布。
"""
import itertools
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


def orbit(M, A):
    out, cur = [], M
    for _ in range(len(A)):
        out += cur
        cur = mm(cur, A)
    return out


def condA(A, C, L):
    LA = mm(L, A)
    W = L + C + mm(C, A)
    return rank_exact(W + LA) == rank_exact(W)


def rowspace_basis(M):
    """返回 row(M) 的精确基（从 rref 取非零行）"""
    if not M:
        return []
    R, piv = rref(M)
    return [row[:] for row in R if any(x != 0 for x in row)]


Am = [[1, 0, 2, 0, -1], [-1, -2, -1, -1, -2], [0, 1, -2, -1, 0],
      [-2, -2, 1, -1, 1], [-2, -2, -1, 0, 0]]
Cm = [[2, 0, 0, 0, 0]]
L0m = [[0, 2, 0, 1, 0]]
A, C, L0 = toF(Am), toF(Cm), toF(L0m)
n = len(A)

OC = orbit(C, A)
Z = orbit(L0, A) + OC
BZ = rowspace_basis(Z)
BL = rowspace_basis(L0)
print("=" * 84)
print("(A)-解集结构判定（反例1）")
print("=" * 84)
print(f"  dim Z = {len(BZ)},  dim row(L0) = {len(BL)}")

# 把 Z 的基改造为 [L0 的行; 其余]，便于参数化
rest = BZ[:]
for b in BL:
    # 消去 rest 中与 b 相关的分量：用 rref 把 BL 放前面
    pass
Mall = rowspace_basis(L0 + BZ)
# 让 L0 的行排在前面
R0, piv0 = rref(L0 + BZ)
Basis = [row[:] for row in R0 if any(x != 0 for x in row)]
print(f"  合并基的行数 = {len(Basis)}")
print()

# 参数化：v = sum c_i * Basis[i]，模掉 row(L0)
# 简化：枚举 c 在 {-R..R}^(len(Basis))
R = 2
cnt = 0
sols = []
total = 0
for c in itertools.product(range(-R, R + 1), repeat=len(Basis)):
    if all(x == 0 for x in c):
        continue
    # 归一化：第一个非零元为正
    first = next(x for x in c if x != 0)
    if first < 0:
        continue
    total += 1
    v = [sum(F(c[i]) * Basis[i][j] for i in range(len(Basis))) for j in range(n)]
    Lx = L0 + [v]
    if rank_exact(Lx) != 2:
        continue
    if condA(A, C, Lx):
        cnt += 1
        if len(sols) < 12:
            sols.append((c, v))

print(f"  枚举方向数（归一化）: {total}")
print(f"  满足 (A) 的方向数: {cnt}")
print()
if sols:
    print("  样例解（系数 c -> v）:")
    for c, v in sols[:8]:
        print(f"    c={c}")
        print(f"      v={[str(x) for x in v]}")
else:
    print(f"  在 |c| <= {R} 的范围内未找到 (A)-解")
    print("  （P1 闭式给出的解可能落在该范围之外，或需要非整数坐标）")
