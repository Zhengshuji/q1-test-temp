# -*- coding: utf-8 -*-
"""
c6_general_A.py -- ⭐ 决定性实验：c6′ 在**非 A-不变**（一般 A）下是否成立？

【构造（利用 A(K) ⊄ K）】
  给定 A, C，K = ker[C;CA]（dim d）。
  取标量 c，令 v_j = A N_j − c N_j（j=1..d），求其**左零化子**
      L0 · v_j = 0  (∀j)   ⟺  L0 A N = c · L0 N
  ⟹ L0 N 与 L0 A N **成比例**（比值 c）⟹ 真平行 ✓（只要 L0 N ≠ 0）
  左零化子的维数 ≥ n − d ≥ 1，故总能取到 ✓

【判定】对这样的实例，找 (A) ∧ T5a 的 L，再检验 (S)。
  · (S) 失败 ⟹ c6′ 在一般 A 下也成立 ✓（结论更强）
  · (S) 成立 ⟹ **c6′ 假** ⟹ 情形 II 可为 YES ⟹ 分支 A 有硬度候选 ⭐⭐
"""
import os, io, contextlib, random, itertools
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]
_lx = {}
with open(os.path.join(_HERE, "linalg_exact.py"), encoding="utf-8") as fh:
    exec(compile(fh.read(), "lx", "exec"), _lx)
solve_exact = _lx["solve_exact"]
_, _, rank_exact, _ = (None, None, _lx["rank_exact"], None)

_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]

_ns2 = {}
for name in ["reliable_S_test.py"]:
    pth = os.path.join(_HERE, name)
    if os.path.exists(pth):
        with open(pth, encoding="utf-8") as fh:
            s = fh.read()
        pre = s.split("def main")[0]
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(pre, "s", "exec"), _ns2)


def solve_lin(Amat, bvec):
    """解 Amat · x = bvec（返回列表或 None）"""
    b = [[x] for x in bvec]
    r = solve_exact(Amat, b)
    if r is None: return None
    y = r[0] if isinstance(r, tuple) else r
    for i in range(len(Amat)):
        if sum(Amat[i][k] * y[k] for k in range(len(Amat[0]))) != bvec[i]:
            return None
    return y


def main():
    print("=== c6′ 在非 A-不变（一般 A）下成立？ ===\n")
    print("%-8s %4s %4s %6s %8s %8s %9s %9s %s" %
          ("trial", "n", "q0", "rkc", "A-不变", "平行", "(A)", "T5a", "(S)?"))
    print("-" * 84)
    rng = random.Random(8642)
    tot = 0
    s_fail = 0
    s_hold = 0
    for trial in range(600000):
        if tot >= 10: break
        n, p = 6, 1
        Ac = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        Wrow = Cc + mm(Cc, Ac)
        rW = rk(Wrow)
        d = n - rW
        if d < 2 or d > 5: continue
        N = ker_basis(Wrow)
        if not N or not N[0] or len(N[0]) != d: continue
        # A-不变性（列拼接）
        AN = mm(Ac, N)
        cj0 = [[N[i][j] for j in range(d)] + [AN[i][j] for j in range(d)]
               for i in range(n)]
        inv = (rk(cj0) == rk(N))
        if inv: continue                        # ★ 只要**非**不变的！
        # 取 c，构造左零化子
        cand = None
        for c in [F(0), F(1), F(-1), F(2), F(1, 2)]:
            vj = [[AN[i][j] - c * N[i][j] for j in range(d)] for i in range(n)]
            MT = [[vj[i][j] for i in range(n)] for j in range(d)]   # d×n
            Kb = ker_basis(MT)                                      # n×(n-r) 列存基
            if not Kb or not Kb[0]: continue
            ncol = len(Kb[0])
            bvecs = [[Kb[i][t] for i in range(len(Kb))] for t in range(ncol)]
            found_c = None
            for i1 in range(ncol):
                for i2 in range(ncol):
                    for a2 in [F(0), F(1), F(-1), F(2)]:
                        comb = [bvecs[i1][i] + a2 * bvecs[i2][i] for i in range(n)]
                        if all(x == 0 for x in comb): continue
                        pv = [sum(comb[i] * N[i][j] for i in range(n)) for j in range(d)]
                        if all(x == 0 for x in pv): continue
                        pvA = [sum(sum(comb[i] * Ac[i][k] for i in range(n)) * N[k][j]
                                   for k in range(n)) for j in range(d)]
                        if rk([pv, pvA]) != 1: continue
                        found_c = [comb]; break
                    if found_c: break
                if found_c: break
            if found_c:
                cand = found_c; break
        if not cand: continue
        L0 = cand
        try:
            _Lx, eta = p1(Ac, Cc, L0)
        except Exception:
            continue
        if not eta: continue
        q0 = sum(eta); k = q0 - 1
        if k < 1: continue
        # 找 (A) ∧ T5a 的 L
        found = None
        for _ in range(400):
            rows = [row[:] for row in L0]
            for _i in range(k):
                rows.append([F(rng.randint(-3, 3)) for _ in range(n)])
            L = rows
            if rk(mm(L, Ac) + L + Wrow) != rk(L + Wrow): continue
            if rk(mm(L, N)) < q0:
                found = L; break
        if found is None: continue
        L = found
        H = mm(L, N)
        if rk(H) == 0: continue
        tot += 1
        # ---- (S) 检验 ----
        # 解 L A = Lam L + G0 C + G1 CA
        # 未知：Lam (q0×q0), G0 (q0×p), G1 (q0×p)
        nA = q0 * q0 + 2 * q0 * p
        LA = mm(L, Ac)
        Rstack = [r[:] for r in L] + [r[:] for r in Cc] + [r[:] for r in mm(Cc, Ac)]
        # 逐行解：sum_k Lam[i][k] L[k][:] + ... = LA[i][:]
        # 构造大矩阵（行 q0 独立）
        sols = []
        okall = True
        for i in range(q0):
            # 未知量：Lam[i][0..q0-1], G0[i][0..p-1], G1[i][0..p-1]
            cols = []
            for kk in range(q0):
                cols.append([L[kk][j] for j in range(n)])
            for kk in range(p):
                cols.append([Cc[kk][j] for j in range(n)])
            for kk in range(p):
                cols.append([mm(Cc, Ac)[kk][j] for j in range(n)])
            # cols[u] 是第 u 个未知量对应的 n-向量；矩阵 A_{j,u} = cols[u][j]
            Amat = [[cols[u][j] for u in range(len(cols))] for j in range(n)]
            sol = solve_lin(Amat, [LA[i][j] for j in range(n)])
            if sol is None:
                okall = False; break
            sols.append(sol)
        if not okall: continue
        # (S): 对每个解，检验 rank((lam I - Lam) H) == rank H for all lam
        # 用 gcd 判据（reliable_S_test 的 rho 阶子式 gcd）→ 这里用简单多项式 gcd
        import math
        any_S = False
        for si in range(len(sols)):
            Lam = [[sols[si][k * q0 + i] for k in range(q0)] for i in range(q0)]
            # 简化：只检查有限个 lam 不充分 —— 改用"是否存在 lam 使秩降"
            # 用符号方式：检查 gcd of rho-minors of (lam I - Lam) H
            rho = rk(H)
            # (lam I - Lam) H 的条目是 lam 的一次多项式
            # 逐项：M[i][j] = lam*H[i][j] - sum_k Lam[i][k] H[k][j]
            MH = [[[H[i][j], -sum(Lam[i][k] * H[k][j] for k in range(q0))]
                   for j in range(len(H[0]))] for i in range(q0)]
            # 求 rho 阶子式的 gcd（多项式，系数为 Fraction）
            polys = []
            for rows in itertools.combinations(range(q0), rho):
                for colsc in itertools.combinations(range(len(H[0])), rho):
                    Msub = [[MH[i][j] for j in colsc] for i in rows]
                    det = poly_det(Msub, rho)
                    if det is not None and not all(x == 0 for x in det):
                        polys.append(det)
            if not polys: continue
            g = polys[0]
            for q in polys[1:]:
                g = poly_gcd(g, q)
                if len(g) == 1: break
            # (S) 失败 ⟺ gcd 非平凡（有根）⟺ deg g >= 1
            if len(g) - 1 >= 1:
                any_S = True
                break
        if any_S:
            s_fail += 1
        else:
            s_hold += 1
        print("%-8d %4d %4d %6d %8s %8s %9s %9s %s" %
              (trial, n, q0, rW, "**否**", "✓", "✓", "✓",
               "失败" if any_S else "**成立**"))
    print()
    print("非 A-不变实例：(S) 失败 %d 个，(S) 成立 %d 个" % (s_fail, s_hold))
    print()
    if s_hold:
        print("⟹ **c6′ 假（一般 A）** ⟹ 情形 II 可为 YES ⟹ 分支 A 有硬度候选 ⭐⭐")
    else:
        print("⟹ c6′ 在这些实例上仍成立（但机制未证）")


