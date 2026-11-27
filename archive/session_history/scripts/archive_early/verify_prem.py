"""
复验子代理的反例，并测试"加前提 rank[L0;C]=p+r 后公式是否成立"。

反例：A=[[-1,-1,-2],[-2,-1,0],[-1,-2,0]], C=[[1,0,0]], L0=[[1,0,0]]
  预期：dim Z=3, dim V=2 → 公式给 k=1，但 R=0 已满足 (5a)(5b)
"""
import itertools

import numpy as np

TOL = 1e-7
rng = np.random.default_rng(999)


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


def cond5a(A, C, L):
    """4 块版本"""
    return rk(st(L @ A, L, C @ A, C)) == rk(st(L, C @ A, C))


def cond5b(A, C, L, npts=25):
    """严格 (S)：rank[sL-LA; CA; C] == rank[L; CA; C] 对所有 s"""
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
    return rk(Z), rk(V)


print("=" * 74)
print("E1 : 复现子代理的反例")
print("=" * 74)
A = np.array([[-1., -1., -2.], [-2., -1., 0.], [-1., -2., 0.]])
C = np.array([[1., 0., 0.]])
L0 = np.array([[1., 0., 0.]])
dz, dv = ZV(A, C, L0)
print(f"  dim Z = {dz}, dim V = {dv}  => 公式 k = {dz - dv}")
print(f"  rank[L0;C] = {rk(st(L0, C))}   (要求 p+r = {C.shape[0]}+{L0.shape[0]} = {C.shape[0]+L0.shape[0]})")
print(f"  (5a) with R=0 : {cond5a(A, C, L0)}")
print(f"  (5b) with R=0 : {cond5b(A, C, L0)}")
print(f"  L0A = {L0 @ A},  CA = {C @ A},  相等? {np.allclose(L0@A, C@A)}")
print("  -> 反例成立：公式（无前提）给 1，实际最小是 0")

print()
print("=" * 74)
print("E2 : 加前提 rank[L0;C]=p+r 后，公式 vs 穷举最优")
print("=" * 74)


def brute_min(A, C, L0, cap=3):
    n = A.shape[1]
    grid = [np.array(v, float) for v in itertools.product(range(-2, 3), repeat=n) if any(v)]
    for k in range(0, cap + 1):
        for combo in itertools.combinations_with_replacement(range(len(grid)), k):
            R = np.array([grid[i] for i in combo]) if k else np.zeros((0, n))
            L = st(L0, R)
            if cond5a(A, C, L) and cond5b(A, C, L):
                return k
    return None


res = {"with_prem_ok": 0, "with_prem_bad": 0, "no_prem_ok": 0, "no_prem_bad": 0}
examples_with = []
for _ in range(3000):
    n = int(rng.integers(2, 4))
    p = int(rng.integers(1, n))
    q = int(rng.integers(1, n - p + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L0 = rng.integers(-2, 3, (q, n)).astype(float)
    if rk(C) < p or rk(L0) < q:
        continue
    dz, dv = ZV(A, C, L0)
    formula = dz - dv
    prem = (rk(st(L0, C)) == p + q)
    truth = brute_min(A, C, L0, cap=min(3, n))
    if truth is None:
        continue
    if prem:
        if formula == truth:
            res["with_prem_ok"] += 1
        else:
            res["with_prem_bad"] += 1
            if len(examples_with) < 3:
                examples_with.append((A.copy(), C.copy(), L0.copy(), formula, truth))
    else:
        if formula == truth:
            res["no_prem_ok"] += 1
        else:
            res["no_prem_bad"] += 1

print("  ", res)
print("  -> 有前提时 formula 与穷举一致的比率：",
      f"{res['with_prem_ok']}/{res['with_prem_ok']+res['with_prem_bad']}")
print("  -> 无前提时 formula 与穷举一致的比率：",
      f"{res['no_prem_ok']}/{res['no_prem_ok']+res['no_prem_bad']}")
for A_, C_, L0_, f_, t_ in examples_with:
    print("   有前提的反例: formula=%s truth=%s" % (f_, t_))
    print("     A=", A_.tolist(), " C=", C_.tolist(), " L0=", L0_.tolist())

print()
print("=" * 74)
print("E3 : k=0 的刻画：只验 row(L0A) ⊆ row(L0,C,CA)")
print("=" * 74)
ok = bad = 0
for _ in range(1500):
    n = int(rng.integers(2, 5))
    p = int(rng.integers(0, n + 1))
    q = int(rng.integers(1, n + 1))
    A = rng.integers(-2, 3, (n, n)).astype(float)
    C = rng.integers(-2, 3, (p, n)).astype(float)
    L0 = rng.integers(-2, 3, (q, n)).astype(float)
    dz, dv = ZV(A, C, L0)
    a = (dz == dv)
    b = in_span(L0 @ A, st(L0, C, C @ A))
    if a == b:
        ok += 1
    else:
        bad += 1
        if bad <= 3:
            print(f"   不一致: dimZ={dz} dimV={dv}  row(L0A)⊆V={b}")
print(f"   'Z=V' 与 'row(L0A)⊆V' 一致 {ok}, 不一致 {bad}")
print("   -> 子代理说下半句 '⟺ Z=V' 是假的；这里看是否成立")
