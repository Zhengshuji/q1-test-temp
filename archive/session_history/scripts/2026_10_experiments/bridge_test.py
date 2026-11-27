# -*- coding: utf-8 -*-
"""
bridge_test.py -- D3 桥接的决定性检验

【问题】(A)（行空间条件）是否蕴含 ker(L) ⊆ ker(L A)？

【为什么关键】
  若 ker L ⊆ ker(LA)，则由"因子化引理"（ker H ⊆ ker T ⟹ ∃Λ, T = Λ∘H）
      LA - G0 C - G1 CA = Λ∘L
  ⟹ 立刻得到分解 LA = ΛL + G0 C + G1 CA ✓ —— 桥接变得干净 ✓

【判据】ker(L) ⊆ ker(LA) ⟺ rk([L ; LA]) == rk(L)   （**行堆叠**！）
"""
import os, io, contextlib, random
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]


def condA(L, A, W):
    """(A)：rk(LA + L + W) == rk(L + W)（行空间条件）"""
    return rk(mm(L, A) + L + W) == rk(L + W)


def main():
    print("=== (A) ⟹ ker(L) ⊆ ker(LA) ? ===\n")
    print("%-8s %4s %4s %5s %5s | %10s %10s" %
          ("trial", "n", "q0", "rk(L)", "rk(LA)", "ker⊆?", "rk([L;LA])"))
    print("-" * 62)
    rng = random.Random(24681357)
    ok = bad = tot = 0
    bad_examples = []
    for trial in range(400000):
        if tot >= 16: break
        n, p, r = rng.choice([(5, 1, 1), (6, 1, 1), (6, 1, 2), (6, 2, 1)])
        Ac = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        if rk(Cc) != p: continue
        W = Cc + mm(Cc, Ac)
        # 随意取 q0 行的 L（含 L0 = C A^m 那类）
        q0 = r + 1
        Lc = [[F(rng.randint(-2, 2)) for _ in range(n)] for _ in range(q0)]
        if rk(Lc) != q0: continue
        if not condA(Lc, Ac, W): continue
        LA = mm(Lc, Ac)
        # ker(L) ⊆ ker(LA) ⟺ rk([L;LA]) == rk(L)
        rowstack = [row[:] for row in Lc] + [row[:] for row in LA]
        ksub = (rk(rowstack) == rk(Lc))
        tot += 1
        if ksub: ok += 1
        else:
            bad += 1
            if len(bad_examples) < 2:
                bad_examples.append((Ac, Cc, Lc))
        print("%-8d %4d %4d %5d %5d | %10s %10d"
              % (trial, n, q0, rk(Lc), rk(LA),
                 "✓" if ksub else "**✗**", rk(rowstack)))
    print()
    print("⟹ ker(L) ⊆ ker(LA) 成立：%d/%d" % (ok, tot))
    if bad:
        print("⟹ **有 %d 个反例** ⟹ (A) 不蕴含 ker 包含关系 ✗" % bad)
        print("   ⟹ 桥接需要真正的因子化（不能靠 ker L ⊆ ker LA）")
        # 打印一个反例
        if bad_examples:
            A, C, L = bad_examples[0]
            print()
            print("【反例】")
            print("  A =", [[str(x) for x in row] for row in A])
            print("  C =", [[str(x) for x in row] for row in C])
            print("  L =", [[str(x) for x in row] for row in L])
            W = C + mm(C, A)
            print("  (A) 成立？", condA(L, A, W))
            print("  rk(L)=%d  rk([L;LA])=%d  ⟹ ker(L) ⊄ ker(LA)"
                  % (rk(L), rk([row[:] for row in L] + [row[:] for row in mm(L, A)])))
    else:
        print("⟹ **(A) ⟹ ker(L) ⊆ ker(LA) 成立** ⟹ 桥接可用因子化引理 ✓")


if __name__ == "__main__":
    main()
