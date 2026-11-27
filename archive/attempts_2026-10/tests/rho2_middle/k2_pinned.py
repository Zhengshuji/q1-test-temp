"""k2_pinned.py — k=2 层：行 1 约束把 Sigma 钉住（Q1-FALSE）

定理（待验证）：设 q=3, k=2, beta = L0R0 + A'^T alpha0。
若 beta 与 alpha0 线性无关，则任何 k=2 解的行空间 Sigma = row(LN) 必等于 span{alpha0, beta}。

本脚本：
  1. 随机实例，要求 d=3, dimV=3, rho0=1, beta ∦ alpha0；
  2. 取唯一的 Sigma，解线性系统 (L,U,Y)，在解空间抽样；
  3. 检查 rank(L)=3、rank(U)=2、铅笔 gcd=1；
  4. 与随机搜索 q=3, rho=2 对拍。
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
import c166_layer_audit as LA
import k2_V_scan as S

mul, rank = AI.mul, AI.rank


def try_sigma(A, C, L0, Sigma_rows, trials=60):
    """Sigma_rows: list of 2 vectors in R^d（行）；返回 (found, rho) 或 None。"""
    d = len(Sigma_rows[0])
    n = len(A)
    V = sympy.Matrix(d, 2, lambda i, j: sympy.Rational(
        Sigma_rows[j][i].numerator, Sigma_rows[j][i].denominator))
    Am, bv, dims = S.build_system(A, C, L0, V)
    sol = sympy.linsolve((Am, bv))
    if sol == sympy.EmptySet:
        return None
    s = list(sol)[0]
    free = sorted({x for e in s for x in e.free_symbols}, key=str)
    n_, d_, q_, k_ = dims
    rng = random.Random(0)
    for _ in range(trials):
        asg = {p: sympy.Integer(rng.randint(-3, 3)) for p in free}
        v0 = [e.subs(asg) for e in s]
        n_, d_, q_, k_ = dims
        nL = q_ * n_
        Umat = [[Fr(int(sympy.Rational(v0[nL + i * k_ + a]).p),
                    int(sympy.Rational(v0[nL + i * k_ + a]).q)) for a in range(k_)]
                for i in range(q_)]
        if rank(Umat) != k_:
            continue                       # 退化点：(5a) 也不再自动
        Lm = [[Fr(int(sympy.Rational(v0[i * n_ + j]).p), int(sympy.Rational(v0[i * n_ + j]).q))
               for j in range(n_)] for i in range(q_)]
        if rank(Lm) != q_:
            continue
        if M.cond5b(Lm, A, C) == 0:
            Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
            Nmat = [[Nv[j][i] for j in range(len(Nv))] for i in range(n)]
            return rank(mul(Lm, Nmat))
    return -1   # 系统有解，但抽样未找到好点


def main():
    rng = random.Random(777)
    tot = hit = 0
    agree = 0
    for t in range(60):
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
        tot += 1
        res = try_sigma(A, C, L0, [a0, beta])
        pred = res is not None and res > 0
        # 独立搜索
        Lb, _ = LA.find_solution(A, C, L0, 3, random.Random(t), 3000, rho_target=2, Nmat=Nmat)
        truth = Lb is not None
        agree += (pred == truth)
        if pred != truth:
            print(f"  t={t} 不一致：pinned={pred} search={truth}")
        if truth:
            hit += 1
    print(f"\n非退化实例 {tot} 个；其中有 q=3,rho=2 解 {hit} 个；钉住法 vs 搜索一致 {agree}/{tot}")


if __name__ == "__main__":
    main()
