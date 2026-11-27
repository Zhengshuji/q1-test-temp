"""
关键引理（严格化目标）：

【引理 Σ】对固定的 d，集合
    Σ_d := { R : row(L0) ⊆ R ⊆ Z, dim R = d, R 满足 (A) 与 (S) }
  满足：  Σ_d = ∅  或  Σ_d 在 Σ_d^{(A)} 中稠密开。

本脚本要数值判定它的一个**可检验的具体形式**：

【引理 Σ'】(S) 的失败条件
    (S) 失败  ⟺  ∃ λ : ∃ v ∈ R/(R∩row(C)), v ≠ 0 : (A − λ)v ∈ R∩row(C)
  这个条件的"失败点 λ"只可能是 T_R 的特征值。

更可操作的形式（用于严格证明）：
    (S) 失败 ⟺ ∃ λ, ∃v∈R\{0}: (Av − λv) ∈ R∩row(C)
    即 R 含有一个"模 row(C) 的 λ-特征向量"。

于是定义
    Φ(R) := { λ : ∃v∈R\{0}, Av − λv ∈ R∩row(C) }   （有限集）
    (S) 成立 ⟺ Φ(R) = ∅

关键：Φ(R) 何时为空？这依赖 R 与 R∩row(C) 的相对位置。
"""
import itertools
from fractions import Fraction as F

import numpy as np

rng = np.random.default_rng(20260110)


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


def basis_of(M):
    if not M:
        return []
    Mn = np.array([[float(x) for x in r] for r in M])
    u, s, vt = np.linalg.svd(Mn, full_matrices=False)
    tol = max(Mn.shape) * (s[0] if s.size else 1) * 1e-12
    rk = int(np.sum(s > tol))
    return [[F(float(x)).limit_denominator(10**7) for x in row] for row in vt[:rk]]


def row_inter(A1, A2):
    """row(A1) ∩ row(A2) 的基（精确）"""
    B1, B2 = basis_of(A1), basis_of(A2)
    if not B1 or not B2:
        return []
    n = len(B1[0])
    # 求同时属于两者的向量：解 [B1^T | -B2^T] z = 0
    k1, k2 = len(B1), len(B2)
    cols = []
    for j in range(n):
        cols.append([B1[i][j] for i in range(k1)] + [-B2[i][j] for i in range(k2)])
    M = [[cols[j][i] for j in range(n)] for i in range(k1 + k2)]
    R, piv = rref(M)
    free = [c for c in range(n) if c not in piv]
    out = []
    for fc in free:
        coeff = [F(0)] * n
        coeff[fc] = F(1)
        for i, pc in enumerate(piv):
            coeff[pc] = -R[i][fc]
        # v = sum coeff_j * B1[j]
        v = [sum(coeff[j] * B1[j][t] for j in range(k1)) for t in range(n)]
        if any(x != 0 for x in v):
            out.append(v)
    return out


