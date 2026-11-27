# -*- coding: utf-8 -*-
"""
b2_criterion2.py —— 引理 A 的正确判据（直接对 J）

【修正】
  上一条"δ ∈ row[W(0);B;W(0)Ā]"是**错的** ✗（θ-块秩恒为 1，判据 0/12）
  正确的判据就是 J 本身的秩：J = 线性部分的系数矩阵，rank(J) = m ?

  并且顺便验证：J 的秩是否 = "dim T_0 Ω*"（切空间维数，用 b1 的方法独立算）
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


def det_of(M):
    n = len(M)
    if n == 0: return Fr(1)
    A = [row[:] for row in M]; d = Fr(1)
    for c in range(n):
        piv = None
        for i in range(c, n):
            if A[i][c] != 0: piv = i; break
        if piv is None: return Fr(0)
        if piv != c: A[c], A[piv] = A[piv], A[c]; d = -d
        d *= A[c][c]; inv = Fr(1) / A[c][c]
        for i in range(c + 1, n):
            f = A[i][c] * inv
            if f: A[i] = [A[i][j] - f * A[c][j] for j in range(n)]
    return d


def main():
    print("=== 引理 A 的正确判据：rank(J) = m （并对照切空间维数）===")
    print("%-14s %3s %8s %8s %10s" % ("(k,s)", "m", "#线性子式", "rank(J)", "=m?"))
    print("-" * 50)
    ok = tot = 0
    for ss, n in [(3, 5), (4, 6), (5, 7)]:
        for t in range(3):
            inst = get_instance(n, ss, 20380000 + 100 * ss + t)
            if inst is None: continue
            dC, s, AT, BAT = inst["dC"], inst["s"], inst["AT"], inst["BAT"]
            r, k = 1, 1; m = s - 1
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
            for _ in range(30):
                sub = {th[i]: sp.Rational(random.randint(-5, 5), random.choice([1, 2, 3])) for i in range(m)}
                Wn = [[sp.nsimplify(e.subs(sub)) for e in row] for row in WBs]
                rho = max(rho, len(sp.Matrix(Wn).rref()[1]))
            lin = []
            for ri in itertools.combinations(range(nr), rho + 1):
                for cj in itertools.combinations(range(nc), rho + 1):
                    d = sp.expand(sp.Matrix([[MBs[i][j] for j in cj] for i in ri]).det())
                    if d == 0: continue
                    if sp.Poly(d, *th).total_degree() <= 1:
                        lin.append([sp.nsimplify(sp.Poly(d, *th).coeff_monomial(v)) for v in th])
            J = sp.Matrix(lin) if lin else sp.Matrix([[0] * m])
            rj = J.rank()
            good = (rj == m)
            tot += 1; ok += 1 if good else 0
            print("%-14s %3d %8d %8d %10s" % ("(1,%d)#%d" % (ss, t), m, len(lin), rj, good))
        print()
    print("⟹ rank(J) = m : %d/%d" % (ok, tot))
    print()
    print("【注】上一条'θ-列块'判据（b2_criterion.py）**不成立**（0/12）——")
    print("      因为 δ 不必落在 row[W(0);B;W(0)Ā] 中 ✗。正确的对象就是 J 本身。")


if __name__ == "__main__":
    main()
