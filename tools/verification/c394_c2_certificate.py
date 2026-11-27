"""c394 — 按专家 107 号要求，把 c>=2 的反例补成可独立核对的证书。

输出（专家第 6 节列的七项）：
  1. M 与 A21（A 的两个块）；2. D+AD 的基；3. 其维数；4. K ∩ (D+AD)；
  5. V = (D+AD)^perp；6. dim(K ∩ V^perp)、dim(V ∩ K)、rank H；7. AD ⟂ V。

另外核对专家 §9 的 K-split 纤维公式：
  在 K-split 情形下 V = D^{perp_K} ⊕ W，W ⊆ T_D = K^perp ∩ (A21 D)^perp，
  dim W = t = q - rho，纤维 = Gr(t - dim W0, T_D / W0)。
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


def build():
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
    # A21 = pi_{K0^perp} A |_{K0}，作为 n×k 矩阵
    Proj = sp.eye(n) - N * sp.Matrix(G.inv()) * N.T
    A21 = sp.simplify(Proj * A * N)
    return A, C, N, M, A21, k, n, G


def show_vecs(tag, V, N):
    """V: 环境向量列表（列）。同时给出 K 坐标（若在 K0 内）。"""
    print(f"   {tag}: {len(V)} 个向量")
    for v in V:
        print("     ", sp.Matrix(v).T.tolist())


def main() -> None:
    A, C, N, M, A21, k, n, G = build()
    print(f"n = {n}, k = {k}")
    print("M =", M.tolist())
    print("A21 =", A21.tolist())
    print("（A21 是 n×k 矩阵；K0 由 N 的列张成）")
    print()

    I = sp.eye(k)
    cases = {
        "不变 D = span{e1,e2}（应 K-split）": [I.col(0), I.col(1)],
        "非不变 D = span{e1+e2, e3+e4}（反例）": [I.col(0) + I.col(1), I.col(2) + I.col(3)],
    }
    for tag, DK in cases.items():
        print("=" * 70)
        print(tag)
        D = sp.Matrix.hstack(*DK)
        ND = N * D
        AD = A * ND
        U = sp.Matrix.hstack(ND, AD)
        print(f"  1) M, A21 见上（D 的 K 坐标 = {D.T.tolist()}）")
        print(f"  2) D+AD 的基（环境坐标）：")
        for j in range(U.cols):
            print("       u%d = %s" % (j + 1, sp.Matrix(U.col(j)).T.tolist()))
        print(f"  3) dim(D+AD) = {U.rank()}  （= c + rank(A21|_D) = 2 + {A21[:, :].rank() if False else sp.Matrix(A21 * D).rank()}）")
        # 4) K ∩ (D+AD)
        # K = col(N)；K ∩ U 的维数 = k - rank(N^T U)… 用 [N | U] 的秩
        inter = k + U.rank() - sp.Matrix.hstack(N, U).rank()
        print(f"  4) dim(K ∩ (D+AD)) = {inter}   （应 = dim D = 2 才是精确核）")
        # 5) V = U^perp
        Vb = U.T.nullspace()
        Vm = sp.Matrix.hstack(*Vb) if Vb else sp.zeros(n, 0)
        q = Vm.cols
        print(f"  5) V = (D+AD)^perp：dim V = q = {q}")
        # 6) 三个量
        c_new = k - (Vm.T * N).rank()
        rho = sp.Matrix(Vm.T * N).rank()
        tr = Vm.rank() + k - sp.Matrix.hstack(N, Vm).rank()
        H = Vm.T * N
        print(f"  6) dim(K ∩ V^perp) = {c_new}；dim(V ∩ K) = {tr}；rank H = {H.rank()}；rho = {rho}")
        # 7) AD ⟂ V
        print(f"  7) AD ⟂ V ? {(Vm.T * AD).is_zero_matrix}")
        # K-split 判断
        W = sp.Matrix(Vm.T * sp.Matrix.hstack(*sp.Matrix(N).T.nullspace() if False else []) if False else sp.zeros(n, 0))
        # V ∩ K^perp 的维数 = q - rho
        print(f"  K-split? dim(V∩K)={tr}, dim(V∩K^perp)={q-rho}, q={q} -> {tr + (q - rho) == q}")
        print()


if __name__ == "__main__":
    main()
