# -*- coding: utf-8 -*-
"""
正确的 (A)-构造：商空间 Ā-不变包。

  (A) ⟺ π(R) 是 Ā-不变的，  π: Z → Z/W,  W = row(C,CA)
  构造：R̄_0 := 包含 π(row(L0)) 的最小 Ā-不变子空间（Krylov 迭代）
        R := row(L0) + span{ π^{-1}(R̄_0) 的基 }

检验是否满足 (A)，以及其维数与 eta/q0 的关系。
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


def orbit(M, A):
    out, cur = [], M
    for _ in range(len(A)):
        out += cur
        cur = mm(cur, A)
    return out


def basis_of(M):
    """行空间的标准正交基（精确转有理）"""
    if not M:
        return []
    Mn = np.array([[float(x) for x in r] for r in M])
    u, s, vt = np.linalg.svd(Mn, full_matrices=False)
    tol = max(Mn.shape) * (s[0] if s.size else 1) * 1e-12
    rk = int(np.sum(s > tol))
    return [[F(float(x)).limit_denominator(10**7) for x in row] for row in vt[:rk]]


def condA(A, C, L):
    LA = mm(L, A)
    W = L + C + mm(C, A)
    return rank_exact(W + LA) == rank_exact(W)


def eta_q0(A, C, L0):
    p, r, n = len(C), len(L0), len(A)
    gens = [row[:] for row in C] + [row[:] for row in L0]
    M, highest = [], [-1] * (p + r)

    def times(v, q):
        out = v[:]
        for _ in range(q):
            out = mm([out], A)[0]
        return out

    for q in range(n + 1):
        for i in range(p + r):
            if highest[i] >= 0 and q > highest[i] + 1:
                continue
            v = times(gens[i], q)
            if rank_exact(M + [v]) > rank_exact(M):
                M.append(v)
                highest[i] = q
        if all(highest[i] >= 0 and q > highest[i] + 1 for i in range(p + r)):
            break
    alpha = [h + 1 if h >= 0 else 0 for h in highest]
    return [alpha[p + j] for j in range(r)], sum(alpha[p + j] for j in range(r))


def projection_to_perp(W_basis, n):
    """返回投影到 W^⊥ 的矩阵 P（n×n，有理）"""
    if not W_basis:
        return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    Wn = np.array([[float(x) for x in r] for r in W_basis])
    # 标准正交化
    Q, _ = np.linalg.qr(Wn.T)
    Q = Q[:, :Wn.shape[0]]
    P = np.eye(n) - Q @ Q.T
    return [[F(float(P[i][j])).limit_denominator(10**7) for j in range(n)] for i in range(n)]


def construct_A_solution(A, C, L0):
    n = len(A)
    OC = orbit(C, A)
    Z = orbit(L0, A) + OC
    W = C + mm(C, A)
    BZ = basis_of(Z)
    BW = basis_of(W)
    dZ, dW = len(BZ), len(BW)
    P = projection_to_perp(BW, n)          # 投影到 W^⊥

    # π(row(L0)) 的基
    piL0 = [[sum(L0[i][t] * P[t][j] for t in range(n)) for j in range(n)] for i in range(len(L0))]
    piL0 = basis_of(piL0)

    # Krylov 迭代：R̄_0 = span{ piL0 · (Ā)^q }
    Rbar = basis_of(piL0)
    frontier = [r[:] for r in Rbar]
    for _ in range(n + 1):
        new = []
        for v in frontier:
            w = [sum(v[t] * A[t][j] for t in range(n)) for j in range(n)]     # v·A
            w = [sum(w[t] * P[t][j] for t in range(n)) for j in range(n)]     # 投影到 W^⊥
            if any(x != 0 for x in w):
                new.append(w)
        if not new:
            break
        before = rank_exact(Rbar)
        cand = basis_of(Rbar + new)
        if len(cand) == before:
            break
        Rbar = cand
        frontier = new

    # R := row(L0) + span{Rbar 的元素}
    R = basis_of(toF(L0) + Rbar)
    return R, len(R), Rbar


cases = [
    ([[1, 0, 2, 0, -1], [-1, -2, -1, -1, -2], [0, 1, -2, -1, 0],
      [-2, -2, 1, -1, 1], [-2, -2, -1, 0, 0]], [[2, 0, 0, 0, 0]], [[0, 2, 0, 1, 0]], "例1"),
    ([[1, 1, -2, 2, 1], [-1, 2, 2, -1, 2], [2, 1, 1, -2, -2],
      [1, 0, 2, 2, -2], [0, -1, 0, 0, -2]], [[1, 0, -1, -2, -2]], [[-1, -1, -1, 0, -1]], "例2"),
]

print("=" * 84)
print("商空间 Ā-不变包构造 (A)-解")
print("=" * 84)
print()
for Am, Cm, L0m, tag in cases:
    A, C, L0 = toF(Am), toF(Cm), toF(L0m)
    eta, q0 = eta_q0(A, C, L0)
    OC = orbit(C, A)
    Z = orbit(L0, A) + OC
    W = C + mm(C, A)
    R, dimR, Rbar = construct_A_solution(A, C, L0)
    print(f"  {tag}: eta={eta} q0={q0}  r={len(L0)}  dimZ={rank_exact(Z)}  dimW={rank_exact(W)}")
    print(f"    构造的 R 的维数 = {dimR}   (期望 q0 = {q0})")
    print(f"    R 的基:")
    for row in R:
        print(f"      {[str(x) for x in row]}")
    print(f"    (A) 成立? {condA(A, C, R)}")
    print()
