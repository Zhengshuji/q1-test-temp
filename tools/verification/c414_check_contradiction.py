"""c414 — 复核 c411 与 c413 的矛盾实例：M=diag(1,1,1,2)、A12=uv^T、D=span{e1,e3}。

比较：设计铅笔（含 W 行）与 D 部分铅笔 $P_D$ 的 gcd 与最小秩；并核对 φ(T_D) 是否为零。
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

lam = sp.symbols("lam")


def gcd_info(P, om, k, tag):
    polys = []
    for rs in itertools.combinations(range(P.rows), om):
        for cs in itertools.combinations(range(k), om):
            det = sp.expand(P.extract(list(rs), list(cs)).det())
            if sp.simplify(det) != 0:
                polys.append(det)
    gg = polys[0]
    for pp in polys[1:]:
        gg = sp.gcd(gg, pp)
    gg = sp.simplify(gg)
    print(f"   {tag}: 非零 {om} 阶子式 {len(polys)} 个；gcd = {sp.sstr(sp.factor(gg))}"
          f"（次数 {sp.degree(gg, lam)}）")
    return gg


def main() -> None:
    C1 = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0]])
    C = sp.Matrix.hstack(C1, sp.zeros(2, 4))
    A11 = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]])
    u = sp.Matrix([0, 0, 1, 0])
    v = sp.Matrix([1, 0, 0, 0])
    A12 = u * v.T
    M = sp.diag(1, 1, 1, 2)
    A = sp.Matrix.vstack(sp.Matrix.hstack(A11, A12), sp.Matrix.hstack(A12, M))
    Wm = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(Wm)
    k = N.cols
    G = N.T * N
    Proj = sp.eye(8) - N * sp.Matrix(G.inv()) * N.T
    A21 = sp.simplify(Proj * A * N)
    print(f"k={k}, rank[C;CA]={Wm.rank()}")
    print(f"A21 = {A21.tolist()}")
    I = sp.eye(k)
    for nm, Dk in (("D=span{e1,e3}", sp.Matrix.hstack(I.col(0), I.col(2))),
                   ("D=span{e2,e3}", sp.Matrix.hstack(I.col(1), I.col(2)))):
        comp = [sp.simplify(x) for x in (Dk.T * G).nullspace()]
        P = [sp.simplify(N * x) for x in comp]
        Vm = sp.Matrix.hstack(*P)
        H = sp.simplify(Vm.T * N)
        HA = sp.simplify(Vm.T * A * N)
        om = H.rank()
        TDb = sp.Matrix.vstack(N.T, (A21 * Dk).T).nullspace()
        phis = [sp.Matrix(sp.Matrix(x).T * A21) for x in TDb]
        dimVphi = sp.Matrix.vstack(*phis).rank() if phis else 0
        print(f"\n{nm}: omega={om}, dim T_D={len(TDb)}, dim phi(T_D)={dimVphi}, "
              f"r(D)={sp.Matrix(A21*Dk).rank()}")
        # D 部分铅笔
        Pl = sp.Matrix(Vm.cols, k, lambda i, j: lam * H[i, j] - HA[i, j])
        g1 = gcd_info(Pl, om, k, "D 部分铅笔")
        # 加一行 Φ（取 φ(T_D) 的一个非零行，若有）
        if dimVphi > 0:
            phi = phis[0]
            for x in phis:
                if sp.Matrix(x).rank() > 0:
                    phi = sp.Matrix(x)
                    break
            Vfull = sp.Matrix.hstack(Vm, sp.zeros(8, 1))
            # 注意：Φ 行不是 V 的行，而是 H_A 的额外行；直接构造扩充铅笔
            P2 = sp.Matrix.vstack(Pl, -phi)
            print(f"   取 Φ 行 = {phi.tolist()}")
            gcd_info(P2, om, k, "加一行 Φ 后")
        else:
            print("   phi(T_D) = 0 => 任何 W 都给 Φ=0，设计铅笔 = D 部分铅笔")


if __name__ == "__main__":
    main()
