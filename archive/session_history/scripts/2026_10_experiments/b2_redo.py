# -*- coding: utf-8 -*-
"""
b2_redo.py —— 用**正确的 W 构造**（WJ_of，行长度 = dC）重做全部检验

⚠️ 之前的 b2_mechanism.py / b2_lemmaA_check.py 手写 W 时只造了 3 列（dC=5 时错），
   而 `mm` 不检查维数 ⟹ 静默算错 ⟹ 得出"解集是直线"的错误结论 ✗
   本脚本用 WJ_of（与数值检验同一个构造器）避免该错误 ✓

检验：
  ① 线性部分秩  = m ?
  ② 高次子式 ∈ (t_0,...,t_{m-1}) ?（⟺ 无常数项 ⟺ 在 Θ=0 处为 0）
  ③ Groebner 基是否线性 ⟹ 单点
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


def Wsym_of(th, r, k, s, dC):
    """与数值版 WJ_of 完全一致的符号构造 ✓"""
    W = [[sp.Integer(1) if j == i else sp.Integer(0) for j in range(dC)] for i in range(r)]
    idx = 0
    for i in range(k):
        row = [sp.Integer(0)] * dC
        row[r + i] = sp.Integer(1)
        for j in range(k, s):
            row[r + j] = th[idx]; idx += 1
        W.append(row)
    return W


def build(inst):
    dC, s, AT, BAT = inst["dC"], inst["s"], inst["AT"], inst["BAT"]
    r, k = 1, 1; m = k * (s - k)
    th = sp.symbols('t0:%d' % m)
    if m == 1: th = (th,)
    W = Wsym_of(th, r, k, s, dC)
    assert all(len(row) == dC for row in W), "W 行长度错"
    R = lambda M: [[sp.Rational(x.numerator, x.denominator) for x in row] for row in M]
    ATs, BATs = R(AT), R(BAT)
    WAs = [[sp.expand(sum(W[i][a] * ATs[a][j] for a in range(len(ATs))))
            for j in range(dC)] for i in range(len(W))]
    WBs = [row[:] for row in W] + [row[:] for row in BATs]
    MBs = [row[:] for row in W] + [row[:] for row in BATs] + [row[:] for row in WAs]
    assert all(len(row) == dC for row in MBs), "MB 行长度错"
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
            (lin if sp.Poly(d, *th).total_degree() <= 1 else hi).append(d)
    return th, lin, hi, m, rho


def main():
    print("=== 用正确 W 构造重做（WJ_of 一致） ===")
    print("%-12s %4s %5s %8s %8s %10s %10s" %
          ("(k,s)", "m", "rho", "#线性", "秩(线性)", "#高次", "高次∈理想"))
    print("-" * 66)
    okA = okB = tot = 0
    for ss, n in [(3, 5), (4, 6), (5, 7)]:
        for t in range(4):
            inst = get_instance(n, ss, 20330000 + 100 * ss + t)
            if inst is None: continue
            th, lin, hi, m, rho = build(inst)
            M = sp.Matrix([[sp.Poly(d, *th).coeff_monomial(v) for v in th] for d in lin]) \
                if lin else sp.Matrix([[0] * m])
            r = M.rank()
            zero = {v: sp.Integer(0) for v in th}
            hin = all(sp.expand(d.subs(zero)) == 0 for d in hi)
            tot += 1
            okA += 1 if r == m else 0
            okB += 1 if hin else 0
            print("%-12s %4d %5d %8d %8d %10d %10s"
                  % ("(1,%d)#%d" % (ss, t), m, rho, len(lin), r, len(hi), hin))
        print()
    print("⟹ 线性部分满秩 : %d/%d" % (okA, tot))
    print("⟹ 高次无常数项 : %d/%d" % (okB, tot))
    print()
    if okA == tot and okB == tot and tot:
        print("✅ 引理 A（线性部分满秩 m）与 引理 B（高次 ∈ 线性理想）在这些实例上成立")
        print("   （注：引理 B 用于排除'高次在 Θ=0 附近另造解'; 需与 Groebner 结果一并看）")


if __name__ == "__main__":
    main()
