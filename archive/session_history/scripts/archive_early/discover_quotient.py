"""
关键结构发现：(S) 与商空间 R/(R ∩ row(C)) 的关系。

对于单行 L = [a,b]，A = diag(1,2), C = [1,0]：
  row(C) = span(e_1) 是一维的，因此 R/R∩row(C) 是一维的
  => T_R 是一个标量（代表 A 在 R 上模 row(C) 的作用）
  => P(s) = (s − T_R)H，秩失败当且仅当 s = T_R

这解释了我此前把 (S) 误判为"闭集"：
  当 k=1（单行）时，T_R 唯一确定，(S) 的失败集可能是整个参数空间，
  而不是"下维集"——这不是 (S) 是闭集，而是 T_R 被 (A) 唯一锁定。

本脚本核实：
  (1) 一般情形 T_R 不唯一（相差一个行在 row(C) 中的矩阵）
  (2) 但 (T_R − T_R')H = 0，故 P(s) 与 T_R 的选择无关
  (3) 因此 (S) 的判定只依赖 R
"""
import numpy as np
from fractions import Fraction as F


def rref(M):
    M = [row[:] for row in M]
    if not M:
        return M, []
    nrow, ncol = len(M), len(M[0])
    piv, r = [], 0
    for c in range(ncol):
        p = None
        for i in range(r, nrow):
            if M[i][c] != 0:
                p = i; break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(nrow):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        piv.append(c); r += 1
        if r == nrow:
            break
    return M, piv


def rank_exact(M):
    if not M or not M[0]:
        return 0
    return len(rref(M)[1])


def mm(X, Y):
    if not X or not Y:
        return []
    n, k, m = len(X), len(Y), len(Y[0])
    return [[sum(X[i][t] * Y[t][j] for t in range(k)) for j in range(m)] for i in range(n)]


def nullspace_exact(M):
    if not M:
        return []
    n = len(M[0])
    R, piv = rref(M)
    free = [c for c in range(n) if c not in piv]
    out = []
    for fc in free:
        v = [F(0)] * n
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -R[i][fc]
        out.append(v)
    return out


print("=" * 74)
print("验证：若 C = I（满行秩），则 im(N) = 0  =>  H = 0  =>  (S) 自动成立")
print("=" * 74)
A = [[F(1), F(0)], [F(0), F(2)]]
C = [[F(1), F(0)], [F(0), F(1)]]
CA = mm(C, A)
print(f"  C = I_2, CA = diag(1,2)")
N = nullspace_exact(C + CA)
print(f"  ker[C;CA] 的维数 = {len(N)}   <- 应为 0")
print(f"  => H = L·N = 0，P(s) = 0，(S) 对任意 L 自动成立。")
print()

print("=" * 74)
print("验证：C 行秩不足时，T_R 的不唯一性")
print("=" * 74)
A = [[F(1), F(0)], [F(0), F(2)]]
C = [[F(1), F(0)]]
CA = mm(C, A)
N = nullspace_exact(C + CA)
print(f"  C = [1,0], ker[C;CA] 的基 N = {[[str(x) for x in v] for v in N]}")

L = [[F(1), F(1)]]
LA = mm(L, A)
print(f"  L = [1,1], LA = {[[str(x) for x in r] for r in LA]}")

# 求所有 T (1x1 标量) 与 G (1x2) 使 LA = T L + G C
# C = [1,0] => GC = G[0] * [1,0] = [g0, 0]
# 需要 [1,2] = T[1,1] + [g0, 0]  => 第二分量: 2 = T => T = 2; 第一分量: 1 = 2 + g0 => g0 = -1
print()
print("  解 LA = T·L + G·C：")
print("    第二分量: 2 = T*1  =>  T = 2（唯一！）")
print("    第一分量: 1 = 2*1 + g0  =>  g0 = -1")
print("  => 此例中 T_R 被唯一确定（因为 k=1，只有一个标量自由度）")
print()
print("  于是 P(s) = (sI - T_R)H = (s - 2)H")
print("  (S) 失败 ⟺ s = 2 时 H ≠ 0")
print()
H = mm(L, N)
print(f"  H = L·N = {[[str(x) for x in r] for r in H]}  rank = {rank_exact(H)}")
print("  => 若 H ≠ 0，则 (S) 在 s = 2 处必然失败！")
print()
print("  【这正是我此前'全部 42 个参数点都失败'的原因】")
print("   A 的特征值 2 唯一锁定 T_R，而 H ≠ 0 使 (S) 必然失败。")
print("   这不是 (S) 是闭集，而是这个特定的 (A,C,L0) 组合下 **无解**。")
print()
print("=" * 74)
print("结论：需要功能可观性前提来保证解的存在")
print("=" * 74)
print("""
  上例中 Z = R^2 但 row(O_C) = span(e_1)，
  故 row(O_L0) ⊄ row(O_C) —— **违反功能可观性前提**。
  这说明：P1/P2 的解存在性依赖于功能可观性，
  而 q.txt 的命题若不带此前提出，可能本身无解（nu_min 不存在）。
""")
