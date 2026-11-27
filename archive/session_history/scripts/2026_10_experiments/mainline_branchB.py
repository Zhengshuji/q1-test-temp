# -*- coding: utf-8 -*-
"""
mainline_branchB.py —— 回到主线：支 B 上 (A)∧(S) 是否可能非空？

【精确做法（分段线性）】
  对固定 J，(A) 的条件是 rank M_J(Θ) ≤ ρ，其中 M_J(Θ) 对 Θ **仿射**。
  Θ 的**阶梯分区**（semi-algebraic cell decomposition 的线性版）：
    在 Θ 上采样，记录"哪些 (ρ+1)-子式为零"的模式（sign pattern），
    每个模式对应一个**开区域**；在区域内部，条件 (A) 要么恒成立、要么恒不成立。
  ⟹ 只要在每个模式的一个代表点上做**精确**检验，就覆盖了所有区域 ✓

【同时检验 (S)】
  称 $(A)$-点 Θ 是"谱可行"若存在 Λ 使 LA = ΛL + G₀C + G₁CA 且
  rank(λH-ΛH) = rank(H) ∀λ（(S)）。
"""
import os, io, contextlib, itertools, random, sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]

# 可靠 (S) 判据
_ss = {}
with open(os.path.join(_HERE, "reliable_S_test.py"), encoding="utf-8") as fh:
    src = fh.read()
print("[info] reliable_S_test.py 前 40 行：")
print("\n".join(src.split("\n")[:12]))
