# -*- coding: utf-8 -*-
"""
第①项关键一步：在**构造出的秩降点**上检查 (S)

若 (S) 成立 ⟹ **构造性的 YES** ⟹ 情形 II 的判定得到完整算法雏形（构造 + 检验）
"""
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\reliable_S_test.py",
           encoding="utf-8").read()
head = src.split("# ---------- 主实验 ----------")[0]
exec(head)


def matpow(M, k):
    n = len(M)
    R = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = mm(R, M)
    return R


def ker_of(M):
    K = ker_basis(M)
    if not K: return []
    nrow = len(K); d = len(K[0])
    if d == 0: return []
    return [[K[i][j] for i in range(nrow)] for j in range(d)]


def build_system(Ac, Cc, Lc, l11, x):
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
    rows.append(x[:] + [F(0), F(0)]); rhs.append([F(0)])
    sol = solve(rows, rhs)
    if sol is None: return None
    return [sol[0][i] for i in range(n)]


def try_construct(Ac, Cc, Lc):
    """返回 (w, x, l11) 或 None"""
    n = len(Ac)
    W = Cc + mm(Cc, Ac)
    base = ker_of(Lc + W)
    if not base: return None
    xs = list(base)
    for i in range(len(base)):
        for j in range(i + 1, len(base)):
            xs.append([base[i][a] + base[j][a] for a in range(n)])
    for x in xs:
        for q in range(1, 13):
            for pnum in range(-24, 25):
                l11 = F(pnum, q)
                w = build_system(Ac, Cc, Lc, l11, x)
                if w is None: continue
                Ln = Lc + [w]
                if rk(mm(Ln, Ac) + Ln + W) == rk(Ln + W):
                    return w, x, l11
    return None


rng = random.Random(13571357)
print("第①项：构造秩降点 + 检查 (S)")
print()
print(f"{'#':>2} {'q0':>3} {'k':>2} {'d_CA':>4} | {'构造':>5} {'(A)':>5} {'T5a':>6} "
      f"{'rank H':>7} | {'(S) 成立?':>9} {'结论':>22}")
print("-" * 92)
shown = 0
yes = 0
for t in range(60000):
    if shown >= 10:
        break
    n, p, r = 5, 1, 1
    Amat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
    Cmat = [[rng.randint(-2, 2) for _ in range(n)]]
    Ac, Cc = toF(Amat), toF(Cmat)
    if rk(Cc) != p: continue
    Lc = mm(Cc, matpow(Ac, 2))
    if rk(Lc) != r: continue
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
    W = Cc + mm(Cc, Ac)
    dCA = n - rk(W)
    res = try_construct(Ac, Cc, Lc)
    shown += 1
    if res is None:
        print(f"{shown:>2} {q0:>3} {k:>2} {dCA:>4} | {'否':>5} {'—':>5} {'—':>6} "
              f"{'—':>7} | {'—':>9} {'未构造出':>22}")
        continue
    w, x, l11 = res
    Ln = Lc + [w]
    NCA = ker_basis(W)
    H = mm(Ln, NCA)
    Fm = mm(mm(Ln, Ac), NCA)
    rH = rk(H) if (H and H[0]) else 0
    okS = S_holds(H, Fm)
    if okS: yes += 1
    print(f"{shown:>2} {q0:>3} {k:>2} {dCA:>4} | {'是':>5} {'通过':>5} {'True':>6} "
          f"{rH:>7} | {str(okS):>9} "
          f"{('**构造性 YES！**' if okS else '有秩降但 (S) 失败'):>22}")

print()
print(f"=== 汇总：构造成功 {(shown)} 个实例中，(S) 成立的有 {yes} 个 ===")
print()
print("判读：")
print("  · 有 (S) 成立 ⟹ 情形 II 的**构造性 YES** ⟹ 判定 = 构造 + 检验")
print("  · 全部 (S) 失败 ⟹ 秩降点存在但 (S) 不成立，需要更强条件")
