# -*- coding: utf-8 -*-
"""
b1_check_contradiction.py —— 查清矛盾：切空间说"孤立点"，扰动说"正维数"

做法：固定实例（与 b1_dim_omega.py 相同），在 Θ₀=(0,0) 附近**精细网格**上
逐点检验 (A)，把命中点**打印出来**，直接看几何形状。
"""
import os, io, contextlib, random
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]

import linalg_q as Q

_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split("rng = random.Random")[0], "t", "exec"), _t)
build_norm_T = _t["build_norm_T"]; p1 = _t["p1"]


def WJ(t, r, k, s, dC):
    W = [[F(1) if j == i else F(0) for j in range(dC)] for i in range(r)]
    idx = 0
    for i in range(k):
        row = [F(0)] * dC; row[r + i] = F(1)
        for j in range(k, s):
            row[r + j] = t[idx]; idx += 1
        W.append(row)
    return W


def rho_and_A(t, r, k, s, dC, AT, BAT):
    W = WJ(t, r, k, s, dC)
    WB = W + BAT
    MB = WB + mm(W, AT)
    return rk(WB), rk(MB) == rk(WB)


def main():
    rng = random.Random(20260203)
    for trial in range(3000):
        n, p, r = 5, 1, 1
        for _ in range(30):
            Ac = Q.mat([[rng.randint(-1, 1) for _ in range(n)] for _ in range(n)])
            Cc = Q.mat([[rng.randint(-1, 1) for _ in range(n)] for _ in range(p)])
            Lc = Q.mat([[rng.randint(-1, 1) for _ in range(n)] for _ in range(r)])
            if Q.rank(Cc) != p or Q.rank(Lc) != r or Q.rank(Lc + Cc) != r + p: continue
            try: Lx, eta = p1(Ac, Cc, Lc)
            except Exception: continue
            if not Lx: continue
            q0 = sum(eta); k = q0 - r
            if k != 1: continue
            bt = build_norm_T(Ac, Cc, Lc, Lx)
            if bt is None: continue
            dC, s, k2, r2, AT, BAT = bt
            if (r2, k2) != (r, k) or s <= k: continue
            if 2*p+q0 >= n: continue
            rho0, ok0 = rho_and_A([F(0), F(0)], r, k, s, dC, AT, BAT)
            if not ok0: continue
            print("实例 n=%d p=%d r=%d q0=%d k=%d s=%d   Θ₀=(0,0) 是 (A)-点 ✓"
                  % (n, p, r, q0, k, s))
            print("ρ(Θ₀) = rk[W(Θ₀);B] = %d ;  [W;B] 的行数 = %d, 列数 = %d"
                  % (rho0, len(WJ([F(0),F(0)], r,k,s,dC)) + len(BAT),
                     len((WJ([F(0),F(0)], r,k,s,dC))[0])))
            print()
            # 精细网格：分母 8，范围 [-2,2]
            print("精细网格（步长 1/8，范围 ±1/2）—— 命中点标 *：")
            den = 8
            hits = []
            for ai in range(-4, 5):
                line = ""
                for bi in range(-4, 5):
                    t = [F(ai, den), F(bi, den)]
                    _, ok = rho_and_A(t, r, k, s, dC, AT, BAT)
                    line += ("*" if ok else ".")
                    if ok: hits.append((F(ai, den), F(bi, den)))
                print("   Θ[0]=%5s | %s" % (str(F(ai, den)), line))
            print("   命中 %d / 81" % len(hits))
            if hits:
                print("   命中点：", [[str(x) for x in q] for q in hits])
            # 更细：沿若干方向扫描
            print("\n沿若干方向的扫描（t 从 -1/2 到 1/2，步长 1/16）：")
            for (dx, dy) in [(1,0),(0,1),(1,1),(1,-1),(2,1),(1,2)]:
                seq = ""
                for vi in range(-8, 9):
                    t = [F(vi*dx, 16), F(vi*dy, 16)]
                    _, ok = rho_and_A(t, r, k, s, dC, AT, BAT)
                    seq += ("*" if ok else ".")
                print("   方向 (%-2d,%2d): %s" % (dx, dy, seq))
            return
    print("未找到实例")


if __name__ == "__main__":
    main()
