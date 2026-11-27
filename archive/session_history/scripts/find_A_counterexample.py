# -*- coding: utf-8 -*-
"""
找出 "(A) 不全成立" 的那个格子，打印完整详情并做高密度复核。
"""
from fractions import Fraction as F

import numpy as np

rng = np.random.default_rng(20260126)   # 与 mechanism3 相同种子，复现同一批实例


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


def inter_dim(A1, A2):
    return rank_exact(A1) + rank_exact(A2) - rank_exact(A1 + A2)


def basis_of(M):
    if not M:
        return []
    Mn = np.array([[float(x) for x in r] for r in M])
    u, s, vt = np.linalg.svd(Mn, full_matrices=False)
    tol = max(Mn.shape) * (s[0] if s.size else 1) * 1e-12
    rk = int(np.sum(s > tol))
    return [[F(float(x)).limit_denominator(10**7) for x in row] for row in vt[:rk]]


def rand_L(L0, Z, d, rng_):
    BL, BZ = basis_of(L0), basis_of(Z)
    r = len(BL)
    if d < r or d > len(BZ):
        return None
    Q = np.linalg.qr(np.array([[float(x) for x in rr] for rr in BL]).T)[0]
    BZn = np.array([[float(x) for x in rr] for rr in BZ])
    Bq = basis_of([[F(float(x)).limit_denominator(10**7) for x in row]
                   for row in (BZn - BZn @ Q @ Q.T)])
    need = d - r
    if need > len(Bq):
        return None
    if need == 0:
        return BL if rank_exact(BL) == d else None
    coef = rng_.normal(size=(need, len(Bq)))
    rows = [[F(float(sum(coef[i][t] * float(Bq[t][j]) for t in range(len(Bq))))).limit_denominator(10**7)
             for j in range(len(Bq[0]))] for i in range(need)]
    L = BL + rows
    return L if rank_exact(L) == d else None


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


print("复现 mechanism3 的扫描，捕捉 (A) 不全成立的格子 ...\n", flush=True)
found = []
for trial in range(120):
    n = int(rng.integers(2, 6))
    p = int(rng.integers(1, n))
    r = int(rng.integers(1, n - p + 1)) if n - p >= 1 else 1
    Am = rng.integers(-2, 3, (n, n))
    Cm = rng.integers(-2, 3, (p, n))
    L0m = rng.integers(-2, 3, (r, n))
    A, C, L0 = toF(Am), toF(Cm), toF(L0m)
    if rank_exact(C) != p or rank_exact(L0) != r:
        continue
    if rank_exact(L0 + C) != r + p:
        continue
    OC = orbit(C, A)
    Z = orbit(L0, A) + OC
    if rank_exact(Z + OC) != rank_exact(OC):
        continue
    W = C + mm(C, A)
    eta, q0 = eta_q0(A, C, L0)
    dZ, dW = rank_exact(Z), rank_exact(W)
    if not (r <= q0 <= dZ):
        continue
    for d in range(q0, dZ + 1):
        okA = tt = 0
        piset = set()
        for _ in range(25):
            L = rand_L(L0, Z, d, rng)
            if L is None:
                continue
            tt += 1
            piset.add(rank_exact(L + W) - dW)
            if condA(A, C, L):
                okA += 1
        if tt < 20:
            continue
        if okA != tt:
            found.append((Am.tolist(), Cm.tolist(), L0m.tolist(), eta, q0,
                          dZ, dW, d, okA, tt, sorted(piset)))

print(f"找到 {len(found)} 个 (A) 不全成立的格子\n")
for (Am, Cm, L0m, eta, q0, dZ, dW, d, okA, tt, piset) in found:
    print("=" * 80)
    print(f"  A = {Am}")
    print(f"  C = {Cm}")
    print(f"  L0 = {L0m}")
    print(f"  eta={eta}  q0={q0}  dimZ={dZ}  dimW={dW}  dim Z/W={dZ-dW}  d={d}")
    print(f"  初测: (A) 命中 {okA}/{tt},  dim π(R) ∈ {piset}")
    # 高密度复核
    A, C, L0 = toF(Am), toF(Cm), toF(L0m)
    OC = orbit(C, A)
    Z = orbit(L0, A) + OC
    W = C + mm(C, A)
    ok2 = tt2 = 0
    for _ in range(400):
        L = rand_L(L0, Z, d, rng)
        if L is None:
            continue
        tt2 += 1
        if condA(A, C, L):
            ok2 += 1
    print(f"  复核(400): (A) 命中 {ok2}/{tt2} = {ok2/tt2:.3f}")
    if 0 < ok2 < tt2:
        print("  ⚠️⚠️ 确认存在 (A) 的**中间命中率** => 0/1 现象被否证！")
        print(f"      dim Z/W = {dZ-dW}, d = {d}, q0 = {q0}")
    else:
        print(f"  => 高密度复核未复现中间值（初测可能是采样偶然）")
    print()
