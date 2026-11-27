# -*- coding: utf-8 -*-
"""
dir1_seq1b.py —— 序 1（修正版）：**逐实例**检验 (A)-理想是否可包含目标

【修正】上一版把**不同** (Ā,B̄) 的子式混在一起做 Gröbner —— 无意义 ✗
        正确做法：**每个 (Ā,B̄) 单独**算 (A)-理想，再检验目标是否 ∈ 该理想。

【检验的目标】T = {θ0²-θ0}（布尔性）。若某个 (Ā,B̄) 使 T ∈ (A)-理想 ⟹ 归约可行。
      并统计：多少比例的 (Ā,B̄) 能做到（若为 0 ⟹ 归约难）
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


def rho_gen(WBs, th, m, rng, n=8):
    best = 0
    for _ in range(n):
        sub = {th[i]: sp.Rational(rng.randint(-3, 3)) for i in range(m)}
        Mn = [[sp.nsimplify(e.subs(sub)) for e in row] for row in WBs]
        best = max(best, len(sp.Matrix(Mn).rref()[1]))
    return best


def A_polys(MBs, rho):
    nr, nc = len(MBs), len(MBs[0])
    if rho + 1 > nc or rho + 1 > nr:
        return []
    out = []
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            d = sp.expand(sp.Matrix([[MBs[i][j] for j in cj] for i in ri]).det())
            if d != 0:
                out.append(d)
    return out


def main():
    print("=== 序 1（修正版）：逐实例检验 (A)-理想 ⊇ {θ0²-θ0} ===\n")
    for (r, k, s, dC) in [(1, 2, 4, 6), (1, 2, 4, 5), (1, 3, 5, 7)]:
        m = k * (s - k)
        th = sp.symbols('t0:%d' % m)
        target = th[0]**2 - th[0]
        print("--- 形状 (r=%d,k=%d,s=%d,dC=%d)，m=%d ---" % (r, k, s, dC, m))
        rng = random.Random(53)
        n_try = n_ok = n_empty = n_gbfail = n_contains = 0
        for _ in range(150):
            AT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(dC)]
            BAT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(k)]
            try:
                WBs, MBs = build(AT, BAT, r, k, s, dC, th)
                rho = rho_gen(WBs, th, m, rng)
                ps = A_polys(MBs, rho)
            except Exception:
                continue
            n_try += 1
            if not ps:
                n_empty += 1
                continue
            try:
                G = sp.groebner(ps, *th, order='grevlex')
                ex = list(G.exprs)
                if not ex or (len(ex) == 1 and ex[0] == 0):
                    # 理想为 (0) ⟹ 包含一切 ⟹ 也包含 target（但这是退化的）
                    n_ok += 1
                    n_contains += 1
                    continue
                # target ∈ 理想 ⟺ 用 G 归约 target 得 0
                Gp = [sp.Poly(g, *th) for g in ex if g != 0]
                if not Gp:
                    n_contains += 1
                    continue
                rem = sp.reduced(sp.Poly(target, *th), Gp, *th)
                r_ = rem[1] if isinstance(rem, tuple) else rem
                if sp.expand(r_) == 0:
                    n_contains += 1
                n_ok += 1
            except Exception:
                n_gbfail += 1
        print("   (Ā,B̄) 有效 %d ；子式集空 %d ；Groebner 失败 %d" % (n_try, n_empty, n_gbfail))
        print("   ⟹ (A)-理想包含 target 的实例数 = %d / %d" % (n_contains, max(n_ok, 1)))
        if n_contains:
            print("   ✓ 存在构造使 target ∈ (A)-理想 ⟹ 归约可行（需显式化）")
        elif n_ok:
            print("   ✗ 全部实例的 (A)-理想都**不含** target ⟹ 这个 target 不可行")
        print()


if __name__ == "__main__":
    main()
