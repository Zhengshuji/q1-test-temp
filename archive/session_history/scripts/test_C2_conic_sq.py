# -*- coding: utf-8 -*-
"""
B-1：(C2) 的 k>=2 检验 —— 方阵 conic 版（形状经精确分析后锁定）

形状：n=6, p=1, r=2, q0=4
  ⟹ k = q0 − r = 2,  dC = 5,  s = dC − r = 3,  dimΘ = k(s−k) = 2
  ⟹ 需 rank[C;CA] = 2 才使 d_CA = n − 2 = 4 = q0（**方阵**）
  ⟹ 此时 {rank H < q0} = {det H = 0}，由定理 D1 是**二次曲线**（次数 ≤ k = 2）
  ⟹ 2p+q0 = 6 ≥ 6 = n ⟹ 也在分支 A 内；d_CA = q0 ⟹ **情形 II**

只需 η1+η2 = 4（比 η1=3 常见得多），故实例搜索快。
"""
import itertools
import random
from fractions import Fraction as F
import numpy as np

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\test_C2_conic.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random(24680001)")[0]
exec(head)


def det_exact(M):
    nn = len(M)
    if nn == 1: return M[0][0]
    if nn == 2: return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    t = F(0)
    for j in range(nn):
        sub = [[M[i][k] for k in range(nn) if k != j] for i in range(1, nn)]
        t += ((-1) ** j) * M[0][j] * det_exact(sub)
    return t


def q2_coeffs(D):
    pts = [(F(0), F(0)), (F(1), F(0)), (F(0), F(1)),
           (F(1), F(1)), (F(2), F(0)), (F(0), F(2))]
    vals = []
    q0 = D['q0']
    for (x, y) in pts:
        Lred, Hm = exact_H([x, y], D)
        if not Hm or not Hm[0] or len(Hm) != q0 or len(Hm[0]) != q0:
            return None
        vals.append(det_exact(Hm))
    rows = [[x * x, x * y, y * y, x, y, F(1)] for (x, y) in pts]
    sol = solve([[rows[i][j] for j in range(6)] for i in range(6)],
                [[vals[i]] for i in range(6)])
    return None if sol is None else sol[0]


def rat_sqrt(q):
    if q < 0: return None
    if q == 0: return F(0)
    n, d = q.numerator, q.denominator
    rn = int(round(n ** 0.5)); rd = int(round(d ** 0.5))
    return F(rn, rd) if (rn * rn == n and rd * rd == d) else None


def conic_pts(co, lim=30):
    a, b, c, d, e, g = co
    out = []; seen = set()
    for pn in range(-lim, lim + 1):
        for pd in range(1, lim + 1):
            x = F(pn, pd)
            A2, B2, C2 = c, b * x + e, a * x * x + d * x + g
            cands = []
            if A2 == 0:
                if B2 != 0: cands.append(-C2 / B2)
            else:
                s = rat_sqrt(B2 * B2 - 4 * A2 * C2)
                if s is not None:
                    cands += [(-B2 + s) / (2 * A2), (-B2 - s) / (2 * A2)]
            for y in cands:
                if a * x * x + b * x * y + c * y * y + d * x + e * y + g == 0:
                    if (x, y) not in seen:
                        seen.add((x, y)); out.append((x, y))
    return out


rng = random.Random(90090009)
print("(C2) 的 k=2 检验（方阵 conic 版：n=6,p=1,r=2,q0=4,d_CA=4）")
print()
print(f"{'#':>2} {'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'k':>2} {'s':>2} {'dCA':>4} | "
      f"{'有理点数':>9} {'rankH<q0':>9} {'(A)':>5} {'(S)成':>6} {'(S)败':>6} {'结论':>8}")
print("-" * 100)
n_inst = 0; yes = 0; bad = 0; noA = 0
for trial in range(20000):
    if n_inst >= 3:
        break
    n, p, r = 6, 1, 2
    for _ in range(40):
        Am = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
        Cm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)]
        Lm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(r)]
        Ac, Cc, Lc = toF(Am), toF(Cm), toF(Lm)
        if rk(Cc) != p or rk(Lc) != r: continue
        if rk(Lc + Cc) != r + p: continue
        if rk(Cc + mm(Cc, Ac)) != 2: continue           # 保证 d_CA = n−2 = 4
        Z = orb(Lc, Ac, n) + orb(Cc, Ac, n); OC = orb(Cc, Ac, n)
        if rk(Z + OC) != rk(OC): continue               # H4 功能可观
        try:
            Lx, eta = p1(Ac, Cc, Lc)
        except Exception:
            continue
        if not condA(Ac, Cc, Lx): continue
        q0 = sum(eta)
        if q0 != 4: continue
        dC = n - p; s = dC - r; k = q0 - r
        if k != 2 or s != 3: continue
        D = build(Ac, Cc, Lc, Lx)
        if D is None: continue
        if D['dCA'] != q0: continue
        co = q2_coeffs(D)
        if co is None: continue
        pts = conic_pts(co, lim=8)
        if not pts: continue
        nlt = nA = nS = nFail = 0
        for (x, y) in pts[:25]:
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
        if nS >= 1 and nFail == 0: yes += 1; concl = "YES"
        elif nFail > 0: bad += 1; concl = "**NO**"
        else: noA += 1; concl = "无A点"
        print(f"{n_inst:>2} {n:>2} {p:>2} {r:>2} {q0:>3} {k:>2} {s:>2} {D['dCA']:>4} | "
              f"{len(pts):>9} {nlt:>9} {nA:>5} {nS:>6} {nFail:>6} {concl:>8}")
        break

print()
print(f"=== 汇总 ===  YES: {yes}   (S) 失败: {bad}   无 A 点: {noA}   共 {n_inst}")
print()
print("判读：")
print("  · 全部 YES 且 bad=0 ⟹ (C2) 在 k=2 亦成立")
print("  · bad>0 ⟹ (C2) 被证伪 ⟹ 情形 II 需真正的代数判定")
