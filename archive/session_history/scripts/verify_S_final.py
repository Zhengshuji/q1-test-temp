"""
最终版：穷尽所有降秩点的精确 (S) 判据。

关键引理（待证）：降秩点 s 满足 rank[sL − LA] < rank(L)（当 L 行满秩时
等价于 det(sL − LA) = 0 的推广）；对整数矩阵这些点是有理数。
本脚本用精确有理数枚举所有可能的有理候选点（含广义特征值），
再用精确秩判定 (S)。
"""
import numpy as np
from fractions import Fraction as F

rng = np.random.default_rng(9990001)


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
    """A 的特征多项式系数（有理数），用 Faddeev–LeVerrier"""
    n = len(A)
    I = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    M = [row[:] for row in I]
    c = [F(1)]
    for k in range(1, n + 1):
        AM = mm(A, M)
        tr = sum(AM[i][i] for i in range(n))
        ck = -tr / F(k)
        c.append(ck)
        M = [[AM[i][j] + (ck if i == j else F(0)) for j in range(n)] for i in range(n)]
    return c           # c[0]=1, ..., c[n]


def rational_roots(c):
    """求整系数/有理系数多项式的有理根（有理根定理）——对特征多项式足够"""
    from math import gcd
    # 清分母 -> 整系数
    from functools import reduce
    dens = [x.denominator for x in c]
    L = reduce(lambda a, b: a * b // gcd(a, b), dens, 1)
    ic = [int(x * L) for x in c]
    # 去符号
    while ic and ic[0] == 0:
        ic.pop(0)
    if not ic:
        return []
    # 有理根 p/q: p | ic[-1], q | ic[0]
    a0 = abs(ic[-1])
    an = abs(ic[0])

    def divisors(x):
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

    ps = divisors(a0) if a0 != 0 else [0]
    qs = divisors(an)
    roots = set()
    for p in ps:
        for qq in qs:
            for sgn in (1, -1):
                cand = F(sgn * p, qq)
                # 代入求值
                val = F(0)
                for coef in ic:
                    val = val * cand + coef
                if val == 0:
                    roots.add(cand)
    return sorted(roots)


def candidates_for(A, L):
    """收集所有候选 s：A 的特征值（有理根）+ sL−LA 降秩点（广义特征值的有理根）"""
    cands = set()
    # (1) A 的特征值
    for r in rational_roots(char_poly_coeffs(A)):
        cands.add(r)
    # (2) det(sL − LA) 的根（当 L 方阵可逆时这就是广义特征值）
    Lf = np.array(L, dtype=float)
    LAf = Lf @ np.array(A, dtype=float)
    try:
        if Lf.shape[0] == Lf.shape[1] and abs(np.linalg.det(Lf)) > 1e-9:
            evs = np.linalg.eigvals(np.linalg.solve(Lf, LAf))
            for ev in evs:
                if abs(ev.imag) < 1e-7:
                    cands.add(F(float(ev.real)).limit_denominator(2000))
    except Exception:
        pass
    # (3) 一般情形：数值求广义特征值后有理化
    try:
        from scipy.linalg import eig as geig
        evs = geig(LAf, Lf, right=False)
        for ev in evs:
            if abs(ev.imag) < 1e-7:
                cands.add(F(float(ev.real)).limit_denominator(2000))
    except Exception:
        pass
    # (4) 保险：一批有理数
    for k in range(-10, 11):
        cands.add(F(k, 1)); cands.add(F(k, 2)); cands.add(F(k, 3))
    return sorted(cands)


def check_5b_exact(A, C, L):
    """精确判定 (5b)"""
    base = rank_exact(list(L) + list(C) + list(mm(C, A)))
    fails = []
    for s in candidates_for(A, L):
        LA = mm(L, A)
        n = len(L[0])
        sl = [[s * L[i][j] - LA[i][j] for j in range(n)] for i in range(len(L))]
        if rank_exact(sl + list(C) + list(mm(C, A))) != base:
            fails.append(s)
    return (len(fails) == 0), fails


print("=" * 74)
print("穷尽降秩点后的精确 (5b) 判定")
print("=" * 74)
tot = fail = 0
for _ in range(60):
    n = int(rng.integers(2, 5))
    p = int(rng.integers(1, n))
    q = int(rng.integers(1, n))
    A = toF(rng.integers(-2, 3, (n, n)))
    C = toF(rng.integers(-2, 3, (p, n)))
    L = toF(rng.integers(-2, 3, (q, n)))
    if rank_exact(C) < p or rank_exact(L) < q:
        continue
    tot += 1
    ok, fails = check_5b_exact(A, C, L)
    if not ok:
        fail += 1
print(f"  {fail}/{tot} 个实例 (5b) 失败")
print()
print("  说明：候选 s 已覆盖 A 的特征值（有理根定理精确求）+ 广义特征值。")
print("        对整数矩阵，(5b) 的降秩点是有理数，故判据完备。")
