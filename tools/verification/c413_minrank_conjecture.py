"""c413 — Q-B 检验：固定 D 的可行性是否等价于"铅笔最低秩"的维数比较？

猜想（$\Phi_0=0$ 情形）：固定 D 时
  存在 t 维 W 使 (5b) 成立  <=>  omega - min_λ rank P_D(λ)  <=  min(t, dim φ(T_D))，
其中 min 取遍 λ ∈ C（铅笔在复域上的最低秩）。

理由：铅笔行空间 = R_λ + Φ ⊆ D°，(5b) <=> R_λ + Φ = D° ∀λ；
对固定 λ，"Φ 与 R_λ 横截"在 Gr(j, D°) 中是**开稠密**的（维数够时非空），
有限个 λ 的交仍非空 => 存在 Φ；故只需维数条件。

本脚本对四个实例算 omega、min rank、t、dim φ(T_D)，并给出猜想预测 vs 实测结论。
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


def build(block_diag, with_A12_rank1=False):
    A, C = d.build_instance(4242)
    A = sp.Matrix(A)
    if with_A12_rank1:
        # 用 c402 的 fixture：C=[C1 0]，A=[[A11,A12],[A12,M]]，A12=u v^T 秩 1
        C1 = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0]])
        C = sp.Matrix.hstack(C1, sp.zeros(2, 4))
        A11 = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]])
        u = sp.Matrix([0, 0, 1, 0])
        v = sp.Matrix([1, 0, 0, 0])
        A12 = u * v.T
        A = sp.Matrix.vstack(sp.Matrix.hstack(A11, A12), sp.Matrix.hstack(A12, block_diag))
    else:
        for i in range(4):
            for j in range(4):
                A[4 + i, 4 + j] = block_diag[i, j]
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    k = N.cols
    G = N.T * N
    Proj = sp.eye(A.rows) - N * sp.Matrix(G.inv()) * N.T
    A21 = sp.simplify(Proj * A * N)
    return A, N, k, G, A21


def min_rank(P, om, k):
    """铅笔 P(lam) 在 C 上的最低秩：先算 omega 阶子式的 gcd；若为常数则最低秩 = omega。"""
    H = sp.Matrix([[P[i, j].coeff(lam, 1) for j in range(k)] for i in range(P.rows)])
    if H.rank() != om:
        return None, None
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
    deg = sp.degree(gg, lam)
    if deg == 0:
        return om, deg
    # 在 gg 的根上找最低秩（数值）
    best = om
    for r in sp.nroots(gg, n=30):
        Pr = sp.Matrix(P.rows, k, lambda i, j: complex(P[i, j].subs(lam, r).evalf(30)))
        # 数值秩：用奇异值
        import numpy as np
        M = np.array(Pr.tolist(), dtype=complex)
        sv = np.linalg.svd(M, compute_uv=False)
        tol = max(M.shape) * (sv[0] if len(sv) else 0) * 1e-12
        rk = int((sv > tol).sum())
        best = min(best, rk)
    return best, deg


def main() -> None:
    cases = [
        ("类10 4242 变体 M=diag(1,1,2,3), D=span{e1+e2,e3}, t=1",
         sp.diag(1, 1, 2, 3), False, sp.Matrix.hstack(sp.eye(4).col(0) + sp.eye(4).col(1), sp.eye(4).col(2)), 1),
        ("类9 4242 变体 c=1, D=span{e1}, t=0",
         sp.diag(1, 1, 2, 3), False, sp.Matrix(sp.eye(4).col(0)), 0),
        ("类4 r=1: M=diag(1,1,1,2), A12 秩1, D=span{e1,e3}, t=1",
         sp.diag(1, 1, 1, 2), True, sp.Matrix.hstack(sp.eye(4).col(0), sp.eye(4).col(2)), 1),
        ("类4 r=0: 同上, D=span{e2,e3}, t=1",
         sp.diag(1, 1, 1, 2), True, sp.Matrix.hstack(sp.eye(4).col(1), sp.eye(4).col(2)), 1),
    ]
    for tag, M, rank1, Dk, t in cases:
        A, N, k, G, A21 = build(M, rank1)
        comp = [sp.simplify(x) for x in (Dk.T * G).nullspace()]
        P = [sp.simplify(N * x) for x in comp]
        Vm = sp.Matrix.hstack(*P)
        H = sp.simplify(Vm.T * N)
        HA = sp.simplify(Vm.T * A * N)
        om = H.rank()
        Pl = sp.Matrix(Vm.cols, k, lambda i, j: lam * H[i, j] - HA[i, j])
        TDb = sp.Matrix.vstack(N.T, (A21 * Dk).T).nullspace()
        dimTD = len(TDb)
        # dim phi(T_D)
        phis = [sp.Matrix(sp.Matrix(x).T * A21) for x in TDb]
        dimVphi = sp.Matrix.vstack(*phis).rank() if phis else 0
        mr, gdeg = min_rank(Pl, om, k)
        pred = "可行" if (om - mr) <= min(t, dimVphi) else "不可行"
        print(f"{tag}")
        print(f"   omega={om}, dim T_D={dimTD}, dim phi(T_D)={dimVphi}, t={t}, "
              f"gcd 次数={gdeg}, min rank={mr}")
        print(f"   猜想预测：omega - minrank = {om - mr} vs min(t, dimφ) = {min(t, dimVphi)} "
              f"=> {pred}")
        print()


if __name__ == "__main__":
    main()
