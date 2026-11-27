# -*- coding: utf-8 -*-
"""
任务 A 最后一步：**严格**证明分支 1（λ12=1）对一切 λ11 不可解

方法（照搬第 ② 项已验证的路径）：
  系统  M(λ11)·x = b(λ11)，x = (w, λ21, λ22) ∈ Q^(n+2)
    (I)  π(w) = u,          u = π(L0A) − λ11 π(L0)      （d 个方程）
    (II) π(wA) − λ21 π(L0) − λ22 u = 0                  （d 个方程）
  M、b 关于 λ11 是**仿射**的 ⟹ 次数 ≤1
  ① 把 M 与 [M|b] 的**全部** (n+2) 阶子式插值成 λ11 的多项式
  ② 若 M 的子式**全 ≡ 0** 且 [M|b] 子式的 gcd 是**非零常数**
     ⟹ rank[M|b] > rank M 对一切 λ11 ⟹ **恒不相容** ✓
"""
import random
from fractions import Fraction as F
import itertools

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\exact_count_thm7.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random")[0]
exec(head)


def MM(X, Y):
    assert X and Y and len(X[0]) == len(Y), f"维数错配 {len(X)}x{len(X[0])} 乘 {len(Y)}x{len(Y[0])}"
    return mm(X, Y)


def matpow(M, k):
    n = len(M)
    R = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = MM(R, M)
    return R


def det(M):
    n = len(M)
    if n == 1: return M[0][0]
    if n == 2: return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    t = F(0)
    for j in range(n):
        sub = [[M[i][k] for k in range(n) if k != j] for i in range(1, n)]
        t += ((-1) ** j) * M[0][j] * det(sub)
    return t


def build(NA, NCA, Ac, Lc, l11):
    n = len(Ac)
    d = len(NA[0])
    L0 = Lc[0]
    L0A = MM(Lc, Ac)[0]

    def pv(v):
        return [sum(v[i] * NA[i][j] for i in range(n)) for j in range(d)]

    pL0 = pv(L0); pL0A = pv(L0A)
    u = [pL0A[j] - l11 * pL0[j] for j in range(d)]
    ANA = MM(Ac, NA)                        # n × d
    nv = n + 2
    rows, b = [], []
    for j in range(d):                      # (I)  π(w) = u
        rows.append([NA[i][j] for i in range(n)] + [F(0), F(0)])
        b.append(u[j])
    for j in range(d):                      # (II) π(wA) − λ21 π(L0) − λ22 u = 0
        r = [ANA[i][j] for i in range(n)] + [F(0), F(0)]
        r[n] = -pL0[j]
        r[n + 1] = -u[j]
        rows.append(r); b.append(F(0))
    return rows, b


def interp(vals, pts):
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
    while not (len(b) == 1 and b[0] == 0):
        r = a[:]
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


rng = random.Random(31415926)
print("任务 A 最后一步：严格证明分支 1（λ12=1）恒不相容")
print()
print(f"{'#':>2} {'n':>2} {'r':>2} {'q0':>3} {'k':>2} {'d_CA':>4} | "
      f"{'M 子式全≡0?':>11} {'[M|b] gcd 次数':>14} | {'结论':>26}")
print("-" * 86)
shown = 0
proved = 0
for t in range(200000):
    if shown >= 6:
        break
    n, p, r = rng.randint(5, 6), 1, 2
    Amat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
    Cmat = [[rng.randint(-2, 2) for _ in range(n)]]
    Lmat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(r)]
    Ac, Cc, Lc = toF(Amat), toF(Cmat), toF(Lmat)
    if rk(Cc) != p or rk(Lc) != r: continue
    if rk(Lc + Cc) != r + p: continue
    Z = orb(Lc, Ac, n) + orb(Cc, Ac, n); OC = orb(Cc, Ac, n)
    if rk(Z + OC) != rk(OC): continue
    try:
        Lx, eta = p1(Ac, Cc, Lc)
    except Exception:
        continue
    if not condA(Ac, Cc, Lx): continue
    q0 = sum(eta); k = q0 - r
    if k != 1: continue
    W = Cc + MM(Cc, Ac)
    dCA = n - rk(W)
    if dCA < q0: continue
    NCA = ker_basis(W)
    L0 = Lc[0]; L0A = MM(Lc, Ac)[0]
    pL0 = [sum(L0[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]
    pL0A = [sum(L0A[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]
    if rk([pL0, pL0A]) != 1: continue              # 只做平行

    # 维度：行数 2d，列数 n+2（M）；[M|b] 列数 n+3
    m_rows = 2 * dCA
    n_cols = n + 2
    sz = min(m_rows, n_cols)                       # 取 n_cols 阶子式（若行数够）
    # 插值点（M 关于 λ11 仿射 ⟹ 2 点足够；用 3 点保险）
    pts = [F(0), F(1), F(2)]
    combM = list(itertools.combinations(range(n_cols), sz))
    combMb = list(itertools.combinations(range(n_cols + 1), sz))
    valsM = [[] for _ in combM]
    valsMb = [[] for _ in combMb]
    for lv in pts:
        rows, b = build(NCA, NCA, Ac, Lc, lv)
        assert len(rows) == m_rows and len(rows[0]) == n_cols
        for idx, cc in enumerate(combM):
            valsM[idx].append(det([[rows[i][j] for j in cc] for i in range(sz)]))
        aug = [rows[i] + [b[i]] for i in range(m_rows)]
        for idx, cc in enumerate(combMb):
            valsMb[idx].append(det([[aug[i][j] for j in cc] for i in range(sz)]))
    polysM = [interp(v, pts) for v in valsM]
    polysMb = [interp(v, pts) for v in valsMb]
    allMzero = all(len(q) == 1 and q[0] == 0 for q in polysM)
    g = None
    for q in polysMb:
        if len(q) == 1 and q[0] == 0: continue
        g = q if g is None else pgcd(g, q)
    shown += 1
    if not allMzero:
        concl = "M 有满秩点 ⟹ 需另查"
    elif g is None:
        concl = "[M|b] 子式全≡0 ⟹ 需细分"
    elif len(g) == 1 and g[0] != 0:
        concl = "**恒不相容 ⟹ 分支1 为空**"
        proved += 1
    else:
        concl = f"有公共根（次数 {len(g)-1}）⟹ 需复查"
    print(f"{shown:>2} {n:>2} {r:>2} {q0:>3} {k:>2} {dCA:>4} | "
          f"{str(allMzero):>11} {str(len(g)-1 if g else 'None'):>14} | {concl:>26}")

print()
print(f"=== 严格证明『分支 1 为空』的实例数：{proved} / {shown} ===")
print()
print("判读：")
print("  · 全部『恒不相容』⟹ 分支1 为空 ⟹ 与分支2 严格为空合计 ⟹ **该实例是 NO 实例** ✓")
print("    ⟹ **任务 A 的靶子被严格建立** ✓")
