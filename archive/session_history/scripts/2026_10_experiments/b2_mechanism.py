# -*- coding: utf-8 -*-
"""
b2_mechanism.py —— 两层机制的精确定式

设  L = {线性子式的公共零点}（可能是正维数线性子空间）
     H = {高次子式的集合}

观察到的两层结构：
   (层1) L 非空（Θ=0 ∈ L）
   (层2) H 的每个元素**限制到 L 上恒为零**  ⟹ (A)-集 ⊆ L
   而 (A)-集 = L ∩ (H 的所有零点) —— Groebner 显示它**仍是单点**（不是整个 L！）

⚠️ 注意矛盾点：若 H|_L ≡ 0，则 L ⊆ H 的零点集 ⟹ (A)-集 ⊇ L ⟹ 应是整个 L（正维数）
   但 Groebner 说 (A)-集是单点 ✗ ⟹ **我对"限制到 L 上"的理解有误**

本脚本：对不满秩的实例，**精确**做 subs 并检验 H|_L 是否真为 0（而不是舍入）。
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
    m = s - 1
    th = sp.symbols('t0:%d' % m)
    if m == 1: th = (th,)
    W = [[sp.Integer(1), sp.Integer(0)] + [sp.Integer(0)] * (dC - 2)]
    W.append([sp.Integer(0), sp.Integer(1)] + list(th))
    W = [row[:dC] for row in W]
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
    print("=== 两层机制的精确定式 ===")
    for t in range(10):
        inst = get_instance(6, 4, 20320000 + 400 + t)
        if inst is None: continue
        th, lin, hi, m, rho = build(inst)
        M = sp.Matrix([[sp.Poly(d, *th).coeff_monomial(v) for v in th] for d in lin])
        r = M.rank()
        if r == m: continue
        print("\n--- 线性部分秩 %d / m=%d ---" % (r, m))
        print("  线性子式：%s" % [str(sp.factor(d)) for d in lin])
        solL = sp.linsolve([sp.Eq(d, 0) for d in lin], *th)
        tup = list(solL)[0]
        print("  L = %s" % (tup,))
        params = sorted({f for e in tup for f in e.free_symbols}, key=str)
        print("  L 的自由参数 = %s （维数 = %d）" % ([str(p) for p in params], len(params)))
        subs = {th[i]: tup[i] for i in range(len(th))}
        print("  把 L 的参数化代入**高次**子式：")
        nonzero = 0
        for d in hi:
            d2 = sp.expand(d.subs(subs))
            if sp.simplify(d2) != 0:
                nonzero += 1
                print("     %s  ->  %s   ← 非零！" % (sp.factor(d), sp.factor(d2)))
        print("  高次子式在 L 上非零的个数 = %d / %d" % (nonzero, len(hi)))
        if nonzero == 0:
            print("  ⚠️ 全部为零 ⟹ 按理 (A)-集应 ⊇ L（正维数）")
            print("     但 Groebner 说 (A)-集是单点 ⟹ **矛盾** ⟹ 需检查 subs 是否正确")
        else:
            print("  ⟹ 高次子式把 L 切小；其零点集 = (A)-集（Groebner: 单点）✓")
        G = sp.groebner(lin + hi, *th, order='lex')
        print("  全部子式的 Groebner 基 = %s" % [str(g) for g in G.exprs])
        return
    print("未找到不满秩实例")


if __name__ == "__main__":
    main()
