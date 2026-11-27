"""exact_r1_q3.py — 精确判定 q=3,rho=1 层（Q1-FALSE）

定理 4.14 的证明与 q 无关：row 1 给 alpha0=u1 v、L0R0=y1 v，故
  alpha0=0 时 v ∝ L0R0（若为 0 则无解）。
所以 q=3,rho=1 的 Sigma 也唯一。剩下只需判定仿射解空间里是否存在
rank[u, y] = 2 的点（即 y 不平行于 u）。

做法：符号解线性系统，把 u、y 写成自由参数 s 的仿射函数，
算三个 2×2 子式；若它们不恒为零 -> 有反例（该层可达）。
"""
import sys
import os
import json
import random

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools", "exact_linalg"))

from fractions import Fraction as Fr
import sympy
import audit_independent as AI
import c162_dimV_formula as M

mul, rank = AI.mul, AI.rank


def check_instance(A, C, L0, verbose=False):
    n = len(A)
    D = M.reduced_data(A, C, L0)
    if not D["inV"]:
        return None
    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    d = len(Nv)
    Nmat = [[Nv[j][i] for j in range(d)] for i in range(n)]
    a0 = mul(L0, Nmat)[0]
    R0 = D["R0"]
    l0r0 = mul(L0, R0)[0]
    if any(a0):
        v = a0[:]
    else:
        if all(x == 0 for x in l0r0):
            return "no_solution_structure"
        v = l0r0[:]
    Ap = D["Ap"]
    w = [sum(v[i] * Ap[i][j] for i in range(d)) for j in range(d)]

    # q=3, k=1：未知量 l1,l2 (2n), u(3), y(3)
    q, k = 3, 1
    m = 2 * n + 3 + 3
    rows, rhs = [], []
    # LN = u v^T：行 1 = L0（已知，检查一致性），行 2,3 是未知 ℓ 的行
    # 行 1: alpha0 = u1 v ; 行 1 of LR0: L0R0 = -u1 w + y1 v
    # 未知行 i=2,3: l_i N = u_i v ; l_i R0 = -u_i w + y2/y3 v
    # 先把行 1 的一致性提出来（与 q 无关）
    # 这里只列未知行 2,3 的方程
    for irow in range(2):                 # 两个未知行
        for j in range(d):
            row = [sympy.Integer(0)] * m
            for t in range(n):
                row[irow * n + t] = sympy.Rational(Nmat[t][j].numerator, Nmat[t][j].denominator)
            row[2 * n + (irow + 1)] = -v[j]      # -u_{irow+2} v_j
            rows.append(row)
            rhs.append(sympy.Integer(0))
        for j in range(d):
            row = [sympy.Integer(0)] * m
            for t in range(n):
                row[irow * n + t] = sympy.Rational(R0[t][j].numerator, R0[t][j].denominator)
            row[2 * n + (irow + 1)] = w[j]       # +u w
            row[2 * n + 3 + (irow + 1)] = -v[j]  # -y v
            rows.append(row)
            rhs.append(sympy.Integer(0))
    # 行 1 的一致性（alpha0 = u1 v, L0R0 = -u1 w + y1 v）另行检查
    if any(a0):
        k0 = next(j for j in range(d) if v[j] != 0)
        if not all(a0[j] * v[k0] == a0[k0] * v[j] for j in range(d)):
            return "inconsistent_row1"
    # 注意：行 1 的 u1、y1 也自由；把 u1,y1 作为符号加入会更有自由度。
    # 简化处理：u1、y1 取一组满足行 1 的解。
    # alpha0=0 => u1=0 => L0R0=y1 v, y1 固定
    if any(a0):
        u1 = a0[k0] / v[k0]
        y1 = None
    else:
        u1 = sympy.Integer(0)
        k0 = next(j for j in range(d) if v[j] != 0)
        y1 = l0r0[k0] / v[k0]

    Am = sympy.Matrix(rows)
    bv = sympy.Matrix(rhs)
    sol = sympy.linsolve((Am, bv))
    if sol == sympy.EmptySet:
        return "inconsistent"
    s = list(sol)[0]
    # 取 u2,u3,y2,y3
    u2, u3 = s[2 * n + 1], s[2 * n + 2]
    y2, y3 = s[2 * n + 4], s[2 * n + 5]
    if y1 is None:
        y1 = sympy.Symbol("y1")
    u = [sympy.sympify(u1), u2, u3]
    y = [sympy.sympify(y1), y2, y3]
    minors = [sympy.expand(u[i] * y[j] - u[j] * y[i]) for i in range(3) for j in range(i + 1, 3)]
    if verbose:
        print("   u =", u)
        print("   y =", y)
        print("   子式 =", [str(mm) for mm in minors])
    good = any(mm != 0 for mm in minors)
    return "reachable" if good else "empty"


def main():
    rng = random.Random(20251026)
    stats = {}
    for t in range(120):
        n = rng.choice([5, 6])
        p = rng.choice([1, 2])
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        L0 = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        if rank(L0) != 1:
            continue
        D = M.reduced_data(A, C, L0)
        if not D["inV"]:
            continue
        if M.cond5a(L0, A, C) and (M.cond5b(L0, A, C) == 0):
            continue                       # L0 是解 -> 不在本通道
        try:
            res = check_instance(A, C, L0)
        except Exception as e:
            res = f"ERR {type(e).__name__}"
        stats[res] = stats.get(res, 0) + 1
        if res == "reachable":
            print(f"[REACHABLE] t={t} n={n} p={p}")
    for kk in sorted(stats, key=str):
        print(f"  {kk}: {stats[kk]}")


if __name__ == "__main__":
    main()
