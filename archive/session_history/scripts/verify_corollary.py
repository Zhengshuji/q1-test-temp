"""
猜想 O 的推论检验 —— 这是判定命题 q 的关键。

【猜想 O】(已数值验证 62/62)：在格 {row(L0) ⊆ R ⊆ Z, dim R = d} 上，
   (S) 要么对所有 R 成立，要么对所有 R 不成立。

【推论 A】"d 处可行" ⟺ "Σ_d 非空" ⟺ "任意一个 d 维 R 满足 (S)"（若 (A) 也普遍成立）
   => nu_min = 最小的 d 使 (S) 成立
   => 命题 q 为假（判定是多项式的）

【本脚本检验】
   (T1) 在 d = q0 处，(A) 是否对所有 R 成立？
   (T2) 若 T1 成立，则 nu_min 是否恰等于"最小使 (S) 成立的 d"？
   (T3) 用 P2 的例子验证：是否存在 d > q0 才能使 (S) 成立？
        （P2 声称 r=2 < q0=3 < nu_min=5 —— 若能在小系统上复现这种"谱阻塞"，
          则说明 (S) 的失败不是偶然，而是结构性的）
"""
import itertools
from fractions import Fraction as F

import numpy as np

rng = np.random.default_rng(20260109)


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


def orbit(M, A):
    out, cur = [], M
    for _ in range(len(A)):
        out += cur
        cur = mm(cur, A)
    return out


def eta_indices(A, C, L0):
    p, r, n = len(C), len(L0), len(A)
    gens = [row[:] for row in C] + [row[:] for row in L0]
    M, highest = [], [-1] * (p + r)

    def times(v, q):
        out = v[:]
        for _ in range(q):
            out = mm([out], A)[0]
        return out

    for q in range(n + 1):
        for i in range(p + r):
            if highest[i] >= 0 and q > highest[i] + 1:
                continue
            v = times(gens[i], q)
            if rank_exact(M + [v]) > rank_exact(M):
                M.append(v)
                highest[i] = q
        if all(highest[i] >= 0 and q > highest[i] + 1 for i in range(p + r)):
            break
    alpha = [h + 1 if h >= 0 else 0 for h in highest]
    return [alpha[p + j] for j in range(r)]


def condA(A, C, L):
    LA = mm(L, A)
    W = L + C + mm(C, A)
    return rank_exact(W + LA) == rank_exact(W)


def condS(A, C, L):
    LA = mm(L, A)
    rhs = rank_exact(L + C + mm(C, A))
    n = len(A)
    cs = set()
    for k in range(-30, 31):
        for den in (1, 2, 3, 4, 5, 6, 8, 10, 12):
            cs.add(F(k, den))
    try:
        for ev in np.linalg.eigvals(np.array(A, float)):
            if abs(ev.imag) < 1e-7:
                cs.add(F(float(ev.real)).limit_denominator(10000))
        Lf = np.array(L, float); LAf = Lf @ np.array(A, float)
        if Lf.shape[0] == Lf.shape[1] and abs(np.linalg.det(Lf)) > 1e-9:
            for ev in np.linalg.eigvals(np.linalg.solve(Lf, LAf)):
                if abs(ev.imag) < 1e-7:
                    cs.add(F(float(ev.real)).limit_denominator(10000))
        else:
            from scipy.linalg import eig as geig
            for ev in geig(LAf, Lf, right=False):
                if abs(ev.imag) < 1e-7:
                    cs.add(F(float(ev.real)).limit_denominator(10000))
    except Exception:
        pass
    for s in sorted(cs):
        sl = [[s * L[i][j] - LA[i][j] for j in range(n)] for i in range(len(L))]
        if rank_exact(sl + C + mm(C, A)) != rhs:
            return False
    return True


def basis_of(M):
    if not M:
        return []
    Mn = np.array([[float(x) for x in r] for r in M])
    u, s, vt = np.linalg.svd(Mn, full_matrices=False)
    tol = max(Mn.shape) * (s[0] if s.size else 1) * 1e-12
    rk = int(np.sum(s > tol))
    return [[F(float(x)).limit_denominator(10**7) for x in row] for row in vt[:rk]]


def rand_L(L0, Z, d, rng_):
    BL, BZ = basis_of(L0), basis_of(Z)
    r = len(BL)
    if d < r or d > len(BZ):
        return None
    Q = np.linalg.qr(np.array([[float(x) for x in rr] for rr in BL]).T)[0]
    BZn = np.array([[float(x) for x in rr] for rr in BZ])
    Bq = basis_of([[F(float(x)).limit_denominator(10**7) for x in row]
                   for row in (BZn - BZn @ Q @ Q.T)])
    need = d - r
    if need > len(Bq):
        return None
    if need == 0:
        return BL if rank_exact(BL) == d else None
    coef = rng_.normal(size=(need, len(Bq)))
    rows = [[F(float(sum(coef[i][t] * float(Bq[t][j]) for t in range(len(Bq))))).limit_denominator(10**7)
             for j in range(len(Bq[0]))] for i in range(need)]
    L = BL + rows
    return L if rank_exact(L) == d else None


