# -*- coding: utf-8 -*-
"""
用精确判别式在多个 (r=p=k=1,s=3,dC=4) 实例上数 Omega* 的解数。
（不用网格 —— 网格对代数点不可靠，见教训 #22。）
"""
import math
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\exact_count_thm7.py",
           encoding="utf-8").read()
exec(src.split("rng = random.Random(112233)")[0])


def dot(x, y):
    return sum(x[i] * y[i] for i in range(len(x)))


def is_sq_frac(x):
    if x < 0:
        return False
    return math.isqrt(x.numerator) ** 2 == x.numerator and \
        math.isqrt(x.denominator) ** 2 == x.denominator


def count_solutions(b, A0, A1, A2, A3, Atilde):
    """返回 (解数, 解列表)；Atilde = 完整 Abar_T（用于直接核验 (A)）"""
    # u(θ) = u0 + θ1 u1 + θ2 u2
    u0 = [F(0), F(0), -b[3], b[2]]
    u1 = [F(0), b[3], F(0), -b[1]]
    u2 = [F(0), -b[2], b[1], F(0)]
    # f1 = u·A0 （线性）
    d00, d10, d01 = dot(u0, A0), dot(u1, A0), dot(u2, A0)
    # f2 = u·(A1 + θ1 A2 + θ2 A3) （二次，直接构造）
    c00 = dot(u0, A1)
    c10 = dot(u0, A2) + dot(u1, A1)
    c01 = dot(u0, A3) + dot(u2, A1)
    c20 = dot(u1, A2)
    c11 = dot(u1, A3) + dot(u2, A2)
    c02 = dot(u2, A3)
    if d10 == 0 and d01 == 0:
        return (None, "f1 退化")
    # 消元
    if d10 != 0:
        al, be = -d01 / d10, -d00 / d10
    else:
        # θ2 = -(d00+d10 θ1)/d01 -> 用对称处理：交换变量
        return (None, "需交换变量")
    Aq = c20 * al * al + c11 * al + c02
    Bq = 2 * c20 * al * be + c10 * al + c11 * be + c01
    Cq = c20 * be * be + c10 * be + c00
    if Aq == 0:
        if Bq == 0:
            return (0, [])
        t2 = -Cq / Bq
        return (1, [(al * t2 + be, t2)])
    Disc = Bq * Bq - 4 * Aq * Cq
    if Disc < 0:
        return (0, [])
    if Disc == 0:
        t2 = -Bq / (2 * Aq)
        return (1, [(al * t2 + be, t2)])
    if not is_sq_frac(Disc):
        return (2, "无理")          # 2 个实解但非有理
    rt = F(math.isqrt(Disc.numerator), math.isqrt(Disc.denominator))
    sols = []
    for t2 in [(-Bq + rt) / (2 * Aq), (-Bq - rt) / (2 * Aq)]:
        sols.append((al * t2 + be, t2))
    return (len(sols), sols)


rng = random.Random(97531)
print("在 (r=p=k=1, s=3, dC=4) 实例上精确数 Omega* 的解数")
print(f"{'#':>2} {'2p+q0':>5} {'<n':>4} {'解数':>5}  解")
print("-" * 78)
found = 0
tried = 0
while found < 10 and tried < 200000:
    tried += 1
    n, p, r = 5, 1, 1
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
    if sum(eta) != 2: continue
    bt = build_norm_T(Ac, Cc, Lc, Lx)
    if bt is None: continue
    dC, s, k, r2, AT, BAT = bt
    if (r2, p, k, s, dC) != (1, 1, 1, 3, 4): continue
    b = BAT[0]
    if b[1] == 0: continue
    cnt, sols = count_solutions(b, AT[0], AT[1], AT[2], AT[3], AT)
    found += 1
    if isinstance(sols, str):
        print(f"{found:>2} {2*p+2:>5} {str(2*p+2<n):>4} {str(cnt):>5}  {sols}")
    else:
        txt = "; ".join(f"({a},{c})" for (a, c) in sols)
        print(f"{found:>2} {2*p+2:>5} {str(2*p+2<n):>4} {cnt:>5}  {txt[:60]}")
print()
print(f"（共尝试 {tried} 个随机实例）")
