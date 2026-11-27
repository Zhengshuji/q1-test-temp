"""
用精确有理数算术（fractions.Fraction）复验 04 的定理 2，排除浮点误差。

条件（修正后的 4 行块版本）：
   (5a)  rank[LA; L; CA; C] = rank[L; CA; C]
等价于
   (A)   row(LA) ⊆ row(L, C, CA)
"""
import itertools
from fractions import Fraction as F

rng = __import__("random").Random(20260103)


def mat(rows):
    return [[F(x) for x in r] for r in rows]


def shape(M):
    return (len(M), len(M[0]) if M else 0)


def rref(M):
    """返回 (行最简形, 主元列, 秩)，精确有理数"""
    M = [row[:] for row in M]
    if not M:
        return M, [], 0
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
    return M, piv, r


def rank(M):
    return rref(M)[2]


def stack(*Ms):
    Ms = [M for M in Ms if M and len(M) > 0]
    if not Ms:
        return []
    return [row for M in Ms for row in M]


def row_space_basis(M):
    """行空间的一组基（取自 rref 的非零行）"""
    R, _, rk = rref(M)
    return [R[i] for i in range(rk)]


def in_span(X, Y):
    """X 的每一行是否都在 Y 的行空间中（精确）"""
    if not X:
        return True
    return rank(stack(Y, X)) == rank(Y)


def zeros(r, c):
    return [[F(0)] * c for _ in range(r)]


def cond5a(A, C, L):
    return rank(stack(mm(L, A), L, mm(C, A), C)) == rank(stack(L, mm(C, A), C))


def condA(A, C, L):
    return in_span(mm(L, A), stack(L, C, mm(C, A)))


def mm(X, Y):
    if not X or not Y:
        return []
    n, k, m = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def rand_mat(r, c):
    return [[F(rng.randint(-3, 3)) for _ in range(c)] for _ in range(r)]


print("=" * 74)
print("P1 : 修正后的 (5a) <=> (A)   [精确算术]")
print("=" * 74)
bad = 0
for _ in range(600):
    n = rng.randint(2, 5)
    p = rng.randint(0, n)
    q = rng.randint(1, n)
    A, C, L = rand_mat(n, n), rand_mat(p, n), rand_mat(q, n)
    if cond5a(A, C, L) != condA(A, C, L):
        bad += 1
print(f"  不一致 {bad}/600 -> {'CONFIRMED' if bad==0 else 'FAILED'}")

print()
print("=" * 74)
print("P2 : 最小行数 = d1 - d0 ？")
print("=" * 74)


def k_formula(A, C, L0):
    return rank(stack(L0, mm(L0, A), C, mm(C, A))) - rank(stack(L0, C, mm(C, A)))


def build_R(A, C, L0):
    Q = stack(L0, C, mm(C, A))
    P = stack(L0, mm(L0, A), C, mm(C, A))
    BQ = row_space_basis(Q)
    BP = row_space_basis(P)
    cur, extra = [r[:] for r in BQ], []
    for v in BP:
        if rank(stack(cur, v)) > rank(cur):
            extra.append(v[:])
            cur = cur + [v[:]]
    return extra


fails = tested = 0
for trial in range(300):
    n = rng.randint(2, 5)
    p = rng.randint(0, n)
    q = rng.randint(1, n)
    A, C = rand_mat(n, n), rand_mat(p, n)
    L0 = rand_mat(q, n)
    if rank(L0) < q:
        continue
    tested += 1
    k = k_formula(A, C, L0)
    R = build_R(A, C, L0)
    if len(R) != k:
        fails += 1
        continue
    if not cond5a(A, C, stack(L0, R)):
        fails += 1
        if fails <= 5:
            print(f"   [t{trial}] 构造的 R 不满足 (5a)  (k={k})")
        continue
print(f"  测试 {tested}，失败 {fails} -> {'CONFIRMED' if fails==0 else 'FAILED'}")

print()
print("=" * 74)
print("P3 : R 为空时 (5a) 成立的充要条件")
print("=" * 74)
res = {"d1minuseq0_and_5a": 0, "d1minuseq0_but_not5a": 0, "5a_but_d1gt0": 0, "other": 0}
for _ in range(600):
    n = rng.randint(2, 5)
    p = rng.randint(0, n)
    q = rng.randint(1, n)
    A, C, L0 = rand_mat(n, n), rand_mat(p, n), rand_mat(q, n)
    k = k_formula(A, C, L0)
    ok = cond5a(A, C, L0)
    if k == 0 and ok:
        res["d1minuseq0_and_5a"] += 1
    elif k == 0 and not ok:
        res["d1minuseq0_but_not5a"] += 1
    elif k > 0 and ok:
        res["5a_but_d1gt0"] += 1
    else:
        res["other"] += 1
print("  ", res)
print("  若 '5a_but_d1gt0' > 0，说明 R=0 已经满足 (5a)，d1-d0 不是最小行数 → 定理 2 需修正")
