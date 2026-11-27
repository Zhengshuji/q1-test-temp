"""c415 — 修正 c411 的测试数据：W 必须取在 T_D 内，并断言 (5a) 与精确核。

c411 的 cert 只取了一个固定 W 而没有检查 W ⊆ T_D —— 对 A21≠0 的实例，
该 W 可能不在 T_D 里，于是 (5a) 失败，那样的"设计"是无效的。
本脚本改用 T_D 的基向量作 W，并逐项断言。
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


def build(diag_M, A12, C=None):
    A, C0 = d.build_instance(4242)
    A = sp.Matrix(A)
    if C is None:
        for i in range(4):
            for j in range(4):
                A[4 + i, 4 + j] = diag_M[i, j]
            # 也换 A12 块（前 4 行的后 4 列）
            for i in range(4):
                for j in range(4):
                    A[i, 4 + j] = A12[i, j]
    else:
        C1 = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0]])
        C = sp.Matrix.hstack(C1, sp.zeros(2, 4))
        A11 = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]])
        A = sp.Matrix.vstack(sp.Matrix.hstack(A11, A12), sp.Matrix.hstack(A12, diag_M))
        C0 = C
    Wm = sp.Matrix.vstack(C0, C0 * A)
    N = m.ker_basis(Wm)
    k = N.cols
    G = N.T * N
    Proj = sp.eye(8) - N * sp.Matrix(G.inv()) * N.T
    A21 = sp.simplify(Proj * A * N)
    return A, C0, N, k, G, A21


def as_col(t, n=8):
    M = sp.Matrix(t)
    if M.shape == (n, 1):
        return M
    if M.shape == (1, n):
        return M.T
    return M.reshape(n, 1)


def run(tag, A, C, N, k, G, A21, Dk, q_target):
    comp = [sp.simplify(x) for x in (Dk.T * G).nullspace()]
    TD = [as_col(t) for t in sp.Matrix.vstack(N.T, (A21 * Dk).T).nullspace()]
    print(f"{tag}")
    print(f"   r(D)={sp.Matrix(A21*Dk).rank()}, dim T_D={len(TD)}")
    if not TD:
        print("   T_D = 0：无 W，占位（w0=0 时需 t=0）")
        return
    Wv = TD[0]
    V = [sp.simplify(N * x) for x in comp] + [Wv]
    Vm = sp.Matrix.hstack(*V)
    H = sp.simplify(Vm.T * N)
    HA = sp.simplify(Vm.T * A * N)
    om = H.rank()
    AD = A * (N * Dk)
    ok5a = (Vm.T * AD).is_zero_matrix
    exact = (k + Vm.rank() - sp.Matrix.hstack(N, Vm).rank()) == Dk.cols
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
    dg = sp.degree(sp.simplify(gg), lam)
    print(f"   q={Vm.rank()} (target {q_target}), omega={om}, (5a)={ok5a}, exact={exact}, "
          f"非零子式={len(polys)}, gcd次数={dg}, phi(T_D)的秩="
          f"{sp.Matrix.vstack(*[sp.Matrix(x).T*A21 for x in TD]).rank() if TD else 0}")


def main() -> None:
    I = sp.eye(4)
    z = sp.zeros(4, 4)
    u = sp.Matrix([0, 0, 1, 0])
    v = sp.Matrix([1, 0, 0, 0])
    A12r1 = u * v.T
    cases = [
        ("类1 M=diag(1,2,3,4), D=span{e1,e2}", sp.diag(1, 2, 3, 4), z,
         sp.Matrix.hstack(I.col(0), I.col(1))),
        ("类2 M=diag(R,2,3), D=ker(M^2+I)=span{e1,e2}",
         sp.Matrix([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 2, 0], [0, 0, 0, 3]]), z,
         sp.Matrix.hstack(I.col(0), I.col(1))),
        ("类3 M=diag(1,1,2,3), D=span{e1,e2}", sp.diag(1, 1, 2, 3), z,
         sp.Matrix.hstack(I.col(0), I.col(1))),
        ("类4 M=diag(1,1,1,2), A12 秩1, D=span{e1,e3}",
         sp.diag(1, 1, 1, 2), A12r1, sp.Matrix.hstack(I.col(0), I.col(2))),
        ("类4 M=diag(1,1,1,2), A12 秩1, D=span{e2,e3}",
         sp.diag(1, 1, 1, 2), A12r1, sp.Matrix.hstack(I.col(1), I.col(2))),
        ("类10 M=diag(1,1,2,3), D=span{e1+e2,e3}", sp.diag(1, 1, 2, 3), z,
         sp.Matrix.hstack(I.col(0) + I.col(1), I.col(2))),
    ]
    for tag, M, A12, Dk in cases:
        A, C, N, k, G, A21 = build(M, A12)
        run(tag, A, C, N, k, G, A21, Dk, q_target=3)


if __name__ == "__main__":
    main()
