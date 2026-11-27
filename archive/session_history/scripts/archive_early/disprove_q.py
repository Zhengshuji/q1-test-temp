"""
q 的证伪算法（随机化多项式时间）—— 完整实现与验证。

【算法】
输入 (A, C, L0)。
1. 计算 Z := row(O_{L0}) + row(O_C)   （包含 row(L0) 的最小 A-不变子空间）
2. 对 d = dim Z, dim Z-1, ..., r 降序：
     在格 {R : row(L0) ⊆ R ⊆ Z, dim R = d} 中随机取若干子空间 R；
     若存在 R 同时满足 (A) 与 (S)，则 ν_min = d，返回。
3. 若全部失败，返回"无解"（可能需增大 d 的上界）。

【为什么正确（关键论断）】
* (A) 是子空间条件：(A) ⟺ row(RA) ⊆ row(L0) + row(C) + row(CA) + R。
* (S) 是**开条件**：
    (5b) ⟺ rank P_L(s) ≡ rank H_L，其中 P_L(s)=(sL−LA)N_{CA}。
    由 P1 Thm 4，等价于某组 h 阶子式无公共根 ⟺ 某组子式不全为零。
    这是"某个多项式 ≠ 0"，故为 Zariski-开。
  => 若某个 d 维子空间满足 (S)，则**几乎所有** d 维子空间都满足。
  => 随机取样即可判定"是否存在 d 维解"。

【若算法正确】=> ν_min 可在随机化多项式时间内计算
                => q 的命题（NP-hard）为**假**（除非 NP ⊆ BPP）
"""
import numpy as np

TOL = 1e-7
rng = np.random.default_rng(31415926)


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
    rhs = rk(st(L, C @ A, C))
    pts = [complex(x) for x in (-7., -3., -1., -0.5, 0., 0.5, 1., 2., 3., 7.)]
    pts += [complex(c) for c in np.linalg.eigvals(A)]
    pts += [complex(rng.normal(), rng.normal()) for _ in range(npts)]
    return all(rk(st((s * L - L @ A).real, C @ A, C)) == rhs for s in pts)


def orbit(M, A):
    n = A.shape[0]
    out, cur = [M], M
    for _ in range(n - 1):
        cur = cur @ A
        out.append(cur)
    return st(*out)


def basis_of(M):
    M = np.atleast_2d(np.asarray(M, float))
    if M.shape[0] == 0:
        return np.zeros((0, M.shape[1]))
    return np.linalg.svd(M, full_matrices=False)[2][: rk(M)]


def rand_subspace(L0, Z, d, tries=1):
    """在格 row(L0) ⊆ R ⊆ Z 中随机取 d 维子空间"""
    BL = basis_of(L0)
    BZ = basis_of(Z)
    r = BL.shape[0]
    if d < r or d > BZ.shape[0]:
        return None
    Q = np.linalg.qr(BL.T)[0]
    Bq = basis_of(BZ - BZ @ Q @ Q.T)      # Z 中正交于 row(L0) 的部分
    need = d - r
    if need > Bq.shape[0]:
        return None
    coef = rng.normal(size=(need, Bq.shape[0]))
    L = st(BL, coef @ Bq)
    return L if rk(L) == d else None


def solve_nu_min(A, C, L0, samples=12, verbose=False):
    n = A.shape[0]
    r = L0.shape[0]
    Z = st(orbit(L0, A), orbit(C, A))
    dZ = rk(Z)
    # 由 (A) 的最小维度下界（定理 2）：dim Z - dim V + r
    V = st(L0, C, C @ A)
    dlo = rk(Z) - rk(V) + r
    for d in range(dlo, dZ + 1):
        hit = 0
        for _ in range(samples):
            L = rand_subspace(L0, Z, d)
            if L is None:
                continue
            if condA(A, C, L) and condS(A, C, L):
                hit += 1
        if verbose:
            print(f"    d={d}: {hit}/{samples} 满足")
        if hit > 0:
            return d, True
    return None, False


def brute_nu_min(A, C, L0, cap=4):
    """网格穷举（仅小规模），作为独立对照"""
    import itertools
    n = A.shape[1]
    pool = [np.eye(n)[i] for i in range(n)]
    for v in itertools.product((-1, 0, 1), repeat=n):
        if any(v):
            pool.append(np.array(v, float))
    for k in range(0, cap + 1):
        for combo in itertools.combinations(range(len(pool)), k):
            R = np.array([pool[i] for i in combo]) if k else np.zeros((0, n))
            L = st(L0, R)
            if rk(L) != L0.shape[0] + k:
                continue
            if condA(A, C, L) and condS(A, C, L):
                return rk(L)
    return None


print("=" * 78)
print("算法验证：随机化算法 vs 穷举")
print("=" * 78)
ok = bad = skipped = 0
mismatch = []
for trial in range(150):
    n = 4
    p = int(rng.integers(1, n - 1))
    r = int(rng.integers(1, n - p))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L0 = rng.integers(-2, 3, (r, n)).astype(float)
    if rk(C) < p or rk(L0) < r or rk(st(L0, C)) != p + r:
        continue

    d_alg, found = solve_nu_min(A, C, L0, samples=10)
    bf = brute_nu_min(A, C, L0, cap=3)

    if bf is None and not found:
        skipped += 1
        continue
    if bf is None:
        # 穷举 cap 不够，无法对照
        skipped += 1
        continue
    if not found:
        bad += 1
        mismatch.append((A, C, L0, d_alg, bf, "算法未找到"))
        continue
    if d_alg == bf:
        ok += 1
    else:
        bad += 1
        mismatch.append((A, C, L0, d_alg, bf, "值不同"))

print(f"  一致 {ok}，不一致 {bad}，跳过 {skipped}")
for A, C, L0, da, bf, why in mismatch[:4]:
    print(f"    {why}: 算法={da} 穷举={bf}")
    print(f"      A={A.tolist()} C={C.tolist()} L0={L0.tolist()}")

print()
print("=" * 78)
print("附加检验：单次采样的成功率（若 (S) 是开条件，应接近 1）")
print("=" * 78)
succ = []
for trial in range(60):
    n = 4
    p = int(rng.integers(1, n - 1))
    r = int(rng.integers(1, n - p))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L0 = rng.integers(-2, 3, (r, n)).astype(float)
    if rk(C) < p or rk(L0) < r or rk(st(L0, C)) != p + r:
        continue
    Z = st(orbit(L0, A), orbit(C, A))
    V = st(L0, C, C @ A)
    d = rk(Z) - rk(V) + r
    if d > rk(Z):
        continue
    cnt = 0
    for _ in range(30):
        L = rand_subspace(L0, Z, d)
        if L is not None and condA(A, C, L) and condS(A, C, L):
            cnt += 1
    succ.append(cnt / 30)
if succ:
    print(f"  在 (A) 允许的最小维度 d 上，随机子空间满足 (5a)∧(5b) 的成功率:")
    print(f"    均值 {np.mean(succ):.3f}   中位数 {np.median(succ):.3f}")
    print(f"    完全失败的实例数: {sum(1 for x in succ if x == 0)}/{len(succ)}")
    print("  （成功率接近 1 => (S) 是开条件；成功率 0 => 该维度确实无解）")
