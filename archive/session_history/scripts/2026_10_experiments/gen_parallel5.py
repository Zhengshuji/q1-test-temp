# -*- coding: utf-8 -*-
"""
gen_parallel5.py —— 真平行实例构造（**保证成功**版）

【数学依据】
  K := ker[C;CA] 是 A-不变的  ⟺  K ⊆ ker[CA^2]
  ⟹ 取 A^2 = 0 就**自动**保证不变性 ✓（因为 CA^2 = 0 ✓）
  ⟹ 且 A' := A|_K 满足 A'^2 = 0 ⟹ 特征值全 0 ⟹ **有理特征向量必存在** ✓

【正确的判据】（见 CLAUDE.md §11，第 21 处更正）
  判 im(AB) ⊆ im(B) 必须用**列拼接**：  rk([B | AB]) == rk(B)      ✗ 不可用行堆叠
"""
import os, io, contextlib
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


def hcat(X, Y):
    """列拼接 [X | Y]"""
    assert len(X) == len(Y)
    return [X[i] + Y[i] for i in range(len(X))]


def im_in(X, Y):
    """im(X) ⊆ im(Y) ？（用**列拼接**判据 ✓）"""
    return rk2(hcat(Y, X)) == rk2(Y)


def is_tp(L0, A, B):
    P0 = mm2(L0, B)
    PA = mm2(mm2(L0, A), B)
    if not any(x != 0 for r in P0 for x in r):
        return False
    return rk2(P0 + PA) == 1


def main():
    print("=== 真平行实例构造 v5（A^2=0 保证成功）===")
    n = 6
    # A^2 = 0：块 [[0, M],[0, 0]]，M 为 3x3 任意
    A = mat([[0, 0, 0,  1, 0, 0],
             [0, 0, 0,  0, 1, 0],
             [0, 0, 0,  0, 0, 1],
             [0, 0, 0,  0, 0, 0],
             [0, 0, 0,  0, 0, 0],
             [0, 0, 0,  0, 0, 0]])
    # 自检 A^2 = 0
    A2 = mm2(A, A)
    print("A^2 == 0 ？", all(x == 0 for r in A2 for x in r))

    C = mat([[0, 0, 0, 1, 0, 0],
             [0, 0, 0, 0, 1, 0]])
    CCA = C + mm2(C, A)
    B = ker(CCA)
    nrow, d = len(B), len(B[0])
    print("n=%d p=%d  d_CA=%d" % (n, len(C), d))

    AB = mm2(A, B)
    print("【正确判据·列拼接】im(AB) ⊆ im(B) ？", im_in(AB, B))

    # 若不变：对每一列 u = B 的列，找 l 使 lB = u
    hits = []
    for j in range(d):
        u = [B[i][j] for i in range(nrow)]
        # 解 l·B = u  （d 方程，n 未知）—— 用独立例程
        DesL = [[B[i][t] for i in range(nrow)] for t in range(d)]
        bL = [[u[t]] for t in range(d)]
        r3 = se(DesL, bL)
        if r3 is None:
            print("  u%d: 无解 ✗" % j)
            continue
        l0, nsol = r3
        rows = ([l0] if any(x != 0 for x in l0) else []) + [w for w in nsol if any(x != 0 for x in w)]
        if not rows:
            continue
        L1 = [rows[0]]
        ok1 = is_tp(L1, A, B)
        print("  u%d: 真平行(r=1)=%s  Pi(L0)=%s" %
              (j, ok1, [[str(x) for x in r] for r in mm2(L1, B)]))
        if ok1:
            hits.append(("r=1", L1))
        if len(rows) >= 2:
            L2 = [rows[0], rows[1]]
            if is_tp(L2, A, B):
                hits.append(("r=2", L2))

    print()
    print("=== 结果：真平行实例 %d 个 ===" % len(hits))
    for tag, L0 in hits[:4]:
        print("  [%s] L0 = %s" % (tag, [[str(x) for x in r] for r in L0]))
        print("        Pi(L0) = %s" % [[str(x) for x in r] for r in mm2(L0, B)])
    return hits


if __name__ == "__main__":
    main()
