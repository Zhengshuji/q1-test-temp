# -*- coding: utf-8 -*-
"""
probe_caseII_YES_q2.py —— **决定性复核**：情形 II 下是否存在 (A) ∧ T5a ∧ (S) 同时成立的实例？

【为什么会怀疑它存在】
  取 L = [L0 ; l]，其中（由 §12/§13 的构造）
     (i)  l 满足几何条件：  im(AN) ⊆ ker l   即  l·A·N = 0
     (ii) [L0 ; l] 满足 (A)
  于是由 T5′（(A) ⟹ F = ΛH）得 F = ΛH ⟹ **F 的每一行都落在 H 的行空间里**。
  当 q0 = 2、rk H = 1 时（H 的两行仍张成 1 维），(S) ⟺ rk(λH−F)=rk H ∀λ
  就**自动成立**（F 的行与 H 的唯

一非零行线性相关）—— 与 λ 无关。

  ⟹ 若这样的 L 真的存在，则**情形 II 可为 YES** ⟹ 与你库里
     `reliable_S_test.py` 的「情形 II：(A)∧(S) = 0/200」**冲突** ⟹ 必须查清谁对。

【本脚本的复核方式（全部精确有理数）】
  ① 直接按**原始 4 块**判据查 (A)：rk[LA;L;C;CA] == rk[L;C;CA]
  ② 直接按**原始 (S)**：对若干 λ（含 λ=0 与随机的整数/有理数）
     查 rk[λL−LA;CA;C] == rk[L;CA;C]
  ③ 同时按**铅笔约化**形式查：rk(λH−F) == rk H，H=L·N_CA，F=LA·N_CA
  ④ 交叉验证 T5a：rk(L·N_CA) < q0
  三者互为独立判据（本项目铁律：等价性检验必含 True 点 ✓）。
"""
import os, io, contextlib
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
ker_basis = _ns["ker_basis"]

_ns2 = {}
with open(os.path.join(_HERE, "linalg_exact.py"), encoding="utf-8") as fh:
    exec(compile(fh.read(), "lx", "exec"), _ns2)
rank_exact, matmul = _ns2["rank_exact"], _ns2["matmul"]

_ns3 = {"__file__": os.path.join(_HERE, "batch_c6p_k.py")}
with open(os.path.join(_HERE, "batch_c6p_k.py"), encoding="utf-8") as fh:
    exec(compile(fh.read().split("def main()")[0], "helpers", "exec"), _ns3)
mat = _ns3["mat"]


def rows(M):
    return [r[:] for r in M]


def stack(*Ms):
    out = []
    for M in Ms:
        if not M:
            continue
        if out:
            assert len(out[0]) == len(M[0]), "stack 列数不一致"
        out += [r[:] for r in M]
    return out


def rk(M):
    return rank_exact(M)


def rankA(A, C, L):
    """原始 4 块 (A)"""
    CA = matmul(C, A)
    return rk(stack(matmul(L, A), L, C, CA)) == rk(stack(L, C, CA))


def rankS_direct(A, C, L, lams):
    """原始 (S)：rk[λL−LA;CA;C] == rk[L;CA;C] ∀λ"""
    CA = matmul(C, A)
    LA = matmul(L, A)
    base = rk(stack(L, CA, C))
    out = []
    for lam in lams:
        M = [[lam * L[i][j] - LA[i][j] for j in range(len(L[0]))] for i in range(len(L))]
        out.append((lam, rk(stack(M, CA, C)) == base, rk(stack(M, CA, C)), base))
    return out


def rankS_pencil(A, C, L, NCA, lams):
    """铅笔约化形式：rk(λH−F) == rk H"""
    H = matmul(L, NCA)
    Fm = matmul(matmul(L, A), NCA)
    rH = rk(H)
    out = []
    for lam in lams:
        M = [[lam * H[i][j] - Fm[i][j] for j in range(len(H[0]))] for i in range(len(H))]
        out.append((lam, rk(M) == rH, rk(M), rH))
    return out


