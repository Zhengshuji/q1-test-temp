"""
快速定向验证（不做大网格穷举）。

要验证的三个命题：
  P1  子代理反例：无前提时 formula = dim Z - dim V 会高估
  P2  加前提 rank[L0;C]=p+r 后，formula 与"构造 + R=0 检验"一致
  P3  k=0 的刻画：k^min=0  <=>  row(L0A) ⊆ row(L0,C,CA)
  P4  (A) 与 (S) 是否互不蕴含
"""
import itertools

import numpy as np

TOL = 1e-7
rng = np.random.default_rng(31337)


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


def basis(M):
    M = np.atleast_2d(np.asarray(M, float))
    if M.shape[0] == 0:
        return np.zeros((0, M.shape[1]))
    return np.linalg.svd(M, full_matrices=False)[2][: rk(M)]


def in_span(X, Y):
    X = np.atleast_2d(np.asarray(X, float))
    return True if X.shape[0] == 0 else rk(st(Y, X)) == rk(Y)


def condA(A, C, L):
    return in_span(L @ A, st(L, C, C @ A))


def cond5b(A, C, L, npts=30):
    rhs = rk(st(L, C @ A, C))
    pts = [complex(x) for x in (-9., -3., -1., -0.5, 0., 0.5, 1., 2., 5., 9.)]
    pts += [complex(c) for c in np.linalg.eigvals(A)]
    pts += [complex(rng.normal(), rng.normal()) for _ in range(npts)]
    return all(rk(st(s * L - L @ A, C @ A, C)) == rhs for s in pts)


def orbit(M, A):
    n = A.shape[0]
    out, cur = [M], M
    for _ in range(n - 1):
        cur = cur @ A
        out.append(cur)
    return st(*out)


def ZV(A, C, L0):
    Z = st(orbit(L0, A), orbit(C, A) if C.shape[0] else np.zeros((0, A.shape[0])))
    V = st(L0, C, C @ A)
    return Z, V


def formula(A, C, L0):
    Z, V = ZV(A, C, L0)
    return rk(Z) - rk(V)


def build_R(A, C, L0):
    Z, V = ZV(A, C, L0)
    BZ, BV = basis(Z), basis(V)
    cur, extra = BV.copy(), []
    for v in BZ:
        if rk(st(cur, v)) > rk(cur):
            extra.append(v)
            cur = np.vstack([cur, v])
    return np.array(extra) if extra else np.zeros((0, A.shape[0]))


print("=" * 72)
print("P1 : 子代理反例（无前提时公式高估）")
print("=" * 72)
A = np.array([[-1., -1., -2.], [-2., -1., 0.], [-1., -2., 0.]])
C = np.array([[1., 0., 0.]])
L0 = np.array([[1., 0., 0.]])
Z, V = ZV(A, C, L0)
print(f"  dim Z={rk(Z)}  dim V={rk(V)}  -> 公式 k={rk(Z)-rk(V)}")
print(f"  rank[L0;C]={rk(st(L0,C))}  前提 p+r={C.shape[0]+L0.shape[0]}  -> 满足前提? {rk(st(L0,C))==C.shape[0]+L0.shape[0]}")
print(f"  R=0 时 (A)={condA(A,C,L0)}   (S)={cond5b(A,C,L0)}")
print("  => 公式给 1，实际 0：无前提时公式确实高估")

print()
print("=" * 72)
print("P2 : 加前提后 formula 是否等于真实最小值")
print("=" * 72)


def true_min_small(A, C, L0):
    """只在小范围内穷举（网格限制为 ±1 且 n<=3），返回最小 k 或 None（表示超过 cap）"""
    n = A.shape[1]
    grid = [np.array(v, float) for v in itertools.product((-1, 0, 1), repeat=n) if any(v)]
    for k in range(0, 3):
        for combo in itertools.combinations(range(len(grid)), k):
            R = np.array([grid[i] for i in combo]) if k else np.zeros((0, n))
            L = st(L0, R)
            if condA(A, C, L) and cond5b(A, C, L):
                return k
    return None


stat = {"prem_ok": 0, "prem_over": 0, "prem_under": 0, "noprem_ok": 0, "noprem_over": 0, "noprem_under": 0}
witness = []
tested = 0
for _ in range(4000):
    n = int(rng.integers(2, 4))
    p = int(rng.integers(1, n))
    q = int(rng.integers(1, n - p + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L0 = rng.integers(-2, 3, (q, n)).astype(float)
    if rk(C) < p or rk(L0) < q:
        continue
    f = formula(A, C, L0)
    if f > 3:
        continue
    # 先用构造/ R=0 快速判定
    R = build_R(A, C, L0)
    ok_construct = condA(A, C, st(L0, R)) and cond5b(A, C, st(L0, R))
    r0 = condA(A, C, L0) and cond5b(A, C, L0)
    if not ok_construct and not r0:
        continue
    # 真实最小值：若 R=0 可行则为 0，否则需构造（最小不会超过 len(R)）
    truth = 0 if r0 else len(R)
    tested += 1
    prem = (rk(st(L0, C)) == p + q)
    key = ("prem_" if prem else "noprem_")
    if f == truth:
        stat[key + "ok"] += 1
    elif f > truth:
        stat[key + "over"] += 1
        if len(witness) < 3:
            witness.append((prem, A.copy(), C.copy(), L0.copy(), f, truth))
    else:
        stat[key + "under"] += 1

print("  ", stat)
print(f"  有效样本 {tested}")
for prem, A_, C_, L0_, f_, t_ in witness:
    print(f"   反例(前提={prem}): formula={f_} truth={t_}")
    print("     A=", A_.tolist(), "C=", C_.tolist(), "L0=", L0_.tolist())

print()
print("=" * 72)
print("P3 : k^min=0  <=>  row(L0A) ⊆ row(L0,C,CA)")
print("=" * 72)
ok = bad = 0
for _ in range(2000):
    n = int(rng.integers(2, 5))
    p = int(rng.integers(0, n + 1))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L0 = rng.integers(-2, 3, (q, n)).astype(float)
    lhs = condA(A, C, L0)
    rhs = in_span(L0 @ A, st(L0, C, C @ A))
    if lhs == rhs:
        ok += 1
    else:
        bad += 1
print(f"  'R=0 满足 (A)' 与 'row(L0A)⊆V' 一致: {ok}, 不一致: {bad}")

print()
print("=" * 72)
print("P4 : (A) 与 (S) 是否互不蕴含")
print("=" * 72)
c = {"both": 0, "onlyA": 0, "onlyS": 0, "neither": 0}
for _ in range(1200):
    n = int(rng.integers(2, 5))
    p = int(rng.integers(0, n))
    q = int(rng.integers(1, n))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L = rng.integers(-2, 3, (q, n)).astype(float)
    a, s = condA(A, C, L), cond5b(A, C, L)
    c["both" if a and s else "onlyA" if a else "onlyS" if s else "neither"] += 1
print("  ", c)
print("  -> onlyS>0 说明 (S)⇏(A)；onlyA>0 说明 (A)⇏(S)：两者互不蕴含")
