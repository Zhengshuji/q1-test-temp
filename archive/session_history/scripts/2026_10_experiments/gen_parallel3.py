# -*- coding: utf-8 -*-
"""
gen_parallel3.py —— 真平行实例构造（最终版：A-不变核 + 特征方向）

【核心洞察】
  若 K := ker[C;CA] 是 A-不变的，记 A' = A|_K。
  则  l B = u  ⟹  l A B = u A'。
  故只要 **u 是 A' 的特征向量**，就有 lAB ∥ lB ∥ u ⟹ 真平行 ✓
  而 l ↦ lB 满射到 im B = K ⟹ 这样的 l 总存在 ✓

【A-不变核怎么造】
  A 取块下三角 [[A11,A12],[0,A22]]，C = [C1,0] ⟹ ker[C;CA] ⊇ 第 2 块。
"""
import os
import io
import contextlib
import itertools

_HERE = os.path.dirname(os.path.abspath(__file__))
_LIB = os.path.join(_HERE, "exact_count_thm7.py")
_ns = {}
with open(_LIB, "r", encoding="utf-8") as fh:
    _src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(_src, _LIB, "exec"), _ns)

F, rk, mm, ker_basis, solve = _ns["F"], _ns["rk"], _ns["mm"], _ns["ker_basis"], _ns["solve"]


def mat(rows):
    return [[F(x) for x in r] for r in rows]


def is_tp(L0, A, B):
    """真平行：rank[Pi(L0); Pi(L0 A)] == 1 且 Pi(L0) != 0"""
    P0 = mm(L0, B)
    PA = mm(mm(L0, A), B)
    if not any(x != 0 for r in P0 for x in r):
        return False
    return rk(P0 + PA) == 1


def main():
    print("=== 真平行实例构造 v3 ===")
    A = mat([[0, 1, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0],
             [0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 0],
             [0, 0, 0, 0, 0, 1],
             [1, 1, 0, 0, 0, 0]])
    C = mat([[1, 0, 0, 0, 0, 0]])
    n = len(A)

    B = ker_basis(C + mm(C, A))
    d = len(B[0])
    print("n=%d  d_CA=%d" % (n, d))

    # A-不变性检查
    print("K 是 A-不变的吗？%s" % (rk(B) == rk(B + mm(A, B))))

    # 解 B*y = rhs 的工具矩阵（n 方程, d 未知）
    DesB = [[B[t][i] for i in range(d)] for t in range(n)]

    hits = []
    for coefT in itertools.product([0, 1, -1, 2], repeat=d):
        if not any(coefT):
            continue
        coef = [F(x) for x in coefT]
        u = [sum(coef[i] * B[j][i] for i in range(d)) for j in range(n)]
        uA = [sum(u[j] * A[j][i] for j in range(n)) for i in range(n)]
        r2 = solve(DesB, [[uA[t]] for t in range(n)])
        if r2 is None:
            continue
        yv = r2[0]
        if rk([coef, yv]) > 1:      # uA 不平行 u
            continue
        # 造 l: 解 l*B = u   (d 方程, n 未知)
        DesL = [[B[j][t] for j in range(n)] for t in range(d)]
        bL = [[u[t]] for t in range(d)]
        r3 = solve(DesL, bL)
        if r3 is None:
            continue
        l = r3[0]
        if all(x == 0 for x in l):
            continue
        L0 = [l]
        ok = is_tp(L0, A, B)
        print("  coef=%-16s u=%s" % ([int(x) for x in coefT], [int(x) for x in u]))
        print("      -> l=%s  真平行=%s  rank(Pi(L0))=%d" % ([int(x) for x in l], ok, rk(mm(L0, B))))
        if ok:
            hits.append((coefT, l))
        if len(hits) >= 3:
            break

    print()
    print("=== 结果：构造到真平行实例 %d 个 ===" % len(hits))
    for c, l in hits:
        print("   coef=%s  l=%s" % ([int(x) for x in c], [int(x) for x in l]))
    return hits


if __name__ == "__main__":
    main()
