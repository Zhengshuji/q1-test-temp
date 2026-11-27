# -*- coding: utf-8 -*-
"""
dir1_seq1.py —— 序 1：在**非空洞形状**上重做理想成员性实验（修正样本量）

【关键修正（相比上一轮）】
  · 上一轮用 $(1,2,3,4)$：那里 max rk[W;B] = d_C ⟹ (ρ+1) 阶子式**不存在**
    ⟹ 大部分 (Ā,B̄) 给出**空**子式集 ⟹ 有效样本只有 2 个 ✗
  · 本轮改用 $(1,2,4,6)$ 等**非空洞形状**，并**报告每一步的命中/失败数**

【判据】构造 (Ā,B̄) 使 (A)-理想 ⊇ T（目标二次系统）⟹ 归约可行
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


def build(AT, BAT, r, k, s, dC, th):
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
    return WBs, MBs


def rho_generic(WBs, th, m, rng, n=8):
    best = 0
    for _ in range(n):
        sub = {th[i]: sp.Rational(rng.randint(-3, 3)) for i in range(m)}
        Mn = [[sp.nsimplify(e.subs(sub)) for e in row] for row in WBs]
        best = max(best, len(sp.Matrix(Mn).rref()[1]))
    return best


def A_polys(WBs, MBs, rho):
    nr, nc = len(MBs), len(MBs[0])
    out = []
    if rho + 1 > nc or rho + 1 > nr:
        return out
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            d = sp.expand(sp.Matrix([[MBs[i][j] for j in cj] for i in ri]).det())
            if d != 0 and d not in out:
                out.append(d)
    return out


def main():
    print("=== 序 1：非空洞形状上的理想成员性实验 ===\n")
    # 非空洞形状：(r,k,s,dC) 满足 ρ = min(r+2k,dC) 且可 < dC
    for (r, k, s, dC) in [(1, 2, 4, 6), (1, 2, 5, 6), (1, 3, 5, 7)]:
        m = k * (s - k)
        th = sp.symbols('t0:%d' % m)
        rng = random.Random(41)
        print("--- 形状 (r=%d,k=%d,s=%d,dC=%d)，m=%d ---" % (r, k, s, dC, m))
        # 先核实该形状非空洞（存在 rank 差）
        nonvac = False
        for _ in range(20):
            AT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(dC)]
            BAT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(k)]
            WBs, MBs = build(AT, BAT, r, k, s, dC, th)
            rho = rho_generic(WBs, th, m, rng)
            # 检查 (ρ+1) 阶子式是否存在
            exists = (rho + 1 <= dC) and (rho + 1 <= len(MBs))
            if exists:
                # 检查是否有非零子式
                ps = A_polys(WBs, MBs, rho)
                if ps:
                    nonvac = True
                    break
        print("   存在 (ρ+1) 阶非零子式？", nonvac)
        if not nonvac:
            print("   ⟹ 该形状空洞，跳过\n")
            continue
        # 收集足量子式
        polys = []; tried = 0; empt = 0
        for _ in range(120):
            AT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(dC)]
            BAT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(k)]
            WBs, MBs = build(AT, BAT, r, k, s, dC, th)
            rho = rho_generic(WBs, th, m, rng)
            try:
                ps = A_polys(WBs, MBs, rho)
            except Exception:
                continue
            tried += 1
            if not ps: empt += 1
            polys += ps
        print("   (Ā,B̄) 尝试 %d 个；其中子式集为空的 %d 个；共得子式 %d 个"
              % (tried, empt, len(polys)))
        # 目标：θ0² - θ0（编码布尔性）
        target = th[0]**2 - th[0]
        # 检查 target 是否 ∈ 理想(polys)
        try:
            G = sp.groebner(polys, *th, order='grevlex')
            Gp = [sp.Poly(g, *th) for g in G.exprs]
            print("   Groebner 基元素数 = %d" % len(Gp))
            if Gp:
                rem = sp.reduced(sp.Poly(target, *th), Gp, *th)
                r_ = rem[1] if isinstance(rem, tuple) else rem
                print("   target = %s 是否 ∈ (A)-理想？ %s"
                      % (target, sp.expand(r_) == 0))
            else:
                print("   理想为空（全部子式恒零）⟹ 任意多项式都 ∈ 理想 ⟹ 归约平凡但无信息")
        except Exception as e:
            print("   Groebner 失败：%s" % e)
        print()


if __name__ == "__main__":
    main()
