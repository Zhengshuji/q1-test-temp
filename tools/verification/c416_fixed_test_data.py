"""c416 — 六类测试数据的**修正版**：每个实例用正确的 A，W 一律取在 T_D 内，逐项断言。

要点（c411 的错误）：
  * c411 对 A21≠0 的实例用了固定 W，可能不在 T_D 里 => (5a) 失败 => 设计无效；
  * c411 的 4242 变体把 A 的右上块也清零了，改了实例本身。
本脚本：4242 变体只替换 K0 块（保持右上块原样）；块状 fixture 用于类 1–4；
W 从 T_D 的基向量与两两组合里选，报告"是否存在 gcd=0 的 W"。
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


def as_col(t, n=8):
    M = sp.Matrix(t)
    if M.shape == (n, 1):
        return M
    if M.shape == (1, n):
        return M.T
    return M.reshape(n, 1)


def inst_4242(Mblk):
    """4242 的 A、C，只把 K0 块（右下 4x4）换成 Mblk。"""
    A, C = d.build_instance(4242)
    A = sp.Matrix(A)
    for i in range(4):
        for j in range(4):
            A[4 + i, 4 + j] = Mblk[i, j]
    return A, sp.Matrix(C)


def inst_block(Mblk, A12):
    C1 = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0]])
    C = sp.Matrix.hstack(C1, sp.zeros(2, 4))
    A11 = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]])
    A = sp.Matrix.vstack(sp.Matrix.hstack(A11, A12), sp.Matrix.hstack(A12, Mblk))
    return A, C


def analyse(tag, A, C, Dk, q=None):
    Wm0 = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(Wm0)
    k = N.cols
    G = N.T * N
    Proj = sp.eye(8) - N * sp.Matrix(G.inv()) * N.T
    A21 = sp.simplify(Proj * A * N)
    comp = [sp.simplify(x) for x in (Dk.T * G).nullspace()]
    TD = [as_col(t) for t in sp.Matrix.vstack(N.T, (A21 * Dk).T).nullspace()]
    print(f"{tag}")
    print(f"   k={k}, dim D={Dk.cols}, r(D)={sp.Matrix(A21*Dk).rank()}, dim T_D={len(TD)}, "
          f"rank phi(T_D)={sp.Matrix.vstack(*[sp.Matrix(x).T*A21 for x in TD]).rank() if TD else 0}")
    found = []
    # 候选 W：T_D 的基向量 + 两两组合（若 t=1 只用基向量）
    cands = [(f"e{i}", [TD[i]]) for i in range(len(TD))]
    for i, j in itertools.combinations(range(len(TD)), 2):
        cands.append((f"e{i}+e{j}", [TD[i], TD[j]]))
    for nm, Wc in cands:
        t = len(Wc)
        V = [sp.simplify(N * x) for x in comp] + [sp.Matrix(w) for w in Wc]
        Vm = sp.Matrix.hstack(*V)
        H = sp.simplify(Vm.T * N)
        HA = sp.simplify(Vm.T * A * N)
        om = H.rank()
        AD = A * (N * Dk)
        ok5a = (Vm.T * AD).is_zero_matrix
        exact = (k + Vm.rank() - sp.Matrix.hstack(N, Vm).rank()) == Dk.cols
        if not (ok5a and exact):
            continue
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
        found.append((nm, Vm.rank(), om, dg))
    if found:
        feasible = [f for f in found if f[3] == 0]
        for nm, qv, om, dg in found:
            print(f"   W={nm}: q={qv}, omega={om}, gcd次数={dg}")
        print(f"   => {'存在可行的 W' if feasible else '所有候选 W 都不可行'}")
    else:
        print("   （无有效候选）")
    print()


def main() -> None:
    I = sp.eye(4)
    z = sp.zeros(4, 4)
    u = sp.Matrix([0, 0, 1, 0])
    v = sp.Matrix([1, 0, 0, 0])
    A12r1 = u * v.T
    R = sp.Matrix([[0, -1, 0, 0], [1, 0, 0, 0], [0, 0, 2, 0], [0, 0, 0, 3]])

    A, C = inst_block(sp.diag(1, 2, 3, 4), z)
    analyse("类1 块状 fixture M=diag(1,2,3,4), D=span{e1,e2}", A, C,
            sp.Matrix.hstack(I.col(0), I.col(1)))
    A, C = inst_block(R, z)
    analyse("类2 块状 fixture M=diag(R,2,3), D=ker(M^2+I)", A, C,
            sp.Matrix.hstack(I.col(0), I.col(1)))
    A, C = inst_block(sp.diag(1, 1, 1, 2), A12r1)
    analyse("类4a 块状 M=diag(1,1,1,2), A12 秩1, D=span{e1,e3}", A, C,
            sp.Matrix.hstack(I.col(0), I.col(2)))
    analyse("类4b 同上, D=span{e2,e3}", A, C, sp.Matrix.hstack(I.col(1), I.col(2)))

    A, C = inst_4242(sp.diag(1, 1, 2, 3))
    analyse("类3/10 4242 变体 M=diag(1,1,2,3), D=span{e1+e2,e3}", A, C,
            sp.Matrix.hstack(I.col(0) + I.col(1), I.col(2)))
    analyse("类3 4242 变体, D=span{e1,e2}", A, C, sp.Matrix.hstack(I.col(0), I.col(1)))
    analyse("类9 4242 变体 c=1, D=span{e1}", A, C, sp.Matrix(I.col(0)))


if __name__ == "__main__":
    main()
