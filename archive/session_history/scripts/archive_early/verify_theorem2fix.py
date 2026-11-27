"""
修正后的定理 2 验证（精确有理数 + 浮点双路）。

修正后的 (5a)   <=>  (A)  row(LA) ⊆ row(L, C, CA)

定理 2'（修正版）：
   最小 k  =  dim Z − dim X
   其中  X := row(L0) + row(C)
         Z := row(O_{L0}) + row(O_C)      （L0 与 C 在 A 下生成的能达行空间）
   且 Z 是 A-不变的。

构造：取 R 的行 = Z 中 X 的一个补基。
"""
import itertools

import numpy as np

TOL = 1e-7


def rk(M):
    M = np.atleast_2d(np.asarray(M, float))
    if M.size == 0 or M.shape[0] == 0:
        return 0
    s = np.linalg.svd(M, compute_uv=False)
    return 0 if s.size == 0 else int(np.sum(s > TOL * max(M.shape) * (s[0] if s[0] > 0 else 1.0)))


def st(*b):
    b = [np.atleast_2d(np.asarray(x, float)) for x in b]
    nc = max((x.shape[1] for x in b), default=0)
    b = [x for x in b if x.shape[0] > 0]
    return np.zeros((0, nc)) if not b else np.vstack(b)


def in_span(X, Y):
    X = np.atleast_2d(np.asarray(X, float))
    return True if X.shape[0] == 0 else rk(st(Y, X)) == rk(Y)


def cond5a(A, C, L):
    return rk(st(L @ A, L, C @ A, C)) == rk(st(L, C @ A, C))


def condA(A, C, L):
    return in_span(L @ A, st(L, C, C @ A))


def orbit(M, A):
    """O_M = [M; MA; ...; MA^{n-1}]"""
    n = A.shape[0]
    out, cur = [M], M
    for _ in range(n - 1):
        cur = cur @ A
        out.append(cur)
    return st(*out)


def k_theory(A, C, L0):
    X = st(L0, C)
    Z = st(orbit(L0, A), orbit(C, A) if C.shape[0] else np.zeros((0, A.shape[0])))
    return rk(Z) - rk(X)


def build_R(A, C, L0):
    """R 的行 = Z 中 X 的补基（Z 是 A-不变子空间）"""
    X = st(L0, C)
    Z = st(orbit(L0, A), orbit(C, A) if C.shape[0] else np.zeros((0, A.shape[0])))
    BX = np.linalg.svd(X, full_matrices=False)[2][: rk(X)] if X.shape[0] else np.zeros((0, A.shape[0]))
    BZ = np.linalg.svd(Z, full_matrices=False)[2][: rk(Z)] if Z.shape[0] else np.zeros((0, A.shape[0]))
    cur, extra = BX.copy(), []
    for v in BZ:
        if rk(st(cur, v)) > rk(cur):
            extra.append(v)
            cur = np.vstack([cur, v])
    return np.array(extra) if extra else np.zeros((0, A.shape[0]))


rng = np.random.default_rng(4242)

print("=" * 74)
print("Q1 : 修正后 (5a) <=> (A)")
print("=" * 74)
bad = 0
for _ in range(800):
    n = int(rng.integers(2, 6))
    p = int(rng.integers(0, n + 1))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L = rng.integers(-2, 3, (q, n)).astype(float)
    if cond5a(A, C, L) != condA(A, C, L):
        bad += 1
print(f"  不一致 {bad}/800 -> {'CONFIRMED' if bad == 0 else 'FAILED'}")

print()
print("=" * 74)
print("Q2 : 最小行数 = dim Z - dim X   （构造 + 最优性）")
print("=" * 74)
fails = tested = 0
for trial in range(500):
    n = int(rng.integers(2, 6))
    p = int(rng.integers(0, n + 1))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L0 = rng.integers(-2, 3, (q, n)).astype(float)
    if rk(L0) < q:
        continue
    tested += 1
    k = k_theory(A, C, L0)
    R = build_R(A, C, L0)
    if R.shape[0] != k:
        fails += 1
        print(f"   [t{trial}] 构造 {R.shape[0]} != 理论 {k}")
        continue
    if not cond5a(A, C, st(L0, R)):
        fails += 1
        print(f"   [t{trial}] 构造的 R 不满足 (5a)")
        continue
    # 最优性：穷举
    if n <= 3 and k >= 1:
        grid = [np.array(v, float) for v in itertools.product(range(-2, 3), repeat=n) if any(v)]
        smaller = any(
            cond5a(A, C, st(L0, np.array([grid[i] for i in c]) if c else np.zeros((0, n))))
            for kk in range(0, k)
            for c in itertools.combinations_with_replacement(range(len(grid)), kk)
        )
        if smaller:
            fails += 1
            print(f"   [t{trial}] 存在少于 {k} 行的解")
print(f"  测试 {tested}，失败 {fails} -> {'CONFIRMED' if fails == 0 else 'FAILED'}")

print()
print("=" * 74)
print("Q3 : Z 的 A-不变性验证")
print("=" * 74)
bad = 0
for _ in range(300):
    n = int(rng.integers(2, 6))
    p = int(rng.integers(0, n + 1))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L0 = rng.integers(-2, 3, (q, n)).astype(float)
    Z = st(orbit(L0, A), orbit(C, A) if C.shape[0] else np.zeros((0, n)))
    if not in_span(Z @ A, Z):
        bad += 1
print(f"  Z·A ⊄ Z 的次数 {bad}/300 -> {'CONFIRMED Z 是 A-不变的' if bad == 0 else 'FAILED'}")

print()
print("=" * 74)
print("Q4 : 具体例子")
print("=" * 74)
A = np.array([[0.0, 1.0], [0.0, 0.0]])
C = np.zeros((0, 2))
L0 = np.array([[0.0, 1.0]])
Z = st(orbit(L0, A), np.zeros((0, 2)))
X = st(L0, C)
print("  A=[[0,1],[0,0]], C=[] , L0=[e2]")
print(f"  X = row(L0)+row(C)  的维数 = {rk(X)}")
print(f"  Z = row(O_L0)+row(O_C) 的维数 = {rk(Z)}")
print(f"  最小 k = {k_theory(A, C, L0)}")
print(f"  取 R=[] 时 (5a) = {cond5a(A, C, L0)}   <-- 应为 True（这是与旧版的关键差别）")
