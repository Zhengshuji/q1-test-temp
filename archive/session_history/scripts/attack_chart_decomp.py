# -*- coding: utf-8 -*-
"""
第②项严格化（(A) 分解路线）：把 2 行增广的搜索降到**本质 1 维**

(A) ⟺ ∃Λ(2×2), G0, G1:  L·A = Λ L + G0 C + G1 CA
消去 G 后（π = 到 row(C,CA)^⊥ 的投影）：
   (I)  π(L0·A − λ11 L0) = λ12 · π(w)
   (II) π(w·A − λ21 L0 − λ22 w) = 0

(I) 把 π(w) 钉死在一条方向上（给定 λ11）⟹ 只需扫**一个**参数 λ11。

对每个 λ11：
   u := π(L0·A) − λ11 π(L0)
   · u ≠ 0 ⟹ 取 λ12 = 1, π(w) = u
   · u = 0 ⟹ 分两支：π(w) = 0，或 π(w) 取一般方向
   然后在 π 下解 (II)（对 w 的 row(C,CA) 部分与 λ21, λ22 是**线性**方程组）
   最后**精确**验证 (A)
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


def satisfies_A(Ac, Cc, L):
    return rk(mm(L, Ac) + L + Cc + mm(Cc, Ac)) == rk(L + Cc + mm(Cc, Ac))


def proj_rows(Ac, Cc):
    """返回 (NA, rkW)：NA 的列张成 row(C,CA)^⊥；π(v) = v·NA  （行向量 v -> d_CA 维）"""
    CA = mm(Cc, Ac)
    W = Cc + CA                      # 行张成 row(C,CA)
    # row(C,CA)^⊥ = ker(W)（W 视为 矩阵：W·x = 0 的解空间）
    NA = ker_basis(W)                # n × d_CA
    return NA, rk(W)


def pi(v, NA):
    """行向量 v（长度 n）-> v·NA（长度 d_CA）"""
    n = len(v)
    d = len(NA[0])
    return [sum(v[i] * NA[i][j] for i in range(n)) for j in range(d)]


def attack(Ac, Cc, Lc, nlam=60, seed=3):
    """扫 λ11，对每个解开 (II) 并精确验证"""
    n = len(Ac)
    L0A = mm(Lc, Ac)
    L0 = Lc[0]
    NA, rkW = proj_rows(Ac, Cc)
    d = len(NA[0])
    rng = random.Random(seed)
    hits = []
    # row(C,CA) 的一个补方向基（用于 w 的 row(C,CA)-部分）
    # 直接以 w 的分量为未知量更稳：w = 未知 n 维行向量
    for _ in range(nlam):
        l11 = F(rng.randint(-30, 30), rng.randint(1, 12))
        pL0A = pi(L0A[0], NA)
        pL0 = pi(L0, NA)
        u = [pL0A[j] - l11 * pL0[j] for j in range(d)]
        if all(x == 0 for x in u):
            # 两支：π(w)=0 或一般方向
            cands = [([F(0)] * d)]
            for _q in range(2):
                cands.append([F(rng.randint(-5, 5), rng.randint(1, 7)) for _ in range(d)])
        else:
            cands = [u[:]]
        for pw in cands:
            # 未知量：w(n) , λ21, λ22  —— (II) 的 d 个方程 + (I) 的 d 个方程
            # (I):  π(w) = pw  （d 个线性方程，只含 w）
            # (II): π(wA) − λ21 π(L0) − λ22 pw = 0  （d 个方程，含 w,λ21,λ22）
            # 合成线性系统，用有理数精确求解
            nv = n + 2
            rows = []
            rhs = []
            for j in range(d):        # (I)
                row = [NA[i][j] for i in range(n)] + [F(0), F(0)]
                rows.append(row); rhs.append([pw[j]])
            # π(wA) 关于 w 是线性的： (wA)·NA = w·(A·NA)
            ANA = mm(Ac, NA)          # n × d
            pL0_ = pi(L0, NA)
            for j in range(d):        # (II)
                row = [ANA[i][j] for i in range(n)] + [F(0), F(0)]
                row[n] = -pL0_[j]     # 系数 of λ21
                row[n + 1] = -pw[j]   # 系数 of λ22
                rows.append(row); rhs.append([F(0)])
            sol = solve(rows, rhs)
            if sol is None:
                continue
            x = sol[0]
            w = [x[i] for i in range(n)]
            if satisfies_A(Ac, Cc, Lc + [w]):
                hits.append((l11, w))
                return hits
    return hits


rng = random.Random(55555)
print("第②项严格化（(A) 分解路线）：本质 1 维搜索 λ11")
print()
print(f"{'#':>2} {'tag':>11} | {'η':>6} {'q0':>3} {'k':>2} | {'rank(RN_C K)':>12} | "
      f"{'命中':>6} {'结论':>26}")
print("-" * 88)
shown = 0
for t in range(30000):
    if shown >= 8:
        break
    n, p, r, m = 5, 1, 1, 2
    Amat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
    Cmat = [[rng.randint(-2, 2) for _ in range(n)]]
    Ac, Cc = toF(Amat), toF(Cmat)
    if rk(Cc) != p: continue
    if rng.random() < 0.7:
        Lc = mm(Cc, matpow(Ac, m)); tag = "gen C A^2"
    else:
        Lc = toF([[rng.randint(-2, 2) for _ in range(n)]]); tag = "random"
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
    if k != 2: continue
    NC = ker_basis(Cc); dC = len(NC[0])
    R = Lx[len(Lc):]; RNC = mm(R, NC)
    L0NC = mm(Lc, NC)
    K = ker_basis(L0NC); mK = len(K[0]) if (K and K[0]) else 0
    Kr = [[K[a][j] for a in range(dC)] for j in range(mK)]
    rkmat = [[mm(RNC, [[Kr[j][a] for a in range(dC)]])[ii][0] for j in range(mK)]
             for ii in range(k)]
    rr = rk(rkmat)
    hits = attack(Ac, Cc, Lc, nlam=80, seed=200 + t)
    shown += 1
    concl = "**2行可行 ⟹ η 高估**" if hits else "无命中 ⟹ 最小=3"
    print(f"{shown:>2} {tag:>11} | {str(eta):>6} {q0:>3} {k:>2} | {rr:>12} | "
          f"{str(len(hits)):>6} {concl:>26}")

print()
print("判读：")
print("  · 命中 ⟹ 2 行 (A)-增广存在 ⟹ p1 的 η 高估")
print("  · 全不命中 ⟹ 与前述三种搜索合计，强烈支持『图卡外的最小增广』")
