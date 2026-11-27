# -*- coding: utf-8 -*-
"""
(C2) 的 k>=2 检验 —— 有理参数化版（不用数值优化）

形状：n=5,p=1,r=1,q0=3 ⟹ k=2, s=3, dimΘ=2, d_CA=5−rank[C;CA] ≥ 3 = q0（情形 II）

由**定理 D1**（已证），det H 关于 Θ 的次数 ≤ k = 2 ⟹ {rank H < q0} = {det H = 0} 是**二次曲线**。

做法：
  1. 精确插值求出 f = det H(θ1,θ2) 的二次型系数
  2. 扫小分母有理 θ1，解 θ2 的二次方程；判别式为有理平方 ⟹ 得**有理点**，精确验证 f=0
  3. 在每个有理点上精确检验 rank H < q0、(A)、(S)
"""
import itertools
import random
from fractions import Fraction as F
import numpy as np

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\test_C2_k2_locked.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random(31313131)")[0]
exec(head)


def q2_coeffs(D):
    """精确求 f(θ1,θ2)=det H 的 6 个系数（次数 ≤ 2）"""
    pts = [(F(0), F(0)), (F(1), F(0)), (F(0), F(1)),
           (F(1), F(1)), (F(2), F(0)), (F(0), F(2))]
    vals = []
    for (x, y) in pts:
        Lred, Hm = exact_H([x, y], D)
        if not Hm or not Hm[0]:
            return None
        q0 = D['q0']
        if len(Hm) != q0 or len(Hm[0]) != q0:
            return None
        # 精确行列式
        def det(M):
            nn = len(M)
            if nn == 1: return M[0][0]
            if nn == 2: return M[0][0] * M[1][1] - M[0][1] * M[1][0]
            t = F(0)
            for j in range(nn):
                sub = [[M[i][k] for k in range(nn) if k != j] for i in range(1, nn)]
                t += ((-1) ** j) * M[0][j] * det(sub)
            return t
        vals.append(det(Hm))
    rows = [[x * x, x * y, y * y, x, y, F(1)] for (x, y) in pts]
    A = [[rows[i][j] for j in range(6)] for i in range(6)]
    b = [[vals[i]] for i in range(6)]
    sol = solve(A, b)
    if sol is None: return None
    return sol[0]


def rat_sqrt(q):
    """若 q 是有理数的平方，返回其有理平方根；否则 None"""
    if q < 0: return None
    if q == 0: return F(0)
    n, d = q.numerator, q.denominator
    rn = int(round(n ** 0.5)); rd = int(round(d ** 0.5))
    if rn * rn == n and rd * rd == d:
        return F(rn, rd)
    return None


def conic_rational_points(co, lim=25):
    """扫小分母有理 θ1，解 θ2，返回有理点表"""
    a, b, c, d, e, g = co
    pts = []
    for pn in range(-lim, lim + 1):
        for pd in range(1, lim + 1):
            x = F(pn, pd)
            # a x² + b x y + c y² + d x + e y + g = 0  ->  c y² + (b x + e) y + (a x² + d x + g) = 0
            A2 = c
            B2 = b * x + e
            C2 = a * x * x + d * x + g
            if A2 == 0:
                if B2 == 0:
                    continue
                y = -C2 / B2
                if a * x * x + b * x * y + c * y * y + d * x + e * y + g == 0:
                    pts.append((x, y))
                continue
            disc = B2 * B2 - 4 * A2 * C2
            s = rat_sqrt(disc)
            if s is None: continue
            for sg in (1, -1):
                y = (-B2 + sg * s) / (2 * A2)
                if a * x * x + b * x * y + c * y * y + d * x + e * y + g == 0:
                    pts.append((x, y))
    # 去重
    seen = set(); out = []
    for p in pts:
        key = (p[0], p[1])
        if key in seen: continue
        seen.add(key); out.append(p)
    return out


rng = random.Random(24680001)
print("(C2) 的 k=2 检验（有理参数化）")
print()
print(f"{'#':>2} {'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'k':>2} {'s':>2} {'dCA':>4} | "
      f"{'曲线上有理点':>12} {'rankH<q0':>9} {'(A)':>5} {'(S)成立':>8} {'(S)失败':>8} {'结论':>8}")
print("-" * 104)
n_inst = 0
yes = 0; bad = 0
for trial in range(400000):
    if n_inst >= 10:
        break
    n, p, r = 5, 1, 1
    for _ in range(60):
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
        if q0 != 3: continue
        dC = n - p; s = dC - r; k = q0 - r
        if k != 2 or s != 3: continue
        D = build(Ac, Cc, Lc, Lx)
        if D is None: continue
        if not (D['dCA'] >= q0): continue
        co = q2_coeffs(D)
        if co is None: continue
        pts = conic_rational_points(co, lim=20)
        if not pts: continue
        nlt = nA = nS = nFail = 0
        for (x, y) in pts[:60]:
            Lred, Hm = exact_H([x, y], D)
            rH = rk(Hm) if (Hm and Hm[0]) else 0
            if rH >= q0: continue
            nlt += 1
            if exact_A([x, y], D):
                nA += 1
                if S_holds(Hm, mm(mm(Lred, Ac), D['NCA'])):
                    nS += 1
                else:
                    nFail += 1
        n_inst += 1
        concl = "YES" if nS >= 1 and nFail == 0 else ("**NO**" if nFail > 0 else "无A点")
        if nS >= 1 and nFail == 0: yes += 1
        if nFail > 0: bad += 1
        print(f"{n_inst:>2} {n:>2} {p:>2} {r:>2} {q0:>3} {k:>2} {s:>2} {D['dCA']:>4} | "
              f"{len(pts):>12} {nlt:>9} {nA:>5} {nS:>8} {nFail:>8} {concl:>8}")
        break

print()
print(f"=== 汇总 ===  全 YES: {yes}   出现 (S) 失败: {bad}   共 {n_inst} 实例")
print()
print("判读：")
print("  · 若全部 YES 且 bad=0 ⟹ (C2) 在 k=2 亦成立（在整条曲线上 (S) 成立）")
print("  · 若 bad>0 ⟹ (C2) 被证伪 ⟹ 情形 II 的退化集上 (S) 会失败 ⟹ 需真正的代数判定")
