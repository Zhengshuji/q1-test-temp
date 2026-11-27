# -*- coding: utf-8 -*-
"""
probe_B_omega_shape.py —— 支 B 的 Omega* 到底是"有限孤立点"还是"正维数集"？

【背景】
  FINAL.md §8 说：支 B（2p+q0 < n）的解集是**有限个孤立点**（零测，采样命中率恒 0）。
  但 parametrization（P1 Thm 3）：最小 (A)-增广 = W_J(Θ)，其中
      J ⊆ {1,...,s}, |J| = k,  Θ ∈ R^{k×(s-k)}
  ⟹ Θ 的参数空间维数是 k(s-k)。当 k=1 且 s>k 时维数 = s-1 ≥ 1 ⟹ **正维数**！

  ⟹ 二者矛盾。本脚本用**直接检验**判定：Omega* 是正维数还是孤立点。

【做法】
  对 k=1, p=1 的小形状（s > k），构造 W_J(Θ)（r+k 行），直接检验 (A)：
      (A) ⟺ rank[W; B; W·Ā] == rank[W; B]
  在若干 Θ 上取值，看 (A) 成立的 Θ 是否构成正维数集（随机点命中）还是孤立点（命中率 0）。
"""
import os, io, contextlib, random
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]

import linalg_q as Q


# ---------------- 从 test_caseII_YES 复用实例构造 ----------------
_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    src = fh.read()
head = src.split("rng = random.Random")[0]
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(head, "t", "exec"), _t)
build_norm_T = _t.get("build_norm_T")
p1 = _t.get("p1")


def WJ_of(t, r, k, s, dC):
    """P1 的 W_J(Θ)：前 r 行 = [I_r | 0]，后 k 行 = [0 | I_k | Θ]"""
    W = []
    for i in range(r):
        W.append([F(1) if j == i else F(0) for j in range(dC)])
    idx = 0
    for i in range(k):
        row = [F(0)] * dC
        row[r + i] = F(1)
        for j in range(k, s):
            row[r + j] = t[idx]; idx += 1
        W.append(row)
    return W


def condA_norm(W, AT, BAT):
    """规范化坐标下的 (A)：rank[W; B; W·Ā] == rank[W; B]"""
    WB = W + BAT
    WA = mm(W, AT)
    return rk(WB + WA) == rk(WB)


def main():
    print("=== 支 B 的 Omega* 形状判定 ===\n")
    rng = random.Random(20260101)
    # 找 k=1 且 s>k 的实例（支 B 需要 2p+q0 < n，即 p 小、q0 小）
    found = False
    for trial in range(40000):
        n, p, r = 5, 1, 1
        for _ in range(200):
            Am = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
            Cm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)]
            Lm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(r)]
            Ac, Cc, Lc = Q.mat(Am), Q.mat(Cm), Q.mat(Lm)
            if Q.rank(Cc) != p or Q.rank(Lc) != r: continue
            if Q.rank(Lc + Cc) != r + p: continue
            try:
                Lx, eta = p1(Ac, Cc, Lc)
            except Exception:
                continue
            if not Lx: continue
            q0 = sum(eta)
            k = q0 - r
            if k != 1: continue
            bt = build_norm_T(Ac, Cc, Lc, Lx)
            if bt is None: continue
            dC, s, k2, r2, AT, BAT = bt
            if (r2, k2) != (r, k) or s <= k: continue
            # 支 B 条件：2p+q0 < n
            if 2 * p + q0 >= n: continue
            print("实例: n=%d p=%d r=%d q0=%d k=%d s=%d  (2p+q0=%d < n=%d ✓ 支 B)"
                  % (n, p, r, q0, k, s, 2 * p + q0, n))
            print("  Θ 参数空间维数 = k(s-k) = %d" % (k * (s - k)))
            print()
            m = k * (s - k)
            hits = 0
            trials = 400
            for _ in range(trials):
                t = [F(rng.randint(-4, 4)) for _ in range(m)]
                W = WJ_of(t, r, k, s, dC)
                if condA_norm(W, AT, BAT):
                    hits += 1
            print("  随机 Θ（%d 个）中 (A) 成立者：%d   （若 >0 ⟹ Omega* **正维数**）"
                  % (trials, hits))
            # 再看 Θ=0 与几个特殊点
            for name, t in [("Θ=0", [F(0)] * m),
                            ("Θ=全1", [F(1)] * m)]:
                W = WJ_of(t, r, k, s, dC)
                print("    %-6s (A) 成立？ %s" % (name, condA_norm(W, AT, BAT)))
            found = True
            break
        if found: break
    if not found:
        print("未找到 k=1 且 s>k 的支 B 实例（可放宽搜索）")


if __name__ == "__main__":
    main()
