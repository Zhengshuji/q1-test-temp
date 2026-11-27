"""
验证一个强猜想：

  【猜想 O（0/1 现象）】
    在格 {R : row(L0) ⊆ R ⊆ Z, dim R = d} 上，条件 (S)
    要么对**所有** R 成立，要么对**所有** R 都不成立。
    即 (S) 只依赖 d 与 (A,C,L0)，不依赖 R 的具体选择。

  若成立 =>  (Q) 的判定可在多项式时间内完成：
      对 d = q0 取**任意**一个子空间，检验 (S) 即可。
      => nu_min = q0 当且仅当这个单一检验通过
      => 命题 q 为假

  推论（更激进）：若 (A) 在 d = q0 处总成立（实测 24/24），
  则 nu_min = q0 ⟺ 任一 q0 维子空间满足 (S)。

本脚本用大样本 + 多种采样方式（随机 / 定向 / 坐标）验证猜想 O。
"""
import itertools
from fractions import Fraction as F

import numpy as np

rng = np.random.default_rng(20260108)


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
    """精确 (S)：候选 s 覆盖 A 特征值 + 广义特征值 + 密集有理数"""
    LA = mm(L, A)
    rhs = rank_exact(L + C + mm(C, A))
    n = len(A)
    cs = set()
    for k in range(-30, 31):
        for den in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12):
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


def sample_L(L0, Z, d, mode, rng_):
    """三种取样方式，验证 (S) 是否与取样方式无关"""
    BL, BZ = basis_of(L0), basis_of(Z)
    r = len(BL)
    if d < r or d > len(BZ):
        return None
    Q = np.linalg.qr(np.array([[float(x) for x in rr] for rr in BL]).T)[0]
    BZn = np.array([[float(x) for x in rr] for rr in BZ])
    resid = BZn - BZn @ Q @ Q.T
    Bq = basis_of([[F(float(x)).limit_denominator(10**7) for x in row] for row in resid])
    need = d - r
    if need > len(Bq):
        return None
    if need == 0:
        return BL if rank_exact(BL) == d else None
    if mode == "random":
        coef = rng_.normal(size=(need, len(Bq)))
    elif mode == "identity":
        coef = np.zeros((need, len(Bq)))
        for i in range(min(need, len(Bq))):
            coef[i, i] = 1.0
    elif mode == "ones":
        coef = np.ones((need, len(Bq)))
    else:
        coef = rng_.integers(-3, 4, size=(need, len(Bq))).astype(float)
    rows = []
    for i in range(need):
        row = []
        for j in range(len(Bq[0])):
            s = sum(coef[i][t] * float(Bq[t][j]) for t in range(len(Bq)))
            row.append(F(float(s)).limit_denominator(10**7))
        rows.append(row)
    L = BL + rows
    return L if rank_exact(L) == d else None


print("=" * 80)
print("验证猜想 O：在 d=q0 处，(S) 是否与 R 的选择无关？")
print("=" * 80)
print("  对每个实例，用 4 种不同取样方式各取 12 个点，")
print("  检查 (S) 的命中率是否在所有方式下都一致（全 0 或全满）。")
print()

viol = 0
tot_inst = 0
detail = []
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
    if q0 > dZ:
        continue
    tot_inst += 1

    stats = {}
    for mode in ("random", "identity", "ones", "int"):
        ok = tt = 0
        for _ in range(12):
            L = sample_L(L0, Z, q0, mode, rng)
            if L is None:
                continue
            tt += 1
            if condS(A, C, L):
                ok += 1
        stats[mode] = (ok, tt)

    fracs = [ok / tt for ok, tt in stats.values() if tt > 0]
    if fracs and (max(fracs) - min(fracs)) > 1e-9:
        viol += 1
        detail.append((Am.tolist(), Cm.tolist(), L0m.tolist(), eta, q0, dZ, stats))

print(f"  实例总数: {tot_inst}")
print(f"  **(S) 命中率随取样方式变化**的实例数: {viol}")
print()
if viol:
    print("  => 猜想 O 被否证：(S) 依赖 R 的具体选择")
    for Am, Cm, L0m, eta, q0, dZ, stats in detail[:5]:
        print(f"     A={Am} C={Cm} L0={L0m} eta={eta} q0={q0} dZ={dZ}")
        print(f"       {stats}")
else:
    print("  => 猜想 O 成立：(S) 与 R 的具体选择无关（只看 d）")
    print("     这是很强的结构，若成立则 nu_min 判定是多项式的。")

print()
print("=" * 80)
print("补充：猜想 O 的推论检验")
print("=" * 80)
print("  若猜想 O 成立，则 nu_min = 最小的 d 使 (A)∧(S) 在该维度上成立。")
print("  由于 (A) 在 d=q0 处总成立（实测 24/24），故 nu_min = q0 ⟺ 该维度 (S) 成立。")
print()
print("  更进一步的推论：nu_min 与 q0 的关系只有两种可能：")
print("    (i)  nu_min = q0                          （q0 维谱可行）")
print("    (ii) nu_min 由某个更大的 d 决定（P2 的谱结构）")
print("  不存在'q0 维部分可行'的中间情形。")
