"""rho1_solver.py — rho=1 层的多项式判定/构造（Q1-FALSE）

依据 THE_LEMMA §4.7：q=2、rank(LN)=1 时

    (5b) <=> 存在 u∈R^2\\{0}, v∈R^d\\{0}, y∉span{u}：
              LN = u v^T,   LR0 = -u w^T + y v^T,   w = v A'

且 L0 的两行数据直接定出 v：
    - alpha0 = L0N ≠ 0  =>  v ∝ alpha0,  取 u1=1；
    - alpha0 = 0        =>  v ∝ L0R0（L0R0=0 则无解），u=(0,1)。

剩余方程对 (ell, t=u2, y2) **线性**；开条件 y∉span{u} 排除一条直线。
本脚本在解空间里挑满足开条件 + rank/(5a)/(5b) 的点。
"""
import sys
import os
import json
import random
import argparse
import itertools

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools", "exact_linalg"))

from fractions import Fraction as Fr
import sympy
import audit_independent as AI
import c162_dimV_formula as M
import c166_layer_audit as LA

mul, rank = AI.mul, AI.rank


def check_rows(L, A, C, L0):
    q = len(L)
    if q < len(L0) or rank(L) != q:
        return None
    if rank(L + [r[:] for r in L0]) != q:
        return None
    CA = mul(C, A)
    if rank(AI.vstack([mul(L, A), L, CA, C])) != rank(AI.vstack([L, CA, C])):
        return None
    if M.cond5b(L, A, C) != 0:
        return None
    Nv = AI.nullspace(AI.vstack([C, CA]))
    Nmat = [[Nv[j][i] for j in range(len(Nv))] for i in range(len(A))]
    return rank(mul(L, Nmat))


def toFr(x):
    r = sympy.Rational(x)
    return Fr(int(r.p), int(r.q))


def solve_case(A, C, L0, verbose=False):
    n = len(A)
    D = M.reduced_data(A, C, L0)
    if len(L0) != 1 or not D["inV"]:
        return None
    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    d = len(Nv)
    Nmat = [[Nv[j][i] for j in range(d)] for i in range(n)]
    Ap, R0 = D["Ap"], D["R0"]
    a0 = mul(L0, Nmat)[0]
    l0r0 = mul(L0, R0)[0]
    case1 = any(x != 0 for x in a0)

    if case1:
        v = a0[:]
        w = [sum(v[i] * Ap[i][j] for i in range(d)) for j in range(d)]
        lhs = [l0r0[j] + w[j] for j in range(d)]
        k = next(j for j in range(d) if v[j] != 0)
        if not all(lhs[j] * v[k] == lhs[k] * v[j] for j in range(d)):
            if verbose:
                print("  第一行不一致：L0R0 + vA' ∉ span{v}")
            return None
        y1 = lhs[k] / v[k]
    else:
        if all(x == 0 for x in l0r0):
            if verbose:
                print("  alpha0=0 且 L0R0=0 ⟹ q=2,rho=1 无解")
            return None
        v = l0r0[:]
        w = [sum(v[i] * Ap[i][j] for i in range(d)) for j in range(d)]
        y1 = Fr(1)

    # 未知量：ell (n), y2, t（case1）
    m = n + 1 + (1 if case1 else 0)
    Aq, bq = [], []
    for k in range(d):
        row = [Fr(0)] * m
        for j in range(n):
            row[j] = Nmat[j][k]
        if case1:
            row[n + 1] = -v[k]
        Aq.append(row)
        bq.append(Fr(0) if case1 else v[k])
    for k in range(d):
        row = [Fr(0)] * m
        for j in range(n):
            row[j] = R0[j][k]
        row[n] = -v[k]
        if case1:
            row[n + 1] = w[k]
        Aq.append(row)
        bq.append(Fr(0) if case1 else -w[k])

    Msym = sympy.Matrix([[sympy.Rational(x.numerator, x.denominator) for x in r] for r in Aq])
    bsym = sympy.Matrix([sympy.Rational(x.numerator, x.denominator) for x in bq])
    solset = sympy.linsolve((Msym, bsym))
    if solset == sympy.EmptySet:
        if verbose:
            print("  线性系统无解")
        return None
    sol = list(solset)[0]
    params = sorted({s for e in sol for s in e.free_symbols}, key=str)

    # y1, y2 与 t 的表达式；开条件 E = y2 - t*y1 ≠ 0
    def E(assign):
        vals = [e.subs(assign) for e in sol]
        y2 = vals[n]
        t = vals[n + 1] if case1 else sympy.Integer(1)
        return sympy.simplify(y2 - t * y1)

    grid = [sympy.Integer(0), sympy.Integer(1), sympy.Integer(-1), sympy.Integer(2), sympy.Rational(1, 2)]
    combos = [dict(zip(params, c)) for c in itertools.product(grid, repeat=len(params))] if params else [{}]
    for assign in combos:
        if case1 and sympy.simplify(E(assign)) == 0:
            continue
        vals = [toFr(e.subs(assign)) for e in sol]
        ell = vals[:n]
        L = [row[:] for row in L0] + [ell]
        rho = check_rows(L, A, C, L0)
        if rho is not None:
            return L, rho
    if verbose:
        print("  解空间里没找到同时满足开条件 + (5a)/(5b) 的点")
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--certs", action="store_true")
    ap.add_argument("--random", type=int, default=0)
    ap.add_argument("--seed", type=int, default=41)
    ap.add_argument("--r", default="1")
    args = ap.parse_args()

    toF = lambda m: [[Fr(x) for x in row] for row in m]
    insts = []
    if args.certs or args.random == 0:
        for fn in ("certificate_middle_layer.json", "certificate_rhostar_lt_dimV.json",
                   "counterexample_refute_dimV1.json", "counterexample_candidate.json",
                   "counterexample_d4.json"):
            d0 = json.load(open(os.path.join(ROOT, "lit", fn), encoding="utf-8"))
            insts.append((fn[:-5], toF(d0["A"]), toF(d0["C"]), toF(d0["L0"])))
    if args.random:
        insts += LA.random_instances(args.random, args.seed,
                                     r_choices=tuple(int(x) for x in args.r.split(",")))

    for name, A, C, L0 in insts:
        try:
            res = solve_case(A, C, L0, verbose=True)
        except Exception as e:
            print(f"{name}: ERR {type(e).__name__}: {e}")
            continue
        if res is None:
            print(f"{name:24s} rho=1 @ q=2: 无解")
        else:
            L, rho = res
            print(f"{name:24s} rho=1 @ q=2: **构造成功** rho={rho}")


if __name__ == "__main__":
    main()
