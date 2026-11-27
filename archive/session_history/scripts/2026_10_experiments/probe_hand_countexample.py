# -*- coding: utf-8 -*-
"""
probe_hand_countexample.py —— 用手算反例检验"分解探针"是否可靠

【手算反例】
  A = [[0,1,0],[0,0,0],[0,0,0]]（A e1 = e2，A^2 = 0）
  C = [0,1,0]（= e2*）  ⟹ CA = C·A = [0,0,0] = 0
  L = [1,0,0]（= e1*）  ⟹ LA = L·A = [0,1,0]

  逐点检验：v = (1,-1,0) 时
      L v = 1, C v = -1, CA v = 0, L(A v) = -1
  任何分解 LA = ΛL + G₀C + G₁CA 都必须给出
      L(A v) = Λ(L v) + G₀(C v) + G₁(CA v)
    ⟹ -1 = Λ(1) + G₀(-1) + G₁(0)
    Λ 是 1×1 ⟹ Λ(1) = Λ₁₁
    G₀ 是 1×2 ⟹ G₀(-1) = -G₀₁₁·1 + 0  ⟹ 设 G₀₁₁ = a₀ ⟹ G₀(-1) = -a₀
    ⟹ -1 = Λ₁₁ - a₀
  而 (A) 判据 rk[LA;L;C;CA] == rk[L;C;CA] 在 (L=L₀; C, CA 与 R 一起堆叠) 下要**完整**核对。

本脚本：直接算 (A) 判据 + 直接解分解系统（用 linalg_q），看是否真有分解。
"""
import os, io, contextlib
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


def main():
    print("=== 手算反例：核形式 vs 分解 ===\n")
    A = Q.mat([[0,1,0],[0,0,0],[0,0,0]])
    C = Q.mat([[0,1,0]])
    L = Q.mat([[1,0,0]])
    CA = Q.mul(C, A); LA = Q.mul(L, A)
    print("A  =", [[str(x) for x in r] for r in A])
    print("C  =", [[str(x) for x in r] for r in C], " CA =", [[str(x) for x in r] for r in CA])
    print("L  =", [[str(x) for x in r] for r in L], " LA =", [[str(x) for x in r] for r in LA])
    print()
    # (A) 判据（4 块：LA; L; C; CA 与 L; C; CA）
    r1 = Q.rank(Q.stack(LA, L, C, CA)); r2 = Q.rank(Q.stack(L, C, CA))
    print("rk[LA;L;C;CA] = %d ; rk[L;C;CA] = %d ; (A) 成立？ %s" % (r1, r2, r1 == r2))
    # 核形式
    kerMC = Q.nullspace(Q.stack(L, C, CA))
    kerLA = Q.nullspace(LA)
    def sub_le(P, Qg):
        if not P: return True
        if not Qg: return Q.rank(P) == 0
        return Q.rank(P + Qg) == Q.rank(Qg)
    print("ker[L;C;CA] =", [[str(x) for x in v] for v in kerMC])
    print("ker[LA]     =", [[str(x) for x in v] for v in kerLA])
    print("KF∩ 成立？ %s" % sub_le(kerMC, kerLA))
    print("ker L ⊆ ker LA ？ %s   （ker L = %s）"
          % (sub_le(Q.nullspace(L), kerLA), [[str(x) for x in v] for v in Q.nullspace(L)]))
    print("ker C ⊆ ker LA ？ %s   （ker C = %s）"
          % (sub_le(Q.nullspace(C), kerLA), [[str(x) for x in v] for v in Q.nullspace(C)]))
    # 分解系统
    rows, rhs = build_system(A, C, L)
    print()
    print("分解系统：%d 方程 / %d 未知量 ；系数秩 %d ；增广秩 %d"
          % (len(rows), len(rows[0]), Q.rank(rows), Q.rank(Q.hcat(rows, rhs))))
    res = Q.solve(rows, rhs)
    print("分解存在？ %s" % (res is not None))
    if res is not None:
        q0 = len(L)
        y = res[0]
        Lam = [[y[kk*q0+i] for kk in range(q0)] for i in range(q0)]
        G0 = [[y[q0*q0 + i*len(C) + m] for m in range(len(C))] for i in range(q0)]
        G1 = [[y[q0*q0 + q0*len(C) + i*len(C) + m] for m in range(len(C))] for i in range(q0)]
        print("  Λ  =", [[str(x) for x in r] for r in Lam])
        print("  G₀ =", [[str(x) for x in r] for r in G0])
        print("  G₁ =", [[str(x) for x in r] for r in G1])
        # 检验逐点恒等式
        n = len(A)
        ok = True
        for j in range(n):
            v = [F(1) if t == j else F(0) for t in range(n)]
            Lv = [sum(L[0][t]*v[t] for t in range(n))]
            Cv = [sum(C[0][t]*v[t] for t in range(n))]
            CAv = [sum(CA[0][t]*v[t] for t in range(n))]
            LAv = [sum(LA[0][t]*v[t] for t in range(n))]
            lhs = sum(Lam[0][k]*Lv[k] for k in range(q0)) \
                + sum(G0[0][m]*Cv[m] for m in range(len(C))) \
                + sum(G1[0][m]*CAv[m] for m in range(len(C)))
            if lhs != LAv[0]:
                ok = False
                print("  逐点检验失败于 v = e%d : ΛL+G0C+G1CA = %s ≠ LAv = %s"
                      % (j+1, lhs, LAv[0]))
        print("  逐点恒等式 L(Av) = Λ(Lv)+G₀(Cv)+G₁(CAv) ？ %s" % ok)


if __name__ == "__main__":
    main()
