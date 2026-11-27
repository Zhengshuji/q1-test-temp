"""
最终验证：直接检验 L6 —— (S) 失败 ⟺ im(H) 含 Λ 的特征向量。

不绕道特征空间，直接算 Λ 与其特征向量。
"""
from fractions import Fraction as F

import numpy as np

rng = np.random.default_rng(20260116)


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


def ker_cols(M):
    if not M:
        return []
    n = len(M[0])
    R, piv = rref(M)
    free = [c for c in range(n) if c not in piv]
    if not free:
        return []
    sols = []
    for fc in free:
        v = [F(0)] * n
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][fc]
        sols.append(v)
    m = len(sols)
    return [[sols[j][i] for j in range(m)] for i in range(n)]


def orbit(M, A):
    out, cur = [], M
    for _ in range(len(A)):
        out += cur
        cur = mm(cur, A)
    return out


def get_lambda(A, C, Lx):
    """解 LA = ΛL + G0C + G1CA，返回 Λ（d×d）"""
    n, p, d = len(A), len(C), len(Lx)
    LA = mm(Lx, A)
    CA = mm(C, A)
    nunk = d + 2 * p
    Lam = []
    for i in range(d):
        cols = []
        for j in range(d):
            cols.append([Lx[j][t] for t in range(n)])
        for l in range(p):
            cols.append([C[l][t] for t in range(n)])
        for m_ in range(p):
            cols.append([CA[m_][t] for t in range(n)])
        Des = [[cols[c][t] for c in range(nunk)] for t in range(n)]
        b = [[LA[i][t]] for t in range(n)]
        R, piv = rref([Des[k] + [b[k][0]] for k in range(n)])
        y = [F(0)] * nunk
        for k_, pc in enumerate(piv):
            if pc < nunk:
                y[pc] = R[k_][nunk]
        Lam.append(y[:d])
    return Lam


def condS(A, C, L):
    LA = mm(L, A)
    rhs = rank_exact(L + C + mm(C, A))
    n = len(A)
    cs = set()
    for k in range(-16, 17):
        for den in (1, 2, 3, 4, 5, 6):
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
    coef = rng_.normal(size=(need, len(Bq))) if need > 0 else np.zeros((0, 1))
    rows = [[F(float(sum(coef[i][t] * float(Bq[t][j]) for t in range(len(Bq))))).limit_denominator(10**7)
             for j in range(len(Bq[0]))] for i in range(need)]
    L = BL + rows
    return L if rank_exact(L) == d else None


print("=" * 80)
print("直接检验 L6： (S) 失败 ⟺ im(H) 含 Λ 的特征向量")
print("=" * 80)
tot = agree = disagree = 0
for trial in range(60):
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
    dZ = rank_exact(Z)
    for d in range(r, min(dZ, n) + 1):
        for _ in range(4):
            L = rand_L(L0, Z, d, rng)
            if L is None:
                continue
            # (A) 必须成立，否则 Λ 可能不存在
            LA = mm(L, A)
            W = L + C + mm(C, A)
            if rank_exact(W + LA) != rank_exact(W):
                continue
            try:
                Lam = get_lambda(A, C, L)
            except Exception:
                continue
            # H = L·N_CA
            NCA = ker_cols(C + mm(C, A))
            nN = len(NCA[0]) if (NCA and NCA[0]) else 0
            if nN == 0:
                continue                     # H = 0，(S) 自动成立
            H = mm(L, NCA)
            s_ok = condS(A, C, L)
            # 检验 im(H) 是否含 Λ 的特征向量
            Lamf = np.array([[float(x) for x in row_] for row_ in Lam])
            evals, evecs = np.linalg.eig(Lamf)
            Hf = np.array([[float(x) for x in row_] for row_ in H])
            # im(H) 的数值基：对 H（d×m）做 SVD，U 的非零奇异值列张成 im(H)
            uH, sH, vtH = np.linalg.svd(Hf, full_matrices=False)
            tolH = max(Hf.shape) * (sH[0] if sH.size else 1) * 1e-9
            imH_basis = uH[:, sH > tolH] if sH.size else np.zeros((len(Lam), 0))
            # 每个特征向量是否在 im(H) 中
            contains = False
            for j in range(len(evals)):
                v = evecs[:, j]
                if imH_basis.shape[1] == 0:
                    continue
                resid = v - imH_basis @ (imH_basis.T @ v)
                if np.linalg.norm(resid) < 1e-6:
                    contains = True
                    break
            pred = (not contains)
            tot += 1
            if pred == s_ok:
                agree += 1
            else:
                disagree += 1
print(f"  检验次数 {tot}")
print(f"  L6 成立 {agree}，不一致 {disagree}")
if tot and disagree == 0:
    print("  => L6 完全成立：(S) 失败 ⟺ im(H) 含 Λ 的特征向量")
elif tot:
    print(f"  => L6 有 {disagree}/{tot} 不一致（数值或结构问题）")
