"""c182_blocks_d6.py — d=6, p=2, A' = 三个 2x2 交换块

目标是看 q_min 是否依赖"r 覆盖了哪些块"（即 V 的块结构），
并找是否有 rho* < dimV 的实例（中间层的块版本）。

用法：python q1_true/scripts/c182_blocks_d6.py
"""
import sys
import os
import random
import itertools

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "scripts", "core"))

from fractions import Fraction as Fr
import audit_independent as AI
import c162_dimV_formula as M
import c166_layer_audit as LA

mul, rank = AI.mul, AI.rank


def swap_block():
    return [[Fr(0), Fr(1)], [Fr(1), Fr(0)]]


def build(blocks, r, u, p=2):
    d = sum(len(b) for b in blocks)
    n = d + p
    Ap = []
    for b in blocks:
        m = len(b)
        for i in range(m):
            Ap.append([b[i][j] if i < m else Fr(0) for j in range(m)]
                      + [Fr(0)] * (d - m))
    # 上面的拼法不对，直接构造
    Ap = [[Fr(0)] * d for _ in range(d)]
    off = 0
    for b in blocks:
        m = len(b)
        for i in range(m):
            for j in range(m):
                Ap[off + i][off + j] = b[i][j]
        off += m
    N = [[Fr(1) if i == j else Fr(0) for j in range(d)] for i in range(n)]
    R0 = [[u[i] * r[j] for j in range(d)] for i in range(n)]
    NA = mul(N, Ap)
    AN = [[NA[i][j] + R0[i][j] for j in range(d)] for i in range(n)]
    A = [[AN[i][j] for j in range(d)] for i in range(n)]
    en = [Fr(0)] * n
    en[n - 1] = Fr(1)
    for _ in range(p):
        for i in range(n):
            A[i].append(en[i])
    C = [[Fr(0)] * n]
    C[0][n - 1] = Fr(1)
    return A, C, Ap


def main():
    blocks = [swap_block(), swap_block(), swap_block()]
    d = 6
    n = 8
    for nblk in (1, 2, 3):
        r = [Fr(0)] * d
        for i in range(nblk):
            r[2 * i] = Fr(1)
        u = [Fr(0)] * n
        u[d] = Fr(1)
        A, C, Ap = build(blocks, r, u)
        L0 = [[Fr(0)] * n]
        for i in range(d):
            L0[0][i] = r[i]
        D = M.reduced_data(A, C, L0)
        if not D["inV"]:
            print("块数", nblk, "不可行")
            continue
        rec = LA.audit_instance("b", A, C, L0, random.Random(1), 40, verbose=False)
        print("r 覆盖块数", nblk, " dimV", len(D["V"]), " rho*", rec["rhostar"],
              " q_min", rec["qmin"])


if __name__ == "__main__":
    main()
