# -*- coding: utf-8 -*-
"""
b2_compare.py —— 决定性对照：同一实例上
   ① 项目的 `exact_count_14_elim.exact_count` 报的解数
   ② 我的 Groebner 法在 (A)-系统上算出的**不同 Θ-解数**
"""
import os, io, contextlib, itertools, random
from fractions import Fraction as Fr
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; orb = _ns["orb"]; condA = _ns["condA"]; toF = _ns["toF"]
_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]; build_norm_T = _t["build_norm_T"]

# 复用项目的 exact_count
_ec = {}
with open(os.path.join(_HERE, "exact_count_14_elim.py"), encoding="utf-8") as fh:
    src2 = fh.read()
head2 = src2.split("# ---------------- 主流程 ----------------")[0]
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(head2, "ec", "exec"), _ec)
exact_count = _ec["exact_count"]


def groebner_theta_count(inst):
    """(A)-系统在 Θ 上的不同解数（用 Groebner 基逐解回代）"""
    dC, s, AT, BAT = inst["dC"], inst["s"], inst["AT"], inst["BAT"]
    r, k, p = 1, 1, 1
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
    sols = sp.solve(polys, th, dict=True)
    return dict(m=m, rho=rho, n_poly=len(polys), gb=[str(g) for g in G.exprs],
                n_sol=len(sols), sols=[{str(k): str(v) for k, v in s_.items()} for s_ in sols[:6]])


def main():
    print("=== 对照：项目的解数 vs Groebner 的 Θ-解数 ===")
    rng = random.Random(60606060)
    shown = 0
    for trial in range(200000):
        n = rng.randint(4, 8); p = 1; r = 1
        for _ in range(40):
            Am = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
            Cm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)]
            Lm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(r)]
            Ac, Cc, Lc = toF(Am), toF(Cm), toF(Lm)
            if rk(Cc) != p or rk(Lc) != r: continue
            if rk(Lc + Cc) != r + p: continue
            Z = orb(Lc, Ac, n) + orb(Cc, Ac, n); OC = orb(Cc, Ac, n)
            if rk(Z + OC) != rk(OC): continue
            try: Lx, eta = p1(Ac, Cc, Lc)
            except Exception: continue
            if not condA(Ac, Cc, Lx): continue
            q0 = sum(eta); dC = n - p; s = dC - r; k = q0 - r
            if k != 1 or (s - k) != 2: continue
            res = exact_count(Ac, Cc, Lc, Lx)
            if res is None or res.get('count') is None: continue
            bt = build_norm_T(Ac, Cc, Lc, Lx)
            if bt is None: continue
            dC2, s2, k2, r2, AT, BAT = bt
            inst = dict(dC=dC2, s=s2, AT=AT, BAT=BAT)
            try:
                g = groebner_theta_count(inst)
            except Exception as e:
                print("  n=%d (1,3)：项目解数=%s ；Groebner 失败：%s" % (n, res['count'], e))
                continue
            print("\n实例 n=%d  (k=1,s=%d)  m=%d" % (n, s, g['m']))
            print("  项目 exact_count 报解数 = %s （gcd 次数 %s）" % (res['count'], res['gcd_deg']))
            print("  Groebner: 子式 %d 个；基 = %s" % (g['n_poly'], g['gb']))
            print("  ⟹ Θ-解数 = %d ；解 = %s" % (g['n_sol'], g['sols']))
            shown += 1
            break
        if shown >= 3: break
    print("\n【判读】")
    print("  · 若项目解数 ≠ Θ-解数 ⟹ 两者数的**不是同一个东西**（项目数的是消元后谱变量的根数）")
    print("  · 若相等 ⟹ 需要进一步找差异")


if __name__ == "__main__":
    main()
