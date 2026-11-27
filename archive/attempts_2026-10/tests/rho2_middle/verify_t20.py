"""verify_t20.py — 复现并验证 k2_pinned 中 t=20 的实例（Q1-FALSE）

若它满足 dim V=3、存在 q=3,rho=2 的解、且 q=2 无解，则是第一个真正的中间层 k=2 实例。
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
import c164_trusted_baseline as TB
import k2_V_scan as S
import k2_pinned as P

mul, rank = AI.mul, AI.rank


def main():
    rng = random.Random(777)
    target = 20
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
        if t != target:
            continue
        print(f"t={t}  d={d} dimV={len(D['V'])} rho0={rank(mul(L0,Nmat))}")
        print("  alpha0=", [str(x) for x in a0], " beta=", [str(x) for x in beta])
        # 解线性系统并取一个好点
        V = sympy.Matrix(d, 2, lambda i, j: sympy.Rational(
            [a0, beta][j][i].numerator, [a0, beta][j][i].denominator))
        Am, bv, dims = S.build_system(A, C, L0, V)
        sol = sympy.linsolve((Am, bv))
        s = list(sol)[0]
        free = sorted({x for e in s for x in e.free_symbols}, key=str)
        n_, d_, q_, k_ = dims
        rng2 = random.Random(0)
        found = None
        for _ in range(200):
            asg = {p: sympy.Integer(rng2.randint(-3, 3)) for p in free}
            v0 = [e.subs(asg) for e in s]
            Lm = [[Fr(int(sympy.Rational(v0[i * n_ + j]).p), int(sympy.Rational(v0[i * n_ + j]).q))
                   for j in range(n_)] for i in range(q_)]
            if rank(Lm) != q_:
                continue
            if M.cond5b(Lm, A, C) == 0:
                found = Lm
                break
        if found is None:
            print("  抽样未找到好点")
            return
        ok, det = TB.check_solution(found, A, C, L0)
        print("  解:", [[str(x) for x in r] for r in found])
        print("  可信基线复核:", ok, det)
        print("  rank(LN) =", rank(mul(found, Nmat)))
        # q=2 是否有解
        L2, _ = LA.find_solution(A, C, L0, 2, random.Random(9), 5000, Nmat=Nmat)
        print("  q=2 有解?", L2 is not None)
        out = os.path.join(ROOT, "q1_false", "tests", "results")
        os.makedirs(out, exist_ok=True)
        json.dump(dict(A=[[str(x) for x in r] for r in A],
                       C=[[str(x) for x in r] for r in C],
                       L0=[[str(x) for x in r] for r in L0],
                       L=[[str(x) for x in r] for r in found]),
                  open(os.path.join(out, "middle_k2_pinned.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
        print("  已保存 q1_false/tests/results/middle_k2_pinned.json")
        return
    print("没找到 t=20")


if __name__ == "__main__":
    main()
