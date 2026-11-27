"""c396 — 层可行性：同一阶 q 下，不同 c 的层能否分别可行？（层单调性的经验检验）

实例：4242，K0 上块换成 diag(1,1,2,3)；n=8, k=4, M=diag(1,1,2,3)。

构造（c394 的推广）：
  取 D <= K0（dim c），U = D + A D，V = U^perp（dim q = 8 - dim U）。
  逐 D 检查：(5a) [AD ⟂ V]、精确核 [K ∩ V^perp = D]、以及 (5b) [omega 阶极大子式的 gcd = 1]。

对 c=1 与 c=2 各枚举候选 D，报告可行的那些，从而看同一 q 下层的可行性。
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


def build():
    A, C = d.build_instance(4242)
    A = sp.Matrix(A)
    for i in range(4):
        for j in range(4):
            A[4 + i, 4 + j] = sp.diag(1, 1, 2, 3)[i, j]
    N = m.ker_basis(sp.Matrix.vstack(C, C * A))
    k = N.cols
    n = A.rows
    G = N.T * N
    M = sp.simplify(sp.Matrix(G.inv() * (N.T * A * N)))
    return A, C, N, M, k, n, G


def gcd_deg(H, HA, om):
    q, k = H.rows, H.cols
    P = sp.Matrix(q, k, lambda i, j: lam * H[i, j] - HA[i, j])
    polys = []
    for rs in itertools.combinations(range(q), om):
        for cs in itertools.combinations(range(k), om):
            det = sp.expand(P.extract(list(rs), list(cs)).det())
            if sp.simplify(det) != 0:
                polys.append(det)
    if not polys:
        return None
    gg = polys[0]
    for pp in polys[1:]:
        gg = sp.gcd(gg, pp)
    return sp.degree(sp.simplify(gg), lam)


def analyse(A, N, k, n, DK):
    D = sp.Matrix.hstack(*DK)
    c = D.cols
    ND = N * D
    AD = A * ND
    U = sp.Matrix.hstack(ND, AD)
    V = U.T.nullspace()
    Vm = sp.Matrix.hstack(*V) if V else sp.zeros(n, 0)
    q = Vm.cols
    exact = (k + U.rank() - sp.Matrix.hstack(N, U).rank()) == c
    H = Vm.T * N
    HA = Vm.T * A * N
    om = H.rank()
    ok5a = (Vm.T * AD).is_zero_matrix
    dg = gcd_deg(H, HA, om) if om > 0 else None
    return dict(c=c, q=q, exact=exact, ok5a=ok5a, om=om, gcd=dg)


def main() -> None:
    A, C, N, M, k, n, G = build()
    I = sp.eye(k)
    print(f"n={n}, k={k}, M=diag(1,1,2,3)")
    print()
    print("c=1 的候选 D（坐标轴 + 若干组合）与 c=2 的候选 D：")
    cands = {}
    for j in range(k):
        cands[f"c1: e{j+1}"] = [I.col(j)]
    for i, j in itertools.combinations(range(k), 2):
        cands[f"c2: e{i+1},e{j+1}"] = [I.col(i), I.col(j)]
    rows = []
    for tag, DK in cands.items():
        res = analyse(A, N, k, n, DK)
        rows.append((tag, res))
        flag = ""
        if res["ok5a"] and res["exact"] and res["gcd"] == 0:
            flag = "  <= 可行"
        print(f"  {tag:22s} q={res['q']}  exact={res['exact']}  (5a)={res['ok5a']}  "
              f"omega={res['om']}  gcd次数={res['gcd']}{flag}")
    print()
    print("=== 汇总：按 c 分组的可行数 ===")
    for c in (1, 2):
        feas = [t for t, r in rows if r["c"] == c and r["ok5a"] and r["exact"] and r["gcd"] == 0]
        print(f"  c={c}: 可行 {len(feas)} 个 / 候选 {sum(1 for t, r in rows if r['c'] == c)} 个")
        for t in feas:
            print(f"       {t}")


if __name__ == "__main__":
    main()
