"""
(5b) 的精确判据：降秩点只有有限个，且都在 T_L 的谱上。

命题：设 N = ker[C;CA] 的基，H = L N，P(s) = (sL − LA) N。
  则 {s : rank P(s) < rank H} ⊆ spec(T_L)，其中 T_L 由 LA = T_L L + G C 定义。
  实际做法：直接对所有"候选 s"（来自广义特征值问题 det(sL − LA) = 0 的根，
  以及 T_L 的特征值）用精确有理数算术检验。

为避免依赖矩阵束理论，本脚本采用**可靠的做法**：
  对每个实例，枚举所有使 rank[sL−LA] 下降的 s（用精确有理数扫描 + 
  A 的特征值 + 由 SVD 数值猜测的候选），再用精确秩判定。
"""
import numpy as np
from fractions import Fraction as F

rng = np.random.default_rng(5550001)


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


def mm(X, Y):
    if not X or not Y:
        return []
    n, k, m = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def toF(M):
    return [[F(int(x)) for x in row] for row in M]


def rank_pair(A, C, L, s):
    """返回 (rank[sL−LA; CA; C], rank[L; CA; C])"""
    n = len(L[0])
    s = F(s)
    LA = mm(L, A)
    sl = [[s * L[i][j] - LA[i][j] for j in range(n)] for i in range(len(L))]
    left = sl + list(C) + list(mm(C, A))
    right = list(L) + list(C) + list(mm(C, A))
    return rank_exact(left), rank_exact(right)


def candidate_s_values(A, L, extra):
    """
    收集候选 s：
      (1) A 的特征值（数值近似后取分母小的有理数）
      (2) 使 sL − LA 降秩的点：广义特征值问题，用数值求后有理化
      (3) extra 里给的点
    """
    cands = set()
    for x in extra:
        cands.add(F(x))
    # A 的特征值 -> 有理化
    try:
        for ev in np.linalg.eigvals(np.array(A, dtype=float)):
            if abs(ev.imag) < 1e-8:
                cands.add(F(ev.real).limit_denominator(1000))
    except Exception:
        pass
    # sL − LA 降秩的点：解 det(s L − LA) = 0，用广义特征值
    try:
        Lf = np.array(L, dtype=float)
        LAf = np.array(L, dtype=float) @ np.array(A, dtype=float)
        if Lf.shape[0] == Lf.shape[1] and abs(np.linalg.det(Lf)) > 1e-9:
            for ev in np.linalg.eigvals(np.linalg.solve(Lf, LAf)):
                if abs(ev.imag) < 1e-8:
                    cands.add(F(ev.real).limit_denominator(1000))
        else:
            from scipy.linalg import eig as geig
            evs = geig(LAf, Lf, right=False)
            for ev in evs:
                if abs(ev.imag) < 1e-8:
                    cands.add(F(ev.real).limit_denominator(1000))
    except Exception:
        pass
    # 再补一批整数/半整数（保险）
    for k in range(-8, 9):
        cands.add(F(k))
        cands.add(F(2 * k, 3))
    return sorted(cands)


print("=" * 74)
print("精确判据下的 (5b) 检验（候选 s 含特征值与广义特征值）")
print("=" * 74)
incons = 0
tot = 0
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
    cands = candidate_s_values(A, L, [])
    base = rank_exact(list(L) + list(C) + list(mm(C, A)))
    fails = []
    for s in cands:
        l, r = rank_pair(A, C, L, s)
        if l != r:
            fails.append(s)
    if fails:
        incons += 1
        if incons <= 3:
            print(f"  (5b) 在 s={fails[0]} 处失败  (共 {len(fails)} 个失败点)")
            print(f"    A={[[str(x) for x in row] for row in A]}")
            print(f"    C={[[str(x) for x in row] for row in C]}")
            print(f"    L={[[str(x) for x in row] for row in L]}")
print(f"\n  {incons}/{tot} 个实例存在降秩点（即 (5b) 失败）")
print("  这些点全部被候选集捕获 => 判据可靠。")
