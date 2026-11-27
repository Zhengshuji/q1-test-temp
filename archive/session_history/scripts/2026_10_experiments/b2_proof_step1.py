# -*- coding: utf-8 -*-
"""
b2_proof_step1.py —— 探明"基恒线性"的**代数来源**：子式是否都是**线性因子之积**？

从 b2_verify.py 的输出看（(1,3) 实例）：
    4(5t0+6t1)/39 , -(4t0²-541t0-12t1²-618t1)/39 , ...
    ⟹ 第一、四式是**线性**的；第二式似乎二次
本脚本**精确因式分解**全部 (ρ+1) 阶子式，检查：
    · 是否每个子式都 = (线性式) × (线性式 或 常数)？
    · 这些线性式的**公共零点**是否只有 Θ=0？
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


def get_instance(n, want_s, seed, tries=200000):
    rng = random.Random(seed)
    for _ in range(tries):
        Ac = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        Lc = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        if rk(Cc) != 1 or rk(Lc) != 1 or rk(Lc + Cc) != 2: continue
        try: Lx, eta = p1(Ac, Cc, Lc)
        except Exception: continue
        if not Lx: continue
        q0 = sum(eta); k = q0 - 1
        if k != 1: continue
        bt = build_norm_T(Ac, Cc, Lc, Lx)
        if bt is None: continue
        dC, s, k2, r2, AT, BAT = bt
        if (r2, k2) != (1, 1) or s != want_s: continue
        if 2 + q0 >= n: continue
        return dict(dC=dC, s=s, AT=AT, BAT=BAT)
    return None


def main():
    for ss, n in [(3, 5), (4, 6)]:
        inst = get_instance(n, ss, 20290000 + ss)
        if inst is None:
            print("(1,%d) 无实例" % ss); continue
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
        print("\n=== (k=1, s=%d) n=%d : dC=%d m=%d rho=%d ===" % (s, n, dC, m, rho))
        print("    [W;B] %d×%d ; [W;B;WĀ] %d×%d" % (len(WB), nc, nr, nc))
        # W 的结构
        print("    W_J(Θ) 的行 =", [[str(e) for e in row] for row in W])
        linforms = []
        for ri in itertools.combinations(range(nr), rho + 1):
            for cj in itertools.combinations(range(nc), rho + 1):
                d = sp.expand(sp.Matrix([[MB[i][j] for j in cj] for i in ri]).det())
                if d == 0: continue
                fac = sp.factor(d)
                deg = sp.Poly(d, *th).total_degree()
                # 提取全部**线性因子**
                num, den = sp.fraction(sp.cancel(fac))
                lf = []
                for f, mult in sp.factor_list(num)[1]:
                    pf = sp.Poly(f, *th)
                    if pf.total_degree() == 1:
                        lf.append((str(f), mult))
                        linforms.append(f)
                print("    子式(rows=%s,cols=%s): deg=%d  factor=%s" % (ri, cj, deg, fac))
                print("        线性因子：%s" % lf)
        # 全部线性因子的公共零点
        uniq = []
        for f in linforms:
            c = sp.cancel(f)
            if not any(sp.simplify(c - g) == 0 or sp.simplify(c + g) == 0 for g in uniq):
                uniq.append(c)
        print("\n    去重后的线性因子（%d 个）：%s" % (len(uniq), [str(u) for u in uniq]))
        if uniq:
            sol = sp.linsolve([sp.Eq(u, 0) for u in uniq], *th)
            print("    它们的公共零点 = %s" % (sol,))


if __name__ == "__main__":
    main()
