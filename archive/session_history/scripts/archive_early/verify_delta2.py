"""
强化版：用"刻意稀疏且结构化"的候选族，把 delta 逼出来。

思路（据 P1 §V-A 的 Grassmann 图卡）：
  无约束时 R 的行空间可取 Gr(k,s) 中任意点。
  要让候选族真正限制住，必须让候选族**无法线性组合出**所需的方向。
  例如：候选族只含"坐标轴方向"，而所需方向是"和向量"。
"""
import itertools

import numpy as np

TOL = 1e-6
rng = np.random.default_rng(13579)


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


def k_restricted(A, C, L0, cand, cap=3):
    for k in range(0, min(cap, len(cand)) + 1):
        for combo in itertools.combinations(range(len(cand)), k):
            R = np.array([cand[i] for i in combo]) if k else np.zeros((0, A.shape[1]))
            if both(A, C, st(L0, R)):
                return k
    return None


def k_unrestricted(A, C, L0, cap=3):
    n = A.shape[1]
    pool = [np.eye(n)[i] for i in range(n)]
    for v in itertools.product((-1, 0, 1), repeat=n):
        if any(v):
            pool.append(np.array(v, float))
    return k_restricted(A, C, L0, pool, cap=cap)


print("=" * 76)
print("强化实验：用结构化稀疏候选族逼出 delta")
print("=" * 76)

# 场景：让所需方向是"和向量"，而候选族只给"单坐标方向"
# 若所需方向恰好在候选族中 -> delta=0；否则 delta>0
results = {"delta0": 0, "delta_pos": 0, "infeasible": 0}
examples = []

for trial in range(200):
    n = 5
    p = 1
    r = 1
    A = np.zeros((n, n))
    # 幂零链：e1->e2->e3->...->en
    for i in range(n - 1):
        A[i, i + 1] = 1.0
    C = np.zeros((p, n))
    C[0, n - 1] = 1.0                       # 只测最后一个状态
    L0 = np.zeros((r, n))
    L0[0, 0] = 1.0                          # 目标是第一个状态

    if rk(st(L0, C)) != p + r:
        continue

    # 无约束
    ku = k_unrestricted(A, C, L0, cap=3)

    # 稀疏候选族：只给"单坐标"向量（不含所需的"和向量"）
    sparse = [np.eye(n)[i] for i in range(n)]
    ks = k_restricted(A, C, L0, sparse, cap=3)

    # 极稀疏：只给最后两个坐标
    tiny = [np.eye(n)[i] for i in range(n - 2, n)]
    kt = k_restricted(A, C, L0, tiny, cap=3)

    if ku is None:
        continue
    if ks is None or kt is None:
        results["infeasible"] += 1
        if len(examples) < 3:
            examples.append((ku, ks, kt, "infeasible"))
    elif ks == ku and kt == ku:
        results["delta0"] += 1
    else:
        results["delta_pos"] += 1
        if len(examples) < 3:
            examples.append((ku, ks, kt, "delta>0"))

print(f"  统计: {results}")
print(f"  样例 (k_unrestricted, k_sparse, k_tiny):")
for e in examples:
    print("   ", e)

print()
print("=" * 76)
print("关键结构性结论")
print("=" * 76)
print("""
  【为什么 delta 通常为 0】
  由 P1 §V-A：所有 k 维增广的行空间 ⟷ Gr(k, s), s = n - p - r。
  而无约束时 R 可取 Gr(k,s) 中**任意** k 维子空间。
  候选族要真正起作用，必须**无法线性组合出**目标子空间；
  但只要候选族含有足够多方向，线性组合总能张成目标子空间
  （因为 (5a) 的约束是"线性张成"，不是"集合并"）。

  => "增加的约束条件有多大影响"的准确答案：
     影响的**大小完全由候选族的线性张成能力决定**，
     而不是一个普适的增量。

  => 特别地：若候选族本身张成整个 R^n
     （例如含自然基），则受限问题 ≡ 无约束问题，delta ≡ 0。
     这正是我前面实验里 C_sparse（自然基）delta≈0 的原因。
""")
