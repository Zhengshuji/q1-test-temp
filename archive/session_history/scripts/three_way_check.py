# -*- coding: utf-8 -*-
"""
决定性对照：对同一实例同一 Θ，比较三个判据
  (a) 三块既约形式  rank[W;B;W Abar_T] == rank[W;B]
  (b) K/K' 判据      Γ ∩ K ⊆ K'   （Γ=graph(Θ)）
  (c) 铅笔判据       row(DΘ+E) ⊆ row(BΘ+C)
并对照原始 4 块 (A)（由 Θ 反推 L 后直接算）。
"""
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\exact_count_thm7.py",
           encoding="utf-8").read()
exec(src.split("rng = random.Random(112233)")[0])


def dot(x, y):
    return sum(x[i] * y[i] for i in range(len(x)))


def ker_of(M):
    return ker_basis(M)


rng = random.Random(13)
found = None
for trial in range(20000):
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
        found = (Ac, Cc, Lc, AT, BAT, Lx); break
    if found: break

Ac, Cc, Lc, AT, BAT, Lx = found
dC = 4; s = 3; k = 1; r = 1; p = 1
b = BAT[0]
Bmat = [[BAT[i][r + j] for j in range(k)] for i in range(len(BAT))]            # p × k
Cmat = [[BAT[i][r + k + j] for j in range(s - k)] for i in range(len(BAT))]   # p × (s-k)
print("B =", [str(x) for x in Bmat[0]], "  C =", [str(x) for x in Cmat[0]])
print()

# N 的商像：gamma(theta) = (gamma1, gamma2)
def gamma_of(t):
    """t = (θ1,θ2)；返回 W_J Abar_T 的 r+k 行的商像（各 s 维）"""
    WJ = []
    for i in range(r):
        WJ.append([F(1) if j == i else F(0) for j in range(dC)])
    idx = 0
    for i in range(k):
        row = [F(0)] * dC
        row[r + i] = F(1)
        for j in range(k, s):
            row[r + j] = t[idx]; idx += 1
        WJ.append(row)
    NJ = mm(WJ, AT)
    return [[NJ[i][r + j] for j in range(s)] for i in range(r + k)]

def a3(t):
    """三块既约形式"""
    WJ = []
    for i in range(r):
        WJ.append([F(1) if j == i else F(0) for j in range(dC)])
    idx = 0
    for i in range(k):
        row = [F(0)] * dC
        row[r + i] = F(1)
        for j in range(k, s):
            row[r + j] = t[idx]; idx += 1
        WJ.append(row)
    MB = WJ + BAT
    MX = WJ + BAT + mm(WJ, AT)
    return rk(MB) == rk(MX)

