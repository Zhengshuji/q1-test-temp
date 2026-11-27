# -*- coding: utf-8 -*-
"""c6_witness_inv.py -- 见证的相容性检查：K 是否 A-不变？"""
import json, os, io, contextlib
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
ns = {}
with open(os.path.join(HERE, "exact_count_thm7.py"), encoding="utf-8") as f:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(f.read(), "lib", "exec"), ns)
rk = ns["rk"]; mm = ns["mm"]; ker_basis = ns["ker_basis"]

with open(os.path.join(HERE, "witness_caseII_parallel_YES.json"), encoding="utf-8") as f:
    w = json.load(f)
A = [[F(x) for x in r] for r in w["A"]]
C = [[F(x) for x in r] for r in w["C"]]
n = w["n"]
W = C + mm(C, A)
N = ker_basis(W)
d = len(N[0])
AN = mm(A, N)
cj = [[N[i][j] for j in range(d)] + [AN[i][j] for j in range(d)] for i in range(n)]
print("d_CA =", d)
print("rk(N) =", rk(N), " rk([N|AN]) 列拼接 =", rk(cj))
print("K 是 A-不变？", rk(cj) == rk(N))
CA = mm(C, A)
CA2N = mm(mm(CA, A), N)
print("CA^2|_K 是否 = 0？", all(all(x == 0 for x in r) for r in CA2N))
print()
print("【相容性判读】")
print("  见证的 (5b) 成立；而 Lean 定理 c6'_of_fact_algclosed 说")
print("  (A) + A-不变 + H≠0  ⟹  (S) 失败  ⟹  (5b) 失败")
print("  ⟹ **见证的 K 必须是 NOT A-不变**，否则矛盾！")
