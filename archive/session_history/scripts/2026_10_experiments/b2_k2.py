# -*- coding: utf-8 -*-
"""
b2_k2.py —— 把"Ω*_J 单点"的检验扩到 **k ≥ 2**

k≥2 时 Θ 是 k×(s−k) 矩阵（m = k(s−k) 个变量），W_J(Θ) 的后 k 行含 Θ 的行。
检查：Groebner 基是否仍**全为一次式**（⟹ 单点）。
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


def get_instance(n, r, want_k, want_s, seed, tries=60000):
    rng = random.Random(seed)
    for it in range(tries):
        Ac = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        Lc = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(r)]
        if rk(Cc) != 1 or rk(Lc) != r or rk(Lc + Cc) != r + 1: continue
        try: Lx, eta = p1(Ac, Cc, Lc)
        except Exception: continue
        if not Lx: continue
        q0 = sum(eta); k = q0 - r
        if k != want_k: continue
        bt = build_norm_T(Ac, Cc, Lc, Lx)
        if bt is None: continue
        dC, s, k2, r2, AT, BAT = bt
        if (r2, k2) != (r, want_k) or s != want_s: continue
        if 2 * 1 + q0 >= n: continue
        return dict(dC=dC, s=s, AT=AT, BAT=BAT, r=r, k=k)
    return None


def analyze(inst):
    dC, s, AT, BAT, r, k = inst["dC"], inst["s"], inst["AT"], inst["BAT"], inst["r"], inst["k"]
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
    G = sp.groebner(polys, *th, order='lex')
    ex = list(G.exprs)
    degs = sorted({sp.Poly(g, *th).total_degree() for g in ex})
    sols = sp.solve(polys, th, dict=True)
    return dict(m=m, rho=rho, n_poly=len(polys), gb=[str(g) for g in ex],
                degs=degs, n_sol=len(sols),
                sols=[{str(a): str(b) for a, b in x.items()} for x in sols[:4]])


def main():
    print("=== k>=2：Groebner 基是否仍全为一次式？ ===")
    for (r, kk, ss, n) in [(1, 2, 3, 6), (1, 2, 4, 7), (2, 2, 3, 7)]:
        inst = get_instance(n, r, kk, ss, 20280000 + 100 * kk + ss + r)
        if inst is None:
            print("(r=%d,k=%d,s=%d) 无实例" % (r, kk, ss)); continue
        res = analyze(inst)
        print("\n--- r=%d, k=%d, s=%d, n=%d ---" % (r, kk, ss, n))
        print("   m=%d  rho=%d  子式=%d" % (res['m'], res['rho'], res['n_poly']))
        print("   Groebner 基（次数 %s）：%s" % (res['degs'], res['gb'][:6]))
        print("   解数 = %d ；解 = %s" % (res['n_sol'], res['sols']))
        print("   ⟹ 基全为一次式？ %s" % (res['degs'] == [1]))
    print("\n【判读】若 k≥2 时基仍全为一次式 ⟹ 'Ω*_J 单点' 可能对一切 k 成立")


if __name__ == "__main__":
    main()
