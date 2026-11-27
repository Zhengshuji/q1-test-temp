# -*- coding: utf-8 -*-
"""
验证一般既约形式：
   (A)  <=>  row(DΘ+E) ⊆ row(BΘ+C)
其中（在规范化 T 坐标系、商掉 E 之后）
   P(Θ) = B Θ + C   : p × (s-k),   B = B2[:, :k],  C = B2[:, k:]
   Q(Θ) = D Θ + E   : (r+k) × (s-k)，行 = N 的各行在商空间中的像
并统计：每个条件的次数 <= p+1，以及 rank(DΘ+E) <= p 是必要条件。
"""
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\exact_count_thm7.py",
           encoding="utf-8").read()
exec(src.split("rng = random.Random(112233)")[0])


def to_float(M):
    return [[float(x) for x in row] for row in M]


def mm_f(X, Y):
    return mm(X, Y)


def quotient_pencils(AT, BAT, r, k, s, dC):
    """
    在商 R^{dC}/E (E = span(e_1..e_r)) 中构造 (B,C,D,E)。
    坐标为：第 (r) .. (r+s-1) 个坐标。
    """
    # B2 = BAT 的后 s 列
    B2 = [[BAT[i][r + j] for j in range(s)] for i in range(len(BAT))]      # p × s
    Bmat = [[B2[i][j] for j in range(k)] for i in range(len(B2))]          # p × k
    Cmat = [[B2[i][k + j] for j in range(s - k)] for i in range(len(B2))]  # p × (s-k)

    N = [AT[i][:] for i in range(len(AT))]
    N = mm([AT[i] for i in range(r + k)], [[F(1) if a == b else F(0) for b in range(dC)]
                                           for a in range(dC)])          # 占位
    # N 的行：row i of Abar_T 乘以 W_J 的行
    WJ = []
    for i in range(r):
        WJ.append([F(1) if j == i else F(0) for j in range(dC)])
    for i in range(k):
        row = [F(0)] * dC
        row[r + i] = F(1)                                             # pivot
        WJ.append(row)
    # 注意：Θ 项由调用者填充；这里只取结构
    return Bmat, Cmat, WJ


rng = random.Random(24680)
print("验证既约形式 (A) <=> row(DΘ+E) ⊆ row(BΘ+C)")
print()
print(f"{'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'k':>2} {'s':>2} | {'p<s-k?':>6} | "
      f"{'等价一致':>10} {'rank(Q)<=p 必要?':>16}")
print("-" * 74)
for trial in range(40):
    n = rng.randint(4, 6)
    p = rng.randint(1, n - 2)
    r = rng.randint(1, n - p - 1)
    got = None
    for _ in range(120):
        Am = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
        Cm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)]
        Lm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(r)]
        Ac, Cc, Lc = toF(Am), toF(Cm), toF(Lm)
        if rk(Cc) != p or rk(Lc) != r: continue
        if rk(Lc + Cc) != r + p: continue
        Z = orb(Lc, Ac, n) + orb(Cc, Ac, n); OC = orb(Cc, Ac, n)
        if rk(Z + OC) != rk(OC): continue
        Lx, eta = p1(Ac, Cc, Lc)
        if not condA(Ac, Cc, Lx): continue
        q0 = sum(eta)
        dC = n - p; s = dC - r; k = q0 - r
        if k < 1 or k > s or k * (s - k) > 2: continue
        bt = build_norm_T(Ac, Cc, Lc, Lx)
        if bt is None: continue
        got = (Ac, Cc, Lc, q0, n, p, r, k, s, dC, bt)
        break
    if got is None: continue
    Ac, Cc, Lc, q0, n, p, r, k, s, dC, bt = got
    dC2, s2, k2, r2, AT, BAT = bt
    if (r2, k2, s2, dC2) != (r, k, s, dC): continue

    # B, C
    Bmat = [[BAT[i][r + j] for j in range(k)] for i in range(len(BAT))]
    Cmat = [[BAT[i][r + k + j] for j in range(s - k)] for i in range(len(BAT))]

    # N 的行 (Θ 依赖)：row r+i of W_J Abar_T，其中 W_J 的第 r+i 行 = e_{r+i} + Θ 项
    # 商像：取坐标 r..r+s-1
    def Q_E_of(t):
        """构造 Q(Θ) = D Θ + E 在给定 Θ (k×(s-k) 展平) 处的值"""
        # W_J 的行 (r+k) × dC
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
        NJ = mm(WJ, AT)                       # (r+k) × dC
        # 商像：坐标 r..r+s-1
        return [[NJ[i][r + j] for j in range(s)] for i in range(r + k)]

    def A_holds(t):
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
        MB = WJ + BAT
        MX = WJ + BAT + mm(WJ, AT)
        return rk(MB) == rk(MX)

    def reduced_holds(t):
        """row(Q) ⊆ row(P)，P = [B|C] 作用方式：P(Θ) = B·Θ + C"""
        idx = 0
        Th = [[F(0)] * (s - k) for _ in range(k)]
        for i in range(k):
            for j in range(s - k):
                Th[i][j] = t[idx]; idx += 1
        P = [[sum(Bmat[i][a] * Th[a][j] for a in range(k)) + Cmat[i][j]
              for j in range(s - k)] for i in range(p)]
        Q = Q_E_of(t)
        # row(Q) ⊆ row(P)  <=>  rank[P;Q] == rank(P)
        return rk(P + Q) == rk(P), rk(Q) <= rk(P)

    # 采样若干 Θ 检验等价
    agree = tot = 0
    nec_ok = True
    for _ in range(25):
        t = [F(rng.randint(-97, 97), rng.randint(1, 89)) * (1 if rng.random() < 0.5 else -1)
             for _ in range(k * (s - k))] if k * (s - k) > 0 else []
        a1 = A_holds(t)
        a2, nec = reduced_holds(t)
        tot += 1
        if a1 == a2:
            agree += 1
        if a1 and not nec:
            nec_ok = False
    print(f"{n:>2} {p:>2} {r:>2} {q0:>3} {k:>2} {s:>2} | {str(p < s-k):>6} | "
          f"{agree:>4}/{tot:<5} {str(nec_ok):>16}")