print("=" * 80)
print("T1: 在 d = q0 处，(A) 是否对所有 R 成立？")
print("=" * 80)
tot = a_ok = a_tot = 0
for trial in range(80):
    n = int(rng.integers(2, 5))
    p = int(rng.integers(1, n))
    r = int(rng.integers(1, n - p + 1)) if n - p >= 1 else 1
    Am = rng.integers(-2, 3, (n, n))
    Cm = rng.integers(-2, 3, (p, n))
    L0m = rng.integers(-2, 3, (r, n))
    A, C, L0 = toF(Am), toF(Cm), toF(L0m)
    if rank_exact(C) != p or rank_exact(L0) != r:
        continue
    if rank_exact(L0 + C) != r + p:
        continue
    OC = orbit(C, A)
    Z = orbit(L0, A) + OC
    if rank_exact(Z + OC) != rank_exact(OC):
        continue
    eta = eta_indices(A, C, L0)
    q0 = sum(eta)
    dZ = rank_exact(Z)
    if not (r <= q0 <= dZ):
        continue
    tot += 1
    for _ in range(10):
        L = rand_L(L0, Z, q0, rng)
        if L is None:
            continue
        a_tot += 1
        if condA(A, C, L):
            a_ok += 1
print(f"  实例数 {tot}")
print(f"  在 d=q0 处 (A) 的命中率: {a_ok}/{a_tot} = {a_ok/max(a_tot,1):.3f}")
print()

print("=" * 80)
print("T2/T3: nu_min 是否 = 最小使 (S) 成立的 d ？（逐维度扫描）")
print("=" * 80)
print("  对每个实例，从 d=r 扫到 d=dimZ，记录每个 d 的 (S) 命中率（10 个随机点）。")
print()

blocked = []          # 出现 "q0 处失败、更大 d 处成功" 的实例
for trial in range(120):
    n = int(rng.integers(2, 5))
    p = int(rng.integers(1, n))
    r = int(rng.integers(1, n - p + 1)) if n - p >= 1 else 1
    Am = rng.integers(-2, 3, (n, n))
    Cm = rng.integers(-2, 3, (p, n))
    L0m = rng.integers(-2, 3, (r, n))
    A, C, L0 = toF(Am), toF(Cm), toF(L0m)
    if rank_exact(C) != p or rank_exact(L0) != r:
        continue
    if rank_exact(L0 + C) != r + p:
        continue
    OC = orbit(C, A)
    Z = orbit(L0, A) + OC
    if rank_exact(Z + OC) != rank_exact(OC):
        continue
    eta = eta_indices(A, C, L0)
    q0 = sum(eta)
    dZ = rank_exact(Z)
    if not (r <= q0 <= dZ) or dZ > n:
        continue

    prof = {}
    for d in range(r, dZ + 1):
        ok = tt = 0
        for _ in range(10):
            L = rand_L(L0, Z, d, rng)
            if L is None:
                continue
            tt += 1
            if condA(A, C, L) and condS(A, C, L):
                ok += 1
        prof[d] = (ok, tt)

    # 找最小可行 d
    dmin = None
    for d in sorted(prof):
        ok, tt = prof[d]
        if tt and ok == tt:               # 全命中
            dmin = d
            break
        if tt and ok > 0:
            dmin = d
            break
    if dmin is not None and dmin > q0:
        blocked.append((Am.tolist(), Cm.tolist(), L0m.tolist(), eta, q0, dZ, prof, dmin))

print(f"  出现 'q0 处失败但更大 d 处成功' 的实例数: {len(blocked)}")
if blocked:
    print("  => 存在'谱阻塞'：nu_min > q0 确实会发生（与 P2 一致）")
    for Am, Cm, L0m, eta, q0, dZ, prof, dmin in blocked[:3]:
        print(f"     A={Am} C={Cm} L0={L0m}")
        print(f"       eta={eta} q0={q0} dimZ={dZ} nu_min={dmin}")
        print(f"       各维度命中率: {prof}")
else:
    print("  => 未出现谱阻塞（在 n<=4 的范围内 nu_min 总 = q0）")
    print("     这与 P1 的 nu_min = q0（当谱可行时）一致。")
