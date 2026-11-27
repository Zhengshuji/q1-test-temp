"""
用【正确的 (5b) 判据】重新验证算法。

正确判据：候选 s 必须覆盖
  (i)  A 的特征值（有理根定理精确求）
  (ii) 使 sL − LA 降秩的点（广义特征值）
  (iii) 一批有理数保险
然后在该候选集上逐点精确判定秩。

（此前算法验证用的是只含少量采样点的判据，可能误判。）
"""
import itertools

import numpy as np
from fractions import Fraction as F

rng = np.random.default_rng(424242)


def rref(M):
    M = [row[:] for row in M]
    if not M:
        return M, []
    nrow, ncol = len(M), len(M[0])
    piv, r = [], 0
    for c in range(ncol):
        p = None
        for i in range(r, nrow):
            if M[i][c] != 0:
                p = i; break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(nrow):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c); r += 1
        if r == nrow:
            break
    return M, piv


def rank_exact(M):
    if not M or not M[0]:
        return 0
    return len(rref(M)[1])


def mm(X, Y):
    if not X or not Y:
        return []
    n, k, m = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def toF(M):
    return [[F(int(x)) for x in row] for row in M]


def char_poly_coeffs(A):
    n = len(A)
    M = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    c = [F(1)]
    for k in range(1, n + 1):
        AM = mm(A, M)
        tr = sum(AM[i][i] for i in range(n))
        ck = -tr / F(k)
        c.append(ck)
        M = [[AM[i][j] + (ck if i == j else F(0)) for j in range(n)] for i in range(n)]
    return c


