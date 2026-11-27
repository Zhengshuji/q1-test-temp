# -*- coding: utf-8 -*-
"""
gen_parallel.py —— **构造**"真平行"实例（不做随机搜！）

背景（CLAUDE.md §0.3）：
  真平行 = rank[ Pi(L0) ; Pi(L0 A) ] == 1   （**全部 r 行**都要成比例）
  其中 Pi(X) = X * N_CA，N_CA 的列张成 ker[C;CA]。
  真平行是**余维 r*d_CA - 1 的薄集** ⟹ 随机采样必错过 ⟹ **必须构造**。

构造配方（把"求 L0"化成齐次线性方程组）：
  固定 A, C，算出 B = N_CA。
  取定方向 u（d_CA 维非零向量），要求
     (I)  l B      = alpha * u        （l 是 L0 的一行）
     (II) l A B    = beta  * u
  未知量 (l, alpha, beta) ⟹ **齐次线性系统** ⟹ 求非零解即可。
  对每一行独立求解，拼成 L0 ⟹ 自动得到"全部 r 行成比例"的真平行实例 ✓

用法：
  python gen_parallel.py            # 默认配置
"""
import os
import sys
import itertools
import io
import contextlib

_HERE = os.path.dirname(os.path.abspath(__file__))
_LIB = os.path.join(_HERE, "exact_count_thm7.py")

_ns = {}
with open(_LIB, "r", encoding="utf-8") as fh:
    _src = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(_src, _LIB, "exec"), _ns)

F = _ns["F"]
rk = _ns["rk"]
mm = _ns["mm"]
tr = _ns["tr"]
ker_basis = _ns["ker_basis"]
solve = _ns["solve"]
cand = _ns["cand"]
condA = _ns["condA"]


# ----------------------------------------------------------------------
# 齐次线性系统求解：返回一个非零解（或 None）
# ----------------------------------------------------------------------
def nullvec(rows, k):
    """rows: 系数矩阵（m 行 k 列）的列表；返回一个非零解向量（长度 k）或 None。"""
    if not rows:
        return None
    Des = [r[:] for r in rows]
    b = [[F(0)] for _ in rows]
    res = solve(Des, b)
    if res is None:
        return None
    y, ns = res
    if ns:
        return ns[0]
    if any(x != 0 for x in y):
        return y
    return None


# ----------------------------------------------------------------------
# 构造：给定 A, C, u，求满足 (I)(II) 的一行 l
# ----------------------------------------------------------------------
def build_row(A, C, B, u, n):
    """
    未知量 (l_0..l_{n-1}, alpha, beta)，共 n+2 个。
      (I)  l B - alpha u = 0     （d_CA 个方程）
      (II) l A B - beta u = 0    （d_CA 个方程）
    """
    d = len(B[0])
    AB = mm(A, B)
    k = n + 2
    rows = []
    # (I)
    for t in range(d):
        row = [B[j][t] for j in range(n)] + [F(0), F(0)]
        row[n] = -u[t]          # alpha 的系数
        rows.append(row)
    # (II)
    for t in range(d):
        row = [AB[j][t] for j in range(n)] + [F(0), F(0)]
        row[n + 1] = -u[t]      # beta 的系数
        rows.append(row)
    v = nullvec(rows, k)
    if v is None:
        return None
    return v[:n]


# ----------------------------------------------------------------------
# 主流程
# ----------------------------------------------------------------------
def is_truly_parallel(L0, A, B):
    """rank[ Pi(L0) ; Pi(L0 A) ] == 1 且 Pi(L0) != 0"""
    P0 = mm(L0, B)
    PA = mm(mm(L0, A), B)
    if not any(x != 0 for r in P0 for x in r):
        return False
    return rk(P0 + PA) == 1


def main():
    n, p = 6, 1
    print("=== 真平行实例的**构造**（gen_parallel.py）===")
    print("n=%d p=%d" % (n, p))

    # 取一组 A, C：用有理数，避免退化
    A = [[F(x) for x in row] for row in [
        [0, 1, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1],
        [-2, -3, -1, 0, 1, 0],
    ]]
    C = [[F(1), F(0), F(0), F(0), F(0), F(0)]]

    CA = mm(C, A)
    B = ker_basis(C + CA)          # n x d_CA
    d = len(B[0]) if B else 0
    print("d_CA = %d" % d)
    if d == 0:
        print("ker[C;CA] = 0 ⟹ 本实例退化，换参数")
        return

    found = []
    # 遍历若干方向 u（穷举小的有理方向）
    cands_u = []
    for c in itertools.product([0, 1, -1], repeat=d):
        if any(c):
            cands_u.append([F(x) for x in c])
    for u in cands_u:
        l = build_row(A, C, B, u, n)
        if l is None:
            continue
        if all(x == 0 for x in l):
            continue
        L0 = [l]
        if is_truly_parallel(L0, A, B):
            found.append((u, l))
            print("  命中 u=%s  l=%s" % ([int(x) for x in u], [int(x) for x in l]))
            if len(found) >= 5:
                break

    print()
    print("=== 结果 ===")
    print("构造到的真平行单行实例数：%d" % len(found))
    if not found:
        print("⚠️ 未构造到（说明该 (A,C) 下条件过强，需换 A 的结构）")
    return found


if __name__ == "__main__":
    main()
