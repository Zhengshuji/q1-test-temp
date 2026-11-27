# -*- coding: utf-8 -*-
"""
batch_c6p.py —— 批量验证猜想 c6′：
   情形 II 平行 ∧ (A) ∧ T5a  ⟹  (S) 必失败（即 im H ∩ ker Λ ≠ {0}）

做法：
  · 取多个 A（A^2=0，保证 ker[C;CA] 是 A-不变的 ✓）、多个 C
  · 对每个实例：构造 L0 = [基础行（(A) 成立）] + [行 ∈ row[C;CA]]
    ⟹ 由 §12 的结构性事实，(A) 保持 ✓ 且 T5a 自动成立 ✓
  · 解出 Λ, G0, G1（已知 L ⟹ 线性 ✓）
  · 对 Λ 的**每个解**检验 (S)：用 T5 ⟺ im H ∩ ker(λI-Λ) = {0} ∀λ
    实现：M(λ) = (λI-Λ)·H 是多项式矩阵；rank H = ρ
          (S) 成立 ⟺ rank_{Q(λ)} M(λ) = ρ ⟺ ρ 阶子式的 gcd = 1
    当 ρ = 1 时简化为：M(λ) 的诸元素无公因子 ⟺ M 不是零矩阵（对某 λ 非零）
"""
import os, io, contextlib, itertools
from fractions import Fraction as F

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    s = fh.read()
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(s, "lib", "exec"), _ns)
ker = _ns["ker_basis"]

_ns2 = {}
with open(os.path.join(_HERE, "linalg_exact.py"), encoding="utf-8") as fh:
    exec(compile(fh.read(), "lx", "exec"), _ns2)
rk2, se, mm2 = _ns2["rank_exact"], _ns2["solve_exact"], _ns2["matmul"]


def mat(r):
    return [[F(x) for x in q] for q in r]


def hcat(X, Y):
    return [X[i] + Y[i] for i in range(len(X))]


def checkA(A, C, L):
    return rk2(mm2(L, A) + L + C + mm2(C, A)) == rk2(L + C + mm2(C, A))


def nullspace(N):
    r = se(N, [[F(0)] for _ in range(len(N))])
    return [] if r is None else r[1]


def solve_Lambda(A, C, L):
    """解 L·A = Λ·L + G0·C + G1·CA ⟹ 返回 [(Λ,G0,G1), ...] 或 []"""
    r, n, p = len(L), len(A), len(C)
    CA = mm2(C, A)
    LA = mm2(L, A)
    nunk = r * r + 2 * r * p
    rows = []
    for i in range(r):
        for j in range(n):
            row = [F(0)] * nunk
            for k in range(r):
                row[k * r + i] = L[k][j]           # Λ[i][k]
            for k in range(p):
                row[r * r + i * p + k] = C[k][j]   # G0[i][k]
            for k in range(p):
                row[r * r + r * p + i * p + k] = CA[k][j]
            rows.append(row)
    rhs = [[-LA[i][j]] for i in range(r) for j in range(n)]
    res = se(rows, rhs)
    if res is None:
        return []
    y, nsol = res
    sols = ([y] if any(x != 0 for x in y) else []) + nsol
    out = []
    for sol in sols:
        Lam = [[sol[k * r + i] for k in range(r)] for i in range(r)]
        G0 = [[sol[r * r + i * p + k] for k in range(p)] for i in range(r)]
        G1 = [[sol[r * r + r * p + i * p + k] for k in range(p)] for i in range(r)]
        out.append((Lam, G0, G1))
    return out


def S_holds(Lam, H):
    """
    检验 (S)：rank_{Q(λ)}((λI-Λ)H) == rank H ？
    实现：H 是 r×d；M(λ)[i][j] = Σ_k (λ δ_ik - Λ[i][k]) H[k][j]
          = λ·H[i][j] - (ΛH)[i][j]
    于是 M(λ) = λ H - ΛH = λ H - F。
    秩判据（精确）：(S) 成立 ⟺ ρ 阶子式的 gcd = 1，ρ = rank H。
    当 ρ = rank H 时，只需看 λH - ΛH 这一**矩阵多项式**的常秩；
    这里用简单而严格的做法：对 ρ = rank(H) 计算所有 ρ 阶子式（关于 λ 的一次多项式），
    求它们的 gcd；gcd 为常数 1 ⟺ (S) 成立。
    """
    r, d = len(H), len(H[0])
    rho = rk2(H)
    if rho == 0:
        return True
    Fm = mm2(Lam, H)
    # 子式：ρ×ρ，取行组合、列组合
    import itertools as it
    polys = []
    for ri in it.combinations(range(r), rho):
        for cj in it.combinations(range(d), rho):
            # 行列式 = det(λ H - F) 的对应子矩阵，是一次多项式 a λ + b
            a_mat = [[H[i][j] for j in cj] for i in ri]
            b_mat = [[Fm[i][j] for j in cj] for i in ri]
            a = det_of(a_mat)
            b = -det_of(b_mat)
            if a == 0 and b == 0:
                continue
            polys.append((a, b))          # a λ + b
    if not polys:
        return False
    # 求 gcd(a λ + b, a' λ + b', ...)
    g = None
    for (a, b) in polys:
        g = (a, b) if g is None else gcd_lin(g, (a, b))
        if g == (F(0), F(1)) or (g[0] == 0 and g[1] != 0):
            return True
    # g 非常数 ⟹ (S) 失败
    return False


