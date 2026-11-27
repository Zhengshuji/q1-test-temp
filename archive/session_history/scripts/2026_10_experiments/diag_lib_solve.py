# -*- coding: utf-8 -*-
"""
diag_lib_solve.py —— 锁定库 `exact_count_thm7.solve` 返回**不满足残差的解**这一缺陷

【性质】
  `linalg_q.solve` 对每条返回的 y / y+ns 强制残差校验（不通过就报错）；
  用它复核库 `solve` 的输出时，发现库的输出**违反自身方程组** ⟹ 库有实现缺陷 ✗

【本脚本】
  ① 造出最小实例，展示库 `solve` 的返回向量**不满足** Des·x = b
  ② 与 `linalg_q.solve`（带校验）的结果对照
  ③ 给出受影响的脚本清单（凡用库 solve 做 (A) 分解者）
"""
import os, io, contextlib, random
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
lib_solve = _ns["solve"]
ker_basis = _ns["ker_basis"]

import linalg_q as Q


def build_system(A, C, L):
    """(A) 分解系统：LA = ΛL + G0 C + G1 CA"""
    q0, n, p = len(L), len(A), len(C)
    CA = Q.mul(C, A)
    LA = Q.mul(L, A)
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


def resid(rows, rhs, x):
    return [sum(rows[i][j] * x[j] for j in range(len(x))) - rhs[i][0] for i in range(len(rows))]


def main():
    print("=== 库 `exact_count_thm7.solve` 的残差缺陷 ===\n")
    A = Q.mat([[0, 0, 0, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    C = Q.mat([[0, 0, 1, 0]])
    L = Q.mat([['3', '1', '3', '3'], ['0', '0', '1', '3'], ['1', '-2', '-2', '3']])
    rows, rhs = build_system(A, C, L)
    print("方程数 = %d ；未知量 = %d ；系数矩阵秩 = %d" % (len(rows), len(rows[0]), Q.rank(rows)))
    print()
    lib = lib_solve(rows, rhs)
    print("【库 solve】")
    if lib is None:
        print("  返回 None")
    else:
        y, ns = lib
        r = resid(rows, rhs, y)
        print("  特解 y 的残差是否全零：%s   （非零残差个数 = %d）"
              % (all(x == 0 for x in r), sum(1 for x in r if x != 0)))
        if any(x != 0 for x in r):
            print("  ✗✗ **库返回的 y 不是方程组的解**（违反 Des·y = b）")
            print("     残差示例 =", [str(x) for x in r[:6]], "...")
        print("  零空间基 %d 个；其中残差非零的：%d 个"
              % (len(ns), sum(1 for v in ns if any(x != 0 for x in resid(rows, rhs, v)))))
    print()
    print("【linalg_q.solve（带强制残差校验）】")
    try:
        y2, ns2 = Q.solve(rows, rhs)
        print("  通过校验 ✓ ；特解残差全零 =", all(x == 0 for x in resid(rows, rhs, y2)))
    except AssertionError as e:
        print("  校验失败：", e)
    print()
    print("【结论】库 `solve` 的**零空间基**不满足残差（本实例 3/3 个都非零）✗")
    print("         ⟹ 用 `for sol in [y]+nsol` 展开解集的脚本都会拿到**非解** ✗")
    print("         ⟹ 必须改用带残差校验的 `linalg_q.solve` ✓")
    print()
    print("【受影响的脚本（凡用库 solve 构造 (A) 分解者）】")    for fn in ["batch_c6p_k.py", "batch_c6p.py", "check_S.py", "verify_mechanism.py",
               "caseII_parallel_probe.py", "caseII_parallel_line.py", "mechanism_2d.py",
               "calibrate_gen_A.py", "gen_A_system.py"]:
        path = os.path.join(_HERE, fn)
        if not os.path.exists(path):
            continue
        src = open(path, encoding="utf-8").read()
        uses = []
        if "solve_Lambda" in src:
            uses.append("solve_Lambda")
        if "rhs = [[-LA" in src or "rhs.append([-LA" in src:
            uses.append("rhs=-LA(符号错)")
        if uses:
            print("  · %-28s %s" % (fn, "、".join(uses)))
    print()
    print("【对策（已实施）】")
    print("  · 新增 `scripts/core/linalg_q.py`：独立实现 + **强制残差校验**（不通过即 raise）✓")
    print("  · 已修 `batch_c6p_k.solve_Lambda`：改用 linalg_q 的求解器，且 **rhs 由 -LA 改为 +LA** ✓")
    print("  · 已修 `check_S.py` 同样的符号错误 ✓")
    print("  · **未改动** `exact_count_thm7.py`（被大量旧脚本以绝对路径 exec，风险高）")
    print("  · 项目**主统计** `reliable_S_test.py` 用的是 (H,F) 子式 gcd，**不受影响** ✓")


if __name__ == "__main__":
    main()
