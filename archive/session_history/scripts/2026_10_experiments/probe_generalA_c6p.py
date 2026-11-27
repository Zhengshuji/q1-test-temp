# -*- coding: utf-8 -*-
"""
probe_generalA_c6p.py —— 检验 **一般 A 版 c6′** 的构造机制是否真的可执行

【背景】
  最新一轮 Lean（history/c6-lean-milestone.md §13、§16）给出两条"去掉 CA^2=0"的定理：
    exists_row_killing_AK :  Nd1 + A(Nd2) = 0 ⟹ f(d1) = 0
                            ⟹ ∃l,  l∘N = f  ∧  l∘A∘N = 0
    condA_of_add_row_C    :  L' = L + P0∘C ⟹ (A) 的核形式被保持（无需 CA^2=0）

  本脚本把这条链**逐环放进真实实例**，看它是否能真正造出
      (A) ∧ T5a ∧ H≠0 ∧ F = ΛH
  的增广行 l。这是"一般 A 的 c6′"是否落地的**判定性实验**。

【已证 / 已定的记号】（与 FINAL.md §1 一致）
  K = ker[C;CA]，B = K 的基（n×d_CA，列满秩）
  A' = A|_K（在基 B 下），A'* = A' 的对偶
  f ∈ K* 是"活跃泛函"；l ∈ V* 是 f 在 row 提升下的原像
  H = L·B,  F = L·A·B
  T5a  ⟺ rk(H) < q0 = len(L)
  (A)  ⟺ rk([LA;L;C;CA]) == rk([L;C;CA])          （原始 4 块判据 ✓）
  几何条件 ⟺  Nd1 + A(Nd2) = 0 ⟹ f(d1) = 0
           ⟺  im(A'*) ⊆ ker f  ∧  f⊥(K ∩ A(K))     （用 B_g 把 K 上的泛函搬到 R^n ✓）

【本脚本的判定项】
  ① f ≠ 0 且几何条件成立  （§13.2 的假设）
  ② 存在 l：l·B = f·B 且几何配对 l(A·B) = 0   （即 l∘N = f ∧ l∘A∘N = 0）
  ③ [L0; l] 是否满足 (A)                        ← **关键**
  ④ 若 (A) 成立：T5a、H≠0、F = ΛH 是否也成立
"""
import os, io, contextlib, itertools
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    s = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(s, "lib", "exec"), _ns)
ker_basis = _ns["ker_basis"]

_ns2 = {}
with open(os.path.join(_HERE, "linalg_exact.py"), encoding="utf-8") as fh:
    exec(compile(fh.read(), "lx", "exec"), _ns2)
rank_exact, solve_exact, matmul = _ns2["rank_exact"], _ns2["solve_exact"], _ns2["matmul"]

_ns3 = {"__file__": os.path.join(_HERE, "batch_c6p_k.py")}
with open(os.path.join(_HERE, "batch_c6p_k.py"), encoding="utf-8") as fh:
    _src = fh.read().split("def main()")[0]
exec(compile(_src, "helpers", "exec"), _ns3)
mat = _ns3["mat"]

def nullspace(N):
    """★ 独立实现的零空间基：返回 {x : N·x = 0} 的一组基（每个长度为 len(N[0])）。

    ⚠️ 本函数修掉了本脚本初版的一个**实质错误**：约束是 f·g = 0（f 为未知量、g 为生成元），
    故必须对 **G^T** 求零空间（G 的行=生成元），而不是对 G 本身求。
    """
    if not N or not N[0]:
        return []
    m, k = len(N), len(N[0])
    A = [[F(x) for x in row] for row in N]
    piv = []
    r = 0
    for c in range(k):
        sel = None
        for i in range(r, m):
            if A[i][c] != 0:
                sel = i
                break
        if sel is None:
            continue
        A[r], A[sel] = A[sel], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(m):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(k)]
        piv.append(c)
        r += 1
        if r == m:
            break
    free = [c for c in range(k) if c not in piv]
    out = []
    for fc in free:
        v = [F(0)] * k
        v[fc] = F(1)
        for i, pc in enumerate(piv):
            v[pc] = -A[i][fc]
        out.append(v)
    return out
det_of = _ns3["det_of"]
solve_Lambda = _ns3["solve_Lambda"]
S_holds = _ns3["S_holds"]

Z = F(0)


# ---------------------------------------------------------------- 基本工具

def rows(M):
    return [r[:] for r in M]


def stack(X, Y):
    """行堆叠；带维数断言（本项目第 13 处的教训）"""
    if not X:
        return rows(Y)
    if not Y:
        return rows(X)
    assert len(X[0]) == len(Y[0]), "stack: 列数不一致"
    return rows(X) + rows(Y)


def rk(M):
    return rank_exact(M)


def condA(A, C, L):
    """原始 4 块 (A) 判据：rk[LA;L;C;CA] == rk[L;C;CA]"""
    CA = matmul(C, A)
    LA = matmul(L, A)
    return rk(stack(LA, stack(L, stack(C, CA)))) == rk(stack(L, stack(C, CA)))


