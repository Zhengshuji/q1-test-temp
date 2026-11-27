# -*- coding: utf-8 -*-
"""
找出真正的 (A)-最小可行维数，与 eta 给出的 q0 对照。

若二者不符 => 我对 P1 的 eta/q0 实现（或理解）有误。
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
    return [alpha[p + j] for j in range(r)], sum(alpha[p + j] for j in range(r)), alpha


cases = [
    ([[1, 0, 2, 0, -1], [-1, -2, -1, -1, -2], [0, 1, -2, -1, 0],
      [-2, -2, 1, -1, 1], [-2, -2, -1, 0, 0]], [[2, 0, 0, 0, 0]], [[0, 2, 0, 1, 0]], "例1"),
    ([[1, 1, -2, 2, 1], [-1, 2, 2, -1, 2], [2, 1, 1, -2, -2],
      [1, 0, 2, 2, -2], [0, -1, 0, 0, -2]], [[1, 0, -1, -2, -2]], [[-1, -1, -1, 0, -1]], "例2"),
]

RANGE = 2
for Am, Cm, L0m, tag in cases:
    A, C, L0 = toF(Am), toF(Cm), toF(L0m)
    eta, q0, alpha = eta_q0(A, C, L0)
    OC = orbit(C, A)
    Z = orbit(L0, A) + OC
    rk_Z = rank_exact(Z)
    BL = basis_of(L0)
    r = len(BL)
    Q = np.linalg.qr(np.array([[float(x) for x in rr] for rr in BL]).T)[0]
    BZn = np.array([[float(x) for x in rr] for rr in basis_of(Z)])
    Bq = basis_of([[F(float(x)).limit_denominator(10**7) for x in row]
                   for row in (BZn - BZn @ Q @ Q.T)])
    dq = len(Bq)

    print("=" * 84)
    print(f"  {tag}: A={Am}")
    print(f"    C={Cm}  L0={L0m}")
    print(f"    alpha={alpha}  eta={eta}  q0=sum(eta)={q0}  r={r}  dimZ={rk_Z}  dim(Z⊖row L0)={dq}")
    print()
    vecs = [list(p) for p in itertools.product(range(-RANGE, RANGE + 1), repeat=dq) if any(p)]
    for d in range(r, rk_Z + 1):
        need = d - r
        if need > dq:
            continue
        found = tried = 0
        if need == 0:
            found = 1 if condA(A, C, L0) else 0
            tried = 1
        else:
            for combo in itertools.combinations(range(len(vecs)), need):
                rows = []
                for idx in combo:
                    c = vecs[idx]
                    row = [sum(F(c[t]) * Bq[t][j] for t in range(dq)) for j in range(len(Bq[0]))]
                    rows.append(row)
                L = BL + rows
                if rank_exact(L) != d:
                    continue
                tried += 1
                if condA(A, C, L):
                    found += 1
        mark = ""
        if found > 0:
            mark = "  <== (A) 可行！"
        print(f"    d={d}: 尝试 {tried}, (A)-解 {found}{mark}")
    print()
