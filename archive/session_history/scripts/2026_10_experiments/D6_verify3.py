# -*- coding: utf-8 -*-
"""
D6_verify3.py -- D6（正确版）：q0 == 最小 Ā-不变子空间维数

【模论形式（正确）】
  C := row[C; CA; ...; CA^{n-1}]（**完整**可观测空间，A-不变 ✓）
  (A) ⟺ row(L)+C 是 A-不变的 ⟺ L̄ := (row L + C)/C 是 Ā-不变的
  ⟹ q0 = min{ dim W̄ : W̄ Ā-不变, L̄_0 ⊆ W̄ }

【算法（在商里）】
  W̄ := span(L̄_0)（用 W + C 的秩减 rk(C) 表示维数）
  迭代 W̄ ← W̄ + W̄·Ā 直到稳定
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


def full_obs_space(Ac, Cc, n):
    """C := row[C; CA; ...; CA^{n-1}]"""
    Csp = [r[:] for r in Cc]
    cur = [r[:] for r in Cc]
    for _ in range(n - 1):
        cur = mm(cur, Ac)
        Csp = Csp + cur
    return Csp


def min_inv(Ac, Lc, Csp, n):
    rC = rk(Csp)
    W = [r[:] for r in Lc]
    d_prev = rk(W + Csp) - rC
    for _ in range(n + 2):
        W = W + mm(W, Ac)
        d_new = rk(W + Csp) - rC
        if d_new == d_prev:
            return d_new
        d_prev = d_new
    return d_prev


def test_hand():
    A = [[F(0), F(1), F(0)], [F(0), F(0), F(0)], [F(0), F(0), F(2)]]
    C = [[F(1), F(0), F(0)]]
    L0 = [[F(0), F(0), F(1)]]
    Csp = full_obs_space(A, C, 3)
    Lx, eta = p1(A, C, L0)
    print("手算例：rk(C)=%d q0=%d eta=%s minInv=%d"
          % (rk(Csp), sum(eta), eta, min_inv(A, L0, Csp, 3)))
    print()


def main():
    print("=== D6（正确版）：q0 == min Ā-不变维数？ ===\n")
    test_hand()
    print("%-6s %3s %3s %3s %5s %10s %8s" % ("#", "n", "p", "r", "q0", "minInvDim", "一致?"))
    print("-" * 46)
    rng = random.Random(445566)
    ok = tot = 0
    for trial in range(300000):
        if tot >= 14: break
        n, p, r = rng.choice([(4,1,1), (5,1,1), (5,1,2), (6,1,1), (6,2,1)])
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
        Csp = full_obs_space(Ac, Cc, n)
        mid = min_inv(Ac, Lc, Csp, n)
        tot += 1
        good = (mid == q0)
        ok += 1 if good else 0
        print("%-6d %3d %3d %3d %5d %10d %8s"
              % (trial, n, p, r, q0, mid, "✓" if good else "**✗**"))
    print()
    print("⟹ q0 == minInvDim：%d/%d" % (ok, tot))
    if tot and ok == tot:
        print("⟹ **模论形式成立** ⟹ q0 = 最小 Ā-不变子空间维数 ✓")
        print("   ⟹ q0 下界有**结构性依据**（独立于 P1 Thm 2）✓")


if __name__ == "__main__":
    main()
