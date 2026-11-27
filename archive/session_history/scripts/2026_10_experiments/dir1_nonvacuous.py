# -*- coding: utf-8 -*-
"""
dir1_nonvacuous.py —— 方向 1 / 子任务 1.1：找**非空洞**的 (Ā,B̄)

【判据】
  (A) ⟺ rank[W(Θ);B;W(Θ)Ā] = rank[W(Θ);B]    （对 Θ 成立）
  若对**一般** Θ 都有 rank[M] = rank[WB]，则 (A) 空洞（无条件力）✗
  若存在 Θ 使 rank[M] > rank[WB]，则 (A) 是**真条件** ✓

【做法】随机取 (Ā,B̄)，在多个 Θ 上比较 rank[M] 与 rank[WB]，
        统计"存在 rank 差"的比例。
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


def analyze(AT, BAT, r, k, s, dC, n_th=40, rng=None):
    """返回 (rank[WB] 的一般值, 出现过的 rank[M] 最大值, 非空洞?)"""
    rng = rng or random.Random(1)
    m = k * (s - k)
    maxWB = 0; maxM = 0; diffs = 0
    for _ in range(n_th):
        t = [F(rng.randint(-3, 3)) for _ in range(m)]
        W = WJ(t, r, k, s, dC)
        WB = W + BAT
        M = WB + mm(W, AT)
        rWB = rk(WB); rM = rk(M)
        maxWB = max(maxWB, rWB); maxM = max(maxM, rM)
        if rM > rWB: diffs += 1
    return maxWB, maxM, diffs


def main():
    print("=== 方向 1 / 1.1：找非空洞实例 ===\n")
    print("%-24s %8s %8s %8s %10s" % ("(r,k,s,dC)", "max rk[WB]", "max rk[M]", "有秩差?", "非空洞?"))
    print("-" * 66)
    rng = random.Random(5)
    found = 0
    for (r, k, s, dC) in [(1,1,3,4), (1,1,4,5), (1,2,3,4), (1,2,4,5), (1,2,4,6),
                          (1,2,5,6), (1,3,4,5), (1,3,5,6), (2,1,3,5), (2,2,4,6)]:
        m = k * (s - k)
        best = (0, 0, 0)
        for _ in range(30):
            AT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(dC)]
            BAT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(k)]
            a, b, d = analyze(AT, BAT, r, k, s, dC, rng=rng)
            if d > best[2]: best = (a, b, d)
        nonvac = best[2] > 0
        if nonvac: found += 1
        print("%-24s %8d %8d %8d %10s"
              % ("(%d,%d,%d,%d)" % (r,k,s,dC), best[0], best[1], best[2],
                 "✓ 非空洞" if nonvac else "✗ 空洞"))
    print()
    print("⟹ 在 30×10 个随机 (Ā,B̄) 中，找到非空洞形状 %d 个" % found)
    print()
    print("【判读】")
    print("  · 若多数形状**非空洞** ⟹ (A) 有约束力 ⟹ 归约有希望 ✓")
    print("  · 若多数**空洞** ⟹ 需特殊构造 (Ā,B̄) 才非空洞 ⟹ 归约更难")


if __name__ == "__main__":
    main()
