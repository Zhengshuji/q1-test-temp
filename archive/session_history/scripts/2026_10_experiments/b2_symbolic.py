# -*- coding: utf-8 -*-
"""
b2_symbolic.py —— 任务 B2：用 sympy **符号地**求消元后一元多项式的次数
                  ⟹ 给出"孤立解个数"的 Bézout 型上界

【命题（B2）】
  固定层 J（|J| = k）。条件 (A) 的**铅笔分解**（项目 verify_pencil_v2.py）：
      (A)  ⟺  ∀i: q_i(Θ) ∈ row P(Θ)
  其中（k=1, p=1 时）P(Θ), q_1(Θ) 是 Θ 的**仿射**函数，q_2(Θ) 是**二次**的。
  记
      条件① P(Θ) ∥ q_1(Θ)   （在 Θ 固定时对 s 线性 → 对 Θ 线性）
      条件② q_2(Θ) ∥ P(Θ)
  则条件① 给出 Θ 的**线性**方程组 A(s)·Θ = b(s)（方阵，(s-1)×(s-1)），
  Cramer 给出 Θ_a(s) = det A_a(s)/det A(s)，代入条件② 清分母得**一元多项式** g(s)，
      解数  ≤  deg g   （Bézout 型上界）
  本脚本符号计算 deg g，并看它随 (k, s) 的增长。

【用法】
  python312_sim\python.exe b2_symbolic.py
"""
import os, io, contextlib, itertools, sys
from fractions import Fraction as F

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))


# ---------------- 复用项目的数值构造，取 AT/BAT ----------------
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
mm = _ns["mm"]

_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]

import random
from fractions import Fraction as Fr


def get_instance(n, p, r, want_k, want_s, seed):
    rng = random.Random(seed)
    for _ in range(200000):
        Ac = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        Lc = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(r)]
        if _ns["rk"](Cc) != p or _ns["rk"](Lc) != r: continue
        if _ns["rk"](Lc + Cc) != r + p: continue
        try: Lx, eta = p1(Ac, Cc, Lc)
        except Exception: continue
        if not Lx: continue
        q0 = sum(eta); k = q0 - r
        if k != want_k: continue
        bt = _t["build_norm_T"](Ac, Cc, Lc, Lx)
        if bt is None: continue
        dC, s, k2, r2, AT, BAT = bt
        if (r2, k2) != (r, want_k) or s != want_s: continue
        if 2 * p + q0 >= n: continue
        return Ac, Cc, Lc, dC, s, AT, BAT
    return None


def W_symbolic(r, k, s, dC):
    """W_J(Θ) 的符号形式（k=1）：前 r 行 = [I_r|0]，后 k 行 = [0|I_k|Θ]"""
    th = sp.symbols('t0:%d' % (k * (s - k)))
    W = []
    for i in range(r):
        W.append([sp.Integer(1) if j == i else sp.Integer(0) for j in range(dC)])
    idx = 0
    for i in range(k):
        row = [sp.Integer(0)] * dC
        row[r + i] = sp.Integer(1)
        for j in range(k, s):
            row[r + j] = th[idx]; idx += 1
        W.append(row)
    return W, list(th)


def main():
    print("=== B2：符号求消元多项式的次数（Bézout 型上界）===")
    print("sympy", sp.__version__, "\n")
    # 取一个小实例：(k,s) = (1,3)
    inst = get_instance(5, 1, 1, 1, 3, seed=20260204)
    if inst is None:
        print("未找到 (k=1,s=3) 的支 B 实例"); return
    Ac, Cc, Lc, dC, s, AT, BAT = inst
    r, k, p = 1, 1, 1
    print("实例：n=%d p=%d r=%d dC=%d s=%d  ((k,s)=(%d,%d))\n" % (5, p, r, dC, s, k, s))
    print("A =", Ac); print("C =", Cc); print("L =", Lc); print()

    # 符号化：AT, BAT 是数值的（有理数），W 是符号的
    Ws, th = W_symbolic(r, k, s, dC)
    ATs = [[sp.Rational(x.numerator, x.denominator) for x in row] for row in AT]
    BATs = [[sp.Rational(x.numerator, x.denominator) for x in row] for row in BAT]

    WAs = [[sp.expand(sum(Ws[i][t] * ATs[t][j] for t in range(len(ATs))))
            for j in range(len(ATs[0]))] for i in range(len(Ws))]
    MB = [Ws[i] + BATs[i] for i in range(len(Ws))] + WAs
    WB = [Ws[i] + BATs[i] for i in range(len(Ws))]

    print("W_J(Θ) 的行数 = %d（=r+k）；[W;B] 的行数 = %d；列数 = %d"
          % (len(Ws), len(WB), dC))
    print("未知量 Θ =", th, "（个数 =", len(th), "）\n")

    # (A): rank[W;B;WĀ] == rank[W;B] ⟺ 全部 (rho+1) 阶子式 = 0，rho = rk[W;B]
    nr, nc = len(MB), len(MB[0])
    # rho 取 [W;B] 的"一般秩"：先用 Θ=0 数值估计，再取 max over 采样
    import random as _r
    rho = 0
    for _ in range(30):
        sub = {th[i]: sp.Rational(_r.randint(-3, 3)) for i in range(len(th))}
        WBn = [[sp.nsimplify(sp.simplify(e.subs(sub))) for e in row] for row in WB]
        rk = len(sp.Matrix(WBn).rref()[1])
        rho = max(rho, rk)
    print("ρ := rk[W;B]（一般值，采样估计）= %d\n" % rho)

    polys = []
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            d = sp.expand(sp.Matrix([[MB[i][j] for j in cj] for i in ri]).det())
            if d != 0:
                polys.append(sp.Poly(d, *th) if len(th) else d)
    print("非零的 (ρ+1) 阶子式个数 =", len(polys))
    if polys:
        print("各子式的总次数：", sorted({sp.Poly(p, *th).total_degree() for p in polys if hasattr(p, 'free_symbols')}))
    print()
    print("⟹ 下一步：对固定 s 把 Θ 消元（Cramer），再代入剩余条件，得一元多项式 g(s)，")
    print("   其次数即为孤立解个数的 Bézout 型上界。")
    print()
    print("【说明】完整消元（含 s 为符号）较慢；本脚本先给出**条件 (A) 的符号形状**，")
    print("        接下来分两步：(i) 固化 s；(ii) 对 Θ 做 Groebner 消元并求 s 的次数。")


if __name__ == "__main__":
    main()
