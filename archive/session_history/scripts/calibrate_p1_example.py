"""
用 P1 §VII 的算例校准我的 (5b) 实现。

P1 断言：n=8, p=r=2, (eta1,eta2)=(3,1), q0=4,
         L_{a,b} 满足 (A) 恒成立；满足 (S) <=> b != 0
         故 nu_min = q0 = 4（例如取 L_{0,1}）

本脚本用**精确有理数算术**独立核对：
  (1) L_{0,1} 是否满足 (A)
  (2) L_{0,1} 是否满足 (5b)  [对所有 lambda]
  (3) L_{0,0} 是否在 lambda=-5 处失败
  (4) 我的候选 s 集合是否正确捕获失败点
"""
from fractions import Fraction as F

import numpy as np

# ---------------- 精确线性代数 ----------------
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
                p = i; break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(nrow):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c); r += 1
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


def Fmat(rows):
    return [[F(x) for x in r] for r in rows]


# ---------------- P1 §VII 的算例 ----------------
n, p, r = 8, 2, 2

A_rows = [
    [-14,  3, -4,  5, -1, -1,   1,  0],
    [ -3,  5,  3, -2, -6,  0,   8,  0],
    [ 22,-17,  1, -9,  8,  3, -11,  0],
    [  9,-11, -2, -6,  7,  1,  -5,  0],
    [ 21, -2, 12,-14, -6,  3,   2,  0],
    [  0,  1,  0,  0, -1,  0,   3,  0],   # 该行 PDF 有错位，按列对齐重建
    [ 10, -9,  1, -3,  5,  1, -10,  0],
    [  0,  0,  0,  0,  0,  0,   0, -1],
]
# 注意：第 6 行原文排版疑似错位（"0 1 0 0 -1 3 0" 只有 7 个数）；
# 这里按 8 列补齐为 [0,1,0,0,-1,0,3,0]，并在下面用 (A) 的自洽性检验它。

C_rows = [
    [ 2, -3,  0,  0,  2,  0,  -4, 0],
    [-1,-10, -3,  2,  5,  0, -10, 0],
]

L_rows = [
    [-2, 3, 1, 0, -2, 0,  1, 0],
    [-7, 8, 3, 0, -6, 0,  2, 0],
]

A = Fmat(A_rows)
C = Fmat(C_rows)
L = Fmat(L_rows)

print("=" * 76)
print("P1 §VII 算例校准")
print("=" * 76)
print(f"  A: {len(A)}x{len(A[0])}   C: {len(C)}x{len(C[0])}   L: {len(L)}x{len(L[0])}")
print(f"  rank(C) = {rank_exact(C)}   (应为 p=2)")
print(f"  rank(L) = {rank_exact(L)}   (应为 r=2)")
print(f"  rank[L;C] = {rank_exact(L + C)}  (应为 r+p=4)")
print()

CA = mm(C, A)
LA = mm(L, A)

# (1) 条件 (A)：row(LA) ⊆ row(L, C, CA)
W = L + C + CA
rk_W = rank_exact(W)
rk_W_LA = rank_exact(W + LA)
print("  (1) 条件 (A):")
print(f"      rank[L;C;CA]      = {rk_W}")
print(f"      rank[LA;L;C;CA]   = {rk_W_LA}")
print(f"      (A) 成立? {rk_W_LA == rk_W}")
print()

# (2) 构造 L_{a,b} (4 行，前 2 行 = L, 后 2 行 = 第 3,4 行 of L_{a,b})
def L_ab(a, b):
    a, b = F(a), F(b)
    row3 = [-4*a - 1, 6*a + 2, 2*a, 0, -4*a - 1, -a, 2*a + 2, 0]
    row4 = [2 - 4*b, 6*b + 1, 2*b, -1, -4*b, -b, 2*b + 3, 0]
    return Fmat(L_rows) + [row3, row4]


def check_5b(Lx, s_list=None):
    """精确检验 (5b)：rank[sL-LA; CA; C] == rank[L; CA; C] 对所有 s"""
    LAx = mm(Lx, A)
    CAx = CA
    rhs = rank_exact(Lx + CAx + C)
    fails = []
    if s_list is None:
        s_list = [F(k) for k in range(-10, 11)]
        s_list += [F(k, 2) for k in range(-10, 11)]
    for s in s_list:
        sl = [[s * Lx[i][j] - LAx[i][j] for j in range(n)] for i in range(len(Lx))]
        lhs = rank_exact(sl + CAx + C)
        if lhs != rhs:
            fails.append(s)
    return rhs, fails


for (a, b) in [(0, 1), (0, 0)]:
    Lx = L_ab(a, b)
    rhs, fails = check_5b(Lx)
    print(f"  (2) L_({a},{b}):  rank[L;CA;C] = {rhs}")
    print(f"      rank(L_({a},{b})) = {rank_exact(Lx)}  (P1 说应为 4)")
    print(f"      在候选 s 上失败的 s: {fails if fails else '无（(S) 成立）'}")
    print()

print("=" * 76)
print("结论")
print("=" * 76)
print("""  P1 断言：L_{0,0} 在 lambda=-5 失败；L_{0,1} 满足 (S)。
  若上面的核对与此一致，则我的 (5b) 实现是正确的；
  若不一致，则说明我的实现有错，需修正。
""")
