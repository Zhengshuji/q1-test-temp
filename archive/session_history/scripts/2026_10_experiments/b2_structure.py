# -*- coding: utf-8 -*-
"""
b2_structure.py —— 支 B 的真解集结构：Ω*_J 是否**恒为单点**？基是否**恒为线性**？

对每个 (k=1, s=3/4) 实例：
  ① 算 (A)-系统的 Groebner 基（lex）
  ② 检查基是否**全为一次多项式**（⟹ Ω*_J 恰为单点，解 = 线性系统唯一解）
  ③ 报出该唯一点
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


def system_of(inst):
    dC, s, AT, BAT = inst["dC"], inst["s"], inst["AT"], inst["BAT"]
    r, k = 1, 1
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
    for _ in range(20):
        sub = {th[i]: sp.Rational(random.randint(-3, 3)) for i in range(m)}
        Wn = [[sp.nsimplify(e.subs(sub)) for e in row] for row in WB]
        rho = max(rho, len(sp.Matrix(Wn).rref()[1]))
    polys = []
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            d = sp.expand(sp.Matrix([[MB[i][j] for j in cj] for i in ri]).det())
            if d != 0 and d not in polys:
                polys.append(d)
    return th, polys, rho


def get_instance(n, want_k, want_s, seed):
    rng = random.Random(seed)
    for _ in range(400000):
        Ac = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        Lc = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        if rk(Cc) != 1 or rk(Lc) != 1 or rk(Lc + Cc) != 2: continue
        try: Lx, eta = p1(Ac, Cc, Lc)
        except Exception: continue
        if not Lx: continue
        q0 = sum(eta); k = q0 - 1
        if k != want_k: continue
        bt = build_norm_T(Ac, Cc, Lc, Lx)
        if bt is None: continue
        dC, s, k2, r2, AT, BAT = bt
        if (r2, k2) != (1, want_k) or s != want_s: continue
        if 2 * 1 + q0 >= n: continue
        return dict(dC=dC, s=s, AT=AT, BAT=BAT)
    return None


def main():
    print("=== 支 B：Ω*_J 的结构（是否恒为单点？基是否恒线性？）===")
    for ss, n, ntest in [(3, 5, 8), (4, 6, 6)]:
        print("\n--- (k=1, s=%d), n=%d ---" % (ss, n))
        ok = 0; lin = 0; degs = set()
        for t in range(ntest):
            inst = get_instance(n, 1, ss, 20270000 + t)
            if inst is None:
                print("   [%d] 无实例" % t); continue
            th, polys, rho = system_of(inst)
            G = sp.groebner(polys, *th, order='lex')
            ex = list(G.exprs)
            ds = set()
            for g in ex:
                p = sp.Poly(g, *th)
                ds.add(p.total_degree())
            degs |= ds
            all_lin = all(sp.Poly(g, *th).total_degree() == 1 for g in ex)
            lin += 1 if all_lin else 0
            sols = sp.solve(polys, th, dict=True)
            ok += 1
            if t < 3:
                print("   [%d] 子式 %d 个；基 = %s ；次数 %s ；线性？%s ；解数 %d"
                      % (t, len(polys), [str(g) for g in ex][:4], sorted(ds), all_lin, len(sols)))
        print("   小结：%d 个实例；基全为线性者 = %d ；出现过的次数 = %s"
              % (ok, lin, sorted(degs)))
    print("\n【判读】")
    print("  · 若基**恒为线性** ⟹ Ω*_J **恒为单点**（解由一次方程组唯一确定）")
    print("    ⟹ 支 B 的'解数'= 层数 #J = C(s,k)，**完全与实例无关** ⟹ 多项式 ✔")
    print("  · 若出现次数 ≥2 ⟹ 单点结论不成立，需按 Bézout 界")


if __name__ == "__main__":
    main()
