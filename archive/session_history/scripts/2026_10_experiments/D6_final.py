# -*- coding: utf-8 -*-
"""
D6_final.py -- D6：用**生成器实例**检验各种候选公式

【候选】
  F1: q0 == dim(C + span{L0 A^k})，C = row[C;CA;...;CA^{n-1}]
  F2: q0 == dim(C + span{L0 A^k})，C = row[C;CA]（项目的 [C;CA]）
  F3: q0 == dim(span{L0 A^k})
"""
import os, io, contextlib, random
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
p1 = _t["p1"]


def obs_space(Ac, Cc, n):
    Csp = [r[:] for r in Cc]
    cur = [r[:] for r in Cc]
    for _ in range(n - 1):
        cur = mm(cur, Ac)
        Csp = Csp + cur
    return Csp


def orbit(Ac, Lc, n):
    rows = [r[:] for r in Lc]
    cur = [r[:] for r in Lc]
    for _ in range(n + 2):
        cur = mm(cur, Ac)
        newrows = rows + cur
        if rk(newrows) == rk(rows):
            break
        rows = newrows
    return rows


def main():
    print("=== D6：生成器实例上的候选公式 ===\n")
    print("%-6s %3s %3s %3s %4s %5s %6s %6s %6s" %
          ("#", "n", "p", "r", "q0", "C", "F1", "F2", "F3"))
    print("-" * 56)
    rng = random.Random(334455)
    f1ok = f2ok = f3ok = tot = 0
    for trial in range(300000):
        if tot >= 14: break
        n, p, r = rng.choice([(4,1,1), (5,1,1), (6,1,1), (5,1,2)])
        Ac = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        mp = rng.randint(1, 3)
        Lc = mm(Cc, Ac)
        for _ in range(mp - 1):
            Lc = mm(Lc, Ac)
        if rk(Lc) != r: continue
        if rk(Lc + Cc) != r + p: continue
        try:
            Lx, eta = p1(Ac, Cc, Lc)
        except Exception:
            continue
        if not Lx: continue
        q0 = sum(eta)
        rC2 = Cc + mm(Cc, Ac)              # [C;CA]
        rCfull = obs_space(Ac, Cc, n)
        orb = orbit(Ac, Lc, n)
        F1 = rk(orb + rCfull)
        F2 = rk(orb + rC2)
        F3 = rk(orb)
        tot += 1
        if F1 == q0: f1ok += 1
        if F2 == q0: f2ok += 1
        if F3 == q0: f3ok += 1
        print("%-6d %3d %3d %3d %4d %5d %6d %6d %6d"
              % (trial, n, p, r, q0, rk(rCfull), F1, F2, F3))
    print()
    print("F1（完整 C）: %d/%d" % (f1ok, tot))
    print("F2（[C;CA]）: %d/%d" % (f2ok, tot))
    print("F3（仅轨道）: %d/%d" % (f3ok, tot))
    print()
    print("【判读】哪个候选恒等于 q0，就是正确的显式公式")


if __name__ == "__main__":
    main()
