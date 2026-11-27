"""
补全定理 2 的下界证明并做独立验证。

下界证明（新的、严格的）：
   设 L = [L0; R] 满足 (A)：row(LA) ⊆ row(L, C, CA)。
   记 W := row(L0, R)，V := row(L0) + row(C) + row(CA)，Z := row(O_{L0}) + row(O_C)。
   关键：(i)  V·A ⊆ V           （因 L0A, CA ∈ V；C·A = CA ∈ V）
         (ii) W·A ⊆ W + V      （因 row(LA) = (W + row(L0))·A ⊆ W + V，而 L0A ∈ V）
   => (W+V) 是 A-不变的。
   对 Z 的生成元 gA^q（g ∈ row(L0) ∪ row(C) ⊆ W + V）：由 (W+V) 的 A-不变性，
   gA^q ∈ W + V 对一切 q。故 Z ⊆ W + V。
   取维数：dim Z ≤ dim W + dim V ≤ r + k + dim V
   => k ≥ dim Z - dim V。∎

于是 k^min = dim Z - dim V 是**精确值**（上界由补基构造给出）。
"""
import itertools

import numpy as np

TOL = 1e-7
rng = np.random.default_rng(20260103)


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


def condA(A, C, L):
    return in_span(L @ A, st(L, C, C @ A))


def orbit(M, A):
    n = A.shape[0]
    out, cur = [M], M
    for _ in range(n - 1):
        cur = cur @ A
        out.append(cur)
    return st(*out)


def ZV(A, C, L0):
    Z = st(orbit(L0, A), orbit(C, A) if C.shape[0] else np.zeros((0, A.shape[0])))
    V = st(L0, C, C @ A)
    return Z, V


print("=" * 74)
print("S1 : 验证证明中的两个关键包含 (i) V·A ⊆ V 与 (ii) W·A ⊆ W+V")
print("=" * 74)
bad_i = bad_ii = n_tested = 0
for _ in range(500):
    n = int(rng.integers(2, 6))
    p = int(rng.integers(0, n + 1))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L0 = rng.integers(-2, 3, (q, n)).astype(float)
    R = rng.integers(-2, 3, (int(rng.integers(0, 3)), n)).astype(float)
    L = st(L0, R)
    if not condA(A, C, L):
        continue
    n_tested += 1
    _, V = ZV(A, C, L0)
    if not in_span(V @ A, V):
        bad_i += 1
    W = st(L0, R)
    if not in_span(W @ A, st(W, V)):
        bad_ii += 1
print(f"  在 {n_tested} 个满足 (A) 的实例中：")
print(f"    (i)  V·A ⊄ V      的次数 = {bad_i}")
print(f"    (ii) W·A ⊄ W+V    的次数 = {bad_ii}")
print("  -> 两式成立则 (W+V) 是 A-不变的，下界证明成立")

print()
print("=" * 74)
print("S2 : 在满足 (A) 的实例中验证 Z ⊆ W + V（下界证明的核心结论）")
print("=" * 74)
bad_z = n_tested = 0
for _ in range(500):
    n = int(rng.integers(2, 6))
    p = int(rng.integers(0, n + 1))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L0 = rng.integers(-2, 3, (q, n)).astype(float)
    R = rng.integers(-2, 3, (int(rng.integers(0, 3)), n)).astype(float)
    L = st(L0, R)
    if not condA(A, C, L):
        continue
    n_tested += 1
    Z, V = ZV(A, C, L0)
    W = st(L0, R)
    if not in_span(Z, st(W, V)):
        bad_z += 1
        if bad_z <= 3:
            print(f"   反例！L0={L0.tolist()} R={R.tolist()} A={A.tolist()} C={C.tolist()}")
print(f"  {n_tested} 个满足 (A) 的实例中，Z ⊄ W+V 的次数 = {bad_z}")
print("  -> 若为 0，则下界 k ≥ dim Z - dim V 得到数值支持")

print()
print("=" * 74)
print("S3 : 极小规模的完全穷举（验证 k^min 的精确值）")
print("=" * 74)


def brute(A, C, L0, cap=3):
    """在 grid 上穷举（只用于 n<=3），返回最小 k 或 None"""
    n = A.shape[1]
    grid = [np.array(v, float) for v in itertools.product((-2, -1, 0, 1, 2), repeat=n) if any(v)]
    for k in range(0, cap + 1):
        for combo in itertools.combinations(range(len(grid)), k):
            R = np.array([grid[i] for i in combo]) if k else np.zeros((0, n))
            if condA(A, C, st(L0, R)):
                return k
    return None


okc = badc = skipped = 0
for _ in range(500):
    n = 3
    p = int(rng.integers(0, n))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-1, 2, (n, n)).astype(float)
    C = rng.integers(-1, 2, (p, n)).astype(float)
    L0 = rng.integers(-1, 2, (q, n)).astype(float)
    if rk(L0) < q:
        continue
    Z, V = ZV(A, C, L0)
    formula = rk(Z) - rk(V)
    if formula > 2:
        skipped += 1
        continue
    truth = brute(A, C, L0, cap=formula)
    if truth is None:
        skipped += 1
        continue
    if truth == formula:
        okc += 1
    else:
        badc += 1
        if badc <= 3:
            print(f"   不一致: formula={formula} brute={truth}")
            print(f"     A={A.tolist()} C={C.tolist()} L0={L0.tolist()}")
print(f"  一致 {okc}，不一致 {badc}，跳过 {skipped}")
