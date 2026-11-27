"""
关键实验：判断 hardness 能否来自 (5b)。

设 R 与 R' 满足 row(R') = row(R)（同一行空间，不同矩阵表示）。
问题：是否存在实例使得
    L  = [L0; R]  满足 (5a)∧(5b)
    L' = [L0; R'] 满足 (5a) 但**不**满足 (5b)？

若"是" => (5b) 依赖 L 的**具体行**（"谱刚性"），
           则"从候选族里挑子集"可能真的产生组合结构
           => 这是 hardness 的唯一可能来源。
若"否" => (5b) 只依赖行空间 => 问题可能整体是多项式的。
"""
import itertools

import numpy as np

TOL = 1e-7
rng = np.random.default_rng(4321)


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


def condS(A, C, L, npts=15):
    rhs = rk(st(L, C @ A, C))
    pts = [complex(x) for x in (-4., -2., -1., -0.5, 0., 0.5, 1., 2., 4.)]
    pts += [complex(c) for c in np.linalg.eigvals(A)]
    pts += [complex(rng.normal(), rng.normal()) for _ in range(npts)]
    return all(rk(st((s * L - L @ A).real, C @ A, C)) == rhs for s in pts)


print("=" * 74)
print("实验 A：同一行空间、不同表示，是否会有 (5b) 的差异？")
print("=" * 74)

found = []
for trial in range(400):
    n = 3
    p = int(rng.integers(1, n))
    q = int(rng.integers(1, n))
    A = rng.integers(-3, 4, (n, n)).astype(float)
    C = rng.integers(-3, 4, (p, n)).astype(float)
    L0 = rng.integers(-3, 4, (q, n)).astype(float)
    if rk(C) < p or rk(L0) < q or rk(st(L0, C)) != p + q:
        continue

    # 找一组候选 R：随机 k×n，k=1..2
    for k in (1, 2):
        Rs = rng.integers(-3, 4, (k, n)).astype(float)
        L = st(L0, Rs)
        if not (condA(A, C, L) and condS(A, C, L)):
            continue
        # 用同一行空间的另一组基：左乘随机可逆矩阵
        for _ in range(30):
            T = rng.integers(-3, 4, (k, k)).astype(float)
            if abs(np.linalg.det(T)) < 1e-6:
                continue
            Rs2 = T @ Rs
            if not np.allclose(Rs2, Rs):
                if not in_span(Rs2, Rs):
                    continue           # 应保证同一行空间
                L2 = st(L0, Rs2)
                a2, s2 = condA(A, C, L2), condS(A, C, L2)
                if a2 and not s2:
                    found.append((A.copy(), C.copy(), L0.copy(), Rs.copy(), Rs2.copy()))
                    break
        if found:
            break
    if len(found) >= 3:
        break

print(f"  找到 '同一行空间、(A) 都成立、但 (5b) 一真一假' 的实例: {len(found)} 个")
if found:
    print("  => (5b) **确实依赖 L 的具体行**（谱刚性成立）")
    A, C, L0, R1, R2 = found[0]
    print("\n  实例：")
    print("   A  =", A.tolist())
    print("   C  =", C.tolist())
    print("   L0 =", L0.tolist())
    print("   R1 =", R1.tolist(), " (5b) =", condS(A, C, st(L0, R1)))
    print("   R2 =", R2.tolist(), " (5b) =", condS(A, C, st(L0, R2)))
    print("   row(R1) == row(R2) ?", in_span(R1, R2) and in_span(R2, R1))
else:
    print("  未找到 => 在此规模下 (5b) 只依赖行空间")

print()
print("=" * 74)
print("实验 B：候选族受限时，最小 k 是否严格大于无约束的 k？")
print("=" * 74)
print("  （若'严格大于'普遍出现，说明候选族约束真的起作用）")

diff = same = 0
for trial in range(200):
    n = 3
    p = int(rng.integers(1, n))
    A = rng.integers(-3, 4, (n, n)).astype(float)
    C = rng.integers(-3, 4, (p, n)).astype(float)
    L0 = rng.integers(-3, 4, (int(rng.integers(1, n - p + 1)), n)).astype(float) \
        if n - p >= 1 else rng.integers(-3, 4, (1, n)).astype(float)
    if rk(C) < p or rk(L0) < L0.shape[0] or rk(st(L0, C)) != p + L0.shape[0]:
        continue

    # 无约束：穷举自然基 + 组合
    pool = [np.array(v, float) for v in itertools.product((-1, 0, 1), repeat=n) if any(v)]
    ku = None
    for k in range(0, 3):
        for combo in itertools.combinations(range(len(pool)), k):
            R = np.array([pool[i] for i in combo]) if k else np.zeros((0, n))
            L = st(L0, R)
            if condA(A, C, L) and condS(A, C, L):
                ku = k
                break
        if ku is not None:
            break
    if ku is None:
        continue

    # 候选族受限：只用自然基 e_i
    cand = [np.eye(n)[i] for i in range(n)] + [np.sum(np.eye(n), axis=0)]
    kr = None
    for k in range(0, 3):
        for combo in itertools.combinations(range(len(cand)), k):
            R = np.array([cand[i] for i in combo]) if k else np.zeros((0, n))
            L = st(L0, R)
            if condA(A, C, L) and condS(A, C, L):
                kr = k
                break
        if kr is not None:
            break
    if kr is None:
        continue
    if kr > ku:
        diff += 1
    else:
        same += 1

print(f"  候选族受限的 k 严格更大: {diff}   相同: {same}")
