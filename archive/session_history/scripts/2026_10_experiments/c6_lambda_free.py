r"""
c6_lambda_free.py -- ⭐⭐⭐ **无 Λ 形式**：(S) ⟺ rank(L·P_λ) = rank(L·N)

【推导】
  (λI − Λ)H = λH − ΛH = λH − F                      （用 (A) ⟹ F = ΛH）
  ⟹ (S) ⟺ rank(λH − F) = rank H  ∀λ
  ⟹ 且 H = L·N,  F = L·A·N  ⟹  λH − F = L·(λN − AN) =: L·P_λ
  ⟹ **(S) ⟺ rank(L·P_λ) = rank(L·N)  ∀λ**
  ⟹ 结合 (5b) ⟺ (S)：**(5b) ⟺ rank(L·P_λ) ≡ rank(L·N)**

【意义】**Λ 完全消失**！判定问题变成纯粹对 L 的条件：
   (5a) ⟺ ker(L·N) ⊆ ker(L·A·N)
   (5b) ⟺ rank(L·P_λ) ≡ rank(L·N)
   两者都只涉及 (q×n) 的 L 与已知的 N, P_λ
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

# --- 多项式 ---
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
        sub = row_ = [row[:j] + row[j + 1:] for row in M[1:]]
        d = Pdet(row_, k - 1); pr = Pm(M[0][j], d)
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
def const_nz(g):
    return g is not None and len(Pt(g)) == 1 and any(x != 0 for x in g)


def check_5b_total(L, A, C, maxminors=1200):
    CA = mm(C, A); LA = mm(L, A)
    base = L + CA + C
    r0 = rk(base); m = len(base); n = len(base[0]); nL = len(LA)
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
    return const_nz(gcd_all(polys))


def check_lambda_free(L, A, N, sh=lambda x: x, maxminors=1200):
    """rank(L·P_λ) ≡ rank(L·N)，P_λ = λN − AN"""
    n = len(A); d = len(N[0])
    AN = mm(A, N)
    LN = mm(L, N)
    rho = rk(LN)
    if rho == 0:
        return True
    # L·P_λ = L·(λN − AN) = λ(LN) − L(AN)
    LAN = mm(L, AN)
    q = len(L)
    P = [[[-LAN[i][j], LN[i][j]] for j in range(d)] for i in range(q)]
    polys = []; cnt = 0
    for rows in itertools.combinations(range(q), rho):
        for cols in itertools.combinations(range(d), rho):
            dd = Pdet([[P[i][j] for j in cols] for i in rows], rho)
            if dd != [Fr(0)]:
                polys.append(dd)
            cnt += 1
            if cnt > maxminors:
                break
        if cnt > maxminors:
            break
    return const_nz(gcd_all(polys))


def solve_lin_full(Amat, bvec):
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


def main():
    print("=== 验证 (5b) ⟺ rank(L·P_λ) ≡ rank(L·N)  [无 Λ] ===\n")
    rng = random.Random(161803)
    n_tot = 0; agree = 0; T = 0; Fa = 0; bad = []
    for trial in range(5000):
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
        # 造 (5a)-成立的 L
        rows = []; rhs = []
        for j in range(n):
            row = [A[i][j] for i in range(n)]
            row += [-C[k][j] for k in range(p)] + [-W[k][j] for k in range(len(W))]
            rows.append(row); rhs.append(Fr(0))
        ss = solve_lin_full(rows, rhs)
        if ss is None:
            continue
        x0, basis = ss
        def rs():
            v = list(x0)
            for b in basis:
                t = Fr(rng.randint(-2, 2))
                v = [v[i] + t * b[i] for i in range(len(v))]
            return v[:n]
        Lc = None
        for _a in range(30):
            tr = []
            for _i in range(q):
                for _k in range(10):
                    v = rs()
                    if rk(tr + [v]) == len(tr) + 1:
                        tr.append(v); break
                else:
                    break
            if len(tr) != q:
                continue
            if rk(mm(tr, N)) == 0:
                continue
            Lc = tr; break
        if Lc is None:
            continue
        L = Lc
        b5 = check_5b_total(L, A, C)
        lf = check_lambda_free(L, A, N)
        n_tot += 1
        if b5 == lf:
            agree += 1
            if b5: T += 1
            else: Fa += 1
        elif len(bad) < 5:
            bad.append((trial, b5, lf))
    print("(5a)-成立的随机实例：%d" % n_tot)
    print("  (5b) ⟺ 无Λ形式 **一致**：%d" % agree)
    print("    两者皆 True ：%d ; 皆 False：%d" % (T, Fa))
    print("  不一致：%d" % (n_tot - agree))
    for b in bad:
        print("    trial=%d 5b=%s lambda_free=%s" % b)

    # True 侧：族
    print("\n--- True 侧：无穷族 ---")
    print("%4s %6s %12s %8s" % ("n", "(5b)", "无Λ形式", "一致?"))
    famT = 0; famAg = 0; famN = 0
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
        if rk(mm(L, N)) == 0:
            continue
        b5 = check_5b_total(L, A, C)
        lf = check_lambda_free(L, A, N)
        famN += 1
        if b5 == lf: famAg += 1
        if b5: famT += 1
        print("%4d %6s %12s %8s" % (n, "T" if b5 else "F", "T" if lf else "F",
                                    "✓" if b5 == lf else "**✗**"))
    tot = n_tot + famN; agr = agree + famAg; Ta = T + famT; Fa2 = Fa + (famN - famT)
    print("\n=== 总计 %d ；一致 %d ；True %d ；False %d ===" % (tot, agr, Ta, Fa2))
    print()
    if agr == tot and Ta > 0 and Fa2 > 0:
        print("⟹⟹⟹ **成立：(5b) ⟺ rank(L·P_λ) ≡ rank(L·N)（无 Λ）**（两侧都有点 ✓✓）")
        print("     ⟹ 判定问题变成纯粹对 (q×n) 的 L 的条件 —— **Λ 完全消失** ⭐")
        print("     ⟹ (5a) ⟺ ker(L·N) ⊆ ker(L·A·N)")
        print("     ⟹ (5b) ⟺ rank(L·P_λ) ≡ rank(L·N)")
    else:
        print("⚠️ 判定力不足或有误")


if __name__ == "__main__":
    main()
