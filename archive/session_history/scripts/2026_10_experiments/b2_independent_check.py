# -*- coding: utf-8 -*-
"""
b2_independent_check.py —— 对"Ω*_J 是单点"做**独立复核**

三个独立判据：
  ① Groebner 基是否全为一次式（⟹ 单点）
  ② 数值求解 (A)-系统（用 sympy 的数值求解 / 直接线性化）
  ③ 与项目 `exact_count` 的数值对照（若项目报 2 而我们只有 1 个 Θ，需解释）
  ④ **直接扫描**：在 Θ 空间的大范围网格上数 (A)-点数
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


def WJ(t, r, k, s, dC):
    W = [[Fr(1) if j == i else Fr(0) for j in range(dC)] for i in range(r)]
    idx = 0
    for i in range(k):
        row = [Fr(0)] * dC; row[r + i] = Fr(1)
        for j in range(k, s):
            row[r + j] = t[idx]; idx += 1
        W.append(row)
    return W


def get_instance(n, want_s, seed):
    rng = random.Random(seed)
    for _ in range(400000):
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
    print("=== 独立复核：Ω*_J 是单点？（判据 ①④）===")
    rng = random.Random(13579)
    for ss, n in [(3, 5), (4, 6)]:
        inst = get_instance(n, ss, 20270000)
        if inst is None:
            print("(1,%d) 无实例" % ss); continue
        dC, s, AT, BAT = inst["dC"], inst["s"], inst["AT"], inst["BAT"]
        r, k = 1, 1; m = k * (s - k)
        print("\n--- (k=1, s=%d), n=%d, m=%d ---" % (s, n, m))
        # 判据④：网格扫描 (A)-点数（范围 ±4，整数格）
        cnt = 0; pts = []
        for combo in itertools.product(range(-4, 5), repeat=m):
            t = [Fr(x) for x in combo]
            W = WJ(t, r, k, s, dC); WB = W + BAT
            if rk(WB + mm(W, AT)) == rk(WB):
                cnt += 1; pts.append(combo)
        print("  ④ 整数格 (±4)^%d = %d 点上，(A)-点数 = %d" % (m, 9**m, cnt))
        print("     命中点：%s" % (pts[:8],))
        # 判据①：Groebner
        th = sp.symbols('t0:%d' % m)
        if m == 1: th = (th,)
        Ws = [[sp.Integer(1) if j == i else sp.Integer(0) for j in range(dC)] for i in range(r)]
        idx = 0
        for i in range(k):
            row = [sp.Integer(0)] * dC
            row[r + i] = sp.Integer(1)
            for j in range(k, s):
                row[r + j] = th[idx]; idx += 1
            Ws.append(row)
        R = lambda M: [[sp.Rational(x.numerator, x.denominator) for x in row] for row in M]
        ATs, BATs = R(AT), R(BAT)
        WAs = [[sp.expand(sum(Ws[i][t] * ATs[t][j] for t in range(len(ATs))))
                for j in range(dC)] for i in range(len(Ws))]
        WB = [row[:] for row in Ws] + [row[:] for row in BATs]
        MB = [row[:] for row in Ws] + [row[:] for row in BATs] + [row[:] for row in WAs]
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
        alllin = all(sp.Poly(g, *th).total_degree() == 1 for g in ex)
        print("  ① Groebner 基 = %s" % [str(g) for g in ex])
        print("     全为一次式？%s  ⟹ %s" % (alllin, "Ω*_J 是**单点** ✓" if alllin else "非单点 ✗"))
        sols = sp.solve(polys, th, dict=True)
        print("     解：%s" % [{str(kk): str(vv) for kk, vv in s_.items()} for s_ in sols])
    print("\n【结论】若 ①、④ 一致指向单点，则：")
    print("   支 B 的 (A)-解 = 每层 J 恰 1 个 ⟹ 总解数 = #J = C(s,k)（多项式）")


if __name__ == "__main__":
    main()
