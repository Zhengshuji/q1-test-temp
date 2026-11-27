"""rho_k_structure.py — 验证一般 rho=k 的结构方程（Q1-FALSE）

对任意解 L（rank(LN)=k），令 M=LN=U V^T（U: q×k, V: d×k），W=A'^T V。
则 (5b) 在 V^⊥ 上强制 N'xi = -U W^T xi，因此

    T := LR0 + U W^T   满足   T = Y V^T   （某个 Y: q×k）。

k=1 时这条 + 开条件还是**充分**的（D46/D47）；k>=2 时只是**必要**的。
本脚本验证这条必要结构在实例上成立，并报告 k 与 q 的关系。
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
import c166_layer_audit as LA

mul, rank = AI.mul, AI.rank


def rat(x):
    x = sympy.Rational(x)
    return x


def toS(Mx):
    return sympy.Matrix([[sympy.Rational(x.numerator, x.denominator) for x in row] for row in Mx])


def check_structure(L, A, C, L0):
    n = len(A)
    D = M.reduced_data(A, C, L0)
    Ap, R0 = D["Ap"], D["R0"]
    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    d = len(Nv)
    Nmat = [[Nv[j][i] for j in range(d)] for i in range(n)]
    Mx = mul(L, Nmat)
    Nx = mul(L, R0)
    k = rank(Mx)
    q = len(L)
    Ms = toS(Mx)
    # U：列空间的基（q×k）
    cols = []
    for j in range(d):
        col = Ms[:, j]
        cand = cols + [col]
        if sympy.Matrix.hstack(*cand).rank() == len(cand):
            cols.append(col)
        if len(cols) == k:
            break
    U = sympy.Matrix.hstack(*cols)                 # q×k
    Vt = (U.T * U).inv() * U.T * Ms                # k×d  = V^T
    V = Vt.T                                       # d×k
    # W = A'^T V: W[j,a] = sum_i V[i,a] Ap[i][j]
    W = sympy.zeros(d, k)
    for j in range(d):
        for a in range(k):
            W[j, a] = sum(V[i, a] * rat(Ap[i][j]) for i in range(d))
    T = toS(Nx) + U * W.T                          # q×d
    # 检查 T = Y V^T
    solvable = True
    Y = None
    try:
        Y = T * V * (Vt * V).inv()
        resid = T - Y * Vt
        solvable = (resid == sympy.zeros(*resid.shape))
    except Exception:
        solvable = False
    # 关键推论：lambda U - Y 必须对一切 lambda 满列秩 k
    pencil_ok = True
    if solvable:
        for lam in (0, 1, -1, 2, -3, sympy.Rational(1, 2)):
            if (lam * U - Y).rank() != k:
                pencil_ok = False
                break
    return k, q, d, solvable, pencil_ok


def main():
    toF = lambda m: [[Fr(x) for x in row] for row in m]
    for fn, q in [("counterexample_candidate.json", 3),
                  ("counterexample_d4.json", 3),
                  ("certificate_middle_layer.json", 2),
                  ("certificate_rhostar_lt_dimV.json", 2)]:
        d0 = json.load(open(os.path.join(ROOT, "lit", fn), encoding="utf-8"))
        A, C, L0 = toF(d0["A"]), toF(d0["C"]), toF(d0["L0"])
        n = len(A)
        Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
        Nmat = [[Nv[j][i] for j in range(len(Nv))] for i in range(n)]
        L = None
        for key in ("L", "L_2row"):
            if key in d0 and len(d0[key]) == q:
                L = toF(d0[key])
                break
        if L is None:
            L, _ = LA.find_solution(A, C, L0, q, random.Random(3), 8000, Nmat=Nmat)
        k, qq, d, ok, pok = check_structure(L, A, C, L0)
        print(f"{fn:42s} q={qq} rho={k} d={d}   结构 T=YV^T: {ok}   pencil 满秩: {pok}")


if __name__ == "__main__":
    main()
