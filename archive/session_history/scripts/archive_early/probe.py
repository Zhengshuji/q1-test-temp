"""
关键判定实验：在"功能可观"前提下，(5a) 是否等价于包含关系 row(LA) ⊆ row(C,CA,L)？

背景：P1 明确写 (A) ⇔ row(LA) ⊆ row(L,C,CA)。
      P3 写的是 rank[LA;CA;C] = rank[CA;C;L] —— 这是秩等式，形式上更弱。
      我的数值实验曾发现二者不等价，怀疑是"功能可观性"前提在起作用。
本脚本把这个前提显式加入，重新判定。
"""
import itertools
import numpy as np

rng = np.random.default_rng(20260101)
TOL = 1e-8


def rank(M):
    M = np.atleast_2d(np.asarray(M, dtype=float))
    if M.size == 0 or M.shape[0] == 0:
        return 0
    s = np.linalg.svd(M, compute_uv=False)
    if s.size == 0:
        return 0
    return int(np.sum(s > TOL * max(M.shape) * (s[0] if s[0] > 0 else 1.0)))


def stack(*blocks):
    blocks = [np.atleast_2d(np.asarray(b, dtype=float)) for b in blocks]
    ncols = max((b.shape[1] for b in blocks), default=0)
    blocks = [b for b in blocks if b.shape[0] > 0]
    return np.zeros((0, ncols)) if not blocks else np.vstack(blocks)


def in_span(X, Y):
    """X 的每一行是否都在 Y 的行空间中"""
    if X.shape[0] == 0:
        return True
    return rank(stack(Y, X)) == rank(Y)


def observability_matrix(A, M, horizon):
    """O = [M; MA; ...; MA^{horizon-1}]"""
    blocks = [M]
    cur = M
    for _ in range(horizon - 1):
        cur = cur @ A
        blocks.append(cur)
    return stack(*blocks)


def cond5a(A, C, L):
    return rank(stack(L @ A, C @ A, C)) == rank(stack(C @ A, C, L))


def cond_A_contain(A, C, L):
    return in_span(L @ A, stack(C, C @ A, L))


def cond5a_plus(A, C, L):
    """P1 的 (A)：rank[LA;L;CA;C] = rank[L;CA;C]"""
    return rank(stack(L @ A, L, C @ A, C)) == rank(stack(L, C @ A, C))


def cond5b(A, C, L, npts=40):
    rhs = rank(stack(C @ A, C, L))
    pts = [complex(x) for x in (-11.0, -3.0, -1.0, -0.5, 0.0, 0.5, 1.0, 2.5, 3.0, 11.0, 1e4)]
    pts += [complex(c) for c in np.linalg.eigvals(A)]
    pts += [complex(rng.normal(), rng.normal()) for _ in range(npts)]
    return all(rank(stack(s * L - L @ A, C @ A, C)) == rhs for s in pts)


def functionally_observable(A, C, L):
    """row(O_L) ⊆ row(O_C)，取 horizon = n 足够（Cayley-Hamilton）"""
    n = A.shape[0]
    OL = observability_matrix(A, L, n)
    OC = observability_matrix(A, C, n) if C.shape[0] > 0 else np.zeros((0, n))
    return in_span(OL, OC)


print("=" * 78)
print("实验 1：不加功能可观前提 —— (5a) 与包含关系是否等价？")
print("=" * 78)
stat = {"agree": 0, "5a_but_not_contain": 0, "contain_but_not_5a": 0}
for _ in range(1500):
    n = int(rng.integers(2, 6))
    p = int(rng.integers(0, n + 1))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L = rng.integers(-2, 3, (q, n)).astype(float)
    a, c = cond5a(A, C, L), cond_A_contain(A, C, L)
    if a and c:
        stat["agree"] += 1
    elif a and not c:
        stat["5a_but_not_contain"] += 1
    elif c and not a:
        stat["contain_but_not_5a"] += 1
    else:
        stat["agree"] += 1
print("  ", stat)
print("   注意：'contain_but_not_5a' 若为 0，说明包含关系 ⇒ (5a)（秩等式更弱）。")

print()
print("=" * 78)
print("实验 2：加功能可观前提 —— (5a) 是否等价于包含关系？")
print("=" * 78)
checked = 0
bad = 0
examples = []
for _ in range(4000):
    n = int(rng.integers(2, 5))
    p = int(rng.integers(1, n))          # 至少一个量测，便于构造功能可观
    q = int(rng.integers(1, n))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L = rng.integers(-2, 3, (q, n)).astype(float)
    if not functionally_observable(A, C, L):
        continue
    checked += 1
    a, c = cond5a(A, C, L), cond_A_contain(A, C, L)
    if a != c:
        bad += 1
        if len(examples) < 3:
            examples.append((A.copy(), C.copy(), L.copy(), a, c))
print(f"  功能可观的实例数 = {checked}； (5a) 与包含关系不一致的个数 = {bad}")
for A, C, L, a, c in examples:
    print("   ----")
    print("   A =\n", A, "\n   C =\n", C, "\n   L =\n", L)
    print("   (5a) =", a, "  contain =", c)

print()
print("=" * 78)
print("实验 3：(5a) 与 P1 的 (A) 是否等价？")
print("=" * 78)
d1 = d2 = 0
for _ in range(1500):
    n = int(rng.integers(2, 6))
    p = int(rng.integers(0, n + 1))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L = rng.integers(-2, 3, (q, n)).astype(float)
    a, b = cond5a(A, C, L), cond5a_plus(A, C, L)
    if a != b:
        d1 += 1
print(f"  不加前提：不一致 {d1}/1500")

d2 = 0
checked = 0
for _ in range(4000):
    n = int(rng.integers(2, 5))
    p = int(rng.integers(1, n))
    q = int(rng.integers(1, n))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L = rng.integers(-2, 3, (q, n)).astype(float)
    if not functionally_observable(A, C, L):
        continue
    checked += 1
    if cond5a(A, C, L) != cond5a_plus(A, C, L):
        d2 += 1
print(f"  功能可观前提下：不一致 {d2}/{checked}")

print()
print("=" * 78)
print("实验 4：(5b) 是否强于 (5a)？ 以及 (5b) 与 (A) 的关系")
print("=" * 78)
w = {"5b_no_5a": 0, "5a_no_5b": 0, "both": 0, "5b_no_A": 0, "A_no_5b": 0}
for _ in range(1200):
    n = int(rng.integers(2, 5))
    p = int(rng.integers(0, n))
    q = int(rng.integers(1, n))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L = rng.integers(-2, 3, (q, n)).astype(float)
    a, s, b = cond5a(A, C, L), cond5b(A, C, L), cond_A_contain(A, C, L)
    if s and not a:
        w["5b_no_5a"] += 1
    if a and not s:
        w["5a_no_5b"] += 1
    if a and s:
        w["both"] += 1
    if s and not b:
        w["5b_no_A"] += 1
    if b and not s:
        w["A_no_5b"] += 1
print("  ", w)
