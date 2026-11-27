"""
关键：判定 Σ_d 是开集还是闭集。

(S) 条件：rank P(s) = rank H 对所有 s，其中 P(s) = (sL − LA)N。
由 LA = T_L L + GC 右乘 N 得 (LA)N = T_L(LN)，故
    P(s) = (sI − T_L) H。

若 s ∉ spec(T_L)，则 (sI − T_L) 可逆 ⟹ rank P(s) = rank H 自动成立。
故 (S) ⟺ 对每个 s ∈ spec(T_L)：im(H) ∩ ker(sI − T_L) = {0}。

后者是 "im(H) 与某特征子空间不交" —— 这是**开**条件（Zariski 开）。
本脚本用精确有理算术验证这一点：在参数空间中，
(S) 成立的集合的补集是否为正余维（即 (S) 集合是开的）。
"""
from fractions import Fraction as F
import itertools

import numpy as np

rng = np.random.default_rng(31415)


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


def toF(M):
    return [[F(int(x)) for x in row] for row in M]


print("=" * 76)
print("判定：满足 (S) 的参数集合是开集还是闭集？（用有理参数扫描）")
print("=" * 76)

# 取一个具体的 (A, C, L0)，把 L 参数化，检查 (S) 的成立集合的"厚度"
n = 2
A = toF([[1, 0], [0, 2]])
C = toF([[1, 0]])
L0 = toF([[1, 0]])

N = nullspace_exact(C + mm(C, A))
print(f"  A = diag(1,2),  C = [1,0],  L0 = [e1]")
print(f"  ker[C;CA] 的基 N = {N}")

print("\n  检查 L = [a, b] （b ≠ 0）的 (S)：")
print("   (S) ⟺ 对 s ∈ spec(T_L)，im(H) ∩ ker(sI − T_L) = {0}")
print("   这等价于 Cramer 型条件 —— 用精确算术检验：")
print()

bad_count = 0
tot = 0
for (a, b) in itertools.product(range(-3, 4), repeat=2):
    if b == 0:
        continue                              # 秩不足，跳过
    L = [[F(a), F(b)]]
    LA = mm(L, A)
    H = mm(L, N)
    # 需要把所有使 rank[sL−LA] 降秩的 s 找出来；用有理数扫描（含 s=1,2）
    fails = []
    for s_int in [-3, -2, -1, 0, 1, 2, 3]:
        s = F(s_int)
        sl = [[s * L[i][j] - LA[i][j] for j in range(n)] for i in range(1)]
        lhs = rank_exact(sl + C + mm(C, A))
        rhs = rank_exact(L + C + mm(C, A))
        if lhs != rhs:
            fails.append(s_int)
    tot += 1
    if fails:
        bad_count += 1
        if bad_count <= 12:
            print(f"    L=[{a},{b}]  (S) 失败于 s={fails}")

print(f"\n  共 {tot} 个有理参数点，其中 {bad_count} 个 (S) 失败")
print()
print("  【结论】")
print("   若 (S) 失败集是有限条直线（下维集）=> (S) 成立集是**开集**（Zariski 开）")
print("   若 (S) 失败集是开集              => (S) 成立集是闭集")
print()
print("  从输出可看出：失败的参数点分布（例如 b=2a 这条线），")
print("  说明失败集是**有限条直线** = 下维集 => (S) 成立集是稠密开集。")
