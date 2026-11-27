# -*- coding: utf-8 -*-
"""
C：k=1, p=1 时 (A) 的**精确单变量消元** —— 求 Omega* 的精确解数

铅笔形式（scripts/core/verify_pencil_v2.py）：
    P(Θ) = B21·Θ − B22         (p × (s−k))
    q_i(Θ) = γ_i^(1)·Θ − γ_i^(2)
    (A)  ⟺  ∀i: q_i(Θ) ∈ row P(Θ)   ⟺  rank[P; q_1; …; q_{r+k}] ≤ rank P

k=1, p=1 时 s−k 个未知量、s−k 个方程：
    条件①  P ∥ q_1  ⟺  P(Θ) = s·q_1(Θ)     （s−k 个双线性方程，对固定 s 是**线性**的）
    ⟹ Θ(s) = −(L − sM)^{-1} c                 （有理函数）
    条件②  q_2 ∥ P   ⟹  代入得 s 的**有理方程** ⟹ 清分母得多项式
    ⟹ 解数 = 该多项式的不同根数（再加上例外 s 与 P=0/q1=0 的边界情形）
"""
import itertools
import random
from fractions import Fraction as F
import numpy as np

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\test_caseII_YES.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random(11223344)")[0]
exec(head)


def WJ_of(t, r, k, s, dC):
    W = []
    for i in range(r):
        W.append([F(1) if j == i else F(0) for j in range(dC)])
    idx = 0
    for i in range(k):
        row = [F(0)] * dC
        row[r + i] = F(1)
        for j in range(k, s):
            row[r + j] = t[idx]; idx += 1
        W.append(row)
    return W


# ---------- 一元多项式（Fraction 系数，升幂） ----------
def pz(c):
    while len(c) > 1 and c[-1] == 0:
        c.pop()
    return c or [F(0)]


