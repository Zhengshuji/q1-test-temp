# -*- coding: utf-8 -*-
"""
dir1_direction_check.py —— 归约**方向**的逻辑核实 + 弱归约的可行性

【逻辑（必须搞清）】
  记 $(A)$ 的多项式系统为 $\mathcal I$（由 $(\rho{+}1)$ 阶子式生成），
  目标系统为 $\mathcal T$（如 1-in-3-SAT 的二次约束）。

  · 若 $\mathcal I\subseteq\mathcal T$（即 $\mathcal I$ 蕴含更多方程）
    ⟹ $V(\mathcal T)\subseteq V(\mathcal I)$
    ⟹ $(A)$ 的解集**更大** ⟹ $(A)$ **更容易**
    ⟹ 不能由此得 NP-hard ✗

  · 若 $\mathcal T\subseteq\mathcal I$
    ⟹ $V(\mathcal I)\subseteq V(\mathcal T)$
    ⟹ $(A)$ 的解集**更小**（更难）
    ⟹ $\mathcal T$ 难 ⟹ $\mathcal I$ 难 ⟹ **得 NP-hard** ✓

【本脚本】对最小形状，用 Groebner 检验：
   能否构造 (Ā,B̄) 使 (A)-理想 **包含** 给定二次式（如 θ0²-θ0）？
"""
import os, io, contextlib, itertools, random
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]

import sympy as sp


def A_ideal(AT, BAT, r, k, s, dC, th, rho):
    W = [[sp.Integer(1) if j == i else sp.Integer(0) for j in range(dC)] for i in range(r)]
    idx = 0
    for i in range(k):
        row = [sp.Integer(0)] * dC
        row[r + i] = sp.Integer(1)
        for j in range(k, s):
            row[r + j] = th[idx]; idx += 1
        W.append(row)
    R = lambda M: [[sp.Rational(x.numerator, x.denominator) for x in row] for row in M]
    ATs, BATs = R(AT), R(BAT)
    WAs = [[sp.expand(sum(W[i][a] * ATs[a][j] for a in range(len(ATs))))
            for j in range(dC)] for i in range(len(W))]
    WBs = [row[:] for row in W] + [row[:] for row in BATs]
    MBs = [row[:] for row in W] + [row[:] for row in BATs] + [row[:] for row in WAs]
    nr, nc = len(MBs), len(MBs[0])
    polys = []
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            d = sp.expand(sp.Matrix([[MBs[i][j] for j in cj] for i in ri]).det())
            if d != 0 and d not in polys:
                polys.append(d)
    # 一般秩
    if rho is None:
        pass
    return polys


def main():
    print("=== 归约方向核实 + 弱归约可行性 ===\n")
    r, k, s, dC = 1, 2, 3, 4
    m = k * (s - k)
    th = sp.symbols('t0:%d' % m)
    print("形状 (r=%d,k=%d,s=%d,dC=%d)，Θ 维数 m=%d\n" % (r, k, s, dC, m))

    print("【逻辑澄清】")
    print("  (A) 的方程集 I，目标方程集 T：")
    print("   · I ⊆ T ⟹ V(T) ⊆ V(I) ⟹ (A) 解集更大 ⟹ (A) 更容易 ⟹ 不能得 NP-hard ✗")
    print("   · T ⊆ I ⟹ V(I) ⊆ V(T) ⟹ (A) 解集更小 ⟹ (A) 更难 ⟹ 得 NP-hard ✓")
    print()
    print("  ⟹ 归约需要：**目标方程 ∈ (A)-理想**（而不是反之）")
    print()

    # 试：找 (Ā,B̄) 使 (A)-理想包含 θ0²-θ0
    rng = random.Random(31)
    target = th[0]**2 - th[0]
    print("【实验】试找 (Ā,B̄) 使 (A)-理想包含 %s" % target)
    hit = 0; tried = 0
    for _ in range(300):
        AT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(dC)]
        BAT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(k)]
        # rho：一般值（用符号 Θ 代入随机数值取 max）
        best = 0
        W = [[sp.Integer(1) if j == i else sp.Integer(0) for j in range(dC)] for i in range(r)]
        idx = 0
        for i in range(k):
            row = [sp.Integer(0)] * dC
            row[r + i] = sp.Integer(1)
            for j in range(k, s):
                row[r + j] = th[idx]; idx += 1
            W.append(row)
        BATs = [[sp.Rational(x.numerator, x.denominator) for x in row] for row in BAT]
        WBs = [row[:] for row in W] + [row[:] for row in BATs]
        best = 0
        for _2 in range(6):
            sub = {th[i]: sp.Rational(rng.randint(-3, 3)) for i in range(m)}
            Mn = [[sp.nsimplify(e.subs(sub)) for e in row] for row in WBs]
            best = max(best, len(sp.Matrix(Mn).rref()[1]))
        try:
            ps = A_ideal(AT, BAT, r, k, s, dC, th, best)
        except Exception:
            continue
        if not ps: continue
        tried += 1
        # 检查 target 是否 ∈ 理想 (ps)：用 Groebner 归约
        try:
            G = sp.groebner(ps, *th, order='grevlex')
            # reduced 需要 Poly 列表
            Gp = [sp.Poly(g, *th) for g in G.exprs]
            if len(Gp) == 0:
                continue
            rem = sp.reduced(sp.Poly(target, *th), Gp, *th)
            r_ = rem[1] if isinstance(rem, tuple) else rem
            if sp.expand(r_) == 0:
                hit += 1
        except Exception:
            continue
    print("  尝试 %d 个 (Ā,B̄)；其中 (A)-理想包含目标者 = %d" % (tried, hit))
    print()
    print("【判读】")
    print("  · 若命中 > 0 ⟹ **归约可行**（存在使目标 ∈ (A)-理想的构造）✓")
    print("  · 若命中 = 0 ⟹ 需要更系统的构造（或目标选得更巧）⚠️")
    print()
    print("  ⚠️ 注意：(A) 的子式由 (Ā,B̄) 决定，而我们**只能通过 (Ā,B̄) 间接控制**理想；")
    print("     这可能使得『精确指定理想』非常困难。")


if __name__ == "__main__":
    main()
