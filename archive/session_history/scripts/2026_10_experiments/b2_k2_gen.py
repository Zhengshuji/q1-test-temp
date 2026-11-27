# -*- coding: utf-8 -*-
"""
b2_k2_gen.py —— 用项目自己的 **L0 = CA^m 生成器**造 k>=2 的支 B 实例
（随机搜索几乎总给出 eta=1，即 k=0；项目 CLAUDE.md §4 已记录此事实）

目标：拿到 (k>=2, 支B: 2p+q0<n) 的实例，检验 Ω*_J 是否仍为单点。
"""
import os, io, contextlib, itertools, random
from fractions import Fraction as Fr
import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; orb = _ns["orb"]
_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]; build_norm_T = _t["build_norm_T"]


def find_L0_CAm(n, p, r, m_pow, seed):
    """L0 = C A^m_pow（取 m_pow 行）"""
    rng = random.Random(seed)
    for _ in range(4000):
        Ac = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        # 计算 C A^k
        def matmul(X, Y):
            return [[sum(X[i][k2] * Y[k2][j] for k2 in range(len(Y)))
                     for j in range(len(Y[0]))] for i in range(len(X))]
        P = [row[:] for row in Cc]
        for _k in range(m_pow):
            P = matmul(P, Ac)
        if rk(P) != r: continue
        # 要求 rank[L0;C] = r+p
        if rk(P + Cc) != r + p: continue
        try: Lx, eta = p1(Ac, Cc, P)
        except Exception: continue
        if not Lx: continue
        q0 = sum(eta); k = q0 - r
        if k < 1: continue
        bt = build_norm_T(Ac, Cc, P, Lx)
        if bt is None: continue
        dC, s, k2, r2, AT, BAT = bt
        if (r2, k2) != (r, k) or s <= k: continue
        return dict(n=n, p=p, r=r, q0=q0, k=k, s=s, dC=dC, AT=AT, BAT=BAT, Ac=Ac, Cc=Cc, Lc=P)
    return None


def main():
    print("=== 用 L0 = CA^m 生成器造 k>=2 实例 ===")
    got = None
    for (n, p, r, mp) in [(6,1,1,2), (7,1,1,2), (7,1,1,3), (8,1,1,3), (6,2,1,2), (7,2,1,2)]:
        for seed in range(6):
            inst = find_L0_CAm(n, p, r, mp, 20400000 + 1000*mp + 100*seed + n)
            if inst is None: continue
            print("  n=%d p=%d r=%d L0=CA^%d : q0=%d k=%d s=%d dC=%d"
                  % (n, p, r, mp, inst['q0'], inst['k'], inst['s'], inst['dC']))
            got = inst
            break
        if got: break
    if not got:
        print("  仍无 k>=1 实例（生成器也未成功）")
        return
    inst = got
    k, s, dC, r = inst['k'], inst['s'], inst['dC'], inst['r']
    m = k * (s - k)
    print("\n  选出实例：k=%d, s=%d, m=k(s-k)=%d, 支B? 2p+q0=%d < n=%d ? %s"
          % (k, s, m, 2*inst['p']+inst['q0'], inst['n'],
             2*inst['p']+inst['q0'] < inst['n']))
    AT, BAT = inst['AT'], inst['BAT']
    # 构造符号 W_J(Θ)（k 行 Θ，每行 s-k 个分量）
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
    WAs = [[sp.expand(sum(W[i][a] * ATs[a][j] for a in range(len(ATs))))
            for j in range(dC)] for i in range(len(W))]
    WBs = [row[:] for row in W] + [row[:] for row in BATs]
    MBs = [row[:] for row in W] + [row[:] for row in BATs] + [row[:] for row in WAs]
    nr, nc = len(MBs), len(MBs[0])
    rho = 0
    for _ in range(25):
        sub = {th[i]: sp.Rational(random.randint(-3, 3), random.choice([1,2]))
               for i in range(m)}
        Wn = [[sp.nsimplify(e.subs(sub)) for e in row] for row in WBs]
        rho = max(rho, len(sp.Matrix(Wn).rref()[1]))
    print("  [W;B] %d×%d ; ρ=%d" % (len(WBs), nc, rho))
    polys = []
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            d = sp.expand(sp.Matrix([[MBs[i][j] for j in cj] for i in ri]).det())
            if d != 0 and d not in polys:
                polys.append(d)
    print("  非零 (ρ+1)-子式 %d 个" % len(polys))
    # 数值：整数格扫描
    Wnum = W
    cnt = 0; pts = []
    if m <= 3:
        for combo in itertools.product(range(-2, 3), repeat=m):
            Wt = [[sp.Integer(1) if j == i else sp.Integer(0) for j in range(dC)] for i in range(r)]
            idx = 0
            for i in range(k):
                row = [sp.Integer(0)] * dC
                row[r + i] = sp.Integer(1)
                for j in range(k, s):
                    row[r + j] = sp.Integer(combo[idx]); idx += 1
                Wt.append(row)
            WAn = [[sum(Wt[i][a] * sp.Rational(AT[a][j].numerator, AT[a][j].denominator)
                        for a in range(len(AT))) for j in range(dC)] for i in range(len(Wt))]
            WBn = [row[:] for row in Wt] + [[sp.Rational(x.numerator, x.denominator) for x in row] for row in BAT]
            MAn = [r_[:] for r_ in WBn] + [[sp.expand(e) for e in r_] for r_ in WAn]
            if sp.Matrix(MAn).rank() == sp.Matrix(WBn).rank():
                cnt += 1; pts.append(combo)
        print("  整数格 (±2)^%d : 命中 %d 个 %s" % (m, cnt, pts[:6]))
    else:
        print("  m=%d 太大，跳过整数格扫描" % m)
    # Groebner
    G = sp.groebner(polys, *th, order='lex')
    ex = list(G.exprs)
    print("  Groebner 基 = %s" % [str(g) for g in ex][:8])
    print("  基全为一次式？ %s" % all(sp.Poly(g, *th).total_degree() == 1 for g in ex))
    sols = sp.solve(polys, th, dict=True)
    print("  解数 = %d ；解 = %s" % (len(sols), [{str(a): str(b) for a, b in x.items()} for x in sols[:4]]))


if __name__ == "__main__":
    main()