def phi_set(A, C, R_rows, s_cands):
    """
    Phi(R) = { λ : ∃v∈R\\{0}, (Av - λv) ∈ R∩row(C) }
    等价判据：rank[ (A^T - λI) 作用于 R 的像 ; (R∩row(C))^⊥ 约束 ] ...
    这里直接用定义检验：存在 v ∈ row(R), v≠0，使 Av - λv ∈ row(R) ∩ row(C)。
    实现：v 取 R 的基的线性组合，v = c·Lbase。
      Av - λv = c·(Lbase A) - λ c·Lbase = c·(Lbase A - λ Lbase)
    要求它 ∈ row(R)∩row(C)。
    记 W = row(R)∩row(C) 的基。
    条件：∃c≠0，使 c·(Lbase A - λ Lbase) ∈ row(W)，即
        rank[ Lbase A - λ Lbase ; W ] == rank(W) 且 c 非零 —
    更直接：令 M(λ) = Lbase A - λ Lbase。
        ∃c≠0 使 c M(λ) ∈ row(W)
      ⟺ rank[ M(λ) ; W ] - rank(W) < rank(Lbase)   ... 需小心
    简洁做法：投影到 W 的正交补。
    """
    B = basis_of(R_rows)                    # R 的基（行）
    W = row_inter(R_rows, C)                # R ∩ row(C) 的基
    # W^⊥ 的基：ker(W)
    def kern_basis(M):
        if not M:
            return []
        n = len(M[0])
        Rr, piv = rref(M)
        free = [c for c in range(n) if c not in piv]
        out = []
        for fc in free:
            v = [F(0)] * n
            v[fc] = F(1)
            for i, pc in enumerate(piv):
                v[pc] = -Rr[i][fc]
            out.append(v)
        return out
    Wperp = kern_basis(W) if W else basis_of([[F(1) if i == j else F(0)
                                               for j in range(len(A))] for i in range(len(A))])
    # 若 W = 0，则 W^⊥ = 全空间 -> (S) 自动成立（P(s)=0 恒等）
    if not W:
        return []                            # Phi 空
    res = []
    for s in s_cands:
        # M(λ) 的行；投影到 Wperp
        LA = mm(B, A)
        Mlam = [[s * B[i][j] - LA[i][j] for j in range(len(B[0]))] for i in range(len(B))]
        # 投影：P = Mlam · Wperp^T
        if Wperp:
            Wp = [[Wperp[t][j] for j in range(len(Wperp[0]))] for t in range(len(Wperp))]
            Proj = mm(Mlam, [[Wp[i][j] for i in range(len(Wp))] for j in range(len(Wp[0]))])
            # Proj 的行是 c 的线性像；存在 c≠0 使 Proj c^T = 0
            # ⟺ rank(Proj) < len(B)
            if rank_exact(Proj) < len(B):
                res.append(s)
    return res


print("=" * 80)
print("检验 Phi(R) 的含义：")
print("  (S) 成立  ⟺  Phi(R) = ∅")
print("  若 W = R ∩ row(C) = 0，则 Phi = ∅（(S) 自动成立）")
print("=" * 80)
print()

# 用 P1 算例的一个小规模版本来检查
cases = [
    ("小例1", [[1, 1], [0, 2]], [[1, 0]], [[0, 1]]),
    ("小例2", [[2, -2, 1], [1, -2, 1], [-1, 0, 1]], [[2, -1, -2]], [[-2, 2, 0]]),
]
s_cands = [F(k, 2) for k in range(-16, 17)]

for name, Am, Cm, L0m in cases:
    A, C, L0 = toF(Am), toF(Cm), toF(L0m)
    OC = orbit(C, A)
    Z = orbit(L0, A) + OC
    eta = eta_indices(A, C, L0)
    q0 = sum(eta)
    dZ = rank_exact(Z)
    print(f"  {name}: eta={eta} q0={q0} dimZ={dZ}")
    # 检验 d = q0 处的 Phi：取若干随机子空间
    BL, BZ = basis_of(L0), basis_of(Z)
    r = len(BL)
    Q = np.linalg.qr(np.array([[float(x) for x in rr] for rr in BL]).T)[0]
    BZn = np.array([[float(x) for x in rr] for rr in BZ])
    Bq = basis_of([[F(float(x)).limit_denominator(10**7) for x in row]
                   for row in (BZn - BZn @ Q @ Q.T)])
    for d in (q0, min(q0 + 1, dZ)):
        need = d - r
        if need < 0 or need > len(Bq):
            continue
        sizes = []
        for trial_i in range(6):
            coef = rng.normal(size=(need, len(Bq)))
            rows = [[F(float(sum(coef[i][t] * float(Bq[t][j]) for t in range(len(Bq))))).limit_denominator(10**7)
                     for j in range(len(Bq[0]))] for i in range(need)]
            L = BL + rows
            if rank_exact(L) != d:
                continue
            ph = phi_set(A, C, L, s_cands)
            W = row_inter(L, C)
            sizes.append((len(W), len(ph)))
        print(f"     d={d}:  每个样本 (dim(R∩row(C)), |Phi(R)|) = {sizes}")
    print()
