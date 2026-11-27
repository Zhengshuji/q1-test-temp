# -*- coding: utf-8 -*-
"""
最终构造：T 的前 r 列使 RNC·T_{:,i}=0；后 s 列（在 ker L0NC 内）使
RNC·T_{:,r+j} = e_j（即规范化出 pivot 1）。然后读出 Θ 并双重验证。
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
    n, k, m = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def toF(M):
    return [[F(int(x)) for x in row] for row in M]


def transpose(M):
    return [[M[i][j] for i in range(len(M))] for j in range(len(M[0]))]


def inv(M):
    n = len(M)
    R, piv = rref([M[i][:] + [F(1) if i == j else F(0) for j in range(n)] for i in range(n)])
    # 必须保证 pivot 都在前 n 列（否则 M 奇异）
    if len(piv) != n or any(p >= n for p in piv):
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


def solve_ls(Des, b):
    """解 Des·y = b（Des: m×k，b: m×1）；返回 (y, 零空间基) 或 None"""
    m, k = len(Des), len(Des[0])
    R, piv = rref([Des[i][:] + [b[i][0]] for i in range(m)])
    for row in R:
        if all(x == 0 for x in row[:k]) and row[k] != 0:
            return None
    y = [F(0)] * k
    for i, pc in enumerate(piv):
        if pc < k:
            y[pc] = R[i][k]
    ns = []
    free = [c for c in range(k) if c not in piv]
    for fc in free:
        v = [F(0)] * k
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            if pc < k:
                v[pc] = -R[i][fc]
        ns.append(v)
    return y, ns


def solve_coeff(target, basis_rows):
    if not basis_rows:
        return [] if all(x == 0 for x in target) else None
    m, k = len(target), len(basis_rows)
    Aug = [[basis_rows[i][j] for i in range(k)] + [target[j]] for j in range(m)]
    R, piv = rref(Aug)
    for row in R:
        if all(x == 0 for x in row[:k]) and row[k] != 0:
            return None
    phi = [F(0)] * k
    for i, pc in enumerate(piv):
        if pc < k:
            phi[pc] = R[i][k]
    return phi


def times(v, A, q):
    out = v[:]
    for _ in range(q):
        out = mm([out], A)[0]
    return out


def P1_construct(A, C, L0):
    n, p, r = len(A), len(C), len(L0)
    gens = [row[:] for row in C] + [row[:] for row in L0]
    ngen = p + r
    M, M_info, rejected = [], [], {}
    for q in range(n + 1):
        for i in range(ngen):
            if i in rejected:
                continue
            v = times(gens[i], A, q)
            if rank_exact(M + [v]) > rank_exact(M):
                M.append(v); M_info.append((i, q))
            else:
                rejected[i] = q
        if len(rejected) == ngen:
            break
    alpha = [rejected.get(i, n + 1) for i in range(ngen)]
    eta = [alpha[p + j] for j in range(r)]
    R_rows = []
    for j in range(r):
        i = p + j
        a_i = alpha[i]
        if a_i > n:
            continue
        Mminus, Minfo = [], []
        for (ii, qq), row in zip(M_info, M):
            if (qq < a_i) or (qq == a_i and ii < i):
                Mminus.append(row); Minfo.append((ii, qq))
        phi = solve_coeff(times(gens[i], A, a_i), Mminus)
        if phi is None:
            continue
        eta_j = eta[j]
        for t in range(1, eta_j):
            shift = eta_j - t
            row = times(gens[i], A, t)
            for q in range(shift + 1, eta_j + 1):
                for idx, (ii, qq) in enumerate(Minfo):
                    if qq != q or phi[idx] == 0:
                        continue
                    term = times(gens[ii], A, q - shift)
                    row = [row[k] - phi[idx] * term[k] for k in range(n)]
            R_rows.append(row)
    return toF(L0) + R_rows, eta, alpha


def condA(A, C, L):
    LA = mm(L, A)
    W = L + C + mm(C, A)
    return rank_exact(W + LA) == rank_exact(W)


Am = [[1, 0, 2, 0, -1], [-1, -2, -1, -1, -2], [0, 1, -2, -1, 0],
      [-2, -2, 1, -1, 1], [-2, -2, -1, 0, 0]]
Cm = [[2, 0, 0, 0, 0]]
L0m = [[0, 2, 0, 1, 0]]
A, C, L0 = toF(Am), toF(Cm), toF(L0m)
n, p, r = len(A), len(C), len(L0)
Lx, eta, alpha = P1_construct(A, C, L0)
R = Lx[len(L0):]
k = len(R)
NC = ker_cols(C)
dC = len(NC[0])
L0NC = mm(L0, NC)
RNC = mm(R, NC)
K = ker_cols(L0NC)
mK = len(K[0])
Krows = [[K[a][j] for a in range(dC)] for j in range(mK)]

print("=" * 80)
print(f"  eta={eta} q0={sum(eta)}  condA(P1解)={condA(A, C, Lx)}")
print(f"  d_C={dC}  k={k}  ker(L0NC) 维数={mK}")
print(f"  RNC = {[[str(x) for x in row] for row in RNC]}")

# T 的前 r 列
Tcols = []
for i in range(r):
    ei = [F(1) if q == i else F(0) for q in range(r)]
    sol = solve_ls([[L0NC[a][j] for j in range(dC)] for a in range(r)],
                   [[ei[a]] for a in range(r)])
    xi, _ = sol
    tgt = mm(RNC, [[xi[j]] for j in range(dC)])[0][0]
    rncK = [mm(RNC, [[Krows[j][a]] for a in range(dC)])[0][0] for j in range(mK)]
    c = [F(0)] * mK
    for j in range(mK):
        if rncK[j] != 0:
            c[j] = -tgt / rncK[j]
            break
    z = [sum(c[j] * Krows[j][a] for j in range(mK)) for a in range(dC)]
    Tcols.append([xi[a] + z[a] for a in range(dC)])

# T 的后 s 列：使 RNC·T_{:,r+j} = e_j（k 个方程）
s = dC - r
rncKmat = [[mm(RNC, [[Krows[j][a]] for a in range(dC)])[0][0]] for j in range(mK)]  # mK×1? 需 k×mK
# 重算：RNC 是 k×dC, Krows[j] 是 dC 向量 -> RNC·Krows[j] 是 k 向量
rncKmat = [[mm(RNC, [[Krows[j][a]] for a in range(dC)])[ii][0] for j in range(mK)]
           for ii in range(k)]                                    # k × mK
cols_ok = True
ns_cache = None
for j in range(s):
    if j < k:
        ej = [[F(1) if ii == j else F(0)] for ii in range(k)]
        sol = solve_ls(rncKmat, ej)
        if sol is None:
            cols_ok = False
            Tcols.append([F(0)] * dC)
            continue
        yj = sol[0]
    else:
        # 在 ker(L0NC) ∩ ker(RNC) 中取（RN_C·z = 0 的解空间基）
        if ns_cache is None:
            sol0 = solve_ls(rncKmat, [[F(0)] for _ in range(k)])
            ns_cache = sol0[1]
        idx = j - k
        if idx >= len(ns_cache):
            cols_ok = False
            Tcols.append([F(0)] * dC)
            continue
        yj = ns_cache[idx]
    Tcols.append([sum(yj[a] * Krows[a][jj] for a in range(mK)) for jj in range(dC)])
T = [[Tcols[j][i] for j in range(dC)] for i in range(dC)]
Tinv = inv(T)
print(f"  后 s 列可解? {cols_ok}")
print(f"  T 可逆? {Tinv is not None}")
if Tinv is not None:
    print(f"  L0NC·T = {[[str(x) for x in row] for row in mm(L0NC, T)]}")
    RNCT = mm(RNC, T)
    print(f"  RNC·T  = {[[str(x) for x in row] for row in RNCT]}")
    print(f"    => 期望 [0...0 | I_k | Theta]")
    if all(RNCT[i][q] == (F(1) if q == r + i else F(0))
           for i in range(k) for q in range(r + k)):
        print("    => 规范化成功！结构为 [0 | I_k | Θ]")
        Theta = [[RNCT[i][r + k + j] for j in range(s - k)] for i in range(k)]
        print(f"    => J = (0..{k-1}),  Θ = {[[str(x) for x in row] for row in Theta]}")
        # 双验证：condA 与三块公式
        MC = mm(inv(mm(transpose(NC), NC)), transpose(NC))
        Abar = mm(mm(MC, A), NC)
        BA = mm(mm(C, A), NC)
        AbarT = mm(mm(Tinv, Abar), T)
        BAT = mm(BA, T)
        WJ = [[F(1) if j == i else F(0) for j in range(dC)] for i in range(r)]
        for i in range(k):
            WJ.append([F(0)] * r + RNCT[i][r:])
        r3 = rank_exact(WJ + BAT + mm(WJ, AbarT)) == rank_exact(WJ + BAT)
        XJ = mm(WJ, Tinv)
        R2 = mm(XJ[r:], MC)
        Lx2 = toF(L0) + R2
        print(f"    三块公式 (A) = {r3}")
        print(f"    从参数化恢复的 L 的 condA = {condA(A, C, Lx2)}")

        # ---- 扫描 Omega*_{A,J} ----
        print()
        print("  === 扫描 Omega*_{A,J}（固定 T）===")
        import itertools
        for J in itertools.combinations(range(s), k):
            rest = [i for i in range(s) if i not in J]
            hits = []
            grid = [F(a, 2) for a in range(-24, 25)]
            for th in grid:
                YJ = [F(0)] * s
                for a2, jj in enumerate(J):
                    YJ[jj] = F(1) if a2 == 0 else th
                for pos in rest:
                    YJ[pos] = th
                WJx = [[F(1) if j == i else F(0) for j in range(dC)] for i in range(r)]
                WJx.append([F(0)] * r + YJ)
                if rank_exact(WJx + BAT + mm(WJx, AbarT)) == rank_exact(WJx + BAT):
                    hits.append(th)
            print(f"    J={J}: 命中 {len(hits)}/{len(grid)} 个 Θ 值")
            if 0 < len(hits) < len(grid):
                print(f"      => 解集是**真子集**（可能是曲线/孤立点）")
                print(f"      命中的 Θ: {[str(x) for x in hits][:12]}")
            elif len(hits) == len(grid):
                print(f"      => 解集是**全空间**（正维数，开集）")
            else:
                print(f"      => 在该网格上无解")


# ============ 追加：在规范化 T 坐标系下扫描 Omega* 的全部解 ============
print()
print("=== 在规范化 T 坐标系下扫描 Omega*（细网格，步长 1/12）===")
STEP = 12
vals = [F(t_, STEP) for t_ in range(-8 * STEP, 8 * STEP + 1)]
hits = []
for a in vals:
    for b in vals:
        YJ2 = [F(0)] * s
        YJ2[0] = F(1)
        if s > 1:
            YJ2[1] = a
        if s > 2:
            YJ2[2] = b
        for rest in range(3, s):
            YJ2[rest] = F(0)
        W2 = [[F(1) if jj == ii else F(0) for jj in range(dC)] for ii in range(r)]
        W2.append([F(0)] * r + YJ2)
        if rank_exact(W2 + BAT + mm(W2, AbarT)) == rank_exact(W2 + BAT):
            hits.append((a, b))
print(f"命中点数: {len(hits)}")
for h in hits[:20]:
    print(f"   Theta = ({h[0]}, {h[1]})")
if len(hits) > 20:
    print(f"   ... 共 {len(hits)} 个")