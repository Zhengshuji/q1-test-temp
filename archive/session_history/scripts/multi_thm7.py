from fractions import Fraction as F
import random, sys
sys.path.insert(0, r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core")
exec(open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\verify_thm7.py", encoding="utf-8").read().split("rng = random.Random")[0])

rng = random.Random(31415)
print("多实例：检验两式是否恒为线性 + 二次型系数")
print(f"{'#':>2} {'b2':>6} {'二次型(θ1²,θ1θ2,θ2²)':>28} {'两式线性?':>10}")
cnt_lin = 0
for t_ in range(8):
    found = None
    for trial in range(4000):
        n, p, r = 5, 1, 1
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
            if sum(eta) != 2: continue
            pr = prep(Ac, Cc, Lc, Lx)
            if pr is None: continue
            dC, s, k, r2, AT, BAT = pr
            if (r2, p, k, s, dC) != (1, 1, 1, 3, 4): continue
            found = (AT, BAT); break
        if found: break
    if not found:
        continue
    AT, BAT = found
    b = BAT[0]
    if b[1] == 0: continue
    a1, a2, a3, a4 = AT[0], AT[1], AT[2], AT[3]
    def u_of(t1, t2):
        return [F(0), b[3]*t1 - b[2]*t2, -(b[3] - b[1]*t2), b[2] - b[1]*t1]
    def f2(t1, t2):
        u = u_of(t1, t2)
        a2v = [a2[j] + t1*a3[j] + t2*a4[j] for j in range(4)]
        return sum(u[i]*a2v[i] for i in range(4))
    def f1(t1, t2):
        u = u_of(t1, t2); return sum(u[i]*a1[i] for i in range(4))
    def quad_coeffs(f):
        f00=f(F(0),F(0)); f10=f(F(1),F(0)); f01=f(F(0),F(1))
        f20=f(F(2),F(0)); f11=f(F(1),F(1)); f02=f(F(0),F(2))
        c11 = f11 - f10 - f01 + f00
        c20 = (f20 - 2*f10 + f00 - c11*0)
        c02 = (f02 - 2*f01 + f00)
        return (c20, c11, c02)
    q1 = quad_coeffs(f1); q2 = quad_coeffs(f2)
    lin = (q1 == (0,0,0)) and (q2 == (0,0,0))
    if lin: cnt_lin += 1
    print(f"{t_:>2} {str(b[1]):>6} {str(q2):>28} {str(lin):>10}")
print()
print(f"两式皆为线性的实例: {cnt_lin}")
