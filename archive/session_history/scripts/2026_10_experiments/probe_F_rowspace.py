# -*- coding: utf-8 -*-
"""
probe_F_rowspace.py —— **决定性对照**：F 的行空间是否总落在 H 的行空间里？

【冲突来源】
  我推得：(A) 的分解 LA = ΛL + G₀C + G₁CA 右乘 N_CA（因 C·N_CA = CA·N_CA = 0）得
        F = Λ·H      ⟹  row(F) ⊆ row(H)      …… (*)
  但项目数据显示：情形 I（d_CA < q0）有 (A)∧(S) = 87/87，而 (S) ⟺ rk(λH−F) == rk H ∀λ。
  若 (*) 成立，(S) 需要 F 的行落在 row(H) 里；反过来若 (*) 不成立，则 T5′ 有问题。

  ⟹ 直接对**情形 I 与情形 II 的实例**逐点算两个量：
        R1 := rk[H ; F]  vs  rk H        （(*)：两者相等？）
        R2 := (S) 是否成立
     并逐点验证 ΛH = F（用 batch_c6p_k.solve_Lambda 的实际 Λ）
"""
import os, io, contextlib, random
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
solve_Lambda = _ns3["solve_Lambda"]
S_holds = _ns3["S_holds"]


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


def condA(A, C, L):
    CA = matmul(C, A)
    return rk(stack(matmul(L, A), L, C, CA)) == rk(stack(L, C, CA))


def main():
    print("=== F 与 H 的行空间关系：逐点对照 ===\n")
    cases = [
        # (tag, A, C, 期望情形)
        ("I-4x4", mat([[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
                  mat([[0,0,1,0]]), "I"),
        ("I-5x5", mat([[0,0,0,1,0],[0,0,0,0,1],[0,0,0,0,0],
                       [0,0,0,0,0],[0,0,0,0,0]]),
                  mat([[0,0,0,1,0]]), "I"),
        ("II-nilp6a", mat([[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1],
                           [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]),
                      mat([[0,0,0,1,0,0],[0,0,0,0,1,0]]), "II"),
    ]
    rng = random.Random(7)
    for tag, A, C, kind in cases:
        n, p = len(A), len(C)
        CA = matmul(C, A)
        B = ker_basis(stack(C, CA))
        if not B or not B[0]:
            print("[%s] ker[C;CA] 平凡，跳过" % tag)
            continue
        d = len(B[0])
        print("[%s] n=%d p=%d d_CA=%d  情形=%s" % (tag, n, p, d, kind))
        npts = 0
        for trial in range(400):
            q0 = rng.choice([1, 2, 3])
            L = [[F(rng.randint(-3, 3)) for _ in range(n)] for _ in range(q0)]
            if rk(L) != q0:
                continue
            if not condA(A, C, L):
                continue
            npts += 1
            H = matmul(L, B)
            Fm = matmul(matmul(L, A), B)
            rH, rF, rHF = rk(H), rk(Fm), rk(stack(H, Fm))
            sols = solve_Lambda(A, C, L)
            lam_ok = any(matmul(Lam, H) == Fm for Lam in sols)
            Sval = None
            for Lam in sols:
                if matmul(Lam, H) == Fm:
                    Sval = S_holds(Lam, H)
                    break
            if npts <= 6:
                print("    q0=%d rkH=%d rkF=%d rk[H;F]=%d | (A)✓ 有Λ使ΛH=F: %s | (S)=%s"
                      % (q0, rH, rF, rHF, lam_ok, Sval))
            if npts >= 60:
                break
        print("    —— (A)-点共 %d 个" % npts)
        print()
    print("【判读】")
    print("  · 若 rk[H;F] == rkH 恒成立 ⟹ F 的行空间 ⊆ H 的行空间 ⟹ 需解释为何 (S) 仍可成立")
    print("  · 若出现 rk[H;F] > rkH ⟹ (*) 不成立 ⟹ 取出的 Λ 不满足 F=ΛH ⟹ T5′ 需加假设 ⚠️")


if __name__ == "__main__":
    main()
