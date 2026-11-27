# -*- coding: utf-8 -*-
"""
D6_hand.py -- 手算小例验证"q0 = 最小 Ā-不变子空间维数"

【例】A = [[0,1,0],[0,0,0],[0,0,2]]，C = [1,0,0]（p=1）
   C  = span{e1}                                  rank 1
   CA = [0,1,0]                                   rank 2
   CA² = [0,0,0]                                  rank 2
   ⟹ C := row[C;CA;CA²] = span{e1,e2}，rank 2，d_CA = 1
   商 V/C 中：ē3 ≠ 0，Ā(ē3) = 2ē3 ⟹ Ā = 2 在商上

   取 L0 = C·A = [0,1,0]（r=1）
   ⟹ L̄0 = 0（因 L0 = CA ∈ C）✗ —— 这例子 L0 ∈ C，不适用

【换】A = [[0,1,0],[0,0,0],[0,0,2]]，C = [1,0,0]，L0 = [0,0,1]（= e3）
   L0 ∉ C = span{e1,e2} ✓  d_CA = 1
   L̄0 = ē3 ≠ 0 ⟹ dim(L̄0) = 1
   Ā ē3 = 2ē3 ⟹ 含 ē3 的最小不变子空间 = span{ē3}，维数 1
   ⟹ minInvDim = 1

   期望 q0 = 1（若 r=1, η=1）
"""
import os, io, contextlib
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]

A = [[F(0), F(1), F(0)], [F(0), F(0), F(0)], [F(0), F(0), F(2)]]
C = [[F(1), F(0), F(0)]]
L0 = [[F(0), F(0), F(1)]]

print("=== 手算小例 ===\n")
print("A =", [[str(x) for x in r] for r in A])
print("C =", [[str(x) for x in r] for r in C])
print("L0 =", [[str(x) for x in r] for r in L0])
print()
Csp = [r[:] for r in C]
cur = [r[:] for r in C]
for k in range(2):
    cur = mm(cur, A)
    print("CA^%d =" % (k + 1), [[str(x) for x in r] for r in cur])
    Csp = Csp + cur
rC = rk(Csp)
n = 3
print()
print("rk(Cspace) =", rC, " d_CA =", n - rC)
print("rk([L0; Cspace]) =", rk(L0 + Csp), " ⟹ dim(L̄0) =", rk(L0 + Csp) - rC)
print()
# 迭代
W = [r[:] for r in L0]
d_prev = rk(W + Csp) - rC
print("init dim(W̄) =", d_prev)
for step in range(4):
    W = W + mm(W, A)
    d_new = rk(W + Csp) - rC
    print("step %d: dim(W̄) = %d" % (step, d_new))
    if d_new == d_prev:
        break
    d_prev = d_new
print()
print("⟹ minInvDim =", d_prev)
print("   这与 '最小 (A)-增广行数' 应当一致")
