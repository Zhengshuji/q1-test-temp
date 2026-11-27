# -*- coding: utf-8 -*-
"""
P_expressivity.py —— 归约的可行性分析：$(A)$ 条件能表达哪些约束？

【问题】归约要成功，必须能用 (A) 的 $(\\rho{+}1)$ 阶子式编码 NP-hard 问题的约束。
但 (A) 的族 $\{M_J(\Theta)\}$ 结构高度受限：
    M_J(Θ) = [W_J(Θ); B̄; W_J(Θ)Ā]，其中
    W_J(Θ) = [I_r 0; 0 I_k Θ]（Θ 只在最后 k 行、最后 s-k 列）
  ⟹ 子式对 Θ 的次数 ≤ 2，且 Θ 的"出现方式"受模板约束

【本脚本】对 (k,s) 小形状，枚举 (Ā, B̄) 的小整数取值，
          收集**全部**出现的子式集合，检查：
   ① 子式张成的空间维数（表达能力）
   ② 是否总能覆盖"一般的二次型"（对比：全部二次型的维数）
"""
import os, io, contextlib, itertools
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]

import sympy as sp


def minors_of(AT, BAT, r, k, s, dC, th, rho=None):
    """给定 Ā=BAT 等，返回 M(Θ) 的全部 (rho+1) 阶子式（符号）"""
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
    if rho is None:
        # 一般秩：取 Θ 随机整数代入
        import random
        rng = random.Random(1)
        best = 0
        for _ in range(20):
            sub = {th[i]: sp.Rational(rng.randint(-3, 3)) for i in range(len(th))}
            Mn = [[sp.nsimplify(e.subs(sub)) for e in row] for row in WBs]
            best = max(best, len(sp.Matrix(Mn).rref()[1]))
        rho = best
    out = []
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            d = sp.expand(sp.Matrix([[MBs[i][j] for j in cj] for i in ri]).det())
            if d != 0:
                out.append(d)
    return out, rho


def main():
    print("=== (A) 条件的表达能力分析（归约可行性）===\n")
    r, k, s, dC = 1, 2, 4, 5
    m = k * (s - k)
    th = sp.symbols('t0:%d' % m)
    print("形状：r=%d k=%d s=%d dC=%d ⟹ Θ 维数 m=%d\n" % (r, k, s, dC, m))
    allp = set()
    n_try = 0
    for combo in itertools.product((-1, 0, 1), repeat=2*dC*dC):
        # Ā 与 B̄ 各取 {-1,0,1} 的元素太多；改为随机采样
        break
    import random
    rng = random.Random(7)
    tried = 0
    for _ in range(60):
        AT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(dC)]
        BAT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(k)]
        try:
            ps, rho = minors_of(AT, BAT, r, k, s, dC, th)
        except Exception:
            continue
        tried += 1
        for p in ps:
            allp.add(sp.expand(p))
        if tried == 1:
            print("第一个实例：ρ=%d，子式 %d 个" % (rho, len(ps)))
            for p in ps[:6]:
                print("   ", p)
            print()
    print("采样 %d 个 (Ā, B̄) 组合，共得到**不同**子式 %d 个" % (tried, len(allp)))
    # 看这些子式张成的空间（按单项式基）
    if allp:
        monos = set()
        for p in allp:
            for mon in sp.Poly(p, *th).monoms():
                monos.add(mon)
        print("涉及的不同单项式个数：", len(monos))
        print("  单项式（次数分布）：", sorted({sum(mn) for mn in monos}))
        # 二次型空间的维数：m(m+1)/2
        print("  m=%d 时全部二次型的维数 = m(m+1)/2 = %d" % (m, m*(m+1)//2))
        # 我们能否得到任意的二次型？检查"只含 θ_j θ_{j'} (j,j'>0)"的单项式
        has = {mn for mn in monos if sum(mn) == 2}
        print("  我们得到的二次单项式：", sorted(has))
        print("  理论上(受模板约束)可出现的二次单项式：", 
              sorted({tuple(sorted((a, b))) for a in range(m) for b in range(m)}))
    print()
    print("【判读】")
    print("  · 若我们能得到的二次单项式**严格少于**全部 ⟹ 表达力受限 ⟹ 归约更难但可能仍可行")
    print("  · 若相同 ⟹ 表达力充分 ⟹ 归约可行（需再构造）")


if __name__ == "__main__":
    main()
