# -*- coding: utf-8 -*-
"""
P_surjectivity.py —— 归约的关键一步：二次形式的**系数映射是否满射**？

【问题】模板
    M(Θ) 的子式 = Θ 的二次形式，系数由 (Ā, B̄) 决定
需问：(Ā,B̄) ↦ (二次形式) 是否**满射**到全部二次形式的空间？
若满射 ⟹ 可编码**任意**二次约束 ⟹ 归约可行 ✓

【做法（线性代数）】
  固定 (r,k,s,dC)，把二次形式写成系数向量（按单项式基）。
  · 目标空间维数 D = m(m+1)/2（对称二次形式）
  · 参数空间：(Ā,B̄) 的条目数
  · 数值采样：收集足够多的 (Ā,B̄) 对应的系数向量，算它们的**张成维数**
    若张成维数 = D ⟹ 满射 ✓（数值意义）
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


def minor_coeff_vectors(AT, BAT, r, k, s, dC, monomials, rho):
    """返回该 (Ā,B̄) 下所有子式的系数向量（在给定单项式基下）"""
    th = sp.symbols('t0:%d' % (k * (s - k)))
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
    vecs = []
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            d = sp.expand(sp.Matrix([[MBs[i][j] for j in cj] for i in ri]).det())
            if d == 0: continue
            P = sp.Poly(d, *th)
            if P.total_degree() != 2: continue
            v = [sp.nsimplify(P.coeff_monomial(mn)) for mn in monomials]
            if any(x != 0 for x in v):
                vecs.append(v)
    return vecs


def main():
    print("=== 归约关键：二次系数映射的满射性 ===\n")
    for (r, k, s, dC) in [(1, 2, 4, 5), (1, 2, 3, 4), (1, 2, 4, 6), (1, 3, 4, 5)]:
        m = k * (s - k)
        th_names = ['t%d' % i for i in range(m)]
        # 单项式基：全部二次单项式（有序对 i<=j）
        monos = []
        for i in range(m):
            for j in range(i, m):
                mn = [0] * m; mn[i] += 1; mn[j] += 1
                monos.append(tuple(mn))
        D = len(monos)
        rng = random.Random(11)
        allv = []
        for _ in range(400):
            AT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(dC)]
            BAT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(k)]
            # rho：一般秩
            try:
                # 用 b2 的方法：取 rk[W;B] 的一般值
                th = sp.symbols('t0:%d' % m)
                W = [[sp.Integer(1) if j == i else sp.Integer(0) for j in range(dC)]
                     for i in range(r)]
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
                rho = best
                vs = minor_coeff_vectors(AT, BAT, r, k, s, dC, monos, rho)
                allv += vs
            except Exception:
                continue
        if not allv:
            print("(r=%d,k=%d,s=%d,dC=%d) 未得到二次子式" % (r,k,s,dC)); continue
        M = sp.Matrix(allv)
        rank_span = M.rank()
        print("(r=%d,k=%d,s=%d,dC=%d)  m=%d ；二次形式空间维数 D=%d ；采样系数向量张成维数 = %d  %s"
              % (r, k, s, dC, m, D, rank_span,
                 "⟹ **满射** ✓" if rank_span >= D else "⟹ 未满射 ✗"))
    print()
    print("【判读】")
    print("  张成维数 = D ⟹ 任意二次形式可由 (Ā,B̄) 实现 ⟹ 可用它编码 NP-hard 约束")
    print("  张成维数 < D ⟹ 表达力受限 ⟹ 归约需绕开未覆盖的方向")


if __name__ == "__main__":
    main()
