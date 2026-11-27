# -*- coding: utf-8 -*-
"""
b2_proof_step2.py —— 真机制探测：二次子式在"线性子式的公共零点"上是否**自动为零**？

若成立，则 (A) 的零点集 = 线性子式的零点集 ⟹ 只需解**线性方程组** ⟹ Θ 唯一。
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


def setup(inst):
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
            if d != 0:
                polys.append((ri, cj, d))
    return th, polys, m, rho, MB, WB


def main():
    for ss, n in [(3, 5), (4, 6)]:
        inst = get_instance(n, ss, 20300000 + ss)
        if inst is None:
            print("(1,%d) 无实例" % ss); continue
        th, polys, m, rho, MB, WB = setup(inst)
        print("\n=== (1,%d) n=%d : m=%d rho=%d, 子式 %d 个 ===" % (ss, n, m, rho, len(polys)))
        lin = [(ri, cj, d) for (ri, cj, d) in polys if sp.Poly(d, *th).total_degree() == 1]
        hi = [(ri, cj, d) for (ri, cj, d) in polys if sp.Poly(d, *th).total_degree() >= 2]
        print("  线性子式 %d 个；高次子式 %d 个" % (len(lin), len(hi)))
        # 线性子式的公共零点
        if lin:
            sol = sp.linsolve([sp.Eq(d, 0) for (_, _, d) in lin], *th)
            print("  线性子式的公共零点 = %s" % (sol,))
            # 取参数化解，代入高次子式
            tups = list(sol)
            if tups and len(tups) == 1:
                tup = tups[0]
                subs_map = {}
                params = set()
                for i, v in enumerate(th):
                    e = tup[i]
                    fs = e.free_symbols
                    if fs:
                        params |= fs
                        subs_map[v] = e
                    else:
                        subs_map[v] = e
                print("  参数 = %s" % (params,))
                print("  把参数化解代入高次子式（看是否恒 0）：")
                allzero = True
                for (ri, cj, d) in hi:
                    d2 = sp.simplify(sp.expand(d.subs(subs_map)))
                    isz = (d2 == 0)
                    if not isz: allzero = False
                    print("    %s -> %s   %s" % ((ri, cj), d2, "≡0 ✓" if isz else "≠0 ✗"))
                print("  ⟹ 高次子式在**整个线性簇**上恒为零？ %s" % allzero)
                if allzero:
                    print("  ⟹⟹ **(A) 的零点集 = 线性子式的零点集** ⟹ 只需解线性方程组 ✓")
        # 也检查 2 个线性式是否独立（⟹ 唯一解）
        if len(lin) >= 2:
            A = [[sp.Poly(d, *th).coeff_monomial(v) for v in th] for (_, _, d) in lin]
            print("  线性子式的系数矩阵秩 = %s （变量数 %d）"
                  % (sp.Matrix(A).rank(), m))


if __name__ == "__main__":
    main()
