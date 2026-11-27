# -*- coding: utf-8 -*-
"""
verify_A_T5a.py —— 验证关键构造：
  取满足 (A) 的 L，再补一行 l ∈ row[C;CA]，则 (A) 保持 ✓ 且 T5a 自动成立 ✓
（若成立 ⟹ 情形 II 平行 的 (A)∧T5a **可为 YES** ⟹ c6 被否定）
"""
import os, io, contextlib, itertools
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    s = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(s, "lib", "exec"), _ns)
mm, ker = _ns["mm"], _ns["ker_basis"]

_ns2 = {}
with open(os.path.join(_HERE, "linalg_exact.py"), encoding="utf-8") as fh:
    exec(compile(fh.read(), "lx", "exec"), _ns2)
rk2, se, mm2 = _ns2["rank_exact"], _ns2["solve_exact"], _ns2["matmul"]


def mat(r):
    return [[F(x) for x in q] for q in r]


def checkA(A, C, L):
    LA = mm2(L, A)
    return rk2(LA + L + C + mm2(C, A)) == rk2(L + C + mm2(C, A))


def main():
    print("=== 验证：补一行 l ∈ row[C;CA] 后 (A) 保持 ⟹ (A)∧T5a 可为 YES ===\n")
    A = mat([[0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0]])
    C = mat([[0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 0]])
    CA = mm2(C, A)
    R = C + CA                      # row[C;CA]
    n = len(A)
    B = ker(R)                      # N_CA
    d = len(B[0])
    print("n=%d  d_CA=%d  rank[C;CA]=%d" % (n, d, rk2(R)))

    # (i) 先找一个满足 (A) 且 Pi ≠ 0 的行 L
    # l ∈ row[C;CA] 的行：由 R 的行线性组合生成
    rows_in_R = [r[:] for r in R]                     # 直接用 R 的行
    base = None
    # 候选：任意向量（用标准基 + 组合扫）——这里直接用 gen_parallel5 得到的 l0
    l0 = [F(1), F(0), F(0), F(0), F(0), F(0)]
    if checkA(A, C, [l0]):
        base = l0
        print("基础行 l0=%s 满足 (A) ✓   Pi(l0)=%s" %
              ([str(x) for x in l0], [str(x) for x in mm2([l0], B)[0]]))

    if base is None:
        print("未找到基础行 ✗"); return

    print("\n--- 补一行 l ∈ row[C;CA]，检查 (A) 是否保持、T5a 是否成立 ---")
    found = []
    # row[C;CA] 中所有非零行的组合（用 R 的行及其简单组合）
    pool = []
    for r in rows_in_R:
        pool.append(r)
    for a, b in itertools.combinations(range(len(rows_in_R)), 2):
        pool.append([rows_in_R[a][i] + rows_in_R[b][i] for i in range(n)])
        pool.append([rows_in_R[a][i] - rows_in_R[b][i] for i in range(n)])
    for l in pool:
        if all(x == 0 for x in l):
            continue
        L = [base, l]
        PiL = mm2(L, B)
        t5a = rk2(PiL) < 2
        okA = checkA(A, C, L)
        gp = rk2(PiL + mm2(mm2(L, A), B)) == 1
        flag = ""
        if okA and t5a:
            flag = "   <=== (A) ∧ T5a ✓✓"
            found.append(L)
        print("  l=%-28s (A)=%-5s T5a=%-5s 真平行=%-5s%s" %
              (str([str(x) for x in l]), okA, t5a, gp, flag))
        if len(found) >= 3:
            break

    print("\n=== 结论 ===")
    if found:
        print("✅ 找到 %d 个同时满足 (A) ∧ T5a 的两行实例：" % len(found))
        for L in found:
            print("   L0 = %s" % [[str(x) for x in r] for r in L])
            print("       Pi(L0) = %s   rank=%d" %
                  ([[str(x) for x in r] for r in mm2(L, B)], rk2(mm2(L, B))))
        print()
        print("⟹ **情形 II 平行 的 (A)∧T5a 可为 YES** ⟹ c6（平行⟹恒 NO）被否定 ✗")
    else:
        print("未找到 —— 需扩大 l 的搜索范围")
    return found


if __name__ == "__main__":
    main()