def main():
    print("=== 情形 II 下 (A) ∧ T5a ∧ (S) 的精确复核 ===\n")
    A = mat([[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
    C = mat([[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0]])
    L0 = mat([[1, 0, 0, 0, 0, 0]])
    # 构造行：取自 §13 的几何构造（l∘A∘N = 0 且 l·N = e1*）
    l = mat([[1, 0, 0, 0, 0, 0]])[0]
    L = [L0[0][:], l]

    CA = matmul(C, A)
    R = stack(C, CA)
    NCA = ker_basis(R)
    n, p, r, q0 = len(A), len(C), len(L0), len(L)
    dCA = len(NCA[0]) if NCA and NCA[0] else 0
    print("n=%d  p=%d  r=%d  q0=%d  d_CA=%d  （情形 II ⟺ d_CA ≥ q0：%s）" %
          (n, p, r, q0, dCA, dCA >= q0))
    print("L = [L0; l] =", [[str(x) for x in row] for row in L])
    print()

    print("【① 原始 4 块 (A)】 rk[LA;L;C;CA] == rk[L;C;CA] ？", rankA(A, C, L))
    print("   rk(L·N_CA) = %d  < q0 = %d ？（T5a）%s" %
          (rk(matmul(L, NCA)), q0, rk(matmul(L, NCA)) < q0))
    print()

    lams = [F(k) for k in [0, 1, -1, 2, -2, 3, 5, 7]] + [F(1, 2), F(-3, 7), F(11, 5)]
    print("【② 原始 (S)】 rk[λL−LA;CA;C] == rk[L;CA;C]：")
    for lam, ok, a, b in rankS_direct(A, C, L, lams):
        print("    λ=%-6s  %-6s  rk=%d  base=%d" % (str(lam), "成立" if ok else "**失败**", a, b))
    print()

    print("【③ 铅笔约化 (S)：rk(λH−F) == rk H】")
    H = matmul(L, NCA)
    Fm = matmul(matmul(L, A), NCA)
    print("    H = L·N_CA =", [[str(x) for x in q] for q in H], " rk H =", rk(H))
    print("    F = LA·N_CA =", [[str(x) for x in q] for q in Fm], " rk F =", rk(Fm))
    for lam, ok, a, b in rankS_pencil(A, C, L, NCA, lams):
        print("    λ=%-6s  %-6s  rk=%d  rk H=%d" % (str(lam), "成立" if ok else "**失败**", a, b))
    print()

    print("【④ 独立判据：F 的行是否都落在 H 的行空间里（秩判据）】")
    print("    rk[H;F] == rk H ？", rk(stack(H, Fm)) == rk(H),
          "（rk[H;F]=%d, rk H=%d）" % (rk(stack(H, Fm)), rk(H)))
    print("    rk(0·H−F) = rk F = %d  vs  rk H = %d  ⟹ λ=0 处 (S) %s" %
          (rk(Fm), rk(H), "成立" if rk(Fm) == rk(H) else "**失败**"))
    print()
    print("=" * 66)
    okA = rankA(A, C, L)
    t5a = rk(matmul(L, NCA)) < q0
    sdirect = all(ok for _, ok, _, _ in rankS_direct(A, C, L, lams))
    spencil = all(ok for _, ok, _, _ in rankS_pencil(A, C, L, NCA, lams))
    print("(A)=%s   T5a=%s   原始(S)=%s   铅笔(S)=%s" % (okA, t5a, sdirect, spencil))
    if okA and t5a and sdirect and spencil:
        print()
        print("⟹⟹ **情形 II 下 (A) ∧ T5a ∧ (S) 同时成立** —— 这是 YES 实例 ✓")
        print("    ⟹ 与 FINAL §4.5「情形 II：(A)∧(S) = 0/200」**冲突** ⟹ 那边必须复核 ✗")
    else:
        print("\n⟹ 未成立，需要继续找（或判据不一致）")


if __name__ == "__main__":
    main()
