# -*- coding: utf-8 -*-
"""
routeC_final2.py -- 路 C 引理的**最终判定**

【精确条件】LAN = Λ∘LN 有解  ⟺  ker(LN) ⊆ ker(LAN)  ⟺  线性系统 LN·X = LAN 可解

【需要的前提（推导得到的）】
   (A)  +  C N = 0  +  C A N = 0  +  **A(ker[C;CA]) ⊆ ker[C;CA] + ker L**
   最后一条是真正的必要条件（而非"A-不变"）。

【本脚本】用项目真实装置 (N = ker[C;CA]) 精确检验。
"""
import os, io, contextlib, random
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]

_lx = {}
with open(os.path.join(_HERE, "linalg_exact.py"), encoding="utf-8") as fh:
    exec(compile(fh.read(), "lx", "exec"), _lx)
solve_exact = _lx["solve_exact"]


def solvable(Hm, Tm):
    if not Hm or not Hm[0]:
        return all(all(x == 0 for x in c) for c in Tm)
    nrow = len(Hm); ncol = len(Hm[0])
    for j in range(len(Tm[0])):
        b = [[Tm[i][j]] for i in range(nrow)]
        res = solve_exact(Hm, b)
        if res is None: return False
        y = res[0] if isinstance(res, tuple) else res
        for i in range(nrow):
            if sum(Hm[i][k] * y[k] for k in range(ncol)) != b[i][0]:
                return False
    return True


def main():
    print("=== 路 C 引理的最终判定（项目真实装置）===\n")
    print("%-10s %9s %8s %8s %11s" % ("trial", "A-不变?", "rk[LN]", "rk[LAN]", "可因子化?"))
    print("-" * 56)
    rng = random.Random(555666)
    inv_ok = inv_tot = ninv_ok = ninv_tot = 0
    shown = 0
    for trial in range(300000):
        if shown >= 18: break
        n, p, r = 6, 1, 1
        Ac = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        W = Cc + mm(Cc, Ac)
        N = ker_basis(W)
        if not N or not N[0]: continue
        AN = mm(Ac, N)
        inv = (rk(N + AN) == rk(N))
        L = None
        for _ in range(100):
            Lc = [[F(rng.randint(-2, 2)) for _ in range(n)] for _ in range(r + 1)]
            if rk(mm(Lc, Ac) + Lc + W) == rk(Lc + W):
                L = Lc; break
        if L is None: continue
        LN = mm(L, N); LAN = mm(mm(L, Ac), N)
        if rk(LN) == 0: continue
        good = solvable(LN, LAN)
        shown += 1
        if inv:
            inv_tot += 1; inv_ok += 1 if good else 0
        else:
            ninv_tot += 1; ninv_ok += 1 if good else 0
        print("%-10s %9s %8d %8d %11s"
              % ("t=%d" % trial, "是" if inv else "否", rk(LN), rk(LAN),
                 "✓" if good else "**✗**"))
    print()
    print("A-不変：  %d/%d 可因子化" % (inv_ok, inv_tot))
    print("非不变：  %d/%d 可因子化" % (ninv_ok, ninv_tot))
    print()
    if inv_tot == inv_ok and inv_tot:
        print("⟹ **A-不变时全部可因子化** ✓ ⟹ 路 C 的引理在 A-不变下成立")
    if ninv_tot > ninv_ok:
        print("⟹ 非 A-不变时有反例 ⟹ 引理**需要** A-不变（或等价条件）")


if __name__ == "__main__":
    main()
