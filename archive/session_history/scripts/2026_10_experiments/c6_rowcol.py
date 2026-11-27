# -*- coding: utf-8 -*-
"""
c6_rowcol.py -- ⚠️ 险情追查：**(5a) 给的是"行空间"包含，还是"列空间"包含？**

【我一度（错误地）认为】
  (5a) ⟹ π(ℓA) ∈ span{π(ℓ')} =: 某空间
  而 "π(ℓ) = ℓ N_CA = H 的第 i 行"
  ⟹ 该空间 = H 的**行空间**
  我误当成 im H（= H 的**列空间**）⟹ 得出"im F ⊆ im H" ⟹ 无条件 c6′ ✗✗

【若真是无条件成立，就与 history/47 的见证矛盾】⟹ 必有错

【本脚本】直接数值判定：在见证实例与退化实例上
   (α) 行空间：rowspace(F) ⊆ rowspace(H) ？（应**总是**成立 —— 因 ΛH=F 自动）
   (β) 列空间：im(F) ⊆ im(H) ？（**不**总成立 —— 见证实例上应失败）
"""
import os, io, contextlib, random, json
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


def rowspace_le(H, Fm):
    """rowspace(F) ⊆ rowspace(H)？（**行堆叠**判据）"""
    return rk([r[:] for r in H] + [r[:] for r in Fm]) == rk(H)


def colspace_le(H, Fm):
    """colspace(F) ⊆ colspace(H)？（**列拼接**判据）"""
    dH = len(H[0]); dF = len(Fm[0])
    cj = [[H[i][j] for j in range(dH)] + [Fm[i][j] for j in range(dF)]
          for i in range(len(H))]
    return rk(cj) == rk(H)


def main():
    print("=== 险情追查：行空间 vs 列空间 ===\n")
    # 1) 见证实例
    with open(os.path.join(_HERE, "witness_caseII_parallel_YES.json"), encoding="utf-8") as f:
        w = json.load(f)
    A = [[F(x) for x in r] for r in w["A"]]
    C = [[F(x) for x in r] for r in w["C"]]
    L = [[F(x) for x in r] for r in w["L0"]]
    n = w["n"]
    W = C + mm(C, A)
    N = ker_basis(W)
    H = mm(L, N); Fm = mm(mm(L, A), N)
    print("--- 见证实例（history/47）---")
    print("  rowspace(F) ⊆ rowspace(H) ？ %s" % ("✓" if rowspace_le(H, Fm) else "✗"))
    print("  colspace(F) ⊆ colspace(H) ？ %s  ← **这就是机制所需的条件**"
          % ("✓" if colspace_le(H, Fm) else "**✗**"))
    print("  rk(H)=%d  rk(F)=%d  rk[H|F] (列拼接)=%d  rk[H;F] (行堆叠)=%d"
          % (rk(H), rk(Fm),
             rk([[H[i][j] for j in range(len(H[0]))] +
                 [Fm[i][j] for j in range(len(Fm[0]))] for i in range(len(H))]),
             rk([r[:] for r in H] + [r[:] for r in Fm])))
    print()

    # 2) 退化族（CA^2=0）——已知 (S) 失败
    print("--- 退化 + 不变族（CA²=0，项目 14/14 的类型）---")
    rng = random.Random(31415)
    cnt = 0
    while cnt < 4:
        Ac = [[F(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        if mm(Ac, Ac) != [[F(0)] * n for _ in range(n)]:
            continue
        Cc = [[F(rng.randint(-1, 1)) for _ in range(n)]]
        if rk(Cc) != 1: continue
        L0 = mm(Cc, Ac)
        if rk(L0) != 1 or rk(L0 + Cc) != 2: continue
        W2 = Cc + mm(Cc, Ac)
        N2 = ker_basis(W2)
        if not N2 or not N2[0]: continue
        try:
            _Lx, eta = p1(Ac, Cc, L0)
        except Exception:
            continue
        if not eta: continue
        q0 = sum(eta); k = q0 - 1
        if k < 1: continue
        # 找 (A)∧T5a
        hit = None
        for _ in range(300):
            rows = [r[:] for r in L0]
            for _i in range(k):
                rows.append([F(rng.randint(-3, 3)) for _ in range(n)])
            if rk(mm(rows, Ac) + rows + W2) != rk(rows + W2): continue
            if rk(mm(rows, N2)) < q0: hit = rows; break
        if hit is None: continue
        H2 = mm(hit, N2); F2 = mm(mm(hit, Ac), N2)
        if rk(H2) == 0: continue
        cnt += 1
        print("  #%d: rowspace✓=%s  colspace=%s   rkH=%d rkF=%d"
              % (cnt, "✓" if rowspace_le(H2, F2) else "✗",
                 "✓" if colspace_le(H2, F2) else "✗", rk(H2), rk(F2)))
    print()
    print("【判读】")
    print("  rowspace 包含 ⟸ 由 ΛH=F **自动成立**（无信息）")
    print("  colspace 包含 ⟸ **这才是** im F ⊆ im H（机制所需）")
    print("  见证实例上 colspace 应 **失败**（否则矛盾）")
    print("  退化+不变族上 colspace 应 **成立**（F=H∘A'）")


if __name__ == "__main__":
    main()