def poly_det(M, k):
    """多项式矩阵的行列式（系数为 Fraction 的列表，低次在前）"""
    if k == 1:
        return M[0][0][:]
    tot = [F(0)]
    for j in range(k):
        sub = [row[:j] + row[j + 1:] for row in M[1:]]
        d = poly_det(sub, k - 1) if k > 1 else None
        if d is None: return None
        # 乘以 M[0][j]
        prod = poly_mul(M[0][j], d)
        if j % 2 == 0:
            tot = poly_add(tot, prod)
        else:
            tot = poly_sub(tot, prod)
    return poly_trim(tot)


def poly_trim(p):
    while len(p) > 1 and p[-1] == 0:
        p = p[:-1]
    return p


def poly_add(a, b):
    n = max(len(a), len(b))
    return poly_trim([(a[i] if i < len(a) else F(0)) + (b[i] if i < len(b) else F(0))
                      for i in range(n)])


def poly_sub(a, b):
    n = max(len(a), len(b))
    return poly_trim([(a[i] if i < len(a) else F(0)) - (b[i] if i < len(b) else F(0))
                      for i in range(n)])


def poly_mul(a, b):
    if a == [F(0)] or b == [F(0)]: return [F(0)]
    r = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return poly_trim(r)


def poly_divmod(a, b):
    a = a[:]; b = poly_trim(b[:])
    if b == [F(0)]: return None
    db = len(b) - 1
    q = [F(0)] * max(1, len(a) - db)
    while len(a) - 1 >= db and not (len(a) == 1 and a[0] == 0):
        d = len(a) - 1 - db
        coef = a[-1] / b[-1]
        q[d] += coef
        for i in range(len(b)):
            a[d + i] -= coef * b[i]
        a = poly_trim(a)
    return poly_trim(q), a


def poly_gcd(a, b):
    a = poly_trim(a[:]); b = poly_trim(b[:])
    while not (len(b) == 1 and b[0] == 0):
        r = poly_divmod(a, b)
        if r is None: break
        a, b = b, r[1]
    # 归一化首项
    if len(a) > 1 and a[-1] != 0:
        lc = a[-1]
        a = [x / lc for x in a]
    return a


if __name__ == "__main__":
    main()
