# -*- coding: utf-8 -*-
"""
c6_CRUX.py -- ⭐⭐⭐ 全项目关键检验

【背景】
  发现 1：项目的"真平行"实例（r=1）**全部退化**（π(L0)=0），16/16
  发现 2：**非退化**平行实例存在（r=2），但**全部 k=0**（L0 本身满足 (A)）
  理论：非退化平行 ⟹ L0A − λL0 ∈ row[C;CA] ⟹ L0 满足 (A) ⟹ k=0

【关键问题】
  在 k=0 的非退化平行实例上（q0 = r），(S) 是否成立？
  · (S) 成立 ⟹ **c6′ 假** ⟹ 情形 II 可为 YES ⟹ 分支 A 有硬度候选 ⭐⭐
  · (S) 失败 ⟹ c6′ 在这些实例上仍成立
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

_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]

# ---- 多项式工具 ----
def pt(p):
    while len(p) > 1 and p[-1] == 0: p = p[:-1]
    return p
def padd(a, b):
    n = max(len(a), len(b))
    return pt([(a[i] if i < len(a) else F(0)) + (b[i] if i < len(b) else F(0)) for i in range(n)])
def psub(a, b):
    n = max(len(a), len(b))
    return pt([(a[i] if i < len(a) else F(0)) - (b[i] if i < len(b) else F(0)) for i in range(n)])
def pmul(a, b):
    if a == [F(0)] or b == [F(0)]: return [F(0)]
    r = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] += x * y
    return pt(r)
def pdivmod(a, b):
    a = a[:]; b = pt(b[:])
    if b == [F(0)]: return None
    db = len(b) - 1
    q = [F(0)] * max(1, len(a) - db)
    while len(a) - 1 >= db and not (len(a) == 1 and a[0] == 0):
        d = len(a) - 1 - db
        co = a[-1] / b[-1]
        q[d] += co
        for i in range(len(b)): a[d + i] -= co * b[i]
        a = pt(a)
    return pt(q), a
def pgcd(a, b):
    a = pt(a[:]); b = pt(b[:])
    while not (len(b) == 1 and b[0] == 0):
        r = pdivmod(a, b)
        if r is None: break
        a, b = b, r[1]
    if len(a) > 1 and a[-1] != 0:
        lc = a[-1]; a = [x / lc for x in a]
    return a
def pdet(M, k):
    if k == 1: return M[0][0][:]
    tot = [F(0)]
    for j in range(k):
        sub = [row[:j] + row[j+1:] for row in M[1:]]
        d = pdet(sub, k-1)
        pr = pmul(M[0][j], d)
        tot = padd(tot, pr) if j % 2 == 0 else psub(tot, pr)
    return pt(tot)


def solve_lin(Amat, bvec):
    b = [[x] for x in bvec]
    r = solve_exact(Amat, b)
    if r is None: return None
    y = r[0] if isinstance(r, tuple) else r
    for i in range(len(Amat)):
        if sum(Amat[i][k] * y[k] for k in range(len(Amat[0]))) != bvec[i]:
            return None
    return y


def s_fails(Lm, Ac, Cc, N, q0, g):
    """(S) 是否**失败**（存在 lam 使秩降）？返回 (fails, nsols)"""
    CAc = mm(Cc, Ac)
    LA = mm(Lm, Ac)
    H = mm(Lm, N)
    rho = rk(H)
    if rho == 0: return None, 0
    # 逐行解 LA[i] = sum_k Lam[i][k] L[k] + G0[i] C + G1[i] CA
    sols = []
    for i in range(q0):
        cols = []
        for kk in range(q0): cols.append([Lm[kk][j] for j in range(len(LA[0]))])
        for kk in range(len(Cc)): cols.append([Cc[kk][j] for j in range(len(LA[0]))])
        for kk in range(len(Cc)): cols.append([CAc[kk][j] for j in range(len(LA[0]))])
        Amat = [[cols[u][j] for u in range(len(cols))] for j in range(len(LA[0]))]
        sol = solve_lin(Amat, [LA[i][j] for j in range(len(LA[0]))])
        if sol is None: return None, 0
        sols.append(sol)
    AnyFail = False
    for si in range(len(sols)):
        Lam = [[sols[si][k * q0 + i] for k in range(q0)] for i in range(q0)]
        # (lam I - Lam) H 的条目为 lam 的一次多项式
        MH = [[[H[i][j], -sum(Lam[i][k] * H[k][j] for k in range(q0))]
               for j in range(len(H[0]))] for i in range(q0)]
        polys = []
        for rows in itertools.combinations(range(q0), rho):
            for csc in itertools.combinations(range(len(H[0])), rho):
                sub = [[MH[i][j] for j in csc] for i in rows]
                d = pdet(sub, rho)
                if d is not None and not all(x == 0 for x in d): polys.append(d)
        if not polys: continue
        gg = polys[0]
        for q in polys[1:]:
            gg = pgcd(gg, q)
            if len(gg) == 1: break
        if len(gg) - 1 >= 1: AnyFail = True; break
    return AnyFail, len(sols)


def main():
    print("=== CRUX：非退化平行 + k=0 实例上 (S) 是否成立？ ===\n")
    print("%-8s %4s %4s %4s %8s %7s %7s %s" %
          ("trial", "n", "q0", "k", "rkH", "π(L0)≠0", "(S)?", "结论"))
    print("-" * 62)
    rng = random.Random(1357911)
    tot = 0
    yes_cnt = 0
    for trial in range(900000):
        if tot >= 8: break
        n, p = 6, 1
        r = 2
        Ac = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        W = Cc + mm(Cc, Ac)
        N = ker_basis(W)
        if not N or not N[0]: continue
        d = len(N[0])
        pv = lambda v: [sum(v[i] * N[i][j] for i in range(n)) for j in range(d)]
        # 只取 k=0 的：L0 本身满足 (A)
        found = None
        for _ in range(120):
            mp = rng.randint(1, 2)
            row1 = mm(Cc, [[F(1) if i == j else F(0) for j in range(n)]
                           for i in range(n)])[0] if False else mm(Cc, Ac)[0]
            row2 = [F(rng.randint(-2, 2)) for _ in range(n)]
            L0 = [row1, row2]
            if rk(L0) != r: continue
            if rk(L0 + Cc) != r + p: continue
            if rk(mm(L0, Ac) + L0 + W) != rk(L0 + W): continue   # L0 满足 (A)
            pL = [pv(L0[0]), pv(L0[1])]
            if all(all(x == 0 for x in w) for w in pL): continue  # 非退化
            pLA = [pv(mm([L0[0]], Ac)[0]), pv(mm([L0[1]], Ac)[0])]
            if rk(pL + pLA) != 1: continue                        # 平行
            found = L0; break
        if found is None: continue
        L0 = found
        try:
            _Lx, eta = p1(Ac, Cc, L0)
        except Exception:
            continue
        if not eta: continue
        q0 = sum(eta); k = q0 - r
        if k != 0: continue
        H = mm(L0, N)
        if rk(H) == 0: continue
        if rk(H) >= q0: continue          # 需 T5a: rank H < q0
        res, ns = s_fails(L0, Ac, Cc, N, q0, 0)
        if res is None: continue
        tot += 1
        if not res: yes_cnt += 1     # (S) 成立 ⟹ c6′ 假
        print("%-8d %4d %4d %4d %8d %7s %7s %s" %
              (trial, n, q0, k, rk(H), "✓", "失败" if res else "**成立**",
               "" if res else "⭐⭐ c6′ 假？"))
    print()
    print("非退化平行 + k=0 + T5a 实例数：%d" % tot)
    print("其中 (S) 失败：%d，(S) 成立：%d" % (tot - yes_cnt, yes_cnt))
    print()
    if yes_cnt:
        print("⟹ ⟹⟹ **发现 (S) 成立的实例** ⟹ c6′ 在这些情形下**假** ⭐⭐")
        print("    ⟹ 情形 II 可为 YES ⟹ 分支 A 有硬度候选！")
    else:
        print("⟹ (S) 全部失败 ⟹ c6′ 在这些实例上仍成立")


if __name__ == "__main__":
    main()
