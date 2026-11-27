# -*- coding: utf-8 -*-
"""
c6_degenerate2.py -- r=2 情形：是否存在**非退化**的平行实例？

【理论】
  r=2 时"平行"= rank[π(L0); π(L0A)] ≤ 1（4 行全部成比例于同一 u）
  非退化 = π(L0) ≠ 0

  **不变 A**：π(L0A) = π(L0)A' ⟹ 平行 ⟺ u 是 A' 的左特征向量
            ⟹ L0A − λL0 ∈ row[C;CA] ⟹ **L0 本身满足 (A)** ⟹ k=0

  **非不变 A**：需"比值不同"结构（ratio-differing）⟹ 需 CA³|_K ∥ CA²|_K
"""
import os, io, contextlib, random
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]

_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]


def matpow(M, k):
    n = len(M)
    R = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = mm(R, M)
    return R


def main():
    print("=== r=2：非退化平行实例存在吗？ ===\n")
    print("%-8s %4s %4s %4s %8s %10s %10s %8s" %
          ("trial", "n", "q0", "k", "A-不变", "π(L0)=0?", "平行", "L0满足A?"))
    print("-" * 68)
    rng = random.Random(123321)
    tot = 0
    deg = 0
    nondeg = 0
    for trial in range(900000):
        if tot >= 14: break
        n, p = 6, 1
        r = 2
        Ac = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        # L0 = 两行：C A^m 与随机行
        mp = rng.randint(1, 2)
        row1 = mm(Cc, matpow(Ac, mp))[0]
        row2 = [F(rng.randint(-2, 2)) for _ in range(n)]
        L0 = [row1, row2]
        if rk(L0) != r: continue
        if rk(L0 + Cc) != r + p: continue
        W = Cc + mm(Cc, Ac)
        N = ker_basis(W)
        if not N or not N[0]: continue
        d = len(N[0])
        AN = mm(Ac, N)
        cj0 = [[N[i][j] for j in range(d)] + [AN[i][j] for j in range(d)]
               for i in range(n)]
        inv = (rk(cj0) == rk(N))
        pv = lambda v: [sum(v[i] * N[i][j] for i in range(n)) for j in range(d)]
        pL0 = [pv(L0[0]), pv(L0[1])]
        pL0A = [pv(mm([L0[0]], Ac)[0]), pv(mm([L0[1]], Ac)[0])]
        pi0 = all(all(x == 0 for x in row) for row in pL0)
        par = (rk(pL0 + pL0A) == 1)
        if not par: continue
        A_for_L0 = (rk(mm(L0, Ac) + L0 + W) == rk(L0 + W))
        try:
            _Lx, eta = p1(Ac, Cc, L0)
        except Exception:
            continue
        if not eta: continue
        q0 = sum(eta); k = q0 - r
        tot += 1
        if pi0: deg += 1
        else: nondeg += 1
        print("%-8d %4d %4d %4d %8s %10s %10s %8s" %
              (trial, n, q0, k, "是" if inv else "**否**",
               "**是**" if pi0 else "否", "✓",
               "是" if A_for_L0 else "**否**"))
    print()
    print("平行实例：%d   退化：%d   非退化：%d" % (tot, deg, nondeg))
    print()
    if nondeg == 0:
        print("⟹ **全部退化** ⟹ c6′ 的实证只覆盖退化分支 ⚠️⚠️")
    else:
        print("⟹ 存在非退化实例（见上表）")


if __name__ == "__main__":
    main()
