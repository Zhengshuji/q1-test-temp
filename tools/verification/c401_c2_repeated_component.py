"""c401 — c=2 的重根分量：可行性是否随 D 变化？

构造实例：K0 块换成 diag(1,1,1,2)（k=4），故 E_1 是 3 维、Gr(2,E_1) 是 2 维（P^2 型）。
取 c=2、t=1、q=3：D ∈ Gr(2,E_1)（2-参数），W ⊆ T_D（dim 2-r），dim W = 1。
随机采样 (D, W)，算 omega 与 gcd 次数，看结论是否随 D 变。

若 gcd 次数随 D 变化 => 分量内的"坏轨迹"是**真子集** => "逐分量一次判定"不成立，
需要像 c=1 那样在分量内再分层（这正是 c=1 论文 eigen/non-eigen 二分的推广）。
"""

from __future__ import annotations

import itertools
import os
import random
import sys

import sympy as sp

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)

import c335_lambda_movement as m  # noqa: E402
import c352_number_field_decider as d  # noqa: E402

lam = sp.symbols("lam")


def build():
    A, C = d.build_instance(4242)
    A = sp.Matrix(A)
    for i in range(4):
        for j in range(4):
            A[4 + i, 4 + j] = sp.diag(1, 1, 1, 2)[i, j]
    N = m.ker_basis(sp.Matrix.vstack(C, C * A))
    k = N.cols
    n = A.rows
    G = N.T * N
    M = sp.simplify(sp.Matrix(G.inv() * (N.T * A * N)))
    Proj = sp.eye(n) - N * sp.Matrix(G.inv()) * N.T
    A21 = sp.simplify(Proj * A * N)
    return A, N, M, A21, k, n, G


def gcd_deg(Vm, N, A, k):
    H = Vm.T * N
    om = H.rank()
    if om == 0:
        return om, None
    HA = Vm.T * A * N
    P = sp.Matrix(Vm.cols, k, lambda i, j: lam * H[i, j] - HA[i, j])
    polys = []
    for rs in itertools.combinations(range(Vm.cols), om):
        for cs in itertools.combinations(range(k), om):
            det = sp.expand(P.extract(list(rs), list(cs)).det())
            if sp.simplify(det) != 0:
                polys.append(det)
    if not polys:
        return om, None
    gg = polys[0]
    for pp in polys[1:]:
        gg = sp.gcd(gg, pp)
    return om, sp.degree(sp.simplify(gg), lam)


def main() -> None:
    A, N, M, A21, k, n, G = build()
    print(f"n={n}, k={k}, M = {M.tolist()}")
    rng = random.Random(11)
    E1 = [sp.Matrix(sp.eye(k).col(0)), sp.Matrix(sp.eye(k).col(1)), sp.Matrix(sp.eye(k).col(2))]
    print()
    print("采样（D ∈ Gr(2,E_1)，W ⊆ T_D，dim W = 1）：")
    outcomes = {}
    for trial in range(12):
        a = rng.randint(-2, 2)
        b = rng.randint(-2, 2)
        c = rng.randint(-2, 2)
        v1 = E1[0] * a + E1[1] * b + E1[2] * c
        a2 = rng.randint(-2, 2)
        b2 = rng.randint(-2, 2)
        c2 = rng.randint(-2, 2)
        v2 = E1[0] * a2 + E1[1] * b2 + E1[2] * c2
        Dk = sp.Matrix.hstack(v1, v2)
        if Dk.rank() < 2:
            continue
        comp = [sp.simplify(x) for x in (Dk.T * G).nullspace()]
        TD = sp.Matrix.vstack(N.T, (A21 * Dk).T).nullspace()
        r = sp.Matrix(A21 * Dk).rank()
        if not TD:
            continue
        # 取 T_D 的一个随机 1 维子空间
        coefs = [rng.randint(-2, 2) for _ in TD]
        w = sum((co * t for co, t in zip(coefs, TD)), sp.zeros(n, 1))
        V = [sp.simplify(N * x) for x in comp] + [sp.Matrix(w)]
        Vm = sp.Matrix.hstack(*V)
        if Vm.rank() != 3:
            continue
        om, dg = gcd_deg(Vm, N, A, k)
        key = (r, om, dg)
        outcomes[key] = outcomes.get(key, 0) + 1
        print(f"  trial {trial:2d}: D 由 {v1.T.tolist()} 与 {v2.T.tolist()} 张成; r={r}, omega={om}, gcd次数={dg}")
    print()
    print("汇总 (r, omega, gcd次数) -> 命中次数：")
    for key, cnt in sorted(outcomes.items(), key=lambda kv: str(kv[0])):
        print(f"   {key}: {cnt}")


if __name__ == "__main__":
    main()
