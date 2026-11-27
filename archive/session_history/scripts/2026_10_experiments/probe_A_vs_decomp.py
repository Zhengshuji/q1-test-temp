# -*- coding: utf-8 -*-
"""
probe_A_vs_decomp.py —— **决定性**：(A) 是否蕴含分解 LA = ΛL + G₀C + G₁CA ？

【为什么这是当前的关键】
  Lean `Theorems/C6.lean` 的 `c6'_final` 把
        hA : L ∘ A = Lam ∘ L + G0 ∘ C + G1 ∘ (C ∘ A)
  当作**假设**。若 (A) 本身就能推出它，c6′ 即可升级为**无条件定理**；
  若不能，则 c6′ 的陈述必须显式加这条假设（或换路线）。

【数学上的怀疑（本轮新提出）】
  (A) 是行空间包含： row(LA) ⊆ row(L, C, CA)。
  但 (A) 的**核形式**（FINAL §4.1 的 "(A) 核形式"）是
        L v = 0 ∧ C v = 0 ∧ C A v = 0  ⟹  L A v = 0        …… (*)
  两者**并不等价**！ (*) 等价于 ker(L) ∩ ker(C) ∩ ker(CA) ⊆ ker(LA)，
  而 (A) 等价于 ker(L) ∩ ker(C) ∩ ker(CA) = ker(L) ∩ ker[C;CA] ⊆ ker(LA)
  —— 后者**弱于** (*) ⟹ (A) 未必给出分解。

【本脚本】
  穷举小整数实例，统计
    ① (A) 成立但**不存在**分解者   ← 关键反例
    ② (A) 成立且分解存在，但 ΛH ≠ F 者
    ③ (A) 成立、分解存在、ΛH = F 者
  并显式打印 ① 的最小实例 + 手算验证。
"""
import os, io, contextlib, itertools
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
ker_basis = _ns["ker_basis"]

import linalg_q as Q


def build_system(A, C, L):
    """(A) 分解系统：LA = ΛL + G0 C + G1 CA"""
    q0, n, p = len(L), len(A), len(C)
    CA = Q.mul(C, A)
    LA = Q.mul(L, A)
    nunk = q0 * q0 + 2 * q0 * p
    rows, rhs = [], []
    for i in range(q0):
        for j in range(n):
            row = [F(0)] * nunk
            for kk in range(q0):
                row[kk * q0 + i] = L[kk][j]
            for m in range(p):
                row[q0 * q0 + i * p + m] = C[m][j]
            for m in range(p):
                row[q0 * q0 + q0 * p + i * p + m] = CA[m][j]
            rows.append(row)
            rhs.append([LA[i][j]])
    return rows, rhs


def check_instance(A, C, L):
    """返回 (isA, has_decomp, lamH_eq_F, Lam, N)

    ⚠️ 本函数初版把**原生 int** 形式的 L 直接传进系统 ⟹ `F/1` 被 Python 算成 **float** ✗
    （`int.__truediv__` 而非 `Fraction.__truediv__`）⟹ 后续精确判据全部失真。
    ⟹ 入口处一律先转成 Fraction ✓
    """
    A = Q.mat(A); C = Q.mat(C); L = Q.mat(L)
    n = len(A)
    CA = Q.mul(C, A)
    R = Q.stack(C, CA)
    isA = Q.condA(A, C, L)
    if not isA:
        return None
    rows, rhs = build_system(A, C, L)
    try:
        res = Q.solve(rows, rhs)
    except AssertionError as e:
        print("  [linalg_q.solve 报警] %s" % e)
        print("    A=", [[str(x) for x in r] for r in A], " C=", [[str(x) for x in r] for r in C],
              " L=", [[str(x) for x in r] for r in L])
        raise
    if res is None:
        return dict(isA=True, decomp=False, eqF=None, key=None)
    y = res[0]
    q0 = len(L)
    Lam = [[y[kk * q0 + i] for kk in range(q0)] for i in range(q0)]
    N = Q.ker_basis_cols(R)
    if not N or not N[0]:
        return dict(isA=True, decomp=True, eqF=True, key=None)
    H = Q.mul(L, N)
    Fm = Q.mul(Q.mul(L, A), N)
    eqF = (Q.mul(Lam, H) == Fm)
    # 若特解不满足，试零空间的其他解
    if not eqF:
        for v in res[1]:
            s = [y[j] + v[j] for j in range(len(y))]
            Lm = [[s[kk * q0 + i] for kk in range(q0)] for i in range(q0)]
            if Q.mul(Lm, H) == Fm:
                eqF = True
                Lam = Lm
                break
    return dict(isA=True, decomp=True, eqF=eqF, key=(tuple(map(tuple, A)), tuple(map(tuple, C)),
                                                    tuple(map(tuple, L))), Lam=Lam)


