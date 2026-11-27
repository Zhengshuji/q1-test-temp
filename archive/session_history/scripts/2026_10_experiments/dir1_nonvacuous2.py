# -*- coding: utf-8 -*-
"""
dir1_nonvacuous2.py —— 精确判据：何时 (A) 非空洞？

【推导】
  (A) ⟺ 全部 (ρ+1) 阶子式 = 0，其中 ρ = rk[W(Θ);B]。
  · 若 ρ = d_C（最大可能）⟹ (ρ+1) 阶子式**不存在** ⟹ 条件**空洞** ✗
  · 若 ρ < d_C ⟹ 存在 (ρ+1) 阶子式 ⟹ 条件**有条件力** ✓

  [W(Θ);B] 的行数 = (r+k) + k = r+2k，列数 = d_C
  ⟹ rk ≤ min(r+2k, d_C)
  ⟹ 非空洞要求：r + 2k > d_C 是不可能的，需 min(r+2k, d_C) < d_C
  ⟹ **必要**：r + 2k < d_C

【本脚本】用精确的 (A) 判据（逐点比较 rank[M] 与 rank[WB]）核实。
"""
import os, io, contextlib, itertools, random
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]


def WJ(t, r, k, s, dC):
    W = [[F(1) if j == i else F(0) for j in range(dC)] for i in range(r)]
    idx = 0
    for i in range(k):
        row = [F(0)] * dC
        row[r + i] = F(1)
        for j in range(k, s):
            row[r + j] = t[idx]; idx += 1
        W.append(row)
    return W


def check(AT, BAT, r, k, s, dC, n_th=60, rng=None):
    """返回：(rho 的一般值, 是否存在 Θ 使 rank[M]>rank[WB]（⟹(A) 有条件力）)"""
    rng = rng or random.Random(1)
    m = k * (s - k)
    maxWB = 0; maxdiff = 0
    for _ in range(n_th):
        t = [F(rng.randint(-3, 3)) for _ in range(m)]
        W = WJ(t, r, k, s, dC)
        WB = W + BAT
        M = WB + mm(W, AT)
        rWB = rk(WB); rM = rk(M)
        maxWB = max(maxWB, rWB)
        maxdiff = max(maxdiff, rM - rWB)
    return maxWB, maxdiff


def main():
    print("=== 精确判据：$(A)$ 非空洞 ⟺ r+2k < d_C ===\n")
    print("%-22s %6s %8s %8s %10s %10s" %
          ("(r,k,s,dC)", "r+2k", "maxWB", "maxDiff", "子式存在?", "非空洞?"))
    print("-" * 70)
    rng = random.Random(17)
    for (r, k, s, dC) in [(1,1,3,4), (1,1,4,5), (1,2,3,4), (1,2,4,5), (1,2,4,6),
                          (1,2,5,6), (1,3,4,5), (1,3,5,6), (1,3,5,7), (2,2,4,6),
                          (1,2,4,7), (1,2,6,7)]:
        m = k * (s - k)
        agg = (0, 0)
        for _ in range(25):
            AT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(dC)]
            BAT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(k)]
            a, d = check(AT, BAT, r, k, s, dC, rng=rng)
            agg = (max(agg[0], a), max(agg[1], d))
        exists_minor = agg[0] < dC
        nonvac = agg[1] > 0
        print("%-22s %6d %8d %8d %10s %10s"
              % ("(%d,%d,%d,%d)" % (r,k,s,dC), r+2*k, agg[0], agg[1],
                 "✓" if exists_minor else "✗(ρ=dC)",
                 "✓" if nonvac else "✗ 空洞"))
    print()
    print("【判读】")
    print("  · r+2k < d_C ⟹ 存在 (ρ+1) 阶子式 ⟹ (A) 有条件力 ✓")
    print("  · r+2k ≥ d_C ⟹ ρ 可达 d_C ⟹ 条件空洞 ✗")
    print()
    print("  ⟹ 归约必须落在 **r+2k < d_C** 的形状上")


if __name__ == "__main__":
    main()
