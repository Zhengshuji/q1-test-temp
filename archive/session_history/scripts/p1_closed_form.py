# -*- coding: utf-8 -*-
"""
实现 P1 §IV 的完整闭式构造，生成满足 (A) 的增广。

记 gens = [C 的各行; L0 的各行] = [g_1..g_{p+r}]
全局顺序: q=0: g_1..g_{p+r};  q=1: g_1 A..g_{p+r} A; ...

保留矩阵 M (按序)，alpha_i = 第一个被拒的幂次, eta_j = alpha_{p+j}
M^-_{p+j} = M 中检查顺序早于 g_{p+j}A^{eta_j} 的行
phi_{p+j}:  L_j A^{eta_j} = phi * M^-_{p+j}   (唯一)
分块:  G^{(q)} = M^- 中幂次为 q 的行;  phi^{(q)} 为对应系数

闭式 (P1 L403-419):
   ell_{j,t} = L_j A^t - sum_{q = eta_j-t+1}^{eta_j} phi^{(q)} G^{(q)} A^{q-(eta_j-t)},
   t = 1, ..., eta_j - 1
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


def times(v, A, q):
    out = v[:]
    for _ in range(q):
        out = mm([out], A)[0]
    return out


def condA(A, C, L):
    LA = mm(L, A)
    W = L + C + mm(C, A)
    return rank_exact(W + LA) == rank_exact(W)


def solve_coeff(target, basis_rows):
    """解 target = phi * basis_rows（精确）。basis_rows 行无关。"""
    if not basis_rows:
        return [] if all(x == 0 for x in target) else None
    n = len(target)
    k = len(basis_rows)
    # 方程: sum_i phi_i * basis_rows[i][j] = target[j]
    # 用最小二乘的正规方程（精确）：构造增广 [B^T | target^T]，解 k 个未知
    Aug = [[basis_rows[i][j] for i in range(k)] + [target[j]] for j in range(n)]
    R, piv = rref(Aug)
    for row in R:
        if all(x == 0 for x in row[:k]) and row[k] != 0:
            return None
    phi = [F(0)] * k
    for i, pc in enumerate(piv):
        if pc < k:
            phi[pc] = R[i][k]
    return phi


def P1_construct(A, C, L0, verbose=False):
    n, p, r = len(A), len(C), len(L0)
    gens = [row[:] for row in C] + [row[:] for row in L0]
    ngen = p + r

    M, M_info = [], []          # M_info: (i, q)
    rejected = {}
    for q in range(n + 1):
        for i in range(ngen):
            if i in rejected:
                continue
            v = times(gens[i], A, q)
            if rank_exact(M + [v]) > rank_exact(M):
                M.append(v)
                M_info.append((i, q))
            else:
                rejected[i] = q
        if len(rejected) == ngen:
            break

    alpha = [rejected.get(i, n + 1) for i in range(ngen)]
    eta = [alpha[p + j] for j in range(r)]

    if verbose:
        print(f"    M 的行 (i,q): {M_info}")
        print(f"    alpha = {alpha}")
        print(f"    eta   = {eta}")

    R_rows = []
    for j in range(r):
        i = p + j
        a_i = alpha[i]
        if a_i > n:
            continue
        # M^- : 检查顺序早于 (a_i, i) 的保留行
        Mminus, Minfo_minus = [], []
        for (ii, qq), row in zip(M_info, M):
            if (qq < a_i) or (qq == a_i and ii < i):
                Mminus.append(row)
                Minfo_minus.append((ii, qq))
        target = times(gens[i], A, a_i)
        phi = solve_coeff(target, Mminus)
        if phi is None:
            if verbose:
                print(f"    j={j}: phi 无解！")
            continue
        # 分块 phi^{(q)}
        phi_q = {}
        for idx, (ii, qq) in enumerate(Minfo_minus):
            phi_q.setdefault(qq, {})[idx] = phi[idx]
        eta_j = eta[j]
        for t in range(1, eta_j):
            shift = eta_j - t
            row = times(gens[i], A, t)          # L_j A^t
            for q in range(shift + 1, eta_j + 1):
                if q not in phi_q:
                    continue
                # G^{(q)} 的行是 **generators** g_ii（对应 M^- 中幂次 q 的保留行 g_ii A^q）
                for idx, (ii, qq) in enumerate(Minfo_minus):
                    if qq != q:
                        continue
                    c = phi[idx]
                    if c == 0:
                        continue
                    # 项:  phi^{(q)}_{ii} * g_ii * A^{q - shift}
                    term = times(gens[ii], A, q - shift)
                    row = [row[k] - c * term[k] for k in range(n)]
            R_rows.append(row)

    Lx = toF(L0) + R_rows
    return Lx, eta, alpha


print("=" * 84)
print("P1 闭式构造的实现与验证")
print("=" * 84)
print()

cases = [
    ([[1, 0, 2, 0, -1], [-1, -2, -1, -1, -2], [0, 1, -2, -1, 0],
      [-2, -2, 1, -1, 1], [-2, -2, -1, 0, 0]], [[2, 0, 0, 0, 0]], [[0, 2, 0, 1, 0]], "反例1"),
    ([[1, 1, -2, 2, 1], [-1, 2, 2, -1, 2], [2, 1, 1, -2, -2],
      [1, 0, 2, 2, -2], [0, -1, 0, 0, -2]], [[1, 0, -1, -2, -2]], [[-1, -1, -1, 0, -1]], "反例2"),
    # P1 §VII 算例（已知 L_{a,b} 满足 (A)，q0=4）需 8x8，此处先用小例
]

for Am, Cm, L0m, tag in cases:
    A, C, L0 = toF(Am), toF(Cm), toF(L0m)
    Lx, eta, alpha = P1_construct(A, C, L0, verbose=True)
    q0 = sum(eta)
    print(f"  {tag}:")
    print(f"    构造的 L*: {len(Lx)} 行 (期望 q0={q0})")
    print(f"    rank(L*) = {rank_exact(Lx)}")
    print(f"    (A) 成立? {condA(A, C, Lx)}")
    for row in Lx:
        print(f"      {[str(x) for x in row]}")
    print()
