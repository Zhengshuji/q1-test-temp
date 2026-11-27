"""c169_family_scan.py — 扫描 R-族（Krylov 维数 2）随 d 的行为

背景：record/COUNTEREXAMPLE_2026-10-22.md 断言
    「这一族 q_min = 3 对任意 d>=3 都成立」。
本脚本把构造推广到一般 d，对 d=3,4,5 精确验证。

构造（推广 c161_R_family.py 与记录里 d=4 的例子）：
    n = d+2,  N = [I_d; 0_{2xd}],  C = e_n^T
    A' = diag(2x2 交换块, lambda_3,...,lambda_d)
    R0 = u (x) r,  r = e_1,  u = (1,1,0,...,0)
    A 的前 d 列 = N A' + R0；第 n-1、n 列都 = e_n
      （于是 row_n(A) = (0,...,0,1,1)，rank[C;CA]=2，K = span{e_1..e_d}）
    L0 = (2,1,0,...,0)   —— 由 beta0 = c*alpha0、alpha0 in V=span{e1,e2} 反推，强制 c=2

用法：python q1_true/scripts/c169_family_scan.py
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

mul, tr, rank = AI.mul, AI.tr, AI.rank


def build(d, lams):
    n = d + 2
    Ap = [[Fr(0)] * d for _ in range(d)]
    Ap[0][1] = Fr(1)
    Ap[1][0] = Fr(1)
    for i in range(2, d):
        Ap[i][i] = Fr(lams[i - 2])
    N = [[Fr(1) if i == j else Fr(0) for j in range(d)] for i in range(n)]
    r = [Fr(1)] + [Fr(0)] * (d - 1)
    # u 必须**不在** K 里，否则 R0 会被压缩 A' 吸收、S=0（踩过的坑）
    u = [Fr(0)] * n
    u[d] = Fr(1)                       # u = e_{d+1}
    R0 = [[u[i] * r[j] for j in range(d)] for i in range(n)]
    NA = mul(N, Ap)
    AN = [[NA[i][j] + R0[i][j] for j in range(d)] for i in range(n)]
    A = [[AN[i][j] for j in range(d)] for i in range(n)]
    en = [Fr(0)] * n
    en[n - 1] = Fr(1)
    for _ in range(2):                 # 第 n-1、n 列都 = e_n
        for i in range(n):
            A[i].append(en[i])
    C = [[Fr(0)] * n]
    C[0][n - 1] = Fr(1)
    # L0：alpha0 = c*e1 + e2，且 l u = c^2 - 1
    c = Fr(2)
    L0 = [[c, Fr(1)] + [Fr(0)] * (n - 2)]
    L0[0][d] = c * c - 1
    return A, C, L0


def main():
    print(f"{'d':>2} {'n':>2} {'lams':>12} | {'dimK':>4} {'dimV':>4} {'rho0':>4} {'rho*':>4} {'q_min':>5}")
    print("-" * 62)
    for d in (3, 4, 5):
        variants = [(), (Fr(3), Fr(5)), (Fr(2), Fr(7), Fr(11))][: max(1, d - 1)]
        for extra in variants:
            lams = (list(extra) + [Fr(k + 3) for k in range(d - 2)])[: d - 2]
            A, C, L0 = build(d, lams)
            n = len(A)
            D = M.reduced_data(A, C, L0)
            if not D["inV"]:
                print(f"{d:>2} {n:>2} {str([str(x) for x in lams]):>12} | 不可行")
                continue
            Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
            Nmat = [[Nv[j][i] for j in range(len(Nv))] for i in range(n)]
            rho0 = rank(mul(L0, Nmat))
            try:
                rec = LA.audit_instance(f"d{d}", A, C, L0, random.Random(7), 40, verbose=False)
            except Exception as e:
                print(f"{d:>2} {n:>2} | ERR {type(e).__name__}")
                continue
            print(f"{d:>2} {n:>2} {str([str(x) for x in lams]):>12} | {D['d']:>4} {len(D['V']):>4} "
                  f"{rho0:>4} {str(rec['rhostar']):>4} {str(rec['qmin']):>5}")


if __name__ == "__main__":
    main()
