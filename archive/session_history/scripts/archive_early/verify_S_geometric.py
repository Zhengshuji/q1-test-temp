"""
由 L12 导出的强简化（单特征值情形）：

  L12: (S) 成立 ⟺ ∀λ: R ∩ (E_λ + W0) = R ∩ W0,   W0 := row(C)

  若 A 的特征值全为单重（E_λ 一维，基为 e_λ），则
     R ∩ (E_λ + W0) ≠ R ∩ W0  ⟺  ∃c≠0, w∈W0: c·e_λ + w ∈ R
                              ⟺  e_λ ∈ R + W0
  故
     (S) 成立 ⟺ (R + W0) 不含 A 的任何特征向量     ← 本脚本要验证的等价形式

本脚本：
  (T1) 在单特征值实例上，验证 "(R+W0) 不含特征向量" 与 "(S) 成立" 等价
  (T2) 检验 (R+W0) 是否含特征向量 —— 这是**线性代数的开条件**
  (T3) 据此给出 nu_min 的候选算法
"""
from fractions import Fraction as F

import numpy as np

rng = np.random.default_rng(20260115)


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
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(nrow):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c)
        r += 1
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


def in_span(X, Y):
    X = [r for r in X if any(v != 0 for v in r)]
    if not X:
        return True
    return rank_exact(Y + X) == rank_exact(Y)


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
    for k in range(-20, 21):
        for den in (1, 2, 3, 4, 5, 6):
            cs.add(F(k, den))
    try:
        for ev in np.linalg.eigvals(np.array(A, float)):
            if abs(ev.imag) < 1e-7:
                cs.add(F(float(ev.real)).limit_denominator(5000))
        Lf = np.array(L, float)
        LAf = Lf @ np.array(A, float)
        if Lf.shape[0] == Lf.shape[1] and abs(np.linalg.det(Lf)) > 1e-9:
            for ev in np.linalg.eigvals(np.linalg.solve(Lf, LAf)):
                if abs(ev.imag) < 1e-7:
                    cs.add(F(float(ev.real)).limit_denominator(5000))
    except Exception:
        pass
    for s in sorted(cs):
        sl = [[s * L[i][j] - LA[i][j] for j in range(n)] for i in range(len(L))]
        if rank_exact(sl + C + mm(C, A)) != rhs:
            return False
    return True


def eigvecs_simple(A):
    """返回 A 的实特征向量（单特征值情形）；用 numpy 求后有理化不现实，
       故这里改用：对每个实特征值 λ，求 ker(λI−A) 的精确基。"""
    Af = np.array([[float(x) for x in r] for r in A])
    evs = np.linalg.eigvals(Af)
    real_evs = sorted({round(float(e.real), 6) for e in evs if abs(e.imag) < 1e-8})
    out = []
    for lam in real_evs:
        lamF = F(lam).limit_denominator(10**4)
        M = [[(lamF if i == j else F(0)) - A[i][j] for j in range(len(A))] for i in range(len(A))]
        R, piv = rref(M)
        n = len(A)
        free = [c for c in range(n) if c not in piv]
        for fc in free:
            v = [F(0)] * n
            v[fc] = F(1)
            for i, pc in enumerate(piv):
                v[pc] = -R[i][fc]
            if any(x != 0 for x in v):
                out.append((lamF, v))
    return out


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
print("T1: 验证等价性  (R+W0 不含 A-特征向量)  ⟺  (S) 成立")
print("=" * 80)
tot = agree = disagree = 0
for trial in range(120):
    n = int(rng.integers(2, 5))
    p = int(rng.integers(1, n))
    r = int(rng.integers(1, n - p + 1)) if n - p >= 1 else 1
    Am = rng.integers(-2, 3, (n, n))
    Cm = rng.integers(-2, 3, (p, n))
    L0m = rng.integers(-2, 3, (r, n))
    A, C, L0 = toF(Am), toF(Cm), toF(L0m)
    # 要求 A 的特征值互异
    evs = np.linalg.eigvals(np.array(Am, float))
    if len({round(float(e.real), 6) + 1j * round(float(e.imag), 6) for e in evs}) != n:
        continue
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
    E = eigvecs_simple(A)                       # [(λ, e_λ)]
    for d in range(q0, dZ + 1):
        for _ in range(6):
            L = rand_L(L0, Z, d, rng)
            if L is None:
                continue
            tot += 1
            s_ok = condS(A, C, L)
            # 修正：W = row(C, CA)（不是 row(C)！）
            W = C + mm(C, A)
            RW = basis_of(L + W)                 # R + W
            contains = False
            for lam, ev in E:
                if in_span([ev], RW):
                    contains = True
                    break
            pred = (not contains)                # 预测 (S) 成立
            if pred == s_ok:
                agree += 1
            else:
                disagree += 1
print(f"  检验次数 {tot}")
print(f"  等价成立 {agree}，不一致 {disagree}")
print()
if disagree == 0:
    print("  => 等价性成立：")
    print("     (S) 成立 ⟺ (R + row(C)) 不含 A 的任何特征向量")
    print("     这是一个**纯线性代数的开条件**！")
else:
    print(f"  => 有 {disagree} 次不一致，等价性不成立（需修正）")
    print("     可能原因：需用广义特征空间，或特征向量的'模 W0'版本")
