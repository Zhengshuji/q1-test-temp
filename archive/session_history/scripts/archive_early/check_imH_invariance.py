"""
关键实验：im(H) 是否 T-不变？

  若 im(H) 是 T-不变的且 im(H)≠0，则 T|_im(H) 在 C 上有特征向量，
  故 im(H)∩ker(sI−T)≠0 对某 s，(S) 必然失败。
  若 im(H) 不是 T-不变的，(S) 可能成立。

用 P1 §VII 的算例（已知 L_{0,1} 满足 (S)）来判定这个结构问题。
"""
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
        return []                        # n×0
    m = len(sols)
    return [[sols[j][i] for j in range(m)] for i in range(n)]


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


# ---------------- P1 §VII 算例 ----------------
A_rows = [
    [-14,  3, -4,  5, -1, -1,   1,  0],
    [ -3,  5,  3, -2, -6,  0,   8,  0],
    [ 22,-17,  1, -9,  8,  3, -11,  0],
    [  9,-11, -2, -6,  7,  1,  -5,  0],
    [ 21, -2, 12,-14, -6,  3,   2,  0],
    [  0,  1,  0,  0, -1,  0,   3,  0],
    [ 10, -9,  1, -3,  5,  1, -10,  0],
    [  0,  0,  0,  0,  0,  0,   0, -1],
]
C_rows = [[2, -3, 0, 0, 2, 0, -4, 0], [-1, -10, -3, 2, 5, 0, -10, 0]]
L_rows = [[-2, 3, 1, 0, -2, 0, 1, 0], [-7, 8, 3, 0, -6, 0, 2, 0]]

A, C, L = toF(A_rows), toF(C_rows), toF(L_rows)
n = 8

CA = mm(C, A)
CC = C + CA
rho = rank_exact(CC)
N = nullspace_cols(CC)
ncols = len(N[0]) if N and N[0] else 0
print("=" * 78)
print("P1 §VII 算例的结构")
print("=" * 78)
print(f"  n = {n}, p = 2, r = 2")
print(f"  rho = rank[C;CA] = {rho}")
print(f"  N_CA 是 {len(N)}×{ncols} 矩阵（列 = ker 的基）")
print(f"  => rho < n? {rho < n}")
print()


def L_ab(a, b):
    a, b = F(a), F(b)
    row3 = [-4*a - 1, 6*a + 2, 2*a, 0, -4*a - 1, -a, 2*a + 2, 0]
    row4 = [2 - 4*b, 6*b + 1, 2*b, -1, -4*b, -b, 2*b + 3, 0]
    return toF(L_rows) + [row3, row4]


def analyze(Lx, tag):
    print(f"  --- {tag} ---")
    LA = mm(Lx, A)
    d = len(Lx)
    H = mm(Lx, N) if ncols else []
    Fm = mm(LA, N) if ncols else []
    print(f"    rank(L) = {rank_exact(Lx)}")
    if ncols:
        h = rank_exact(H)
        print(f"    H = L·N  ({len(H)}×{len(H[0])}), rank(H) = {h}")
        print(f"    F = LA·N ({len(Fm)}×{len(Fm[0])})")
        # (S) 检验
        rhs = rank_exact(Lx + C + CA)
        fails = []
        for s in [F(k, 2) for k in range(-14, 15)]:
            sl = [[s * Lx[i][j] - LA[i][j] for j in range(n)] for i in range(d)]
            if rank_exact(sl + C + CA) != rhs:
                fails.append(s)
        print(f"    (S) 失败点: {fails[:6] if fails else '无'}")
        # 求 Λ（解 LA = ΛL + G0 C + G1 CA）
        p = len(C)
        nunk = d + 2 * p
        Lam_rows = []
        for i in range(d):
            cols = []
            for j in range(d):
                cols.append([Lx[j][t] for t in range(n)])
            for l in range(p):
                cols.append([C[l][t] for t in range(n)])
            for m_ in range(p):
                cols.append([CA[m_][t] for t in range(n)])
            Des = [[cols[c][t] for c in range(len(cols))] for t in range(n)]
            b = [[LA[i][t]] for t in range(n)]
            Aug = [Des[k][:] + [b[k][0]] for k in range(n)]
            R, piv = rref(Aug)
            ok = True
            for row in R:
                if all(x == 0 for x in row[:nunk]) and row[nunk] != 0:
                    ok = False
            if not ok:
                print(f"      行 {i}: 无解")
                Lam_rows.append(None)
                continue
            y = [F(0)] * nunk
            for k_, pc in enumerate(piv):
                if pc < nunk:
                    y[pc] = R[k_][nunk]
            Lam_rows.append(y[:d])
        if all(x is not None for x in Lam_rows):
            Lam = Lam_rows
            print(f"    Λ = {[[str(x) for x in r] for r in Lam]}")
            # 检验 im(H) 是否 Λ-不变
            HB = basis_of(H)
            if HB:
                LamH = mm(Lam, [[HB[i][j] for i in range(len(HB))] for j in range(len(HB[0]))])
                LamH_rows = [[LamH[j][i] for j in range(len(LamH))] for i in range(len(LamH[0]))]
                inv = in_span(LamH_rows, HB)
                print(f"    im(H) 是 Λ-不变的? {inv}")
            else:
                print(f"    H = 0 => im(H) = 0")
        # im(H) 与 ker(sI−Λ) 的交
        if all(x is not None for x in Lam_rows):
            Lam = Lam_rows
            inter_found = []
            for s in [F(k, 2) for k in range(-14, 15)]:
                sI_L = [[(s if i == j else F(0)) - Lam[i][j] for j in range(d)] for i in range(d)]
                if rank_exact(sI_L) == d:
                    continue                      # 可逆 => ker = {0}
                K = nullspace_cols(sI_L)
                if not K or not K[0]:
                    continue
                nk = len(K[0])
                Krows = [[K[i][j] for j in range(nk)] for i in range(len(K))]
                # im(K) ∩ im(H) ≠ 0 ?
                HB = basis_of(H)
                KH = HB + Krows
                if rank_exact(KH) < rank_exact(HB) + rank_exact(Krows):
                    inter_found.append(s)
            print(f"    im(H) ∩ ker(sI−Λ) ≠ 0 的 s: {inter_found[:6] if inter_found else '无'}")
    print()


analyze(L_ab(0, 0), "L_{0,0}（P1 说 (S) 失败于 λ=-5）")
analyze(L_ab(0, 1), "L_{0,1}（P1 说 (S) 成立）")
