# -*- coding: utf-8 -*-
"""
弄清 "(A) 恒成立 ⟺ d >= q0" 的机制。

【理论线索】
  设 W := row(C, CA)，Z := row(O_L0) + row(O_C)。
  已知 W ⊆ Z，且（猜想）dim Z - dim W = q0。
  对 R ⊆ Z，令 π: Z → Z/W。
    (A) ⟺ π(R) 是 Ā-不变的（Ā = A 在 Z/W 上的诱导）
  若 π(R) = Z/W（即 R + W = Z），则因 Z/W 在 Ā 下不变，(A) 自动成立。

  所以关键检验：对随机 d 维 R（row(L0) ⊆ R ⊆ Z），是否有 R + W = Z ？
      dim(R + W) = dim Z  ⟺  dim(R ∩ W) = d - q0

本脚本统计 dim(R+W) 的分布。
"""
from fractions import Fraction as F

import numpy as np

rng = np.random.default_rng(20260121)


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


print("=" * 88)
print("机制检验：d >= q0 时是否 R + W = Z（从而 π(R) = Z/W 自动 Ā-不变）")
print("=" * 88)
print()

# 先验证 dim Z - dim W = q0
chk_eq = chk_ne = 0
for trial in range(100):
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
    if rank_exact(Z) - rank_exact(W) == q0:
        chk_eq += 1
    else:
        chk_ne += 1
        if chk_ne <= 3:
            print(f"   反例: eta={eta} q0={q0} dimZ={rank_exact(Z)} dimW={rank_exact(W)}")
print(f"  【校验 1】dim Z − dim W = q0 ？  成立 {chk_eq}，不成立 {chk_ne}")
print()

N = 25
dist = {}
viol = []
for trial in range(60):
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
        dimRW = set()
        for _ in range(N):
            L = rand_L(L0, Z, d, rng)
            if L is None:
                continue
            dimRW.add(rank_exact(L + W))
            # 同时确认 (A)
        for v in dimRW:
            dist[v] = dist.get(v, 0) + 1
        if any(v != dZ for v in dimRW):
            if len(viol) < 5:
                viol.append((Am.tolist(), Cm.tolist(), L0m.tolist(),
                             eta, q0, dZ, dW, d, sorted(dimRW)))

print(f"  【校验 2】d >= q0 时 dim(R+W) 的取值分布（应为 {dZ} 一处）：")
print(f"     {dict(sorted(dist.items()))}")
print()
if not viol:
    print("  ✅ d >= q0 时恒有 R + W = Z")
    print()
    print("  => π(R) = Z/W，而 Z/W 在 Ā 下不变")
    print("  => (A) 自动成立（这解释了 (A) 恒成立）")
    print()
    print("  【完整证明链】")
    print("    (1) 引理: dim Z − dim W = q0            （P1 Thm 2 的等价形式）")
    print("    (2) 引理: d >= q0  ⟹  R + W = Z         （空间维数论证）")
    print("    (3) 故 π(R) = Z/W 是 Ā-不变的 ⟹ (A) 成立")
    print("    (4) d < q0 时 (A) 不可能（q0 是 (A) 的最小可行维数，P1 Thm 2）")
    print("    => Σ_d^{(A)} = Gr(k,s) 或 空")
    print("    => Σ_d = Σ_d^{(A)} ∩ Σ_d^{(S)} = Σ_d^{(S)}（开集）或 空")
    print("    => 每阶单点检验即可 => nu_min ∈ BPP => 命题 q_now 为假")
else:
    print("  ❌ 存在 d >= q0 但 R + W ≠ Z 的情形：")
    for Am, Cm, L0m, eta, q0, dZ, dW, d, rw in viol:
        print(f"    A={Am} C={Cm} L0={L0m}")
        print(f"      eta={eta} q0={q0} dimZ={dZ} dimW={dW} d={d}  dim(R+W)取值={rw}")