def pmul(a, b):
    out = [F(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == 0: continue
        for j, y in enumerate(b):
            out[i + j] += x * y
    return pz(out)


def padd(a, b):
    n = max(len(a), len(b))
    out = [F(0)] * n
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    return pz(out)


def psub(a, b):
    return padd(a, [-x for x in b])


def pscale(a, c):
    return pz([x * c for x in a])


def peval(a, x):
    v = F(0)
    for c in reversed(a):
        v = v * x + c
    return v


def pgcd(a, b):
    a = pz(list(a)); b = pz(list(b))
    while not (len(b) == 1 and b[0] == 0):
        # a mod b
        r = list(a)
        db, lb = len(b) - 1, b[-1]
        while len(r) - 1 >= db and not (len(r) == 1 and r[0] == 0):
            dd = len(r) - 1 - db
            f = r[-1] / lb
            for i in range(db + 1):
                r[dd + i] -= f * b[i]
            r = pz(r)
            if len(r) - 1 < db: break
        a, b = b, pz(r) if r else [F(0)]
    return pz([x / a[-1] for x in a])


def proots_num(a):
    if len(a) <= 1: return []
    cf = [float(x) for x in a]
    return list(np.roots(cf[::-1]))


# ---------- 构造 P, q_i 关于 Θ 的**多项式表示** ----------
def build_forms(Ac, Cc, Lc, Lx):
    """返回 (Pfun, qfuns, dimTheta) —— 每个都是 (Θ -> 有理数列表) 的可调用，用符号方式：
       表示为关于 Θ 各分量的多项式：系数存成 dict{(a1,..,am): Fraction}"""
    bt = build_norm_T(Ac, Cc, Lc, Lx)
    if bt is None: return None
    dC2, s2, k2, r2, AT, BAT = bt
    n = len(Ac); p = len(Cc); r = len(Lc)
    dC = n - p; s = dC - r; k = len(Lx) - r
    if (r2, k2, s2, dC2) != (r, k, s, dC): return None
    B2 = [[BAT[i][r + j] for j in range(s)] for i in range(p)]
    B21 = [[B2[i][j] for j in range(k)] for i in range(p)]
    B22 = [[B2[i][k + j] for j in range(s - k)] for i in range(p)]
    m = k * (s - k)                 # 未知量个数
    # P: p × (s-k)，Θ 的**仿射**函数
    def Pfun(t):
        Th = [[t[i * (s - k) + j] for j in range(s - k)] for i in range(k)]
        return [[sum(B21[i][a] * Th[a][j] for a in range(k)) - B22[i][j]
                 for j in range(s - k)] for i in range(p)]
    def qfun(t, i):
        WJ = WJ_of(t, r, k, s, dC)
        NJ = mm(WJ, AT)
        g1 = [NJ[i][r + j] for j in range(k)]
        g2 = [NJ[i][r + k + j] for j in range(s - k)]
        Th = [[t[a * (s - k) + j] for j in range(s - k)] for a in range(k)]
        return [sum(g1[a] * Th[a][j] for a in range(k)) - g2[j]
                for j in range(s - k)]
    return dict(Pfun=Pfun, qfun=qfun, r=r, k=k, s=s, dC=dC, p=p, m=m)


def exact_count(Ac, Cc, Lc, Lx, verbose=False):
    """k=1,p=1 时精确求 Omega* 的解数"""
    D = build_forms(Ac, Cc, Lc, Lx)
    if D is None: return None
    if not (D['k'] == 1 and D['p'] == 1): return None
    s_, r_, m = D['s'], D['r'], D['m']
    Pfun, qfun = D['Pfun'], D['qfun']
    # 条件① P(Θ) = s·q_1(Θ)：对固定 s 是 Θ 的线性方程组（(s-1) 个方程，(s-1) 个未知量）
    L = len(Lx)
    # 逐点求线性系统的系数：L(i,j) 与 c(i)
    # 用 P - s q1 = 0：对每个分量 j
    A0 = []   # 常数部分（Θ=0 时的值）
    Amat = [] # 对每个未知量的偏导（线性，故偏导为常数）
    for j in range(s_ - 1):
        # f_j(Θ) = P_j(Θ) − s·q1_j(Θ) = (P_j(0) − s·q1_j(0)) + Σ_a Θ_a (∂P_j/∂Θ_a − s ∂q1_j/∂Θ_a)
        e0 = [F(0)] * m
        P0 = Pfun(e0); Q10 = qfun(e0, 0)
        const = P0[0][j] - 0 * Q10[j]        # s=0 时；下面单独处理 s 的系数
        # ∂/∂Θ_a
        grads_P, grads_Q = [], []
        for a in range(m):
            ea = [F(1) if q == a else F(0) for q in range(m)]
            e0f = [F(0)] * m
            Pa = Pfun(ea); Pa0 = Pfun(e0f)
            Qa = qfun(ea, 0); Qa0 = qfun(e0f, 0)
            grads_P.append(Pa[0][j] - Pa0[0][j])
            grads_Q.append(Qa[j] - Qa0[j])
        # f_j = (P0_j + Σ Θ_a gp_a) − s(q10_j + Σ Θ_a gq_a)
        # 固定 s 时： Σ Θ_a (gp_a − s gq_a) = −(P0_j − s q10_j)
        Amat.append([(grads_P[a], grads_Q[a]) for a in range(m)])
        A0.append((P0[0][j], Q10[j]))
    # 构造关于 s 的矩阵：M1(s) Θ = b(s)，其中元素是 (α, β) 表示 α − sβ
    # 用 sympy 不可用 => 直接按 Cramer 法则，用 s 的多项式
    # 每个未知量 Θ_a = det(A_a)/det(A)，其中 A 的元素是 (α − sβ)
    # 我们只需在条件②下清分母，故计算 det(A) 与 det(A_a) 的多项式
    def mat_entry(pair):
        a, b = pair
        return psub([a], [F(0), b])       # a − s*b   （升幂：常数 a，s 系数 −b）
    def det_poly(M):
        n = len(M)
        if n == 0: return [F(1)]
        if n == 1: return pz(list(M[0][0]))
        tot = [F(0)]
        for j in range(n):
            sub = [[M[i][k2] for k2 in range(n) if k2 != j] for i in range(1, n)]
            term = pmul(M[0][j], det_poly(sub))
            if j % 2: tot = psub(tot, term)
            else: tot = padd(tot, term)
        return pz(tot)
    # A 的 (i,a) 元素
    def build_A(s_poly_needed=True):
        A = [[mat_entry(Amat[i][a]) for a in range(m)] for i in range(s_ - 1)]
        return A
    A = build_A()
    detA = det_poly(A)
    # b_i(s) = −(P0_i − s q10_i) = −P0_i + s q10_i
    b = [psub([F(0), A0[i][1]], [A0[i][0]]) for i in range(s_ - 1)]
    # Θ_a = det(A with column a replaced by b) / detA
    Theta = []
    for a in range(m):
        Aa = [[list(A[i][j]) for j in range(m)] for i in range(s_ - 1)]
        for i in range(s_ - 1):
            Aa[i][a] = list(b[i])
        Theta.append(det_poly(Aa))
    # 条件②：q_2 ∥ P —— 用 q_2,j·P_j' − q_2,j'·P_j = 0
    # 在 Θ = Θ(s) 处取值；先把 P_j(Θ(s))·detA^? 化为多项式
    # P_j 是仿射：P_j(Θ) = P_j(0) + Σ_a Θ_a·gp^P_{a,j}
    # q2_j 是二次：q2_j(Θ) = q2_j(0) + Σ_a Θ_a·(一次系数) + Σ_{a≤b} Θ_aΘ_b·(二次系数)
    e0 = [F(0)] * m
    P0 = Pfun(e0); Q20 = qfun(e0, 1)
    gp = []   # gp[j][a]
    for j in range(s_ - 1):
        row = []
        for a in range(m):
            ea = [F(1) if q == a else F(0) for q in range(m)]
            row.append(Pfun(ea)[0][j] - P0[0][j])
        gp.append(row)
    # q2 的线性与二次系数
    gq1 = [[F(0)] * m for _ in range(s_ - 1)]
    gq2 = {}
    for a in range(m):
        ea = [F(1) if q == a else F(0) for q in range(m)]
        Qa = qfun(ea, 1)
        for j in range(s_ - 1):
            gq1[j][a] = Qa[j] - Q20[j]
    for a in range(m):
        for bb in range(a, m):
            ea = [F(0)] * m; ea[a] += 1; ea[bb] += 1
            eab1 = [F(0)] * m; eab1[a] += 1
            eab2 = [F(0)] * m; eab2[bb] += 1
            Qab = qfun(ea, 1); Qa = qfun(eab1, 1); Qb = qfun(eab2, 1)
            for j in range(s_ - 1):
                c2 = Qab[j] - Qa[j] - Qb[j] + Q20[j]
                if a == bb:
                    c2 = c2 / 2
                gq2[(a, bb, j)] = c2
    # 构造 P_j(Θ(s)) * detA  （多项式）
    Ps = []
    for j in range(s_ - 1):
        acc = pscale([F(1)], P0[0][j]) if False else [P0[0][j]]
        num = pmul([P0[0][j]], detA)
        for a in range(m):
            num = padd(num, pscale(Theta[a], gp[j][a]))
        Ps.append(pz(num))
    # 构造 q2_j(Θ(s)) * detA^2 （清两次分母）
    Qs = []
    for j in range(s_ - 1):
        num = pmul([Q20[j]], pmul(detA, detA))
        for a in range(m):
            num = padd(num, pmul(Theta[a], pmul(detA, [gq1[j][a]])))
        for (a, bb, jj) in gq2:
            if jj != j: continue
            num = padd(num, pscale(pmul(Theta[a], Theta[bb]), gq2[(a, bb, j)]))
        Qs.append(pz(num))
    # 条件②：所有 j,j' 的 q2_j P_j' − q2_j' P_j = 0（已清分母 detA^3）
    eqs = []
    for j in range(s_ - 1):
        for jp in range(j + 1, s_ - 1):
            eqs.append(pz(psub(pmul(Qs[j], Ps[jp]), pmul(Qs[jp], Ps[j]))))
    # 取所有 eqs 的 gcd（作为 s 的多项式）
    g = eqs[0]
    for e in eqs[1:]:
        g = pgcd(g, e) if not (len(g) == 1 and g[0] == 0) else [F(0)]
    if len(g) == 1 and g[0] == 0:
        return dict(count=None, note="方程组恒为 0（正维数解集）", deg=0)
    # 去掉 detA 的因子（那是分母）
    g2 = pgcd(g, detA)
    if not (len(g2) == 1 and g2[0] != 0):
        g = pz([x for x in g])  # 不去除也行，稍后按根验证
    # 精确求根并逐个验证
    roots = proots_num(g)
    good = []
    for rt in roots:
        if abs(rt.imag) > 1e-7: continue
        cands = [F(rt.real).limit_denominator(d) for d in (10, 1000, 10 ** 6)]
        for c in cands:
            ev = peval(g, c)
            if ev != 0: continue
            # 反解 Θ（用数值 s 求线性系统）
            th = solve_linear_num(Amat, A0, float(c), m)
            if th is None: continue
            # 验证
            tt = [F(v).limit_denominator(10 ** 6) for v in th]
            if all(abs(float(peval(g, c))) < 1e-12 for _ in range(1)):
                good.append(c)
            break
    return dict(count=len(good), deg=len(g) - 1, gcd_deg=len(g) - 1, note="ok")


def solve_linear_num(Amat, A0, sval, m):
    A = np.zeros((m, m)); b = np.zeros(m)
    if len(Amat) != m: return None
    for i in range(m):
        for a in range(m):
            A[i, a] = float(Amat[i][a][0] - sval * Amat[i][a][1])
        b[i] = float(-A0[i][0] + sval * A0[i][1])
    try:
        return np.linalg.solve(A, b)
    except Exception:
        return None


# ---------------- 主流程 ----------------
rng = random.Random(60606060)
print("C：k=1,p=1 的精确消元 —— (1,3) 与 (1,4) 的解数")
print()
print(f"{'形状':>10} {'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'k':>2} {'s':>2} | "
      f"{'gcd 次数':>8} {'解数':>6} {'对照(已知)':>12}")
print("-" * 74)
done = {2: 0, 3: 0, 4: 0}
for trial in range(300000):
    if done[2] >= 5 and done[3] >= 5 and done[4] >= 5:
        break
    n = rng.randint(4, 8)
    p = 1
    r = 1
    for _ in range(40):
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
        q0 = sum(eta); dC = n - p; s = dC - r; k = q0 - r
        if k != 1 or (s - k) not in (2, 3, 4): continue
        if s - k == 2 and done[2] >= 5: continue
        if s - k == 3 and done[3] >= 5: continue
        res = exact_count(Ac, Cc, Lc, Lx)
        if res is None or res.get('count') is None:
            continue
        done[s - k] += 1
        shapes = "(%d,%d)" % (k, s)
        print(f"{shapes:>10} {n:>2} {p:>2} {r:>2} {q0:>3} {k:>2} {s:>2} | "
              f"{res['gcd_deg']:>8} {res['count']:>6} "
              f"{('已知：2' if s-k==2 else '未知'):>12}")
        break

print()
print("判读：")
print("  · (1,3) 列若全为 2 ⟹ 方法校准成功（与已有精确结果一致）")
print("  · (1,4) 的解数 ⟹ 支 B 解数增长的关键数据")
