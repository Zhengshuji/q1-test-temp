# -*- coding: utf-8 -*-
"""最小诊断：直接构造 (I)∧(II) 的解 w，然后**逐步手工核对** (A)"""
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


rng = random.Random(20250101)
got = None
for t in range(20000):
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
    if len(Lx) - len(Lc) != 2: continue
    got = (Ac, Cc, Lc, Lx, eta); break

Ac, Cc, Lc, Lx, eta = got
n = 5
print("实例：n=5 p=1 r=1  L0 = C·A^2   η =", eta, " q0 =", sum(eta))
print()
CA = mm(Cc, Ac)
W = Cc + CA
NA = ker_basis(W)                     # n × d_CA
d = len(NA[0])
rkW = rk(W)
print(f"rank[C;CA] = {rkW},  d_CA = {d}  （NA 是 {len(NA)}×{d}）")
NAt = [[NA[i][j] for i in range(n)] for j in range(d)]   # d × n，为便于行向量乘


def pv(v):
    """π(v) = v·NA  （v 为行向量长度 n）"""
    return [sum(v[i] * NAt[j][i] for i in range(n)) for j in range(d)]


L0 = Lc[0]
L0A = mm(Lc, Ac)[0]
print("π(L0) =", [str(x) for x in pv(L0)])
print("π(L0·A) =", [str(x) for x in pv(L0A)])
print()

# 逐点：任取 λ11，构造 (I)∧(II) 的线性系统并解
for trial in range(6):
    l11 = F(rng.randint(-9, 9), rng.randint(1, 7))
    u = [pv(L0A)[j] - l11 * pv(L0)[j] for j in range(d)]
    if all(x == 0 for x in u):
        print(f"λ11={l11}: u=0，跳过（走别的分支）")
        continue
    pw = u[:]
    nv = n + 2
    rows, rhs = [], []
    for j in range(d):                      # (I): π(w) = pw
        rows.append([NA[i][j] for i in range(n)] + [F(0), F(0)])
        rhs.append([pw[j]])
    ANA = mm(Ac, NA)                        # n × d
    pL0 = pv(L0)
    for j in range(d):                      # (II): π(wA) − λ21 π(L0) − λ22 pw = 0
        r = [ANA[i][j] for i in range(n)] + [F(0), F(0)]
        r[n] = -pL0[j]
        r[n + 1] = -pw[j]
        rows.append(r); rhs.append([F(0)])
    sol = solve(rows, rhs)
    if sol is None:
        print(f"λ11={l11}: (I)∧(II) 无解")
        continue
    x = sol[0]
    w = [x[i] for i in range(n)]
    l21, l22 = x[n], x[n + 1]
    # ---- 手工核对 ----
    r1 = [L0A[i] - l11 * L0[i] - 1 * w[i] for i in range(n)]          # 第 1 行残差（λ12=1）
    wA = mm([w], Ac)[0]
    r2 = [wA[i] - l21 * L0[i] - l22 * w[i] for i in range(n)]          # 第 2 行残差
    in1 = (rk(W + [r1]) == rkW)
    in2 = (rk(W + [r2]) == rkW)
    okA = (rk(mm(Lc + [w], Ac) + Lc + [w] + W) == rk(Lc + [w] + W))
    print(f"λ11={l11} λ21={l21} λ22={l22}")
    print(f"   第1行残差 ∈ row(C,CA)? {in1}    第2行残差 ∈ row(C,CA)? {in2}")
    print(f"   精确检验 (A): {okA}")
    if not (in1 and in2):
        print("   ⟹ 说明 solve 给出的解**并不满足** (I)/(II) —— 实现的 bug")
    elif not okA:
        print("   ⟹ 残差都在 row(C,CA) 里但 (A) 检验失败 —— satisfies_A 的 bug")
    else:
        print("   ⟹ 找到一个可行的 2 行增广！")
    break
