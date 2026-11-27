"""c181_scan_u.py — 在 p=1, d=3 上扫 u（R0 = u (x) r）的结构

固定 A' = [[0,1,0],[1,0,0],[0,0,3]]（交换块 + 1 维块）、r = e1、
N = [I_3;0] (n=5)、C = e_5^T；A 前 3 列 = N A' + R0，后两列 = e_5。

对不同的 u（u 不在 K = span{e1,e2,e3} 里）算 q_min，看是否依赖 u 的结构。

用法：python q1_true/scripts/c181_scan_u.py
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


def build(Ap, u, r):
    d = len(Ap)
    n = d + 2
    N = [[Fr(1) if i == j else Fr(0) for j in range(d)] for i in range(n)]
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


def main():
    Ap = [[Fr(0), Fr(1), Fr(0)],
          [Fr(1), Fr(0), Fr(0)],
          [Fr(0), Fr(0), Fr(3)]]
    r = [Fr(1), Fr(0), Fr(0)]
    d, n = 3, 5
    u_list = []
    for k in range(1, 4):
        import itertools
        for supp in itertools.combinations([3, 4], k):
            for vals in itertools.product([-1, 1], repeat=k):
                u = [Fr(0)] * n
                for s, v in zip(supp, vals):
                    u[s] = Fr(v)
                u_list.append(u)
    # 再加带 K 分量的
    for extra in ([1, 0, 0], [0, 1, 0], [1, 1, 0]):
        u = [Fr(x) for x in extra] + [Fr(1), Fr(0)]
        u_list.append(u)
    print("u 个数:", len(u_list))
    for u in u_list:
        A, C = build(Ap, u, r)
        L0 = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(0)]]
        D = M.reduced_data(A, C, L0)
        if not D["inV"]:
            print("  u", [str(x) for x in u], " 不可行")
            continue
        rec = LA.audit_instance("u", A, C, L0, random.Random(1), 30, verbose=False)
        print("  u", [str(x) for x in u], " dimV", len(D["V"]),
              " rho*", rec["rhostar"], " q_min", rec["qmin"])


if __name__ == "__main__":
    main()
