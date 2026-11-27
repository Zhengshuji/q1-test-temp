"""
独立穷举验证 k^min = dim Z - dim V（加前提 rank[L0;C]=p+r，C 行满秩）。

关键：不用任何构造，完全靠网格穷举得到真实最小值。
"""
import itertools

import numpy as np

TOL = 1e-7
rng = np.random.default_rng(555)


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


def condA(A, C, L):
    return in_span(L @ A, st(L, C, C @ A))


def orbit(M, A):
    n = A.shape[0]
    out, cur = [M], M
    for _ in range(n - 1):
        cur = cur @ A
        out.append(cur)
    return st(*out)


def formula(A, C, L0):
    Z = st(orbit(L0, A), orbit(C, A))
    V = st(L0, C, C @ A)
    return rk(Z) - rk(V)


def brute(A, C, L0, cap):
    """网格穷举；坐标基 + ±1 组合。cap 为上限。"""
    n = A.shape[1]
    pool = []
    # 用标准基 + 一些 ±1 向量作为候选池（比全网格小得多，但覆盖面好）
    for i in range(n):
        v = np.zeros(n)
        v[i] = 1.0
        pool.append(v)
    for v in itertools.product((-1, 0, 1), repeat=n):
        if any(v):
            pool.append(np.array(v, float))
    for k in range(0, cap + 1):
        for combo in itertools.combinations(range(len(pool)), k):
            R = np.array([pool[i] for i in combo]) if k else np.zeros((0, n))
            if condA(A, C, st(L0, R)):
                return k
    return None


ok = bad = skipped = 0
mismatches = []
for _ in range(400):
    n = 3
    p = int(rng.integers(0, n))
    q = int(rng.integers(1, n - p + 1)) if n - p >= 1 else 1
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float) if p > 0 else np.zeros((0, n))
    L0 = rng.integers(-2, 3, (q, n)).astype(float)

    if p > 0 and rk(C) < p:
        continue
    if rk(L0) < q:
        continue
    if rk(st(L0, C)) != p + q:      # 前提
        continue
    f = formula(A, C, L0)
    if f > 2 or f < 0:
        skipped += 1
        continue

    # 先快速判定 k=0
    if condA(A, C, L0):
        truth = 0
    else:
        truth = brute(A, C, L0, cap=f)
    if truth is None:
        skipped += 1
        continue
    if truth == f:
        ok += 1
    else:
        bad += 1
        mismatches.append((A, C, L0, f, truth))

print(f"  一致 {ok}，不一致 {bad}，跳过 {skipped}")
for A, C, L0, f, t in mismatches[:5]:
    print(f"   formula={f} brute={t}")
    print(f"     A={A.tolist()}")
    print(f"     C={C.tolist()}  L0={L0.tolist()}")
