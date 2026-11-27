# -*- coding: utf-8 -*-
"""
routeC_solve.py -- **精确**检验 LAN = LN·X 可解（逐列求解，含残差校验）

⚠️ 上一版用 "rk[LN|LAN] == rk[LN]" 作为判据 —— 那**只是** range 包含，
   而 range 包含 **不** 蕴含可分解（见反例 H=diag(1,0), T=diag(0,1)）✗
   本脚本用**线性方程组求解**（精确、带残差）作判据 ✓
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
    """检验是否存在 X 使 Hm·X = Tm（逐列求解 + 残差校验）"""
    if not Hm or not Hm[0]:
        return all(all(x == 0 for x in col) for col in Tm)
    nrow = len(Hm); ncol = len(Hm[0])
    X = []
    for j in range(len(Tm[0])):
        b = [[Tm[i][j]] for i in range(nrow)]
        res = solve_exact(Hm, b)
        if res is None:
            return False
        y = res[0] if isinstance(res, tuple) else res
        # 残差校验
        for i in range(nrow):
            s = sum(Hm[i][k] * y[k] for k in range(ncol))
            if s != b[i][0]:
                return False
        X.append(y)
    return True


def main():
    print("=== 路 C：**精确**检验 LAN = LN·X 可解 ===\n")
    print("%-10s %12s %8s %8s %10s" % ("trial", "A(ker)⊆ker?", "rk[LN]", "rk[LAN]", "可解?"))
    print("-" * 58)
    rng = random.Random(998877)
    ninv_ok = ninv_tot = inv_ok = inv_tot = 0
    shown = 0; bad = 0
    for trial in range(300000):
        if shown >= 16: break
        n, p, r = 6, 1, 1
        Ac = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        W = Cc + mm(Cc, Ac)
        NK = ker_basis(W)
        if not NK or not NK[0]: continue
        dK = len(NK[0])
        coeff = [F(rng.randint(-1, 1)) for _ in range(dK)]
        if all(c == 0 for c in coeff): continue
        v = [sum(NK[i][j] * coeff[j] for j in range(dK)) for i in range(n)]
        if all(x == 0 for x in v): continue
        Av = [sum(Ac[i][j] * v[j] for j in range(n)) for i in range(n)]
        inv = all(sum(W[i][j] * Av[j] for j in range(n)) == 0 for i in range(len(W)))
        N = [[v[i]] for i in range(n)]
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
        if not good: bad += 1
        if inv:
            inv_tot += 1; inv_ok += 1 if good else 0
        else:
            ninv_tot += 1; ninv_ok += 1 if good else 0
        print("%-10s %12s %8d %8d %10s"
              % ("t=%d" % trial, "是" if inv else "否", rk(LN), rk(LAN),
                 "✓" if good else "**✗ 反例**"))
    print()
    print("A-不变：  %d/%d 可解" % (inv_ok, inv_tot))
    print("非不变：  %d/%d 可解" % (ninv_ok, ninv_tot))
    print()
    if bad:
        print("⟹ **存在不可解的反例** ⟹ 引理需要额外条件（如 A-不变）✗")
    else:
        print("⟹ 全部可解 ⟹ (A) ∧ CN=0 ∧ CAN=0 ⟹ 存在 Λ 使 F = ΛH ✓")


if __name__ == "__main__":
    main()
