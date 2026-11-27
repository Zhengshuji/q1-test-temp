# -*- coding: utf-8 -*-
"""
b2_bound.py —— 任务 B2：给出 Ω*_J 的**解数上界**并与实际解数比较

【关键事实（b2_elim.py 已测）】
  定义 (A) 的多项式在 Θ 上**次数 ≤ 2**（与 s 无关）。
  ⟹ **Bézout 界**：  #Ω*_J  ≤  2^{k(s-k)}

【本脚本】
  ① 用 Groebner 基（lex）算商环的**维数**（= 解数，含重数）；
  ② 计算实际的不同解数（用有理根/数值根）；
  ③ 比较 实际 / Bezout 界 的两个增长。
"""
import os, io, contextlib, itertools, random
from fractions import Fraction as Fr
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]
_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]; build_norm_T = _t["build_norm_T"]


def get_instance(n, p, r, want_k, want_s, seed):
    rng = random.Random(seed)
    for _ in range(400000):
        Ac = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        Lc = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(r)]
        if rk(Cc) != p or rk(Lc) != r or rk(Lc + Cc) != r + p: continue
        try: Lx, eta = p1(Ac, Cc, Lc)
        except Exception: continue
        if not Lx: continue
        q0 = sum(eta); k = q0 - r
        if k != want_k: continue
        bt = build_norm_T(Ac, Cc, Lc, Lx)
        if bt is None: continue
        dC, s, k2, r2, AT, BAT = bt
        if (r2, k2) != (r, want_k) or s != want_s: continue
        if 2 * p + q0 >= n: continue
        return dict(dC=dC, s=s, AT=AT, BAT=BAT)
    return None


def build_polys(inst):
    r, k, dC, s, AT, BAT = 1, 1, inst["dC"], inst["s"], inst["AT"], inst["BAT"]
    m = k * (s - k)
    th = sp.symbols('t0:%d' % m)
    if m == 1: th = (th,)
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
    WAs = [[sp.expand(sum(W[i][t] * ATs[t][j] for t in range(len(ATs))))
            for j in range(dC)] for i in range(len(W))]
    WB = [row[:] for row in W] + [row[:] for row in BATs]
    MB = [row[:] for row in W] + [row[:] for row in BATs] + [row[:] for row in WAs]
    nr, nc = len(MB), len(MB[0])
    rho = 0
    for _ in range(25):
        sub = {th[i]: sp.Rational(random.randint(-3, 3)) for i in range(m)}
        Wn = [[sp.nsimplify(e.subs(sub)) for e in row] for row in WB]
        rho = max(rho, len(sp.Matrix(Wn).rref()[1]))
    polys = []
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            d = sp.expand(sp.Matrix([[MB[i][j] for j in cj] for i in ri]).det())
            if d != 0 and d not in polys:
                polys.append(d)
    return th, polys, m, rho


def count_solutions(polys, th):
    """用 Groebner 基算商环维数（= 解数，含重数）"""
    try:
        G = sp.groebner(polys, *th, order='lex')
        exprs = list(G.exprs)
        # 每个变量的"纯幂界"：基中形如 v^d 的首项
        bounds = {}
        for v in th:
            mn = None
            for g in exprs:
                try:
                    p = sp.Poly(g, *th)
                except Exception:
                    continue
                if p.is_zero: continue
                # 该多项式是否只含 v（纯幂）
                others = [w for w in th if w != v]
                dep_others = any(p.degree(w) > 0 for w in others)
                if not dep_others and p.degree(v) > 0:
                    mn = p.degree(v) if mn is None else min(mn, p.degree(v))
            bounds[v] = mn
        if any(b is None for b in bounds.values()):
            return None, bounds, exprs
        total = 1
        for b in bounds.values(): total *= b
        return total, bounds, exprs
    except Exception as e:
        return 'err:%s' % e, None, None


def main():
    print("=== B2：解数上界（Bézout）vs 实际解数 ===")
    print("sympy", sp.__version__, "\n")
    print("%-10s %5s %5s %10s %10s %10s" % ("(k,s)", "m", "ρ", "Bezout=2^m", "商环维数", "多项式的次数"))
    print("-" * 60)
    for ss, seed in [(3, 20260204), (4, 20260205), (5, 20260206)]:
        n = 5 if ss <= 3 else (6 if ss == 4 else 7)
        inst = get_instance(n, 1, 1, 1, ss, seed)
        if inst is None:
            print("(1,%d) 未找到实例" % ss); continue
        th, polys, m, rho = build_polys(inst)
        cnt, bounds, LMs = count_solutions(polys, th)
        degs = sorted({sp.Poly(p, *th).total_degree() for p in polys})
        print("%-10s %5d %5d %10d %10s %10s"
              % ("(1,%d)" % ss, m, rho, 2 ** m, str(cnt), str(degs)))
        if bounds:
            print("            每个变量的纯幂界：", {str(k): v for k, v in bounds.items()})
    print()
    print("【判读】")
    print("  · Bezout 界 2^m 随 m 指数增长（m = k(s-k)）")
    print("  · 若商环维数**明显小得多** ⟹ 实际解数远低于 Bezout ⟹ 系统高度退化")
    print("  · 若商环维数 = 0 或 None ⟹ 需换判据（可能正维数）")


if __name__ == "__main__":
    main()
