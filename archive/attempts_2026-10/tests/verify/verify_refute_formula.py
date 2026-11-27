"""verify_refute_formula.py — 独立验证 Q1-TRUE 交来的层公式反例（Q1-FALSE）

实例：n=5, p=2, r=2, 声称 d=1, dimV=1, rho0=0, q_min=3, rho*=1。
若成立，则 q_min = 3 > max(r, rho*+1) = 2，公式被推翻。
"""
import sys
import os
import json
import random

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools", "exact_linalg"))

from fractions import Fraction as Fr
import audit_independent as AI
import c162_dimV_formula as M
import c166_layer_audit as LA
import c164_trusted_baseline as TB

mul, rank = AI.mul, AI.rank


def main():
    A = [[Fr(x) for x in row] for row in [
        [5, 3, 5, 4, 2], [0, 1, 3, 0, 6], [2, 5, 6, 2, 2], [3, 6, 4, 0, 6], [0, 6, 5, 3, 1]]]
    C = [[Fr(x) for x in row] for row in [[5, 5, 1, 3, 6], [6, 0, 4, 4, 1]]]
    L0 = [[Fr(1), Fr(0), Fr(0), Fr(0), Fr(-9869, 14034)],
          [Fr(0), Fr(1), Fr(0), Fr(0), Fr(2040, 2339)]]
    n = len(A)
    CA = mul(C, A)
    Nv = AI.nullspace(AI.vstack([C, CA]))
    d = len(Nv)
    Nmat = [[Nv[j][i] for j in range(d)] for i in range(n)]
    D = M.reduced_data(A, C, L0)
    print(f"n={n} p={len(C)} r={len(L0)} d={d} dimV={len(D['V'])} rho0={rank(mul(L0,Nmat))} inV={D['inV']}")

    # L0 本身可行吗（q=r=2 的唯一候选）
    ok0, det0 = TB.check_solution(L0, A, C, L0)
    print(f"L0 本身是解? {ok0}  {det0}")
    # 直接看 (5a)(5b)
    print(f"  (5a)={M.cond5a(L0,A,C)}  (5b) gcd={M.cond5b(L0,A,C)}")

    # q=3 的解（rho=1）
    found = None
    for seed in range(6):
        L, rho = LA.find_solution(A, C, L0, 3, random.Random(seed), 30000, rho_target=1, Nmat=Nmat)
        if L is not None:
            found = (L, rho)
            break
    if found:
        L, rho = found
        ok, det = TB.check_solution(L, A, C, L0)
        print(f"q=3, rho=1 的解: {ok} {det}")
        print("  L =", [[str(x) for x in row] for row in L])
    else:
        print("q=3, rho=1 未搜到")

    # q=2 是否有解（V 只能是 row(L0)）
    anyq2 = False
    for seed in range(3):
        L2, _ = LA.find_solution(A, C, L0, 2, random.Random(seed), 5000, Nmat=Nmat)
        if L2 is not None:
            anyq2 = True
            break
    print(f"q=2 有解? {anyq2}")

    # rho=0 可达吗
    L0deg, _ = LA.find_solution(A, C, L0, 3, random.Random(99), 20000, rho_target=0, Nmat=Nmat)
    print(f"q=3, rho=0 有解? {L0deg is not None}")


if __name__ == "__main__":
    main()
