# -*- coding: utf-8 -*-
"""最小诊断：直接打印 f2(k,0) 的有限差分，定出真实次数。"""
import random
from fractions import Fraction as F

# --- 复用 exact_count_thm7.py 的前半部分（函数定义 + 实例搜索） ---
src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\exact_count_thm7.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random(112233)")[0]
exec(head)

rng = random.Random(112233)
found = None
for trial in range(30000):
    n, p, r = 5, 1, 1
    for _ in range(150):
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
        if sum(eta) != 2: continue
        bt = build_norm_T(Ac, Cc, Lc, Lx)
        if bt is None: continue
        dC, s, k, r2, AT, BAT = bt
        if (r2, p, k, s, dC) != (1, 1, 1, 3, 4): continue
        found = (AT, BAT); break
    if found: break

AT, BAT = found
b = BAT[0]
A0, A1, A2, A3 = AT[0], AT[1], AT[2], AT[3]      # 行 0..3
print("b =", [str(x) for x in b])
print()

# u(θ) 显式线性
u0 = [F(0), F(0), -b[3], b[2]]                    # 常数项
u1 = [F(0), b[3], F(0), -b[1]]                    # θ1 系数
u2 = [F(0), -b[2], b[1], F(0)]                    # θ2 系数

def uof(t1, t2):
    return [u0[i] + t1*u1[i] + t2*u2[i] for i in range(4)]

def a2of(t1, t2):
    return [A1[j] + t1*A2[j] + t2*A3[j] for j in range(4)]

def f2(t1, t2):
    uu = uof(t1, t2); av = a2of(t1, t2)
    return sum(uu[i]*av[i] for i in range(4))

# 直接由 u0,u1,u2 与 A1,A2,A3 构造二次型系数（无任何插值）
def dot(x, y): return sum(x[i]*y[i] for i in range(4))
c00 = dot(u0, A1)
c10 = dot(u0, A2) + dot(u1, A1)
c01 = dot(u0, A3) + dot(u2, A1)
c20 = dot(u1, A2)
c11 = dot(u1, A3) + dot(u2, A2)
c02 = dot(u2, A3)
print("直接构造的二次型系数:")
print(f"  c00={c00}\n  c10={c10}\n  c01={c01}\n  c20={c20}\n  c11={c11}\n  c02={c02}")
print()

def quad(t1, t2):
    return c00 + c10*t1 + c01*t2 + c20*t1*t1 + c11*t1*t2 + c02*t2*t2

print("f2 vs 直接二次型 的一致性:")
bad = 0
for t1 in [F(-3), F(-2), F(-1), F(0), F(1), F(2), F(3), F(5, 2)]:
    for t2 in [F(-2), F(0), F(1), F(7, 3)]:
        if f2(t1, t2) != quad(t1, t2):
            bad += 1
            if bad <= 3:
                print(f"  不一致 θ=({t1},{t2}): f2={f2(t1,t2)} quad={quad(t1,t2)}")
print(f"  不一致数: {bad}")
print()

print("f2(k,0) 的值与有限差分（k=0..4）:")
vals = [f2(F(k), F(0)) for k in range(5)]
print("  值 :", [str(v) for v in vals])
d1 = [vals[i+1]-vals[i] for i in range(4)]
d2 = [d1[i+1]-d1[i] for i in range(3)]
d3 = [d2[i+1]-d2[i] for i in range(2)]
print("  一阶差分:", [str(v) for v in d1])
print("  二阶差分:", [str(v) for v in d2])
print("  三阶差分:", [str(v) for v in d3])
print(f"  => 次数 <= 2 ? {all(v == 0 for v in d3)}")
print()
print("检验 u 是否满足三个约束（在若干 θ 上）:")
for (t1, t2) in [(F(1), F(2)), (F(-3), F(5)), (F(7, 2), F(-1, 3))]:
    uu = uof(t1, t2)
    r1 = uu[0]
    r2 = uu[1] + t1*uu[2] + t2*uu[3]
    r3 = sum(b[i]*uu[i] for i in range(4))
    print(f"  θ=({t1},{t2}): u·e1={r1}  u·v={r2}  u·b={r3}")

# ================= 用正确系数做精确消元与判别式 =================
print()
print("=== f1 的正确系数（直接构造）===")
d00 = dot(u0, A0); d10 = dot(u1, A0); d01 = dot(u2, A0)
print(f"  f1 = ({d00}) + ({d10})·θ1 + ({d01})·θ2")
print(f"  f1(0,0) = {f1v(F(0),F(0)) if False else dot(uof(F(0),F(0)), A0)}")

def f1v(t1, t2):
    return sum(uof(t1,t2)[i]*A0[i] for i in range(4))
print(f"  校验 f1(1,0) 与 d00+d10: {f1v(F(1),F(0)) == d00+d10}")

print()
print("=== 消元求判别式 ===")
if d10 != 0:
    # θ1 = α θ2 + β
    al = -d01/d10; be = -d00/d10
    print(f"  θ1 = ({al})·θ2 + ({be})")
    Aq = c20*al*al + c11*al + c02
    Bq = 2*c20*al*be + c10*al + c11*be + c01
    Cq = c20*be*be + c10*be + c00
    print(f"  一元二次: A={Aq}, B={Bq}, C={Cq}")
    if Aq == 0:
        print(f"  A=0 -> 一次方程: 解数 = {0 if Bq == 0 else 1}")
    else:
        Disc = Bq*Bq - 4*Aq*Cq
        print(f"  判别式 Δ = {Disc}")
        import math
        def is_sq_frac(x):
            if x < 0: return False
            n, dd = x.numerator, x.denominator
            return math.isqrt(n)**2 == n and math.isqrt(dd)**2 == dd
        print(f"  Δ>0? {Disc>0}   Δ=0? {Disc==0}   Δ为有理平方? {is_sq_frac(Disc)}")
        nsol = 2 if Disc > 0 else (1 if Disc == 0 else 0)
        print(f"  => 实解个数 = {nsol}")
        if is_sq_frac(Disc) and Disc >= 0:
            rn = math.isqrt(Disc.numerator); rd = math.isqrt(Disc.denominator)
            rt = F(rn, rd)
            for t2v in [(-Bq+rt)/(2*Aq), (-Bq-rt)/(2*Aq)]:
                t1v = al*t2v + be
                print(f"     解 θ=({t1v}, {t2v}):  f1={f1v(t1v,t2v)}  f2={f2(t1v,t2v)}")