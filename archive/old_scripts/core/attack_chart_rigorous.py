# -*- coding: utf-8 -*-
"""
第②项**严格收尾**：把 M(λ) 与 [M|b](λ) 的 6×6 子式插值成 λ 的多项式

逻辑：
  rank M(λ) = 6  ⟺  M 的某个 6×6 子式 ≠ 0
  若 M 的**全部** 6×6 子式 ≡ 0            ⟹ rank M ≤ 5 对一切 λ
  若 [M|b] 的某个 6×6 子式 ≢ 0           ⟹ rank[M|b] = 6 在其非零点
  ⟹ rank[M|b] > rank M  ⟹ 不相容
  严格收尾：若 [M|b] 全部 6×6 子式的 **gcd 是非零常数**，则它们无公共零点
            ⟹ rank[M|b] = 6 **对一切 λ** ⟹ **恒不相容** ✓
"""
import random
from fractions import Fraction as F
import itertools

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\exact_count_thm7.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random")[0]
exec(head)


def matpow(M, k):
    n = len(M)
    R = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = mm(R, M)
    return R


def det(M):
    n = len(M)
    if n == 0: return F(1)
    if n == 1: return M[0][0]
    if n == 2: return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    t = F(0)
    for j in range(n):
        sub = [[M[i][k] for k in range(n) if k != j] for i in range(1, n)]
        t += ((-1) ** j) * M[0][j] * det(sub)
    return t


def build(Ac, Cc, Lc, l11):
    n = len(Ac)
    L0 = Lc[0]; L0A = mm(Lc, Ac)[0]
    W = Cc + mm(Cc, Ac); NA = ker_basis(W); d = len(NA[0])

    def pv(v):
        return [sum(v[i] * NA[i][j] for i in range(n)) for j in range(d)]

    u = [pv(L0A)[j] - l11 * pv(L0)[j] for j in range(d)]
    pw = u[:]
    ANA = mm(Ac, NA); pL0 = pv(L0)
    rows, rhs = [], []
    for j in range(d):
        rows.append([NA[i][j] for i in range(n)] + [F(0), F(0)]); rhs.append([pw[j]])
    for j in range(d):
        r = [ANA[i][j] for i in range(n)] + [F(0), F(0)]
        r[n] = -pL0[j]; r[n + 1] = -pw[j]
        rows.append(r); rhs.append([F(0)])
    return rows, [rhs[i][0] for i in range(len(rhs))]


def interp(vals, pts):
    """拉格朗日插值（vals/pts 等长，返回升幂系数列表）"""
    m = len(pts)
    coef = [F(0)] * m
    for i in range(m):
        num = [F(1)]; den = F(1)
        for j in range(m):
            if j == i: continue
            new = [F(0)] * (len(num) + 1)
            for a, c in enumerate(num):
                new[a + 1] += c
                new[a] -= c * pts[j]
            num = new; den *= (pts[i] - pts[j])
        for a in range(len(num)):
            coef[a] += vals[i] * num[a] / den
    while len(coef) > 1 and coef[-1] == 0:
        coef.pop()
    return coef


def pgcd(a, b):
    a = [x for x in a]; b = [x for x in b]
    while len(a) > 1 and a[-1] == 0: a.pop()
    while len(b) > 1 and b[-1] == 0: b.pop()
    if len(b) == 1 and b[0] == 0: return a
    while not (len(b) == 1 and b[0] == 0):
        r = [x for x in a]
        db, lb = len(b) - 1, b[-1]
        while len(r) - 1 >= db and not (len(r) == 1 and r[0] == 0):
            dd = len(r) - 1 - db
            f = r[-1] / lb
            for i in range(db + 1):
                r[dd + i] -= f * b[i]
            while len(r) > 1 and r[-1] == 0: r.pop()
            if len(r) - 1 < db: break
        a, b = b, r
    return [x / a[-1] for x in a]


rng = random.Random(777001)
print("第②项严格收尾：子式插值 ⟹ 判定『恒不相容』")
print()
print(f"{'#':>2} | {'M 的 6×6 子式全 ≡0?':>20} | {'[M|b] 子式的 gcd 次数':>21} | {'结论':>30}")
print("-" * 84)
shown = 0
for t in range(40000):
    if shown >= 3:
        break
    n, p, r, m = 5, 1, 1, 2
    Amat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
    Cmat = [[rng.randint(-2, 2) for _ in range(n)]]
    Ac, Cc = toF(Amat), toF(Cmat)
    if rk(Cc) != p: continue
    Lc = mm(Cc, matpow(Ac, m))
    if rk(Lc) != r: continue
    if rk(Lc + Cc) != r + p: continue
    Z = orb(Lc, Ac, n) + orb(Cc, Ac, n); OC = orb(Cc, Ac, n)
    if rk(Z + OC) != rk(OC): continue
    try:
        Lx, eta = p1(Ac, Cc, Lc)
    except Exception:
        continue
    if not condA(Ac, Cc, Lx): continue
    if sum(eta) - r != 2: continue
    # 7 个插值点（子式次数 ≤ 6）
    pts = [F(0), F(1), F(2), F(3), F(4), F(5), F(6)]
    colsM = 7; colsMb = 8
    minorsM = [[] for _ in range(7)]        # C(7,6)=7 个 6×6 子式
    minorsMb = [[] for _ in range(28)]      # C(8,6)=28
    combM = list(itertools.combinations(range(colsM), 6))
    combMb = list(itertools.combinations(range(colsMb), 6))
    for lv in pts:
        rows, b = build(Ac, Cc, Lc, lv)
        for idx, cc in enumerate(combM):
            sub = [[rows[i][j] for j in cc] for i in range(len(rows))]
            minorsM[idx].append(det(sub))
        aug = [rows[i] + [b[i]] for i in range(len(rows))]
        for idx, cc in enumerate(combMb):
            sub = [[aug[i][j] for j in cc] for i in range(len(aug))]
            minorsMb[idx].append(det(sub))
    polysM = [interp(v, pts) for v in minorsM]
    polysMb = [interp(v, pts) for v in minorsMb]
    allMzero = all(len(q) == 1 and q[0] == 0 for q in polysM)
    g = None
    for q in polysMb:
        if len(q) == 1 and q[0] == 0: continue
        g = q if g is None else pgcd(g, q)
    shown += 1
    if not allMzero:
        concl = "M 有满秩点 ⟹ 需另查"
    elif g is None:
        concl = "[M|b] 子式全 ≡0 ⟹ 需细分"
    elif len(g) == 1 and g[0] != 0:
        concl = "**恒不相容 ⟹ 严格确认**"
    else:
        concl = f"有公共根（次数 {len(g)-1}）⟹ 需在该 λ 处复查"
    print(f"{shown:>2} | {str(allMzero):>20} | {str(len(g)-1 if g else 'None'):>21} | {concl:>30}")

print()
print("判读：")
print("  · 『恒不相容』⟹ 该实例**不存在** 2 行 (A)-增广（严格）")
print("    ⟹ 与 q0=3 合计 ⟹ 这是**图卡外的最小增广** ⟹ P1 Thm 3 不完整（严格）")
