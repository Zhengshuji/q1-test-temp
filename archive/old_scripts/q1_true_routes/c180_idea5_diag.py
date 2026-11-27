"""c180_idea5_diag.py — IDEA5 靶子 A 的最小版本：A' = diag(mu_1..mu_d)

构造同 c161/c169：n=d+2, N=[I_d;0], C=e_n^T, A' 对角互异,
R0 = u (x) r（u=e_{d+1} 不在 K 里），A 前 d 列 = N A' + R0，后两列 = e_n；
L0 = r（于是 alpha0 = r ∈ V = <r>_{A'}）。

对不同的 r（不同 support）算 q_min，看是否随 support 组合变化。

用法：python q1_true/scripts/c180_idea5_diag.py
"""
import sys
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "scripts", "core"))

from fractions import Fraction as Fr
import audit_independent as AI
import c162_dimV_formula as M
import c166_layer_audit as LA

mul, rank = AI.mul, AI.rank


def build(d, mus, r):
    n = d + 2
    Ap = [[Fr(0)] * d for _ in range(d)]
    for i in range(d):
        Ap[i][i] = Fr(mus[i])
    N = [[Fr(1) if i == j else Fr(0) for j in range(d)] for i in range(n)]
    u = [Fr(0)] * n
    u[d] = Fr(1)
    R0 = [[u[i] * r[j] for j in range(d)] for i in range(n)]
    NA = mul(N, Ap)
    AN = [[NA[i][j] + R0[i][j] for j in range(d)] for i in range(n)]
    A = [[AN[i][j] for j in range(d)] for i in range(n)]
    en = [Fr(0)] * n
    en[n - 1] = Fr(1)
    for _ in range(2):
        for i in range(n):
            A[i].append(en[i])
    C = [[Fr(0)] * n]
    C[0][n - 1] = Fr(1)
    return A, C


def closure_dim(Ap, r, d):
    V = [r]
    for _ in range(d + 1):
        imgs = [mul([v], Ap)[0] for v in V]
        V2 = AI.row_basis(V + imgs)
        if len(V2) == len(V):
            break
        V = V2
    return len(V)


def main():
    for d in (3, 4):
        mus = [Fr(2 * i + 1) for i in range(d)]
        Ap = [[Fr(0)] * d for _ in range(d)]
        for i in range(d):
            Ap[i][i] = Fr(mus[i])
        print("=" * 64)
        print("d =", d, " mu =", [str(x) for x in mus])
        for k in range(1, d + 1):
            r = [Fr(1) if i < k else Fr(0) for i in range(d)]
            dimV = closure_dim(Ap, r, d)
            A, C = build(d, mus, r)
            n = len(A)
            L0 = [[Fr(0)] * n]
            for i in range(d):
                L0[0][i] = r[i]
            D = M.reduced_data(A, C, L0)
            if not D["inV"]:
                print("  |supp r| =", k, " dimV", dimV, " 不可行")
                continue
            rec = LA.audit_instance("d" + str(d), A, C, L0, random.Random(1), 40, verbose=False)
            print("  |supp r| =", k, " dimV", dimV, " rho0", rec.get("rho0"),
                  " rho*", rec["rhostar"], " q_min", rec["qmin"])


if __name__ == "__main__":
    main()
