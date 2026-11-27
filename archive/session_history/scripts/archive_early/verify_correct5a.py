"""
用【修正后的 (5a)】(4 行块版本) 验证 04 的定理 2。
同时验证引理 1：(5a) <=> row(LA) subset row(L,C,CA)。
"""
import itertools

import numpy as np

rng = np.random.default_rng(20260102)
TOL = 1e-7


def _r(M):
    return np.atleast_2d(np.asarray(M, dtype=float).real)


def rank(M):
    M = _r(M)
    if M.size == 0 or M.shape[0] == 0:
        return 0
    s = np.linalg.svd(M, compute_uv=False)
    return 0 if s.size == 0 else int(np.sum(s > TOL * max(M.shape) * (s[0] if s[0] > 0 else 1.0)))


def stack(*b):
    b = [_r(x) for x in b]
    nc = max((x.shape[1] for x in b), default=0)
    b = [x for x in b if x.shape[0] > 0]
    return np.zeros((0, nc)) if not b else np.vstack(b)


def in_span(X, Y):
    X, Y = _r(X), _r(Y)
    return True if X.shape[0] == 0 else rank(stack(Y, X)) == rank(Y)


# ---------------- 修正后的条件 ----------------
def cond5a_correct(A, C, L):
    """正确版本：左端 4 块 [LA; L; CA; C]，右端 3 块 [L; CA; C]"""
    return rank(stack(L @ A, L, C @ A, C)) == rank(stack(L, C @ A, C))


def cond5a_wrong(A, C, L):
    """旧错误版本：左端 3 块 [LA; CA; C]，右端 3 块 [CA; C; L]"""
    return rank(stack(L @ A, C @ A, C)) == rank(stack(C @ A, C, L))


def cond_contain(A, C, L):
    return in_span(L @ A, stack(L, C, C @ A))


print("=" * 76)
print("V1 : 修正后的 (5a)  <=>  row(LA) subset row(L,C,CA)   (引理 1)")
print("=" * 76)
bad = 0
for _ in range(1500):
    n = int(rng.integers(2, 6))
    p = int(rng.integers(0, n + 1))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L = rng.integers(-2, 3, (q, n)).astype(float)
    if cond5a_correct(A, C, L) != cond_contain(A, C, L):
        bad += 1
print(f"  不一致 {bad}/1500  ->  {'CONFIRMED' if bad == 0 else 'FAILED'}")

print()
print("=" * 76)
print("V2 : 旧版本(3 块) 与包含关系不等价（说明修正的必要性）")
print("=" * 76)
bad2 = 0
for _ in range(1500):
    n = int(rng.integers(2, 6))
    p = int(rng.integers(0, n + 1))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L = rng.integers(-2, 3, (q, n)).astype(float)
    if cond5a_wrong(A, C, L) != cond_contain(A, C, L):
        bad2 += 1
print(f"  不一致 {bad2}/1500  ->  旧版本确实不等价（修正必要）")

print()
print("=" * 76)
print("V3 : 定理 2  ——  min k = d1 - d0 = rank[L0;L0A;C;CA] - rank[L0;C;CA]")
print("=" * 76)


def k_formula(A, C, L0):
    d0 = rank(stack(L0, C, C @ A))
    d1 = rank(stack(L0, L0 @ A, C, C @ A))
    return d1 - d0


def build_R(A, C, L0):
    Q, P = stack(L0, C, C @ A), stack(L0, L0 @ A, C, C @ A)
    BQ = np.linalg.svd(Q, full_matrices=False)[2][: rank(Q)] if Q.shape[0] else np.zeros((0, A.shape[0]))
    BP = np.linalg.svd(P, full_matrices=False)[2][: rank(P)] if P.shape[0] else np.zeros((0, A.shape[0]))
    cur, extra = BQ.copy(), []
    for v in BP:
        if rank(stack(cur, v)) > rank(cur):
            extra.append(v)
            cur = np.vstack([cur, v])
    return np.array(extra) if extra else np.zeros((0, A.shape[0]))


fails = tested = 0
for trial in range(400):
    n = int(rng.integers(2, 6))
    p = int(rng.integers(0, n + 1))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L0 = rng.integers(-2, 3, (q, n)).astype(float)
    if rank(L0) < q:
        continue
    tested += 1
    k = k_formula(A, C, L0)
    R = build_R(A, C, L0)
    if R.shape[0] != k:
        fails += 1
        print(f"   [t{trial}] 构造 {R.shape[0]} 行 != 公式 {k}")
        continue
    if not cond5a_correct(A, C, stack(L0, R)):
        fails += 1
        print(f"   [t{trial}] 构造的 R 不满足修正后的 (5a)")
        continue
    # 最优性：穷举更少行数
    if n <= 3 and k >= 1:
        grid = [np.array(v, float) for v in itertools.product(range(-2, 3), repeat=n) if any(v)]
        smaller = any(
            cond5a_correct(A, C, stack(L0, np.array([grid[i] for i in c]) if c else np.zeros((0, n))))
            for kk in range(0, k)
            for c in itertools.combinations_with_replacement(range(len(grid)), kk)
        )
        if smaller:
            fails += 1
            print(f"   [t{trial}] 存在行数少于 {k} 的解")
print(f"  测试 {tested}，失败 {fails}  ->  {'CONFIRMED' if fails == 0 else 'FAILED'}")

print()
print("=" * 76)
print("V4 : 一个具体例子（04 §2 推论）")
print("=" * 76)
A = np.array([[0.0, 1.0], [0.0, 0.0]])
C = np.zeros((0, 2))
L0 = np.array([[0.0, 1.0]])
print("  A=[[0,1],[0,0]], C=[] , L0=[e2]")
print(f"  d0 = rank[L0;C;CA]        = {rank(stack(L0, C, C@A))}")
print(f"  d1 = rank[L0;L0A;C;CA]    = {rank(stack(L0, L0@A, C, C@A))}")
print(f"  最小 k = {k_formula(A, C, L0)}   （需要 R=[e1]）")
R = np.array([[1.0, 0.0]])
print(f"  取 R=[e1] 后 (5a) = {cond5a_correct(A, C, stack(L0, R))}")
print(f"  取 R=[]   后 (5a) = {cond5a_correct(A, C, L0)}")
