# -*- coding: utf-8 -*-
"""
决定性检验（优化版）：
  (1) 快速扫描，找 (A) 为"部分成立"的格子
  (2) 只对这些格子深入检验 (A)∧(S) 的命中率
"""
from collections import defaultdict
from fractions import Fraction as F

import numpy as np

rng = np.random.default_rng(20260124)


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


def condS_fast(A, C, L):
    """(S) 精确检验，候选 s 精简但覆盖关键点"""
    LA = mm(L, A)
    rhs = rank_exact(L + C + mm(C, A))
    n = len(A)
    cs = set([F(0), F(1), F(-1), F(2), F(-2), F(1, 2), F(-1, 2)])
    try:
        for ev in np.linalg.eigvals(np.array(A, float)):
            if abs(ev.imag) < 1e-7:
                cs.add(F(float(ev.real)).limit_denominator(1000))
        Lf = np.array(L, float)
        LAf = Lf @ np.array(A, float)
        if Lf.shape[0] == Lf.shape[1] and abs(np.linalg.det(Lf)) > 1e-9:
            for ev in np.linalg.eigvals(np.linalg.solve(Lf, LAf)):
                if abs(ev.imag) < 1e-7:
                    cs.add(F(float(ev.real)).limit_denominator(1000))
    except Exception:
        pass
    for s in sorted(cs):
        sl = [[s * L[i][j] - LA[i][j] for j in range(n)] for i in range(len(L))]
        if rank_exact(sl + C + mm(C, A)) != rhs:
            return False
    return True


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


N = 16
# 阶段 1：快速扫描找 (A) 部分成立的格子
partial_cells = []
tot_cells = 0
A_stats = defaultdict(int)

print("阶段 1：扫描 (A) 的命中率结构 ...", flush=True)
for trial in range(200):
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
    eta, q0 = eta_q0(A, C, L0)
    dZ = rank_exact(Z)
    if not (r <= q0 <= dZ):
        continue

    for d in range(q0, dZ + 1):
        ok = tt = 0
        for _ in range(N):
            L = rand_L(L0, Z, d, rng)
            if L is None:
                continue
            tt += 1
            if condA(A, C, L):
                ok += 1
        if tt < N * 0.5:
            continue
        tot_cells += 1
        kind = "all" if ok == tt else ("none" if ok == 0 else "part")
        A_stats[kind] += 1
        if kind == "part":
            partial_cells.append((Am.tolist(), Cm.tolist(), L0m.tolist(),
                                  eta, q0, dZ, d, ok, tt))

print(f"  总格子数 {tot_cells}： (A) 结构 = {dict(A_stats)}")
print(f"  找到 (A) 部分成立的格子: {len(partial_cells)}", flush=True)
print()

# 阶段 2：对部分格子检验 (A)∧(S)
if partial_cells:
    print("阶段 2：对 (A) 部分成立的格子检验 (A)∧(S) ...", flush=True)
    M2 = 30
    for (Am, Cm, L0m, eta, q0, dZ, d, a_ok, a_tt) in partial_cells[:8]:
        A, C, L0 = toF(Am), toF(Cm), toF(L0m)
        OC = orbit(C, A)
        Z = orbit(L0, A) + OC
        a_cnt = s_cnt = tt = 0
        for _ in range(M2):
            L = rand_L(L0, Z, d, rng)
            if L is None:
                continue
            tt += 1
            if condA(A, C, L):
                a_cnt += 1
                if condS_fast(A, C, L):
                    s_cnt += 1
        print(f"  A={Am}")
        print(f"  C={Cm}  L0={L0m}")
        print(f"    eta={eta} q0={q0} dimZ={dZ} d={d}")
        print(f"    (A) {a_cnt}/{tt}   (A)∧(S) {s_cnt}/{tt}"
              f"   {'<== 0/1 仍成立' if s_cnt in (0, tt) else '<== 中间值！0/1 被否证'}")
        print()
else:
    print("  未找到 (A) 部分成立的格子（该现象可能极罕见）")
