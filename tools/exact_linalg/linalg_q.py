# -*- coding: utf-8 -*-
"""
linalg_q.py —— 本项目**统一使用**的独立精确线性代数层（带维数断言 + 残差校验）

【为什么需要它】
  本会话发现库 `exact_count_thm7.solve` 在一类系统上会返回**不满足残差的"解"** ✗，
  而多个脚本（`batch_c6p_k.py`、`check_S.py` 等）依赖它做 (A) 的分解 ⟹ 结论被污染。
  为杜绝这类**静默错误**，这里把独立实现集中成一层，并强制：
    ① 每次矩阵乘法检查维数（本项目第 13 处的教训）；
    ② 解线性方程组后**显式验证残差全零**，否则报错而不静默返回。

【与已有资产的关系】
  · `linalg_exact.py` 是更早的独立实现（正确）——本文件在其上补齐**断言与校验**，
    并额外提供 `nullspace` / `left_inverse` / `rowspace` 等常用工具。
  · **不改动** `exact_count_thm7.py`（它被大量旧脚本以绝对路径 exec，改动风险大）；
    而是让需要 (A) 分解的脚本改调本层。
"""
from fractions import Fraction as F


# ---------------------------------------------------------------- 基础

def mat(rows):
    return [[F(x) for x in r] for r in rows]


def assert_rect(M, name="M"):
    if M:
        w = len(M[0])
        for i, r in enumerate(M):
            assert len(r) == w, "%s 第 %d 行列数不一致" % (name, i)


def mul(X, Y):
    """矩阵乘法，**带维数断言**（杜绝库 mm 那种静默错配）"""
    assert X and Y, "mul: 空矩阵"
    assert_rect(X, "X")
    assert_rect(Y, "Y")
    assert len(X[0]) == len(Y), "mul 维数不匹配: %d vs %d" % (len(X[0]), len(Y))
    n, k, m = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def stack(*Ms):
    out = []
    for M in Ms:
        if not M:
            continue
        assert_rect(M, "stack")
        if out:
            assert len(out[0]) == len(M[0]), "stack 列数不一致"
        out += [r[:] for r in M]
    return out


def hcat(X, Y):
    """列拼接 [X | Y]"""
    assert_rect(X, "X"); assert_rect(Y, "Y")
    assert len(X) == len(Y), "hcat 行数不一致"
    return [X[i] + Y[i] for i in range(len(X))]


# ---------------------------------------------------------------- 秩 / 零空间

def rref(M):
    """返回 (R, pivots)。带维数断言。"""
    if not M:
        return [], []
    assert_rect(M, "rref")
    A = [r[:] for r in M]
    m, k = len(A), len(A[0])
    piv, r = [], 0
    for c in range(k):
        sel = None
        for i in range(r, m):
            if A[i][c] != 0:
                sel = i
                break
        if sel is None:
            continue
        A[r], A[sel] = A[sel], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(k)]
        piv.append(c)
        r += 1
        if r == m:
            break
    return A, piv


def rank(M):
    return 0 if not M or not M[0] else len(rref(M)[1])


def nullspace(M):
    """{x : M·x = 0} 的一组基，**每个基向量是列表的一行**（行约定）。

    ⚠️ 本项目其它脚本（`exact_count_thm7.ker_basis`）用的是**列约定**
    （返回 n×d 矩阵，基向量是**列**）。两者会静默混用出错 ⟹
    需要列约定时请显式调用 **`ker_basis_cols`** ✓
    """
    if not M or not M[0]:
        return []
    R, piv = rref(M)
    k = len(M[0])
    out = []
    for fc in [c for c in range(k) if c not in piv]:
        v = [F(0)] * k
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][fc]
        out.append(v)
    return out


def ker_basis_cols(M):
    """ker(M) 的基，**列约定**：返回 n×d 矩阵（d = 零空间维数，基向量是列）。

    与 `exact_count_thm7.ker_basis` 的约定一致，便于直接做 L·N 这类矩阵乘法 ✓
    """
    vs = nullspace(M)
    if not vs:
        return []
    n = len(M[0])
    return [[vs[j][i] for j in range(len(vs))] for i in range(n)]


