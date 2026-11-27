"""c402 — 可控实例：A21 秩 1，使 Gr(2,E1) 同时含 r=0 与 r=1 两层。

构造（K0 = span{e5..e8}、K0^perp = span{e1..e4}）：
  C  = [C1 0]，C1 = [[1,0,0,0],[0,1,0,0]]（2x4 秩 2）
  A  = [[A11, A12], [A21b, M]]，其中
       A11 让 rank[C1; C1 A11] = 4（取一般位置）
       A12 = u v^T（秩 1），u ∈ ker C1 ⟹ C1 A12 = 0 ⟹ K0 = span{e5..e8}
       M   = diag(1,1,1,2)（故 E1 = span{e1,e2,e3} 是 3 维）
  A21 = pi_{K0^perp} A |_{K0} = A12（秩 1）

于是 Gr(2,E1) 上：r(D) = 1 当 D 不在 ker(v^T) ∩ E1 里，否则 r(D) = 0。
两层都非空。对每层采样，算 omega 与 gcd 次数。
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

lam = sp.symbols("lam")


def build():
    C1 = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0]])
    C = sp.Matrix.hstack(C1, sp.zeros(2, 4))
    A11 = sp.Matrix([[0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 1, 0, 0]])
    u = sp.Matrix([0, 0, 1, 0])          # u ∈ ker C1
    v = sp.Matrix([1, 0, 0, 0])
    A12 = u * v.T                        # 秩 1，列落在 ker C1
    M = sp.diag(1, 1, 1, 2)
    A = sp.Matrix.vstack(
        sp.Matrix.hstack(A11, A12),
        sp.Matrix.hstack(A12, M),        # A21b 也取 A12 使 A 对称，便于检查
    )
    return A, C, A12, M


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
    A, C, A12, M = build()
    n = A.rows
    W = sp.Matrix.vstack(C, C * A)
    N = m.ker_basis(W)
    k = N.cols
    G = N.T * N
    print(f"n={n}, k={k}（应 4）")
    print("N 的列（K0 的基）：", N.tolist())
    print("rank[C;CA] =", W.rank(), "（应 4）")
    Mc = sp.simplify(sp.Matrix(G.inv() * (N.T * A * N)))
    print("压缩 M =", Mc.tolist())
    Proj = sp.eye(n) - N * sp.Matrix(G.inv()) * N.T
    A21 = sp.simplify(Proj * A * N)
    print("A21 的秩 =", A21.rank(), "（应 1）")
    print()
    E1 = [sp.Matrix(sp.eye(k).col(0)), sp.Matrix(sp.eye(k).col(1)), sp.Matrix(sp.eye(k).col(2))]
    rng = random.Random(5)
    print("采样 D ∈ Gr(2,E1)，W ⊆ T_D（1 维）：")
    outcomes = {}
    for trial in range(20):
        co = [rng.randint(-2, 2) for _ in range(6)]
        v1 = E1[0] * co[0] + E1[1] * co[1] + E1[2] * co[2]
        v2 = E1[0] * co[3] + E1[1] * co[4] + E1[2] * co[5]
        Dk = sp.Matrix.hstack(v1, v2)
        if Dk.rank() < 2:
            continue
        comp = [sp.simplify(x) for x in (Dk.T * G).nullspace()]
        r = sp.Matrix(A21 * Dk).rank()
        TD = sp.Matrix.vstack(N.T, (A21 * Dk).T).nullspace()
        if not TD:
            continue
        coef = [rng.randint(-2, 2) for _ in TD]
        w = sum((c * t for c, t in zip(coef, TD)), sp.zeros(n, 1))
        V = [sp.simplify(N * x) for x in comp] + [sp.Matrix(w)]
        Vm = sp.Matrix.hstack(*V)
        if Vm.rank() != 3:
            continue
        om, dg = gcd_deg(Vm, N, A, k)
        outcomes.setdefault((r, om, dg), 0)
        outcomes[(r, om, dg)] += 1
        print(f"  trial {trial:2d}: r={r} dim T_D={len(TD)} omega={om} gcd次数={dg}")
    print()
    print("汇总 (r, omega, gcd) -> 次数：")
    for key, cnt in sorted(outcomes.items(), key=lambda kv: str(kv[0])):
        print(f"   {key}: {cnt}")


if __name__ == "__main__":
    main()
