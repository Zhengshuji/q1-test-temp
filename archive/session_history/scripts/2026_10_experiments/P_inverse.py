# -*- coding: utf-8 -*-
"""
P_inverse.py —— 逆问题：给定目标二次形式，求 (Ā,B̄)

【做法】
  对 $(r,k,s,d_C)$，把 $\bar A,\bar B$ 的条目视为符号，算出子式中二次项的
  系数（作为 $\bar A,\bar B$ 条目的多项式），得到映射
      $\Phi:\ (\bar A,\bar B)\ \longmapsto\ (\text{二次系数向量})\in\mathbb{Q}^D$
  然后检查：$\Phi$ 是否满射（用雅可比的一般秩），并给出一个显式逆像。
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


def coeff_map(r, k, s, dC):
    """返回 (sym_list, coeff_func) —— coeff_func 给 (Ā,B̄) 数值 → 二次系数向量"""
    m = k * (s - k)
    th = sp.symbols('t0:%d' % m)
    # Ā, B̄ 的符号条目
    Asym = sp.symbols('a0:%d' % (dC*dC))
    Bsym = sp.symbols('b0:%d' % (k*dC))
    AT = [[Asym[i*dC + j] for j in range(dC)] for i in range(dC)]
    BAT = [[Bsym[i*dC + j] for j in range(dC)] for i in range(k)]
    ATs, BATs = AT, BAT
    W = [[sp.Integer(1) if j == i else sp.Integer(0) for j in range(dC)] for i in range(r)]
    idx = 0
    for i in range(k):
        row = [sp.Integer(0)] * dC
        row[r + i] = sp.Integer(1)
        for j in range(k, s):
            row[r + j] = th[idx]; idx += 1
        W.append(row)
    WAs = [[sp.expand(sum(W[i][a] * ATs[a][j] for a in range(dC))) for j in range(dC)]
           for i in range(len(W))]
    WBs = [row[:] for row in W] + [row[:] for row in BATs]
    MBs = [row[:] for row in W] + [row[:] for row in BATs] + [row[:] for row in WAs]
    nr, nc = len(MBs), len(MBs[0])
    # 一般秩 rho：取 Ā,B̄ 的随机数值 + Θ 随机数值
    rng = random.Random(3)
    def num(M, sub):
        return [[sp.nsimplify(e.subs(sub)) for e in row] for row in M]
    rho = 0
    for _ in range(6):
        sub = {Asym[i]: sp.Rational(rng.randint(-2, 2)) for i in range(dC*dC)}
        sub.update({Bsym[i]: sp.Rational(rng.randint(-2, 2)) for i in range(k*dC)})
        sub.update({th[i]: sp.Rational(rng.randint(-2, 2)) for i in range(m)})
        Mn = num(WBs, sub)
        rho = max(rho, len(sp.Matrix(Mn).rref()[1]))
    # 收集二次系数（作为 Ā,B̄ 的多项式）
    monos = []
    for i in range(m):
        for j in range(i, m):
            mn = [0]*m; mn[i] += 1; mn[j] += 1
            monos.append(tuple(mn))
    coeffs = {mn: [] for mn in monos}     # 每个单项式 → 系数表达式列表
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            d = sp.expand(sp.Matrix([[MBs[i][j] for j in cj] for i in ri]).det())
            if d == 0: continue
            P = sp.Poly(d, *th)
            if P.total_degree() != 2: continue
            for mn in monos:
                c = P.coeff_monomial(mn)
                if c != 0:
                    coeffs[mn].append(sp.expand(c))
    return th, Asym, Bsym, monos, coeffs, rho


def main():
    print("=== 逆问题：二次系数如何依赖 (Ā,B̄) ===\n")
    for (r, k, s, dC) in [(1, 2, 4, 5), (1, 2, 3, 4)]:
        m = k * (s - k)
        th, Asym, Bsym, monos, coeffs, rho = coeff_map(r, k, s, dC)
        print("(r=%d,k=%d,s=%d,dC=%d): m=%d, ρ=%d" % (r, k, s, dC, m, rho))
        print("  二次单项式 %d 个；有非零系数的项：" % len(monos))
        cnt = 0
        for mn in monos:
            if coeffs[mn]:
                cnt += 1
                ex = coeffs[mn][0]
                deg = sp.Poly(ex, *(Asym + Bsym)).total_degree() if ex.free_symbols else 0
                print("    %s : %d 个子式给出系数；样例系数 = %s （次数 %d）"
                      % (str(mn), len(coeffs[mn]), sp.factor(ex) if ex.free_symbols else ex, deg))
        print("  ⟹ %d/%d 个二次单项式可由 (Ā,B̄) 非零实现" % (cnt, len(monos)))
        # 检查：是否每个系数都是 (Ā,B̄) 的二次型？那么"指定系数"是一个二次方程组
        allquad = all(
            (not ex.free_symbols) or
            sp.Poly(ex, *(Asym + Bsym)).total_degree() <= 2
            for mn in monos for ex in coeffs[mn])
        print("  所有系数对 (Ā,B̄) 的次数 ≤ 2 ？", allquad)
        print()


if __name__ == "__main__":
    main()
