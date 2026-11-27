# -*- coding: utf-8 -*-
"""
找 "(A) 恒成立 ⟺ d >= q0" 的真正机制。

候选机制（逐个检验）：
  M1: R·A ⊆ W                （更强，蕴含 (A)）
  M2: R + W = Z              （已被否证）
  M3: π(R) 的维数恰好使其 Ā-不变
  M4: R·A ⊆ R                （R 本身 A-不变，最强）
"""
from fractions import Fraction as F

import numpy as np

rng = np.random.default_rng(20260122)


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


def in_span(X, Y):
    X = [r for r in X if any(v != 0 for v in r)]
    if not X:
        return True
    return rank_exact(Y + X) == rank_exact(Y)


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


N = 20
stat = {"M1_all": 0, "M1_none": 0, "M1_part": 0,
        "M4_all": 0, "M4_none": 0, "M4_part": 0,
        "A_all": 0, "A_part": 0}
tot = 0

for trial in range(50):
    n = int(rng.integers(2, 6))
    p = int(rng.integers(1, n))
    r = int(rng.integers(1, n - p + 1)) if n - p >= 1 else 1
    A = toF(rng.integers(-2, 3, (n, n)))
    C = toF(rng.integers(-2, 3, (p, n)))
    L0 = toF(rng.integers(-2, 3, (r, n)))
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
    dZ = rank_exact(Z)
    if not (r <= q0 <= dZ):
        continue

    for d in range(q0, dZ + 1):
        m1 = m4 = a_ok = 0
        tt = 0
        for _ in range(N):
            L = rand_L(L0, Z, d, rng)
            if L is None:
                continue
            tt += 1
            LA = mm(L, A)
            if in_span(LA, W):
                m1 += 1
            if in_span(LA, L):
                m4 += 1
            if in_span(LA, L + C + mm(C, A)):
                a_ok += 1
        if tt < N * 0.5:
            continue
        tot += 1
        for name, cnt in (("M1", m1), ("M4", m4)):
            if cnt == tt:
                stat[name + "_all"] += 1
            elif cnt == 0:
                stat[name + "_none"] += 1
            else:
                stat[name + "_part"] += 1
        if a_ok == tt:
            stat["A_all"] += 1
        else:
            stat["A_part"] += 1

print("=" * 80)
print(f"  在 {tot} 个 (实例, d>=q0) 格子上统计各机制")
print("=" * 80)
print()
print(f"  M1 (R·A ⊆ W)      : 恒成立 {stat['M1_all']}, 恒不成立 {stat['M1_none']}, 部分 {stat['M1_part']}")
print(f"  M4 (R·A ⊆ R)      : 恒成立 {stat['M4_all']}, 恒不成立 {stat['M4_none']}, 部分 {stat['M4_part']}")
print(f"  (A)  (R·A ⊆ R+W)  : 恒成立 {stat['A_all']}, 部分 {stat['A_part']}")
print()
if stat["A_part"] == 0:
    print("  ✅ (A) 在 d >= q0 时恒成立（本实验再次确认）")
    if stat["M1_all"] == tot:
        print("     机制 = M1：R·A ⊆ W")
    elif stat["M4_all"] == tot:
        print("     机制 = M4：R·A ⊆ R（R 自身 A-不变）")
    else:
        print("     M1/M4 都不是普遍机制，需另找解释")
else:
    print(f"  ❌ (A) 有 {stat['A_part']} 个格子非恒成立")
