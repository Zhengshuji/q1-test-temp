# -*- coding: utf-8 -*-
"""
决定性判定：那 4 个『未找到』的实例中，{rank H < q0} 到底是空还是优化器失败？

设定：d_CA = q0 = 2，dimTheta = 2 ⟹ H 是 2x2，{rank H < q0} = {det H = 0}，
det H(θ1,θ2) 是**二元二次多项式**（H 关于 Θ 仿射）。

判定方法（精确有理算术，不用优化器）：
  写出 f = det H = a θ1² + b θ1θ2 + c θ2² + d θ1 + e θ2 + g
  配方：f = α·u² + β·v² + γ  （线性可逆变换）
  f = 0 有实解 ⟺  (α,β 异号)  或  (γ 与 α 同号且 α,β 同号)  或 (γ = 0 且 …)
  即：**f 的符号像**是否含 0。
"""
import itertools
import random
from fractions import Fraction as F

import numpy as np

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\test_C1_wider.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random(99887766)")[0]
exec(head)


def det2(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]


def detH_quad(D):
    """精确求 det H(θ1,θ2) 的 6 个系数（二次插值）"""
    pts = [(F(0), F(0)), (F(1), F(0)), (F(0), F(1)),
           (F(1), F(1)), (F(2), F(0)), (F(0), F(2))]
    vals = []
    for (x, y) in pts:
        Lred, Hm = exact_H([x, y], D)
        vals.append(det2(Hm))
    # f = a x^2 + b xy + c y^2 + d x + e y + g
    # 由 6 个点解出 6 个系数（线性方程组，精确）
    rows = []
    for (x, y) in pts:
        rows.append([x * x, x * y, y * y, x, y, F(1)])
    A = [[rows[i][j] for j in range(6)] for i in range(6)]
    b = [[vals[i]] for i in range(6)]
    sol = solve(A, b)
    if sol is None:
        return None
    return sol[0]


def has_real_zero(a, b, c, d, e, g):
    """f = a x² + b xy + c y² + d x + e y + g 是否有实零点（精确判定）"""
    # 齐次部分矩阵 M = [[a, b/2],[b/2, c]]
    # 用可逆线性变换把 f 化为 α u² + β v² + γ
    # 判别式法：先消交叉项
    if b != 0:
        # 完成平方：a x² + b xy = a (x + b y/(2a))² - b² y²/(4a)   (a ≠ 0 时)
        if a != 0:
            c2 = c - b * b / (4 * a)
            e2 = e
            d2 = d
            # f = a·(x + b y/(2a))² + c2 y² + d x + e2 y + g
            # 令 u = x + b y/(2a) ⟹ d x = d u - d b y/(2a)
            e3 = e2 - d * b / (2 * a)
            g3 = g
            # f = a u² + c2 y² + d u + e3 y + g3
            # 配方：a(u + d/(2a))² + c2(y + e3/(2 c2))² + g3 - d²/(4a) - e3²/(4 c2)
            gg = g3 - d2 * d2 / (4 * a)
            if c2 != 0:
                gg = gg - e3 * e3 / (4 * c2)
                # f = a U² + c2 V² + gg
                # 有实零点 ⟺ gg 落在 a·ℝ≥0 + c2·ℝ≥0 中
                if a * c2 < 0:            # 异号（双曲型）⟹ 值域为 ℝ ⟹ 有零点
                    return True
                # 同号
                if gg == 0:
                    return True
                return (gg * a < 0)       # gg 与 a 异号 ⟹ 可被 a U²+c2 V² 抵消
            else:
                # c2 = 0: f = a U² + e3 y + gg  (e3 已调整) —— 检查 y 方向能否归零
                if e3 != 0:
                    return True           # y 可取任意值使 e3 y 补偿 a U²+gg
                return (gg * a <= 0)
        else:
            # a = 0, b ≠ 0 ⟹ 有 xy 项 ⟹ 双曲型 ⟹ 值域为 ℝ
            return True
    # b = 0: f = a x² + c y² + d x + e y + g
    gg = g
    if a != 0:
        gg -= d * d / (4 * a)
    if c != 0:
        gg -= e * e / (4 * c)
    if a == 0 and c == 0:
        return (d == 0 and e == 0 and gg == 0) or (d != 0 or e != 0)
    if a == 0 or c == 0:
        return True                      # 退化为一次 ⟹ 一般有解
    if a * c < 0:
        return True
    if gg == 0:
        return True
    return (gg * a < 0)


rng = random.Random(44332211)
print("判定『未找到』的实例：{rank H < q0} 是空集，还是优化器失败？")
print("（d_CA = q0 = 2, dimTheta = 2 ⟹ H 是 2x2，条件 = det H = 0，二元二次型）")
print()
print(f"{'#':>2} {'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'dCA':>4} | "
      f"{'det H 系数 (a,b,c,d,e,g)':>44} {'有实零点':>9} {'结论':>22}")
print("-" * 108)
n_inst = 0
for trial in range(200000):
    if n_inst >= 8:
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
        a, b, c, d, e, g = co
        hz = has_real_zero(a, b, c, d, e, g)
        n_inst += 1
        cs = "(" + ",".join(str(x) for x in (a, b, c, d, e, g)) + ")"
        concl = ("{rankH<q0} ≠ ∅ ⟹ 需再查(A)∧(S)" if hz
                 else "{rankH<q0} = ∅ ⟹ 恒 NO")
        print(f"{n_inst:>2} {n:>2} {p:>2} {r:>2} {q0:>3} {D['dCA']:>4} | "
              f"{cs:>44} {str(hz):>9} {concl:>22}")
        break

print()
print("判读：")
print("  · 若全部『有实零点 = False』⟹ 那 4 个『未找到』是真的不存在 ⟹ **猜想 (C1) 被证伪**")
print("    ⟹ 情形 II 的答案**依实例而定**（YES 与 NO 都会出现）⟹ 需真正的判定算法 ⟹ 硬度落点确认")
print("  · 若出现『有实零点 = True』⟹ 是优化器失败，需改进搜索")
