# -*- coding: utf-8 -*-
"""
b2_lemmaA.py —— 引理 A 的精确判据：线性部分的**系数矩阵是否可逆**？

若线性子式恰好是 m 个、且其 m×m 系数矩阵行列式 != 0，则
    线性部分的唯一零点是 Θ=0 ✓

本脚本：① 数线性子式个数；② 抽其系数矩阵；③ 算行列式；④ 报告秩。
并在多实例多形状上统计"是否恒可逆"。
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


def analyze(inst, verbose=False):
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
    lin = []   # (rows, cols, poly, coeff vector)
    hi = []
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            d = sp.expand(sp.Matrix([[MB[i][j] for j in cj] for i in ri]).det())
            if d == 0: continue
            P = sp.Poly(d, *th)
            if P.total_degree() <= 1:
                lin.append((ri, cj, d, [sp.nsimplify(P.coeff_monomial(v)) for v in th]))
            else:
                hi.append((ri, cj, d))
    if verbose:
        print("   [W;B] %d×%d ; MB %d×%d ; ρ=%d" % (len(WB), nc, nr, nc, rho))
        print("   线性子式 %d 个；高次 %d 个" % (len(lin), len(hi)))
        for (ri, cj, d, cv) in lin:
            print("     lin rows=%s cols=%s : %s   coeff=%s" % (ri, cj, sp.factor(d), cv))
    if not lin:
        return dict(m=m, nlin=0, rank=0, square=False, det=None)
    Msq = sp.Matrix([cv for (_, _, _, cv) in lin])
    square = (Msq.rows == Msq.cols == m)
    det = sp.nsimplify(Msq.det()) if square else None
    return dict(m=m, nlin=len(lin), rank=Msq.rank(), square=square, det=det)


def main():
    print("=== 引理 A：线性部分的系数矩阵 ===")
    print("%-14s %4s %6s %6s %9s %12s" % ("(k,s)", "m", "#线性", "秩", "方阵?", "det!=0"))
    print("-" * 60)
    ok = 0; tot = 0
    for ss, n in [(3, 5), (4, 6), (5, 7)]:
        for t in range(4):
            inst = get_instance(n, ss, 20320000 + 100 * ss + t)
            if inst is None:
                print("(1,%d) 实例 %d 未找到" % (ss, t)); continue
            res = analyze(inst, verbose=(t == 0 and ss == 3))
            tot += 1
            good = (res['rank'] == res['m'])
            if good: ok += 1
            print("%-14s %4d %6d %6d %9s %12s"
                  % ("(1,%d)#%d" % (ss, t), res['m'], res['nlin'], res['rank'],
                     str(res['square']), str(res['det'] not in (None, 0))))
        print()
    print("⟹ 线性部分满秩 %d/%d" % (ok, tot))
    if ok == tot and tot:
        print("⟹ **引理 A 在这些实例上成立**：线性部分唯一确定 Θ=0 ✓")


if __name__ == "__main__":
    main()
