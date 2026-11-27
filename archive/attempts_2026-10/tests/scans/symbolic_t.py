"""symbolic_t.py — candidate 的 d=3 符号消元尝试（Q1-FALSE）

目标：把 t 当符号，解线性系统 (L,U,Y)，算铅笔子式的 gcd，得到"好 t"的精确集合。
若 sympy 能完成，就能判定 ∃t；若超时/爆炸，记录为"消元爆炸"的证据。

用法：
    python q1_false/tests/symbolic_t.py
"""
import sys
import os
import json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools", "exact_linalg"))

from fractions import Fraction as Fr
import sympy
import audit_independent as AI
import c162_dimV_formula as M

mul, rank = AI.mul, AI.rank


def main():
    d0 = json.load(open(os.path.join(ROOT, "lit", "counterexample_candidate.json"), encoding="utf-8"))
    F = lambda m: [[Fr(x) for x in r] for r in m]
    A, C, L0 = F(d0["A"]), F(d0["C"]), F(d0["L0"])
    n = len(A)
    D = M.reduced_data(A, C, L0)
    Ap, R0 = D["Ap"], D["R0"]
    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    d = len(Nv)
    Nmat = [[Nv[j][i] for j in range(d)] for i in range(n)]
    a0 = mul(L0, Nmat)[0]
    a0v = sympy.Matrix([sympy.Rational(x.numerator, x.denominator) for x in a0])
    comp = []
    for i in range(d):
        e = sympy.zeros(d, 1)
        e[i] = 1
        if sympy.Matrix.hstack(a0v, *comp, e).rank() == len(comp) + 2:
            comp.append(e)
        if len(comp) == d - 1:
            break

    t, lam = sympy.symbols("t lam")
    b = comp[0] + t * comp[1]
    V = sympy.Matrix.hstack(a0v, b)          # d×2
    Vt = V.T
    W = sympy.zeros(d, 2)
    for j in range(d):
        for a in range(2):
            W[j, a] = sum(V[i, a] * sympy.Rational(Ap[i][j].numerator, Ap[i][j].denominator)
                          for i in range(d))

    q, k = 3, 2
    nL, nU, nY = q * n, q * k, q * k
    N = nL + nU + nY
    rows, rhs = [], []
    # LN - U V^T = 0
    for i in range(q):
        for j in range(d):
            row = [sympy.Integer(0)] * N
            for tt in range(n):
                row[i * n + tt] = sympy.Rational(Nmat[tt][j].numerator, Nmat[tt][j].denominator)
            for a in range(k):
                row[nL + i * k + a] = -Vt[a, j]
            rows.append(row)
            rhs.append(sympy.Integer(0))
    # LR0 + U W^T - Y V^T = 0
    for i in range(q):
        for j in range(d):
            row = [sympy.Integer(0)] * N
            for tt in range(n):
                row[i * n + tt] += sympy.Rational(R0[tt][j].numerator, R0[tt][j].denominator)
            for a in range(k):
                row[nL + i * k + a] += W[j, a]
                row[nL + nU + i * k + a] -= Vt[a, j]
            rows.append(row)
            rhs.append(sympy.Integer(0))

    print("求解符号线性系统 ...", flush=True)
    Am = sympy.Matrix(rows)
    bv = sympy.Matrix(rhs)
    sol = sympy.linsolve((Am, bv))
    if sol == sympy.EmptySet:
        print("无解（对所有 t）")
        return
    s = list(sol)[0]
    free = sorted({x for e in s for x in e.free_symbols if x != t}, key=str)
    print(f"解空间自由参数 {len(free)} 个", flush=True)

    assignments = [
        {p: sympy.Integer(i + 2) for i, p in enumerate(free)},          # 2,3,4,...
        {p: sympy.Integer((i * 3) % 5 + 1) for i, p in enumerate(free)},
        {p: sympy.Integer((i * 7) % 11 + 1) for i, p in enumerate(free)},
    ]
    for ai, asg in enumerate(assignments):
        vals = [sympy.together(e.subs(asg)) for e in s]

        def pick(i, j, off):
            return vals[off + i * k + j]

        U = sympy.Matrix(3, k, lambda i, j: pick(i, j, nL))
        Y = sympy.Matrix(3, k, lambda i, j: pick(i, j, nL + nU))
        P = lam * U - Y
        minors = [sympy.factor(sympy.expand(P[i, 0] * P[j, 1] - P[i, 1] * P[j, 0]))
                  for i in range(3) for j in range(i + 1, 3)]
        print(f"[{ai}] 计算 gcd ...", flush=True)
        g = sympy.gcd(minors[0], minors[1])
        g = sympy.gcd(g, minors[2])
        print(f"[{ai}] gcd(子式) = {sympy.factor(g)}", flush=True)


if __name__ == "__main__":
    main()
