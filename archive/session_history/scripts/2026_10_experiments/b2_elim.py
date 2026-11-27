# -*- coding: utf-8 -*-
"""
b2_elim.py —— 任务 B2：符号消元求"消元后一元多项式的次数"（= 孤立解个数上界）

【做法（k=1）】
  条件 (A)  ⟺  [W;B;WĀ] 的全部 (ρ+1) 阶子式 = 0，其中 ρ = rk[W;B]。
  这些子式是 Θ（k(s-k) 个变量）的**多项式**（因 W 对 Θ 仿射）。
  用 sympy 的 Groebner 基消去 Θ，得到只含 s 的多项式 —— 本次先把 s 数值化，
  看"截断后系统的解数"是否 ≤ 某个与 (k,s) 无关的小常数。

  更直接地：把 (A) 的多项式系统对 Θ 求解：
     · 若解集是**有限点**，解数 ≤ Bezout 界 Π deg；
     · 用 Groebner 基（lex, Θ 为变量）算"商环维数" = 解数（含重数）。
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
        return dict(Ac=Ac, Cc=Cc, Lc=Lc, dC=dC, s=s, AT=AT, BAT=BAT)
    return None


def analyze(inst, verbose=True):
    r, k, p = 1, 1, 1
    dC, s, AT, BAT = inst["dC"], inst["s"], inst["AT"], inst["BAT"]
    m = k * (s - k)
    th = sp.symbols('t0:%d' % m) if m else ()
    if m == 1: th = (th,)
    # W_J(Θ) 符号
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
    # ⚠️ 行堆叠：[W ; B]（W 是 (r+k)×dC，B 是 k×dC —— 行数不同，不能逐元素相加！）
    WB = [row[:] for row in W] + [row[:] for row in BATs]
    MB = [row[:] for row in W] + [row[:] for row in BATs] + [row[:] for row in WAs]
    nr, nc = len(MB), len(MB[0])
    # 一般秩 ρ：采样
    rho = 0
    for _ in range(25):
        sub = {th[i]: sp.Rational(random.randint(-3, 3)) for i in range(m)}
        Wn = [[sp.nsimplify(e.subs(sub)) for e in row] for row in WB]
        rho = max(rho, len(sp.Matrix(Wn).rref()[1]))
    # 生成全部 (rho+1) 阶子式
    polys = []
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            d = sp.expand(sp.Matrix([[MB[i][j] for j in cj] for i in ri]).det())
            if d != 0:
                polys.append(d)
    degs = sorted({sp.Poly(d, *th).total_degree() for d in polys}) if polys else []
    if verbose:
        print("  dC=%d s=%d  m=k(s-k)=%d  ρ=%d  [W;B]%d×%d  [W;B;WĀ]%d×%d"
              % (dC, s, m, rho, len(WB), nc, nr, nc))
        print("  非零 (ρ+1)-子式个数 = %d ；次数集合 = %s" % (len(polys), degs))
    # Groebner（lex, 全 Θ 消到常数）：商环维数 = 解数（含重数）
    info = dict(m=m, n_poly=len(polys), degs=degs, rho=rho)
    if polys and m >= 1:
        try:
            G = sp.groebner(polys, *th, order='lex')
            # 商环维数：逐变量数"标准单项式"
            std = G.basis
            # 用 sympy 的 GroebnerBasis 求维数（有限维时 = 首项理想下标准单项式数）
            # 近似法：算 1 在该理想下的标准形是否非零，并用希尔伯特级数
            try:
                hs = G.hilbert_dimension()          # 若有限维返回 0
                info['hilb_dim'] = hs
            except Exception as e:
                info['hilb_dim'] = 'err:%s' % e
            # 解数（含重）：用 Groebner + 特征值/结式不易；改数"标准单项式"
            from sympy.polys.orderings import lex
            lm = [sp.LM(g, *th, order='lex') for g in std]
            maxd = [sp.degree(sp.Poly(lm_i.as_expr(), *th).as_expr(), v) if lm_i != 1 else 0
                    for lm_i in lm for v in th]
            info['leading_monomials'] = [str(x) for x in lm]
        except Exception as e:
            info['groebner_err'] = str(e)
    return info


def main():
    print("=== B2：符号消元（k=1），求解数上界 ===")
    print("sympy", sp.__version__, "\n")
    for (ss, seed) in [(3, 20260204), (4, 20260205), (5, 20260206)]:
        n = 5 if ss <= 3 else (6 if ss == 4 else 7)
        inst = get_instance(n, 1, 1, 1, ss, seed)
        if inst is None:
            print("(k=1, s=%d)：未找到支 B 实例（n=%d）" % (ss, n)); continue
        print("--- (k=1, s=%d) ---" % ss)
        info = analyze(inst)
        print("  =>", {k: v for k, v in info.items() if k != 'leading_monomials'})
        print()


if __name__ == "__main__":
    main()
