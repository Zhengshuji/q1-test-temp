# -*- coding: utf-8 -*-
"""
probe_B_dim3.py —— 支 B：快速判定 Omega* 的维数

策略：先找一个 **Ω* 非空** 的支 B 实例（这是关键前提，很多实例 Ω* 为空），
再在找到的 (A)-点附近测试命中率，并做**沿各方向的直线扫描**。
"""
import os, io, contextlib, random, sys
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]

import linalg_q as Q

_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split("rng = random.Random")[0], "t", "exec"), _t)
build_norm_T = _t["build_norm_T"]; p1 = _t["p1"]


def WJ_of(t, r, k, s, dC):
    W = []
    for i in range(r):
        W.append([F(1) if j == i else F(0) for j in range(dC)])
    idx = 0
    for i in range(k):
        row = [F(0)] * dC
        row[r + i] = F(1)
        for j in range(k, s):
            row[r + j] = t[idx]; idx += 1
    return W


def condA(W, AT, BAT):
    WB = W + BAT
    return rk(WB + mm(W, AT)) == rk(WB)


def main():
    print("=== 支 B：Omega* 维数快速判定 ===\n")
    rng = random.Random(31415)
    grid = [F(a) for a in range(-2, 3)]
    best = None
    checked = 0
    for trial in range(6000):
        n, p, r = 5, 1, 1
        for _ in range(40):
            Ac = Q.mat([[rng.randint(-1, 1) for _ in range(n)] for _ in range(n)])
            Cc = Q.mat([[rng.randint(-1, 1) for _ in range(n)] for _ in range(p)])
            Lc = Q.mat([[rng.randint(-1, 1) for _ in range(n)] for _ in range(r)])
            if Q.rank(Cc) != p or Q.rank(Lc) != r: continue
            if Q.rank(Lc + Cc) != r + p: continue
            try:
                Lx, eta = p1(Ac, Cc, Lc)
            except Exception:
                continue
            if not Lx: continue
            q0 = sum(eta); k = q0 - r
            if k != 1: continue
            bt = build_norm_T(Ac, Cc, Lc, Lx)
            if bt is None: continue
            dC, s, k2, r2, AT, BAT = bt
            if (r2, k2) != (r, k) or s <= k: continue
            if 2 * p + q0 >= n: continue
            checked += 1
            m = k * (s - k)
            # 快速筛：网格上找 (A)-点
            found = None
            for a in grid:
                for b in grid:
                    if condA(WJ_of([a, b], r, k, s, dC), AT, BAT):
                        found = [a, b]; break
                if found: break
            if found:
                best = (n, p, r, q0, k, s, dC, AT, BAT, found)
                break
        if best: break
    print("检查过的支 B 实例数：%d" % checked)
    if not best:
        print("未找到 Ω* 非空的支 B 实例")
        return
    n, p, r, q0, k, s, dC, AT, BAT, base = best
    m = k * (s - k)
    print("实例 n=%d p=%d r=%d q0=%d k=%d s=%d  (2p+q0=%d<n=%d)  Θ 维数=%d"
          % (n, p, r, q0, k, s, 2 * p + q0, n, m))
    print("找到的 (A)-点 Θ₀ =", [str(x) for x in base], "\n")
    hit = sum(1 for _ in range(400)
              if condA(WJ_of([base[i] + F(rng.randint(-1, 1), 32) for i in range(m)],
                             r, k, s, dC), AT, BAT))
    print("Θ₀ 附近小扰动 400 个（步长 1/32）中 (A) 成立：%d  ⟹ 命中率 %.3f"
          % (hit, hit / 400))
    for a in range(m):
        lh = sum(1 for v in range(-6, 7)
                 if condA(WJ_of([base[i] + (F(v, 4) if i == a else F(0)) for i in range(m)],
                                r, k, s, dC), AT, BAT))
        print("   沿 Θ[%d] 直线（13 点，步长 1/4）：命中 %d / 13" % (a, lh))
    print("\n【判读】命中率≈1 或直线全命中 ⟹ Ω* 含开集（**正维数**）")


if __name__ == "__main__":
    main()
