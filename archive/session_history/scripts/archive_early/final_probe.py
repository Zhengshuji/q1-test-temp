"""
最终判定实验（干净版）。

定义（严格按 P3 Theorem 2）：
   (5a)  rank[LA; CA; C] = rank[CA; C; L]
   (5b)  rank[sL - LA; CA; C] = rank[CA; C; L]   for all s in C
其中 L = [L0 ; R]，rows(L) = r + |R| 就是观测器阶数。

P1 的等价形式：
   (A)   row(LA) ⊆ row(L, C, CA)
   (S)   rank[λL - LA; CA; C] = rank[L; CA; C]  ∀λ

本脚本要判定四件事：
  F1  (5a) 与 (A) 是否等价？             （预期：不等价，(A) ⇒ (5a)）
  F2  满足 (A)+(S) 时最小 |R| 是否等于    dim row(O_{L0}) - rank(L0)？
  F3  该最小值是否多项式可算？           （预期：是）
  F4  若把 R 限制在给定候选族，最小 |R| 是否 = 最小集合覆盖？（预期：是）
"""
import itertools

import numpy as np

rng = np.random.default_rng(31415)
TOL = 1e-7


def _real(M):
    M = np.asarray(M)
    return np.atleast_2d(M.real.astype(float))


def rank(M):
    M = _real(M)
    if M.size == 0 or M.shape[0] == 0:
        return 0
    s = np.linalg.svd(M, compute_uv=False)
    if s.size == 0:
        return 0
    return int(np.sum(s > TOL * max(M.shape) * (s[0] if s[0] > 0 else 1.0)))


def stack(*blocks):
    blocks = [_real(b) for b in blocks]
    ncols = max((b.shape[1] for b in blocks), default=0)
    blocks = [b for b in blocks if b.shape[0] > 0]
    return np.zeros((0, ncols)) if not blocks else np.vstack(blocks)


def in_span(X, Y):
    """X 的每一行是否都在 Y 的行空间里"""
    X, Y = _real(X), _real(Y)
    if X.shape[0] == 0:
        return True
    return rank(stack(Y, X)) == rank(Y)


# ----------------------------------------------------------------- 条件
def cond5a(A, C, L):
    return rank(stack(L @ A, C @ A, C)) == rank(stack(C @ A, C, L))


def condA(A, C, L):
    """P1 的 (A)：row(LA) ⊆ row(L,C,CA)"""
    return in_span(L @ A, stack(L, C, C @ A))


def cond5b(A, C, L, npts=30):
    rhs = rank(stack(C @ A, C, L))
    pts = [complex(x) for x in (-7.0, -2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0, 7.0)]
    pts += [complex(c) for c in np.linalg.eigvals(A)]
    pts += [complex(rng.normal(), rng.normal()) for _ in range(npts)]
    for s in pts:
        if rank(s * L - L @ A) + rank(stack(C @ A, C, s * L - L @ A, L)) - rank(
            stack(C @ A, C, s * L - L @ A)
        ) != rank(stack(C @ A, C, L)):
            pass
    return all(rank(stack(s * L - L @ A, C @ A, C)) == rhs for s in pts)


def condS(A, C, L, npts=30):
    rhs = rank(stack(L, C @ A, C))
    pts = [complex(x) for x in (-7.0, -2.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.0, 7.0)]
    pts += [complex(c) for c in np.linalg.eigvals(A)]
    pts += [complex(rng.normal(), rng.normal()) for _ in range(npts)]
    return all(rank(stack(x * L - L @ A, C @ A, C)) == rhs for x in pts)


def observable_orbit(A, M):
    """O_M = [M; MA; MA^2; ...]，最多 n 项（Cayley-Hamilton）"""
    n = A.shape[0]
    blocks, cur = [M], M
    for _ in range(n - 1):
        cur = cur @ A
        blocks.append(cur)
    return stack(*blocks)


# ---------------------------------------------------------------- F1
print("=" * 78)
print("F1 : (5a) 与 (A) 的关系")
print("=" * 78)
only5a = onlyA = both = neither = 0
for _ in range(2000):
    n = int(rng.integers(2, 6))
    p = int(rng.integers(0, n + 1))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L = rng.integers(-2, 3, (q, n)).astype(float)
    a, b = cond5a(A, C, L), condA(A, C, L)
    if a and b:
        both += 1
    elif a:
        only5a += 1
    elif b:
        onlyA += 1
    else:
        neither += 1
print(f"  两者都真 {both} | 仅 (5a) 真 {only5a} | 仅 (A) 真 {onlyA} | 都假 {neither}")
print("  结论：" + ("(A) ⇒ (5a)，但反之不成立 → 二者不等价"
                 if onlyA == 0 and only5a > 0 else "需再看"))

# ---------------------------------------------------------------- F2/F3
print()
print("=" * 78)
print("F2/F3 : 满足 (A)+(S) 的最小 |R| = dim row(O_L0) - rank(L0) ？")
print("=" * 78)


def orbit_min(A, C, L0):
    """dim row([C;CA;O_L0]) - rank([C;CA;L0])  —— 多项式可算"""
    base = stack(C, C @ A)
    return rank(stack(base, observable_orbit(A, L0))) - rank(stack(base, L0))


