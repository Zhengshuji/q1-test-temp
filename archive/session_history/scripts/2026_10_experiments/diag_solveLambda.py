# -*- coding: utf-8 -*-
"""
diag_solveLambda.py —— 逐解对照：库 `solve` 的解集 vs 独立求解器的解集

上一个脚本按"y=0"找证书失败了 ⟹ bug 的机制不是我最初以为的那样。
本脚本对同一个具体实例，把所有解向量逐条列出，找出**分歧的确切位置**。
"""
import os, io, contextlib
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
ker_basis = _ns["ker_basis"]
lib_solve = _ns["solve"]
lib_rref = _ns["rref"]

_ns2 = {}
with open(os.path.join(_HERE, "linalg_exact.py"), encoding="utf-8") as fh:
    exec(compile(fh.read(), "lx", "exec"), _ns2)
rank_exact, solve_exact, matmul = _ns2["rank_exact"], _ns2["solve_exact"], _ns2["matmul"]

_ns3 = {"__file__": os.path.join(_HERE, "batch_c6p_k.py")}
with open(os.path.join(_HERE, "batch_c6p_k.py"), encoding="utf-8") as fh:
    exec(compile(fh.read().split("def main()")[0], "helpers", "exec"), _ns3)
mat = _ns3["mat"]
solve_Lambda_lib = _ns3["solve_Lambda"]


def stack(*Ms):
    out = []
    for M in Ms:
        if not M:
            continue
        if out:
            assert len(out[0]) == len(M[0]), "stack 列数不一致"
        out += [r[:] for r in M]
    return out


def rk(M):
    return rank_exact(M)


def condA(A, C, L):
    CA = matmul(C, A)
    return rk(stack(matmul(L, A), L, C, CA)) == rk(stack(L, C, CA))


def build_system(A, C, L):
    q0, n, p = len(L), len(A), len(C)
    CA = matmul(C, A)
    LA = matmul(L, A)
    nunk = q0 * q0 + 2 * q0 * p
    rows, rhs = [], []
    for i in range(q0):
        for j in range(n):
            row = [F(0)] * nunk
            for kk in range(q0):
                row[kk * q0 + i] = L[kk][j]
            for m in range(p):
                row[q0 * q0 + i * p + m] = C[m][j]
            for m in range(p):
                row[q0 * q0 + q0 * p + i * p + m] = CA[m][j]
            rows.append(row)
            rhs.append([LA[i][j]])
    return rows, rhs, nunk


def resid(rows, rhs, x):
    return [sum(rows[i][j] * x[j] for j in range(len(x))) - rhs[i][0] for i in range(len(rows))]


def main():
    A = mat([[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    C = mat([[0,0,1,0]])
    L = mat([['3','1','3','3'],['0','0','1','3'],['1','-2','-2','3']])
    print("实例：A =", [[str(x) for x in r] for r in A])
    print("      C =", [[str(x) for x in r] for r in C])
    print("      L =", [[str(x) for x in r] for r in L])
    print("(A) 成立？", condA(A, C, L))
    rows, rhs, nunk = build_system(A, C, L)
    print("未知量个数 = %d ；方程个数 = %d ；系数矩阵秩 = %d" % (nunk, len(rows), rk(rows)))
    print()

    lib = lib_solve(rows, rhs)
    ind = solve_exact(rows, rhs)
    print("库 solve  ：特解 y 全零=%s ；零空间基 %d 个" %
          (not any(x != 0 for x in lib[0]), len(lib[1])))
    print("独立 solve：特解 y 全零=%s ；零空间基 %d 个" %
          (not any(x != 0 for x in ind[0]), len(ind[1])))
    print()
    print("库特解  残差全零？", all(x == 0 for x in resid(rows, rhs, lib[0])))
    print("独立特解残差全零？", all(x == 0 for x in resid(rows, rhs, ind[0])))
    print()
    print("【库 solve 的零空间基】")
    for v in lib[1]:
        print("   ", [str(x) for x in v], " 残差全零？", all(x == 0 for x in resid(rows, rhs, v)))
    print("【独立 solve 的零空间基】")
    for v in ind[1]:
        print("   ", [str(x) for x in v], " 残差全零？", all(x == 0 for x in resid(rows, rhs, v)))
    print()
    print("【关键】库的『特解+零空间基』张成的空间 vs 独立的：")
    lib_all = ([lib[0]] if any(x != 0 for x in lib[0]) else []) + list(lib[1])
    ind_all = [ind[0]] + list(ind[1])
    print("  库解的个数 = %d ；独立解的个数 = %d" % (len(lib_all), len(ind_all)))
    for tag, vs in (("库", lib_all), ("独立", ind_all)):
        M = [v[:] for v in vs]
        print("  %s：秩 = %d" % (tag, rk(M) if M else 0))


if __name__ == "__main__":
    main()
