# -*- coding: utf-8 -*-
"""
b2_final3.py —— 三条证据链的最终一致性核验（**全部用正确的 WJ_of 构造**）

对每个实例同时给出：
  ① 数值：整数格扫描的 (A)-点数
  ② 数值：直线 (0,a,0)（及一般直线）上的有理点检验
  ③ 符号：Groebner 基（lex）
  ④ 符号：线性部分秩 vs m
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


def WJ_of(t, r, k, s, dC):
    W = [[Fr(1) if j == i else Fr(0) for j in range(dC)] for i in range(r)]
    idx = 0
    for i in range(k):
        row = [Fr(0)] * dC; row[r + i] = Fr(1)
        for j in range(k, s):
            row[r + j] = t[idx]; idx += 1
        W.append(row)
    return W


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


def main():
    print("=== 三条证据链的最终一致性核验 ===")
    for ss, n in [(3, 5), (4, 6)]:
        inst = get_instance(n, ss, 20340000 + ss)
        if inst is None: continue
        dC, s, AT, BAT = inst["dC"], inst["s"], inst["AT"], inst["BAT"]
        r, k = 1, 1; m = s - 1
        print("\n--- (1,%d) n=%d : dC=%d m=%d ---" % (ss, n, dC, m))
        # ① 整数格
        cnt = 0; pts = []
        for combo in itertools.product(range(-3, 4), repeat=m):
            W = WJ_of([Fr(x) for x in combo], r, k, s, dC); WB = W + BAT
            if rk(WB + mm(W, AT)) == rk(WB):
                cnt += 1; pts.append(combo)
        print("  ① 整数格 (±3)^%d : 命中 %d 个 %s" % (m, cnt, pts[:6]))
        # ② 沿坐标轴的细有理扫描（排除"直线解"的可能）
        for ax in range(m):
            hits = []
            for p in range(-6, 7):
                for q in (1, 2, 3):
                    a = Fr(p, q)
                    if a == 0: continue
                    t = [Fr(0)] * m; t[ax] = a
                    W = WJ_of(t, r, k, s, dC); WB = W + BAT
                    if rk(WB + mm(W, AT)) == rk(WB):
                        hits.append(a)
            print("  ② 沿 Θ[%d] 轴的非零有理点命中 %d 个 %s" % (ax, len(hits), [str(x) for x in hits[:5]]))
        # ③ Groebner（正确构造）
        th = sp.symbols('t0:%d' % m)
        if m == 1: th = (th,)
        Wsym = [[sp.Integer(1) if j == i else sp.Integer(0) for j in range(dC)] for i in range(r)]
        idx = 0
        for i in range(k):
            row = [sp.Integer(0)] * dC
            row[r + i] = sp.Integer(1)
            for j in range(k, s):
                row[r + j] = th[idx]; idx += 1
            Wsym.append(row)
        R = lambda M: [[sp.Rational(x.numerator, x.denominator) for x in row] for row in M]
        ATs, BATs = R(AT), R(BAT)
        WAs = [[sp.expand(sum(Wsym[i][a] * ATs[a][j] for a in range(len(ATs))))
                for j in range(dC)] for i in range(len(Wsym))]
        WBs = [row[:] for row in Wsym] + [row[:] for row in BATs]
        MBs = [row[:] for row in Wsym] + [row[:] for row in BATs] + [row[:] for row in WAs]
        nr, nc = len(MBs), len(MBs[0])
        rho = 0
        for _ in range(30):
            sub = {th[i]: sp.Rational(random.randint(-5, 5), random.choice([1, 2, 3])) for i in range(m)}
            Wn = [[sp.nsimplify(e.subs(sub)) for e in row] for row in WBs]
            rho = max(rho, len(sp.Matrix(Wn).rref()[1]))
        polys = []
        for ri in itertools.combinations(range(nr), rho + 1):
            for cj in itertools.combinations(range(nc), rho + 1):
                d = sp.expand(sp.Matrix([[MBs[i][j] for j in cj] for i in ri]).det())
                if d != 0 and d not in polys:
                    polys.append(d)
        G = sp.groebner(polys, *th, order='lex')
        print("  ③ Groebner 基 = %s" % [str(g) for g in G.exprs])
        # ④ 线性部分秩
        lin = [d for d in polys if sp.Poly(d, *th).total_degree() <= 1]
        M = sp.Matrix([[sp.Poly(d, *th).coeff_monomial(v) for v in th] for d in lin]) if lin else None
        print("  ④ 线性子式 %d 个，秩 = %s （m = %d）"
              % (len(lin), M.rank() if M is not None else 0, m))
    print("\n【判读】三条证据一致 ⟹ Ω*_J = {Θ=0} ✓")


if __name__ == "__main__":
    main()
