# -*- coding: utf-8 -*-
"""
b2_proof_step3.py —— 关键判据的普遍性检验：
   ① 全部子式的**线性部分**是否张成 m 维（⟹ 线性部分唯一确定 Θ）？
   ② 全部**高次部分**是否在 (线性部分=0) 的点上自动消失？

若 ①+② 普遍成立，则 Ω*_J 恒为 {Θ=0}，证明只需给出 ①、② 的论证。
本脚本对**多实例多形状**统计 ①②。
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


def get_instance(n, r, want_k, want_s, seed, tries=150000):
    rng = random.Random(seed)
    for _ in range(tries):
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
    lin_rows = []   # 线性部分的系数向量
    hi_polys = []
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            d = sp.expand(sp.Matrix([[MB[i][j] for j in cj] for i in ri]).det())
            if d == 0: continue
            P = sp.Poly(d, *th)
            if P.total_degree() <= 1:
                lin_rows.append([sp.nsimplify(P.coeff_monomial(v)) for v in th])
            else:
                hi_polys.append(d)
    rank_lin = sp.Matrix(lin_rows).rank() if lin_rows else 0
    # ② 在线性部分的公共零点（= 0，因满秩）上，高次是否恒 0
    zero_sub = {v: sp.Integer(0) for v in th}
    hi_zero_at_0 = all(sp.expand(d.subs(zero_sub)) == 0 for d in hi_polys)
    # ③ 高次子式是否 ∈ 线性部分生成的理想
    #    —— 当线性部分满秩时，理想 I = (t_0,...,t_{m-1})，
    #       而 d ∈ I ⟺ d 无常数项 ⟺ d(0)=0（因为 I 就是所有无常数项的多项式）
    if rank_lin == m:
        all_in_ideal = all(sp.expand(d.subs(zero_sub)) == 0 for d in hi_polys)
    else:
        all_in_ideal = None
    return dict(m=m, rho=rho, n_lin=len(lin_rows), rank_lin=rank_lin,
                n_hi=len(hi_polys), hi_zero_at_0=hi_zero_at_0,
                all_in_ideal=all_in_ideal)


def main():
    print("=== 关键判据的普遍性 ===")
    print("%-22s %4s %4s %6s %8s %6s %8s %10s" %
          ("(r,k,s)", "m", "rho", "#线性", "秩(线性)", "#高次", "0处为0", "∈线性理想"))
    print("-" * 82)
    cases = [(1, 1, 3, 5), (1, 1, 4, 6), (1, 1, 5, 7), (1, 2, 3, 6), (1, 2, 4, 7)]
    for (r, kk, ss, n) in cases:
        cnt_ok = 0; tot = 0
        for t in range(4):
            inst = get_instance(n, r, kk, ss, 20310000 + 1000 * kk + 100 * ss + t)
            if inst is None: continue
            try:
                res = analyze(inst)
            except Exception as e:
                print("%-22s 分析失败: %s" % ("(r=%d,k=%d,s=%d)" % (r, kk, ss), e)); break
            tot += 1
            tag = "(r=%d,k=%d,s=%d)" % (r, kk, ss)
            print("%-22s %4d %4d %6d %8d %6d %8s %10s"
                  % (tag, res['m'], res['rho'], res['n_lin'], res['rank_lin'],
                     res['n_hi'], res['hi_zero_at_0'], res['all_in_ideal']))
            if res['rank_lin'] == res['m']:
                cnt_ok += 1
        if tot:
            print("   ⟹ %-18s : 线性部分满秩 %d/%d" % ("(r=%d,k=%d,s=%d)" % (r, kk, ss), cnt_ok, tot))
        print()


if __name__ == "__main__":
    main()
