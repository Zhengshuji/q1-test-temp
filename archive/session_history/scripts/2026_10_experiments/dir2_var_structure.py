# -*- coding: utf-8 -*-
"""
dir2_var_structure.py —— 方向 2：$\Omega^\star_J$ 的结构（是否为线性簇之并？）

【猜想 2.1】$\Omega^\star_J$ 按 $\operatorname{rk}[W(\Theta);B]$ 分层，每层是**线性簇**。
  （若成立 ⟹ 逐层线性判定 ⟹ 多项式算法）

【检验（小形状，可精确计算）】
  对 (k=2) 的小实例：
    ① 算 Groebner 基，看次数分布
    ② 算理想是否为**根理想**且由线性式生成
    ③ 把解集按 $\operatorname{rk}[W(\Theta);B]$ 分层，看每层的定义方程
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


def main():
    print("=== 方向 2：Ω*_J 的结构（线性簇之并？）===\n")
    r, k, s, dC = 1, 2, 4, 6     # m = 4；r+2k=5 < dC=6 ⟹ 非空洞 ✓
    m = k * (s - k)
    th = sp.symbols('t0:%d' % m)
    print("形状 (r=%d,k=%d,s=%d,dC=%d)，m=%d（r+2k=%d < dC ⟹ 非空洞）\n"
          % (r, k, s, dC, m, r + 2*k))
    rng = random.Random(67)
    for trial in range(20):
        AT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(dC)]
        BAT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(k)]
        WBs, MBs = build(AT, BAT, r, k, s, dC, th)
        # rho
        rho = 0
        for _ in range(8):
            sub = {th[i]: sp.Rational(rng.randint(-3, 3)) for i in range(m)}
            Mn = [[sp.nsimplify(e.subs(sub)) for e in row] for row in WBs]
            rho = max(rho, len(sp.Matrix(Mn).rref()[1]))
        nr, nc = len(MBs), len(MBs[0])
        if rho + 1 > nc or rho + 1 > nr: continue
        ps = []
        for ri in itertools.combinations(range(nr), rho + 1):
            for cj in itertools.combinations(range(nc), rho + 1):
                d = sp.expand(sp.Matrix([[MBs[i][j] for j in cj] for i in ri]).det())
                if d != 0 and d not in ps: ps.append(d)
        if not ps: continue
        degs = sorted({sp.Poly(p, *th).total_degree() for p in ps})
        print("实例 #%d: ρ=%d，子式 %d 个，次数 %s" % (trial, rho, len(ps), degs))
        for p in ps[:5]:
            print("     ", sp.factor(p))
        # Groebner
        try:
            G = sp.groebner(ps, *th, order='lex')
            ex = list(G.exprs)
            gdegs = sorted({sp.Poly(g, *th).total_degree() for g in ex})
            print("   Groebner 基次数 %s；基 = %s" % (gdegs, [str(g) for g in ex]))
            # 线性性：基是否全为一次
            alllin = all(sp.Poly(g, *th).total_degree() == 1 for g in ex)
            print("   ⟹ 基全为一次式（⟹ Ω*_J 线性簇）？ %s" % alllin)
        except Exception as e:
            print("   Groebner 失败：%s" % e)
        print()
        if trial >= 4: break


if __name__ == "__main__":
    main()
