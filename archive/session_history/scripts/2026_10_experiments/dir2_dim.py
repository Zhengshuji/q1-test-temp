# -*- coding: utf-8 -*-
"""
dir2_dim.py -- 方向 2: 用**可靠的维数判据**测定 Omega*_J 的维数

【为什么换判据】
  上一版用"Groebner 基的高次元涉及几个变量"作为 dim 上界 -- **不可靠** ✗
  (变量数 != 维数; 例如 xy=0 涉及 2 个变量但维数是 1)

【可靠判据】
  理想 I 的维数 = 0  <=>  对每个变量 t_j, 饱和化 I : (t_j^inf) 含 1
  更实用: 用 Groebner 基做**试根/维数估计**:
     - dim I = 0  <=> 每个变量有纯幂在首项理想中
     - 否则用"按变量分层": 逐变量看是否可以"消去"

【本脚本】用最实用的判据: 
   对每个变量, 检查理想中是否存在**只含该变量**的多项式 (纯幂)
   dim=0 <=> 全部变量都有纯幂
   若非零维, 报告"哪些变量没有纯幂"(= 自由方向)
"""
import os, io, contextlib, itertools, random, signal
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]

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


def build(AT, BAT, r, k, s, dC, th):
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
    return WBs, MBs


def A_polys(MBs, rho):
    nr, nc = len(MBs), len(MBs[0])
    if rho + 1 > nc or rho + 1 > nr:
        return []
    out = []
    for ri in itertools.combinations(range(nr), rho + 1):
        for cj in itertools.combinations(range(nc), rho + 1):
            d = sp.expand(sp.Matrix([[MBs[i][j] for j in cj] for i in ri]).det())
            if d != 0:
                out.append(d)
    return out


def pure_powers(ps, th):
    """返回: {变量: 是否存在只含该变量的非零多项式}; 用 Groebner 基的纯幂检测"""
    G = sp.groebner(ps, *th, order='lex')
    ex = [g for g in G.exprs if g != 0]
    res = {}
    for v in th:
        found = None
        for g in ex:
            P = sp.Poly(g, *th)
            others = [w for w in th if w != v]
            if all(P.degree(w) == 0 for w in others) and P.degree(v) > 0:
                found = P.degree(v)
                break
        res[v] = found
    return res, ex


def main():
    print("=== 方向 2: Omega*_J 的可靠维数判据 ===\n")
    rng = random.Random(83)
    for (r, k, s, dC, ni) in [(1, 2, 4, 6, 4), (1, 2, 5, 6, 3),
                              (1, 3, 5, 7, 3), (1, 1, 4, 5, 3)]:
        m = k * (s - k)
        th = sp.symbols('t0:%d' % m)
        print("--- (r=%d,k=%d,s=%d,dC=%d) m=%d ---" % (r, k, s, dC, m))
        got = 0
        for trial in range(ni):
            AT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(dC)]
            BAT = [[F(rng.randint(-1, 1)) for _ in range(dC)] for _ in range(k)]
            WBs, MBs = build(AT, BAT, r, k, s, dC, th)
            rho = 0
            for _ in range(6):
                sub = {th[i]: sp.Rational(rng.randint(-3, 3)) for i in range(m)}
                Mn = [[sp.nsimplify(e.subs(sub)) for e in row] for row in WBs]
                rho = max(rho, len(sp.Matrix(Mn).rref()[1]))
            ps = A_polys(MBs, rho)
            if not ps:
                continue
            try:
                if HAVE:
                    signal.alarm(20)
                pp, ex = pure_powers(ps, th)
                if HAVE:
                    signal.alarm(0)
            except TO:
                print("   实例 #%d: 超时" % trial); continue
            except Exception as e:
                print("   实例 #%d: 失败 %s" % (trial, e)); continue
            lacks = [v for v in th if pp[v] is None]
            got += 1
            print("   实例 #%d: rho=%d 子式 %d; 基 %d 元" % (trial, rho, len(ps), len(ex)))
            print("      有纯幂的变量 %s" % sorted(str(v) for v in th if pp[v] is not None))
            print("      **无纯幂**的变量 %s  ==> dim >= %d"
                  % (sorted(str(v) for v in lacks), len(lacks)))
            if got >= 2:
                break
        print()
    print("【判读】")
    print("  - 若无纯幂变量数 == 0 ==> dim Omega*_J = 0 (有限/孤立)")
    print("  - 若无纯幂变量数 > 0  ==> 正维数; 该数给出维数的**上界**")
    print("  - 关键: 看它是否随 NONE")


if __name__ == "__main__":
    main()
