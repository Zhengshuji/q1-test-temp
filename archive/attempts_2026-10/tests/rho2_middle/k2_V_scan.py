"""k2_V_scan.py — k=2 时 V 是否被线性结构钉住？（Q1-FALSE）

问题：k=1 时 L0 的数据把 v 定死。k=2 时 V 是含 alpha0 的 2-平面（d>=3 时是连续的）。
      线性结构（LN=UV^T, LR0=-UW^T+YV^T）是否只对个别 V 可解？

做法：固定实例，参数化 V = span{alpha0, beta(t)}，对每个 t 解 (L,U,Y) 的线性系统，
      报告是否可解。若对连续多个 t 可解 => V 没被钉住，(5a) 才是关键约束。

用法：
    python q1_false/tests/k2_V_scan.py --inst counterexample_candidate.json
"""
import sys
import os
import json
import argparse

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, "tools", "exact_linalg"))

from fractions import Fraction as Fr
import sympy
import audit_independent as AI
import c162_dimV_formula as M
import c166_layer_audit as LA

mul, rank = AI.mul, AI.rank


def toS(Mx):
    return sympy.Matrix([[sympy.Rational(x.numerator, x.denominator) for x in row] for row in Mx])


def build_system(A, C, L0, V):
    """未知量顺序：L (q*n), U (q*k), Y (q*k)。返回 (Amat, bvec, dims)。"""
    n = len(A)
    D = M.reduced_data(A, C, L0)
    Ap, R0 = D["Ap"], D["R0"]
    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    d = len(Nv)
    Nmat = [[Nv[j][i] for j in range(d)] for i in range(n)]
    q = 3
    k = 2
    dV = V                 # d×k（sympy）
    Vt = dV.T              # k×d
    # W = A'^T V（d×k）
    W = sympy.zeros(d, k)
    for j in range(d):
        for a in range(k):
            W[j, a] = sum(dV[i, a] * sympy.Rational(Ap[i][j].numerator, Ap[i][j].denominator)
                          for i in range(d))
    nL, nU, nY = q * n, q * k, q * k
    N = nL + nU + nY

    def idxL(i, j):
        return i * n + j

    def idxU(i, a):
        return nL + i * k + a

    def idxY(i, a):
        return nL + nU + i * k + a

    rows, rhs = [], []
    # LN = U V^T  (q×d)
    for i in range(q):
        for j in range(d):
            row = [0] * N
            for t in range(n):
                row[idxL(i, t)] = sympy.Rational(Nmat[t][j].numerator, Nmat[t][j].denominator)
            for a in range(k):
                row[idxU(i, a)] = -Vt[a, j]
            rows.append(row)
            rhs.append(0)
    # L R0 + U W^T - Y V^T = 0
    for i in range(q):
        for j in range(d):
            row = [0] * N
            for t in range(n):
                row[idxL(i, t)] += sympy.Rational(R0[t][j].numerator, R0[t][j].denominator)
            for a in range(k):
                row[idxU(i, a)] += W[j, a]
                row[idxY(i, a)] -= Vt[a, j]
            rows.append(row)
            rhs.append(0)
    return sympy.Matrix(rows), sympy.Matrix(rhs), (n, d, q, k)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--inst", default="counterexample_candidate.json")
    args = ap.parse_args()
    path = args.inst if os.path.isabs(args.inst) else os.path.join(ROOT, "lit", args.inst)
    d0 = json.load(open(path, encoding="utf-8"))
    toF = lambda m: [[Fr(x) for x in row] for row in m]
    A, C, L0 = toF(d0["A"]), toF(d0["C"]), toF(d0["L0"])
    n = len(A)
    D = M.reduced_data(A, C, L0)
    Nv = AI.nullspace(AI.vstack([C, mul(C, A)]))
    d = len(Nv)
    Nmat = [[Nv[j][i] for j in range(d)] for i in range(n)]
    a0 = mul(L0, Nmat)[0]
    print(f"n={n} d={d} alpha0={[str(x) for x in a0]} dimV={len(D['V'])}")

    # 参数化：V 的列 = [alpha0, beta(t)]，beta 在 R^d 里取一个补空间的方向
    a0v = sympy.Matrix([sympy.Rational(x.numerator, x.denominator) for x in a0])
    # 取 e_i 中与 a0 线性无关的组成补空间基
    comp = []
    for i in range(d):
        e = sympy.zeros(d, 1)
        e[i] = 1
        if sympy.Matrix.hstack(a0v, *comp, e).rank() == len(comp) + 2:
            comp.append(e)
        if len(comp) == d - 1:
            break
    print(f"补空间维数 {len(comp)}")

    tvals = [sympy.Integer(x) for x in (-3, -2, -1, 0, 1, 2, 3)] + \
            [sympy.Rational(1, 3), sympy.Rational(-1, 3), sympy.Rational(2, 5),
             sympy.Rational(-2, 5), sympy.Rational(3, 7), sympy.Rational(5, 2)]
    for t in tvals:
        beta = comp[0] if len(comp) == 1 else comp[0] + t * comp[1]
        if len(comp) == 1:
            beta = comp[0]
        Vcols = sympy.Matrix.hstack(a0v, beta)
        if Vcols.rank() != 2:
            print(f"  t={t}: V 退化")
            continue
        Amat, bvec, dims = build_system(A, C, L0, Vcols)
        try:
            sol = sympy.linsolve((Amat, bvec))
            ok = sol != sympy.EmptySet
        except Exception as e:
            ok = f"ERR {e}"
        extra = ""
        if ok is True:
            s = list(sol)[0]
            free = sorted({x for e in s for x in e.free_symbols}, key=str)
            n_, d_, q_, k_ = dims
            import random as _rnd
            _rng = _rnd.Random(0)
            seen = good = 0
            for _try in range(60):
                asg = {p: sympy.Integer(_rng.randint(-3, 3)) for p in free}
                s0 = [e.subs(asg) for e in s]
                Lm = [[Fr(int(sympy.Rational(s0[i * n_ + j]).p), int(sympy.Rational(s0[i * n_ + j]).q))
                       for j in range(n_)] for i in range(q_)]
                if rank(Lm) != q_:
                    continue
                seen += 1
                if M.cond5b(Lm, A, C) == 0:
                    good += 1
            extra = f"  满秩样本 {seen} 个，其中 (5b) 成立 {good} 个"
        print(f"  t={t}: 可解? {ok}{extra}")


if __name__ == "__main__":
    main()
