r"""
c6_S_iff_5b.py -- ⭐⭐⭐ **定理：(5b) ⟺ (S)**

【推导】
  r0 := rank[L; C; CA] = rank H + (n−d)            （因 row L + K^⊥ = π^{-1}(row H)，dim K^⊥ = n−d）
  rank[λL − LA; CA; C] = rank((λI−Λ)H) + (n−d)      （因 π(λL−LA) = λH − ΛH = (λI−Λ)H）

  ⟹  (5b)  ⟺  rank[λL−LA;CA;C] ≡ r0  ∀λ
            ⟺  rank((λI−Λ)H) ≡ rank H  ∀λ
            ⟺  **(S)**  ✓

【意义】
  · **撤销** history/47 的"（S）只是必要条件"担忧 —— 两者**等价**
  · 项目此前 14/14 的 (S)-证据在**两个方向**上都有效 ✓
  · 判定问题只需处理 **(S)**（更容易表达）

【验证】对 (5a) 成立的实例：解 F = ΛH 得 Λ，然后比较
        (5b): 全矩阵铅笔子式 gcd 为常数
        (S) : (λI−Λ)H 的 ρ 阶子式 gcd 为常数
"""
import os
import io
import contextlib
import random
import itertools
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ns = {}
with open(os.path.join(_HERE, "exact_count_thm7.py"), encoding="utf-8") as fh:
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(fh.read(), "lib", "exec"), _ns)
rk = _ns["rk"]; mm = _ns["mm"]; ker_basis = _ns["ker_basis"]

# ---------- 多项式 ----------
def Pt(p):
    q = list(p)
    while len(q) > 1 and q[-1] == 0:
        q.pop()
    return q
def Pa(a, b):
    n = max(len(a), len(b))
    return Pt([(a[i] if i < len(a) else Fr(0)) + (b[i] if i < len(b) else Fr(0)) for i in range(n)])
def Ps(a, b):
    n = max(len(a), len(b))
    return Pt([(a[i] if i < len(a) else Fr(0)) - (b[i] if i < len(b) else Fr(0)) for i in range(n)])
