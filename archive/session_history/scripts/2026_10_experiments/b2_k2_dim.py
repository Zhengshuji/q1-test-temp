# -*- coding: utf-8 -*-
"""
b2_k2_dim.py —— 钉死 k=2 实例的 Ω*_J 结构（有限？正维数？）

用与 b1 相同的方法：
  ① 切空间维数（定义子式的梯度矩阵秩）
  ② 非零随机扰动命中率（**必须排除零扰动**！）
  ③ 沿各坐标轴的细扫描
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


def find_inst(n, p, r, mp, seed):
    rng = random.Random(seed)
    def mul(X, Y):
        return [[sum(X[i][a] * Y[a][j] for a in range(len(Y))) for j in range(len(Y[0]))]
                for i in range(len(X))]
    for _ in range(4000):
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
        bt = build_norm_T(Ac, Cc, P, Lx)
        if bt is None: continue
        dC, s, k2, r2, AT, BAT = bt
        if (r2, k2) != (r, k) or s <= k: continue
        return dict(n=n, p=p, r=r, q0=q0, k=k, s=s, dC=dC, AT=AT, BAT=BAT)
    return None


def main():
    print("=== k=2 的 Ω*_J 结构 ===")
    inst = None
    for seed in range(20):
        cand = find_inst(6, 1, 1, 2, 20400000 + seed)
        if cand is None: continue
        # ⚠️ 必须过滤**支 B**（2p+q0 < n）；支 A 上 (A) 可能整个空间都满足
        if 2 * cand['p'] + cand['q0'] < cand['n']:
            inst = cand; break
    if not inst:
        print("未找到 **支 B** 的 k>=2 实例（只有支 A 的——支 A 上 Ω* 可能是整个空间）")
        return
    n, p, r, k, s, dC = inst['n'], inst['p'], inst['r'], inst['k'], inst['s'], inst['dC']
    m = k * (s - k)
    print("实例 n=%d p=%d r=%d q0=%d k=%d s=%d dC=%d m=%d  支B? %s"
          % (n, p, r, inst['q0'], k, s, dC, m, 2*p+inst['q0'] < n))
    AT, BAT = inst['AT'], inst['BAT']

    def Wnum(theta):
        W = [[Fr(1) if j == i else Fr(0) for j in range(dC)] for i in range(r)]
        idx = 0
        for i in range(k):
            row = [Fr(0)] * dC
            row[r + i] = Fr(1)
            for j in range(k, s):
                row[r + j] = theta[idx]; idx += 1
            W.append(row)
        return W

    def isA(theta):
        W = Wnum(theta); WB = W + BAT
        return rk(WB + mm(W, AT)) == rk(WB)

    # 找一些 (A)-点（网格）
    base_pts = []
    for combo in itertools.product(range(-2, 3), repeat=m):
        if isA([Fr(x) for x in combo]):
            base_pts.append(combo)
    print("  整数格 (±2)^%d : (A)-点 %d 个 %s" % (m, len(base_pts), base_pts[:5]))
    if not base_pts:
        print("  网格上无 (A)-点（解可能非有理）")
    # ① 切空间维数
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
        sub = {th[i]: sp.Rational(random.randint(-3, 3), random.choice([1,2])) for i in range(m)}
        Wn = [[sp.nsimplify(e.subs(sub)) for e in row] for row in WBs]
        rho = max(rho, len(sp.Matrix(Wn).rref()[1]))
    polys = []
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            d = sp.expand(sp.Matrix([[MBs[i][j] for j in cj] for i in ri]).det())
            if d != 0 and d not in polys:
                polys.append(d)
    # ① 切空间维数（在某个 (A)-点处）
    if base_pts:
        pt = [Fr(x) for x in base_pts[0]]
        h = Fr(1, 1000)
        def det_of(Mm):
            nn = len(Mm)
            if nn == 0: return Fr(1)
            A = [r_[:] for r_ in Mm]; dd = Fr(1)
            for c in range(nn):
                piv = None
                for i2 in range(c, nn):
                    if A[i2][c] != 0: piv = i2; break
                if piv is None: return Fr(0)
                if piv != c: A[c], A[piv] = A[piv], A[c]; dd = -dd
                dd *= A[c][c]; iv = Fr(1)/A[c][c]
                for i2 in range(c+1, nn):
                    f = A[i2][c]*iv
                    if f: A[i2] = [A[i2][j2]-f*A[c][j2] for j2 in range(nn)]
            return dd
        def mval(t):
            Wt = Wnum(t); WBt = Wt + BAT
            return WBt + mm(Wt, AT), WBt
        # 用数值方式算梯度（有理数中心差分）
        def det_at(t, ri, cj):
            M_, _ = mval(t)
            return det_of([[M_[i2][j2] for j2 in cj] for i2 in ri])
        rows = []
        for ri in itertools.combinations(range(nr), rho + 1):
            for cj in itertools.combinations(range(nc), rho + 1):
                f0 = det_at(pt, ri, cj)
                if f0 != 0: continue   # 该子式在 pt 处已非零 ⟹ pt 不是精确 (A)-点
                grad = []
                for a in range(m):
                    tp = list(pt); tp[a] += h
                    tm = list(pt); tm[a] -= h
                    grad.append((det_at(tp, ri, cj) - det_at(tm, ri, cj)) / (2*h))
                if any(g != 0 for g in grad): rows.append(grad)
        dimT = (m - rk(rows)) if rows else m
        Mnum = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in rows]) if rows else None
        dimT = m - (Mnum.rank() if Mnum is not None else 0)
        print("  ① 切空间维数 dim T = %d （m = %d）⟹ %s"
              % (dimT, m, "孤立 ✓" if dimT == 0 else "**正维数** ✗"))
    # ② 非零随机扰动（排除零！）
    rng2 = random.Random(4242)
    if base_pts:
        pt = [Fr(x) for x in base_pts[0]]
        nz = 0; hit = 0
        for _ in range(2000):
            d = [Fr(rng2.randint(-1, 1), 512) for _ in range(m)]
            if all(x == 0 for x in d): continue
            nz += 1
            if isA([pt[i]+d[i] for i in range(m)]): hit += 1
        print("  ② 非零扰动 %d 次（步长 1/512）命中 %d" % (nz, hit))
    # ③ Groebner
    G = sp.groebner(polys, *th, order='lex')
    ex = list(G.exprs)
    print("  ③ Groebner 基（%d 个）：" % len(ex))
    for g in ex: print("       %s   [次数 %d]" % (g, sp.Poly(g, *th).total_degree()))
    print("  ④ 理想是否零维？ %s" %
          ("是" if all(any(sp.Poly(g, *th).degree(v) > 0 and
                          all(sp.Poly(g, *th).degree(w) == 0 for w in th if w != v)
                          for g in ex) for v in th) else "否（可能正维数）"))


if __name__ == "__main__":
    main()
