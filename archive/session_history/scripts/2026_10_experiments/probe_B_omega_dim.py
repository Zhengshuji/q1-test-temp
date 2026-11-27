# -*- coding: utf-8 -*-
"""
probe_B_omega_dim.py —— 钉死支 B 的 Omega* 维数：正维数 还是 孤立点？

判据：若 Omega* 在某点 Θ₀ 附近含**开球**，则对随机小扰动仍成立（命中率 ~1）；
      若 Θ₀ 是孤立点，则小扰动几乎必失败（命中率 ~0）。
"""
import os, io, contextlib, random
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
head = src.split("rng = random.Random")[0]
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(head, "t", "exec"), _t)
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


def condA_norm(W, AT, BAT):
    WB = W + BAT
    return rk(WB + mm(W, AT)) == rk(WB)


def main():
    print("=== 支 B：Omega* 维数判定 ===\n")
    rng = random.Random(777)
    for trial in range(40000):
        n, p, r = 5, 1, 1
        for _ in range(200):
            Ac = Q.mat([[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)])
            Cc = Q.mat([[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)])
            Lc = Q.mat([[rng.randint(-2, 2) for _ in range(n)] for _ in range(r)])
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
            m = k * (s - k)
            # 找一个 (A)-点
            base = None
            for _ in range(3000):
                t = [F(rng.randint(-3, 3)) for _ in range(m)]
                if condA_norm(WJ_of(t, r, k, s, dC), AT, BAT):
                    base = t; break
            if base is None:
                continue          # 该实例没有 (A)-点，换下一个实例如
            print("实例 n=%d p=%d r=%d q0=%d k=%d s=%d  (支 B ✓)   Θ 维数 = %d"
                  % (n, p, r, q0, k, s, m))
            print("找到一个 (A)-点 Θ₀ =", [str(x) for x in base])
            # 在 Θ₀ 附近取小扰动（分母 16），看命中率
            hit = 0; total = 0
            for _ in range(300):
                pert = [base[i] + F(rng.randint(-1, 1), 16) for i in range(m)]
                total += 1
                if condA_norm(WJ_of(pert, r, k, s, dC), AT, BAT):
                    hit += 1
            print("  Θ₀ 附近小扰动（%d 个，步长 1/16）中 (A) 成立：%d  ⟹ 命中率 %.2f"
                  % (total, hit, hit / total))
            # 沿每个坐标轴方向做直线扫描：看是否整条线上的点都成立
            for a in range(m):
                line_hits = 0
                for v in range(-5, 6):
                    t2 = list(base); t2[a] = base[a] + F(v, 4)
                    if condA_norm(WJ_of(t2, r, k, s, dC), AT, BAT):
                        line_hits += 1
                print("    沿 Θ[%d] 直线（11 点，步长 1/4）：命中 %d" % (a, line_hits))
            print()
            print("  判读：")
            print("   · 附近命中率 ≈1 或沿直线全命中 ⟹ Omega* **含开集**（正维数）")
            print("   · 命中率 ≈0（仅 Θ₀）      ⟹ Θ₀ 是**孤立点**")
            print("   · 沿某方向全命中、其他方向不高 ⟹ Omega* 是**低维但正维数**的集合")
            return
    print("未找到合适实例")


if __name__ == "__main__":
    main()
