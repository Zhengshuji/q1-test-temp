"""exact_sigma.py — 固定 Sigma 时的精确判定（专家四步法的实现）

对固定 Sigma：
  1. 解线性系统，得到 (L,U,Y) 的一般解（自由参数当符号 s）；
  2. 算铅笔 λU-Y 的各 2×2 子式 p_I(λ,s)；
  3. 算 gcd_{Q(s)[λ]}(p_I)。
     - gcd = 1  => 对一般 s 无公共根 => A(Sigma) 含好点（该层可达）；
     - gcd ≠ 1  => 对一切 s 都有公共根 => A(Sigma) 整体落在坏集（该层不可达）。

先在实例 C 的 t=0（经验上好）与 t=1（经验上坏）上校验。
"""
import sys
import os
import json

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


def exact_gcd(A, C, L0, Sigma, verbose=True):
    d = len(Sigma[0])
    V = sympy.Matrix(d, 2, lambda i, j: sympy.Rational(
        Sigma[j][i].numerator, Sigma[j][i].denominator))
    Am, bv, dims = S.build_system(A, C, L0, V)
    solset = sympy.linsolve((Am, bv))
    if solset == sympy.EmptySet:
        return "inconsistent"
    sol = list(solset)[0]
    free = sorted({x for e in sol for x in e.free_symbols}, key=str)
    n_, d_, q_, k_ = dims
    lam = sympy.symbols("lam")
    U = sympy.Matrix(q_, k_, lambda i, j: sol[q_ * n_ + i * k_ + j])
    Y = sympy.Matrix(q_, k_, lambda i, j: sol[q_ * n_ + q_ * k_ + i * k_ + j])
    P = lam * U - Y
    minors = [sympy.expand(P[i, 0] * P[j, 1] - P[i, 1] * P[j, 0])
              for i in range(q_) for j in range(i + 1, q_)]
    if verbose:
        print(f"  自由参数 {len(free)} 个；子式次数（λ）= {[sympy.degree(mm, lam) for mm in minors]}")
    g = minors[0]
    for mm in minors[1:]:
        g = sympy.gcd(g, mm)
    return sympy.factor(g)


def main():
    d0 = json.load(open(os.path.join(ROOT, "lit", "counterexample_candidate.json"), encoding="utf-8"))
    F = lambda m: [[Fr(x) for x in r] for r in m]
    A, C, L0 = F(d0["A"]), F(d0["C"]), F(d0["L0"])
    n = len(A)
    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    d = len(Nv)
    Nmat = [[Nv[j][i] for j in range(d)] for i in range(n)]
    a0 = mul(L0, Nmat)[0]
    # 与 k2_V_scan 相同的参数化：Sigma(t)=span{a0, e1 + t e3}
    a0v = sympy.Matrix([sympy.Rational(x.numerator, x.denominator) for x in a0])
    e1 = [sympy.Integer(1), sympy.Integer(0), sympy.Integer(0)]
    e3 = [sympy.Integer(0), sympy.Integer(0), sympy.Integer(1)]
    for t, nm in ((0, "t=0 (经验好)"), (1, "t=1 (经验坏)")):
        Sigma = [[Fr(1), Fr(0), Fr(0)], [Fr(1) + Fr(0), Fr(0) + Fr(t * 0), Fr(t)]]
        # 直接用整数构造：Sigma = span{a0, e1 + t e3}
        s1 = [Fr(x) for x in a0]
        s2 = [Fr(1), Fr(0), Fr(t)]
        print(f"--- {nm}  Sigma=span{{{[str(x) for x in s1]}, {[str(x) for x in s2]}}}")
        g = exact_gcd(A, C, L0, [s1, s2])
        print(f"    gcd = {g}")


if __name__ == "__main__":
    main()
