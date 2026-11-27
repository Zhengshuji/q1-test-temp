# -*- coding: utf-8 -*-
"""
决定性检验：q0 处随机采样找不到 (A)-解，是"空"还是"测度零非空"？

构造（P1 §III）：R* = row(L0) + span{ L_j A^t : j=1..r, 1 <= t <= eta_j - 1 }
  P1 Theorem 1 保证由有序秩保留构造出的增广满足 (A)。
  故若 R* 满足 (A) 且 dim R* = q0，则 Sigma_{q0}^{(A)} != 空（测度零非空）。
"""
from fractions import Fraction as F

import numpy as np

rng = np.random.default_rng(20260127)


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


def times(v, A, q):
    out = v[:]
    for _ in range(q):
        out = mm([out], A)[0]
    return out


def eta_indices(A, C, L0):
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
        if all(highest[i] >= 0 and q > highest[i] + 1 for i in range(p + r)):
            break
    alpha = [h + 1 if h >= 0 else 0 for h in highest]
    return [alpha[p + j] for j in range(r)], sum(alpha[p + j] for j in range(r)), alpha


def condA(A, C, L):
    LA = mm(L, A)
    W = L + C + mm(C, A)
    return rank_exact(W + LA) == rank_exact(W)


def P1_construct(A, C, L0):
    """P1 §III 的增广：R* = span{ L_j A^t : 1 <= t <= eta_j - 1 }"""
    eta, q0, alpha = eta_indices(A, C, L0)
    rows = []
    for j in range(len(L0)):
        for t in range(1, eta[j]):
            rows.append(times(L0[j], A, t))
    return toF(L0) + rows, eta, q0


cases = [
    ([[1, 0, 2, 0, -1], [-1, -2, -1, -1, -2], [0, 1, -2, -1, 0],
      [-2, -2, 1, -1, 1], [-2, -2, -1, 0, 0]], [[2, 0, 0, 0, 0]], [[0, 2, 0, 1, 0]]),
    ([[1, 1, -2, 2, 1], [-1, 2, 2, -1, 2], [2, 1, 1, -2, -2],
      [1, 0, 2, 2, -2], [0, -1, 0, 0, -2]], [[1, 0, -1, -2, -2]], [[-1, -1, -1, 0, -1]]),
]

print("=" * 84)
print("检验：q0 处 P1 的构造是否给出 (A)-解（=> 测度零非空）")
print("=" * 84)
print()

for Am, Cm, L0m in cases:
    A, C, L0 = toF(Am), toF(Cm), toF(L0m)
    eta, q0, alpha = eta_indices(A, C, L0)
    OC = orbit(C, A)
    Z = orbit(L0, A) + OC
    W = C + mm(C, A)
    Lx, _, _ = P1_construct(A, C, L0)
    print(f"  A={Am}")
    print(f"  C={Cm}  L0={L0m}")
    print(f"    eta={eta}  alpha={alpha}  q0={q0}  dimZ={rank_exact(Z)}  dimW={rank_exact(W)}")
    print(f"    P1 构造的 L*: 行数={len(Lx)}  秩={rank_exact(Lx)}")
    if Lx:
        print(f"    L* = {[[str(x) for x in row] for row in Lx]}")
    a_ok = condA(A, C, Lx) if Lx else False
    print(f"    (A) 成立? {a_ok}    rank(L*) = {rank_exact(Lx)}  (应为 q0={q0})")
    print()
