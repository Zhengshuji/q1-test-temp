"""
用精确有理数算术重新核实 (S) 的等价刻画。

教训：数值 SVD 的秩判定在病态/临界情形会出错。
本脚本用 Fractions 做精确 RREF 与精确秩，重测：

  (S1)  rank[sL−LA; CA; C] == rank[L; CA; C] 对所有 s      <- (5b) 原文
  (S2)  rank[(sL−LA)N] ≡ rank[L N]  对所有 s                <- 等价改写
  (S3)  gcd_s(所有 h 阶子式) = 常数                          <- P1 Theorem 4
  (S4)  存在某个 h 阶子式不恒为零                             <- 我先前用的（可能错）
"""
import itertools
from fractions import Fraction as F

import numpy as np

rng = np.random.default_rng(20260106)


# ---------------- 精确有理数线性代数 ----------------
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


def nullspace_basis_exact(M):
    """行空间 M 的正交补的基（即 ker M 的基），用 [C;CA] 的零空间"""
    if not M:
        n = 0
    else:
        n = len(M[0])
    R, piv = rref(M)
    free = [c for c in range(n) if c not in piv]
    basis = []
    for fc in free:
        v = [F(0)] * n
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][fc]
        basis.append(v)
    return basis


def matmul(X, Y):
    if not X or not Y:
        return []
    n, k, m = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def matmul_vec(X, v):
    return [sum(X[i][j] * v[j] for j in range(len(v))) for i in range(len(X))]


def to_frac(M):
    return [[F(int(x)) for x in row] for row in M]


# ---------------- 判定 ----------------
def rank_5b_side(A, C, L, s):
    """rank[sL−LA; CA; C] 与 rank[L; CA; C]"""
    sF = F(s)
    left = []
    for i in range(len(L)):
        row = [sF * L[i][j] - sum(L[i][t] * A[t][j] for t in range(len(A))) for j in range(len(L[0]))]
        left.append(row)
    left = left + list(C) + list(matmul(C, A))
    right = list(L) + list(C) + list(matmul(C, A))
    return rank_exact(left), rank_exact(right)


def check_S1(A, C, L, pts):
    """(5b) 原文：所有 s 处秩相等"""
    base = rank_exact(list(L) + list(C) + list(matmul(C, A)))
    for s in pts:
        l, r = rank_5b_side(A, C, L, s)
        if l != r:
            return False, s
    return True, None


def poly_mat_P(A, C, L):
    """返回 P(s) = (sL−LA)N 的系数矩阵（关于 s 的一次多项式），以及 h=rank(LN)"""
    N = nullspace_basis_exact(list(C) + list(matmul(C, A)))
    if not N:
        return None, None, 0
    LN = matmul(L, N)                      # h 候选
    h = rank_exact(LN)
    LAN = matmul(matmul(L, A), N)
    # P(s) = s (L N) − (LA) N  -> 返回 (LN, LAN)
    return LN, LAN, h


def check_S3(A, C, L):
    """
    (S3)：gcd_s(所有 h 阶子式) 是否为常数。
    精确做法：求所有 h 阶子式的公共根集合是否为空。
    这里用一个小技巧：公共根 = 所有 h 阶子式的公共零点。
    等价地：P(s) 的秩处处为 h  <=>  对所有 s 秩 = h。
    用有理数 s 采样 + 对多项式做一次精确代数检查（此处用采样近似，但用精确秩）。
    """
    LN, LAN, h = poly_mat_P(A, C, L)
    if LN is None:
        return True, h                     # N 空 -> P ≡ 0 -> 自动成立
    if h == 0:
        return True, 0
    # 求所有 h 阶子式的公共根：用随机线性组合构成一个 h×h 子式，取其根
    # 更稳妥：直接检查 P(s) 秩是否处处 = h。用有理数 s 采样（精确秩）。
    import fractions
    pts = [F(x) for x in (-5, -2, -1, 0, 1, 2, 5)]
    # 加入 A 的特征值的候选（可能是有理数）：用迹/行列式启发，或直接取整数 s 扫描
    for s in pts:
        P = [[s * LN[i][j] - LAN[i][j] for j in range(len(LN[0]))] for i in range(len(LN))]
        if rank_exact(P) != h:
            return False, h, s
    return True, h, None


ok_s1 = bad_s1 = 0
incons_S1_S3 = 0
examples = []
for _ in range(120):
    n = int(rng.integers(2, 5))
    p = int(rng.integers(1, n))
    q = int(rng.integers(1, n))
    A = to_frac(rng.integers(-2, 3, (n, n)))
    C = to_frac(rng.integers(-2, 3, (p, n)))
    L = to_frac(rng.integers(-2, 3, (q, n)))
    if rank_exact(C) < p or rank_exact(L) < q:
        continue

    pts = [F(x) for x in (-3, -2, -1, 0, 1, 2, 3)]
    s1, wit = check_S1(A, C, L, pts)
    s3 = check_S3(A, C, L)
    s3_ok = s3[0]

    if s1 != s3_ok:
        incons_S1_S3 += 1
        if len(examples) < 3:
            examples.append((A, C, L, s1, s3_ok, wit, s3))

print(f"  (5b) 原文 与 (S3) gcd 判据 不一致次数: {incons_S1_S3} / 120")
for A, C, L, s1, s3, wit, s3full in examples:
    print(f"    (5b)={s1} (S3)={s3}   (5b)失败点 s={wit}   (S3) h={s3full[1]} 失败点={s3full[2] if len(s3full)>2 else None}")
    print(f"      A={A}")
    print(f"      C={C}")
    print(f"      L={L}")
print()
print("  说明：若不一致次数为 0，则 '(5b)' 与 'gcd 判据' 在精确算术下一致；")
print("        若 S1 为 False 而 S3 为 True（或反之），说明两者的采样点集合不同，")
print("        需要把采样点扩到所有可能的降秩点（A 的特征值、广义特征值）。")
