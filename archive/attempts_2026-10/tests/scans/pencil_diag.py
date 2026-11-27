"""pencil_diag.py — 诊断 k=2 铅笔：坏在哪里（Q1-FALSE）

对 candidate 的不同 V(t)，取线性系统的一个解 L，算出 (U,Y)，检查
  rank(U), rank(Y), 铅笔 λU-Y 的子式 gcd 与根。
看"坏"是 λ=0（Y 降秩）还是别的 λ。
"""
import sys
import os
import json
import random

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools", "exact_linalg"))
sys.path.insert(0, HERE)

from fractions import Fraction as Fr
import sympy
import audit_independent as AI
import c162_dimV_formula as M
import k2_V_scan as S

mul, rank = AI.mul, AI.rank


def toS(Mx):
    return sympy.Matrix([[sympy.Rational(x.numerator, x.denominator) for x in row] for row in Mx])


def diag_for_t(A, C, L0, a0v, comp, t, n, d, Nmat, Ap, R0):
    b = comp[0] if t == 0 else comp[0] + t * comp[1]
    V = sympy.Matrix.hstack(a0v, b)
    Am, bv, dims = S.build_system(A, C, L0, V)
    sol = sympy.linsolve((Am, bv))
    if sol == sympy.EmptySet:
        print(f"t={t}: 不相容")
        return
    s = list(sol)[0]
    free = sorted({x for e in s for x in e.free_symbols}, key=str)
    n_, d_, q_, k_ = dims
    rng = random.Random(0)
    for _ in range(120):
        asg = {p: sympy.Integer(rng.randint(-2, 2)) for p in free}
        v0 = [e.subs(asg) for e in s]
        Lm = [[Fr(int(sympy.Rational(v0[i * n_ + j]).p), int(sympy.Rational(v0[i * n_ + j]).q))
               for j in range(n_)] for i in range(q_)]
        if rank(Lm) != q_:
            continue
        Mx = mul(Lm, Nmat)
        Nx = mul(Lm, R0)
        if rank(Mx) != 2:
            continue
        Ms = toS(Mx)
        cols = []
        for j in range(d):
            c = Ms[:, j]
            cand = cols + [c]
            if sympy.Matrix.hstack(*cand).rank() == len(cand):
                cols.append(c)
            if len(cols) == 2:
                break
        if len(cols) != 2:
            continue
        U = sympy.Matrix.hstack(*cols)
        Vt = (U.T * U).inv() * U.T * Ms
        Vd = Vt.T
        W = sympy.zeros(d, 2)
        for j in range(d):
            for a in range(2):
                W[j, a] = sum(Vd[i, a] * sympy.Rational(Ap[i][j].numerator, Ap[i][j].denominator)
                              for i in range(d))
        T = toS(Nx) + U * W.T
        Y = T * Vd * (Vt * Vd).inv()
        lam = sympy.symbols("lam")
        P = lam * U - Y
        minors = [sympy.expand(P[i, 0] * P[j, 1] - P[i, 1] * P[j, 0])
                  for i in range(3) for j in range(i + 1, 3)]
        g = minors[0]
        for mm in minors[1:]:
            g = sympy.gcd(g, mm)
        print(f"t={t}: rank(U)={U.rank()} rank(Y)={Y.rank()}  gcd(minors)={sympy.factor(g)}  roots={sympy.solve(g, lam)}")
        return
    print(f"t={t}: 未采到有效解")


def main():
    d0 = json.load(open(os.path.join(ROOT, "lit", "counterexample_candidate.json"), encoding="utf-8"))
    F = lambda m: [[Fr(x) for x in r] for r in m]
    A, C, L0 = F(d0["A"]), F(d0["C"]), F(d0["L0"])
    n = len(A)
    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    d = len(Nv)
    Nmat = [[Nv[j][i] for j in range(d)] for i in range(n)]
    D = M.reduced_data(A, C, L0)
    Ap, R0 = D["Ap"], D["R0"]
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
    for t in [0, 1, -1, 2]:
        diag_for_t(A, C, L0, a0v, comp, t, n, d, Nmat, Ap, R0)


if __name__ == "__main__":
    main()
