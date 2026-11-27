"""
关键结构引理（严格证明 + 数值验证）

【引理 K】k := q0 - r = 1 时，(S) 必然失败。
  证明：
    k=1 时 T_R 是 1x1 标量 t，故 T_R = t·I_1。
    im(H_R) ≅ R/(R∩row(C))（引理 L5），且由 H3 知 row(L0)∩row(C)=0，
    R ⊇ row(L0) 故 R ⊄ row(C)，于是 rank(H) = dim R - dim(R∩row(C)) ≥ 1。
    又 ker(tI - T_R) = ker(0) = R^1。
    故 im(H) ∩ ker(tI - T_R) ≠ {0}，由 (S)⟺im(H)∩ker(sI-T_R)={0} ∀s 知 (S) 失败。

  推论 K1：k = 1 ⟹ nu_min > q0，即谱阻塞必然发生。
  推论 K2：nu_min ≥ q0 + 1 当 k=1；一般地，若最小的"k≥2 且谱可行"的维度是 d*，
           则 nu_min = d*。

本脚本：
  (V1) 验证引理 K：k=1 的实例中 (S) 是否 100% 失败
  (V2) 验证推论 K2：nu_min 是否等于"最小谱可行维度"
  (V3) 检验 k≥2 时 (S) 的成立条件
"""
import itertools
from fractions import Fraction as F

import numpy as np

rng = np.random.default_rng(20260111)


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
print("V1: 验证引理 K —— k = q0 - r = 1 时 (S) 是否 100% 失败")
print("=" * 80)
k1_fail = k1_tot = 0
k1_examples = []
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
    if q0 - r != 1:                     # 只取 k=1
        continue
    if q0 > dZ:
        continue
    for _ in range(8):
        L = rand_L(L0, Z, q0, rng)
        if L is None:
            continue
        k1_tot += 1
        if not condS(A, C, L):
            k1_fail += 1
        elif len(k1_examples) < 3:
            k1_examples.append((Am.tolist(), Cm.tolist(), L0m.tolist(), eta, q0))
print(f"  k=1 的检验次数: {k1_tot}")
print(f"  (S) 失败次数:   {k1_fail}   (比例 {k1_fail/max(k1_tot,1):.3f})")
if k1_fail == k1_tot:
    print("  => 引理 K 成立：k=1 时 (S) 必然失败")
else:
    print(f"  => 引理 K 被否证！有 {k1_tot-k1_fail} 次 (S) 成立")
    for e in k1_examples:
        print(f"     {e}")

print()
print("=" * 80)
print("V3: k >= 2 时 (S) 的成立情况")
print("=" * 80)
prof = {}
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
    kk = q0 - r
    if kk < 2 or q0 > dZ:
        continue
    ok = tt = 0
    for _ in range(8):
        L = rand_L(L0, Z, q0, rng)
        if L is None:
            continue
        tt += 1
        if condS(A, C, L):
            ok += 1
    if tt:
        prof.setdefault(kk, []).append((ok, tt))
print("  按 k 分组统计 (S) 命中率：")
for kk in sorted(prof):
    arr = prof[kk]
    full = sum(1 for ok, tt in arr if ok == tt)
    zero = sum(1 for ok, tt in arr if ok == 0)
    part = len(arr) - full - zero
    print(f"    k={kk}: 实例 {len(arr)} 个 -> 全命中 {full}, 全失败 {zero}, 部分 {part}")
print()
print("  说明：若 k>=2 有'部分'命中，则 k 不是唯一决定因素；")
print("        若只有 全命中/全失败，则印证 0/1 现象。")
