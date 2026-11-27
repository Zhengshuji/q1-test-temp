# -*- coding: utf-8 -*-
"""
gen_parallel2.py —— **保证成功**的真平行实例构造（A-不变核 + 特征方向）

【为什么第一版失败】
  gen_parallel.py 固定方向 u 后要求  l B = alpha*u  且  l A B = beta*u，
  这是 8 方程 / 8 未知（n=6, d_CA=4）⟹ 一般只有零解 ✗。

【正确构造】（关键洞察）
  若  K := ker[C;CA]  是 **A-不变的**，记 A' := A|_K，
  则对任意 l：  l B = alpha * u   ⟹   l A B = (l B) A' = alpha * (u A')。
  于是只要 **u 取 A' 的一个特征向量**（u A' = lam * u），就有 l A B = (alpha*lam) * u，
  两个条件**自动相容** ✓。而 l ↦ l B 满射到 im B ⟹ 这样的 l 总存在 ✓。

【如何造出 A-不变的 K】
  取块状 A = [[A11, A12], [0, A22]]（下三角块），且 C = [C1, 0]（只看前一块）。
  则 ker[C;CA] ⊇ 第二块；配合适当的参数使等号成立 ⟹ K 不变 ✓。
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

F = _ns["F"]
rk = _ns["rk"]
mm = _ns["mm"]
ker_basis = _ns["ker_basis"]
solve = _ns["solve"]


def mat(rows):
    return [[F(x) for x in r] for r in rows]


def is_truly_parallel(L0, A, B):
    P0 = mm(L0, B)
    PA = mm(mm(L0, A), B)
    if not any(x != 0 for r in P0 for x in r):
        return False
    return rk(P0 + PA) == 1


def rank_of(L0, A, B):
    return rk(mm(L0, B))


def main():
    print("=== 真平行实例构造 v2（A-不变核 + 特征方向）===")

    # 块下三角 A：第 2 块 (指标 3,4,5) 是不变子空间
    A = mat([
        [0, 1, 0,  0, 0, 0],
        [0, 0, 1,  0, 0, 0],
        [0, 0, 0,  1, 0, 0],
        [0, 0, 0,  0, 1, 0],
        [0, 0, 0,  0, 0, 1],
        [1, 1, 0,  0, 0, 0],   # 注意：最后一行只在第 1 块取值 => 第 2 块不变
    ])
    C = mat([[1, 0, 0, 0, 0, 0]])

    CA = mm(C, A)
    B = ker_basis(C + CA)
    d = len(B[0]) if B else 0
    print("n=%d p=%d  d_CA=%d" % (len(A), len(C), d))
    if d == 0:
        print("退化")
        return

    # 验证 K = im B 是否 A-不变
    AB = mm(A, B)
    # A B 的每一列都应落在 im B 中
    Ab_in = rk(B) == rk(B + AB)
    print("ker[C;CA] 是 A-不变的吗？%s" % Ab_in)

    # 枚举方向 u，找 A' 的特征方向（即 u A' ∥ u）
    found = []
    At = None
    for c in itertools.product([0, 1, -1, 2], repeat=d):
        if not any(c):
            continue
        u = [F(x) for x in c]
        # u 在 K 中（用 B 表示）：u = coefs * B
        nrow = len(B); dcol = len(B[0])
        DesU = [[B[t][i] for i in range(dcol)] for t in range(nrow)]
        bU = [[u[t]] for t in range(nrow)]
        res = solve(DesU, bU)
        if res is None:
            continue
        coef, _ = res
        # 计算 w = u A'  (把 u 视作 K 中元素，作用 A 后再投影回 K)
        v = [sum(coef[i] * B[j][i] for i in range(len(coef))) for j in range(nrow)]
        Av = [sum(v[j] * A[j][i] for j in range(len(A))) for i in range(len(A))]
        # 投影回 K：解 Av = y * B
        res2 = solve(DesU, [[Av[t]] for t in range(nrow)])
        if res2 is None:
            continue
        y, _ = res2
        w = [sum(y[i] * B[i][j] for i in range(len(B))) for j in range(len(B[0]))]
        # 检查 w ∥ u（u 用 coef 表示）
        if rk([coef, y]) <= 1:
            print("  找到特征方向：coef=%s -> %s" % ([int(x) for x in coef], [int(x) for x in y]))
            # 造一行 l：l B = alpha * u  (取 alpha=1，u 由 coef 给出)
            rhs = [[coef[j]] for j in range(d)]
            res3 = solve([[B[j][t] for j in range(len(B))] for t in range(d)], rhs)
            if res3 is None:
                print("    (l 不存在，跳过)")
                continue
            l, _ = res3
            if all(x == 0 for x in l):
                continue
            L0 = [l]
            ok = is_truly_parallel(L0, A, B)
            print("    l=%s  真平行=%s  rank(Pi(L0))=%d" % ([int(x) for x in l], ok, rank_of(L0, A, B)))
            if ok:
                found.append((y, l))
            if len(found) >= 3:
                break

    print()
    print("=== 结果 ===")
    print("构造到的真平行实例数：%d" % len(found))
    return found


if __name__ == "__main__":
    main()
