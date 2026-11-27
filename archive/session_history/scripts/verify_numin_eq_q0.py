"""
验证 P1 的断言 nu_min = q0（在满足 H1-H4 的前提下）。

q0 = sum_j eta_j，其中 eta_j 是功能可观性指数，
按 P1 §III 的"全局有序秩保留"构造读出。

构造（P1 §III-A）：
  生成元 g_1..g_{p+r} = C 的各行, L0 的各行
  全局顺序：g_1..g_{p+r}; g_1 A..g_{p+r} A; g_1 A^2.. ...
  逐行做秩保留；alpha_i = 1 + max{ q : g_i A^q 被保留 }
  eta_j = alpha_{p+j}
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


def functional_observability_indices(A, C, L0):
    """P1 §III 的全局有序秩保留构造 -> alpha_i -> eta_j"""
    p, r = len(C), len(L0)
    n = len(A)
    gens = [row[:] for row in C] + [row[:] for row in L0]
    M = []                      # 已保留行
    highest = [-1] * (p + r)    # 每个生成元已保留的最高幂次
    info = []                   # (generator index, power)
    for q in range(n + 1):
        for i in range(p + r):
            if highest[i] >= 0 and q > highest[i] + 1:
                continue        # 已遇依赖，后续全依赖（P1 Lemma 1）
            g = gens[i]
            v = g if q == 0 else mm([g], np.linalg.matrix_power(np.array(A, float), q).tolist())[0]
            # 用精确幂：直接连乘
            v = g[:]
            for _ in range(q):
                v = mm([v], A)[0]
            if rank_exact(M + [v]) > rank_exact(M):
                M.append(v)
                info.append((i, q))
                highest[i] = q
        # 终止条件
        if all(highest[i] >= 0 and q > highest[i] + 1 for i in range(p + r)):
            break
    alpha = [h + 1 if h >= 0 else 0 for h in highest]
    eta = [alpha[p + j] for j in range(r)]
    return eta, sum(eta), M, info


def nullspace_exact(M):
    if not M:
        return []
    n = len(M[0])
    R, piv = rref(M)
    free = [c for c in range(n) if c not in piv]
    out = []
    for fc in free:
        v = [F(0)] * n
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][fc]
        out.append(v)
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
    for k in range(-14, 15):
        cs.add(F(k)); cs.add(F(k, 2)); cs.add(F(k, 3)); cs.add(F(k, 4)); cs.add(F(k, 5))
    try:
        for ev in np.linalg.eigvals(np.array(A, float)):
            if abs(ev.imag) < 1e-7:
                cs.add(F(float(ev.real)).limit_denominator(2000))
        Lf = np.array(L, float); LAf = Lf @ np.array(A, float)
        if Lf.shape[0] == Lf.shape[1] and abs(np.linalg.det(Lf)) > 1e-9:
            for ev in np.linalg.eigvals(np.linalg.solve(Lf, LAf)):
                if abs(ev.imag) < 1e-7:
                    cs.add(F(float(ev.real)).limit_denominator(2000))
        else:
            from scipy.linalg import eig as geig
            for ev in geig(LAf, Lf, right=False):
                if abs(ev.imag) < 1e-7:
                    cs.add(F(float(ev.real)).limit_denominator(2000))
    except Exception:
        pass
    for s in sorted(cs):
        sl = [[s * L[i][j] - LA[i][j] for j in range(n)] for i in range(len(L))]
        if rank_exact(sl + C + mm(C, A)) != rhs:
            return False
    return True


def orbit(M, A):
    out, cur = [], M
    for _ in range(len(A)):
        out += cur
        cur = mm(cur, A)
    return out


def nu_min_bruteforce(A, C, L0, cap=3):
    """穷举最小 d（小规模）"""
    n = len(A)
    r = len(L0)
    I = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    pool = [row[:] for row in I] + [[F(v) for v in p]
                                    for p in itertools.product((-1, 0, 1), repeat=n) if any(p)]
    for d in range(r, min(cap, n) + 1):
        kr = d - r
        for combo in itertools.combinations(range(len(pool)), kr):
            L = L0 + [pool[i] for i in combo]
            if rank_exact(L) != d:
                continue
            if condA(A, C, L) and condS(A, C, L):
                return d
    return None


print("=" * 78)
print("验证 P1 断言：nu_min = q0   （在 H1-H4 前提下）")
print("=" * 78)
print()

cases = [
    ("例1", [[1, 1], [0, 2]], [[1, 0]], [[0, 1]]),
    ("例2", [[1, 0], [0, 2]], [[1, 1]], [[1, -1]]),
    ("例3", [[0, 1], [0, 0]], [[1, 0]], [[0, 1]]),
    ("例4", [[1, 0], [0, 2]], [[1, 1]], [[0, 1]]),
    ("例5", [[1, 1], [0, 1]], [[1, 0]], [[0, 1]]),
]

for name, Am, Cm, L0m in cases:
    A, C, L0 = toF(Am), toF(Cm), toF(L0m)
    n = len(A)
    p, r = len(C), len(L0)
    rk_C, rk_L = rank_exact(C), rank_exact(L0)
    rk_CL = rank_exact(L0 + C)
    OC = orbit(C, A)
    Z = orbit(L0, A) + OC
    fobs = rank_exact(Z + OC) == rank_exact(OC)
    eta, q0, M, info = functional_observability_indices(A, C, L0)
    numin = nu_min_bruteforce(A, C, L0, cap=min(3, n))

    print(f"  {name}: A={Am}  C={Cm}  L0={L0m}")
    print(f"     H1 rank(C)={rk_C}=p? {rk_C==p}   H2 rank(L0)={rk_L}=r? {rk_L==r}   "
          f"H3 rank[L0;C]={rk_CL}={r+p}? {rk_CL==r+p}   H4 fobs? {fobs}")
    print(f"     eta = {eta}   q0 = sum eta = {q0}    nu_min(穷举) = {numin}")
    if fobs and rk_CL == r + p and numin is not None:
        verdict = "一致 ✓" if numin == q0 else f"**不一致** (nu_min={numin}, q0={q0})"
        print(f"     => nu_min vs q0: {verdict}")
    print()
