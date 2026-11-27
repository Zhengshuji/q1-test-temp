# -*- coding: utf-8 -*-
"""
b2_criterion.py —— 引理 A 的**精确判据**验证

【推导】
  设 δ 是"一阶保持"方向（即 J·δ = 0）。
  可证 δ ∈ row[W(0);B;W(0)Ā]（因为 v(εδ) 必须在行空间中）。
  而 δ 只支撑在 Θ-坐标（最后 s-1 = m 列）上：
      W(0) 的可变行 = [0,...,0, 1, 0,...,0]（前 r+k 列定，后 m 列 = Θ）
      δ 是该行的增量 ⟹ δ 前 r+k 列为 0 ✓
  ⟹ δ = Σ_i c_i · (第 i 行)  且 δ|_{前 r+k 列} = 0
  ⟹ **δ ∈ row-space 由 θ-列块张成的子空间**

  ⟹ 判据： [W(0);B;W(0)Ā] 的 **θ-列块**（后 m 列）的**行秩** = m ？
      （若 = m，则任何"组合出 δ"的行组合都唯一确定，且前 r+k 列条件迫使 c=0 ⟹ δ=0）

【本脚本】直接验证：该 θ-列块的秩（= 行秩）是否 = m = s-1
"""
import os, io, contextlib, itertools, random
from fractions import Fraction as Fr
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]
_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]; build_norm_T = _t["build_norm_T"]


def get_instance(n, want_s, seed, tries=150000):
    rng = random.Random(seed)
    for _ in range(tries):
        Ac = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        Lc = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        if rk(Cc) != 1 or rk(Lc) != 1 or rk(Lc + Cc) != 2: continue
        try: Lx, eta = p1(Ac, Cc, Lc)
        except Exception: continue
        if not Lx: continue
        q0 = sum(eta); k = q0 - 1
        if k != 1: continue
        bt = build_norm_T(Ac, Cc, Lc, Lx)
        if bt is None: continue
        dC, s, k2, r2, AT, BAT = bt
        if (r2, k2) != (1, 1) or s != want_s: continue
        if 2 + q0 >= n: continue
        return dict(dC=dC, s=s, AT=AT, BAT=BAT)
    return None


def main():
    print("=== 引理 A 的精确判据：θ-列块的秩 ===")
    print("%-14s %3s %5s %6s %10s %10s" %
          ("(k,s)", "r+k", "dC", "m=s-1", "θ块秩", "=m?"))
    print("-" * 56)
    ok = tot = 0
    for ss, n in [(3, 5), (4, 6), (5, 7), (6, 8)]:
        for t in range(3):
            inst = get_instance(n, ss, 20370000 + 100 * ss + t)
            if inst is None: continue
            dC, s, AT, BAT = inst["dC"], inst["s"], inst["AT"], inst["BAT"]
            r, k = 1, 1; m = s - 1
            # [W(0);B]（数值）
            W0 = [[Fr(1) if j == i else Fr(0) for j in range(dC)] for i in range(r)]
            row = [Fr(0)] * dC
            row[r + k - 1] = Fr(1)
            # 注意：Θ=0 时可变行的 θ-部分全为 0，故该行 = [0,...,0,1,0,...,0]
            W0.append(row)
            WB0 = W0 + BAT
            # W(0)Ā
            WA0 = mm(W0, AT)
            K = WB0 + WA0
            # θ-列块：后 m 列
            th_blk = [[K[i][dC - m + j] for j in range(m)] for i in range(len(K))]
            rkb = len(sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row]
                                 for row in th_blk]).rref()[1])
            good = (rkb == m)
            tot += 1; ok += 1 if good else 0
            print("%-14s %3d %5d %6d %10d %10s"
                  % ("(1,%d)#%d" % (ss, t), r + k, dC, m, rkb, good))
        print()
    print("⟹ θ-列块满秩（秩 = m）: %d/%d" % (ok, tot))
    if ok == tot and tot:
        print("⟹ **判据成立**：δ 必须在 row[W(0);B;W(0)Ā] 中，而 θ-列块行满秩")
        print("   且 δ 的前 r+k 列为 0 ⟹ δ = 0 ⟹ ker J = 0 ⟹ 引理 A ✓")


if __name__ == "__main__":
    main()
