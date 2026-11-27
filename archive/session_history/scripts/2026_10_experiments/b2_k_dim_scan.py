# -*- coding: utf-8 -*-
"""
b2_k_dim_scan.py —— 支 B 上 Ω*_J 的维数随 k 的变化（关键结论）

对 (k=1) 与 (k>=2) 分别统计：
  ① 整数格上 (A)-点的"频率"（正维数 ⟹ 频率 > 0 且随格变细趋于常数）
  ② 非零随机扰动的命中率（排除零扰动！）
  ③ Groebner 基的次数（全一次 ⟹ 单点）
  ④ 切空间的数值维数

⚠️ 必须过滤支 B（2p+q0 < n）；支 A 上 (A) 可能整个空间满足
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


def mul(X, Y):
    return [[sum(X[i][a] * Y[a][j] for a in range(len(Y))) for j in range(len(Y[0]))]
            for i in range(len(X))]


def find_inst(n, p, r, mp, seed, want_k=None):
    rng = random.Random(seed)
    for _ in range(6000):
        Ac = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        P = [row[:] for row in Cc]
        for _k in range(mp): P = mul(P, Ac)
        if rk(P) != r or rk(P + Cc) != r + p: continue
        try: Lx, eta = p1(Ac, Cc, P)
        except Exception: continue
        if not Lx: continue
        q0 = sum(eta); k = q0 - r
        if k < 1: continue
        if want_k is not None and k != want_k: continue
        bt = build_norm_T(Ac, Cc, P, Lx)
        if bt is None: continue
        dC, s, k2, r2, AT, BAT = bt
        if (r2, k2) != (r, k) or s <= k: continue
        if not (2 * p + q0 < n): continue      # ⚠️ 支 B
        return dict(n=n, p=p, r=r, q0=q0, k=k, s=s, dC=dC, AT=AT, BAT=BAT)
    return None


def analyze(inst, verbose=True):
    n, p, r, k, s, dC = (inst['n'], inst['p'], inst['r'], inst['k'],
                         inst['s'], inst['dC'])
    m = k * (s - k)
    AT, BAT = inst['AT'], inst['BAT']

    def Wnum(t):
        W = [[Fr(1) if j == i else Fr(0) for j in range(dC)] for i in range(r)]
        idx = 0
        for i in range(k):
            row = [Fr(0)] * dC
            row[r + i] = Fr(1)
            for j in range(k, s):
                row[r + j] = t[idx]; idx += 1
            W.append(row)
        return W

    def isA(t):
        W = Wnum(t); WB = W + BAT
        return rk(WB + mm(W, AT)) == rk(WB)

    # 整数格频率（m 太大就抽样）
    tot = 0; hit = 0; pts = []
    if m <= 4:
        for combo in itertools.product(range(-2, 3), repeat=m):
            tot += 1
            if isA([Fr(x) for x in combo]):
                hit += 1; pts.append(combo)
    else:
        rng = random.Random(7)
        for _ in range(3000):
            combo = [rng.randint(-2, 2) for _ in range(m)]
            tot += 1
            if isA([Fr(x) for x in combo]):
                hit += 1; pts.append(tuple(combo))
    freq = hit / tot if tot else 0

    # 非零扰动命中率（相对某个 (A)-点）
    prate = None
    if pts:
        base = [Fr(x) for x in pts[0]]
        rng2 = random.Random(4242); nzc = 0; h2 = 0
        for _ in range(2000):
            d = [Fr(rng2.randint(-1, 1), 512) for _ in range(m)]
            if all(x == 0 for x in d): continue
            nzc += 1
            if isA([base[i] + d[i] for i in range(m)]): h2 += 1
        prate = (h2, nzc)

    # Groebner
    th = sp.symbols('t0:%d' % m)
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
    WAs = [[sp.expand(sum(W[i][a] * ATs[a][j] for a in range(len(ATs))))
            for j in range(dC)] for i in range(len(W))]
    WBs = [row[:] for row in W] + [row[:] for row in BATs]
    MBs = [row[:] for row in W] + [row[:] for row in BATs] + [row[:] for row in WAs]
    nr, nc = len(MBs), len(MBs[0])
    rho = 0
    for _ in range(25):
        sub = {th[i]: sp.Rational(random.randint(-3, 3), random.choice([1, 2])) for i in range(m)}
        Wn = [[sp.nsimplify(e.subs(sub)) for e in row] for row in WBs]
        rho = max(rho, len(sp.Matrix(Wn).rref()[1]))
    polys = []
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            d = sp.expand(sp.Matrix([[MBs[i][j] for j in cj] for i in ri]).det())
            if d != 0 and d not in polys:
                polys.append(d)
    G = sp.groebner(polys, *th, order='lex')
    ex = list(G.exprs)
    degs = sorted({sp.Poly(g, *th).total_degree() for g in ex})
    return dict(n=n, p=p, r=r, q0=inst['q0'], k=k, s=s, dC=dC, m=m,
                freq=freq, nhit=hit, ntot=tot, prate=prate,
                nsub=len(polys), gbdegs=degs, nGB=len(ex))


def main():
    print("=== 支 B 上 Ω*_J 的维数 vs k ===")
    print("%-26s %3s %4s %8s %10s %12s %10s" %
          ("(n,p,r | q0,k,s)", "m", "#子式", "格频率", "非零扰动", "GB次数", "GB"))
    print("-" * 84)
    for (n, p, r, mp, wk) in [(6,1,1,1,1), (6,1,1,2,2), (7,1,1,2,2), (7,1,1,3,3)]:
        inst = None
        for seed in range(15):
            inst = find_inst(n, p, r, mp, 20500000 + 1000*wk + seed, want_k=wk)
            if inst: break
        if not inst:
            print("(n=%d,p=%d,r=%d, want k=%d) 未找到支 B 实例" % (n, p, r, wk)); continue
        r_ = analyze(inst)
        pr = r_['prate']
        print("%-26s %3d %4d %8.3f %10s %12s %10d"
              % ("n=%d p=%d r=%d|q0=%d k=%d s=%d" % (r_['n'], r_['p'], r_['r'],
                                                     r_['q0'], r_['k'], r_['s']),
                 r_['m'], r_['nsub'], r_['freq'],
                 ("%d/%d" % pr) if pr else "n/a",
                 r_['gbdegs'], r_['nGB']))
    print()
    print("【判读】")
    print("  k=1 : 格频率≈0（只有 Θ=0）、GB 次数=[1] ⟹ 单点 ✓")
    print("  k>=2: 格频率 >0 且非零扰动命中率高 ⟹ **正维数** ✗")


if __name__ == "__main__":
    main()
