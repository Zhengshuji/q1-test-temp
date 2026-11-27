# -*- coding: utf-8 -*-
"""
可靠版 (S) 判据 + 分支 A 的分情形实验。

(S) 判据（可靠）：
   P(λ) = λH − F  (q0 × d_CA)
   ρ = rank H = P(λ) 的一般秩
   (S) <=> rank P(λ) = ρ 对所有 λ
       <=> P 的全部 ρ 阶子式（作为 λ 的多项式）的 gcd 是非零常数
   （若 ρ = 0：则要求 P ≡ 0）

严格有理算术 + 多项式 gcd。绝不使用此前那个不可靠的 condS。
"""
import math
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\exact_count_thm7.py",
           encoding="utf-8").read()
exec(src.split("rng = random.Random(112233)")[0])


# ---------- 多项式工具（系数列表，index = 次） ----------
def p_zero(p):
    return all(c == 0 for c in p) or len(p) == 0


def p_trim(p):
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p if p else [F(0)]


def p_add(a, b):
    n = max(len(a), len(b))
    return p_trim([(a[i] if i < len(a) else F(0)) + (b[i] if i < len(b) else F(0))
                   for i in range(n)])


def p_sub(a, b):
    n = max(len(a), len(b))
    return p_trim([(a[i] if i < len(a) else F(0)) - (b[i] if i < len(b) else F(0))
                   for i in range(n)])


def p_mul(a, b):
    if p_zero(a) or p_zero(b):
        return [F(0)]
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j, y in enumerate(b):
            out[i + j] += x * y
    return p_trim(out)


def p_divmod(a, b):
    a = a[:]; b = p_trim(b[:])
    if p_zero(b):
        raise ZeroDivisionError
    if len(a) < len(b):
        return [F(0)], a
    q = [F(0)] * (len(a) - len(b) + 1)
    lead = b[-1]
    while len(a) >= len(b) and not p_zero(a):
        d = len(a) - len(b)
        c = a[-1] / lead
        q[d] = c
        for i in range(len(b)):
            a[d + i] -= c * b[i]
        a = p_trim(a)
        if len(a) < len(b):
            break
    return p_trim(q), p_trim(a)


def p_gcd(a, b):
    a = p_trim(a[:]); b = p_trim(b[:])
    while not p_zero(b):
        _, r = p_divmod(a, b)
        a, b = b, r
    return p_trim(a)


# ---------- 矩阵（元素为多项式） ----------
def det_poly(M):
    n = len(M)
    if n == 0:
        return [F(1)]
    if n == 1:
        return M[0][0]
    total = [F(0)]
    for j in range(n):
        if p_zero(M[0][j]):
            continue
        sub = [[M[i][k] for k in range(n) if k != j] for i in range(1, n)]
        term = p_mul(M[0][j], det_poly(sub))
        if j % 2 == 0:
            total = p_add(total, term)
        else:
            total = p_sub(total, term)
    return p_trim(total)


def rank_const(H):
    return rk(H)


def S_holds(H, Fm, verbose=False):
    """可靠判据：rank(λH − F) 是否恒等于 rank H"""
    if not H or not H[0]:
        return True                     # d_CA = 0 => (S) 自动成立
    q = len(H); d = len(H[0])
    rho = rank_const(H)
    if rho == 0:
        # 要求 λH − F ≡ 0
        return all(Fm[i][j] == 0 for i in range(q) for j in range(d))
    from itertools import combinations
    # 先确认一般秩 = rho
    P1 = [[H[i][j] for j in range(d)] for i in range(q)]
    if rk(P1) != rho:
        return False
    g = None
    for rs in combinations(range(q), rho):
        for cs in combinations(range(d), rho):
            # 子式 = det(λ H_sub − F_sub)
            M = []
            for i in rs:
                row = []
                for j in cs:
                    # λ*H[i][j] − F[i][j]
                    row.append([-Fm[i][j], H[i][j]])
                M.append(row)
            dm = det_poly(M)
            if p_zero(dm):
                continue
            g = dm if g is None else p_gcd(g, dm)
            if len(g) == 1:
                return True             # 已是非零常数
    if g is None:
        return False
    return len(p_trim(g)) == 1


# ---------- 主实验 ----------
rng = random.Random(20240608)