def Pm(a, b):
    if Pt(a) == [Fr(0)] or Pt(b) == [Fr(0)]:
        return [Fr(0)]
    r = [Fr(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            r[i + j] += x * y
    return Pt(r)
def Pd(a, b):
    a = Pt(a); b = Pt(b); db = len(b) - 1
    q = [Fr(0)] * max(1, len(a) - db)
    while len(a) - 1 >= db and a != [Fr(0)]:
        d = len(a) - 1 - db; co = a[-1] / b[-1]; q[d] += co
        for i in range(len(b)):
            a[d + i] -= co * b[i]
        a = Pt(a)
    return Pt(q), a
def Pg(a, b):
    a, b = Pt(a), Pt(b)
    while b != [Fr(0)]:
        _, r = Pd(a, b); a, b = b, r
    if len(a) > 1:
        lc = a[-1]; a = [x / lc for x in a]
    return a
def Pdet(M, k):
    if k == 1:
        return [Fr(x) for x in M[0][0]]
    tot = [Fr(0)]
    for j in range(k):
        sub = [row[:j] + row[j + 1:] for row in M[1:]]
        d = Pdet(sub, k - 1); pr = Pm(M[0][j], d)
        tot = Pa(tot, pr) if j % 2 == 0 else Ps(tot, pr)
    return Pt(tot)
def gcd_all(polys):
    if not polys:
        return None
    g = polys[0]
    for q in polys[1:]:
        g = Pg(g, q)
        if len(g) == 1:
            break
    return g
def is_const_nonzero(g):
    return g is not None and len(Pt(g)) == 1 and any(x != 0 for x in g)


# ---------- 线性求解（带回代安全）----------
def solve_lin_full(Amat, bvec):
    """返回 (x0, basis)：特解 + 零空间基（便于取不同的解）"""
    m = len(Amat); n = len(Amat[0])
    M = [[Fr(Amat[i][j]) for j in range(n)] + [Fr(bvec[i])] for i in range(m)]
    piv = 0; where = [-1] * n
    for c in range(n):
        p = None
        for i in range(piv, m):
            if M[i][c] != 0:
                p = i; break
        if p is None:
            continue
        M[piv], M[p] = M[p], M[piv]
        pv = M[piv][c]; M[piv] = [x / pv for x in M[piv]]
        for i in range(m):
            if i != piv and M[i][c] != 0:
                f = M[i][c]
                M[i] = [M[i][j] - f * M[piv][j] for j in range(n + 1)]
        where[c] = piv; piv += 1
        if piv == m:
            break
    for i in range(piv, m):
        if all(M[i][j] == 0 for j in range(n)) and M[i][n] != 0:
            return None
    x0 = [Fr(0)] * n
    for c in range(n):
        if where[c] >= 0:
            x0[c] = M[where[c]][n]
    free = [c for c in range(n) if where[c] < 0]
    basis = []
    for fc in free:
        v = [Fr(0)] * n
        v[fc] = Fr(1)
        for c in range(n):
            if where[c] >= 0:
                v[c] = -M[where[c]][fc]
        basis.append(v)
    return x0, basis


def solve_lin(Amat, bvec):
    r = solve_lin_full(Amat, bvec)
    return None if r is None else r[0]


def check_5b_total(L, A, C, maxminors=1500):
    """(5b)：全矩阵铅笔 [λL−LA; CA; C] 的 r0 阶子式 gcd 是否为非零常数"""
    CA = mm(C, A); LA = mm(L, A)
    base = L + CA + C
    r0 = rk(base); m = len(base); n = len(base[0])
    nL = len(LA)                      # ⚠️ 用 len(LA)（与 LA 同源）
    assert nL <= m, "行数不匹配"
    if r0 == 0:
        return True
    P = [[([-LA[i][j], L[i][j]] if i < nL else [base[i][j]]) for j in range(n)]
         for i in range(m)]
    polys = []; cnt = 0
    for rows in itertools.combinations(range(m), r0):
        for cols in itertools.combinations(range(n), r0):
            d = Pdet([[P[i][j] for j in cols] for i in rows], r0)
            if d != [Fr(0)]:
                polys.append(d)
            cnt += 1
            if cnt > maxminors:
                break
        if cnt > maxminors:
            break
    return is_const_nonzero(gcd_all(polys))


def check_S(L, A, C, H, Lam, maxminors=1500):
    """(S)：rank((λI−Λ)H) ≡ rank H"""
    q = len(H); d = len(H[0])
    rho = rk(H)
    if rho == 0:
        return True
    # (λI − Λ)H 的条目：−ΛH + λH
    P = [[[-Lam[i][j] for j in range(1)] for j in range(1)] for i in range(1)]  # 占位
    PH = []
    LamH = mm(Lam, H)
    for i in range(q):
        row = []
        for j in range(d):
            row.append([-LamH[i][j], H[i][j]])
        PH.append(row)
    polys = []; cnt = 0
    for rows in itertools.combinations(range(q), rho):
        for cols in itertools.combinations(range(d), rho):
            dd = Pdet([[PH[i][j] for j in cols] for i in rows], rho)
            if dd != [Fr(0)]:
                polys.append(dd)
            cnt += 1
            if cnt > maxminors:
                break
        if cnt > maxminors:
            break
    return is_const_nonzero(gcd_all(polys))


def find_Lam(H, Fm):
    """解 F = Λ H（F: q×d, H: q×d）"""
    q = len(H); d = len(H[0])
    # 未知量 Λ[i][m]，共 q*q；方程 F[i][j] = Σ_m Λ[i][m] H[m][j]
    Amat = []
    bvec = []
    for i in range(q):
        for j in range(d):
            row = [Fr(0)] * (q * q)
            for m in range(q):
                row[i * q + m] = Fr(H[m][j])
            Amat.append(row); bvec.append(Fr(Fm[i][j]))
    sol = solve_lin(Amat, bvec)
    if sol is None:
        return None
    return [[sol[i * q + m] for m in range(q)] for i in range(q)]


def main():
    print("=== 验证 (5b) ⟺ (S) ===\n")
    rng = random.Random(271828)
    n_tot = 0
    agree = 0
    T = 0; Fa = 0
    bad = []
    for trial in range(6000):
        n = 5
        p = rng.choice([1, 2])
        q = rng.choice([1, 2])
        A = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(n)]
        C = [[Fr(rng.randint(-2, 2)) for _ in range(n)] for _ in range(p)]
        if rk(C) != p:
            continue
        W = C + mm(C, A)
        N = ker_basis(W)
        if not N or not N[0]:
            continue
        d = len(N[0])
        # 构造 (5a)-成立的 L：v 满足 vA ∈ row[C;CA]
        rows = []; rhs = []
        for j in range(n):
            row = [A[i][j] for i in range(n)]
            row += [-C[k][j] for k in range(p)] + [-W[k][j] for k in range(len(W))]
            rows.append(row); rhs.append(Fr(0))
        solset = solve_lin_full(rows, rhs)
        if solset is None:
            continue
        x0, basis = solset
        def rand_sol():
            """⚠️ 解向量的前 n 个分量才是协向量（后 3p 个是 a,b 辅助变量）"""
            v = list(x0)
            for b in basis:
                t = Fr(rng.randint(-2, 2))
                v = [v[i] + t * b[i] for i in range(len(v))]
            return [v[i] for i in range(n)]      # ← 截断！
        # 取 q 个（在 vA∈row[C;CA] 的解空间里）且 H≠0 的行
        Lcand = None
        for _attempt in range(40):
            trial_rows = []
            for _i in range(q):
                for _k in range(12):
                    v = rand_sol()
                    if rk(trial_rows + [v]) == len(trial_rows) + 1:
                        trial_rows.append(v); break
                else:
                    break
            if len(trial_rows) != q:
                continue
            Ht = mm(trial_rows, N)
            if rk(Ht) == 0:
                continue
            Lcand = trial_rows
            break
        if Lcand is None:
            continue
        L = Lcand
        H = mm(L, N)
        if rk(H) == 0:
            continue
        Fm = mm(mm(L, A), N)
        Lam = find_Lam(H, Fm)
        if Lam is None:
            continue
        b5 = check_5b_total(L, A, C)
        s5 = check_S(L, A, C, H, Lam)
        n_tot += 1
        if b5 == s5:
            agree += 1
            if b5:
                T += 1
            else:
                Fa += 1
        elif len(bad) < 6:
            bad.append((trial, b5, s5, n, p, q, d, rk(H)))
    print("(5a)-成立的实例：%d" % n_tot)
    print("  (5b) 与 (S) **一致**：%d" % agree)
    print("    两者皆 True ：%d" % T)
    print("    两者皆 False：%d" % Fa)
    print("  不一致：%d" % (n_tot - agree))
    for t in bad:
        print("    trial=%d 5b=%s S=%s (n=%d,p=%d,q=%d,d=%d,rkH=%d)" % t)

    # ---------- 补 True 侧：无穷族（n≥4）----------
    print("\n--- True 侧：history/51 的无穷族 ---")
    print("%4s %6s %6s %8s %8s" % ("n", "(5b)", "(S)", "一致?", "rkH"))
    famT = 0; famAgree = 0; famTot = 0
    for n in range(4, 11):
        C = [[Fr(0)] * n]; C[0][0] = Fr(1)
        A = [[Fr(0)] * n for _ in range(n)]
        A[0][1] = Fr(1); A[1][2] = Fr(1)
        CA = mm(C, A)
        L0 = CA[:]
        R = [[Fr(0)] * n]; R[0][2] = Fr(1)
        L = L0 + R
        W = C + mm(C, A)
        N = ker_basis(W)
        if not N or not N[0]:
            continue
        d = len(N[0])
        H = mm(L, N)
        if rk(H) == 0:
            continue
        Fm = mm(mm(L, A), N)
        Lam = find_Lam(H, Fm)
        if Lam is None:
            print("%4d %6s %6s %8s %8d  ← F=ΛH 无解（不应发生）" % (n, "-", "-", "✗", rk(H)))
            continue
        b5 = check_5b_total(L, A, C)
        s5 = check_S(L, A, C, H, Lam)
        famTot += 1
        if b5 == s5:
            famAgree += 1
        if b5:
            famT += 1
        print("%4d %6s %6s %8s %8d" % (n, "T" if b5 else "F", "T" if s5 else "F",
                                       "✓" if b5 == s5 else "**✗**", rk(H)))
    print("  族小结：%d 个；一致 %d；(5b) 为 True %d" % (famTot, famAgree, famT))
    print()
    total_agree = agree + famAgree
    total_n = n_tot + famTot
    T_all = T + famT
    Fa_all = Fa + (famTot - famT)
    print("=== 总计：%d 个，(5b) 与 (S) 一致 %d ；True %d ；False %d ===" %
          (total_n, total_agree, T_all, Fa_all))
    print()
    if total_agree == total_n and T_all > 0 and Fa_all > 0:
        print("⟹⟹⟹ **定理成立：(5b) ⟺ (S)**（两侧都有点 ✓✓）")
        print("     ⟹ **撤销** history/47 的\"（S）只是必要条件\"担忧")
        print("     ⟹ 项目的 14/14 (S)-证据在**两个方向**上有效 ✓")
        print("     ⟹ 判定问题只需处理 (S) ⭐")
    else:
        print("⚠️ 判定力或一致性不足")


if __name__ == "__main__":
    main()
