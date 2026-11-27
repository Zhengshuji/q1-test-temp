"""c392 — 三个量的区分：rho、c_old = dim(V ∩ K0^⊥)、c_new = dim(K0 ∩ V^⊥)、dim(V ∩ K0)。

旧框架：J = row[C;CA] = K0^⊥，c_old = dim(V ∩ J)，rho = dim pi_K0(V)，q = rho + c_old。
新框架（压缩）：omega = rank(LN)，c_new = k - omega = dim(K0 ∩ V^⊥)。
论文：c = k - omega（= c_new）；但论文另外断言 omega = dim(V ∩ K0)。
本脚本用精确算术把这些量都算出来对比。
"""

import os
import random
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import c335_lambda_movement as m  # noqa: E402
import c352_number_field_decider as d  # noqa: E402


def main() -> None:
    A, C = d.build_instance(4242)
    A = sp.Matrix(A)
    n = A.rows
    N = m.ker_basis(sp.Matrix.vstack(C, C * A))
    k = N.cols
    # K0^perp 的基：J = row[C;CA] 的行
    J = sp.Matrix.vstack(C, C * A)
    G = N.T * N
    P = N * sp.Matrix(G.inv()) * N.T          # 到 K0 的正交投影
    print(f"n={n}, k={k}, dim J = {J.rank()} (应 = n-k = {n-k})")
    print()
    print(" q | rank H | c_new=k-rankH | rho | c_old=q-rho | dim(V∩K0) | dim(V∩K0^⊥)")
    print("---+--------+---------------+-----+-------------+-----------+------------")
    random.seed(7)
    for q in (3, 4, 5, 6):
        for t in range(3):
            L = sp.Matrix([[random.randint(-2, 2) for _ in range(n)] for _ in range(q)])
            if L.rank() < q:
                continue
            H = L * N
            rH = H.rank()
            c_new = k - rH
            rho = sp.Matrix(P * L.T).rank()          # dim pi_K0(V)
            c_old = q - rho
            dimVK0 = q + k - sp.Matrix.vstack(L, N.T).rank()
            # dim(V ∩ K0^⊥) = q - rho
            print(f" {q} |   {rH}    |      {c_new}        |  {rho}  |      {c_old}      |     {dimVK0}     |     {q-rho}")
        print("---+--------+---------------+-----+-------------+-----------+------------")


if __name__ == "__main__":
    main()
