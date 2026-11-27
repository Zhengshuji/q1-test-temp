# -*- coding: utf-8 -*-
"""
在仿射退化集上判定 (A)∧(S)  —— 直接检验猜想 (C1)

形状 n=6,p=2,r=1,q0=2（k=1, d_CA=q0=2, dimTheta=2）：
  {rank H < q0} = {det H = 0}，而 det H 仿射 ⟹ 一条**直线**。
  沿直线取点，精确检验 (A) 与 (S)。若某点 (A)∧(S) 成立 ⟹ 该实例 YES。
"""
import itertools
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\decide_caseII_empty.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random(44332211)")[0]
exec(head)


def on_locus_points(co, npts=40):
    """由仿射 det H = d θ1 + e θ2 + g = 0 给出一批直线上的点"""
    a, b, c, d, e, g = co
    pts = []
    if d != 0:
        for k in range(-npts, npts + 1):
            y = F(k, 3)
            x = -(e * y + g) / d
            pts.append([x, y])
    elif e != 0:
        for k in range(-npts, npts + 1):
            x = F(k, 3)
            y = -(d * x + g) / e
            pts.append([x, y])
    return pts


rng = random.Random(13572468)
print("在仿射退化集上判定 (A)∧(S)")
print()
print(f"{'#':>2} {'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'dCA':>4} | "
      f"{'线上取点数':>9} {'rankH<q0':>9} {'(A)数':>6} {'(S)数':>6} {'结论':>14}")
print("-" * 84)
n_inst = 0
yes = 0
for trial in range(200000):
    if n_inst >= 6:
        break
    n, p, r = 6, 2, 1
    for _ in range(30):
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
        if k * (s - k) != 2: continue
        if 2 * p + q0 < n: continue
        D = build(Ac, Cc, Lc, Lx)
        if D is None: continue
        if not (D['dCA'] == q0 == 2): continue
        co = detH_quad(D)
        if co is None: continue
        pts = on_locus_points(co, npts=40)
        nlt = nA = nS = 0
        for t in pts:
            Lred, Hm = exact_H(t, D)
            rH = rk(Hm) if (Hm and Hm[0]) else 0
            if rH >= q0: continue
            nlt += 1
            if exact_A(t, D):
                nA += 1
                if S_holds(Hm, mm(mm(Lred, Ac), D['NCA'])):
                    nS += 1
        n_inst += 1
        ok = (nS >= 1)
        if ok: yes += 1
        print(f"{n_inst:>2} {n:>2} {p:>2} {r:>2} {q0:>3} {D['dCA']:>4} | "
              f"{len(pts):>9} {nlt:>9} {nA:>6} {nS:>6} "
              f"{('YES' if ok else 'NO'):>14}")
        break

print()
print(f"=== 汇总 ===  YES: {yes} / {n_inst}")
print()
print("判读：")
print("  · 若全部 YES ⟹ 支持猜想 (C1)（情形 II 恒 YES ⟹ 判定平凡）")
print("  · 若出现 NO ⟹ (C1) 被证伪 ⟹ 情形 II 的答案依实例而定 ⟹ 需真正的判定算法（硬度落点）")
