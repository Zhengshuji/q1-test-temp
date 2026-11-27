"""
量化 (5a) 与 (5a)+(5b) 的最小行数差距。

  k_{(5a)}        = dim Z - dim V            （定理 2，已证，多项式）
  k_{(5a)+(5b)}   = nu_min >= q_0 = k_{(5a)} （同时满足谱条件）

本脚本枚举小实例，分别计算：
  (i)  仅 (5a) 的最小 k
  (ii) 同时满足 (5a)(5b) 的最小 k
看二者是否真的会不同。
"""
import itertools

import numpy as np

TOL = 1e-7
rng = np.random.default_rng(8888)


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


def condS(A, C, L, npts=20):
    """严格 (S)：rank[sL-LA; CA; C] == rank[L; CA; C] for all s"""
    rhs = rk(st(L, C @ A, C))
    pts = [complex(x) for x in (-5., -2., -1., -0.5, 0., 0.5, 1., 2., 5.)]
    pts += [complex(c) for c in np.linalg.eigvals(A)]
    pts += [complex(rng.normal(), rng.normal()) for _ in range(npts)]
    for s in pts:
        lhs = rk(st((s * L - L @ A).real, C @ A, C))
        if lhs != rhs:
            return False
    return True


def orbit(M, A):
    n = A.shape[0]
    out, cur = [M], M
    for _ in range(n - 1):
        cur = cur @ A
        out.append(cur)
    return st(*out)


def k5a(A, C, L0):
    Z = st(orbit(L0, A), orbit(C, A) if C.shape[0] else np.zeros((0, A.shape[0])))
    V = st(L0, C, C @ A)
    return rk(Z) - rk(V)


def k_both(A, C, L0, cap=4):
    """穷举求同时满足 (5a)(5b) 的最小 k"""
    n = A.shape[1]
    pool = []
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
            L = st(L0, R)
            if condA(A, C, L) and condS(A, C, L):
                return k
    return None


print("=" * 74)
print("比较 k_{(5a)} 与 k_{(5a)+(5b)}")
print("=" * 74)
diff = same = none = 0
examples = []
for _ in range(600):
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
    if rk(st(L0, C)) != p + q:
        continue
    k1 = k5a(A, C, L0)
    if k1 > 2:
        continue
    k2 = k_both(A, C, L0, cap=min(3, n))
    if k2 is None:
        none += 1
        continue
    if k2 == k1:
        same += 1
    else:
        diff += 1
        if len(examples) < 4:
            examples.append((A.copy(), C.copy(), L0.copy(), k1, k2))

print(f"  相同: {same}   不同: {diff}   穷举未找到(>cap): {none}")
print()
for A, C, L0, k1, k2 in examples:
    print(f"  k_(5a)={k1}  k_(5a)+(5b)={k2}")
    print(f"    A={A.tolist()}")
    print(f"    C={C.tolist()}  L0={L0.tolist()}")
print()
print("  若 '不同' > 0，说明 (5b) 确实会把最小行数抬高，")
print("  即我的定理 2 (只覆盖 (5a)) 不足以回答 q.txt 的问题。")
