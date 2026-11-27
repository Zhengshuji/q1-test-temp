"""
修正后的结构分析。

【被否证的引理 K】k=1 ⟹ (S) 必然失败。  —— 错！40/40 次 (S) 成立。

【修正方向】k=1 时 (S) 似乎**自动成立**（而不是失败）。

理由（新的推导）：
  k=1 时，N_{CA} 的像与 R 的相对位置使得 H = L·N_{CA} 的结构特殊。
  由 L5：rank(H) = dim R − dim(R ∩ row(C))。
  k=1 时若 R ∩ row(C) = 0，则 rank(H) = 1 = dim R（R 是 1 维！）
  => H 是 1×d' 的**行满秩**矩阵
  => P(s) = (s − T_R)·H  （T_R 是 1×1 标量）
  => rank P(s) = rank(H) 对**所有** s（因 H 的行空间固定，标量乘法不降秩）
  => (S) 自动成立！

  【关键】我此前错误地以为 "ker(sI−T_R) = R^1"，这是对的；
  但 P(s) = (s−T_R)·H 是**标量乘矩阵**，不是矩阵乘向量——
  标量乘法不改变秩（除非标量为 0，而 s=T_R 时 P=0！）。

  等等，s = T_R 时 P(T_R) = 0，rank = 0 ≠ rank(H)。
  除非 T_R 不是实数/eigenvalue 不在采样范围内……

  这条推理仍有问题。让me直接计算。

本脚本：直接计算 k=1 实例的 T_R、H、P(s)，看清结构。
"""
import itertools
from fractions import Fraction as F

import numpy as np

rng = np.random.default_rng(20260112)


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


# 用手工构造的 k=1 实例直接审视结构
print("=" * 78)
print("直接计算 k=1 实例的 T_R, H, P(s) 结构")
print("=" * 78)

# 取一个简单的 k=1 例子
Am = [[1, 0], [0, 2]]
Cm = [[1, 0]]
L0m = [[0, 1]]
A, C, L0 = toF(Am), toF(Cm), toF(L0m)

print(f"  A={Am}, C={Cm}, L0={L0m}")
NCA = nullspace_exact(C + mm(C, A))
print(f"  N_CA 的基 (dim={len(NCA)}): {[[str(x) for x in v] for v in NCA]}")

# k=1 的 L: 取 L0 加一行
for extra in ([F(1), F(0)], [F(1), F(1)], [F(0), F(1)]):
    L = L0 + [extra]
    if rank_exact(L) != 2:
        continue
    LA = mm(L, A)
    H = mm(L, NCA) if NCA else []
    print(f"\n  L = {[[str(x) for x in r] for r in L]}")
    print(f"    LA = {[[str(x) for x in r] for r in LA]}")
    if NCA:
        Hm = [[sum(L[i][t] * NCA[j][t] for t in range(len(A))) for j in range(len(NCA))]
              for i in range(len(L))]
        print(f"    H = L·N_CA = {[[str(x) for x in r] for r in Hm]}   rank(H) = {rank_exact(Hm)}")
        print(f"      dim(L∩row(C)) 需要单独算")
        # (S) 检验
        rhs = rank_exact(L + C + mm(C, A))
        fails = []
        for s in [F(k, 2) for k in range(-12, 13)]:
            sl = [[s * L[i][j] - LA[i][j] for j in range(len(A))] for i in range(len(L))]
            if rank_exact(sl + C + mm(C, A)) != rhs:
                fails.append(s)
        print(f"    (S) 失败点: {fails if fails else '无'}")
    else:
        print("    N_CA = 0 => H = 0 => (S) 自动成立")

print()
print("=" * 78)
print("关键：N_CA = 0 的情形")
print("=" * 78)
print("""  上面 A=diag(1,2), C=[1,0] 时：
    C = [1,0], CA = [1,0]，故 [C;CA] 的秩 = 1，N_CA 的维数 = 1。
  所以 N_CA != 0。

  但若 [C;CA] 足够"大"（秩 = n），则 N_CA = 0，于是 H = 0，P(s) = 0，
  (S) 自动成立！

  => **简化条件**：若 rank[C;CA] = n（即 (A,C) 的首次可观性充分），
     则对**任意** R，(S) 都成立，此时 nu_min = q0 且问题平凡。
""")

# 验证这个简化条件
print("=" * 78)
print("验证：rank[C;CA] = n 时，(S) 是否总成立？")
print("=" * 78)
ok = bad = 0
for trial in range(200):
    n = int(rng.integers(2, 5))
    p = int(rng.integers(1, n + 1))
    Am2 = rng.integers(-2, 3, (n, n))
    Cm2 = rng.integers(-2, 3, (p, n))
    A2, C2 = toF(Am2), toF(Cm2)
    if rank_exact(C2) != p:
        continue
    if rank_exact(C2 + mm(C2, A2)) != n:
        continue                       # 只取 rank[C;CA]=n
    # 任取 L
    r2 = int(rng.integers(1, n + 1))
    L0_2 = toF(rng.integers(-2, 3, (r2, n)))
    if rank_exact(L0_2) != r2:
        continue
    L2 = toF(rng.integers(-2, 3, (int(rng.integers(1, 3)), n)))
    if rank_exact(L2) != len(L2):
        continue
    # (S) 检验
    LA2 = mm(L2, A2)
    rhs = rank_exact(L2 + C2 + mm(C2, A2))
    fails = False
    for s in [F(k, 2) for k in range(-10, 11)]:
        sl = [[s * L2[i][j] - LA2[i][j] for j in range(n)] for i in range(len(L2))]
        if rank_exact(sl + C2 + mm(C2, A2)) != rhs:
            fails = True
            break
    if fails:
        bad += 1
    else:
        ok += 1
print(f"  rank[C;CA]=n 的实例中: (S) 成立 {ok} 次, 失败 {bad} 次")
if bad == 0:
    print("  => 简化条件确认：rank[C;CA]=n ⟹ (S) 对任意 L 自动成立")
    print("     => nu_min = q0 且问题在 P 中（此时 N_CA=0, H=0, P(s)=0）")
else:
    print(f"  => 有 {bad} 次失败，简化条件不成立")
