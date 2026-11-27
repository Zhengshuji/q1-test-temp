"""
核心问题的可判定性探索。

命题 q 归结为：
   (Q)  对满足 H1-H4 的系统，(A)∧(S) 是否存在 q0 维的解？
        等价于 nu_min = q0？

观察（引理 1/2）：(A) 与 (S) 都只依赖 R = row(L)。
所以 (Q) 等价于：
   在 Grassmann 流形 {R : row(L0) ⊆ R ⊆ Z, dim R = q0} 上，
   半代数集 Σ(A) ∩ Σ(S) 是否非空。

关键：若 (A) 由线性条件定义（仿射子空间），(S) 是 Zariski-开，
则 Σ = 仿射 ∩ 开。若仿射部分非空且不可约，则 Σ 要么空要么稠密开。

本脚本要回答三个层次的问题：
  L1: Σ(A) 是否就是整个 Gr(d, Z)？还是真子集？
  L2: Σ(S) 在 Σ(A) 上是"要么全有要么全无"（0/1）还是"部分"？
  L3: 若 L2 是 0/1，则 nu_min = q0 ⟺ 随机取样命中 ⟺ 可判定。
      若 L2 出现"部分"，则 Θ 是实质障碍，问题更难。
"""
import itertools
from fractions import Fraction as F

import numpy as np

rng = np.random.default_rng(20260107)


# ---------------- 精确有理线性代数 ----------------
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
    for k in range(-24, 25):
        for den in (1, 2, 3, 4, 5, 6, 7, 8):
            cs.add(F(k, den))
    try:
        for ev in np.linalg.eigvals(np.array(A, float)):
            if abs(ev.imag) < 1e-7:
                cs.add(F(float(ev.real)).limit_denominator(5000))
        Lf = np.array(L, float); LAf = Lf @ np.array(A, float)
        if Lf.shape[0] == Lf.shape[1] and abs(np.linalg.det(Lf)) > 1e-9:
            for ev in np.linalg.eigvals(np.linalg.solve(Lf, LAf)):
                if abs(ev.imag) < 1e-7:
                    cs.add(F(float(ev.real)).limit_denominator(5000))
        else:
            from scipy.linalg import eig as geig
            for ev in geig(LAf, Lf, right=False):
                if abs(ev.imag) < 1e-7:
                    cs.add(F(float(ev.real)).limit_denominator(5000))
    except Exception:
        pass
    for s in sorted(cs):
        sl = [[s * L[i][j] - LA[i][j] for j in range(n)] for i in range(len(L))]
        if rank_exact(sl + C + mm(C, A)) != rhs:
            return False
    return True


def random_L_in_lattice(L0, Z, d, rng_):
    """在 row(L0) ⊆ R ⊆ Z 中取随机 d 维子空间"""
    def basis_of(M):
        if not M:
            return []
        Mn = np.array([[float(x) for x in r] for r in M])
        u, s, vt = np.linalg.svd(Mn, full_matrices=False)
        tol = max(Mn.shape) * (s[0] if s.size else 1) * 1e-12
        rk = int(np.sum(s > tol))
        return [[F(float(x)).limit_denominator(10**7) for x in row] for row in vt[:rk]]
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
        L = BL
        return L if rank_exact(L) == d else None
    coef = rng_.normal(size=(need, len(Bq)))
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
print("L1/L2 探索：Σ(A) 与 Σ(S) 在格上的分布")
print("=" * 80)
print("  对每个满足 H1-H4 的实例，在 d = q0 处取 N 个随机子空间，")
print("  记录 (A) 命中率与 (A)∧(S) 命中率。")
print()

NS = 24
records = []
for trial in range(60):
    n = int(rng.integers(2, 4))
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
        continue                                   # H4
    eta = eta_indices(A, C, L0)
    q0 = sum(eta)
    dZ = rank_exact(Z)
    if q0 > dZ:
        continue
    if dZ > n:
        continue
    ca = cs = 0
    tot = 0
    for _ in range(NS):
        L = random_L_in_lattice(L0, Z, q0, rng)
        if L is None:
            continue
        tot += 1
        a_ok = condA(A, C, L)
        if a_ok:
            ca += 1
            if condS(A, C, L):
                cs += 1
    if tot:
        records.append((Am.tolist(), Cm.tolist(), L0m.tolist(), eta, q0, dZ, ca, cs, tot))

print(f"  有效实例: {len(records)}")
print()
print("  A/C/L0 (摘要)                     eta  q0 dZ | (A)命中  (A)∧(S)命中")
print("  " + "-" * 74)
inter = []
for Am, Cm, L0m, eta, q0, dZ, ca, cs, tot in records:
    tag = ""
    if 0 < cs < tot:
        tag = "   <== 部分命中（Θ 是实质障碍）"
        inter.append((Am, Cm, L0m, eta, q0, dZ, ca, cs, tot))
    print(f"  {str(Am)[:20]:22s} {str(Cm)[:10]:11s} {str(eta):5s} {q0:2d} {dZ:2d} |  "
          f"{ca:2d}/{tot:2d}    {cs:2d}/{tot:2d}{tag}")

print()
print("=" * 80)
print("结论")
print("=" * 80)
print(f"  出现'部分命中'的实例数: {len(inter)} / {len(records)}")
if inter:
    print("  => Θ 是实质障碍，Σ 不是简单的 0/1 结构")
    for Am, Cm, L0m, eta, q0, dZ, ca, cs, tot in inter[:3]:
        print(f"     A={Am} C={Cm} L0={L0m} eta={eta} q0={q0} dZ={dZ} "
              f"(A)={ca}/{tot} (A)∧(S)={cs}/{tot}")
else:
    print("  => 未出现部分命中：Σ(A)∧Σ(S) 在格上呈 0/1 分布")
    print("     这支持'随机取样可判定 nu_min'，即命题 q 可能为假。")
