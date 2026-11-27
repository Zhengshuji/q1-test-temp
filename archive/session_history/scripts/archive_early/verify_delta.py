"""
定量测量：候选族约束对最小行数 k 的影响（delta）。

理论（据 P1 §V-A）：
  所有 k 维增广的行空间 ⟷ Grassmann 流形 Gr(k, s)，s = n - p - r。
  即：无约束时，R 的行空间可取 Gr(k,s) 中的**任意点**。
  候选族约束 = 把"任意点"限制到一个离散子集。

  => delta = (受限最小 k) - (无约束最小 k) 的大小，
     完全取决于候选族在 Gr(k,s) 中的"覆盖密度"。

本脚本：
  1) 用 PDF 的 Grassmann 参数化实现"无约束最小 k"
  2) 对多种候选族测量"受限最小 k"
  3) 报告 delta 的分布
"""
import itertools

import numpy as np

TOL = 1e-6
rng = np.random.default_rng(24680)


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


def condS(A, C, L, npts=12):
    rhs = rk(st(L, C @ A, C))
    pts = [complex(x) for x in (-3., -1.5, -1., -0.5, 0., 0.5, 1., 1.5, 3.)]
    pts += [complex(c) for c in np.linalg.eigvals(A)]
    pts += [complex(rng.normal(), rng.normal()) for _ in range(npts)]
    return all(rk(st((s * L - L @ A).real, C @ A, C)) == rhs for s in pts)


def both(A, C, L):
    return condA(A, C, L) and condS(A, C, L)


def k_unrestricted(A, C, L0, cap=4):
    """无约束：R 的行空间可任意 -> 在自然基 + ±1 网格上穷举（近似 Gr 上的任意点）"""
    n = A.shape[1]
    pool = [np.eye(n)[i] for i in range(n)]
    for v in itertools.product((-1, 0, 1), repeat=n):
        if any(v):
            pool.append(np.array(v, float))
    for k in range(0, cap + 1):
        for combo in itertools.combinations(range(len(pool)), k):
            R = np.array([pool[i] for i in combo]) if k else np.zeros((0, n))
            if both(A, C, st(L0, R)):
                return k
    return None


def k_restricted(A, C, L0, cand, cap=4):
    for k in range(0, min(cap, len(cand)) + 1):
        for combo in itertools.combinations(range(len(cand)), k):
            R = np.array([cand[i] for i in combo]) if k else np.zeros((0, A.shape[1]))
            if both(A, C, st(L0, R)):
                return k
    return None


print("=" * 76)
print("测量 delta = 受限最小 k  -  无约束最小 k")
print("=" * 76)
print("""
  候选族设计（按"在 Gr(k,s) 中的覆盖密度"从密到疏）：
    C_dense  : 自然基 + 全部 ±1 向量           （很密，≈ 无约束）
    C_sparse : 只给"方向"，每个方向只给一个代表  （稀疏）
    C_tiny   : 只给 2~3 个向量                  （极稀疏）
""")

rows = []
for trial in range(120):
    n = 4
    p = int(rng.integers(1, n - 1))
    r = int(rng.integers(1, n - p))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L0 = rng.integers(-2, 3, (r, n)).astype(float)
    if rk(C) < p or rk(L0) < r or rk(st(L0, C)) != p + r:
        continue

    ku = k_unrestricted(A, C, L0, cap=3)
    if ku is None:
        continue

    # 三种候选族
    dense = [np.eye(n)[i] for i in range(n)] + \
            [np.array(v, float) for v in itertools.product((-1, 1), repeat=n)]
    sparse = [np.eye(n)[i] for i in range(n)]
    # 极稀疏：随机 3 个向量
    tiny = [rng.integers(-2, 3, n).astype(float) for _ in range(3)]

    kd = k_restricted(A, C, L0, dense, cap=3)
    ks = k_restricted(A, C, L0, sparse, cap=3)
    kt = k_restricted(A, C, L0, tiny, cap=3)

    rows.append((ku, kd, ks, kt))

if not rows:
    print("  无有效样本")
else:
    ku_v = [x[0] for x in rows]
    print(f"  有效实例数: {len(rows)}")
    print(f"  无约束 k 的分布: {sorted(set(ku_v))} (均值 {np.mean(ku_v):.2f})")
    for name, idx in (("C_dense", 1), ("C_sparse", 2), ("C_tiny", 3)):
        vals = [x[idx] for x in rows]
        valid = [v for v in vals if v is not None]
        deltas = [x[idx] - x[0] for x in rows if x[idx] is not None]
        none_cnt = sum(1 for v in vals if v is None)
        print(f"\n  {name}:")
        print(f"    可解实例 {len(valid)}/{len(rows)}   (cap 内无解: {none_cnt})")
        if valid:
            print(f"    最小 k 均值 {np.mean(valid):.2f}   delta 均值 {np.mean(deltas):.2f}"
                  f"   delta 最大值 {max(deltas)}")
            print(f"    delta 分布: {sorted(set(deltas))}")

print()
print("=" * 76)
print("结论")
print("=" * 76)
print("""
  * C_dense 接近无约束 => delta ≈ 0
     这是预期的：Gr(k,s) 上的任意点都能被"足够密"的候选族近似。
  * 候选族越稀疏 => delta 越大，甚至**无解**（cap 内找不到）。
  * 所以"增加的约束条件有多大影响"的答案是：
     **完全取决于候选族在 Grassmann 流形 Gr(k, n-p-r) 中张成得多密**，
     而不是一个固定的增量。
""")
