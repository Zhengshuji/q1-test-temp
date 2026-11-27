"""c409 — 核对 408 引理 2：在 W 的 P¹ 图卡上铅笔子式的 s-次数。

取 c406 的实例与 D，T_D 维 3；取 W(s) = span{w0 + s w1}（P(T_D) 的一张卡），
算 H(s)、H_A(s) 与全部 2 阶子式的 s-次数、lambda-次数、以及 gcd 次数是否随 s 变。
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
s = sp.symbols("s")


def build():
    A, C = d.build_instance(4242)
    A = sp.Matrix(A)
    for i in range(4):
        for j in range(4):
            A[4 + i, 4 + j] = sp.diag(1, 1, 2, 3)[i, j]
    N = m.ker_basis(sp.Matrix.vstack(C, C * A))
    k = N.cols
    G = N.T * N
    Proj = sp.eye(A.rows) - N * sp.Matrix(G.inv()) * N.T
    A21 = sp.simplify(Proj * A * N)
    return A, N, k, G, A21


def as_col(t, n):
    M = sp.Matrix(t)
    if M.shape == (n, 1):
        return M
    if M.shape == (1, n):
        return M.T
    return M.reshape(n, 1)


def main() -> None:
    A, N, k, G, A21 = build()
    n = A.rows
    I = sp.eye(k)
    Dk = sp.Matrix.hstack(I.col(0) + I.col(1), I.col(2))
    comp = [sp.simplify(x) for x in (Dk.T * G).nullspace()]
    TD = [as_col(t, n) for t in sp.Matrix.vstack(N.T, (A21 * Dk).T).nullspace()]
    print(f"n={n}, k={k}, dim T_D = {len(TD)}")
    w0 = TD[0]
    # 选 w1 使 phi_{w1} != 0（否则沿 ker phi 退化，s 会消失）
    w1 = None
    for cand in TD:
        phi = sp.simplify(cand.T * A21)
        if phi != sp.zeros(1, k):
            w1 = cand
            break
    assert w1 is not None, "all TD lie in the kernel of phi"
    print(f"选 w1 使 phi_w1 != 0: {w1.T.tolist()}")
    W = sp.Matrix(w0 + s * w1)          # 列向量，分量是 s 的线性式
    print(f"W(s) 的分量（s 的线性式）: {W.T.tolist()}")
    V = [sp.simplify(N * x) for x in comp] + [W]
    Vm = sp.Matrix.hstack(*V)
    H = sp.simplify(Vm.T * N)
    HA = sp.simplify(Vm.T * A * N)
    print("H 与 s 无关？", all(sp.simplify(sp.diff(H[i, j], s)) == 0 for i in range(H.rows) for j in range(k)))
    print(f"max deg_s(HA) = {max(sp.degree(sp.expand(HA[i, j]), s) for i in range(HA.rows) for j in range(k))}")
    om = 2
    degs = []
    P = sp.Matrix(H.rows, k, lambda i, j: lam * H[i, j] - HA[i, j])
    polys = []
    for rs in itertools.combinations(range(H.rows), om):
        for cs in itertools.combinations(range(k), om):
            det = sp.expand(P.extract(list(rs), list(cs)).det())
            if sp.simplify(det) != 0:
                polys.append(det)
                degs.append((sp.degree(det, s), sp.degree(det, lam)))
    print(f"非零 {om} 阶子式个数 = {len(polys)}；各子式的 (deg_s, deg_lambda) = {degs}")
    gg = polys[0]
    for pp in polys[1:]:
        gg = sp.gcd(gg, pp)
    gg = sp.simplify(gg)
    print(f"gcd = {sp.sstr(sp.factor(gg))}；deg_lambda = {sp.degree(gg, lam)}；deg_s = {sp.degree(gg, s)}")


if __name__ == "__main__":
    main()