def rational_roots(c):
    from functools import reduce
    from math import gcd
    dens = [x.denominator for x in c]
    L = reduce(lambda a, b: a * b // gcd(a, b), dens, 1)
    ic = [int(x * L) for x in c]
    while ic and ic[0] == 0:
        ic.pop(0)
    if not ic:
        return []
    a0, an = abs(ic[-1]), abs(ic[0])

    def divs(x):
        if x == 0:
            return [1]
        d = []
        i = 1
        while i * i <= x:
            if x % i == 0:
                d.append(i)
                if i != x // i:
                    d.append(x // i)
            i += 1
        return sorted(set(d))

    roots = set()
    for p in (divs(a0) if a0 else [0]):
        for q in divs(an):
            for sg in (1, -1):
                cand = F(sg * p, q)
                val = F(0)
                for coef in ic:
                    val = val * cand + coef
                if val == 0:
                    roots.add(cand)
    return sorted(roots)


def candidates(A, L):
    c = set()
    for r in rational_roots(char_poly_coeffs(A)):
        c.add(r)
    Lf = np.array(L, dtype=float)
    LAf = Lf @ np.array(A, dtype=float)
    try:
        if Lf.shape[0] == Lf.shape[1] and abs(np.linalg.det(Lf)) > 1e-9:
            for ev in np.linalg.eigvals(np.linalg.solve(Lf, LAf)):
                if abs(ev.imag) < 1e-7:
                    c.add(F(float(ev.real)).limit_denominator(2000))
    except Exception:
        pass
    try:
        from scipy.linalg import eig as geig
        for ev in geig(LAf, Lf, right=False):
            if abs(ev.imag) < 1e-7:
                c.add(F(float(ev.real)).limit_denominator(2000))
    except Exception:
        pass
    for k in range(-6, 7):
        c.add(F(k)); c.add(F(k, 2)); c.add(F(k, 3))
    return sorted(c)


def condA_exact(A, C, L):
    """row(LA) ⊆ row(L, C, CA)，精确判定"""
    LA = mm(L, A)
    W = list(L) + list(C) + list(mm(C, A))
    return rank_exact(W + LA) == rank_exact(W)


def condS_exact(A, C, L):
    base = rank_exact(list(L) + list(C) + list(mm(C, A)))
    LA = mm(L, A)
    n = len(L[0])
    for s in candidates(A, L):
        sl = [[s * L[i][j] - LA[i][j] for j in range(n)] for i in range(len(L))]
        if rank_exact(sl + list(C) + list(mm(C, A))) != base:
            return False
    return True


def both(A, C, L):
    return condA_exact(A, C, L) and condS_exact(A, C, L)


# ---------- 独立对照：网格穷举（小规模）----------
def brute(A, C, L0, cap=3):
    n = len(A)
    I = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    pool = [row[:] for row in I]
    for v in itertools.product((-1, 0, 1), repeat=n):
        if any(v):
            pool.append([F(x) for x in v])
    for k in range(0, cap + 1):
        for combo in itertools.combinations(range(len(pool)), k):
            R = [pool[i] for i in combo]
            L = L0 + R
            if both(A, C, L):
                return len(L)
    return None


# ---------- 算法：随机子空间 ----------
def rand_L(L0, Z, d):
    def basis_of(M):
        if not M:
            return []
        Mnp = np.array([[float(x) for x in r] for r in M])
        u, s, vt = np.linalg.svd(Mnp, full_matrices=False)
        tol = max(Mnp.shape) * (s[0] if s.size else 1) * 1e-12
        rk = int(np.sum(s > tol))
        return [[F(float(x)).limit_denominator(10**6) for x in row] for row in vt[:rk]]
    BL, BZ = basis_of(L0), basis_of(Z)
    r = len(BL)
    if d < r or d > len(BZ):
        return None
    Q = np.linalg.qr(np.array([[float(x) for x in r_] for r_ in BL]).T)[0]
    BZn = np.array([[float(x) for x in r_] for r_ in BZ])
    resid = BZn - BZn @ Q @ Q.T
    Bq = basis_of([[F(float(x)).limit_denominator(10**6) for x in row] for row in resid])
    need = d - r
    if need > len(Bq):
        return None
    coef = rng.normal(size=(need, len(Bq)))
    rows = [[F(float(sum(coef[i][t] * float(Bq[t][j]) for t in range(len(Bq))))).limit_denominator(10**6)
             for j in range(len(Bq[0]))] for i in range(need)]
    L = BL + rows
    return L if rank_exact(L) == d else None


def orbit(M, A):
    out, cur = [], M
    n = len(A)
    for _ in range(n):
        out += cur
        cur = mm(cur, A)
    return out


print("=" * 76)
print("用正确 (5b) 判据重新验证：算法 vs 穷举")
print("=" * 76)
ok = bad = skip = 0
mism = []
for trial in range(40):
    n = 3
    p = int(rng.integers(1, n))
    q = int(rng.integers(1, n - p + 1)) if n - p >= 1 else 1
    A = toF(rng.integers(-1, 2, (n, n)))
    C = toF(rng.integers(-1, 2, (p, n)))
    L0 = toF(rng.integers(-1, 2, (q, n)))
    if rank_exact(C) < p or rank_exact(L0) < q:
        continue
    Z = orbit(L0, A) + orbit(C, A)
    dZ = rank_exact(Z)
    bf = brute(A, C, L0, cap=3)
    if bf is None:
        skip += 1
        continue
    # 算法：从 r 到 dZ 找最小可行
    alg = None
    for d in range(q, dZ + 1):
        for _ in range(8):
            L = rand_L(L0, Z, d)
            if L is None:
                continue
            if both(A, C, L):
                alg = len(L)
                break
        if alg is not None:
            break
    if alg is None:
        alg = dZ + 1     # 未找到
    if alg == bf:
        ok += 1
    else:
        bad += 1
        mism.append((A, C, L0, alg, bf))

print(f"  一致 {ok}，不一致 {bad}，跳过 {skip}")
for A, C, L0, a, b in mism[:4]:
    print(f"    算法={a} 穷举={b}")
    print(f"      A={[[str(x) for x in r] for r in A]}")
    print(f"      C={[[str(x) for x in r] for r in C]}  L0={[[str(x) for x in r] for r in L0]}")
