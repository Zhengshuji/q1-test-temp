"""c393 — c=1 但 (S2) 不成立的可行设计存在吗？（论文判定程序完备性的关键）

构造：n=8, k=4, M=diag(1,1,2,3)（K0 块替换后的 4242 实例）。
取 1 维 D <= K0，V <= D^perp ∩ (AD)^perp 且 V ∩ K0 = 0、dim(K0 ∩ V^perp) = 1（即 omega = k-1 = 3）。
检查 (5a) 与 (5b)（极大子式 gcd），看是否存在这样的**可行**设计。

若存在，则论文的"V ⊇ D_v"参数化只覆盖 c=1 层的一个子族，判定程序的完备性需要额外论证。
"""

import itertools
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import c335_lambda_movement as m  # noqa: E402
import c352_number_field_decider as d  # noqa: E402

A, C = d.build_instance(4242)
A = sp.Matrix(A)
B = sp.diag(1, 1, 2, 3)
for i in range(4):
    for j in range(4):
        A[4 + i, 4 + j] = B[i, j]
W = sp.Matrix.vstack(C, C * A)
N = m.ker_basis(W)
k = N.cols
n = A.rows
G = N.T * N
M = sp.simplify(sp.Matrix(G.inv() * (N.T * A * N)))
lam = sp.symbols("lam")
print(f"k={k}, n={n}, M=diag(1,1,2,3)")

I = sp.eye(k)
found = 0
for j in range(k):
    D = I.col(j)                     # 1 维 D <= K0（K 坐标）
    ND = N * D
    AD = A * ND
    # 候选 V：在 D^perp ∩ (AD)^perp 中取 3 维，且 V ∩ K0 = 0
    U = sp.Matrix.hstack(ND, AD)
    basis = U.T.nullspace()          # D^perp ∩ (AD)^perp 的基
    if len(basis) < 3:
        continue
    # 从基里枚举三元组
    for combo in itertools.combinations(range(len(basis)), 3):
        Vm = sp.Matrix.hstack(*[basis[t] for t in combo])
        if Vm.rank() < 3:
            continue
        # V ∩ K0 = 0 ⟺ rank[Vm; N^T] = 3 + 4
        if sp.Matrix.vstack(Vm.T, N.T).rank() != 3 + k:
            continue
        L = Vm.T                          # 3 行，行空间 = V
        H = L * N
        if H.rank() != k - 1:
            continue
        HA = L * A * N
        # (5a)
        if not (HA * m.ker_basis(H)).is_zero_matrix:
            continue
        # (5b): omega = k-1 = 3 阶极大子式的 gcd
        om = k - 1
        P = sp.Matrix(L.rows, k, lambda i, j: lam * H[i, j] - HA[i, j])
        polys = []
        for rs in itertools.combinations(range(L.rows), om):
            for cs in itertools.combinations(range(k), om):
                det = sp.expand(P.extract(list(rs), list(cs)).det())
                if sp.simplify(det) != 0:
                    polys.append(det)
        if not polys:
            continue
        gg = polys[0]
        for pp in polys[1:]:
            gg = sp.gcd(gg, pp)
        dg = sp.degree(gg, lam)
        if dg == 0:
            found += 1
            print(f"  ** 可行且 (S2) 不成立：D = e{j+1}，V 由基 {combo} 张成")
            print(f"     (5a)=True, gcd 次数 = 0, V∩K0 = 0, dim D_v = k-1 = {om}")
            if found >= 2:
                break
    if found >= 2:
        break
print(f"共找到 {found} 个")
