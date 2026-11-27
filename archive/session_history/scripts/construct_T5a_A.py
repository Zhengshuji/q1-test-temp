# -*- coding: utf-8 -*-
"""
第①项：构造满足 T5a ∧ (A) 的 L

思路：取 x ∈ ker L0 ∩ ker[C;CA]（若存在），要求额外行 w 满足 w·x = 0
      ⟹ x ∈ ker L ∩ ker[C;CA] ⟹ T5a 自动成立 ✓
      ⟹ 问题化为 (I) ∧ (II) ∧ (w·x=0) 是否可解

(I)  π(L0·A − λ11 L0) = λ12 π(w)
(II) π(w·A − λ21 L0 − λ22 w) = 0
未知量：w(n), λ21, λ22；固定 λ12 = 1；扫 λ11
最后**精确**验证 (A) 与 T5a
"""
import random
from fractions import Fraction as F

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


def ker_of(M):
    K = ker_basis(M)          # n × d（行数 n，列数 d）
    if not K: return []
    nrow = len(K); d = len(K[0])
    if d == 0: return []
    return [[K[i][j] for i in range(nrow)] for j in range(d)]   # d 个向量，各长 n


def solve_constrained(Ac, Cc, Lc, l11, x, rhsw):
    """解 (I)∧(II)∧(w·x = rhsw)；返回 w 或 None"""
    n = len(Ac)
    L0 = Lc[0]; L0A = mm(Lc, Ac)[0]
    W = Cc + mm(Cc, Ac); NA = ker_basis(W); d = len(NA[0])

    def pv(v):
        return [sum(v[i] * NA[i][j] for i in range(n)) for j in range(d)]

    u = [pv(L0A)[j] - l11 * pv(L0)[j] for j in range(d)]
    pw = u[:]
    ANA = mm(Ac, NA); pL0 = pv(L0)
    rows, rhs = [], []
    for j in range(d):                                   # (I)
        rows.append([NA[i][j] for i in range(n)] + [F(0), F(0)]); rhs.append([pw[j]])
    for j in range(d):                                   # (II)
        r = [ANA[i][j] for i in range(n)] + [F(0), F(0)]
        r[n] = -pL0[j]; r[n + 1] = -pw[j]
        rows.append(r); rhs.append([F(0)])
    rows.append(x[:] + [F(0), F(0)]); rhs.append([rhsw])  # w·x = 0
    sol = solve(rows, rhs)
    if sol is None:
        return None
    xx = sol[0]
    return [xx[i] for i in range(n)]


rng = random.Random(24681012)
print("第①项：构造满足 T5a ∧ (A) 的 L —— (I)∧(II)∧(w·x=0)")
print()
print(f"{'#':>2} {'q0':>3} {'k':>2} {'d_CA':>4} {'dim(kerL0∩kerC∩kerCA)':>20} | "
      f"{'扫 λ11':>7} {'命中':>5} {'(A) 精确验证':>11} {'T5a 验证':>9}")
print("-" * 96)
shown = 0
for t in range(40000):
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
    # ker L0 ∩ ker[C;CA]
    base = ker_of(Lc + W)                 # 交集 = ker[L0; C; CA]
    if not base: continue
    # 遍历候选 x：所有基向量 + 两两组合（线性组合）
    xs = list(base)
    for i in range(len(base)):
        for j in range(i + 1, len(base)):
            xs.append([base[i][a] + base[j][a] for a in range(n)])
    found = None
    lam_used = None
    for x in xs:
        for q in range(1, 13):
            for pnum in range(-24, 25):
                l11 = F(pnum, q)
                w = solve_constrained(Ac, Cc, Lc, l11, x, F(0))
                if w is None: continue
                Ln = Lc + [w]
                if rk(mm(Ln, Ac) + Ln + W) == rk(Ln + W):     # (A)
                    found = w; lam_used = l11; break
            if found: break
        if found: break
    shown += 1
    if found:
        Ln = Lc + [found]
        NCA = ker_basis(W)
        t5a = (n - rk(Ln + W)) > 0                        # ker L ∩ ker[C;CA] ≠ 0
        print(f"{shown:>2} {q0:>3} {k:>2} {dCA:>4} {len(base):>20} | "
              f"{str(len(xs)):>7} {'是':>5} {'通过':>11} {str(t5a):>9}")
    else:
        print(f"{shown:>2} {q0:>3} {k:>2} {dCA:>4} {len(base):>20} | "
              f"{str(len(xs)):>7} {'否':>5} {'—':>11} {'—':>9}")

print()
print("判读：")
print("  · 命中 ⟹ 该实例存在满足 T5a ∧ (A) 的 L ⟹ 情形 II 的秩降点可**构造性**地找到")
print("  · 全不命中 ⟹ 需要更强的构造（或该系统恒不可解）")
