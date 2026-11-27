"""c399 — 核实 q=3 的 c=2 可行设计（c397 找到的那个）。

D = span{e1+e2, e3}（K 坐标），W = (0,0,1,1,0,0,0,0)（在 K^perp 内），V = D^{perp_K} ⊕ W。
逐项核对：dim V = 3、(5b) 的 gcd = 0、(5a) [AD ⟂ V]、精确核 [K ∩ V^perp = D]、omega = 2 = k-c。
"""

from __future__ import annotations

import itertools
import os
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import c335_lambda_movement as m  # noqa: E402
import c352_number_field_decider as d  # noqa: E402

lam = sp.symbols("lam")


def main() -> None:
    A, C = d.build_instance(4242)
    A = sp.Matrix(A)
    for i in range(4):
        for j in range(4):
            A[4 + i, 4 + j] = sp.diag(1, 1, 2, 3)[i, j]
    N = m.ker_basis(sp.Matrix.vstack(C, C * A))
    k = N.cols
    n = A.rows
    G = N.T * N
    I = sp.eye(k)
    Dk = sp.Matrix.hstack(I.col(0) + I.col(1), I.col(2))
    comp = [sp.simplify(c) for c in (Dk.T * G).nullspace()]
    W = sp.Matrix([[0], [0], [1], [1], [0], [0], [0], [0]])
    V = [sp.simplify(N * c) for c in comp] + [W]
    Vm = sp.Matrix.hstack(*V)
    print("dim V =", Vm.rank(), "（应为 q=3）")
    H = sp.simplify(Vm.T * N)
    HA = sp.simplify(Vm.T * A * N)
    print("omega = rank H =", H.rank(), "（k-c = 2）")
    AD = A * (N * Dk)
    print("(5a) AD ⟂ V ?", (Vm.T * AD).is_zero_matrix)
    # 精确核：dim(K ∩ V^perp)
    inter = k + Vm.rank() - sp.Matrix.hstack(N, Vm).rank()
    print("dim(K ∩ V^perp) =", inter, "（= dim D = 2?）")
    # (5b)
    om = H.rank()
    P = sp.Matrix(Vm.cols, k, lambda i, j: lam * H[i, j] - HA[i, j])
    polys = []
    for rs in itertools.combinations(range(Vm.cols), om):
        for cs in itertools.combinations(range(k), om):
            det = sp.expand(P.extract(list(rs), list(cs)).det())
            if sp.simplify(det) != 0:
                polys.append(det)
    gg = polys[0]
    for pp in polys[1:]:
        gg = sp.gcd(gg, pp)
    print(f"(5b): {len(polys)} 个 {om} 阶子式，gcd 次数 =", sp.degree(sp.simplify(gg), lam))
    print("L 的行（=V 的基）：")
    for i in range(Vm.cols):
        print("   ", sp.Matrix(Vm.col(i)).T.tolist())


if __name__ == "__main__":
    main()
