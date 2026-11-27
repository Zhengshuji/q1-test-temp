# -*- coding: utf-8 -*-
"""
probe_final_hypothesis.py —— 最终确认：分解**真正需要**的假设是哪个？

【本轮的关键转折】
  我一直在纠结 Lean 的类型细节，但真正的问题是**数学**：
    (A) 的「核形式」 KF∩ : (ker L ∩ ker C ∩ ker CA) ⊆ ker(LA)
    是否足以构造分解 LA = ΛL + G₀C + G₁CA ？

  我此前的构造（在 M = (L,C,C∘A) 的像上用 liftQ 定义 ψ）**隐含了一个错误假设**：
    "坐标分量 (w,0,0)、(0,g,0)、(0,0,h) 都落在 M.range 中" —— **一般是假的** ✗
    （例如 (0,0,h) ∈ M.range 要求 h ∈ im(C∘A)）

  而"行空间形式" (A)row 恰好给出正确的分量分解：
    row(LA) ⊆ row(L) ∪ row(C) ∪ row(CA)   ⟹   LA = ΛL + G₀C + G₁CA
    其中 Λ 定义在 L.range 上、（ker L ⊆）… 需要的是**这一组**核包含：
      ker L ⊆ ker(LA) 、 ker C ⊆ ker(LA) 、 ker CA ⊆ ker(LA)
    —— 它们**各自**由 row(LA) ⊆ row(L)、row(LA) ⊆ row(C)、row(LA) ⊆ row(CA) 给出，
       而这三条**合起来**才是 row(LA) ⊆ row(L) + row(C) + row(CA) ✓

【本脚本】对 (A)row 与 KF∩ 分别检验
  ① (A)row ⟹ （分解存在）
  ② KF∩ ⟹ （分解存在）
  并给出反例（若有）。
"""
import os, io, contextlib, itertools
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)

import linalg_q as Q


def build_system(A, C, L):
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


def sub_le(P, Qgen):
    if not P:
        return True
    if not Qgen:
        return Q.rank(P) == 0
    return Q.rank(P + Qgen) == Q.rank(Qgen)


def main():
    print("=== (A)row 与 KF∩ 对分解的充分性 ===\n")
    n, p = 3, 1
    As = [Q.mat([[0,1,0],[0,0,0],[0,0,0]]),
          Q.mat([[0,1,0],[0,0,1],[0,0,0]]),
          Q.mat([[0,1,0],[0,0,0],[0,0,2]])]
    st = dict(tot=0, Arow=0, KFi=0, dec=0,
              Arow_dec=0, KFi_dec=0, KFi_notdec=0, Arow_notdec=0)
    ex = []
    for A in As:
        for Crow in itertools.product([-1, 0, 1], repeat=n):
            C = Q.mat([list(Crow)])
            if Q.rank(C) != p:
                continue
            CA = Q.mul(C, A)
            for q0 in [1, 2]:
                for Lr in itertools.product(itertools.product([-1, 0, 1], repeat=n), repeat=q0):
                    L = Q.mat([list(r) for r in Lr])
                    if Q.rank(L) != q0:
                        continue
                    st["tot"] += 1
                    LA = Q.mul(L, A)
                    Arow = Q.rank(Q.stack(LA, L, C, CA)) == Q.rank(Q.stack(L, C, CA))
                    KFi = sub_le(Q.nullspace(Q.stack(L, C, CA)), Q.nullspace(LA))
                    rows, rhs = build_system(A, C, L)
                    dec = Q.solve(rows, rhs) is not None
                    if dec:
                        st["dec"] += 1
                    if Arow:
                        st["Arow"] += 1
                        if dec:
                            st["Arow_dec"] += 1
                        else:
                            st["Arow_notdec"] += 1
                    if KFi:
                        st["KFi"] += 1
                        if dec:
                            st["KFi_dec"] += 1
                        else:
                            st["KFi_notdec"] += 1
                            if len(ex) < 3:
                                ex.append((A, C, L))
    print("枚举实例数          : %d" % st["tot"])
    print("(A)row 成立         : %d" % st["Arow"])
    print("KF∩ 成立            : %d" % st["KFi"])
    print("分解存在            : %d" % st["dec"])
    print()
    print("(A)row ⟹ 分解       : 成立 %d / 反例 %d" % (st["Arow_dec"], st["Arow_notdec"]))
    print("KF∩   ⟹ 分解       : 成立 %d / **反例 %d** ← 若 >0，则核形式**不足以**做分解 ✗"
          % (st["KFi_dec"], st["KFi_notdec"]))
    if ex:
        print("\nKF 交 成立 但分解不存在的例子：")
        for A, C, L in ex:
            print("  A=", [[str(x) for x in r] for r in A])
            print("  C=", [[str(x) for x in r] for r in C])
            print("  L=", [[str(x) for x in r] for r in L])


if __name__ == "__main__":
    main()