def solve(Des, b):
    """解 Des·x = b。返回 (y, ns) 或 None（不相容）。

    ★ **关键**：返回前显式验证残差 `Des·y == b` 及 `Des·(y+ns) == b`；
      不通过就 raise（绝不静默返回错解）。

    ⚠️ 实现要点（本函数前两版都有 bug，记录以免重犯）：
      ① 增广列的秩**不能**参与 `rank` —— 否则会把不相容系统误判为相容；
      ② 特解**不能**"按主元列的顺序读增广列" —— 行交换会让主元与行号错位，
         必须按**主元列**定位其所在行，再取该行的增广元（本版做法）✓
    """
    if not Des:
        return None
    assert_rect(Des, "Des")
    assert len(b) == len(Des), "solve: b 的行数应与 Des 相同"
    m, k = len(Des), len(Des[0])
    M = [[F(Des[i][j]) for j in range(k)] + [F(b[i][0])] for i in range(m)]
    # 标准 Gauss–Jordan（作用于增广矩阵）
    piv, r = [], 0
    for c in range(k):
        sel = None
        for i in range(r, m):
            if M[i][c] != 0:
                sel = i
                break
        if sel is None:
            continue
        M[r], M[sel] = M[sel], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[r][j] for j in range(k + 1)]
        piv.append(c)
        r += 1
        if r == m:
            break
    for i in range(m):
        if all(M[i][j] == 0 for j in range(k)) and M[i][k] != 0:
            return None
    # 特解：自由变量取 0；每个主元列取其**所在行**（全行搜索，不假设行序）的增广元
    y = [F(0)] * k
    pset = set(piv)
    for c in piv:
        target = None
        for i in range(m):
            if M[i][c] != 0 and all(M[i][j] == 0 for j in range(c)):
                target = i
                break
        if target is None:
            continue
        y[c] = M[target][k]
    ns = nullspace(Des)

    def _ok(v):
        return all(sum(F(Des[i][j]) * v[j] for j in range(k)) == F(b[i][0]) for i in range(m))

    if not _ok(y):
        raise AssertionError("solve: 特解未通过残差校验（求解器实现有误）")
    for v in ns:
        if not _ok([y[j] + v[j] for j in range(k)]):
            raise AssertionError(
                "solve: 零空间基未通过残差校验（求解器实现有误）\n"
                "  v = %s\n  残差 = %s" % (
                    [str(x) for x in v],
                    [str(sum(F(Des[i][j]) * (y[j] + v[j]) for j in range(k)) - F(b[i][0]))
                     for i in range(m)]))
    return y, ns


def left_inverse(B):
    """B 为 n×d 列满秩 ⟹ 返回 d×n 的 Bg 使 Bg·B = I_d"""
    n, d = len(B), len(B[0])
    Bt = [[B[i][j] for i in range(n)] for j in range(d)]
    out = []
    for j in range(d):
        r = solve(Bt, [[F(1) if i == j else F(0)] for i in range(d)])
        if r is None:
            return None
        out.append(r[0])
    return out


def rowspace(M):
    """M 的行空间的一组基（行向量）"""
    if not M or not M[0]:
        return []
    R, piv = rref(M)
    return [R[i][:] for i in range(len(piv))]


# ---------------------------------------------------------------- 项目级判据

def condA(A, C, L):
    """(5a)/(A)：rk[LA;L;C;CA] == rk[L;C;CA]（原始 4 块，见 FINAL T1）"""
    CA = mul(C, A)
    return rank(stack(mul(L, A), L, C, CA)) == rank(stack(L, C, CA))


LAMS = [F(0), F(1), F(-1), F(2), F(-2), F(3), F(-3),
        F(1, 2), F(-1, 2), F(1, 3), F(-2, 3), F(5, 7), F(7, 5)]


def S_holds(A, C, L, B, lams=None):
    """(S) 的**两种独立判据**，必须同时成立才返回 True：

      判据A（FINAL §1.1 的原始定义）: ∀λ, rk[λL−LA;CA;C] == rk[L;CA;C]
      判据B（T2 的铅笔约化）        : ∀λ, rk(λH−F) == rk H
    """
    lams = lams or LAMS
    CA = mul(C, A)
    LA = mul(L, A)
    base = rank(stack(L, CA, C))
    okA = True
    for lam in lams:
        M = [[lam * L[i][j] - LA[i][j] for j in range(len(L[0]))] for i in range(len(L))]
        if rank(stack(M, CA, C)) != base:
            okA = False
            break
    H = mul(L, B)
    Fm = mul(LA, B)
    rH = rank(H)
    okB = True
    for lam in lams:
        M = [[lam * H[i][j] - Fm[i][j] for j in range(len(H[0]))] for i in range(len(H))]
        if rank(M) != rH:
            okB = False
            break
    return okA and okB


def decomp_Lambda(A, C, L):
    """解 (A) 的分解 LA = ΛL + G₀C + G₁CA，返回 Λ（或 None）。

    ★ 用本层的 `solve`（带残差校验）⟹ 不会出现"库 solve 给出错误解"那类污染 ✓
    约定：返回的 Λ 满足 ΛL ≡ LA (mod C, CA)，故 **ΛH = F** ✓
    """
    q0, n, p = len(L), len(A), len(C)
    CA = mul(C, A)
    LA = mul(L, A)
    nunk = q0 * q0 + 2 * q0 * p
    rows, rhs = [], []
    for i in range(q0):
        for j in range(n):
            row = [F(0)] * nunk
            for kk in range(q0):
                row[kk * q0 + i] = L[kk][j]
            for m in range(p):
                row[q0 * q0 + i * p + m] = C[m][j]
            for m in range(p):
                row[q0 * q0 + q0 * p + i * p + m] = CA[m][j]
            rows.append(row)
            rhs.append([LA[i][j]])
    res = solve(rows, rhs)
    if res is None:
        return None
    y = res[0]
    return [[y[kk * q0 + i] for kk in range(q0)] for i in range(q0)]
