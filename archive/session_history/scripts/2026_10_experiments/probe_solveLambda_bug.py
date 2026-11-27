# -*- coding: utf-8 -*-
"""
probe_solveLambda_bug.py —— 查 `solve_Lambda`（库包装）是否**漏解**

【动机】
  独立求解器给出：(A) ⟹ 分解存在，且 ΛH = F（I-4x4 80/80、I-5x5 50/50、II 46/46）。
  而 `batch_c6p_k.solve_Lambda`（库 `solve` 的包装）在**同一族**上大量返回"无解"✗。
  ⟹ 二者必有一个错。本脚本逐点对照，找出分歧的最小实例。
"""
import os, io, contextlib, random
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
ker_basis = _ns["ker_basis"]
lib_solve = _ns["solve"]

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
    return rows, rhs


def main():
    print("=== solve_Lambda（库包装） vs 独立求解器 ===\n")
    A = mat([[0,0,0,1],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    C = mat([[0,0,1,0]])
    n = len(A)
    B = ker_basis(stack(C, matmul(C, A)))
    rng = random.Random(11)
    shown = 0
    nA = 0
    disagree = 0
    for trial in range(4000):
        q0 = rng.choice([2, 3])
        L = [[F(rng.randint(-3, 3)) for _ in range(n)] for _ in range(q0)]
        if rk(L) != q0:
            continue
        if not condA(A, C, L):
            continue
        nA += 1
        rows, rhs = build_system(A, C, L)
        # 独立
        ind = solve_exact(rows, rhs)
        # 库
        lib = lib_solve(rows, rhs)
        s_lib = solve_Lambda_lib(A, C, L)
        if ind is None:
            continue
        H = matmul(L, B)
        Fm = matmul(matmul(L, A), B)
        Lam_ind = [[ind[0][kk * q0 + i] for kk in range(q0)] for i in range(q0)]
        ok_ind = (matmul(Lam_ind, H) == Fm)
        ok_lib = any(matmul(Lam, H) == Fm for Lam in s_lib)
        if (not ok_lib) and ok_ind:
            disagree += 1
        if shown < 3 and not ok_lib:
            shown += 1
            print("实例 q0=%d  L=%s" % (q0, [[str(x) for x in r] for r in L]))
            print("  独立：特解存在=%s  Λ=%s  ΛH==F? %s" %
                  (ind is not None, [[str(x) for x in r] for r in Lam_ind], ok_ind))
            print("  库  ：solve 返回 %s ；solve_Lambda 给出 %d 个 Λ ；有 ΛH==F? %s" %
                  ("非 None" if lib is not None else "None", len(s_lib), ok_lib))
            print("  库 solve 的零空间基个数 = %s ；独立零空间基个数 = %s" %
                  (len(lib[1]) if lib else "-", len(ind[1])))
            print()
        if nA >= 200:
            break
    print("(A)-点 %d ：库与独立**分歧**（独立有解、库无解）%d 个" % (nA, disagree))
    print()
    print("【判读】分歧 > 0 ⟹ `solve_Lambda` 会**漏解** ⟹ 依赖它的 (S) 结论可能被污染 ⚠️")


if __name__ == "__main__":
    main()
