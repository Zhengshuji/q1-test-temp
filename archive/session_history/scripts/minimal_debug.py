# -*- coding: utf-8 -*-
"""最小测试：定位 times/mm/eta 的 bug"""
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


Am = [[1, 0, 2, 0, -1], [-1, -2, -1, -1, -2], [0, 1, -2, -1, 0],
      [-2, -2, 1, -1, 1], [-2, -2, -1, 0, 0]]
Cm = [[2, 0, 0, 0, 0]]
L0m = [[0, 2, 0, 1, 0]]

A = toF(Am)
C = toF(Cm)
L0 = toF(L0m)

print("A =", [[str(x) for x in row] for row in A])
print("L0 =", [[str(x) for x in row] for row in L0])
print()

# 手工核对 L0 * A
L0A = mm(L0, A)
print("mm(L0, A) =", [[str(x) for x in row] for row in L0A])

# numpy 核对
Anp = np.array(Am, dtype=object)
L0np = np.array(L0m, dtype=object)
print("numpy   =", (L0np @ Anp).tolist())
print()

# 用分数域的手工计算
manual = []
for j in range(5):
    s = sum(F(L0m[0][i]) * F(Am[i][j]) for i in range(5))
    manual.append(str(s))
print("手工    =", manual)
print()

# 检查 eta 计算
def times(v, A, q):
    out = v[:]
    for _ in range(q):
        out = mm([out], A)[0]
    return out

print("times(L0[0], A, 0) =", [str(x) for x in times(L0[0], A, 0)])
print("times(L0[0], A, 1) =", [str(x) for x in times(L0[0], A, 1)])
print("times(L0[0], A, 2) =", [str(x) for x in times(L0[0], A, 2)])
print()

# eta 构造
def orbit(M, A):
    out, cur = [], M
    for _ in range(len(A)):
        out += cur
        cur = mm(cur, A)
    return out

def eta_q0(A, C, L0, verbose=False):
    p, r, n = len(C), len(L0), len(A)
    gens = [row[:] for row in C] + [row[:] for row in L0]
    M, highest = [], [-1] * (p + r)
    for q in range(n + 1):
        for i in range(p + r):
            if highest[i] >= 0 and q > highest[i] + 1:
                continue
            v = times(gens[i], A, q)
            if rank_exact(M + [v]) > rank_exact(M):
                M.append(v)
                highest[i] = q
                if verbose:
                    print(f"   保留 g_{i} A^{q} (秩 {rank_exact(M)})")
        if all(highest[i] >= 0 and q > highest[i] + 1 for i in range(p + r)):
            break
    alpha = [h + 1 if h >= 0 else 0 for h in highest]
    return [alpha[p + j] for j in range(r)], sum(alpha[p + j] for j in range(r)), alpha, M

print("eta 构造（verbose）：")
eta, q0, alpha, M = eta_q0(A, C, L0, verbose=True)
print(f"  alpha={alpha}  eta={eta}  q0={q0}")
print(f"  M 的行数 = {len(M)}, rank(M) = {rank_exact(M)}")
print()
print("M =", [[str(x) for x in row] for row in M])
print()

# 检查构造的 R*
rows = []
for j in range(len(L0)):
    for t in range(1, eta[j]):
        rows.append(times(L0[j], A, t))
print("R* (t=1..eta-1) =", [[str(x) for x in row] for row in rows])
print()

# 真·P1 构造：M 中属于 L0 谱系的保留行（去掉 C 的行）
print("M 中前 p 行是 C 的谱系，后续是 L0 的谱系：")
for idx, row in enumerate(M):
    print(f"  M[{idx}] = {[str(x) for x in row]}")
