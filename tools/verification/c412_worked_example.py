"""c412 — worked example 的全部数据（LaTeX 可直贴）。

实例：4242 的 A、C（n=8, p=2），K0 块换成 diag(1,1,2,3)。
设计：q=3、D=span{e1+e2, e3}（K 坐标）、W=(0,0,1,1,0,0,0,0)。
输出：A、C、N、M、A21、D、V、H、H_A、六个非零 2 阶子式、gcd 与 Bezout 恒等式、全部不变量。
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


def tex(M):
    M = sp.Matrix(M)
    rows = []
    for i in range(M.rows):
        rows.append(" & ".join(sp.latex(sp.simplify(M[i, j])) for j in range(M.cols)))
    return "\\begin{pmatrix}" + " \\\\ ".join(rows) + "\\end{pmatrix}"


def main() -> None:
    A, C = d.build_instance(4242)
    A = sp.Matrix(A)
    C = sp.Matrix(C)
    for i in range(4):
        for j in range(4):
            A[4 + i, 4 + j] = sp.diag(1, 1, 2, 3)[i, j]
    Wm = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(Wm)
    k = N.cols
    G = N.T * N
    M = sp.simplify(sp.Matrix(G.inv() * (N.T * A * N)))
    Proj = sp.eye(A.rows) - N * sp.Matrix(G.inv()) * N.T
    A21 = sp.simplify(Proj * A * N)
    print("% ==== A ====")
    print(tex(A))
    print("% ==== C ====")
    print(tex(C))
    print("% ==== [C;CA] 的秩 ====", Wm.rank(), "  k =", k)
    print("% ==== N（K0 的基）====")
    print(tex(N))
    print("% ==== M（压缩）====")
    print(tex(M))
    print("% ==== A21 ====")
    print(tex(A21))
    I = sp.eye(k)
    Dk = sp.Matrix.hstack(I.col(0) + I.col(1), I.col(2))
    print("% ==== D 的 K 坐标 ====")
    print(tex(Dk))
    comp = [sp.simplify(x) for x in (Dk.T * G).nullspace()]
    Wv = sp.Matrix([[0], [0], [1], [1], [0], [0], [0], [0]])
    V = [sp.simplify(N * x) for x in comp] + [Wv]
    Vm = sp.Matrix.hstack(*V)
    print("% ==== V 的基（环境坐标，列）====")
    print(tex(Vm))
    print("% dim V =", Vm.rank())
    H = sp.simplify(Vm.T * N)
    HA = sp.simplify(Vm.T * A * N)
    print("% ==== H ====")
    print(tex(H))
    print("% ==== H_A ====")
    print(tex(HA))
    om = H.rank()
    inter = k + Vm.rank() - sp.Matrix.hstack(N, Vm).rank()
    AD = A * (N * Dk)
    print(f"% omega = {om}, dim(K0 cap V^perp) = {inter}, dim D = {Dk.cols}, "
          f"(5a) = {(Vm.T * AD).is_zero_matrix}")
    P = sp.Matrix(Vm.cols, k, lambda i, j: lam * H[i, j] - HA[i, j])
    polys = []
    for rs in itertools.combinations(range(Vm.cols), om):
        for cs in itertools.combinations(range(k), om):
            det = sp.expand(P.extract(list(rs), list(cs)).det())
            if sp.simplify(det) != 0:
                polys.append(sp.factor(det))
    print("% ==== 非零 2 阶子式 ====")
    for pp in polys:
        print("%  ", sp.latex(pp))
    gg = polys[0]
    for pp in polys[1:]:
        gg = sp.gcd(gg, pp)
    print("% gcd =", sp.latex(sp.simplify(gg)), " 次数 =", sp.degree(sp.simplify(gg), lam))
    # Bezout：找 m3=lam-1 与 m5=lam-3
    cand = [p for p in polys if sp.simplify(p) != 0]
    print("% 子式的 (deg, lc)：", [(sp.degree(p, lam), sp.LC(sp.Poly(p, lam))) for p in cand])


if __name__ == "__main__":
    main()
