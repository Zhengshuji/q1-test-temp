# -*- coding: utf-8 -*-
"""
diag_Lambda_map.py —— 定位 Λ 抽取的**映射**问题（第 3 层排查）

关键：`solve_Lambda` 用  Lam[i][k] = sol[k*r + i]  取 Λ。
本脚本直接验证：对同一条 sol 向量，**两种**索引约定下 ΛH = F 哪一个成立。
"""
import os, io, contextlib
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
ker_basis = _ns["ker_basis"]

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
    return rows, rhs


def main():
    A = mat([[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    C = mat([[0,0,1,0]])
    L = mat([['3','1','3','3'],['0','0','1','3'],['1','-2','-2','3']])
    q0 = len(L)
    B = ker_basis(stack(C, matmul(C, A)))
    H = matmul(L, B)
    Fm = matmul(matmul(L, A), B)
    print("H =", [[str(x) for x in r] for r in H])
    print("F =", [[str(x) for x in r] for r in Fm])
    print()
    rows, rhs = build_system(A, C, L)
    ind = solve_exact(rows, rhs)
    sols = [ind[0]] + list(ind[1])
    print("解的条数 = %d ；未知量 = %d ；q0 = %d" % (len(sols), len(rows[0]), q0))
    print()
    for si, sol in enumerate(sols):
        Lam_a = [[sol[k * q0 + i] for k in range(q0)] for i in range(q0)]   # solve_Lambda 的约定
        Lam_b = [[sol[i * q0 + k] for k in range(q0)] for i in range(q0)]   # 转置约定
        print("解 %d ：前 %d 个分量（Λ 部分）= %s" %
              (si, q0 * q0, [str(x) for x in sol[:q0 * q0]]))
        print("   约定A Λ =", [[str(x) for x in r] for r in Lam_a], " ΛH==F ?", matmul(Lam_a, H) == Fm)
        print("   约定B Λ =", [[str(x) for x in r] for r in Lam_b], " ΛH==F ?", matmul(Lam_b, H) == Fm)
    print()
    libs = solve_Lambda_lib(A, C, L)
    print("库 solve_Lambda 返回 %d 个 Λ ；其中有 ΛH==F 的：%s"
          % (len(libs), any(matmul(Lm, H) == Fm for Lm in libs)))
    for Lm in libs:
        print("   库 Λ =", [[str(x) for x in r] for r in Lm], " ΛH==F ?", matmul(Lm, H) == Fm)


if __name__ == "__main__":
    main()
