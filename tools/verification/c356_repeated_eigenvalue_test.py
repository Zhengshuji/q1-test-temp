"""c356 -- 重特征值实例：同一特征空间里不同方向给出不同结论（attempts/376）。

构造：4242 的 A，把 K0 上的块换成 diag(1,1,2,3) => 压缩 = diag(1,1,2,3)，E_1 是 2 维。
对 6 个方向算纤维 generic gcd：有的 0（生成好），有的 2（全坏）。
因此"每个特征值取一个特征向量"会给出错误结论。
"""

import sys, itertools
sys.path.insert(0, "tools/verification")
from fractions import Fraction as F
import sympy as sp
import c335_lambda_movement as m
import c352_number_field_decider as d
import c354_generic_gcd_nf as g
import c355_rf_gcd as rf
from nf import NF, mat_nullspace

A, C = d.build_instance(4242)
A2 = sp.Matrix(A)
B = sp.diag(1, 1, 2, 3)
for i in range(4):
    for j in range(4):
        A2[4 + i, 4 + j] = B[i, j]
W = sp.Matrix.vstack(C, C * A2)
N = m.ker_basis(W)
n = A2.rows
G = N.T * N
M = G.inv() * (N.T * A2 * N)


def fibre_deg(A, N, v, Fq):
    """给定 v，返回该纤维 generic gcd 的 lambda 次数（-1 表示构造失败）。"""
    polys = g.fibre_polys(A, N, v, Fq, None)
    if not polys:
        return -1
    P = [[rf.RF(cc) for cc in Pi] for Pi in polys]
    P = [rf.poly_trim_rf(Q) for Q in P]
    P = [Q for Q in P if rf.poly_deg_rf(Q) >= 0]
    if not P:
        return -1
    gg = P[0]
    for Q in P[1:]:
        gg = rf.poly_gcd_rf(gg, Q)
        if rf.poly_deg_rf(gg) == 0:
            break
    return rf.poly_deg_rf(gg)


Fq = NF([-1, 1])
rf.Fq_one = (Fq,)

mu = Fq.elt(F(1))
Mf = []
for i in range(4):
    row = []
    for j in range(4):
        r = sp.Rational(M[i, j])
        row.append(Fq.elt(F(r.p, r.q)))
    Mf.append(row)
rows = [[Fq.sub(Mf[i][j], mu) if i == j else Mf[i][j] for j in range(4)] for i in range(4)]
ns = mat_nullspace(Fq, rows)
print("E_1 维数 =", len(ns))

for (a, b) in [(1, 0), (0, 1), (1, 1), (1, 2), (2, -1), (3, 1)]:
    c = [Fq.elt(F(a)), Fq.elt(F(b)), Fq.zero(), Fq.zero()]
    v = [Fq.zero() for _ in range(n)]
    for j in range(4):
        if Fq.is_zero(c[j]):
            continue
        for i in range(n):
            if N[i, j] != 0:
                v[i] = Fq.add(v[i], Fq.mul(Fq.elt(F(int(N[i, j]))), c[j]))
    dg = fibre_deg(A2, N, v, Fq)
    print(f"方向 ({a},{b}): 纤维 gcd 次数 = {dg}" + ("  => 生成好" if dg == 0 else ""))
