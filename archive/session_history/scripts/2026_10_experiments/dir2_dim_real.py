# -*- coding: utf-8 -*-
"""
dir2_dim_real.py -- 方向 2 (修正装置): 用 build_norm_T 的真实 A 测 Omega*_J 的维数

【为什么必须修正】
  上一版 (dir2_dim.py) 用**任意** A 代替真实 A -- 与真实 (A) 条件不一致 ⚠️
  真实装置: build_norm_T 给出 (dC, s, k, r, AT, BAT)，其中 AT 是真实的规范化 A。
  (A) 条件: rank[W(Theta);BAT;W(Theta)AT] = rank[W(Theta);BAT]

【可靠维数判据】纯幂检测 (每个变量是否有只含它的多项式在 Groebner 基中)
"""
import os, io, contextlib, itertools, random, signal
from fractions import Fraction as F

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

import sympy as sp


class TO(Exception):
    pass


def _h(sig, frm):
    raise TO()


try:
    signal.signal(signal.SIGALRM, _h)
    HAVE = True
except Exception:
    HAVE = False


def get_real(n, want_s, seed, tries=150000):
    """用 build_norm_T 取**真实装置**"""
    rng = random.Random(seed)
    for _ in range(tries):
        Ac = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)]]
        Lc = [[F(rng.randint(-1, 1)) for _ in range(n)]]
        if rk(Cc) != 1 or rk(Lc) != 1 or rk(Lc + Cc) != 2:
            continue
        try:
            Lx, eta = p1(Ac, Cc, Lc)
        except Exception:
            continue
        if not Lx:
            continue
        q0 = sum(eta); k = q0 - 1
        if k < 1:
            continue
        bt = build_norm_T(Ac, Cc, Lc, Lx)
        if bt is None:
            continue
        dC, s, k2, r2, AT, BAT = bt
        if (r2, k2) != (1, k) or s != want_s:
            continue
        if not (2 * 1 + q0 < n):     # 支 B
            continue
        return dict(n=n, q0=q0, k=k, s=s, dC=dC, AT=AT, BAT=BAT)
    return None


def Wsym(th, r, k, s, dC):
    W = [[sp.Integer(1) if j == i else sp.Integer(0) for j in range(dC)] for i in range(r)]
    idx = 0
    for i in range(k):
        row = [sp.Integer(0)] * dC
        row[r + i] = sp.Integer(1)
        for j in range(k, s):
            row[r + j] = th[idx]; idx += 1
        W.append(row)
    return W


def analyze(inst, tmo=30):
    dC, s, k, AT, BAT = inst['dC'], inst['s'], inst['k'], inst['AT'], inst['BAT']
    r = 1
    m = k * (s - k)
    th = sp.symbols('t0:%d' % m)
    W = Wsym(th, r, k, s, dC)
    R = lambda M: [[sp.Rational(x.numerator, x.denominator) for x in row] for row in M]
    ATs, BATs = R(AT), R(BAT)
    WAs = [[sp.expand(sum(W[i][a] * ATs[a][j] for a in range(len(ATs))))
            for j in range(dC)] for i in range(len(W))]
    WBs = [row[:] for row in W] + [row[:] for row in BATs]
    MBs = [row[:] for row in W] + [row[:] for row in BATs] + [row[:] for row in WAs]
    nr, nc = len(MBs), len(MBs[0])
    # rho: rank[WB] 的**一般值**（在 Theta 上）
    rho = 0
    rng2 = random.Random(5)
    for _ in range(10):
        sub = {th[i]: sp.Rational(rng2.randint(-3, 3)) for i in range(m)}
        Mn = [[sp.nsimplify(e.subs(sub)) for e in row] for row in WBs]
        rho = max(rho, len(sp.Matrix(Mn).rref()[1]))
    if rho + 1 > nc or rho + 1 > nr:
        return dict(rho=rho, n_minor=0, note="子式不存在 (rho+1>min(nr,nc))")
    ps = []
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            d = sp.expand(sp.Matrix([[MBs[i][j] for j in cj] for i in ri]).det())
            if d != 0 and d not in ps:
                ps.append(d)
    if not ps:
        return dict(rho=rho, n_minor=0, note="子式全零 (空洞)")
    try:
        if HAVE:
            signal.alarm(tmo)
        G = sp.groebner(ps, *th, order='lex')
        if HAVE:
            signal.alarm(0)
    except TO:
        return dict(rho=rho, n_minor=len(ps), note="Groebner 超时")
    except Exception as e:
        return dict(rho=rho, n_minor=len(ps), note="Groebner 失败: %s" % e)
    ex = [g for g in G.exprs if g != 0]
    pure = {}
    for v in th:
        found = None
        for g in ex:
            P = sp.Poly(g, *th)
            others = [w for w in th if w != v]
            if all(P.degree(w) == 0 for w in others) and P.degree(v) > 0:
                found = P.degree(v); break
        pure[v] = found
    lacks = [v for v in th if pure[v] is None]
    return dict(rho=rho, n_minor=len(ps), n_gb=len(ex),
                degs=sorted({sp.Poly(g, *th).total_degree() for g in ex}),
                lacks=len(lacks), dim_at_most=len(lacks))


def main():
    print("=== 方向 2 (修正装置): 真实 A 下 Omega*_J 的维数 ===\n")
    for (n, want_s, seed0) in [(6, 4, 30100000), (7, 5, 30200000), (6, 3, 30300000)]:
        print("--- n=%d, s=%d (支 B) ---" % (n, want_s))
        got = 0
        for t in range(4):
            inst = get_real(n, want_s, seed0 + t)
            if inst is None:
                continue
            res = analyze(inst)
            got += 1
            print("   q0=%d k=%d dC=%d : rho=%d 子式=%d ; %s"
                  % (inst['q0'], inst['k'], inst['dC'], res['rho'], res['n_minor'],
                     res.get('note', '基 %d 元 次数 %s ; 无纯幂变量=%d (dim<=%d)'
                             % (res['n_gb'], res['degs'], res['lacks'],
                                res['dim_at_most']))))
            if got >= 2:
                break
        print()
    print("【判读】")
    print("  · k=1 应给 '无纯幂变量=0' (dim=0) -- 与 history/30 一致")
    print("  · k>=2 若给 '无纯幂变量>0' ==> 高维")


if __name__ == "__main__":
    main()