def test_instance(Ac, Cc, Lc, q0, Lx, label):
    n = len(Ac); p = len(Cc); r = len(Lc)
    dC = n - p; s = dC - r; k = q0 - r
    bt = build_norm_T(Ac, Cc, Lc, Lx)
    if bt is None:
        return None
    dC2, s2, k2, r2, AT, BAT = bt
    if (r2, k2, s2, dC2) != (r, k, s, dC):
        return None
    # N_CA
    CA = mm(Cc, Ac)
    NCA = ker_basis(CA + Cc)                     # n × d_CA（列基）
    dCA = len(NCA[0]) if (NCA and NCA[0]) else 0
    # T^{-1} M_C：由 build_norm_T 内部构造；这里重算
    NC = ker_basis(Cc)
    MC = mm(inv(mm(tr(NC), NC)), tr(NC))
    # 重建 T
    L0NC = mm(Lc, NC)
    R = Lx[len(Lc):]; RNC = mm(R, NC)
    K = ker_basis(L0NC); mK = len(K[0]) if (K and K[0]) else 0
    if mK == 0:
        return None
    Kr = [[K[a][j] for a in range(dC)] for j in range(mK)]
    Tcols = []
    for i in range(r):
        ei = [F(1) if q == i else F(0) for q in range(r)]
        so = solve([[L0NC[a][j] for j in range(dC)] for a in range(r)],
                   [[ei[a]] for a in range(r)])
        if so is None:
            return None
        xi = so[0]
        tgt = mm(RNC, [[xi[j]] for j in range(dC)])[0][0]
        rkl = [mm(RNC, [[Kr[j][a]] for a in range(dC)])[0][0] for j in range(mK)]
        c = [F(0)] * mK
        for j in range(mK):
            if rkl[j] != 0:
                c[j] = -tgt / rkl[j]; break
        z = [sum(c[j] * Kr[j][a] for j in range(mK)) for a in range(dC)]
        Tcols.append([xi[a] + z[a] for a in range(dC)])
    rkmat = [[mm(RNC, [[Kr[j][a] for a in range(dC)]])[ii][0] for j in range(mK)]
             for ii in range(k)]
    nsc = None
    for j in range(s):
        if j < k:
            ej = [[F(1) if ii == j else F(0)] for ii in range(k)]
            so = solve(rkmat, ej)
            if so is None:
                return None
            yj = so[0]
        else:
            if nsc is None:
                nsc = solve(rkmat, [[F(0)] for _ in range(k)])[1]
            ix = j - k
            if ix >= len(nsc):
                return None
            yj = nsc[ix]
        Tcols.append([sum(yj[a] * Kr[a][jj] for a in range(mK)) for jj in range(dC)])
    T = [[Tcols[j][i] for j in range(dC)] for i in range(dC)]
    Ti = inv(T)
    if Ti is None:
        return None
    # 采样 Θ，保留满足 (A) 的，再测 (S)
    cnt_A = 0; cnt_S = 0; tot = 0
    pert_keep = 0; pert_tot = 0          # 扰动检验：找 (A)∧(S) 点后扰动
    found_good = None
    rankH_full = 0                        # (A) 点中 rank H = d_CA 的个数
    rankH_vals = set()
    a2_ag = 0; a2_tot = 0; a2_raw_true = 0; a2_red_true = 0   # A2 地基检查
    a2_examples = []
    thetas = []
    if k * (s - k) == 0:
        thetas = [[]]
    else:
        for _ in range(40):
            thetas.append([F(rng.randint(-97, 97), rng.randint(1, 89)) *
                           (1 if rng.random() < 0.5 else -1) for _ in range(k * (s - k))])
    for t in thetas:
        WJ = []
        for i in range(r):
            WJ.append([F(1) if j == i else F(0) for j in range(dC)])
        idx = 0
        for i in range(k):
            row = [F(0)] * dC
            row[r + i] = F(1)
            for j in range(k, s):
                row[r + j] = t[idx]; idx += 1
            WJ.append(row)
        tot += 1
        # ---- A2 地基检查：原始 4 块 (A)  vs  三块约化 ----
        CA_ = mm(Cc, Ac)
        Lco = mm(mm(WJ, Ti), MC)
        Lc2 = Lc + Lco[r:]                 # 真正的 [L0; R] 形式
        ra = (rk(mm(Lc2, Ac) + Lc2 + CA_ + Cc) == rk(Lc2 + CA_ + Cc))
        rr = (rk(WJ + BAT + mm(WJ, AT)) == rk(WJ + BAT))
        a2_tot += 1
        if ra == rr: a2_ag += 1
        a2_raw_true += (1 if ra else 0)
        a2_red_true += (1 if rr else 0)
        if ra != rr and len(a2_examples) < 2:
            a2_examples.append(t)
        if rk(WJ + BAT + mm(WJ, AT)) != rk(WJ + BAT):
            continue
        cnt_A += 1
        # ℒ N_C = W_J T^{-1}  =>  ℒ N_CA = W_J T^{-1} M_C N_CA
        Lred = mm(mm(WJ, Ti), MC)                  # q0 × n
        if dCA == 0:
            cnt_S += 1
            if found_good is None:
                found_good = t
            continue
        Hm = mm(Lred, NCA)
        Fm = mm(mm(Lred, Ac), NCA)
        rH = rk(Hm) if (Hm and Hm[0]) else 0
        rankH_vals.add(rH)
        if rH == dCA:
            rankH_full += 1
        if S_holds(Hm, Fm):
            cnt_S += 1
            if found_good is None:
                found_good = t
    # ---- 扰动检验：(A)∧(S) 是否在扰动下保持（=> (S) 开） ----
    if found_good is not None:
        for _p in range(12):
            t2 = found_good[:]
            for a in range(len(t2)):
                t2[a] += F(rng.randint(-3, 3), rng.randint(100, 1000)) * \
                    (1 if rng.random() < 0.5 else -1)
            WJ = []
            for i in range(r):
                WJ.append([F(1) if j == i else F(0) for j in range(dC)])
            idx = 0
            for i in range(k):
                row = [F(0)] * dC
                row[r + i] = F(1)
                for j in range(k, s):
                    row[r + j] = t2[idx]; idx += 1
                WJ.append(row)
            pert_tot += 1
            if rk(WJ + BAT + mm(WJ, AT)) != rk(WJ + BAT):
                continue
            Lred2 = mm(mm(WJ, Ti), MC)
            if dCA == 0 or S_holds(mm(Lred2, NCA), mm(mm(Lred2, Ac), NCA)):
                pert_keep += 1
    return dict(label=label, n=n, p=p, r=r, q0=q0, dCA=dCA,
                tot=tot, cnt_A=cnt_A, cnt_S=cnt_S,
                pert_keep=pert_keep, pert_tot=pert_tot,
                rankH_full=rankH_full, rankH_vals=sorted(rankH_vals),
                a2_ag=a2_ag, a2_tot=a2_tot,
                a2_raw_true=a2_raw_true, a2_red_true=a2_red_true,
                a2_examples=a2_examples)