def det_of(M):
    """精确行列式（小矩阵）"""
    n = len(M)
    if n == 0:
        return F(1)
    if n == 1:
        return M[0][0]
    A = [row[:] for row in M]
    det = F(1)
    for c in range(n):
        piv = None
        for i in range(c, n):
            if A[i][c] != 0:
                piv = i; break
        if piv is None:
            return F(0)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]; det = -det
        det *= A[c][c]
        inv = F(1) / A[c][c]
        for i in range(c + 1, n):
            f = A[i][c] * inv
            if f != 0:
                A[i] = [A[i][j] - f * A[c][j] for j in range(n)]
    return det


def gcd_lin(p, q):
    """两个一次多项式 (aλ+b) 的 gcd（归一化，首项为 1 或常数）"""
    def red(x):
        a, b = x
        if a == 0 and b == 0:
            return None
        return (a, b)
    p, q = red(p), red(q)
    while q is not None and not (q[0] == 0 and q[1] == 0):
        if q[0] == 0:                     # q 是非零常数 ⟹ gcd = 1
            return (F(0), F(1))
        # p mod q ： p - (a_p/a_q) λ^(deg p - deg q) · q
        if p[0] == 0:
            return (F(0), F(1))
        f = p[0] / q[0]
        p, q = q, (F(0), p[1] - f * q[1])
    return (F(0), F(1))


def main():
    print("=== 批量验证 c6′：(A)∧T5a ⟹ (S) 失败 ？ ===\n")
    trials = []
    # 多个 A（A^2=0）+ 多个 C
    A_list = [
        ("nilp6a", mat([[0,0,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1],
                        [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])),
        ("nilp6b", mat([[0,0,0,1,1,0],[0,0,0,0,1,1],[0,0,0,0,0,1],
                        [0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])),
        ("nilp4",  mat([[0,0,1,0],[0,0,0,1],[0,0,0,0],[0,0,0,0]])),
    ]
    C_list = [
        ("p2a", mat([[0,0,0,1,0,0],[0,0,0,0,1,0]])),
        ("p2b", mat([[0,0,0,1,1,0],[0,0,0,0,1,0]])),
        ("p1",  mat([[0,0,0,1,0,0]])),
    ]

    n_ok, n_S, n_tot = 0, 0, 0
    for aname, A in A_list:
        n = len(A)
        for cname, C in C_list:
            if len(C[0]) != n:
                continue
            CA = mm2(C, A)
            R = C + CA
            B = ker(R)
            if not B or not B[0]:
                continue
            d = len(B[0])
            r = 2
            # 基础行：e1（对 nilp 结构通常满足 (A)）
            base = [F(1) if i == 0 else F(0) for i in range(n)]
            # 第二行：取 R 的某个非零行（∈ row[C;CA] ✓）
            second = None
            for row in R:
                if any(x != 0 for x in row):
                    second = row[:]; break
            if second is None:
                continue
            L = [base, second]
            if not checkA(A, C, L):
                # 换 base 的尝试（用 e_i）
                found = False
                for i in range(n):
                    b2 = [F(1) if k == i else F(0) for k in range(n)]
                    if checkA(A, C, [b2, second]):
                        L = [b2, second]; found = True; break
                if not found:
                    print("[%s/%s] 未找到满足 (A) 的基础行，跳过" % (aname, cname))
                    continue
            H = mm2(L, B)
            t5a = rk2(H) < r
            tp = rk2(H + mm2(mm2(L, A), B)) == 1
            okA = checkA(A, C, L)
            n_tot += 1
            if not (okA and t5a):
                print("[%s/%s] (A)=%s T5a=%s —— 不满足前提，跳过" % (aname, cname, okA, t5a))
                continue
            n_ok += 1
            sols = solve_Lambda(A, C, L)
            any_S = False
            for Lam, G0, G1 in sols:
                if mm2(Lam, H) != mm2(mm2(L, A), B):
                    continue                    # 只取满足 F = ΛH 的解
                if S_holds(Lam, H):
                    any_S = True
                    break
            if any_S:
                n_S += 1
            print("[%s/%s] n=%d d_CA=%d  (A)=True T5a=True 真平行=%s | 解数=%d  **存在 (S) 成立的解？%s**" %
                  (aname, cname, n, d, tp, len(sols), any_S))

    print("\n=== 统计 ===")
    print("满足 (A)∧T5a 的实例数：%d" % n_ok)
    print("其中 **(S) 成立的**：%d" % n_S)
    if n_ok and n_S == 0:
        print("⟹ **c6′ 在这些实例上全部成立** ✓（(A)∧T5a ⟹ (S) 失败）")
    elif n_S:
        print("⟹ **发现反例！** c6′ 假 ⟹ 情形 II 平行可为 YES ✓✓")
    return n_ok, n_S


if __name__ == "__main__":
    main()
