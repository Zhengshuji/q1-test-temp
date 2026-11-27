# -*- coding: utf-8 -*-
"""
b2_verify.py —— 核验：Ω*_J 到底有几个解？（与项目 (1,3)=2 对照）

做法：
  ① 用 Groebner 基的 lex 形式**解出**全部解（回代）
  ② 直接随机采样找 (A)-点，看找到几个
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
        return dict(n=n, dC=dC, s=s, AT=AT, BAT=BAT)
    return None


def polys_of(inst):
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
    for _ in range(25):
        sub = {th[i]: sp.Rational(random.randint(-3, 3)) for i in range(m)}
        Wn = [[sp.nsimplify(e.subs(sub)) for e in row] for row in WB]
        rho = max(rho, len(sp.Matrix(Wn).rref()[1]))
    polys = []
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            d = sp.expand(sp.Matrix([[MB[i][j] for j in cj] for i in ri]).det())
            if d != 0 and d not in polys:
                polys.append(d)
    return th, polys


def main():
    print("=== 核验 Ω*_J 的解数 ===")
    for ss, seed in [(3, 20260204), (4, 20260205)]:
        n = 5 if ss == 3 else 6
        inst = get_instance(n, 1, 1, 1, ss, seed)
        if inst is None:
            print("(1,%d) 无实例" % ss); continue
        th, polys = polys_of(inst)
        print("\n--- (k=1, s=%d)  n=%d  m=%d  多项式 %d 个 ---" % (ss, n, len(th), len(polys)))
        for p in polys[:6]:
            print("   ", sp.factor(p))
        G = sp.groebner(polys, *th, order='lex')
        print("\n  Groebner 基（lex）：")
        for g in G.exprs:
            print("   ", sp.factor(g))
        # 解
        sols = sp.solve(polys, th, dict=True)
        print("\n  sympy.solve 给出的解（%d 个）：" % len(sols))
        for s_ in sols[:10]:
            print("   ", {str(k): str(v) for k, v in s_.items()})
        # 数值：直接主成分分解（随机点找解）
        print("\n  数值采样找 (A)-点（范围 ±3 的整数格）：")
        cnt = 0; pts = []
        for combo in itertools.product(range(-3, 4), repeat=len(th)):
            sub = {th[i]: sp.Integer(combo[i]) for i in range(len(th))}
            ok = all(sp.simplify(p.subs(sub)) == 0 for p in polys)
            if ok:
                cnt += 1; pts.append(combo)
        print("   整数格上命中 %d 个：%s" % (cnt, pts[:10]))
        # 精确实数解（若一元）
        if len(th) == 1:
            for p in polys:
                print("   一元多项式因式分解：", sp.factor(p), " 根：", sp.solve(p, th[0]))


if __name__ == "__main__":
    main()
