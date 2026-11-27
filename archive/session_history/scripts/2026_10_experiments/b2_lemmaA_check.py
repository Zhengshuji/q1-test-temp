# -*- coding: utf-8 -*-
"""
b2_lemmaA_check.py —— 核实 (1,4) 上"线性部分不满秩"的实例：真实解集到底是什么？
   ① 线性部分的零点（正维数？）
   ② 全部子式的零点（Groebner）
   ③ 高次部分是否在线性零点集上恒零？还是把解集切到单点？
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


def build(inst):
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
    lin, hi = [], []
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            d = sp.expand(sp.Matrix([[MB[i][j] for j in cj] for i in ri]).det())
            if d == 0: continue
            (lin if sp.Poly(d, *th).total_degree() <= 1 else hi).append(d)
    return th, lin, hi, m, rho


def main():
    print("=== 核实 (1,4) 上线性部分不满秩的实例 ===")
    for t in range(8):
        inst = get_instance(6, 4, 20320000 + 400 + t)
        if inst is None: continue
        th, lin, hi, m, rho = build(inst)
        M = sp.Matrix([[sp.Poly(d, *th).coeff_monomial(v) for v in th] for d in lin]) if lin else None
        r = M.rank() if M is not None else 0
        if r == m:
            continue          # 只看不满秩的
        print("\n--- 找到线性部分不满秩的实例（lin 秩 = %d / m = %d）---" % (r, m))
        print("  线性子式（%d 个）：" % len(lin))
        for d in lin: print("     ", sp.factor(d))
        print("  高次子式（%d 个），前 5 个：" % len(hi))
        for d in hi[:5]: print("     ", sp.factor(d))
        # 线性部分的解集
        solL = sp.linsolve([sp.Eq(d, 0) for d in lin], *th)
        print("\n  线性部分的解集 = %s" % (solL,))
        # 全部子式的解集（Groebner）
        allp = lin + hi
        G = sp.groebner(allp, *th, order='lex')
        print("  全部子式的 Groebner 基 = %s" % [str(g) for g in G.exprs])
        sols = sp.solve(allp, th, dict=True)
        print("  全部子式的解 = %s （%d 个）" % ([{str(a): str(b) for a, b in s_.items()} for s_ in sols], len(sols)))
        # 高次部分限制到线性解集：参数化
        tups = list(solL)
        if tups:
            tup = tups[0]
            params = sorted({f for e in tup for f in e.free_symbols}, key=str)
            subs = {}
            # 用 linsolve 的参数化：变量 -> 表达式
            piv = [i for i, e in enumerate(tup) if not e.free_symbols]
            print("  参数 = %s" % ([str(p) for p in params],))
            if params:
                subs = {th[i]: tup[i] for i in range(len(th))}
                print("  把线性参数化解代入高次子式：")
                for d in hi:
                    d2 = sp.simplify(sp.expand(d.subs(subs)))
                    print("     %s  ->  %s" % (sp.factor(d), sp.factor(d2)))
        return
    print("未找到（说明线性部分普遍满秩）")


if __name__ == "__main__":
    main()
