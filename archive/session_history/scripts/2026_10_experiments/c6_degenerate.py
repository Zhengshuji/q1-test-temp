# -*- coding: utf-8 -*-
"""
c6_degenerate.py -- ⭐ 决定性检查：项目的"真平行"实例是否**退化**（pi(L0)=0）？

【理论推论（r=1）】
  真平行 ⟺ pi(L0A) = c·pi(L0)（pi(v) = v·N_CA）
  ⟹ (L0A − cL0) 在 ker[C;CA] 上为 0
  ⟹ (L0A − cL0) ∈ row[C;CA]（因 row[C;CA] = ker[C;CA]^⊥）
  ⟹ L0A ∈ c·L0 + row[C;CA] ⊆ span{L0} + row[C;CA]
  ⟹ **L0 本身满足 (A)** ⟹ q0 = r = 1 ⟹ k = 0

  但若 pi(L0) = 0（**退化**），则"平行"判据被脚本**强制设为真**（见 verify_T12.py 的 pL0_zero 分支）
  ⟹ 这些实例的"真平行"是**退化的**，k 可以 ≥ 1

【本脚本】直接检查项目实例
"""
import os, io, contextlib, random
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]

_t = {}
with open(os.path.join(_HERE, "test_caseII_YES.py"), encoding="utf-8") as fh:
    src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src.split("rng = random.Random")[0], "t", "exec"), _t)
p1 = _t["p1"]


def matpow(M, k):
    n = len(M)
    R = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = mm(R, M)
    return R


def main():
    print("=== 项目的\"真平行\"实例是否退化？ ===\n")
    print("%-8s %4s %4s %4s %10s %12s %14s" %
          ("trial", "n", "q0", "k", "pi(L0)=0?", "L0 满足(A)?", "真平行(非退化?)"))
    print("-" * 70)
    rng = random.Random(555777)
    tot = 0
    deg = 0
    nondeg = 0
    nondeg_k0 = 0
    for trial in range(400000):
        if tot >= 16: break
        n, p = 6, 1
        r = 1
        Ac = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        mp = rng.randint(1, 3)
        L0 = mm(Cc, matpow(Ac, mp))
        if rk(L0) != r: continue
        if rk(L0 + Cc) != r + p: continue
        W = Cc + mm(Cc, Ac)
        N = ker_basis(W)
        if not N or not N[0]: continue
        d = len(N[0])
        pv = lambda v: [sum(v[i] * N[i][j] for i in range(n)) for j in range(d)]
        pL0 = pv(L0[0]); pL0A = pv(mm(L0, Ac)[0])
        pi0 = all(x == 0 for x in pL0)
        if pi0:
            par = True          # 脚本把 pi(L0)=0 当作"平行"
        else:
            par = (rk([pL0, pL0A]) == 1)
        if not par: continue
        # L0 本身是否满足 (A)？
        A_for_L0 = (rk(mm(L0, Ac) + L0 + W) == rk(L0 + W))
        try:
            _Lx, eta = p1(Ac, Cc, L0)
        except Exception:
            continue
        if not eta: continue
        q0 = sum(eta); k = q0 - r
        tot += 1
        if pi0: deg += 1
        else:
            nondeg += 1
            if k == 0: nondeg_k0 += 1
        print("%-8d %4d %4d %4d %10s %12s %14s" %
              (trial, n, q0, k, "**是**" if pi0 else "否",
               "是" if A_for_L0 else "**否**",
               "退化" if pi0 else ("非退化(k=0)" if k == 0 else "**非退化(k>=1)**")))
    print()
    print("总实例：%d   退化(pi(L0)=0)：%d   非退化：%d" % (tot, deg, nondeg))
    print("其中非退化且 k=0：%d" % nondeg_k0)
    print()
    if nondeg > 0 and nondeg == nondeg_k0:
        print("⟹ **理论预测成立**：非退化平行 ⟹ k=0（L0 本身满足 (A)）✓")
        print("   ⟹ 项目报的 k>=1 平行实例全部是**退化**的 ⚠️")
    elif nondeg == 0:
        print("⟹ 采到的平行实例**全部退化** ⚠️")
        print("   ⟹ c6′ 的实证基础只覆盖退化分支 ⚠️")
    else:
        print("⟹ **存在非退化且 k>=1 的平行实例** —— 理论推论有误，需检查")


if __name__ == "__main__":
    main()