def build_R(A, C, L0):
    base = stack(C, C @ A)
    Q = stack(base, L0)
    P = stack(base, observable_orbit(A, L0))
    BQ = np.linalg.svd(Q, full_matrices=False)[2] if Q.shape[0] else np.zeros((0, A.shape[0]))
    BQ = BQ[:rank(Q)]
    BP = np.linalg.svd(P, full_matrices=False)[2] if P.shape[0] else np.zeros((0, A.shape[0]))
    BP = BP[:rank(P)]
    cur, extra = BQ.copy(), []
    for v in BP:
        if rank(stack(cur, v)) > rank(cur):
            extra.append(v)
            cur = np.vstack([cur, v])
    return np.array(extra) if extra else np.zeros((0, A.shape[0]))


ok_a = ok_s = fail = tested = 0
for trial in range(500):
    n = int(rng.integers(2, 6))
    p = int(rng.integers(0, n + 1))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L0 = rng.integers(-2, 3, (q, n)).astype(float)
    if rank(L0) < q:
        continue
    tested += 1
    k = orbit_min(A, C, L0)
    R = build_R(A, C, L0)
    if R.shape[0] != k:
        fail += 1
        continue
    L = stack(L0, R)
    if condA(A, C, L):
        ok_a += 1
    if condS(A, C, L):
        ok_s += 1
print(f"  测试 {tested} 个实例")
print(f"  构造出的 R（{0} 行）满足 (A) 的个数: {ok_a}")
print(f"  构造出的 R 满足 (S) 的个数      : {ok_s}")
print(f"  构造行数 ≠ 公式的个数           : {fail}")
print("  说明：公式给出的是满足 (A) 的最小行数下界；(S) 可能需要更多行。")

# ---------------------------------------------------------------- F4
print()
print("=" * 78)
print("F4 : 候选族受限时，最小 |R| 是否 = 最小集合覆盖？")
print("=" * 78)
print("""
  构造（让覆盖真正被强制）：
     A = I_r  （恒等）， C = 0， 于是 row(C,CA) = {0}
     L0 取 r 行，使得 row(L0 A) = row(L0) 且 rank(L0) = r-? ...
  为避免"单个函数填充整个空间"的平凡解，必须让 L0 的行在 A 下产生
  互相独立的方向。本实验采用最小可靠模型：
     A = blockdiag over e in U  of [[0,1],[0,0]]   (n = 2r)
     C = 0
     L0: 一行 -> 该块的第 2 个基向量 y_e  （即 L0 = [y_1; ...; y_r]）
     candidate for S : row  sum_{e in S} x_e
  则 row(L0 A) = row(x_1,...,x_r)，
     row(C) + row(CA) + row(L0) = span{x_e} + span{y_e} = R^n
  于是 (5a)/(A) 成立 ⟺ span{x_e} ⊆ span{x_e} + span{cand}  —— 恒成立，退化。
  改用：L0 = [x_1;...;x_r]，candidate = sum_{e in S} y_e，A: x_e -> y_e, y_e -> 0。
  这时 row(L0 A) = span{y_e}，而 row(C)+row(CA)+row(L0) = span{x_e,y_e}，
  (A) 要求 row(L0 A) ⊆ row(L) + row(C,CA) = span{x_e} + span{cand}，
  即 span{y_e} ⊆ span{y_e 中 cand 覆盖的部分} ⟺ U ⊆ ∪ S_i  —— 集合覆盖！
""")

bad = tested = 0
first = None
for trial in range(400):
    m = int(rng.integers(2, 7))
    r = int(rng.integers(2, 6))
    sets = [sorted(rng.choice(r, size=int(rng.integers(1, r + 1)), replace=False).tolist())
            for _ in range(m)]
    for e in range(r):
        if not any(e in s for s in sets):
            j = int(rng.integers(0, m))
            sets[j] = sorted(set(sets[j]) | {e})

    n = 2 * r
    A = np.zeros((n, n))
    for i in range(r):
        A[2 * i, 2 * i + 1] = 1.0          # x_i -> y_i
    C = np.zeros((0, n))
    L0 = np.zeros((r, n))
    for i in range(r):
        L0[i, 2 * i] = 1.0                 # L0 = [x_1;...;x_r]
    cand = []
    for S in sets:
        v = np.zeros(n)
        for e in S:
            v[2 * e + 1] = 1.0             # sum of y_e
        cand.append(v)

    kmin = None
    for k in range(0, m + 1):
        for combo in itertools.combinations(range(m), k):
            R = np.array([cand[i] for i in combo]) if k else np.zeros((0, n))
            if condA(A, C, stack(L0, R)):
                kmin = k
                break
        if kmin is not None:
            break

    sc = None
    for k in range(0, m + 1):
        for combo in itertools.combinations(range(m), k):
            cov = set()
            for i in combo:
                cov |= set(sets[i])
            if len(cov) == r:
                sc = k
                break
        if sc is not None:
            break

    tested += 1
    if sc != kmin:
        bad += 1
        if first is None:
            first = (sets, r, sc, kmin)
print(f"  测试 {tested} 个实例，不一致 {bad} → {'一致（CONFIRMED）' if bad == 0 else '不一致'}")
if first:
    print(f"  首个反例: sets={first[0]} r={first[1]} 集合覆盖={first[2]} 观测器={first[3]}")
