# -*- coding: utf-8 -*-
"""
probe_B_omega_dim2.py —— 支 B 的 Omega* 维数（快速版）

复用 probe_B_omega_shape.py 里已确认可行的实例搜索（上限 40000×200），
但一旦找到 k=1, s>k, 支B 的实例就**立即**做维数判定。
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
    print("=== 支 B：Omega* 维数判定（快速版）===\n")
    rng = random.Random(777)
    target = None
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
            # 要求至少有一个 (A)-点（否则该实例 Ω* 为空，不用于维数判定）
            has = any(condA_norm(WJ_of([F(a), F(b)], r, k, s, dC), AT, BAT)
                      for a in range(-2, 3) for b in range(-2, 3))
            if not has:
                continue
            target = (n, p, r, q0, k, s, dC, AT, BAT)
            break
        if target: break
    if not target:
        print("未找到支 B 实例")
        return
    n, p, r, q0, k, s, dC, AT, BAT = target
    m = k * (s - k)
    print("实例 n=%d p=%d r=%d q0=%d k=%d s=%d   (2p+q0=%d < n=%d ✓ 支 B)"
          % (n, p, r, q0, k, s, 2 * p + q0, n))
    print("Θ 参数空间维数 = k(s-k) = %d\n" % m)

    # 1) Θ=0 是否 (A)-点
    ok0 = condA_norm(WJ_of([F(0)] * m, r, k, s, dC), AT, BAT)
    print("Θ=0 是 (A)-点？", ok0)

    # 2) 找任意一个 (A)-点（若 Θ=0 不是）
    base = [F(0)] * m
    if not ok0:
        base = None
        for _ in range(20000):
            t = [F(rng.randint(-3, 3)) for _ in range(m)]
            if condA_norm(WJ_of(t, r, k, s, dC), AT, BAT):
                base = t; break
        print("搜索到 (A)-点？", base is not None)
    if base is None:
        return
    print("Θ₀ =", [str(x) for x in base])

    # 3) 小扰动命中率
    hit = 0; total = 0
    for _ in range(400):
        pert = [base[i] + F(rng.randint(-1, 1), 32) for i in range(m)]
        total += 1
        if condA_norm(WJ_of(pert, r, k, s, dC), AT, BAT):
            hit += 1
    print("\nΘ₀ 附近小扰动（%d 个，步长 1/32）中 (A) 成立：%d  ⟹ 命中率 %.3f"
          % (total, hit, hit / total))

    # 4) 沿各坐标轴的直线扫描
    for a in range(m):
        lh = 0
        for v in range(-6, 7):
            t2 = list(base); t2[a] = base[a] + F(v, 4)
            if condA_norm(WJ_of(t2, r, k, s, dC), AT, BAT):
                lh += 1
        print("   沿 Θ[%d] 直线（13 点，步长 1/4）：命中 %d" % (a, lh))

    print("\n【判读】")
    print("  命中率 ≈1 或直线全命中 ⟹ Omega* **含开集**（正维数）")
    print("  命中率 ≈0 且直线只命中 1 点 ⟹ Θ₀ 是**孤立点**")


if __name__ == "__main__":
    main()
