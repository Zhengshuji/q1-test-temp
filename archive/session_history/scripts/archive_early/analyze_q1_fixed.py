"""
修正版：N_CA 必须是**列**形式（n × (n−rho)）。

之前把 nullspace_exact 返回的行向量直接喂给 mm，导致 H、F、P(s) 全错。
本脚本用正确的列形式重新分析 rho<n 的结构。
"""
from fractions import Fraction as F

import numpy as np

rng = np.random.default_rng(20260114)


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


def nullspace_cols(M):
    """返回 n×(n−rank) 矩阵，其**列**是 ker M 的基"""
    if not M:
        return []
    n = len(M[0])
    R, piv = rref(M)
    free = [c for c in range(n) if c not in piv]
    if not free:
        return [[] for _ in range(0)]      # 返回 [] 表示 n×0 空矩阵
    sols = []
    for fc in free:
        v = [F(0)] * n
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][fc]
        sols.append(v)
    # n × m
    m = len(sols)
    return [[sols[j][i] for j in range(m)] for i in range(n)]


def orbit(M, A):
    out, cur = [], M
    for _ in range(len(A)):
        out += cur
        cur = mm(cur, A)
    return out


def solve_exact(Des, b):
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
print("修正后的结构分析：A=diag(1,2), C=[1,0], L0=[e2]")
print("=" * 78)
A, C, L0 = toF([[1, 0], [0, 2]]), toF([[1, 0]]), toF([[0, 1]])
n, p, r = 2, 1, 1
N = nullspace_cols(C + mm(C, A))
print(f"  N_CA 是 {len(N)}×{len(N[0]) if N and N[0] else 0} 矩阵（列=ker 的基）")
if N and N[0]:
    print(f"    N = {[[str(x) for x in row] for row in N]}")

for extra in ([F(1), F(0)], [F(1), F(1)], [F(0), F(1)]):
    L = L0 + [extra]
    if rank_exact(L) != 2:
        continue
    LA = mm(L, A)
    d = len(L)
    print(f"\n  L = {[[str(x) for x in r_] for r_ in L]}")
    print(f"    LA = {[[str(x) for x in r_] for r_ in LA]}")

    # 正确计算 H = L·N
    if N and N[0]:
        H = mm(L, N)
        Fm = mm(LA, N)
        print(f"    H = L·N = {[[str(x) for x in r_] for r_ in H]}   rank(H) = {rank_exact(H)}")
        print(f"    F = LA·N = {[[str(x) for x in r_] for r_ in Fm]}")
    else:
        print("    N 为空 => H = 0, F = 0 => (S) 自动成立")
        H = None

    # 解 Λ: LA = ΛL + G0 C + G1 CA
    sols = []
    for i in range(d):
        cols = []
        for j in range(d):
            cols.append([L[j][t] for t in range(n)])
        for l in range(p):
            cols.append([C[l][t] for t in range(n)])
        CA = mm(C, A)
        for m_ in range(p):
            cols.append([CA[m_][t] for t in range(n)])
        Des = [[cols[c][t] for c in range(len(cols))] for t in range(n)]
        b = [[LA[i][t]] for t in range(n)]
        res = solve_exact(Des, b)
        sols.append(res)
    lam_rows = []
    for i, s in enumerate(sols):
        if s is None:
            lam_rows.append(None)
            continue
        y, ns = s
        lam_rows.append((y[:d], len(ns), len(y)))
    for i, s in enumerate(lam_rows):
        if s is None:
            print(f"    行 {i}: 无解")
        else:
            Lam, dns, nunk = s
            print(f"    行 {i}: Λ_i = {[str(x) for x in Lam]}  (解空间维数 {dns}/{nunk})")

    # 检验 (S)
    rhs = rank_exact(L + C + mm(C, A))
    fails = []
    for s in [F(k, 2) for k in range(-12, 13)]:
        sl = [[s * L[i][j] - LA[i][j] for j in range(n)] for i in range(d)]
        if rank_exact(sl + C + mm(C, A)) != rhs:
            fails.append(s)
    print(f"    (S) 失败点: {fails if fails else '无'}")

print()
print("=" * 78)
print("关键检查：P(s) = (sI − Λ)H 是否与 Λ 的选择无关？")
print("=" * 78)
L = L0 + [F(1), F(1)]
if rank_exact(L) == 2:
    d = 2
    LA = mm(L, A)
    # 取两组合法的 Λ（从解空间随机取）
    # 行 0
    cols = []
    for j in range(d):
        cols.append([L[j][t] for t in range(n)])
    cols.append([C[0][t] for t in range(n)])
    CA = mm(C, A)
    cols.append([CA[0][t] for t in range(n)])
    Des0 = [[cols[c][t] for c in range(len(cols))] for t in range(n)]
    b0 = [[LA[0][t]] for t in range(n)]
    res0 = solve_exact(Des0, b0)
    y0, ns0 = res0
    print(f"  行 0 的解空间维数 = {len(ns0)}")
    print(f"    零空间基: {[[str(x) for x in v] for v in ns0]}")
    print(f"    特解: {[str(x) for x in y0]}")

    # 用不同的 Λ 计算 P(s)
    print()
    print("  取两组不同的 Λ（同一行），比较 P(s) 与 H 的秩关系：")
    for t_idx, delta in enumerate([None] + ns0):
        yv = y0[:] if delta is None else [y0[j] + delta[j] for j in range(len(y0))]
        Lam_row = yv[:d]
        if H is not None and N and N[0]:
            # 用这一行的 Λ 与 H 的对应行
            Hr = H[0] if False else None
        # 构造完整 Λ（两行）用特解近似
        print(f"    变体: Λ_0 = {[str(x) for x in Lam_row]}")
