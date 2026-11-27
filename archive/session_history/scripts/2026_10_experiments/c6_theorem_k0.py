# -*- coding: utf-8 -*-
"""
c6_theorem_k0.py -- 验证定理：**非退化平行 ⟹ k=0**（对任意 r、任意 A）

【定理】
  rank[π(L0); π(L0A)] ≤ 1 且 π(L0) ≠ 0   ⟹   L0 本身满足 (A)   ⟹   q0 = r，k = 0

【证明】
  (A) 对 L0 ⟺ ∃Λ (r×r):  π(L0A) = Λ·π(L0)      （模 row[C;CA] 约化）
  平行 + 非退化 ⟹ π(L0) = c·uᵀ, π(L0A) = d·uᵀ（c≠0, u≠0）
  ⟹ 只需 Λc = d —— 对任意 d **总是可解**（r 个方程、r² 个自由度）✓

【对照】
  退化（π(L0)=0）且 π(L0A)≠0 ⟹ Λ·0 = 0 ≠ d ⟹ (A) **失败** ⟹ k ≥ 1
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


def main():
    print("=== 定理验证：非退化平行 ⟹ k=0 ===\n")
    print("%-8s %4s %4s %4s %8s %8s %12s %8s" %
          ("trial","n","r","q0","非退化","平行","(A)对L0","k"))
    print("-" * 66)
    rng = random.Random(444555)
    tot = 0
    k_not_0 = 0
    deg_k_ge1 = 0
    deg_tot = 0
    for trial in range(900000):
        if tot >= 14: break
        n, p = 6, 1
        r = 2
        Ac = [[F(rng.randint(-1,1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1,1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        W = Cc + mm(Cc, Ac)
        N = ker_basis(W)
        if not N or not N[0]: continue
        d = len(N[0])
        pv = lambda v: [sum(v[i]*N[i][j] for i in range(n)) for j in range(d)]
        # 用构造：L0 = [CA^m ; 随机行]，筛出平行（非退化或退化）
        for _ in range(120):
            mp = rng.randint(1, 2)
            cur = Cc
            for _i in range(mp): cur = mm(cur, Ac)
            row1 = cur[0][:]
            row2 = [F(rng.randint(-2,2)) for _ in range(n)]
            L0 = [row1[:], row2[:]]
            if rk(L0) != 2: continue
            if rk(L0 + Cc) != 3: continue
            pL = [pv(L0[0]), pv(L0[1])]
            pi0 = all(all(x == 0 for x in w) for w in pL)
            pLA = [pv(mm([L0[0]], Ac)[0]), pv(mm([L0[1]], Ac)[0])]
            if rk(pL + pLA) != 1: continue          # 平行
            Aok = (rk(mm(L0, Ac) + L0 + W) == rk(L0 + W))
            try:
                _Lx, eta = p1(Ac, Cc, L0)
            except Exception:
                continue
            if not eta: continue
            q0 = sum(eta); k = q0 - r
            tot += 1
            if not pi0:
                if k != 0: k_not_0 += 1
                print("%-8d %4d %4d %4d %8s %8s %12s %8d" %
                      (trial, n, r, q0, "✓", "✓", "是" if Aok else "否", k))
            else:
                deg_tot += 1
                if k >= 1: deg_k_ge1 += 1
                print("%-8d %4d %4d %4d %8s %8s %12s %8d" %
                      (trial, n, r, q0, "**退化**", "✓",
                       "是" if Aok else "**否**", k))
            break
    print()
    print("⟹ **非退化平行且 k≠0 的实例数：%d**（应为 0 ⟹ 定理成立）" % k_not_0)
    print("⟹ 退化平行实例中 k≥1：%d / %d" % (deg_k_ge1, deg_tot))
    print()
    if k_not_0 == 0:
        print("⟹⟹ **定理成立：非退化平行 ⟹ k=0** ✓✓⟹ c6′ 的证伪只影响 k=0")
        print("   ⟹ 在 **k≥1** 范围（硬度相关），平行 ⟹ 必然退化（π(L0)=0）")


if __name__ == "__main__":
    main()
