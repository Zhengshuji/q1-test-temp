# -*- coding: utf-8 -*-
"""完整比对：参数化解的 RN_CT 与 [0|Y_J]，并在 P1 §VII 算例上验证 condA。"""
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
    n, k, m = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def toF(M):
    return [[F(int(x)) for x in row] for row in M]


def transpose(M):
    return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]


def inv(M):
    n = len(M)
    R, piv = rref([M[i][:] + [F(1) if i == j else F(0) for j in range(n)] for i in range(n)])
    if len(piv) != n:
        return None
    return [row[n:] for row in R]


def ker_cols(M):
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


def solve_exact(Des, b):
    m, k = len(Des), len(Des[0])
    R, piv = rref([Des[i][:] + [b[i][0]] for i in range(m)])
    for row in R:
        if all(x == 0 for x in row[:k]) and row[k] != 0:
            return None
    y = [F(0)] * k
    for i, pc in enumerate(piv):
        if pc < k:
            y[pc] = R[i][k]
    return y


def condA(A, C, L):
    LA = mm(L, A)
    W = L + C + mm(C, A)
    return rank_exact(W + LA) == rank_exact(W)


def build(A, C, L0):
    n, p, r = len(A), len(C), len(L0)
    NC = ker_cols(C)
    dC = len(NC[0])
    MC = mm(inv(mm(transpose(NC), NC)), transpose(NC))
    L0NC = mm(L0, NC)
    Tcols = []
    for i in range(r):
        e = [F(1) if q == i else F(0) for q in range(r)]
        Tcols.append(solve_exact([[L0NC[i2][j] for j in range(dC)] for i2 in range(r)],
                                 [[e[i2]] for i2 in range(r)]))
    KN = ker_cols(L0NC)
    for j in range(len(KN[0])):
        Tcols.append([KN[i][j] for i in range(dC)])
    T = [[Tcols[j][i] for j in range(dC)] for i in range(dC)]
    return dict(NC=NC, MC=MC, T=T, Tinv=inv(T), dC=dC, r=r, p=p, n=n)


def gen_R(S, A, C, J, th, k):
    dC, r = S['dC'], S['r']
    s = dC - r
    Y = [F(0)] * s
    Y[J[0]] = F(1)
    rest = [i for i in range(s) if i not in J]
    for pos in rest:
        Y[pos] = th
    WJ = [[F(1) if j == i else F(0) for j in range(dC)] for i in range(r)]
    WJ.append([F(0)] * r + Y)
    XJ = mm(WJ, S['Tinv'])
    R = mm(XJ[r:], S['MC'])
    return R, Y, WJ


# ---------- 反例1 ----------
Am = [[1, 0, 2, 0, -1], [-1, -2, -1, -1, -2], [0, 1, -2, -1, 0],
      [-2, -2, 1, -1, 1], [-2, -2, -1, 0, 0]]
Cm = [[2, 0, 0, 0, 0]]
L0m = [[0, 2, 0, 1, 0]]
A, C, L0 = toF(Am), toF(Cm), toF(L0m)
S = build(A, C, L0)
print("=" * 80)
print("反例1：RN_CT 与 [0|Y_J] 的完整比对")
print("=" * 80)
for J in [(0,)]:
    R, Y, WJ = gen_R(S, A, C, J, F(0), 1)
    RNCT = mm(mm(R, S['NC']), S['T'])
    print(f"  J={J}, Y={[str(x) for x in Y]}")
    print(f"  RN_CT = {[[str(x) for x in row] for row in RNCT]}")
    print(f"  期望 [0|Y] = {[[str(x) for x in ([F(0)]*(S['r']) + Y)]]}")
    Lx = toF(L0) + R
    print(f"  L = {[[str(x) for x in row] for row in Lx]}")
    print(f"  condA = {condA(A, C, Lx)}")
    # 直接算 (A) 的原始秩
    LA = mm(Lx, A)
    print(f"  rank[LA;L;CA;C] = {rank_exact(LA + Lx + C + mm(C,A))}, "
          f"rank[L;CA;C] = {rank_exact(Lx + C + mm(C,A))}")
print()

# ---------- P1 §VII 算例 ----------
A8 = [[-14, 3, -4, 5, -1, -1, 1, 0], [-3, 5, 3, -2, -6, 0, 8, 0],
      [22, -17, 1, -9, 8, 3, -11, 0], [9, -11, -2, -6, 7, 1, -5, 0],
      [21, -2, 12, -14, -6, 3, 2, 0], [0, 1, 0, 0, -1, 0, 3, 0],
      [10, -9, 1, -3, 5, 1, -10, 0], [0, 0, 0, 0, 0, 0, 0, -1]]
C8 = [[2, -3, 0, 0, 2, 0, -4, 0], [-1, -10, -3, 2, 5, 0, -10, 0]]
L8 = [[-2, 3, 1, 0, -2, 0, 1, 0], [-7, 8, 3, 0, -6, 0, 2, 0]]
A2, C2, L02 = toF(A8), toF(C8), toF(L8)
try:
    S2 = build(A2, C2, L02)
    k2 = 2
    print("=" * 80)
    print("P1 §VII 算例（n=8, q0=4, k=2）")
    print("=" * 80)
    dC2, r2 = S2['dC'], S2['r']
    print(f"  d_C={dC2}, r={r2}, s={dC2-r2}, k={k2}")
    import itertools
    for J in list(itertools.combinations(range(dC2 - r2), k2))[:2]:
        for th in [F(0), F(1)]:
            # k=2: Theta 是 2x(s-2)
            s2 = dC2 - r2
            rest = [i for i in range(s2) if i not in J]
            Y = [[F(0)] * s2 for _ in range(k2)]
            for a, jj in enumerate(J):
                Y[a][jj] = F(1)
            for a in range(k2):
                for b, pos in enumerate(rest):
                    Y[a][pos] = th if a == b else F(0)
            WJ = [[F(1) if j == i else F(0) for j in range(dC2)] for i in range(r2)]
            for a in range(k2):
                WJ.append([F(0)] * r2 + Y[a])
            XJ = mm(WJ, S2['Tinv'])
            R = mm(XJ[r2:], S2['MC'])
            Lx = toF(L02) + R
            print(f"  J={J} th={th}: rank(L)={rank_exact(Lx)}  condA={condA(A2, C2, Lx)}")
except Exception as ex:
    print(f"  P1 算例处理失败: {ex}")
