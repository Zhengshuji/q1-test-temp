r"""
exact_gcd.py -- 共享的多项式 gcd 与 (5b) 判据（**修正版**）

⚠️ 本模块的存在理由（第 40 处更正，见 PROOF_AUDIT.md §7）：

  旧实现有一个致命 bug：
      ps = [所有 ρ 阶子式]        # 可能含零多项式
      g  = ps[0]                  # 若 ps[0] == 0 则 g = 0
      for x in ps[1:]:
          g = Pg(g, x)
          if len(g) == 1: break   # g == ['0'] 时被误判为"已互素" ✗
  ⟹ (5b) 被误报为**失败**（假阴性）⟹ 漏报解 ✗

  触发条件：开头**至少两个** ρ 阶子式同时为零多项式。

  正确做法：**先过滤零多项式**，且只在 g 是**非零常数**时提前退出。

  另一个（2026-10-21 修正）：旧 cond_5b 只检查 ρ 阶子式的 gcd（**下界**），
  没有检查 (ρ+1) 阶子式（**上界**）。若 F ≠ ΛM，normal rank 可能 > ρ，
  此时 gcd 判据仍可能为真 ⟹ **假阳性**。现在 cond_5b 同时检查两个方向；
  诊断可用 cond_5b_diagnose(M, F)。

用法：
    from exact_gcd import cond_5b, cond_5b_verbose, cond_5b_diagnose
"""
import os, io, contextlib, itertools
from fractions import Fraction as Fr

# ---------- 多项式算术（次数升序，末尾零去掉）----------

def Pt(p):
    q = list(p)
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    return q

def Pa(a, b):
    n = max(len(a), len(b))
    return Pt([(a[i] if i < len(a) else Fr(0)) + (b[i] if i < len(b) else Fr(0))
               for i in range(n)])

def Ps(a, b):
    n = max(len(a), len(b))
    return Pt([(a[i] if i < len(a) else Fr(0)) - (b[i] if i < len(b) else Fr(0))
               for i in range(n)])

def Pm(a, b):
    if Pt(a) == [Fr(0)] or Pt(b) == [Fr(0)]:
        return [Fr(0)]
    r = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return Pt(r)

def Pdv(a, b):
    """(商, 余)"""
    a = Pt(a); b = Pt(b); db = len(b) - 1
    q = [Fr(0)] * max(1, len(a) - db)
    while len(a) - 1 >= db and a != [Fr(0)]:
        d = len(a) - 1 - db; co = a[-1] / b[-1]; q[d] += co
        for i in range(len(b)):
            a[d + i] -= co * b[i]
        a = Pt(a)
    return Pt(q), a

def Pg(a, b):
    """gcd（首一化）"""
    a, b = Pt(a), Pt(b)
    while b != [Fr(0)]:
        _, r = Pdv(a, b); a, b = b, r
    if len(a) > 1:
        lc = a[-1]; a = [x / lc for x in a]
    return a

def Pdet(M, k):
    """多项式矩阵的 k 阶行列式（递归展开）"""
    if k == 1:
        return [Fr(x) for x in M[0][0]]
    tot = [Fr(0)]
    for j in range(k):
        sub = [row[:j] + row[j + 1:] for row in M[1:]]
        d = Pdet(sub, k - 1); pr = Pm(M[0][j], d)
        tot = Pa(tot, pr) if j % 2 == 0 else Ps(tot, pr)
    return Pt(tot)

# ---------- 判据 ----------

ZERO = [Fr(0)]

def is_zero(p):
    return Pt(p) == ZERO

def is_nonzero_const(p):
    p = Pt(p)
    return len(p) == 1 and p[0] != 0

def gcd_list(ps):
    """**修正版** gcd：跳过零多项式；只在非零常数时提前退出"""
    nz = [p for p in ps if not is_zero(p)]
    if not nz:
        return ZERO                      # 全零 ⟹ gcd = 0
    g = nz[0]
    for x in nz[1:]:
        g = Pg(g, x)
        if is_nonzero_const(g):
            break
    return Pt(g)

def _pencil(M, F):
    """系数矩阵：P(λ) = [-F | M]，每个元素是 [常数项, λ 系数]。"""
    q = len(M); d = len(M[0])
    return [[[-F[i][j], M[i][j]] for j in range(d)] for i in range(q)], q, d

def _nonzero_minor_exists(P, q, d, k, maxm):
    """P 是否有某个 k 阶子式是**非零多项式**（即 normal rank ≥ k）。"""
    if k <= 0 or k > q or k > d:
        return False
    cnt = 0
    for rows in itertools.combinations(range(q), k):
        for cols in itertools.combinations(range(d), k):
            if not is_zero(Pdet([[P[i][j] for j in cols] for i in rows], k)):
                return True
            cnt += 1
            if cnt > maxm:
                raise RuntimeError(
                    "cond_5b: minor scan exceeded maxm=%d; increase maxm" % maxm)
    return False

