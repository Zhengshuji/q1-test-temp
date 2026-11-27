# -*- coding: utf-8 -*-
"""
用 P1 §V 的参数化直接计算 Omega*_{A,J} 的维数。

  N_C: ker C 的基 (n × d_C),  d_C = n - p
  M_C: 左逆 (d_C × n),  M_C N_C = I
  T  : d_C × d_C 使 L0 N_C T = [I_r  0]
  Abar = M_C A N_C,  B_A = C A N_C
  Abar_T = T^{-1} Abar T,  B_{A,T} = B_A T

  W_J(Θ) = [[I_r, 0], [0, Y_J(Θ)]]  ( (r+k) × d_C )
  Y_J(Θ) = [I_k  Θ] Π_J^T,  Θ ∈ R^{k×(s-k)},  s = d_C - r

  (A) 的约化形式:
      rank [ W_J(Θ) Abar_T ]  =  rank [ W_J(Θ) ]
           [   B_{A,T}    ]         [ B_{A,T}  ]

本脚本在 Θ 空间上细密扫描，判定 Omega*_{A,J} 是有限点集还是正维数。
"""
import itertools
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
    return y


def ker_cols(M):
    if not M:
        return []
    n = len(M[0])
    R, piv = rref(M)
    free = [c for c in range(n) if c not in piv]
    if not free:
        return [[] for _ in range(0)]
    sols = []
    for fc in free:
        v = [F(0)] * n
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][fc]
        sols.append(v)
    m = len(sols)
    return [[sols[j][i] for j in range(m)] for i in range(n)]


def transpose(M):
    if not M:
        return []
    return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]


def inv(M):
    n = len(M)
    A = [M[i][:] + [F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    R, piv = rref(A)
    if len(piv) != n or any(p != i for i, p in enumerate(piv)):
        return None
    return [row[n:] for row in R]


def setup(A, C, L0):
    n, p, r = len(A), len(C), len(L0)
    NC = ker_cols(C)                       # n × d_C
    dC = len(NC[0]) if (NC and NC[0]) else 0
    # L0 N_C 的精确行
    L0NC = mm(L0, NC)                      # r × d_C
    # 求 T 使 L0NC · T = [I_r | 0]
    # 先求 L0NC 的行空间补全：取 M_C 使 M_C N_C = I
    # M_C: d_C × n，满足 M_C N_C = I_{d_C}
    NCt = transpose(NC)                    # d_C × n
    # N_C 列满秩 => N_C^T N_C 可逆，M_C = (N_C^T N_C)^{-1} N_C^T
    NCtNC = mm(NCt, NC)
    invNCtNC = inv(NCtNC)
    MC = mm(invNCtNC, NCt)                 # d_C × n
    Abar = mm(mm(MC, A), NC)
    BA = mm(mm(C, A), NC)
    # T: 使 L0NC T = [I_r | 0]
    # 构造 T 的列：前 r 列解 L0NC x = e_i，后 d_C-r 列解 L0NC x = 0
    L0NCt = L0NC
    # 解 L0NC x = b  （x 是 d_C 维列向量）
    def solve_col(b):
        Des = [[L0NCt[i][j] for j in range(dC)] for i in range(r)]
        bb = [[b[i]] for i in range(r)]
        return solve_exact(Des, bb)
    Tcols = []
    for i in range(r):
        e = [F(1) if k == i else F(0) for k in range(r)]
        x = solve_col(e)
        if x is None:
            return None
        Tcols.append(x)
    for k in range(dC - r):
        # 取 L0NC 的核中的向量
        pass
    KN = ker_cols(L0NC)                    # d_C × (d_C - r)
    for j in range(len(KN[0]) if (KN and KN[0]) else 0):
        Tcols.append([KN[i][j] for i in range(dC)])
    if len(Tcols) != dC:
        return None
    T = [[Tcols[j][i] for j in range(dC)] for i in range(dC)]   # d_C × d_C
    if rank_exact(T) != dC:
        return None
    Tinv = inv(T)
    AbarT = mm(mm(Tinv, Abar), T)
    BAT = mm(BA, T)
    return dict(NC=NC, MC=MC, T=T, dC=dC, AbarT=AbarT, BAT=BAT, r=r, p=p, n=n)


Am = [[1, 0, 2, 0, -1], [-1, -2, -1, -1, -2], [0, 1, -2, -1, 0],
      [-2, -2, 1, -1, 1], [-2, -2, -1, 0, 0]]
Cm = [[2, 0, 0, 0, 0]]
L0m = [[0, 2, 0, 1, 0]]
A, C, L0 = toF(Am), toF(Cm), toF(L0m)
S = setup(A, C, L0)
if S is None:
    print("setup 失败")
    raise SystemExit
print("=" * 84)
print("P1 §V 参数化下的 Omega*_{A,J}")
print("=" * 84)
print(f"  n={S['n']} p={S['p']} r={S['r']} d_C={S['dC']}")
print(f"  Abar_T = {[[str(x) for x in row] for row in S['AbarT']]}")
print(f"  B_A,T  = {[[str(x) for x in row] for row in S['BAT']]}")
print()

dC, r, k = S['dC'], S['r'], 1
s = dC - r
print(f"  s = d_C - r = {s},  k = 1,  Theta in R^(1 x {s-k})")

# 枚举 J (|J| = k = 1)
results = {}
for J in itertools.combinations(range(s), k):
    # Y_J(Theta) = [I_k  Theta] Pi_J^T  -> 1 x s
    # 构造：位置 J[0]=1，其余位置为 theta
    rest = [i for i in range(s) if i not in J]
    hits = []
    RANGE = 4
    grid = [F(a, 2) for a in range(-RANGE * 2, RANGE * 2 + 1)]
    for th in grid:
        Y = [F(0)] * s
        Y[J[0]] = F(1)
        for idx, pos in enumerate(rest):
            Y[pos] = th
        # W_J = [[I_r, 0], [0, Y]]
        WJ = []
        for i in range(r):
            WJ.append([F(1) if j == i else F(0) for j in range(dC)])
        WJ.append([F(0)] * r + Y)
        left = mm(WJ, S['AbarT'])
        # P1 式 (20)：左端是三块 [ W_J ; B_A,T ; W_J Abar_T ]
        LHS = WJ + S['BAT'] + left
        RHS = WJ + S['BAT']
        if rank_exact(LHS) == rank_exact(RHS):
            hits.append(th)
    results[J] = hits
    print(f"  J={J}: (A) 命中的 Θ 值（网格 {RANGE*2+1} 点，步长 1/2）: {[str(t) for t in hits]}")

print()
tot = sum(len(v) for v in results.values())
print(f"  总命中数 = {tot}")
if tot == 0:
    print("  => 在该网格上无 (A)-解（可能需要更大范围或非网格值）")
elif all(len(v) <= 3 for v in results.values()):
    print("  => 解集看起来是**有限点集**")
else:
    print("  => 解集可能是**正维数**（曲线上有连续多个点）")
