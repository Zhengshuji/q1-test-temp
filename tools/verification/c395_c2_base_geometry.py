"""c395 — c=2 的底几何：M-不变 2-子空间簇 I_2(M) 的结构核对。

对 k=4 的三种 M，核对"不变 2-平面 = 两族之和"的结构，并核对维数公式。

  情形 1：M = diag(1,2,3,4)          单实谱        -> I_2 是有限集（6 个点）
  情形 2：M = diag(1,1,2,3)          对角、重根     -> Gr(2,E1) ∪ (P(E1)×P(E2)) ∪ ...（含点与曲线）
  情形 3：M = diag(1,1,1,2)          重根 dim 3    -> Gr(2,E1)（正维）∪ P(E1)×P(E2)（曲线）
  情形 4：M = J(0) ⊕ diag(2,3)       Jordan 块     -> 块内的不变 2-平面只有 flag 的前两个向量

核对方式：随机取 M-不变 2-平面（解 M X = X T），检查它是否落在预测的族里；
并对情形 2/3 核对 Gr(2,E1) 的维数。
"""

from __future__ import annotations

import itertools
import random

import sympy as sp


def invariant_planes_from_pairs(M, k):
    """由"两个特征向量/广义特征向量"张成的不变 2-平面（用 MX = XT 的线性系统验证）。"""
    out = []
    M = sp.Matrix(M)
    for i, j in itertools.combinations(range(k), 2):
        X = sp.zeros(k, 2)
        X[i, 0] = 1
        X[j, 1] = 1
        T = sp.zeros(2, 2)
        # 检查 span{e_i,e_j} 是否 M-不变：MX 的列是否落在 span{e_i,e_j}
        MX = M * X
        basis = sp.Matrix.hstack(X.col(0), X.col(1))
        cols = [MX.col(0), MX.col(1)]
        ok = all(sp.Matrix.hstack(basis, c).rank() == 2 for c in cols)
        if ok:
            out.append((i, j))
    return out


def main() -> None:
    k = 4
    cases = {
        "情形 1  M = diag(1,2,3,4)（单实谱）": sp.diag(1, 2, 3, 4),
        "情形 2  M = diag(1,1,2,3)（重根 dim 2）": sp.diag(1, 1, 2, 3),
        "情形 3  M = diag(1,1,1,2)（重根 dim 3）": sp.diag(1, 1, 1, 2),
    }
    for tag, M in cases.items():
        pairs = invariant_planes_from_pairs(M, k)
        print(tag)
        print(f"   坐标 2-平面中不变的：{pairs}  （共 {len(pairs)} 个）")
        # 预测：E1 的维数
        ev = {}
        for i in range(k):
            ev.setdefault(M[i, i], []).append(i)
        print(f"   特征空间分解：{ {str(a): [b+1 for b in bs] for a, bs in ev.items()} }")
        n_gr = sum(1 for a, bs in ev.items() if len(bs) >= 2)
        n_mix = sum(1 for a, bs in ev.items() for b2, bs2 in ev.items() if a < b2)
        print(f"   预测分量：Gr(2, E_λ) 型 {n_gr} 个（正维）+ ℙ(E_λ)×ℙ(E_μ) 型 {n_mix} 个")
        print()

    print("情形 4  M = J_2(0) ⊕ diag(2,3)：")
    J = sp.zeros(4, 4)
    J[0, 1] = 1
    J[2, 2] = 2
    J[3, 3] = 3
    pairs = invariant_planes_from_pairs(J, 4)
    print(f"   坐标 2-平面中不变的：{pairs}")
    print("   （Jordan 块内只有 flag 的 span{e_1,e_2}；其余是与对角块的混合）")


if __name__ == "__main__":
    main()
