"""c410 — 核对：dim D° 到底是 c 还是 omega？铅笔的行空间是否整体落在 D° 里？

D° = {f ∈ K0* : f|_D = 0}，故 dim D° = k - dim D = k - c = omega。
本脚本在三组 (k,c) 上核对：
  (i) dim D° = omega（用 D 的零化子的维数）；
  (ii) H 的行空间 ⊆ D°（即每行在 D 上为零）；
  (iii) lambda H - H_A 的行空间 ⊆ D°（对若干 lambda）。
"""

from __future__ import annotations

import os
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import c335_lambda_movement as m  # noqa: E402
import c352_number_field_decider as d  # noqa: E402


def build(diag):
    A, C = d.build_instance(4242)
    A = sp.Matrix(A)
    for i in range(4):
        for j in range(4):
            A[4 + i, 4 + j] = diag[i, j]
    N = m.ker_basis(sp.Matrix.vstack(C, C * A))
    k = N.cols
    G = N.T * N
    return A, N, k, G


def main() -> None:
    lam = sp.symbols("lam")
    for tag, diag in (
        ("M = diag(1,1,2,3)", sp.diag(1, 1, 2, 3)),
        ("M = diag(1,1,1,2)", sp.diag(1, 1, 1, 2)),
    ):
        A, N, k, G = build(diag)
        n = A.rows
        print(f"=== {tag}: n={n}, k={k} ===")
        # 用 c=2 的 D：span{e1+e2, e3}
        I = sp.eye(k)
        Dk = sp.Matrix.hstack(I.col(0) + I.col(1), I.col(2))
        c = Dk.cols
        comp = [sp.simplify(x) for x in (Dk.T * G).nullspace()]  # D^{perp_K0}，k-c 维
        # (i) D° 的维数 = k - c
        print(f"   c=dim D={c}, k-c={k-c}；omega 应为 k-c")
        # 取一个 split 设计：V = D^{perp_K0} + 一行 W（W 取 (0,0,1,1,0,...,0)）
        W = sp.Matrix([[0], [0], [1], [1], [0], [0], [0], [0]])
        V = [sp.simplify(N * x) for x in comp] + [W]
        Vm = sp.Matrix.hstack(*V)
        H = sp.simplify(Vm.T * N)
        HA = sp.simplify(Vm.T * A * N)
        print(f"   V 的维数 q={Vm.rank()}，omega=rank H={H.rank()}，k-c={k-c}（应相等）")
        # (ii) H 的行 ⊆ D°
        # 行 r 在 D 上为零 <=> r * Dk_col = 0
        bad = [i for i in range(H.rows) if not (sp.Matrix(H.row(i)) * Dk).is_zero_matrix]
        print(f"   H 的行是否全在 D° 里（在 D 上为零）：{'是' if not bad else f'否，坏行 {bad}'}")
        # (iii) lambda H - H_A 的行 ⊆ D°
        for lv in (0, 1, 2, 5):
            P = sp.simplify(lv * H - HA)
            bad = [i for i in range(P.rows) if not (sp.Matrix(P.row(i)) * Dk).is_zero_matrix]
            print(f"   λ={lv}: 行是否全在 D° 里：{'是' if not bad else f'否，坏行 {bad}'}；"
                  f"rank={P.rank()}（应 <= k-c={k-c}）")
        print()


if __name__ == "__main__":
    main()
