"""
决定性实验：命题 q 的困难是否来自连续参数 Θ？

思路（绕开 J/Θ 参数化，直接在 Grassmann 流形上搜）：
  取满足 H1–H4 的小例子，穷举所有 d 维子空间 L（用精确有理算术），
  记录最小的 d 使 (A)∧(S) 成立 —— 即 nu_min。

然后回答：
  (Q1) nu_min 是否等于 q0？（P1 说 q0 = sum eta_j）
  (Q2) 在 nu_min 维上，满足条件的 L 是"稀疏"还是"通有"？
       —— 若通有，则 Θ 不构成障碍（命题 q 可能为假）；
          若稀疏/孤立，则 Θ 构成实质障碍（困难来自连续部分）。

用 P1 的 Grasmann 视角：nu_min 维的最优 L 由 (J,Θ) 参数化，
所以"Θ 是否构成障碍" = "最优 L 的集合在 Gr 上是否是开集"。
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


def toF(M):
    return [[F(int(x)) for x in row] for row in M]


def condA(A, C, L):
    LA = mm(L, A)
    W = L + C + mm(C, A)
    return rank_exact(W + LA) == rank_exact(W)


def condS(A, C, L, s_cands):
    LA = mm(L, A)
    rhs = rank_exact(L + C + mm(C, A))
    n = len(A)
    for s in s_cands:
        sl = [[s * L[i][j] - LA[i][j] for j in range(n)] for i in range(len(L))]
        if rank_exact(sl + C + mm(C, A)) != rhs:
            return False
    return True


def cand_s(A, C, L):
    """候选降秩点：A 的特征值（整数/半整数扫描）+ 广义特征值的数值有理化 + 一批有理数"""
    c = set()
    for k in range(-12, 13):
        c.add(F(k)); c.add(F(k, 2)); c.add(F(k, 3)); c.add(F(k, 4))
    try:
        for ev in np.linalg.eigvals(np.array(A, float)):
            if abs(ev.imag) < 1e-7:
                c.add(F(float(ev.real)).limit_denominator(1000))
        Lf = np.array(L, float); LAf = Lf @ np.array(A, float)
        if Lf.shape[0] == Lf.shape[1] and abs(np.linalg.det(Lf)) > 1e-9:
            for ev in np.linalg.eigvals(np.linalg.solve(Lf, LAf)):
                if abs(ev.imag) < 1e-7:
                    c.add(F(float(ev.real)).limit_denominator(1000))
        else:
            from scipy.linalg import eig as geig
            for ev in geig(LAf, Lf, right=False):
                if abs(ev.imag) < 1e-7:
                    c.add(F(float(ev.real)).limit_denominator(1000))
    except Exception:
        pass
    return sorted(c)


def orbit(M, A):
    out, cur = [], M
    for _ in range(len(A)):
        out += cur
        cur = mm(cur, A)
    return out


# ---------------- 满足 H1-H4 的例子 ----------------
print("=" * 78)
print("例 1: A=[[1,1],[0,2]], C=[1,0], L0=[0,1]")
print("=" * 78)
A = toF([[1, 1], [0, 2]])
C = toF([[1, 0]])
L0 = toF([[0, 1]])
print(f"  rank(C)={rank_exact(C)}, rank(L0)={rank_exact(L0)}, "
      f"rank[L0;C]={rank_exact(L0 + C)}")
Z = orbit(L0, A) + orbit(C, A)
OC = orbit(C, A)
print(f"  Z 的秩 = {rank_exact(Z)},  row(O_C) 的秩 = {rank_exact(OC)}")
print(f"  H4 (功能可观 Z ⊆ row(O_C))? {rank_exact(Z + OC) == rank_exact(OC)}")
print()

n = 2
found = {}
for d in range(L0.__len__(), n + 1):
    hits = []
    I = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    pool = [row[:] for row in I] + [[F(v) for v in p]
                                    for p in itertools.product((-1, 0, 1), repeat=n) if any(p)]
    # 取 L = [L0; 额外 (d-r) 行]
    kr = d - len(L0)
    for combo in itertools.combinations(range(len(pool)), kr):
        L = L0 + [pool[i] for i in combo]
        if rank_exact(L) != d:
            continue
        if not condA(A, C, L):
            continue
        sc = cand_s(A, C, L)
        if condS(A, C, L, sc):
            hits.append(L)
    if hits:
        found[d] = hits
        print(f"  d = {d}: 找到 {len(hits)} 个满足 (A)∧(S) 的 L")
        break
    else:
        print(f"  d = {d}: 无解")

if found:
    dmin = min(found)
    print(f"\n  => nu_min = {dmin}")
    print(f"     q0 = ? (p1 说 q0 = sum eta_j)")

print()
print("=" * 78)
print("例 2: A=[[1,0],[0,2]], C=[1,1], L0=[1,-1]")
print("=" * 78)
A2 = toF([[1, 0], [0, 2]])
C2 = toF([[1, 1]])
L02 = toF([[1, -1]])
print(f"  rank(C)={rank_exact(C2)}, rank(L02)={rank_exact(L02)}, "
      f"rank[L0;C]={rank_exact(L02 + C2)}")
OC2 = orbit(C2, A2)
print(f"  row(O_C) 的秩 = {rank_exact(OC2)}")
Z2 = orbit(L02, A2) + OC2
print(f"  Z 的秩 = {rank_exact(Z2)}, H4? {rank_exact(Z2 + OC2) == rank_exact(OC2)}")
print()
for d in range(L02.__len__(), 3):
    hits = []
    I = [[F(1) if i == j else F(0) for j in range(2)] for i in range(2)]
    pool = [row[:] for row in I] + [[F(v) for v in p]
                                    for p in itertools.product((-1, 0, 1), repeat=2) if any(p)]
    kr = d - len(L02)
    for combo in itertools.combinations(range(len(pool)), kr):
        L = L02 + [pool[i] for i in combo]
        if rank_exact(L) != d:
            continue
        if not condA(A2, C2, L):
            continue
        sc = cand_s(A2, C2, L)
        if condS(A2, C2, L, sc):
            hits.append(L)
    if hits:
        print(f"  d = {d}: 找到 {len(hits)} 个满足 (A)∧(S) 的 L  -> nu_min = {d}")
        break
    else:
        print(f"  d = {d}: 无解")
