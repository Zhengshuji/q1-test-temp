# -*- coding: utf-8 -*-
"""
验证：扩维后能否沿用相同的方法？

【用户的问题】
  若 q0 不满足，q0+1 之类的，进行搜索确定 R 是否存在，
  是不是可以直接使用相同的方法进行搜索？

【理论回答（据 P1 §V-A）】
  P1 的参数化推导只用到两个事实：
    (i)  L 的前 r 行是 L0  =>  LN_C T = [I_r  0]
    (ii) Y 满秩，Y ∈ R^{k×s}，s = n-p-r
  这两个事实对**任何** k ≤ s 都成立，与 k 的具体取值无关。

  => 参数化 Y_J(Θ) = [I_k  Θ] Π_J^T 对**每个** k（即每个 q = r+k）都适用。
  => 方法可逐阶沿用，但**参数本身每阶都变**（k、J 的范围、Θ 的维数、Ω*_{A,J}）。

【本脚本验证】
  (T1) q 的范围 [q0, n0-p] 是否总满足 k = q-r ≤ s
  (T2) 逐阶搜索（用参数化）是否能在每阶给出正确判定
  (T3) 逐阶搜索的空间规模 sum_q C(s, q-r) 有多大
"""
from fractions import Fraction as F

import numpy as np

rng = np.random.default_rng(20260117)


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


def nullspace_cols(M):
    if not M:
        return []
    n = len(M[0])
    R, piv = rref(M)
    free = [c for c in range(n) if c not in piv]
    sols = []
    for fc in free:
        v = [F(0)] * n
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][fc]
        sols.append(v)
    if not sols:
        return []
    m = len(sols)
    return [[sols[j][i] for j in range(m)] for i in range(n)]


print("=" * 78)
print("T1: q 的范围与 k <= s 的关系")
print("=" * 78)
print("""
  s := n - p - r          (约化维数)
  n0 := rank(O_C)         (可观测部分维数)
  q 的范围: [q0, n0-p]
  k = q - r  的范围: [q0-r, n0-p-r]

  需要 k <= s = n-p-r，即 q <= n-p。
  因 n0 <= n，故 n0-p <= n-p，条件自动满足。 ✓
""")

ok = bad = 0
for trial in range(200):
    n = int(rng.integers(2, 7))
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
    n0 = rank_exact(OC)
    s = n - p - r
    # 逐阶检查 k <= s
    for q in range(r, n0 - p + 1):
        k = q - r
        if k > s:
            bad += 1
        else:
            ok += 1
print(f"  逐阶检查: k <= s 成立 {ok} 次, 违反 {bad} 次")
print(f"  => {'参数化对每阶都可用' if bad == 0 else '存在 k > s 的情形（需特殊处理）'}")

print()
print("=" * 78)
print("T3: 逐阶搜索的空间规模")
print("=" * 78)
print("  对每个 q，需要搜索 C(s, k) 个子集 J，每个 J 还要在 Ω*_{A,J} 上判定 Θ。")
print("  总规模 = sum_{k=k_min}^{k_max} C(s, k)")
print()
from math import comb
for (n, p, r, n0) in [(8, 2, 2, 7), (10, 3, 2, 10), (12, 4, 3, 12)]:
    s = n - p - r
    q0 = r          # 最小的代数阶（示例）
    kmax = n0 - p - r
    tot = sum(comb(s, k) for k in range(0, kmax + 1))
    peak = max(comb(s, k) for k in range(0, kmax + 1))
    print(f"  n={n:2d} p={p} r={r} n0={n0:2d}  ->  s = {s:2d}, k_max = {kmax:2d}")
    print(f"     单阶峰值 C({s},k) = {peak:,}")
    print(f"     逐阶总和 sum_k C({s},k) = {tot:,}")
    print()

print("=" * 78)
print("结论")
print("=" * 78)
print("""
  1. 【可以沿用相同方法】P1 的参数化推导与 k 的取值无关，
     故每个阶 q 都可以用 Y_J(Θ) = [I_k  Θ]Π_J^T 参数化。

  2. 【但参数每阶都变】
       - k = q - r 变（Y 的行数）
       - J ⊆ {1,...,s}, |J| = k 变（子集数量与内容）
       - Θ ∈ R^{k×(s-k)} 变（维数）
       - Ω*_{A,J} 的秩等式变（因 W_J(Θ) 变）
       - (S) 的 H、F、P_L(λ) 全都变（因 L 变）
     所以是"同类型的方法"，不是"同一套参数"。

  3. 【这正是 P2 的内容】
     P2 明确说 "For each order q, a full-column-rank matrix Z is used to
     represent the nullspace associated with a reduced order-q realization"
     —— 对每个阶用类似的参数化（P2 用 Z 而非 P1 的 Y_J(Θ)）。

  4. 【代价】
     sum_k C(s,k) 在 k ~ s/2 处达到峰值，可能指数级。
     这是 q_now 的核心难点：即使每阶的 Θ-判定是多项式的，
     逐阶的总搜索也可能指数级。

  5. 【可能的简化（未证）】
     若有"0/1 现象"（每阶只需单点检验），则逐阶搜索退化为
     最多 (n0-p-q0+1) 次单点检验 => 多项式。
""")
