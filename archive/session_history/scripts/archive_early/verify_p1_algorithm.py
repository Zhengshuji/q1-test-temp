"""
实现并验证 P1 §III–IV 的算法，确认：
  (1) 有序秩保留构造 -> 功能可观性指数 eta_j
  (2) 一阶依赖关系   -> 系数行 phi_{p+j}
  (3) 公式 (8)       -> 额外行 l_{j,t}
  (4) 结果满足 (A)，且行数 = q0 = sum_j eta_j
"""
import numpy as np

TOL = 1e-7
rng = np.random.default_rng(1234)


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


def ordered_rank_retention(A, C, L0):
    """
    P1 §III 的全局有序秩保留构造。
    全局顺序: g1..g_{p+r}; g1 A .. ; g1 A^2 .. (按幂次递增，同幂内按 generator 序号)
    返回: M(保留行，按保留顺序), alpha_i (i=1..p+r), 以及每个保留行的 (generator, power)
    """
    p = C.shape[0]
    r = L0.shape[0]
    gens = [C[i] for i in range(p)] + [L0[j] for j in range(r)]
    n = A.shape[0]
    M = np.zeros((0, n))
    info = []          # 每个保留行的 (generator index, power)
    highest = [-1] * (p + r)   # 每个 generator 的最高保留幂次
    q = 0
    while q <= n:                     # Cayley-Hamilton: 幂次到 n 足够
        progressed = False
        for i in range(p + r):
            if highest[i] >= 0 and q > highest[i] + 1:
                continue              # 该 generator 已遇到依赖，后续全依赖
            v = gens[i] @ np.linalg.matrix_power(A, q) if q > 0 else gens[i].copy()
            if rk(st(M, v)) > rk(M):
                M = st(M, v)
                info.append((i, q))
                highest[i] = q
                progressed = True
        q += 1
        if all(highest[i] >= 0 and q > highest[i] + 1 for i in range(p + r)):
            break
    alpha = [highest[i] + 1 for i in range(p + r)]
    return M, alpha, info


def first_dependence_coeffs(A, C, L0, M, info):
    """
    对每个 generator i，求 phi_i 使 g_i A^{alpha_i} = phi_i · M^-_i
    M^-_i = 在 g_i A^{alpha_i} 被检查之前保留的行的矩阵（按全局顺序）
    按 P1 的全局顺序：幂次 q < alpha_i 的全部；q = alpha_i 且 generator < i 的
    """
    p = C.shape[0]
    r = L0.shape[0]
    gens = [C[i] for i in range(p)] + [L0[j] for j in range(r)]
    alpha = [max(pw for (gi, pw) in info if gi == i) + 1 for i in range(p + r)]
    phis = {}
    for i in range(p + r):
        ai = alpha[i]
        # M^-_i：按全局顺序在 g_i A^{ai} 之前被检查的**保留**行
        keep = [k for k, (gi, pw) in enumerate(info)
                if pw < ai or (pw == ai and gi < i)]
        if not keep:
            continue
        Mi = M[keep]
        target = gens[i] @ np.linalg.matrix_power(A, ai)
        # 解 phi Mi = target
        phi, *_ = np.linalg.lstsq(Mi.T, target, rcond=None)
        if rk(Mi) != len(keep):
            continue
        phis[i] = (phi, keep, target)
    return phis, alpha


def build_augmentation(A, C, L0, M, info, phis, alpha):
    """按公式 (8) 构造额外行 l_{j,t}"""
    p = C.shape[0]
    L = [L0[j].copy() for j in range(L0.shape[0])]
    extra = []
    for j in range(L0.shape[0]):
        i = p + j
        eta = alpha[i]
        if eta == 1:
            continue
        phi, keep, _ = phis[i]
        # phi 的分量对应 M[keep] 的行，而这些行是 (generator, power)
        base_rows = [(info[k][0], info[k][1]) for k in keep]
        # phi 在 P1 中按 power 分块 (q=0..eta)
        for t in range(1, eta):
            # l_{j,t} = Lj A^t - sum_{q=1}^{t} phi^{(q)} G^{(q)} A^{t-q}
            # 等价地，在 keep 中取 power>=1 的项，系数为 phi 对应分量
            row = L0[j] @ np.linalg.matrix_power(A, t)
            for (gi, pw), coef in zip(base_rows, phi):
                if pw >= 1:
                    # 该项对应的 generator 行是 gens[gi]，幂次 pw
                    gens_i = (C[gi] if gi < p else L0[gi - p])
                    row = row - coef * (gens_i @ np.linalg.matrix_power(A, pw))
            extra.append(row)
    return extra


print("=" * 74)
print("验证 P1 算法")
print("=" * 74)
ok = bad = 0
for trial in range(60):
    n = int(rng.integers(2, 5))
    p = int(rng.integers(1, n))
    r = int(rng.integers(1, n - p + 1)) if n - p >= 1 else 1
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L0 = rng.integers(-2, 3, (r, n)).astype(float)
    if rk(C) < p or rk(L0) < r or rk(st(L0, C)) != p + r:
        continue

    M, alpha, info = ordered_rank_retention(A, C, L0)
    phis, alpha = first_dependence_coeffs(A, C, L0, M, info)
    extra = build_augmentation(A, C, L0, M, info, phis, alpha)

    q0 = sum(alpha[C.shape[0] + j] for j in range(r))
    k_expected = q0 - r
    R = np.array(extra) if extra else np.zeros((0, n))
    L = st(L0, R)

    okA = condA(A, C, L)
    okK = (R.shape[0] == k_expected)
    if okA and okK:
        ok += 1
    else:
        bad += 1
        if bad <= 4:
            print(f"  [t{trial}] eta={[alpha[C.shape[0]+j] for j in range(r)]} "
                  f"k_expected={k_expected} k_got={R.shape[0]} (A)={okA}")

print(f"  通过 {ok}，失败 {bad}")
print("  说明：若通过率高，则我对算法步骤的描述正确。")
