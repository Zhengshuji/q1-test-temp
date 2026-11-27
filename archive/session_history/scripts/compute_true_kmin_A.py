# -*- coding: utf-8 -*-
"""
计算 (A)-最小维数，与 eta/q0 对照。

理论：
  (A) ⟺ π(R) 是 Ā-不变的，  π: Z → Z/W
  R ⊇ row(L0)  ⟹  π(R) ⊇ π(row(L0))
  故 π(R) 必须包含 R̄_0 := 含 π(row(L0)) 的最小 Ā-不变子空间
  => dim R >= dim R̄_0
  => (A)-最小维数 = min{ dim R : π(R) ⊇ R̄_0, R ⊇ row(L0) }

本脚本计算 d0 := dim R̄_0，并显式构造达到它的 R。
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


def perp_projector(W_basis, n):
    if not W_basis:
        return [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    Wn = np.array([[float(x) for x in r] for r in W_basis])
    Q, _ = np.linalg.qr(Wn.T)
    Q = Q[:, :Wn.shape[0]]
    P = np.eye(n) - Q @ Q.T
    return [[F(float(P[i][j])).limit_denominator(10**7) for j in range(n)] for i in range(n)]


def krylov_package(A, seeds, P, n):
    """含 seeds 的最小 Ā-不变子空间，在 W^⊥ 中（P 是投影）"""
    def pi(v):
        return [sum(v[t] * P[t][j] for t in range(n)) for j in range(n)]

    cur = basis_of([pi(s) for s in seeds])
    frontier = [r[:] for r in cur]
    for _ in range(2 * n + 2):
        newf = []
        for v in frontier:
            w = pi(mm([v], A)[0])
            if any(x != 0 for x in w):
                newf.append(w)
        if not newf:
            break
        before = len(cur)
        cand = basis_of(cur + newf)
        if len(cand) == before:
            break
        cur = cand
        frontier = newf
    return cur


cases = [
    ([[1, 0, 2, 0, -1], [-1, -2, -1, -1, -2], [0, 1, -2, -1, 0],
      [-2, -2, 1, -1, 1], [-2, -2, -1, 0, 0]], [[2, 0, 0, 0, 0]], [[0, 2, 0, 1, 0]], "例1"),
    ([[1, 1, -2, 2, 1], [-1, 2, 2, -1, 2], [2, 1, 1, -2, -2],
      [1, 0, 2, 2, -2], [0, -1, 0, 0, -2]], [[1, 0, -1, -2, -2]], [[-1, -1, -1, 0, -1]], "例2"),
]

print("=" * 88)
print("(A)-最小维数 vs eta/q0")
print("=" * 88)
print()
for Am, Cm, L0m, tag in cases:
    A, C, L0 = toF(Am), toF(Cm), toF(L0m)
    n = len(A)
    eta, q0 = eta_q0(A, C, L0)
    OC = orbit(C, A)
    Z = orbit(L0, A) + OC
    W = C + mm(C, A)
    BW = basis_of(W)
    P = perp_projector(BW, n)
    Rbar = krylov_package(A, L0, P, n)
    d0 = len(Rbar)

    print(f"  {tag}: eta={eta}  q0={q0}  r={len(L0)}  dimZ={rank_exact(Z)}  dimW={rank_exact(W)}")
    print(f"    dim R̄_0 (最小 Ā-不变包) = {d0}")
    print(f"    => (A)-最小维数 >= {d0}")

    # 显式构造 R = row(L0) + Rbar 的提升
    R = basis_of(toF(L0) + Rbar)
    print(f"    构造 R = row(L0) + R̄_0 的提升: dim = {len(R)},  (A) = {condA(A, C, R)}")
    # 尝试更小的：只用 Rbar（若它已含 row(L0) 的 π-原像信息）
    print(f"    q0 = {q0}  vs  d0 = {d0}  ->  {'相等 ✓' if q0 == d0 else '**不等** ✗'}")
    print()
