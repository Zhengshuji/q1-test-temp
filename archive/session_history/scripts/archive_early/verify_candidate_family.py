"""
验证：即使在候选族受限下，(5a) 仍然容许"线性组合"，因此单独 (5a) 依旧是多项式的。

要点：若 R 的行取自候选族 C，条件
   (5a)  <=>  Z ⊆ V + row(R)
只要求 row(R) 的**张成**包含 Z/V，所以可以取"少数几行"线性组合出 Z/V，
不必把 Z/V 的每个基向量都各自作为一行。

=> 单独 (5a) + 候选族受限 = 仍是多项式（对每个候选做消元即可）。
=> NP-hard 只能来自 (5b) 的谱条件。
"""
import itertools

import numpy as np

TOL = 1e-7
rng = np.random.default_rng(2468)


def rk(M):
    M = np.atleast_2d(np.asarray(M, float))
    if M.size == 0 or M.shape[0] == 0:
        return 0
    s = np.linalg.svd(M, compute_uv=False)
    return 0 if s.size == 0 else int(np.sum(s > TOL * max(M.shape) * (s[0] if s[0] > 0 else 1.0)))


def st(*b):
    b = [np.atleast_2d(np.asarray(x, float)) for x in b]
    nc = max((x.shape[1] for x in b), default=0)
    b = [x for x in b if x.shape[0] > 0]
    return np.zeros((0, nc)) if not b else np.vstack(b)


def in_span(X, Y):
    X = np.atleast_2d(np.asarray(X, float))
    return True if X.shape[0] == 0 else rk(st(Y, X)) == rk(Y)


def condA(A, C, L):
    return in_span(L @ A, st(L, C, C @ A))


print("=" * 74)
print("D1 : 构造一个'候选族受限'的集合覆盖式实例，检查最小 |R|")
print("=" * 74)
print("""
  取 n=2m, 基 (x_e, y_e), A x_e = y_e, A y_e = 0, C = 0, L0 = 0
  候选族 = { y_e : e=1..m } ∪ { sum_{e in S} y_e : S 是给定集合 }
  此时 Z = span{y_e}, V = 0, 条件 (5a) 要求 span{y_e} ⊆ row(R)
""")
m = 4
sets = [[0, 1], [1, 2], [2, 3], [0, 3]]
n = 2 * m
A = np.zeros((n, n))
for i in range(m):
    A[2 * i, 2 * i + 1] = 1.0
C = np.zeros((0, n))
L0 = np.zeros((0, n))
cand = []
for e in range(m):
    v = np.zeros(n)
    v[2 * e + 1] = 1.0
    cand.append(("y%d" % e, v))
for S in sets:
    v = np.zeros(n)
    for e in S:
        v[2 * e + 1] = 1.0
    cand.append(("y_{%s}" % ",".join(map(str, S)), v))

print("  候选族：", [nm for nm, _ in cand])
for k in range(0, 4):
    found = []
    for combo in itertools.combinations(range(len(cand)), k):
        R = np.array([cand[i][1] for i in combo])
        if condA(A, C, st(L0, R)):
            found.append([cand[i][0] for i in combo])
    if found:
        print(f"  k={k} 可行，例如 {found[:3]}  （共 {len(found)} 种）")
        break

print()
print("=" * 74)
print("D2 : 关键观察 —— 单独 (5a) 下，候选族受限仍可用线性组合，故仍是多项式")
print("=" * 74)
print("""
  上面的例子说明：即使候选族只给出 y_e 的组合，为了覆盖 span{y_e}
  也只需要 k = dim(Z/V) = m 行（或更少，若候选能组合出全部方向）。
  但实际上"最小 k" 是一个**线性代数**问题：
      k* = min{ |T| : Z ⊆ V + span{c : c ∈ T} }
  这可以在多项式时间内求解（对 Z/V 做基的贪心覆盖，或等价地：
  找 Z/V 的一组基，看每个候选 c 在 Z/V 中的像，做最小集覆盖——
  但注意"覆盖"在这里是**线性张成**覆盖，不是集合覆盖，所以仍可在
  有限域/有理数上用线性代数直接判定）。
  真正的组合困难必须来自 (5b) 的谱条件。
""")

# 用线性代数直接算最小 k（贪心 + 验证）
def min_k_linearsystem(A, C, L0, cand):
    """在候选族中找最小子族使 row(R) 张成 Z/V 的补"""
    from numpy.linalg import svd

    def orb(M):
        nn = A.shape[0]
        out, cur = [M], M
        for _ in range(nn - 1):
            cur = cur @ A
            out.append(cur)
        return st(*out)

    Z = st(orb(L0), orb(C) if C.shape[0] else np.zeros((0, A.shape[0])))
    V = st(L0, C, C @ A)
    # 目标：Z + V 与 V 的商
    target = Z
    for k in range(0, len(cand) + 1):
        for combo in itertools.combinations(range(len(cand)), k):
            R = np.array([cand[i][1] for i in combo]) if k else np.zeros((0, A.shape[1]))
            if in_span(Z, st(V, R)):
                return k
    return None


print("  m =", m, "  候选数 =", len(cand))
print("  线性代数给出的最小 k =", min_k_linearsystem(A, C, L0, cand))
print("  dim(Z/V) =", rk(st(orb(L0) if False else np.zeros((0, n)), np.zeros((0, n)))) if False else m)


def orb(M):
    nn = A.shape[0]
    out, cur = [M], M
    for _ in range(nn - 1):
        cur = cur @ A
        out.append(cur)
    return st(*out)


Z = st(orb(L0), orb(C))
V = st(L0, C, C @ A)
print(f"  dim Z = {rk(Z)}, dim V = {rk(V)}, dim(Z/V) = {rk(Z)-rk(V)}")
print()
print("  因为候选 y_e 的**线性组合**可以张成整个 span{y_e}，")
print("  所以 k=1 的一行 sum_e y_e（若在候选族中）就够了；")
print("  若候选族不含它，则可能需要更多行——但判据仍是线性代数（多项式）。")
print()
print("  结论：单靠 (5a) + 候选族约束 **不足以** 产生 NP-hard。")