def cond_5b(M, F, maxm=200000):
    """
    (5b)：rank(λM − F) = rank(M)  ∀λ ∈ ℂ。

    **这是两个方向，缺一不可**：

      (i)  上界：P(λ) = [-F | M] 的所有 (ρ+1) 阶子式恒等于零
           （等价于 normal rank ≤ ρ = rank(M)）；
      (ii) 下界：非零的 ρ 阶子式的 gcd 是**非零常数**（无公共根）。

    只检查 (ii) 是**错的**：当 normal rank > ρ 时，(ii) 仍可能为真，
    给出假阳性（见文件末尾的回归用例 3）。若已知 F = ΛM（或 (5a) 成立），
    (i) 自动成立；但本函数不假设这一点，仍然显式检查。
    """
    q = len(M); d = len(M[0])
    rho = _rank(M)
    if rho == 0:
        # M = 0 时，(5b) 等价于 F = 0。
        return all(F[i][j] == 0 for i in range(q) for j in range(d))
    if rho > d or rho > q:
        return False
    P, q, d = _pencil(M, F)
    # (i) 上界：不能有 (ρ+1) 阶非零子式
    if _nonzero_minor_exists(P, q, d, rho + 1, maxm):
        return False
    # (ii) 下界：ρ 阶子式的 gcd 为非零常数
    ps = []
    for rows in itertools.combinations(range(q), rho):
        for cols in itertools.combinations(range(d), rho):
            ps.append(Pdet([[P[i][j] for j in cols] for i in rows], rho))
    g = gcd_list(ps)
    if is_zero(g):
        return False
    return is_nonzero_const(g)

def cond_5b_diagnose(M, F, maxm=200000):
    """返回诊断字典：upper_ok / lower_ok / gcd / rank / ok。"""
    q = len(M); d = len(M[0]); rho = _rank(M)
    if rho == 0:
        ok = all(F[i][j] == 0 for i in range(q) for j in range(d))
        return {"rank": 0, "upper_ok": ok, "lower_ok": ok,
                "gcd": [Fr(1)] if ok else [Fr(0)], "ok": ok}
    P, q, d = _pencil(M, F)
    upper = not _nonzero_minor_exists(P, q, d, rho + 1, maxm)
    ps = []
    for rows in itertools.combinations(range(q), rho):
        for cols in itertools.combinations(range(d), rho):
            ps.append(Pdet([[P[i][j] for j in cols] for i in rows], rho))
    g = gcd_list(ps)
    lower = (not is_zero(g)) and is_nonzero_const(g)
    return {"rank": rho, "upper_ok": upper, "lower_ok": lower,
            "gcd": g, "ok": upper and lower}

def cond_5b_verbose(M, F, maxm=200000):
    """返回 (结论, gcd) 便于调试。"""
    diag = cond_5b_diagnose(M, F, maxm=maxm)
    return diag["ok"], diag["gcd"]

def _rank(M):
    """精确秩（局部实现，避免外部依赖）"""
    if not M or not M[0]:
        return 0
    A = [[Fr(x) for x in row] for row in M]
    m = len(A); n = len(A[0]); r = 0
    for c in range(n):
        p = None
        for i in range(r, m):
            if A[i][c] != 0:
                p = i; break
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r

# ---------- 自检 ----------

if __name__ == "__main__":
    # 回归用例 1：开头两个子式为零（旧 bug 的触发条件）
    M = [[Fr(0), Fr(0), Fr(-1)],
         [Fr(0), Fr(0), Fr(-1)],
         [Fr(0), Fr(0), Fr(0)],
         [Fr(0), Fr(0), Fr(-1)]]
    F = [[Fr(0), Fr(0), Fr(1)],
         [Fr(0), Fr(0), Fr(0)],
         [Fr(0), Fr(0), Fr(2)],
         [Fr(0), Fr(0), Fr(-3)]]
    r, g = cond_5b_verbose(M, F)
    print("回归用例 1（开头两子式为零）：gcd =", [str(x) for x in g], " (5b) =", r)
    assert r is True, "回归失败：应判 (5b)=True"
    print("  ✓ 通过（旧实现会误判为 False）")

    # 回归用例 2：真的有秩降（λ=-1 处）
    M2 = [[Fr(0), Fr(-1)], [Fr(-1), Fr(0)], [Fr(0), Fr(-1)]]
    F2 = [[Fr(-1), Fr(1)], [Fr(1), Fr(0)], [Fr(-1), Fr(1)]]
    r2, g2 = cond_5b_verbose(M2, F2)
    print("回归用例 2（λ=-1 处秩降）：gcd =", [str(x) for x in g2], " (5b) =", r2)
    assert r2 is False, "回归失败：应判 (5b)=False"
    print("  ✓ 通过")

    # 回归用例 3：假阳性（normal rank > ρ；旧 cond_5b 只查 gcd 会报 True）
    M3 = [[Fr(1), Fr(0)], [Fr(0), Fr(0)]]
    F3 = [[Fr(0), Fr(0)], [Fr(0), Fr(1)]]
    d3 = cond_5b_diagnose(M3, F3)
    print("回归用例 3（上界失败）：", d3)
    assert d3["upper_ok"] is False and d3["ok"] is False, \
        "回归失败：cond_5b 必须拒绝 normal rank > ρ 的假阳性"
    print("  ✓ 通过（旧实现会误报 True）")

    # 回归用例 4：ρ = 0 时 (5b) ⟺ F = 0
    M4 = [[Fr(0), Fr(0)], [Fr(0), Fr(0)]]
    F4 = [[Fr(0), Fr(0)], [Fr(0), Fr(0)]]
    assert cond_5b(M4, F4) is True, "ρ=0 且 F=0 应判 True"
    assert cond_5b(M4, F3) is False, "ρ=0 且 F≠0 应判 False"
    print("回归用例 4（ρ=0）：✓ 通过")

    # 回归用例 5：合法的 (5b)（M 3×2, F = ΛM, 无秩降）
    M5 = [[Fr(1), Fr(0)], [Fr(0), Fr(1)], [Fr(0), Fr(0)]]
    F5 = [[Fr(0), Fr(0)], [Fr(1), Fr(0)], [Fr(0), Fr(1)]]
    d5 = cond_5b_diagnose(M5, F5)
    print("回归用例 5（合法 (5b)）：", d5)
    assert d5["ok"] is True, "回归失败：这个实例应满足 (5b)"
    print("  ✓ 通过")

    print("\n全部回归通过 ✓")
