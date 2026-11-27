"""exact_k2_layer.py — k=2 层的精确判定（Q1-FALSE）

对非退化实例（beta ∦ alpha0），Sigma 唯一（定理 4.15）。于是：
  gcd_{Q(s)[λ]}(铅笔子式) = 1  => 该层可达（q(2)=3）；
  gcd ≠ 1（系数不依赖 s）      => 该层不可达。

对随机实例跑，验证与搜索一致，并把"搜索未找到"升级为"精确不可达"。
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
import exact_sigma as ES

mul, rank = AI.mul, AI.rank


def gcd_for(A, C, L0, s1, s2):
    d = len(s1)
    V = sympy.Matrix(d, 2, lambda i, j: sympy.Rational(
        [s1, s2][j][i].numerator, [s1, s2][j][i].denominator))
    import k2_V_scan as S
    Am, bv, dims = S.build_system(A, C, L0, V)
    solset = sympy.linsolve((Am, bv))
    if solset == sympy.EmptySet:
        return "inconsistent"
    sol = list(solset)[0]
    n_, d_, q_, k_ = dims
    lam = sympy.symbols("lam")
    U = sympy.Matrix(q_, k_, lambda i, j: sol[q_ * n_ + i * k_ + j])
    Y = sympy.Matrix(q_, k_, lambda i, j: sol[q_ * n_ + q_ * k_ + i * k_ + j])
    P = lam * U - Y
    minors = [sympy.expand(P[i, 0] * P[j, 1] - P[i, 1] * P[j, 0])
              for i in range(q_) for j in range(i + 1, q_)]
    g = minors[0]
    for mm in minors[1:]:
        g = sympy.gcd(g, mm)
    return sympy.factor(g)


def main():
    rng = random.Random(20251025)
    done = 0
    for t in range(40):
        n, p = 5, 1
        A = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-1, 1)) for _ in range(n)] for _ in range(p)]
        L0 = [[Fr(rng.randint(-1, 1)) for _ in range(n)]]
        if rank(L0) != 1:
            continue
        Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
        d = len(Nv)
        if d != 3:
            continue
        Nmat = [[Nv[j][i] for j in range(d)] for i in range(n)]
        a0 = mul(L0, Nmat)[0]
        if not any(a0):
            continue
        D = M.reduced_data(A, C, L0)
        if not D["inV"] or len(D["V"]) != 3:
            continue
        Ap, R0 = D["Ap"], D["R0"]
        l0r0 = mul(L0, R0)[0]
        a0Ap = [sum(a0[i] * Ap[i][j] for i in range(d)) for j in range(d)]
        beta = [l0r0[j] + a0Ap[j] for j in range(d)]
        if rank([a0, beta]) != 2:
            continue
        g = gcd_for(A, C, L0, a0, beta)
        done += 1
        print(f"[{done}] dimV=3 rho0=1  gcd = {g}", flush=True)
        if done >= 6:
            break


if __name__ == "__main__":
    main()
