# -*- coding: utf-8 -*-
"""verify_solve.py —— 用独立例程裁判库的 solve（CLAUDE.md §10）"""
import os, io, contextlib
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src, "lib", "exec"), _ns)

lib_solve = _ns["solve"]
lib_mm = _ns["mm"]
lib_ker = _ns["ker_basis"]

_ns2 = {}
with open(os.path.join(_HERE, "linalg_exact.py"), encoding="utf-8") as fh:
    exec(compile(fh.read(), "lx", "exec"), _ns2)
solve_exact = _ns2["solve_exact"]
rank_exact = _ns2["rank_exact"]


def mat(rows):
    return [[F(x) for x in r] for r in rows]


A = mat([[0, 1, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0],
         [0, 0, 0, 1, 0, 0],
         [0, 0, 0, 1, 1, 0],
         [0, 0, 0, 0, 2, 1],
         [1, 1, 0, 0, 0, 1]])
C = mat([[1, 0, 0, 0, 0, 0]])

CCA = C + lib_mm(C, A)
B = lib_ker(CCA)
n, d = len(B), len(B[0])
print("n=%d d_CA=%d" % (n, d))
print("独立 rank(B)      =", rank_exact(B))
print("独立 rank([B;AB]) =", rank_exact(B + lib_mm(A, B)))

DesB = [[B[t][i] for i in range(d)] for t in range(n)]
AB = lib_mm(A, B)

print()
print("=== 逐列对比：库 solve  vs  独立 solve_exact ===")
Mcols_lib, Mcols_ind = [], []
for j in range(d):
    b = [[AB[t][j]] for t in range(n)]
    rl = lib_solve(DesB, b)
    ri = solve_exact(DesB, b)
    tl = "OK" if rl is not None else "FAIL"
    ti = "OK" if ri is not None else "FAIL"
    flag = "  <== 分歧!" if (rl is None) != (ri is None) else ""
    print("  col %d: 库=%-4s 独立=%-4s%s" % (j, tl, ti, flag))
    if rl is not None:
        Mcols_lib.append(rl[0])
    if ri is not None:
        Mcols_ind.append(ri[0])

# 用独立解组装 M，并验证 A·B = B·M
if len(Mcols_ind) == d:
    M = [[Mcols_ind[j][i] for j in range(d)] for i in range(d)]
    lhs = lib_mm(A, B)
    rhs = lib_mm(B, M)
    print()
    print("用**独立解**组装 M 后，A·B == B·M ？", lhs == rhs)
    if lhs != rhs:
        print("  A·B =", [[int(x) for x in r] for r in lhs])
        print("  B·M =", [[int(x) for x in r] for r in rhs])
    else:
        print("  ✓ 说明库 solve 的 FAIL 是**误报**，独立例程正确")
        print("  M =", [[int(x) for x in r] for r in M])
