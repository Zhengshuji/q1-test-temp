# -*- coding: utf-8 -*-
"""
gen_parallel4.py —— 真平行实例构造（终版）

原理（见 CLAUDE.md §9）：
  K := ker[C;CA] 若 A-不变，记 A' = A|_K，其在基 B 下的矩阵为 M（满足 A·B = B·M）。
  对任意行 l：  lB = u  ⟹  lAB = u·M
  故只要 u 是 M 的左特征向量（u M = lam·u），就有 lAB = lam·u ∥ lB ⟹ 真平行 ✓
  而 l ↦ lB 满射到 K ⟹ 这样的 l 总存在；且解空间维数 = n - d + 1 ⟹ 可取多行 ⟹ r>=2 ✓
"""
import os, io, contextlib, itertools
from fractions import Fraction

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
    P0 = mm(L0, B); PA = mm(mm(L0, A), B)
    if not any(x != 0 for r in P0 for x in r):
        return False
    return rk(P0 + PA) == 1


def main():
    print("=== 真平行实例构造 v4 ===")
    # 块下三角：第二块上三角（有理对角）⟹ A' 的特征值有理 ⟹ 特征向量存在
    A = mat([[0, 1, 0,  0, 0, 0],
             [0, 0, 1,  0, 0, 0],
             [0, 0, 0,  1, 0, 0],
             [0, 0, 0,  1, 1, 0],
             [0, 0, 0,  0, 2, 1],
             [1, 1, 0,  0, 0, 1]])
    C = mat([[1, 0, 0, 0, 0, 0]])
    n = len(A); d_expected = None

    B = ker_basis(C + mm(C, A))
    nrow, d = len(B), len(B[0])
    print("n=%d  d_CA=%d" % (nrow, d))
    print("K 是 A-不变的吗？%s" % (rk(B) == rk(B + mm(A, B))))

    # 1) 求 M：解 B·M = A·B（逐列）
    DesB = [[B[t][i] for i in range(d)] for t in range(nrow)]
    AB = mm(A, B)
    Mcols = []
    for j in range(d):
        r = solve(DesB, [[AB[t][j]] for t in range(nrow)])
        if r is None:
            print("M 求解失败"); return []
        Mcols.append(r[0])
    M = [[Mcols[j][i] for j in range(d)] for i in range(d)]

    # 2) 找 M 的有理特征向量：lam 遍历小有理数
    lams = [F(k) for k in range(-3, 4)] + [F(1, 2), F(-1, 2), F(3, 2)]
    eigs = []
    for lam in lams:
        N = [[M[i][j] - (lam if i == j else 0) for j in range(d)] for i in range(d)]
        r = solve(N, [[F(0)] for _ in range(d)])
        if r is None:
            continue
        y, ns = r
        vecs = list(ns)
        if any(x != 0 for x in y):
            vecs.append(y)
        for v in vecs:
            if any(x != 0 for x in v):
                eigs.append((lam, v))
    print("找到 %d 个（有理）特征方向" % len(eigs))

    # 3) 对每个特征方向造 L0（可多行：lB = alpha*u 的解空间）
    hits = []
    for lam, v in eigs:
        # u = B·v^T （左特征向量 u 满足 uM = lam u；此处用 v 作为坐标）
        u = [sum(B[i][j] * v[j] for j in range(d)) for i in range(nrow)]
        if not any(x != 0 for x in u):
            continue
        # 解 l·B = u  （d 方程, n 未知）
        DesL = [[B[j][t] for j in range(nrow)] for t in range(d)]
        bL = [[u[t]] for t in range(d)]
        r3 = solve(DesL, bL)
        if r3 is None:
            continue
        l0, nsol = r3
        rows = []
        if any(x != 0 for x in l0):
            rows.append(l0)
        for w in nsol:
            if any(x != 0 for x in w):
                rows.append(w)
        # 单行实例
        if rows:
            L0 = [rows[0]]
            if is_tp(L0, A, B):
                hits.append(("r=1", lam, L0))
        # 两行实例（从解空间取两行，检查完整平行判据）
        if len(rows) >= 2:
            L0 = [rows[0], rows[1]]
            if is_tp(L0, A, B):
                hits.append(("r=2", lam, L0))

    print()
    print("=== 结果：真平行实例 %d 个 ===" % len(hits))
    for tag, lam, L0 in hits[:6]:
        P0 = mm(L0, B)
        print("  [%s] lam=%s  rank(Pi(L0))=%d  Pi(L0)=%s" %
              (tag, lam, rk(P0), [[int(x) for x in r] for r in P0]))
        print("        L0=%s" % [[int(x) for x in r] for r in L0])
    return hits


if __name__ == "__main__":
    main()
