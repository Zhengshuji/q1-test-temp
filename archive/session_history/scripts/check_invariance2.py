"""
关键判定（简洁版）：
   im(H) 是否 Λ-不变？  Λ 的特征值是什么？  (S) 是否失败？

用 P1 §VII 算例比较 L_{0,0}（(S) 失败）与 L_{0,1}（(S) 成立）。
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


def ker_cols(M):
    """返回 n×m 矩阵，列为 ker M 的基（m 可为 0）"""
    if not M:
        return []
    n = len(M[0])
    R, piv = rref(M)
    free = [c for c in range(n) if c not in piv]
    if not free:
        return []
    sols = []
    for fc in free:
        v = [F(0)] * n
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][fc]
        sols.append(v)
    m = len(sols)
    return [[sols[j][i] for j in range(m)] for i in range(n)]


def to_rows(M):
    """n×m 矩阵 -> m 个行向量"""
    if not M or not M[0]:
        return []
    n, m = len(M), len(M[0])
    return [[M[i][j] for i in range(n)] for j in range(m)]


A_rows = [
    [-14, 3, -4, 5, -1, -1, 1, 0], [-3, 5, 3, -2, -6, 0, 8, 0],
    [22, -17, 1, -9, 8, 3, -11, 0], [9, -11, -2, -6, 7, 1, -5, 0],
    [21, -2, 12, -14, -6, 3, 2, 0], [0, 1, 0, 0, -1, 0, 3, 0],
    [10, -9, 1, -3, 5, 1, -10, 0], [0, 0, 0, 0, 0, 0, 0, -1],
]
C_rows = [[2, -3, 0, 0, 2, 0, -4, 0], [-1, -10, -3, 2, 5, 0, -10, 0]]
L_rows = [[-2, 3, 1, 0, -2, 0, 1, 0], [-7, 8, 3, 0, -6, 0, 2, 0]]

A, C = toF(A_rows), toF(C_rows)
n, p = 8, 2
CA = mm(C, A)
N = ker_cols(C + CA)
nN = len(N[0]) if (N and N[0]) else 0
print("=" * 76)
print(f"  rho = rank[C;CA] = {rank_exact(C + CA)},  N_CA 的列数 = {nN}")
print("=" * 76)


def L_ab(a, b):
    a, b = F(a), F(b)
    return toF(L_rows) + [
        [-4 * a - 1, 6 * a + 2, 2 * a, 0, -4 * a - 1, -a, 2 * a + 2, 0],
        [2 - 4 * b, 6 * b + 1, 2 * b, -1, -4 * b, -b, 2 * b + 3, 0],
    ]


def get_lambda(Lx):
    """解 LA = ΛL + G0 C + G1 CA，返回 Λ 的特解（每行一个）"""
    LA = mm(Lx, A)
    d = len(Lx)
    nunk = d + 2 * p
    Lam = []
    for i in range(d):
        cols = []
        for j in range(d):
            cols.append([Lx[j][t] for t in range(n)])
        for l in range(p):
            cols.append([C[l][t] for t in range(n)])
        for m_ in range(p):
            cols.append([CA[m_][t] for t in range(n)])
        Des = [[cols[c][t] for c in range(nunk)] for t in range(n)]
        b = [[LA[i][t]] for t in range(n)]
        R, piv = rref([Des[k] + [b[k][0]] for k in range(n)])
        y = [F(0)] * nunk
        for k_, pc in enumerate(piv):
            if pc < nunk:
                y[pc] = R[k_][nunk]
        Lam.append(y[:d])
    return Lam


for (a, b), tag in [((0, 0), "L_{0,0}"), ((0, 1), "L_{0,1}")]:
    Lx = L_ab(a, b)
    LA = mm(Lx, A)
    d = len(Lx)
    H = mm(Lx, N) if nN else []
    Lam = get_lambda(Lx)
    print(f"\n  ===== {tag} =====   rank(L) = {rank_exact(Lx)}")
    # (S)
    rhs = rank_exact(Lx + C + CA)
    fails = [s for s in [F(k, 2) for k in range(-16, 17)]
             if rank_exact([[s * Lx[i][j] - LA[i][j] for j in range(n)] for i in range(d)]
                           + C + CA) != rhs]
    print(f"    (S) 失败点: {[str(x) for x in fails] if fails else '无（(S) 成立）'}")
    print(f"    Λ = {[[str(x) for x in r] for r in Lam]}")
    if nN:
        h = rank_exact(H)
        print(f"    H 的秩 = {h}  (H 是 {len(H)}×{len(H[0])})")
        # im(H) 的基（H 的列空间 = H 的行空间的转置...）
        # H 的像 = {H·v}，其基 = H 的列空间的基
        Hc = [[H[i][j] for i in range(len(H))] for j in range(len(H[0]))]  # 列
        HB = to_rows(ker_cols([])) if False else None
        # 用 rref 求 H 的列空间基
        Hcol = [[H[i][j] for i in range(len(H))] for j in range(len(H[0]))]
        Rc, pivc = rref(Hcol)          # rref 作用于 (m 列数 × d) 会转置，故先转
        # 直接：im(H) = row(H^T)，用 H 的列做行
        imH_rows = Hcol                 # 每个是长度 d 的向量
        RB, pivB = rref(imH_rows)
        imH_basis = [RB[i] for i in range(rank_exact(imH_rows))]
        print(f"    im(H) 的基（{len(imH_basis)} 个）: {[[str(x) for x in v] for v in imH_basis]}")
        # Λ 作用
        Lam_imH = []
        for v in imH_basis:
            w = [sum(v[t] * Lam[t][j] for t in range(d)) for j in range(d)] if False else None
        # 正确：Λ 作用在列向量上：w = Λ · v^T
        Lam_imH = [[sum(Lam[i][t] * v[t] for t in range(d)) for i in range(d)] for v in imH_basis]
        allin = True
        for w in Lam_imH:
            if rank_exact(imH_basis + [w]) > len(imH_basis):
                allin = False
        print(f"    Λ(im(H)) ⊆ im(H)?  {allin}")
        # Λ 的特征值（数值）
        Lamf = np.array([[float(x) for x in r] for r in Lam])
        evs = np.linalg.eigvals(Lamf)
        print(f"    Λ 的特征值（数值）: {np.round(evs, 4).tolist()}")
