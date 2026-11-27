# -*- coding: utf-8 -*-
"""
最终判定：q0 处 (A) 是"空"还是"测度零非空"？
方法：在 Z ⊖ row(L0) 中用**有理网格穷举** d 维子空间（能捕捉测度零的解）。
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


cases = [
    ([[1, 0, 2, 0, -1], [-1, -2, -1, -1, -2], [0, 1, -2, -1, 0],
      [-2, -2, 1, -1, 1], [-2, -2, -1, 0, 0]], [[2, 0, 0, 0, 0]], [[0, 2, 0, 1, 0]]),
    ([[1, 1, -2, 2, 1], [-1, 2, 2, -1, 2], [2, 1, 1, -2, -2],
      [1, 0, 2, 2, -2], [0, -1, 0, 0, -2]], [[1, 0, -1, -2, -2]], [[-1, -1, -1, 0, -1]]),
]

for Am, Cm, L0m in cases:
    A, C, L0 = toF(Am), toF(Cm), toF(L0m)
    eta, q0 = eta_q0(A, C, L0)
    OC = orbit(C, A)
    Z = orbit(L0, A) + OC
    W = C + mm(C, A)
    BL = basis_of(L0)
    r = len(BL)
    rk_Z = rank_exact(Z)
    need = q0 - r
    print("=" * 84)
    print(f"  A={Am}")
    print(f"  C={Cm}  L0={L0m}")
    print(f"    eta={eta} q0={q0} dimZ={rk_Z} r={r} need={need}")
    # Z ⊖ row(L0)
    Q = np.linalg.qr(np.array([[float(x) for x in rr] for rr in BL]).T)[0]
    BZn = np.array([[float(x) for x in rr] for rr in basis_of(Z)])
    resid = BZn - BZn @ Q @ Q.T
    Bq = basis_of([[F(float(x)).limit_denominator(10**7) for x in row] for row in resid])
    dq = len(Bq)
    print(f"    Z ⊖ row(L0) 的维数 = {dq}")
    if need == 0:
        ok = condA(A, C, L0)
        print(f"    need=0 => R = 空, (A) 成立? {ok}")
        print()
        continue
    # 穷举 need 维子空间（有理网格）
    RANGE = 3
    found = 0
    tried = 0
    vecs = [list(p) for p in itertools.product(range(-RANGE, RANGE + 1), repeat=dq)
            if any(p)]
    for combo in itertools.combinations(range(len(vecs)), need):
        rows = []
        for idx in combo:
            c = vecs[idx]
            row = [sum(F(c[t]) * Bq[t][j] for t in range(dq)) for j in range(len(Bq[0]))]
            rows.append(row)
        L = BL + rows
        if rank_exact(L) != q0:
            continue
        tried += 1
        if condA(A, C, L):
            found += 1
            if found <= 2:
                print(f"    ✓ 找到 (A)-解: R = {[[str(x) for x in row] for row in rows]}")
    print(f"    穷举了 {tried} 个不同的 q0 维子空间，其中 {found} 个满足 (A)")
    if found == 0:
        print(f"    => q0 处 (A) **无解**（在这个网格下）")
    else:
        print(f"    => q0 处 (A) **有解**（测度零非空！随机采样会漏掉）")
    print()
