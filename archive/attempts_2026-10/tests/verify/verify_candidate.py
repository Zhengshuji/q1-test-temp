"""verify_candidate.py — 构造并复核候选反例（Q1-FALSE）

对 q1_false/tests/results/candidate_r1_nontight.json：
重建 q=3,rho=1 的符号解，采样出 rank(L)=3 且 rank[u y]=2 的点，
用 c164 可信基线复核；再用 D47 判定器确认 q=2 不可行。
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
import c164_trusted_baseline as TB
import rho1_solver as RS

mul, rank = AI.mul, AI.rank


def main():
    path = os.path.join(ROOT, "q1_false", "tests", "results", "candidate_r1_nontight.json")
    d0 = json.load(open(path, encoding="utf-8"))
    F = lambda m: [[Fr(x) for x in r] for r in m]
    A, C, L0 = F(d0["A"]), F(d0["C"]), F(d0["L0"])
    n = len(A)
    D = M.reduced_data(A, C, L0)
    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    d = len(Nv)
    Nmat = [[Nv[j][i] for j in range(d)] for i in range(n)]
    a0 = mul(L0, Nmat)[0]
    R0 = D["R0"]
    l0r0 = mul(L0, R0)[0]
    print(f"n={n} p={len(C)} d={d} dimV={len(D['V'])} alpha0={[str(x) for x in a0]} L0R0={[str(x) for x in l0r0]}")
    print("L0 是解?", M.cond5a(L0, A, C) and (M.cond5b(L0, A, C) == 0))
    sol2 = RS.solve_case(A, C, L0)
    print("q=2,rho=1 精确可行?", sol2 is not None)

    v = a0[:] if any(a0) else l0r0[:]
    if all(x == 0 for x in v):
        print("v=0，结构上无解")
        return
    Ap = D["Ap"]
    w = [sum(v[i] * Ap[i][j] for i in range(d)) for j in range(d)]
    k0 = next(j for j in range(d) if v[j] != 0)
    u1 = Fr(0) if not any(a0) else a0[k0] / v[k0]
    y1 = None if any(a0) else l0r0[k0] / v[k0]

    # 未知量：l1,l2 (2n), u2,u3, y2,y3
    m = 2 * n + 4
    rows, rhs = [], []
    for irow in range(2):
        for j in range(d):
            row = [sympy.Integer(0)] * m
            for t in range(n):
                row[irow * n + t] = sympy.Rational(Nmat[t][j].numerator, Nmat[t][j].denominator)
            row[2 * n + irow] = -v[j]
            rows.append(row)
            rhs.append(sympy.Integer(0))
        for j in range(d):
            row = [sympy.Integer(0)] * m
            for t in range(n):
                row[irow * n + t] = sympy.Rational(R0[t][j].numerator, R0[t][j].denominator)
            row[2 * n + irow] = w[j]
            row[2 * n + 2 + irow] = -v[j]
            rows.append(row)
            rhs.append(sympy.Integer(0))
    sol = sympy.linsolve((sympy.Matrix(rows), sympy.Matrix(rhs)))
    if sol == sympy.EmptySet:
        print("线性系统无解")
        return
    s = list(sol)[0]
    free = sorted({x for e in s for x in e.free_symbols}, key=str)
    print(f"自由参数 {len(free)} 个")
    rng = random.Random(0)
    maxrank = 0
    for _ in range(500):
        asg = {p: sympy.Integer(rng.randint(-4, 4)) for p in free}
        v0 = [e.subs(asg) for e in s]

        def val(i):
            return Fr(int(sympy.Rational(v0[i]).p), int(sympy.Rational(v0[i]).q))
        l1 = [val(t) for t in range(n)]
        l2 = [val(n + t) for t in range(n)]
        u2, u3 = val(2 * n), val(2 * n + 1)
        y2, y3 = val(2 * n + 2), val(2 * n + 3)
        L = [L0[0][:], l1, l2]
        rk = rank(L)
        maxrank = max(maxrank, rk)
        if rk != 3:
            continue
        # y ∉ span u
        uu = [u1, u2, u3]
        yy = [y1 if y1 is not None else Fr(0), y2, y3]
        if rank([yy, uu]) != 2:
            continue
        ok, det = TB.check_solution(L, A, C, L0)
        if ok:
            print("*** 找到合法解 ***")
            print("  L =", [[str(x) for x in r] for r in L])
            print("  (5a)(5b) 全过:", det)
            print("  rank(LN) =", rank(mul(L, Nmat)))
            out = os.path.join(ROOT, "lit", "counterexample_r1_nontight_2026-10-26.json")
            json.dump(dict(A=[[str(x) for x in r] for r in A],
                           C=[[str(x) for x in r] for r in C],
                           L0=[[str(x) for x in r] for r in L0],
                           L=[[str(x) for x in r] for r in L],
                           note="r=1, q=2 不可行, q=3,rho=1 有解"),
                      open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            print("  已保存", out)
            return
    print(f"500 次采样未找到合法点；采样中 rank(L) 最大 = {maxrank}")


if __name__ == "__main__":
    main()
