# -*- coding: utf-8 -*-
"""
probe_decomp_hypotheses.py —— 找出"分解"**恰好需要**的假设（用于 Lean 表述）

【三个候选条件】
  W1 : ∀v, L v = 0 → C v = 0 → L (A v) = 0        （含 CA 的核形式的"L,C 部分"）
  W2 : ∀v, C v = 0 → C (A v) = 0 → L (A v) = 0      （含 CA 的核形式的"CA 部分"）
  KF∩: ∀v, L v = 0 → C v = 0 → C (A v) = 0 → L (A v) = 0   （项目 Lean 现在用的）

【要回答】
  W1 ∧ W2 ⟹ DEC ？  以及 W1∧W2 与 (A)row、KF∩ 的关系
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
    print("=== 分解所需的假设：穷举检验 ===\n")
    n, p = 3, 1
    As = [Q.mat([[0,1,0],[0,0,0],[0,0,0]]),
          Q.mat([[0,1,0],[0,0,1],[0,0,0]]),
          Q.mat([[0,1,0],[0,0,0],[0,0,2]])]
    st = dict(tot=0, Arow=0, KFi=0, W1=0, W1W2=0, dec=0,
              Arow_not_W1W2=0, W1W2_not_dec=0, KFi_not_W1W2=0)
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
                    W1 = sub_le(Q.nullspace(Q.stack(L, C)), Q.nullspace(LA))
                    W2 = sub_le(Q.nullspace(Q.stack(C, CA)), Q.nullspace(LA))
                    KFi = sub_le(Q.nullspace(Q.stack(L, C, CA)), Q.nullspace(LA))
                    rows, rhs = build_system(A, C, L)
                    dec = Q.solve(rows, rhs) is not None
                    if Arow:
                        st["Arow"] += 1
                        if not (W1 and W2):
                            st["Arow_not_W1W2"] += 1
                    if KFi:
                        st["KFi"] += 1
                        if not (W1 and W2):
                            st["KFi_not_W1W2"] += 1
                    if W1:
                        st["W1"] += 1
                    if W1 and W2:
                        st["W1W2"] += 1
                        if not dec:
                            st["W1W2_not_dec"] += 1
                            if len(ex) < 3:
                                ex.append((A, C, L))
                    if dec:
                        st["dec"] += 1
    print("枚举实例数              : %d" % st["tot"])
    print("(A)row                 : %d" % st["Arow"])
    print("KF∩                    : %d" % st["KFi"])
    print("W1                     : %d" % st["W1"])
    print("W1 ∧ W2                : %d" % st["W1W2"])
    print("DEC                    : %d" % st["dec"])
    print()
    print("(A)row ⟹ W1∧W2 ?        : 反例 %d 个" % st["Arow_not_W1W2"])
    print("KF∩ ⟹ W1∧W2 ?           : 反例 %d 个   ← 若 >0，项目现有核形式不够" % st["KFi_not_W1W2"])
    print("W1∧W2 ⟹ DEC ?           : 反例 %d 个   ← 若 0，则假设就取 W1∧W2 ✓" % st["W1W2_not_dec"])
    for A, C, L in ex:
        print("  反例 A=", [[str(x) for x in r] for r in A], " C=", [[str(x) for x in r] for r in C],
              " L=", [[str(x) for x in r] for r in L])


if __name__ == "__main__":
    main()
