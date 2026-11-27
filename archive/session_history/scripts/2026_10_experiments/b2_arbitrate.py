# -*- coding: utf-8 -*-
"""
b2_arbitrate.py —— 仲裁：Groebner 基 {t0,t2} vs 数值 (A) 在 (0,1,0) 处为 False

做法：对该实例，逐个 (ρ+1) 阶子式在 (0,1,0) 与 (0,0,0) 处**求值**，
      并直接检验 rank 条件。看哪个子式在 (0,1,0) 处非零（那就说明它不是解）。
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


def main():
    print("=== 仲裁 ===")
    for t in range(10):
        inst = get_instance(6, 4, 20320000 + 400 + t)
        if inst is None: continue
        dC, s, AT, BAT = inst["dC"], inst["s"], inst["AT"], inst["BAT"]
        r, k = 1, 1; m = s - 1
        th = sp.symbols('t0:%d' % m)
        if m == 1: th = (th,)
        Wsym = [[sp.Integer(1), sp.Integer(0)] + [sp.Integer(0)] * (dC - 2)]
        Wsym.append([sp.Integer(0), sp.Integer(1)] + list(th))
        Wsym = [row[:dC] for row in Wsym]
        R = lambda M: [[sp.Rational(x.numerator, x.denominator) for x in row] for row in M]
        ATs, BATs = R(AT), R(BAT)
        WAs = [[sp.expand(sum(Wsym[i][a] * ATs[a][j] for a in range(len(ATs))))
                for j in range(dC)] for i in range(len(Wsym))]
        WBs = [row[:] for row in Wsym] + [row[:] for row in BATs]
        MBs = [row[:] for row in Wsym] + [row[:] for row in BATs] + [row[:] for row in WAs]
        nr, nc = len(MBs), len(MBs[0])
        # ρ 的精确值：取一般位置的秩
        rho = 0
        for _ in range(30):
            sub = {th[i]: sp.Rational(random.randint(-5, 5), random.choice([1, 2, 3]))
                   for i in range(m)}
            Wn = [[sp.nsimplify(e.subs(sub)) for e in row] for row in WBs]
            rho = max(rho, len(sp.Matrix(Wn).rref()[1]))
        print("\n--- 实例 #%d : MB %d×%d, ρ=%d ---" % (t, nr, nc, rho))
        # 逐个 (ρ+1) 阶子式，在 Θ=0 与 Θ=(0,1,0) 处求值
        vals0, vals1 = [], []
        for ri in itertools.combinations(range(nr), rho + 1):
            for cj in itertools.combinations(range(nc), rho + 1):
                d = sp.expand(sp.Matrix([[MBs[i][j] for j in cj] for i in ri]).det())
                if d == 0: continue
                v0 = sp.simplify(d.subs({th[i]: 0 for i in range(m)}))
                v1 = sp.simplify(d.subs({th[0]: 0, th[1]: 1, th[2]: 0})) if m == 3 else None
                vals0.append((ri, cj, d, v0, v1))
        print("  非零子式 %d 个" % len(vals0))
        nz1 = [(ri, cj, d, v1) for (ri, cj, d, v0, v1) in vals0 if v1 not in (None, 0)]
        print("  在 Θ=(0,1,0) 处**非零**的子式个数 = %d" % len(nz1))
        for (ri, cj, d, v1) in nz1[:6]:
            print("     rows=%s cols=%s : %s  ->  %s" % (ri, cj, sp.factor(d), v1))
        # 数值 rank 对照
        W = WJ_of([Fr(0), Fr(1), Fr(0)], r, k, s, dC); WB = W + BAT
        print("  数值（Θ=(0,1,0)）: rk[W;B]=%d, rk[W;B;WĀ]=%d ⟹ (A)=%s"
              % (rk(WB), rk(WB + mm(W, AT)), rk(WB + mm(W, AT)) == rk(WB)))
        if nz1 and rk(WB + mm(W, AT)) == rk(WB):
            print("  ⚠️⚠️ 矛盾：子式非零但 rank 相等 —— 说明 rank 相等**不等价于**全部子式为零 ✗")
            print("      ⟹ 或 ρ 取错了（应取 rk[W;B] 的**一般值**，而非 max over 采样）")
        return


if __name__ == "__main__":
    main()