def main():
    print("=== (A) vs 分解存在性：穷举小整数实例 ===\n")
    n, p = 3, 1
    count = dict(total=0, isA=0, nodecomp=0, decomp=0, eqF=0, neF=0)
    examples = []
    A_list = [
        Q.mat([[0, 1, 0], [0, 0, 0], [0, 0, 0]]),      # A e1 = e2，A^2 = 0
        Q.mat([[0, 1, 0], [0, 0, 1], [0, 0, 0]]),      # 幂零指标 3
        Q.mat([[0, 1, 0], [0, 0, 0], [0, 0, 2]]),      # 有特征值 2
    ]
    for A in A_list:
        for Crow in itertools.product([-1, 0, 1], repeat=n):
            C = [list(Crow)]
            if Q.rank(C) != p:
                continue
            for q0 in [1, 2]:
                for Lrows in itertools.product(itertools.product([-1, 0, 1], repeat=n), repeat=q0):
                    L = [list(r) for r in Lrows]
                    if Q.rank(L) != q0:
                        continue
                    count["total"] += 1
                    r = check_instance(A, C, L)
                    if r is None:
                        continue
                    count["isA"] += 1
                    if not r["decomp"]:
                        count["nodecomp"] += 1
                        if len(examples) < 3:
                            examples.append((A, C, L))
                    else:
                        count["decomp"] += 1
                        if r["eqF"]:
                            count["eqF"] += 1
                        else:
                            count["neF"] += 1
    print("枚举实例总数            : %d" % count["total"])
    print("其中 (A) 成立           : %d" % count["isA"])
    print("  ① (A)✓ 但**无分解**    : %d   ← 关键" % count["nodecomp"])
    print("  ② (A)✓ 有分解、ΛH = F : %d" % count["eqF"])
    print("  ③ (A)✓ 有分解、ΛH ≠ F : %d   ← 也关键" % count["neF"])
    print()
    if examples:
        print("=== ① 的最小反例（手算可验）===")
        for A, C, L in examples:
            CA = Q.mul(C, A)
            print("  A =", [[str(x) for x in r] for r in A])
            print("  C =", [[str(x) for x in r] for r in C])
            print("  L =", [[str(x) for x in r] for r in L])
            print("  LA=", [[str(x) for x in r] for r in Q.mul(L, A)],
                  " CA=", [[str(x) for x in r] for r in CA])
            print("  (A): rk[LA;L;C;CA]=%d  rk[L;C;CA]=%d  ⟹ %s"
                  % (Q.rank(Q.stack(Q.mul(L, A), L, C, CA)), Q.rank(Q.stack(L, C, CA)),
                     Q.condA(A, C, L)))
            rows, rhs = build_system(A, C, L)
            print("  分解系统：秩(系数)=%d  秩(增广)=%d  ⟹ 无解 ⟹ 分解不存在 ✗"
                  % (Q.rank(rows), Q.rank(Q.hcat(rows, rhs))))
            print()
    print("【判读】")
    print("  ① > 0 ⟹ **(A) 不蕴含分解** ⟹ Lean `c6'_final` 的假设比 (A) 强 ⚠️")
    print("            ⟹ c6′ 若要无条件，必须另找路线（或显式加假设）")


if __name__ == "__main__":
    main()
