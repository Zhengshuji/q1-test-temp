"""调试 Q2 的失败案例：k 公式 > 0 但 R=0 已满足 (5a)"""
import itertools

import numpy as np

TOL = 1e-7
rng = np.random.default_rng(4242)


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
    n = A.shape[0]
    out, cur = [M], M
    for _ in range(n - 1):
        cur = cur @ A
        out.append(cur)
    return st(*out)


# 复现 trial 序列，找到第一个失败
trial_ok = 0
found = None
for trial in range(500):
    n = int(rng.integers(2, 6))
    p = int(rng.integers(0, n + 1))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L0 = rng.integers(-2, 3, (q, n)).astype(float)
    if rk(L0) < q:
        continue
    X = st(L0, C)
    Z = st(orbit(L0, A), orbit(C, A) if C.shape[0] else np.zeros((0, n)))
    k = rk(Z) - rk(X)
    if k >= 1 and cond5a(A, C, L0):
        found = (trial, n, p, q, A, C, L0, k, rk(X), rk(Z))
        break

if found is None:
    print("未复现（可能随机序列不同）")
else:
    trial, n, p, q, A, C, L0, k, rx, rz = found
    print(f"=== trial {trial}: n={n} p={p} q={q}, k公式={k}, dimX={rx}, dimZ={rz} ===")
    print("A =\n", A)
    print("C =\n", C)
    print("L0 =\n", L0)
    print("L0A =\n", L0 @ A)
    print()
    print("rank[L0;C;CA]           =", rk(st(L0, C, C @ A)))
    print("rank[L0;L0A;C;CA]       =", rk(st(L0, L0 @ A, C, C @ A)))
    print("(5a) with R=0           =", cond5a(A, C, L0))
    print("(A)  with R=0           =", condA(A, C, L0))
    print()
    print("row(L0A) 是否 ⊆ row(L0,C,CA) :", in_span(L0 @ A, st(L0, C, C @ A)))
    print("row(C) 的维数               :", rk(C) if C.shape[0] else 0)
    print("row(CA) 的维数              :", rk(C @ A) if C.shape[0] else 0)
    print()
    print("X = row(L0)+row(C) 是否 A-不变:", in_span(X @ A, X))
    print("Z 是否 A-不变                 :", in_span(Z @ A, Z))
    print("Z ⊇ X ?                       :", in_span(X, Z))
    print()
    # 关键：L0A 落在哪里
    print("L0A 的各行:")
    for i, row in enumerate(L0 @ A):
        print(f"   {row}  in row(L0,C,CA)={in_span(np.atleast_2d(row), st(L0,C,C@A))}"
              f"  in row(C,CA)={in_span(np.atleast_2d(row), st(C,C@A))}")
