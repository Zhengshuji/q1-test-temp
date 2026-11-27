# -*- coding: utf-8 -*-
"""
routeC_kernel.py -- 路 C 的**真正条件**：ker(LN) ⊆ ker(LAN) ?

【为什么这是真正的条件】
   LAN = Λ∘LN 有解 ⟺ ker(LN) ⊆ ker(LAN)（有限维线性代数）
   而 range(LAN) ⊆ range(LN) 只是**必要**条件 ✗

【本脚本】在项目真实装置 + (A) 下，精确检验 ker 条件。
"""
import os, io, contextlib, random
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]


def main():
    print("=== 路 C：ker(LN) ⊆ ker(LAN) 的检验 ===\n")
    print("%-10s %9s %8s %8s %10s %10s" %
          ("trial", "A-不变?", "rk[LN]", "rk[LAN]", "ker条件", "range条件"))
    print("-" * 62)
    rng = random.Random(777888)
    shown = 0
    kbad = kbad_inv = kbad_ninv = 0
    for trial in range(300000):
        if shown >= 16: break
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
        # range 条件：列拼接  rk[LN | LAN] == rk(LN)
        rcond = (rk(LN + LAN) == rk(LN))          # LN+LAN 是行堆叠；这里只用来看维度
        # 列拼接（用于 range 条件）
        dLN = len(LN[0])
        coljoin = [[LN[i][j] for j in range(dLN)] + [LAN[i][j] for j in range(dLN)]
                   for i in range(len(LN))]
        rcond = (rk(coljoin) == rk(LN))
        # kernel 条件：ker(LN) ⊆ ker(LAN) ⟺ 行堆叠 rk[LN ; LAN] == rk(LN)
        rowstack = [LN[i][:] for i in range(len(LN))] + \
                   [LAN[i][:] for i in range(len(LAN))]
        kcond = (rk(rowstack) == rk(LN))
        shown += 1
        if not kcond:
            kbad += 1
            if inv: kbad_inv += 1
            else: kbad_ninv += 1
        print("%-10s %9s %8d %8d %10s %10s"
              % ("t=%d" % trial, "是" if inv else "否", rk(LN), rk(LAN),
                 "✓" if kcond else "**✗**", "✓" if rcond else "✗"))
    print()
    print("ker 条件失败：%d 个（其中 A-不变 %d、非不变 %d）" % (kbad, kbad_inv, kbad_ninv))
    print()
    if kbad == 0:
        print("⟹ **ker 条件全部成立** ⟹ 路 C 引理成立 ✓")
    else:
        print("⟹ **ker 条件有失败** ⟹ 路 C 引理需要额外假设 ✗")
        print("   注意：行堆叠 rk([LN;LAN])==rk(LN) 是 ker 条件的判据")


if __name__ == "__main__":
    main()