print("分支 A 分情形实验（可靠 (S) 判据：ρ 阶子式的多项式 gcd）+ 扰动开性检验")
print()
print(f"{'n':>2} {'p':>2} {'r':>2} {'q0':>3} | {'d_CA':>4} {'d_CA>=q0':>8} | "
      f"{'(A)命中':>8} {'(A)∧(S)':>8} | {'扰动保持':>8}")
print("-" * 76)
rows = []
for trial in range(4000):
    if len(rows) >= 14:
        break
    n = rng.randint(3, 6)
    p = rng.randint(1, n - 1)
    r = rng.randint(1, n - p)
    for _ in range(120):
        Am = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
        Cm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)]
        Lm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(r)]
        Ac, Cc, Lc = toF(Am), toF(Cm), toF(Lm)
        if rk(Cc) != p or rk(Lc) != r: continue
        if rk(Lc + Cc) != r + p: continue
        Z = orb(Lc, Ac, n) + orb(Cc, Ac, n); OC = orb(Cc, Ac, n)
        if rk(Z + OC) != rk(OC): continue
        try:
            Lx, eta = p1(Ac, Cc, Lc)
        except Exception:
            continue
        if not condA(Ac, Cc, Lx): continue
        q0 = sum(eta)
        dC = n - p; s = dC - r; k = q0 - r
        if k < 1 or k > s: continue          # 需要 k>=1（k=0 时族是单点，另行处理）
        if 2 * p + q0 < n: continue          # 只要分支 A
        res = test_instance(Ac, Cc, Lc, q0, Lx, "")
        if res is None:
            continue
        rows.append(res)
        print(f"{n:>2} {p:>2} {r:>2} {q0:>3} | {res['dCA']:>4} "
              f"{str(res['dCA']>=q0):>8} | {res['cnt_A']:>3}/{res['tot']:<4} "
              f"{res['cnt_S']:>3}/{res['tot']:<4} | "
              f"{res['pert_keep']:>3}/{res['pert_tot']:<4} | "
              f"rankH={res['rankH_vals']} full={res['rankH_full']}/{res['cnt_A']} | "
              f"A2: {res['a2_ag']}/{res['a2_tot']} rawT={res['a2_raw_true']} "
              f"redT={res['a2_red_true']}")
        break

print()
ge = [x for x in rows if x['dCA'] >= x['q0']]
lt = [x for x in rows if x['dCA'] < x['q0']]
print(f"=== 汇总 ===")
print(f"  d_CA >= q0 的实例 {len(ge)} 个：(A)∧(S) 命中总数 "
      f"{sum(x['cnt_S'] for x in ge)} / {sum(x['tot'] for x in ge)}")
print(f"  d_CA <  q0 的实例 {len(lt)} 个：(A)∧(S) 命中总数 "
      f"{sum(x['cnt_S'] for x in lt)} / {sum(x['tot'] for x in lt)}")
