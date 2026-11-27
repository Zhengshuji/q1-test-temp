"""
证伪 q 的核心猜想检验。

【猜想 K1】对每个维度 d，条件
      "(5a)∧(5b) 可被某个 d 维的 row(L) 实现"
   在 L 的 A-不变包 Z 的格内要么对几乎所有 d 维子空间成立，
   要么对任何 d 维子空间都不成立。
   （即 (S) 是 Zariski-开条件 -> 随机取样即可判定）

【若 K1 成立】则存在**随机化多项式算法**：
   对 d = dim Z - dim V, ... 依次取随机 d 维子空间，
   若满足 (5a)∧(5b) 则 ν_min = d。
   -> q 为假（问题在 BPP ⊆ 实际可解）

本脚本直接检验 K1：对每个 d，取很多随机 d 维子空间，
看"满足 (5b) 的比例"是否总是 0 或接近 1。
"""
import numpy as np

TOL = 1e-7
rng = np.random.default_rng(20260105)


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
    pts = [complex(x) for x in (-5., -2., -1., -0.5, 0., 0.5, 1., 2., 5.)]
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


def random_subspace_in_lattice(L0, Z, d):
    """在 row(L0) ⊆ R ⊆ Z 的格里取一个随机 d 维子空间"""
    BL = basis_of(L0)
    BZ = basis_of(Z)
    r = BL.shape[0]
    if d < r or d > BZ.shape[0]:
        return None
    # 把 Z 的基正交化到 row(L0) 的正交补
    Q = np.linalg.qr(BL.T)[0]                       # (n, r)
    resid = BZ - BZ @ Q @ Q.T
    if rk(resid) < BZ.shape[0] - r:
        pass
    Bq = basis_of(resid)                            # Z 中与 row(L0) 正交的部分
    need = d - r
    if need > Bq.shape[0]:
        return None
    # 在 Bq 中随机取 need 维
    coef = rng.normal(size=(need, Bq.shape[0]))
    extra = coef @ Bq
    L = st(BL, extra)
    if rk(L) != d:
        return None
    return L


print("=" * 78)
print("检验 K1：对每个维度 d，(5b) 的可满足性是否呈 0/1 分布")
print("=" * 78)
print("  （每格取 40 个随机 d 维子空间，统计满足 (5a)∧(5b) 的比例）\n")

n = 4
found_odd = []
for trial in range(40):
    p = int(rng.integers(1, n - 1))
    r = int(rng.integers(1, n - p))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L0 = rng.integers(-2, 3, (r, n)).astype(float)
    if rk(C) < p or rk(L0) < r or rk(st(L0, C)) != p + r:
        continue

    Z = st(orbit(L0, A), orbit(C, A))
    V = st(L0, C, C @ A)
    dmin = rk(Z) - rk(V) + r          # (A) 允许的最小维度 + r
    dmax = rk(Z)

    for d in range(r, dmax + 1):
        cnt = tot = 0
        for _ in range(40):
            L = random_subspace_in_lattice(L0, Z, d)
            if L is None:
                continue
            tot += 1
            if condA(A, C, L) and condS(A, C, L):
                cnt += 1
        if tot == 0:
            continue
        frac = cnt / tot
        # 记录"既不是 0 也不是 1"的格子（会否证 K1）
        if 0.05 < frac < 0.95:
            found_odd.append((A.copy(), C.copy(), L0.copy(), d, cnt, tot))

print(f"  既非 0 也非 1 的格子数: {len(found_odd)}")
if found_odd:
    print("  => K1 被否证（(S) 不是纯 Zariski-开条件，或有其它退化）")
    for A, C, L0, d, cnt, tot in found_odd[:3]:
        print(f"     d={d}  {cnt}/{tot} 满足")
else:
    print("  => K1 在所有测试格子上成立：满足 (5b) 的比例总是 0 或 1")
    print("     这支持'随机取样即可判定'的证伪路线。")