def b_KK(t):
    """Γ ∩ K ⊆ K'"""
    # Γ = graph: {(θ1 u, θ2 u, u)} 用 (u,v1,v2) 坐标
    # K = ker[B | C]  (1×3)
    Kmat = [Bmat[0] + Cmat[0]]
    K = ker_of(Kmat)                      # 3 × dim
    # K' = ker[D | E]
    g = gamma_of(t)                       # (r+k) × s
    D = [[g[i][j] for j in range(k)] for i in range(r + k)]              # (r+k) × k
    E = [[g[i][k + j] for j in range(s - k)] for i in range(r + k)]      # (r+k) × (s-k)
    Kp = ker_of([D[i] + E[i] for i in range(r + k)])
    # Γ 的基（graph of Θ）：对每个 v 基向量 e_j，给出 (Θ e_j, e_j)
    Th = [[t[i * (s - k) + j] for j in range(s - k)] for i in range(k)]
    G = []
    for j in range(s - k):
        vec = [Th[i][j] for i in range(k)] + [F(1) if a == j else F(0) for a in range(s - k)]
        G.append(vec)
    # Γ ∩ K：解 G 的线性组合在 K 中 => 用坐标
    # 把 Γ 的基写成列，求 ∩ K
    # 简便：Γ 的元素 = sum c_j G[j]；要求 ∈ K
    if not K or not K[0]:
        return True
    dK = len(K[0])
    # K 的基按列：Kmat 的核向量
    # 求 Γ∩K：解 [G^T ; K^T] …用「两个子空间的交」标准做法
    # 交集 = ker[ G^T 的零化 ]… 这里直接：求 c 使 sum c_j G_j ∈ K
    # 即 sum c_j G_j 与 K 的正交补正交
    Korth = ker_of(tr(K))   # K^perp 的基（按列）
    # （下面直接按标准做法求 Γ∩K）
    # 直接：Γ∩K 由 ker[[G 的零化],[K 的零化]] ... 换用：G 与 K 的基张成的空间中，交集
    # 用标准公式：dim(Γ∩K) = dimΓ + dimK - dim(Γ+K)
    GK = G + [[K[a][j] for a in range(3)] for j in range(dK)]
    dimGK = rk(GK)
    dimInter = len(G) + dK - dimGK
    if dimInter == 0:
        return True                     # Γ∩K = {0} ⊆ K'
    # 求交集的一组基（用坐标法）
    # Γ 的元素 = Gcoef^T G；要在 K 中
    # 用「联立」：向量 x = sum c_j G_j，要求 x ⟂ K^perp
    Kperp = ker_of(tr(K))               # 3 × dKperp（K^perp 的基，按列）
    if not Kperp or not Kperp[0]:
        return True
    dP = len(Kperp[0])
    # 条件：对每个 p in Kperp: <sum c_j G_j, p> = 0
    Mcon = [[dot(G[j], [Kperp[x][a] for x in range(3)]) for j in range(len(G))]
            for a in range(dP)]
    # 求 Mcon c = 0 的解空间基
    cB = ker_of(Mcon)                   # len(G) × ?
    if cB and cB[0]:
        interG = []
        for t_ in range(len(cB[0])):
            coef = [cB[j][t_] for j in range(len(G))]
            vec = [sum(coef[j] * G[j][x] for j in range(len(G))) for x in range(3)]
            interG.append(vec)
    else:
        interG = []
    if not interG:
        return True
    # 检查 interG 是否都在 K' 中
    for v in interG:
        if rk(Kp + [v]) != rk(Kp):
            return False
    return True

def c_pencil(t):
    """row(DΘ+E) ⊆ row(BΘ+C)"""
    Th = [[t[i * (s - k) + j] for j in range(s - k)] for i in range(k)]
    P = [[sum(Bmat[i][a] * Th[a][j] for a in range(k)) + Cmat[i][j]
          for j in range(s - k)] for i in range(p)]
    g = gamma_of(t)
    D = [[g[i][j] for j in range(k)] for i in range(r + k)]
    E = [[g[i][k + j] for j in range(s - k)] for i in range(r + k)]
    Q = [[sum(D[i][a] * Th[a][j] for a in range(k)) + E[i][j]
          for j in range(s - k)] for i in range(r + k)]
    return rk(P + Q) == rk(P)

print("对照测试（一般有理数 Θ）:")
print(f"{'θ':>26} {'(a)三块':>8} {'(b)K/K′':>8} {'(c)铅笔':>8}")
print("-" * 60)
cnt = {'a': 0, 'b': 0, 'c': 0}
for _ in range(20):
    t = [F(rng.randint(-97, 97), rng.randint(1, 89)) * (1 if rng.random() < 0.5 else -1)
         for _ in range(2)]
    ra, rb, rc = a3(t), b_KK(t), c_pencil(t)
    cnt['a'] += ra; cnt['b'] += rb; cnt['c'] += rc
    print(f"{str(t):>26} {str(ra):>8} {str(rb):>8} {str(rc):>8}")
print()
print(f"命中数: (a)={cnt['a']}/20  (b)={cnt['b']}/20  (c)={cnt['c']}/20")
