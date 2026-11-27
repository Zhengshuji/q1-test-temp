"""c391 — c>=2 的方向定理：ker H 必须是压缩 M 的不变子空间（精确核查，v2）。

构造（这台机器上 n=8, p=2, k=4, M = diag(1,1,2,3)，实例同 c357 的反例）：
  取 D <= K0（dim c = 2），令 U = D + A D，V = U^perp（行空间）。
  这是"把 D 当核方向"的**自然设计**：V 的行消去 D 与 A D，故 (5a) 自动成立。

  量：
    c      = dim(K0 ∩ V^⊥) = dim(K0 ∩ U)          （核方向维数）
    ω      = rank(LN) = k - c
    tr     = dim(V ∩ K0)                           （横截前提：应为 k - c）
    (5a)   : V ⟂ A D
    inv    : M(D) ⊆ D

  预期：
    * D 是 M-不变  ⟹ c = dim D, tr = k-c, inv ✓；
    * D 不是 M-不变 ⟹ c = dim(K0 ∩ U) > dim D（设计落到**更高**的层），inv ✗。
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


def instance():
    A, C = d.build_instance(4242)
    A = sp.Matrix(A)
    B = sp.diag(1, 1, 2, 3)
    for i in range(4):
        for j in range(4):
            A[4 + i, 4 + j] = B[i, j]
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    k = N.cols
    n = A.rows
    G = N.T * N
    M = sp.simplify(sp.Matrix(G.inv() * (N.T * A * N)))
    return A, C, N, M, k, n


def analyse(A, N, M, k, n, D_K):
    """D_K: K 坐标的列向量列表。"""
    D = sp.Matrix.hstack(*D_K)
    c0 = D.cols
    ND = N * D
    AD = A * ND
    U = sp.Matrix.hstack(ND, AD)
    dimU = U.rank()
    # V = U^perp
    V = U.T.nullspace()
    Vm = sp.Matrix.hstack(*V) if V else sp.zeros(n, 0)
    dimV = Vm.cols
    # c = dim(K0 ∩ U) = k - rank(V^T N) （因为 K0 ∩ U 与 V 相互正交补）
    c = k - (Vm.T * N).rank() if dimV else k
    omega = k - c
    # tr = dim(V ∩ K0) = dim V + k - rank[V; N^T]
    tr = dimV + k - sp.Matrix.vstack(Vm.T, N.T).rank()
    # (5a)：V ⟂ A D
    ok5a = (Vm.T * AD).is_zero_matrix if dimV else True
    # 不变性：M(D) ⊆ D
    MD = M * D
    inv = sp.Matrix.hstack(D, MD).rank() == c0
    return dict(c0=c0, dimU=dimU, dimV=dimV, c=c, omega=omega, tr=tr, ok5a=ok5a, inv=inv)


def show(tag, res, k):
    print(f"{tag}")
    print(f"   dim D = {res['c0']}, dim U = {res['dimU']}, dim V = {res['dimV']}")
    print(f"   c = {res['c']}, omega = {res['omega']}, dim(V∩K0) = {res['tr']} (k-c = {k-res['c']})")
    print(f"   (5a) = {res['ok5a']}, M(D) ⊆ D = {res['inv']}")


def main() -> None:
    A, C, N, M, k, n = instance()
    print(f"n = {n}, k = {k}, M = {M.tolist()}")
    print()
    I = sp.eye(k)
    cases = [
        ("D = span{e1,e2}（M-不变：μ=1 的特征空间）", [I.col(0), I.col(1)]),
        ("D = span{e1,e4}（M-不变：μ=1 与 μ=3）", [I.col(0), I.col(3)]),
        ("D = span{e1,e1+e3}（非 M-不变）", [I.col(0), I.col(0) + I.col(2)]),
        ("D = span{e1+e2, e3+e4}（非 M-不变）", [I.col(0) + I.col(1), I.col(2) + I.col(3)]),
    ]
    for tag, DK in cases:
        res = analyse(A, N, M, k, n, DK)
        show(tag, res, k)
        print()


if __name__ == "__main__":
    main()
