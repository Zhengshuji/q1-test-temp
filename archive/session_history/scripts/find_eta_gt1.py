"""
寻找 eta_j > 1 的非平凡例子，验证 nu_min = q0。

eta_j > 1 意味着 L_j A 不在 row(L0, C) 中 —— 这需要 C 不覆盖 L0 的 A-像。
但要满足 H3（rank[L0;C]=r+p）与 H4（功能可观）。
"""
import itertools
from fractions import Fraction as F

import numpy as np


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


def times_A(v, A, q):
    r = v[:]
    for _ in range(q):
        r = mm([r], A)[0]
    return r


def eta_indices(A, C, L0):
    p, r, n = len(C), len(L0), len(A)
    gens = [row[:] for row in C] + [row[:] for row in L0]
    M, highest = [], [-1] * (p + r)
    for q in range(n + 1):
        for i in range(p + r):
            if highest[i] >= 0 and q > highest[i] + 1:
                continue
            v = times_A(gens[i], A, q)
            if rank_exact(M + [v]) > rank_exact(M):
                M.append(v)
                highest[i] = q
        if all(highest[i] >= 0 and q > highest[i] + 1 for i in range(p + r)):
            break
    alpha = [h + 1 if h >= 0 else 0 for h in highest]
    return [alpha[p + j] for j in range(r)]


def orbit(M, A):
    out, cur = [], M
    for _ in range(len(A)):
        out += cur
        cur = mm(cur, A)
    return out


def condA(A, C, L):
    LA = mm(L, A)
    W = L + C + mm(C, A)
    return rank_exact(W + LA) == rank_exact(W)


def condS(A, C, L):
    LA = mm(L, A)
    rhs = rank_exact(L + C + mm(C, A))
    n = len(A)
    cs = set()
    for k in range(-20, 21):
        for den in (1, 2, 3, 4, 5, 6):
            cs.add(F(k, den))
    try:
        for ev in np.linalg.eigvals(np.array(A, float)):
            if abs(ev.imag) < 1e-7:
                cs.add(F(float(ev.real)).limit_denominator(4000))
        Lf = np.array(L, float); LAf = Lf @ np.array(A, float)
        if Lf.shape[0] == Lf.shape[1] and abs(np.linalg.det(Lf)) > 1e-9:
            for ev in np.linalg.eigvals(np.linalg.solve(Lf, LAf)):
                if abs(ev.imag) < 1e-7:
                    cs.add(F(float(ev.real)).limit_denominator(4000))
        else:
            from scipy.linalg import eig as geig
            for ev in geig(LAf, Lf, right=False):
                if abs(ev.imag) < 1e-7:
                    cs.add(F(float(ev.real)).limit_denominator(4000))
    except Exception:
        pass
    for s in sorted(cs):
        sl = [[s * L[i][j] - LA[i][j] for j in range(n)] for i in range(len(L))]
        if rank_exact(sl + C + mm(C, A)) != rhs:
            return False
    return True


def nu_min_bf(A, C, L0, cap):
    n, r = len(A), len(L0)
    I = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    pool = [row[:] for row in I] + [[F(v) for v in p]
                                    for p in itertools.product((-1, 0, 1), repeat=n) if any(p)]
    for d in range(r, min(cap, n) + 1):
        for combo in itertools.combinations(range(len(pool)), d - r):
            L = L0 + [pool[i] for i in combo]
            if rank_exact(L) != d:
                continue
            if condA(A, C, L) and condS(A, C, L):
                return d
    return None


print("=" * 78)
print("寻找 eta > 1 的例子（n=3）")
print("=" * 78)
rng = np.random.default_rng(2024)
found = []
tried = 0
for _ in range(400):
    n = 3
    Am = rng.integers(-2, 3, (n, n)).tolist()
    Cm = rng.integers(-2, 3, (1, n)).tolist()
    L0m = rng.integers(-2, 3, (1, n)).tolist()
    A, C, L0 = toF(Am), toF(Cm), toF(L0m)
    if rank_exact(C) != 1 or rank_exact(L0) != 1:
        continue
    if rank_exact(L0 + C) != 2:
        continue
    OC = orbit(C, A)
    Z = orbit(L0, A) + OC
    if rank_exact(Z + OC) != rank_exact(OC):
        continue                                    # H4
    eta = eta_indices(A, C, L0)
    if sum(eta) <= 1:
        continue                                    # 只找 eta>1
    tried += 1
    nm = nu_min_bf(A, C, L0, cap=3)
    if nm is not None:
        found.append((Am, Cm, L0m, eta, sum(eta), nm))
    if len(found) >= 6:
        break

print(f"  满足 H1-H4 且 eta>1 的实例数: {len(found)}")
print()
for Am, Cm, L0m, eta, q0, nm in found:
    tag = "一致 ✓" if nm == q0 else f"**不一致** (nu_min={nm}, q0={q0})"
    print(f"  A={Am} C={Cm} L0={L0m}")
    print(f"     eta={eta}  q0={q0}  nu_min(穷举)={nm}   {tag}")
print()
print("  若全部一致，则 P1 断言 nu_min = q0 在这个范围内成立。")
