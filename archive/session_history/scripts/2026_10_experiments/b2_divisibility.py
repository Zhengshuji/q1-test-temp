# -*- coding: utf-8 -*-
"""
b2_divisibility.py —— 引理 B 的**可除性**形式

若每个高次子式 $I_j$ 都被某个**线性部分** $L$（或线性部分的组合）整除，
则 $L=0\Rightarrow I_j=0$ ⟹ 引理 B ✓（且这是可检验的代数事实）

检验：① 每个高次子式是否 = (线性式)·(线性式)？
      ② 或更弱：每个高次子式是否 ∈ 理想 (L_1,...,L_r)？（用 Groebner 归约，余式 = 0）
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


def get_instance(n, want_s, seed, tries=150000):
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
    print("=== 引理 B 的可除性形式 ===")
    print("%-12s %5s %6s %8s %10s %12s" %
          ("(k,s)", "m", "#线性", "#高次", "全可除?", "全∈理想?"))
    print("-" * 62)
    okdiv = okid = tot = 0
    for ss, n in [(3, 5), (4, 6)]:
        for t in range(3):
            inst = get_instance(n, ss, 20390000 + 100 * ss + t)
            if inst is None: continue
            dC, s, AT, BAT = inst["dC"], inst["s"], inst["AT"], inst["BAT"]
            r, k = 1, 1; m = s - 1
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
            WAs = [[sp.expand(sum(W[i][a] * ATs[a][j] for a in range(len(ATs))))
                    for j in range(dC)] for i in range(len(W))]
            WBs = [row[:] for row in W] + [row[:] for row in BATs]
            MBs = [row[:] for row in W] + [row[:] for row in BATs] + [row[:] for row in WAs]
            nr, nc = len(MBs), len(MBs[0])
            rho = 0
            for _ in range(30):
                sub = {th[i]: sp.Rational(random.randint(-5, 5), random.choice([1, 2, 3]))
                       for i in range(m)}
                Wn = [[sp.nsimplify(e.subs(sub)) for e in row] for row in WBs]
                rho = max(rho, len(sp.Matrix(Wn).rref()[1]))
            lin, hi = [], []
            for ri in itertools.combinations(range(nr), rho + 1):
                for cj in itertools.combinations(range(nc), rho + 1):
                    d = sp.expand(sp.Matrix([[MBs[i][j] for j in cj] for i in ri]).det())
                    if d == 0: continue
                    (lin if sp.Poly(d, *th).total_degree() <= 1 else hi).append(sp.expand(d))
            # ① 可除性：每个高次子式 = 线性多项式 的乘积？
            alldiv = True
            for d in hi:
                fac = sp.factor(d)
                if sp.Poly(d, *th).total_degree() != 2:
                    alldiv = False; break
                # 二次式 = 两个线性式之积？
                num, den = sp.fraction(sp.cancel(fac))
                lf = [f for f, _ in sp.factor_list(num)[1]
                      if sp.Poly(f, *th).total_degree() == 1]
                # 允许：多项式 = c * (lin1)*(lin2) 或 c*(lin)^2
                degsum = sum(sp.Poly(f, *th).total_degree() * e
                             for f, e in sp.factor_list(num)[1])
                if degsum != 2 or not lf:
                    alldiv = False; break
            # ② 是否 ∈ 理想 (lin)
            okideal = True
            if lin:
                G = sp.groebner(lin, *th, order='grevlex')
                for d in hi:
                    _, r_ = sp.reduced(d, G.exprs, *th)
                    if sp.expand(r_) != 0:
                        okideal = False; break
            else:
                okideal = False
            tot += 1
            okdiv += 1 if alldiv else 0
            okid += 1 if okideal else 0
            print("%-12s %5d %6d %8d %10s %12s"
                  % ("(1,%d)#%d" % (ss, t), m, len(lin), len(hi), alldiv, okideal))
        print()
    print("⟹ 高次子式全部可分解为线性因子之积 : %d/%d" % (okdiv, tot))
    print("⟹ 高次子式全部 ∈ 线性部分的理想     : %d/%d" % (okid, tot))


if __name__ == "__main__":
    main()
