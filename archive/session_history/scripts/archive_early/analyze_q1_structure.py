"""
q1 的核心：rho < n 时的结构分析。

关键：由 (A) 有 LA ⊆ row(L, C, CA)，即存在 (Λ, G0, G1) 使
      LA = Λ L + G0 C + G1 CA.        (*)
   右乘 N_CA（ker[C;CA] 的基）得
      (LA)N_CA = Λ (L N_CA)  =>  F = Λ H.

   Λ 一般**不唯一**（(*)' 的解空间是仿射的）。
   本脚本要回答：
     (Q1) Λ 的不唯一性有多大？
     (Q2) P(s) = sH − F = (sI−Λ)H 是否与 Λ 的选择无关？
     (Q3) (S) 的成立性与 Λ 的谱有何关系？
"""
import itertools
from fractions import Fraction as F

import numpy as np

rng = np.random.default_rng(20260113)


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
                p = i; break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(nrow):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c); r += 1
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


def nullspace_exact(M):
    if not M:
        return []
    n = len(M[0])
    R, piv = rref(M)
    free = [c for c in range(n) if c not in piv]
    out = []
    for fc in free:
        v = [F(0)] * n
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][fc]
        out.append(v)
    return out


def orbit(M, A):
    out, cur = [], M
    for _ in range(len(A)):
        out += cur
        cur = mm(cur, A)
    return out


def solve_general(Des, b):
    """
    解 Des · y = b，其中 Des 是 (m×k)，b 是 (m×1)。
    返回 (特解 y, 零空间基) 或 None（不相容）。
    """
    m, k = len(Des), len(Des[0])
    Aug = [Des[i][:] + [b[i][0]] for i in range(m)]
    R, piv = rref(Aug)
    for row in R:
        if all(x == 0 for x in row[:k]) and row[k] != 0:
            return None
    y = [F(0)] * k
    for i, pc in enumerate(piv):
        if pc < k:
            y[pc] = R[i][k]
    free = [c for c in range(k) if c not in piv]
    ns = []
    for fc in free:
        v = [F(0)] * k
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            if pc < k:
                v[pc] = -R[i][fc]
        ns.append(v)
    return y, ns


print("=" * 78)
print("分析 LA = ΛL + G0 C + G1 CA 的解结构")
print("=" * 78)
print("  对每一行 i：L_i A = Σ_j Λ_ij L_j + Σ_l (G0)_il C_l + Σ_m (G1)_im (CA)_m")
print("  即 L_i A ∈ row(L, C, CA)（这正是 (A) 的等价形式）")
print()

# 选一个 rho < n 的实例
Am = [[1, 0], [0, 2]]
Cm = [[1, 0]]
L0m = [[0, 1]]
A, C, L0 = toF(Am), toF(Cm), toF(L0m)
print(f"  A={Am}, C={Cm}, L0={L0m}")
print(f"  rank[C;CA] = {rank_exact(C + mm(C, A))}  (n={len(A)})")
NCA = nullspace_exact(C + mm(C, A))
print(f"  N_CA 的基: {[[str(x) for x in v] for v in NCA]}")
print()

# 对几个 L 计算 Λ、H、F
for extra in ([F(1), F(0)], [F(1), F(1)], [F(0), F(1)]):
    L = L0 + [extra] if rank_exact(L0 + [extra]) == 2 else None
    if L is None:
        continue
    LA = mm(L, A)
    W = L + C + mm(C, A)
    print(f"  L = {[[str(x) for x in r] for r in L]}   rank(L)={rank_exact(L)}")
    print(f"    (A) 成立? {rank_exact(W + LA) == rank_exact(W)}")
    # 对每行解 Λ 与 G
    d = len(L)
    p = len(C)
    # 行 i: L_i A = Σ_j Λ_ij L_j + Σ_l G_il C_l + Σ_m H_im (CA)_m
    # 未知数: Λ_i* (d个), G0_i* (p个), G1_i* (p个)  —— 共 d+2p
    # 方程: n 个 (L_i A 的分量)
    sols = []
    for i in range(d):
        # 构造设计矩阵: 列 = [L_1^T ... L_d^T, C_1^T ... C_p^T, CA_1^T ... CA_p^T]
        cols = []
        for j in range(d):
            cols.append([L[j][t] for t in range(len(A))])
        for l in range(p):
            cols.append([C[l][t] for t in range(len(A))])
        CA = mm(C, A)
        for m_ in range(p):
            cols.append([CA[m_][t] for t in range(len(A))])
        # cols 是 (n_unk × n)，转置成 (n × n_unk)
        Des = [[cols[c][t] for c in range(len(cols))] for t in range(len(A))]
        b = [[LA[i][t]] for t in range(len(A))]
        res = solve_general(Des, b)
        if res is None:
            sols.append(None)
        else:
            y, ns = res
            sols.append((y, len(ns), len(cols)))
    for i, s in enumerate(sols):
        if s is None:
            print(f"    第 {i} 行无解（违反 (A)？）")
        else:
            y, dimns, nunk = s
            Lam = [y[j] for j in range(d)]
            Fval = [y[d + 2 * p + 0] if False else None]
            print(f"    第 {i} 行: Λ_i = {[str(x) for x in Lam]}, "
                  f"解空间维数 = {dimns}/{nunk}")
    # 计算 H, F
    H = mm(L, NCA) if NCA else []
    Fm = mm(LA, NCA) if NCA else []
    if H:
        print(f"    H = {[[str(x) for x in r] for r in H]}, F = {[[str(x) for x in r] for r in Fm]}")
        print(f"    rank H = {rank_exact(H)}")
        # (S) 检验
        rhs = rank_exact(L + C + mm(C, A))
        fails = []
        for s in [F(k, 2) for k in range(-12, 13)]:
            sl = [[s * L[i][j] - LA[i][j] for j in range(len(A))] for i in range(len(L))]
            if rank_exact(sl + C + mm(C, A)) != rhs:
                fails.append(s)
        print(f"    (S) 失败点: {fails if fails else '无'}")
    print()
