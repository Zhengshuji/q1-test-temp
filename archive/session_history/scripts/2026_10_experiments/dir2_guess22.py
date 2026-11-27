# -*- coding: utf-8 -*-
"""
dir2_guess22.py -- 方向 2 / 猜想 2.2 检验: Groebner 基的变量依赖结构

【猜想 2.2】Groebner 基恒为"线性部分 + 仅 d 个变量的二次部分", d 很小 (<=2?)
  ==> dim Omega*_J <= d

【做法】对每个实例:
  1. 算 (A)-子式
  2. 算 Groebner 基 (lex)
  3. 统计: 线性元涉及哪些变量; 高次元涉及哪些变量
  4. 报告 dim 上界 = 高次元涉及的变量数
"""
import os, io, contextlib, itertools, random, signal
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]

import sympy as sp


class TO(Exception):
    pass


def _h(sig, frm):
    raise TO()


try:
    signal.signal(signal.SIGALRM, _h)
    HAVE_ALARM = True
except Exception:
    HAVE_ALARM = False


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


def analyze_shape(r, k, s, dC, n_inst=6, rng=None, tmo=25):
    rng = rng or random.Random(73)
    m = k * (s - k)
    th = sp.symbols('t0:%d' % m)
    print("--- 形状 (r=%d,k=%d,s=%d,dC=%d), m=%d, r+2k=%d ---"
          % (r, k, s, dC, m, r + 2 * k))
    got = 0
    for trial in range(n_inst):
        AT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(dC)]
        BAT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(k)]
        WBs, MBs = build(AT, BAT, r, k, s, dC, th)
        rho = 0
        for _ in range(6):
            sub = {th[i]: sp.Rational(rng.randint(-3, 3)) for i in range(m)}
            Mn = [[sp.nsimplify(e.subs(sub)) for e in row] for row in WBs]
            rho = max(rho, len(sp.Matrix(Mn).rref()[1]))
        ps = A_polys(MBs, rho)
        if not ps:
            continue
        try:
            if HAVE_ALARM:
                signal.alarm(tmo)
            G = sp.groebner(ps, *th, order='lex')
            if HAVE_ALARM:
                signal.alarm(0)
        except TO:
            print("   实例 #%d: 超时 (%ds)" % (trial, tmo))
            continue
        except Exception as e:
            print("   实例 #%d: Groebner 失败 %s" % (trial, e))
            continue
        ex = [g for g in G.exprs if g != 0]
        if not ex:
            print("   实例 #%d: 理想 = (0) (空洞)" % trial)
            continue
        lin_vars = set(); hi_vars = set(); degs = set()
        for g in ex:
            P = sp.Poly(g, *th)
            dg = P.total_degree()
            degs.add(dg)
            vs = {v for v in th if P.degree(v) > 0}
            if dg == 1:
                lin_vars |= vs
            else:
                hi_vars |= vs
        got += 1
        print("   实例 #%d: rho=%d, 子式 %d 个; 基 %d 元, 次数 %s"
              % (trial, rho, len(ps), len(ex), sorted(degs)))
        print("      线性元变量 %s" % sorted(str(v) for v in lin_vars))
        print("      高次元变量 %s  ==> dim <= %d"
              % (sorted(str(v) for v in hi_vars), len(hi_vars)))
        if got >= 3:
            break
    print()
    return got


def main():
    print("=== 方向 2 / 猜想 2.2: Groebner 基的变量依赖结构 ===\n")
    for (r, k, s, dC, ni) in [(1, 2, 4, 6, 6),
                              (1, 2, 5, 6, 4),
                              (1, 3, 5, 7, 3),
                              (1, 3, 6, 7, 3)]:
        analyze_shape(r, k, s, dC, n_inst=ni)
    print("【判读】")
    print("  - 若'高次元变量数'恒 <= 2 ==> 猜想 2.2 成立 ==> dim Omega*_J <= 2")
    print("    ==> 可用低维二次系统求解 ==> P in P ==> q1 不是 NP-hard")
    print("  - 若随 (k,s) 增长 ==> 猜想 2.2 假 ==> 需另找结构")


if __name__ == "__main__":
    main()