def _left_inverse(B):
    """解 B^T x_col = e_j（j 为行指标）：即求 d×n 矩阵 B_g 满足 B_g B = I"""
    n, d = len(B), len(B[0])
    Bt = [[B[i][j] for i in range(n)] for j in range(d)]        # d×n
    out = []
    for j in range(d):
        ej = [[F(1) if i == j else F(0)] for i in range(d)]
        r = solve_exact(Bt, ej)
        if r is None:
            return None
        out.append(r[0])
    return out


def induced_map(B, A, Bg):
    """A' = A|_K 在基 B 下的矩阵：A·B = B·A'  ⟹  A' = Bg·A·B"""
    AB = matmul(A, B)
    return matmul(Bg, AB)


def geom_ok2(A, B, Bg, Aind, frow):
    """几何条件的**完整**判定：im(Aind) ⊆ ker f  ∧  f⊥(K ∩ A(K))"""
    d = len(B[0])
    # (1) im Aind ⊆ ker f
    for j in range(d):
        col = [Aind[i][j] for i in range(d)]
        if sum(frow[i] * col[i] for i in range(d)) != 0:
            return False
    # (2) K ∩ A(K) ⊆ ker f ：求系数 (c1,c2) 使 B c1 + A B c2 = 0，检查 frow·c1 = 0
    AK = matmul(A, B)
    W = stack(B, AK)                        # n × 2d
    KW = ker_basis(W)                       # 2d × m
    if KW and KW[0]:
        for j in range(len(KW[0])):
            c1 = [KW[i][j] for i in range(d)]
            if sum(frow[i] * c1[i] for i in range(d)) != 0:
                return False
    return True


# ---------------------------------------------------------------- 主流程

def analyze(tag, A, C, L0, verbose=True):
    n, p, r = len(A), len(C), len(L0)
    CA = matmul(C, A)
    R = stack(C, CA)
    B = ker_basis(R)
    if not B or not B[0]:
        return None
    d = len(B[0])
    q0_theory = r + 1                        # k=1：先试加 1 行
    Bg = _left_inverse(B)
    if Bg is None:
        print("[%s] B 无左逆 ⟹ B 非列满秩？跳过" % tag)
        return None
    Aind = induced_map(B, A, Bg)             # A' = A|_K 在基 B 下
    # 几何条件的生成元：
    #   (1) im(Aind) 的列 ⟹ f·Aind[:,j] = 0
    #   (2) K ∩ A(K) ⟹ 同 geom_ok2
    gens = []
    for j in range(d):
        gens.append([Aind[i][j] for i in range(d)])
    AK = matmul(A, B)
    KW = ker_basis(stack(B, AK))
    if KW and KW[0]:
        for j in range(len(KW[0])):
            gens.append([KW[i][j] for i in range(d)])
    gens = [g for g in gens if any(x != 0 for x in g)]
    if not gens:
        print("[%s] n=%d p=%d r=%d d_CA=%d | **无约束** ⟹ 任意 f ≠ 0 都满足几何条件" %
              (tag, n, p, r, d))
        fs = [[F(1) if i == 0 else F(0) for i in range(d)]]
    else:
        # 约束：f·g = 0（g 为生成元）⟹ 未知量是 f 的 **d 个坐标**。
        # gens[i][j] = 第 j 个生成元的第 i 个坐标 ⟹ 约束矩阵取 gens **本身**（行=生成元，列=坐标）✓
        Gcon = [[gens[j][i] for i in range(d)] for j in range(len(gens))]   # m × d
        fs = nullspace(Gcon)
        if verbose:
            print("      [诊断] A' = %s" % [[str(x) for x in q] for q in Aind])
            print("      [诊断] 生成元 (%d 个) = %s" %
                  (len(gens), [[str(x) for x in g] for g in gens]))
            print("      [诊断] d=%d  约束矩阵秩=%d  ⟹ f 的解空间维数应为 %d" %
                  (d, rk(Gcon), d - rk(Gcon)))
            print("      [诊断] f 的解空间 = %s" %
                  [[str(x) for x in q] for q in fs])
        if not fs:
            print("[%s] n=%d p=%d r=%d d_CA=%d | **无解** ⟹ 不存在 f ⟹ 几何条件不可满足" %
                  (tag, n, p, r, d))
            return dict(tag=tag, n=n, p=p, r=r, d=d, n_f=0, built=0, condA=0, S_ok=0)
    n_f = n_built = n_A = n_S = 0
    detail = []
    for frow in fs:
        if not any(x != 0 for x in frow):
            continue
        if not geom_ok2(A, B, Bg, Aind, frow):
            continue
        n_f += 1
        # 解 l：l·B = f·B  且  l·(A·B) = 0
        # 未知量 l ∈ Q^n；方程：sum_i l_i B[i][j] = sum_i frow[i] B[i][j]  （d 条）
        #                     sum_i l_i (A B)[i][j] = 0                    （d 条）
        Des = []
        rhs = []
        for j in range(d):
            Des.append([B[i][j] for i in range(n)])
            rhs.append([sum(frow[i] * B[i][j] for i in range(d))])
        for j in range(d):
            Des.append([AK[i][j] for i in range(n)])
            rhs.append([Z])
        sol = solve_exact(Des, rhs)
        if sol is None:
            continue
        l = sol[0]
        if not any(x != 0 for x in l):
            detail.append((frow, None, "(l=0：几何条件逼死 f)"))
            continue
        n_built += 1
        L = [L0[0][:], l]
        okA = condA(A, C, L)
        H = matmul(L, B)
        Fm = matmul(matmul(L, A), B)
        rkH = rk(H)
        rkH0 = rk(matmul(L0, B))                 # L0 那部分对 rank H 的贡献
        rkHl = rk(matmul([l], B))                # 构造行 l 对 rank H 的贡献
        t5a = rkH < len(L)
        detail.append((frow, l, "A=%s rkH=%d/%d (L0行:%d, l行:%d) T5a=%s" %
                       (okA, rkH, len(L), rkH0, rkHl, t5a)))
        if okA:
            n_A += 1
            # F = ΛH ？
            sols = solve_Lambda(A, C, L)
            consistent = any(matmul(Lam, H) == Fm for Lam in sols)
            if t5a and consistent:
                for Lam in sols:
                    if matmul(Lam, H) == Fm and rk(Lam) > 0:
                        if S_holds(Lam, H):
                            n_S += 1
                            break
        if verbose:
            print("    f=%s  l=%s" % ([str(x) for x in frow], [str(x) for x in l]))
    print("[%s] n=%d p=%d r=%d d_CA=%d | 有效 f 数=%d  可解 l 数=%d  (A) 成立=%d  (S) 成立=%d" %
          (tag, n, p, r, d, n_f, n_built, n_A, n_S))
    if verbose:
        for frow, l, msg in detail:
            print("      · f=%s  %s" % ([str(x) for x in frow], msg))
    return dict(tag=tag, n=n, p=p, r=r, d=d, n_f=n_f, built=n_built, condA=n_A, S_ok=n_S)


