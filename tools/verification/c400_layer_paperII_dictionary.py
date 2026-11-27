"""c400 — 层程序与 Paper II 的 W-表述的对齐（字典验证）。

预期字典（本脚本逐项核对）：
  U  = pi_1(W) = row(V N)        ⊆ K*（K 坐标下的行空间）
  D  = ker H = K ∩ V^perp        = U^{perp_K}
  (5a)  ⟺  pi_2(W) ⊆ pi_1(W)
  c  = k - dim U
  M(D) ⊆ D  ⟺  U 是 M^* 不变的

对若干设计（含 c=1 的 4242 反例构造、c=2 的 c399 构造）核对。
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
    for i in range(4):
        for j in range(4):
            A[4 + i, 4 + j] = sp.diag(1, 1, 2, 3)[i, j]
    N = m.ker_basis(sp.Matrix.vstack(C, C * A))
    k = N.cols
    n = A.rows
    G = N.T * N
    M = sp.simplify(sp.Matrix(G.inv() * (N.T * A * N)))
    return A, N, M, k, n, G


def check(tag, Vm, A, N, M, k, n):
    """Vm: n×q 矩阵，列是 V 的基（环境坐标）。"""
    q = Vm.cols
    H = Vm.T * N
    HA = Vm.T * A * N
    om = H.rank()
    c = k - om
    # W = row(V [N AN]) ⊆ R^{2k}：行是 (x N, x A N)
    Wblk = sp.Matrix.hstack(Vm.T * N, Vm.T * A * N)     # q × 2k，行 = (xN, xAN)
    pi1 = Wblk[:, :k]
    pi2 = Wblk[:, k:]
    U = pi1.T                                          # 行空间的列表示
    # U 的行空间（K 坐标）
    Ur = U.rowspace()
    dimU = len(Ur)
    # (5a) ⟺ pi2 的行落在 pi1 的行空间里
    pisub = sp.Matrix.vstack(pi1, pi2).rank() == sp.Matrix(pi1).rank()
    # D = ker H（K 坐标）
    ns = H.nullspace(); Dm = sp.Matrix.hstack(*ns) if ns else sp.zeros(k, 0)
    dimD = Dm.cols
    # U^{perp_K}：{x in K : <x, u> = 0 for u in U}（K 坐标，G 内积）
    G = N.T * N
    perp = sp.Matrix(pi1 * G).nullspace()               # 与 U 的行正交
    dimPerp = len(perp)
    # D 与 U^perp 是同一个空间？
    same = False
    if dimD == dimPerp and dimD > 0:

        Pm = sp.Matrix.hstack(*perp)
        same = sp.Matrix.hstack(Dm, Pm).rank() == dimD
    elif dimD == 0 and dimPerp == 0:
        same = True
    # M(D) ⊆ D  ⟺ U 是 M^* 不变：等价地 M(D) ⊆ D
    inv = True
    if dimD > 0:

        inv = sp.Matrix.hstack(Dm, M * Dm).rank() == dimD
    print(f"{tag}")
    print(f"   q={q}, omega=rank H={om}, c=k-omega={c}, dim U={dimU}（应=k-c={k-c}）")
    print(f"   D=ker H: dim={dimD}; U^perp_K: dim={dimPerp}; 同一个空间? {same}")
    print(f"   (5a) ⟺ pi2 ⊆ pi1 : {pisub}")
    print(f"   M(D) ⊆ D : {inv}")
    print()


def main() -> None:
    A, N, M, k, n, G = build()
    I = sp.eye(k)
    # 例子 1：c=2 的可行设计（c399）
    Dk = sp.Matrix.hstack(I.col(0) + I.col(1), I.col(2))
    comp = [sp.simplify(c) for c in (Dk.T * G).nullspace()]
    Wv = sp.Matrix([[0], [0], [1], [1], [0], [0], [0], [0]])
    Vm = sp.Matrix.hstack(*([sp.simplify(N * c) for c in comp] + [Wv]))
    check("例子 1：c=2 可行设计（D=span{e1+e2,e3}）", Vm, A, N, M, k, n)
    # 例子 2：c=1 的强制设计（D=e1, V=D^{perp_K}）
    D1 = sp.Matrix(I.col(0))
    comp1 = [sp.simplify(c) for c in (D1.T * G).nullspace()]
    Vm1 = sp.Matrix.hstack(*[sp.simplify(N * c) for c in comp1])
    check("例子 2：c=1 强制设计（D=e1, q=3）", Vm1, A, N, M, k, n)
    # 例子 3：随机 4 行（一般位置，c=0）
    import random
    random.seed(3)
    L = sp.Matrix([[random.randint(-2, 2) for _ in range(n)] for _ in range(4)])
    check("例子 3：随机 4 行（一般位置）", L.T, A, N, M, k, n)


if __name__ == "__main__":
    main()
