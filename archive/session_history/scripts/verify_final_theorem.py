"""
最终正确的定理 2。

(A)  row(LA) ⊆ row(L, C, CA)

定义：
   Z  := row(O_{L0}) + row(O_C)        （A-不变的能达行空间，包含所有可能的 L 行）
   U  := row(L0) + row(C) + row(CA)    （条件 (A) 右端在 R=0 时的部分）

命题：
   (i)  R=0 满足 (A)  <=>  row(L0A) ⊆ U
   (ii) 一般地，最小行数 k = dim Z − dim( Z ∩ ( row(L0) + row(C) + row(CA) ) )
        等价地 k = dim( Z + U ) − dim(U)  ... 需验证
   (iii) R 的构造：取 Z 中 (Z∩(row(L0)+row(C)+row(CA))) 的补基
"""
import itertools

import numpy as np

TOL = 1e-7
rng = np.random.default_rng(777)


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


def basis(M):
    M = np.atleast_2d(np.asarray(M, float))
    if M.shape[0] == 0:
        return np.zeros((0, M.shape[1]))
    return np.linalg.svd(M, full_matrices=False)[2][: rk(M)]


def in_span(X, Y):
    X = np.atleast_2d(np.asarray(X, float))
    return True if X.shape[0] == 0 else rk(st(Y, X)) == rk(Y)


def intersect_basis(A1, A2):
    """row(A1) ∩ row(A2) 的基"""
    B1, B2 = basis(A1), basis(A2)
    if B1.shape[0] == 0 or B2.shape[0] == 0:
        return np.zeros((0, A1.shape[1]))
    # 求 {x : x = a B1 = b B2} ；用零空间法
    k1, k2 = B1.shape[0], B2.shape[0]
    M = np.hstack([B1.T, -B2.T])          # (n, k1+k2)
    # 求 M z = 0 的解空间
    u, s, vt = np.linalg.svd(M)
    ns = vt[s.shape[0]:] if False else vt[np.sum(s > 1e-9):]
    return (ns[:, :k1] @ B1) if ns.shape[0] else np.zeros((0, A1.shape[1]))


def cond5a(A, C, L):
    return rk(st(L @ A, L, C @ A, C)) == rk(st(L, C @ A, C))


def condA(A, C, L):
    return in_span(L @ A, st(L, C, C @ A))


def orbit(M, A):
    n = A.shape[0]
    out, cur = [M], M
    for _ in range(n - 1):
        cur = cur @ A
        out.append(cur)
    return st(*out)


def spaces(A, C, L0):
    Z = st(orbit(L0, A), orbit(C, A) if C.shape[0] else np.zeros((0, A.shape[0])))
    V = st(L0, C, C @ A)                       # row(L0)+row(C)+row(CA)
    return Z, V


def k_theory(A, C, L0):
    Z, V = spaces(A, C, L0)
    inter = intersect_basis(Z, V)
    return rk(Z) - rk(inter), Z, V, inter


def build_R(A, C, L0):
    k, Z, V, inter = k_theory(A, C, L0)
    BZ, BI = basis(Z), basis(inter)
    cur, extra = BI.copy(), []
    for v in BZ:
        if rk(st(cur, v)) > rk(cur):
            extra.append(v)
            cur = np.vstack([cur, v])
    return np.array(extra) if extra else np.zeros((0, A.shape[0]))


print("=" * 74)
print("T1 : R=0 满足 (A)  <=>  row(L0A) ⊆ row(L0,C,CA)")
print("=" * 74)
bad = 0
for _ in range(800):
    n = int(rng.integers(2, 6))
    p = int(rng.integers(0, n + 1))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L0 = rng.integers(-2, 3, (q, n)).astype(float)
    lhs = condA(A, C, L0)
    rhs = in_span(L0 @ A, st(L0, C, C @ A))
    if lhs != rhs:
        bad += 1
print(f"  不一致 {bad}/800 -> {'CONFIRMED' if bad == 0 else 'FAILED'}")

print()
print("=" * 74)
print("T2 : 最小行数 = dim Z - dim(Z ∩ row(L0,C,CA))")
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
    k, Z, V, inter = k_theory(A, C, L0)
    R = build_R(A, C, L0)
    if R.shape[0] != k:
        fails += 1
        print(f"   [t{trial}] 构造 {R.shape[0]} != 公式 {k}")
        continue
    if not cond5a(A, C, st(L0, R)):
        fails += 1
        print(f"   [t{trial}] R 不满足 (5a)  (k={k})")
        continue
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
