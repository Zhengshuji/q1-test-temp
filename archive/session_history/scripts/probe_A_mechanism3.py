# -*- coding: utf-8 -*-
"""
弄清 "(A) 恒成立 ⟺ d >= q0" 的机制（最后一击）。

【关键公式推导】
  V := row(L0) + row(C) + row(CA) = row(L0) + W,   W := row(C,CA)
  dim V = r + dim W - dim(row(L0) ∩ W)
  由 P1 Thm 2 的等价形式： q0 - r = dim Z - dim V
  => q0 = dim Z - dim W + dim(row(L0) ∩ W)          (*)

  (A) ⟺ π(R) 是 Ā-不变的，  π: Z → Z/W
  dim π(R) = d - dim(R ∩ W)
  若 dim π(R) = dim Z/W，则 π(R) = Z/W，自动不变

  由 (*) 知：需要 d - dim(R ∩ W) = dim Z - dim W
             ⟺ dim(R ∩ W) = d - (dim Z - dim W)
             = d - q0 + dim(row(L0) ∩ W)

本脚本验证：
  (V1) 公式 (*) 是否成立
  (V2) d >= q0 时 dim π(R) 的分布
  (V3) π(R) 是否总 Ā-不变
"""
from fractions import Fraction as F

import numpy as np

rng = np.random.default_rng(20260126)


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


def intersection_basis(A1, A2):
    """row(A1) ∩ row(A2) 的秩（用 Grassmann：dim(X∩Y) = dimX+dimY-dim(X+Y)）"""
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


# ---------- V1: 公式 (*) ----------
print("=" * 84)
print("V1: 检验  q0 = dim Z - dim W + dim(row(L0) ∩ W)")
print("=" * 84)
ok = bad = 0
bads = []
for trial in range(150):
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
    pred = rank_exact(Z) - rank_exact(W) + intersection_basis(L0, W)
    if pred == q0:
        ok += 1
    else:
        bad += 1
        if len(bads) < 3:
            bads.append((eta, q0, rank_exact(Z), rank_exact(W), intersection_basis(L0, W), pred))
print(f"  成立 {ok}，不成立 {bad}")
if bads:
    for eta, q0, dZ, dW, inter, pred in bads:
        print(f"    反例: eta={eta} q0={q0} dimZ={dZ} dimW={dW} dim(L0∩W)={inter} 预测={pred}")
print()

# ---------- V2/V3 ----------
print("=" * 84)
print("V2/V3: d >= q0 时 dim π(R) 与 (A) 的关系")
print("=" * 84)
dist_pi = {}
cnt = 0
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
    q0_pred = dZ - dW + intersection_basis(L0, W)
    if not (r <= q0 <= dZ):
        continue
    for d in range(q0, dZ + 1):
        piset = set()
        okA = 0
        tt = 0
        for _ in range(25):
            L = rand_L(L0, Z, d, rng)
            if L is None:
                continue
            tt += 1
            piset.add(rank_exact(L + W) - dW)      # = dim π(R)
            if condA(A, C, L):
                okA += 1
        if tt < 20:
            continue
        cnt += 1
        key = (tuple(sorted(piset)), okA == tt)
        dist_pi[key] = dist_pi.get(key, 0) + 1

print(f"  {cnt} 个格子。 键 = (dim π(R) 的取值集合, (A) 是否全成立)")
for key in sorted(dist_pi, key=lambda k: (str(k[0]), k[1])):
    piset, allA = key
    print(f"    dim π(R) ∈ {str(piset):32s}  (A) 全成立={allA}:  {dist_pi[key]} 格")
print()
print("  若 (A) 全成立 且 dim π(R) 恒为同一值 => π(R) 恒等于 Z/W（或某个固定不变子空间）")
print("  => 这就是 (A) 恒成立的机制")