def main():
    print("=== 检验「一般 A 版 c6′」的构造机制 ===")
    print("（同时检验 Lean `c6'_final` 的**全部假设**能否在真实实例上同时满足）\n")
    cases = []

    # 情形 1：A^2 = 0（本项目已验证族，d_CA=4 ≥ q0=2 ⟹ 情形 II）
    cases.append(("nilp6a/p2",
                  mat([[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]),
                  mat([[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0]]),
                  mat([[1, 0, 0, 0, 0, 0]])))
    cases.append(("nilp6b/p2",
                  mat([[0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 1, 1], [0, 0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]),
                  mat([[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0]]),
                  mat([[1, 0, 0, 0, 0, 0]])))

    # 情形 2：A^2 ≠ 0，但 CA^2 = 0（同样是"K 是 A-不变的"，A' 幂零）
    A3 = mat([[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]])
    cases.append(("A2ne0/CA2=0",
                  A3,
                  mat([[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0]]),
                  mat([[1, 0, 0, 0, 0, 0]])))

    # 情形 3：**一般 A** —— K 不是 A-不变的（CA^2 ≠ 0）
    A4 = mat([[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1],
              [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
    cases.append(("generalA(K 非不变)",
                  A4,
                  mat([[0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0]]),
                  mat([[1, 0, 0, 0, 0, 0]])))

    results = []
    for tag, A, C, L0 in cases:
        print("-" * 70)
        r = analyze(tag, A, C, L0, verbose=True)
        if r:
            results.append(r)
    print("\n=== 汇总 ===")
    print("%-22s %5s %6s %6s %6s %8s %8s" %
          ("实例", "d_CA", "有效f", "可解l", "(A)成立", "(S)成立", ""))
    for r in results:
        print("%-22s %5d %6d %6d %8d %8d" %
              (r["tag"], r["d"], r["n_f"], r["built"], r["condA"], r["S_ok"]))
    tot_A = sum(r["condA"] for r in results)
    tot_S = sum(r["S_ok"] for r in results)
    print("\n合计：(A) 成立 %d 个；(S) 成立 %d 个" % (tot_A, tot_S))
    print("""
【判读说明】
  · rkH  = rk(L·N)，其中 L = [L0 ; l]。rkH = q0 时 **T5a 失败**（无秩降）⟹ 该 l 无用。
  · c6′ 想要的是 rkH < q0 且 (S) 失败。(S) 成立 = 反例。
  · 本检验用的是**原始 4 块 (A) 判据**（rk[LA;L;C;CA]==rk[L;C;CA]），与 FINAL T1 一致 ✓。""")
    if tot_A == 0:
        print("⟹ **(A) 在一般 A 版构造下全部失败** ⟹ 该构造机制**不能**给出 c6′ ✗")
    elif tot_S == 0:
        print("⟹ (A) 可为真，但 (S) 全部失败 ⟹ 与 c6′ 一致 ✓")
    else:
        print("⟹ **发现反例**：(A) ∧ T5a ∧ (S) 同时成立 ⟹ c6′ 假 ⟹ 情形 II 平行可为 YES")


if __name__ == "__main__":
    main()
