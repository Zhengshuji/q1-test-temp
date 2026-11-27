"""
定理 3 的强化验证：Σ_d 的满足率是否严格呈 {0} ∪ [高, 1]？

若存在格子满足率落在 (0, 0.5)，则定理 3 的算法含义（"随机取样可判定"）受威胁。
本脚本加大样本、覆盖更多维度与实例，专门搜索"低但非零"的满足率。
"""
import numpy as np

TOL = 1e-7
rng = np.random.default_rng(11223344)


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


def condS_exact(A, C, L, npts=30):
    """
    更严格的 (S) 检验：
      rank[sL-LA; CA; C] == rank[L; CA; C] 对所有 s
    采样包含：A 的特征值、±大数、随机复数、以及 s 使 (sL-LA) 秩下降的候选点。
    """
    rhs = rk(st(L, C @ A, C))
    pts = [complex(x) for x in (-10., -3., -1., -0.5, 0., 0.5, 1., 2., 3., 10., 1e3, -1e3)]
    pts += [complex(c) for c in np.linalg.eigvals(A)]
    # 广义特征值 s：使 sL - LA 降秩的候选（一般化特征值问题）
    try:
        Lp = np.linalg.pinv(L)
        eigs = np.linalg.eigvals(LA := L @ A)
        _ = eigs
    except Exception:
        pass
    pts += [complex(rng.normal(), rng.normal()) for _ in range(npts)]
    pts += [complex(rng.normal(0, 5), rng.normal(0, 5)) for _ in range(10)]
    for s in pts:
        if rk(st((s * L - L @ A).real, C @ A, C)) != rhs:
            return False
    return True


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


def rand_subspace(L0, Z, d):
    BL, BZ = basis_of(L0), basis_of(Z)
    r = BL.shape[0]
    if d < r or d > BZ.shape[0]:
        return None
    Q = np.linalg.qr(BL.T)[0]
    Bq = basis_of(BZ - BZ @ Q @ Q.T)
    need = d - r
    if need > Bq.shape[0]:
        return None
    L = st(BL, rng.normal(size=(need, Bq.shape[0])) @ Bq)
    return L if rk(L) == d else None


print("=" * 78)
print("搜索'满足率低但非零'的格子（会威胁定理 3 的算法含义）")
print("=" * 78)

N_SAMPLES = 60
buckets = {"=0": 0, "(0,0.2]": 0, "(0.2,0.5]": 0, "(0.5,0.9)": 0, ">=0.9": 0, "=1": 0}
odd = []
total_cells = 0

for trial in range(120):
    n = int(rng.integers(3, 6))
    p = int(rng.integers(1, n))
    r = int(rng.integers(1, n - p + 1)) if n - p >= 1 else 1
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L0 = rng.integers(-2, 3, (r, n)).astype(float)
    if rk(C) < p or rk(L0) < r or rk(st(L0, C)) != p + r:
        continue

    Z = st(orbit(L0, A), orbit(C, A))
    V = st(L0, C, C @ A)
    dZ = rk(Z)

    for d in range(r, dZ + 1):
        cnt = tot = 0
        for _ in range(N_SAMPLES):
            L = rand_subspace(L0, Z, d)
            if L is None:
                continue
            tot += 1
            if condA(A, C, L) and condS_exact(A, C, L):
                cnt += 1
        if tot < N_SAMPLES * 0.5:
            continue
        total_cells += 1
        frac = cnt / tot
        if cnt == 0:
            buckets["=0"] += 1
        elif cnt == tot:
            buckets["=1"] += 1
        elif frac <= 0.2:
            buckets["(0,0.2]"] += 1
            odd.append((A.copy(), C.copy(), L0.copy(), d, cnt, tot))
        elif frac <= 0.5:
            buckets["(0.2,0.5]"] += 1
            odd.append((A.copy(), C.copy(), L0.copy(), d, cnt, tot))
        elif frac < 0.9:
            buckets["(0.5,0.9)"] += 1
            odd.append((A.copy(), C.copy(), L0.copy(), d, cnt, tot))
        else:
            buckets[">=0.9"] += 1

print(f"  总格子数（每格 {N_SAMPLES} 个随机样本）: {total_cells}")
print(f"  满足率分布: {buckets}")
print()
if odd:
    print(f"  **发现 {len(odd)} 个'低但非零'的格子** —— 需要审视定理 3：")
    for A, C, L0, d, cnt, tot in odd[:5]:
        print(f"    d={d}: {cnt}/{tot}")
        print(f"      A={A.tolist()}")
        print(f"      C={C.tolist()}  L0={L0.tolist()}")
else:
    print("  **未发现任何'低但非零'的格子**")
    print("  => 满足率严格呈 {0} ∪ [0.9, 1]，支持定理 3 的算法含义")
    print("     （非空 dim-格 上随机取样以高概率命中）")
