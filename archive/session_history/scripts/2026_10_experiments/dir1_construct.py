# -*- coding: utf-8 -*-
"""
dir1_construct.py —— 方向 1 / 子任务 1.2：**构造性求解逆问题**

【目标】给定目标二次形式 Q（在 Θ 上），找一个 (Ā,B̄) 使
        (A)-子式集合的理想 **包含** Q。

【做法（贪心 + 线性代数）】
  1. 把 Ā 的元素与 B̄ 的元素分成若干"自由度"
  2. 对每个候选 (Ā,B̄) 计算子式集合的系数矩阵
  3. 用线性组合尝试匹配 Q

  因为子式系数对 (Ā,B̄) 是**二次**的，直接求解困难；
  ⟹ 先做**随机搜索 + 线性组合**：
     收集足够多的子式（每个是 Θ 的二次形式），看 Q 是否在其张成中。
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


def minors(AT, BAT, r, k, s, dC, th, rho):
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
    out = []
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            d = sp.expand(sp.Matrix([[MBs[i][j] for j in cj] for i in ri]).det())
            if d != 0:
                out.append(d)
    return out


def main():
    print("=== 方向 1 / 1.2：构造性逆问题（靶：编码 x²=x 与子句约束）===\n")
    # 最小形状：k=2, s=3, dC=4 ⟹ m=2（两个参数 θ0,θ1）
    r, k, s, dC = 1, 2, 3, 4
    m = k * (s - k)
    th = sp.symbols('t0:%d' % m)
    print("形状 (r=%d,k=%d,s=%d,dC=%d)：Θ 维数 m=%d\n" % (r, k, s, dC, m))
    rng = random.Random(99)
    # 收集足量子式（数值 (Ā,B̄)）
    vecs = []; polys = []
    monos = []
    for i in range(m):
        for j in range(i, m):
            mn = [0]*m; mn[i] += 1; mn[j] += 1
            monos.append(tuple(mn))
    D = len(monos)
    tried = 0
    for _ in range(600):
        AT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(dC)]
        BAT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(k)]
        try:
            # rho：一般值（用 b2 的做法：max over Θ）
            best = 0
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
            for _2 in range(6):
                sub = {th[i]: sp.Rational(rng.randint(-3, 3)) for i in range(m)}
                Mn = [[sp.nsimplify(e.subs(sub)) for e in row] for row in WBs]
                best = max(best, len(sp.Matrix(Mn).rref()[1]))
            ps = minors(AT, BAT, r, k, s, dC, th, best)
            tried += 1
            for p in ps:
                P = sp.Poly(p, *th)
                if P.total_degree() == 2:
                    polys.append(p)
                    vecs.append([sp.nsimplify(P.coeff_monomial(mn)) for mn in monos])
        except Exception:
            continue
    print("采样 %d 个 (Ā,B̄)，得到二次子式 %d 个" % (tried, len(polys)))
    if not polys:
        print("未得到二次子式（该形状的 (ρ+1) 阶子式可能都是线性/常数）")
        # 看看次数分布
        return
    M = sp.Matrix(vecs)
    print("二次系数矩阵 %d×%d，秩 = %d （目标 D=%d）" % (M.rows, M.cols, M.rank(), D))
    # 检查目标形式 Q = θ0*θ1 是否在张成中
    targets = {
        "θ0*θ1": [1 if mn == tuple(sorted([0,1])) or mn == (0,1) else 0 for mn in monos],
        "(θ0)^2": [1 if mn == (2,0) else 0 for mn in monos],
        "(θ1)^2": [1 if mn == (0,2) else 0 for mn in monos],
        "θ0^2-1(即 (θ0)^2 的常数项另加)": None,
    }
    # 注意：monos 是有序对 (i<=j) 的多重次数向量
    def mono_of(i, j):
        mn = [0]*m; mn[i] += 1; mn[j] += 1
        return tuple(mn)
    print("\n单项式基：", monos)
    for name, (a, b) in [("θ0²", (0,0)), ("θ0θ1", (0,1)), ("θ1²", (1,1))]:
        vec = [1 if mn == mono_of(a, b) else 0 for mn in monos]
        # 解 M^T λ = vec（最小二乘/精确）
        try:
            sol = M.T.solve(sp.Matrix(vec)) if M.T.rank() == M.T.cols else None
        except Exception:
            sol = None
        if sol is not None:
            # 验证
            resid = M.T * sol - sp.Matrix(vec)
            ok = all(x == 0 for x in resid)
            print("  %-6s 可由子式线性组合实现？ %s" % (name, ok))
        else:
            print("  %-6s 无法直接判定（需最小二乘）" % name)
    print()
    print("【判读】")
    print("  · 若 θ0²、θ0θ1、θ1² 都可由子式组合实现 ⟹ 可编码任意二次形式 ⟹ 归约可行 ✓")
    print("  · 注意：需要**单个子式**恰为目标（或目标的倍数），因为 (A) 要求每个子式为 0")
    print("    而线性组合 != 零 → 需要 *理想成员性* 而非 *线性张成*")


if __name__ == "__main__":
    main()
