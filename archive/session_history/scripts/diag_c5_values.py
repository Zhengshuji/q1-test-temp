# -*- coding: utf-8 -*-
"""最小诊断：打印 w、π(w)、u(λ)、π(wA)、c·π(L0)，核对 π-等式与 (A)"""
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\exact_count_thm7.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random")[0]
exec(head)


def MM(X, Y):
    assert X and Y and len(X[0]) == len(Y), "维数错配"
    return mm(X, Y)


def matpow(M, k):
    n = len(M)
    R = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = MM(R, M)
    return R


rng = random.Random(777001)
inst = None
for t in range(300000):
    n, p, r = 5, 1, 2
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
    if rk([pL0, pL0A]) != 1: continue
    inst = (Ac, Cc, Lc, W, NCA, dCA, q0, k, pL0, pL0A)
    break

Ac, Cc, Lc, W, NCA, dCA, q0, k, pL0, pL0A = inst
n = len(Ac)
print(f"实例：n={n} r={len(Lc)} q0={q0} k={k} d_CA={dCA}")
print()
print("π(L0)  =", [str(x) for x in pL0])
print("π(L0A) =", [str(x) for x in pL0A])
print("（平行 ⟹ 成比例）")
print()

# --- 按 verify_c5_witness 的方式构造 ---
NT = tr(NCA); G = MM(NT, NCA); Gi = inv(G); P = MM(Gi, NT)


def w0_of(lam):
    u = [pL0A[j] - lam * pL0[j] for j in range(dCA)]
    return MM([u], P)[0]


def pv(v):
    return [sum(v[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]


basis_rows = []
for v in W:
    if rk(basis_rows + [v]) > rk(basis_rows):
        basis_rows.append(v)
Sgens = [pv(MM([b], Ac)[0]) for b in basis_rows]
m = len(Sgens)
print(f"|basis_rows| = {len(basis_rows)},  |Sgens| = {m}")
for i, s in enumerate(Sgens):
    print(f"  π(b_{i}A) =", [str(x) for x in s])
print()

w0_0, w0_1 = w0_of(F(0)), w0_of(F(1))
dw = [w0_1[i] - w0_0[i] for i in range(n)]
pA0 = pv(MM([w0_0], Ac)[0])
pAd = pv(MM([dw], Ac)[0])
print("π(w0(0)A)  =", [str(x) for x in pA0])
print("π(dw·A)    =", [str(x) for x in pAd])
print()

# 系统（修正符号版）：  Σ γ_i s_i + λ pAd − c pL0 = −pA0
nv = 1 + m + 1
rows, rhs = [], []
for j in range(dCA):
    rr = [F(0)] * nv
    rr[0] = pAd[j]
    for i in range(m):
        rr[1 + i] = Sgens[i][j]
    rr[1 + m] = -pL0[j]
    rows.append(rr); rhs.append([-pA0[j]])
sol = solve(rows, rhs)
print("系统相容？", sol is not None)
if sol is None:
    raise SystemExit
z = sol[0]
lam, gammas, c = z[0], z[1:1 + m], z[1 + m]
print("解： λ =", lam, " γ =", [str(x) for x in gammas], " c =", c)
print()

w0 = w0_of(lam)
w = w0[:]
for i in range(m):
    for a in range(n):
        w[a] += gammas[i] * basis_rows[i][a]
print("w =", [str(x) for x in w])
print()
print("核对 ①: π(w) == u(λ) ?")
pw = pv(w)
u = [pL0A[j] - lam * pL0[j] for j in range(dCA)]
print("   π(w) =", [str(x) for x in pw])
print("   u(λ) =", [str(x) for x in u])
print("   相等？", pw == u)
print()
print("核对 ②: π(w·A) == c·π(L0) ?")
pwA = pv(MM([w], Ac)[0])
cL0 = [c * x for x in pL0]
print("   π(wA)   =", [str(x) for x in pwA])
print("   c·π(L0) =", [str(x) for x in cL0])
print("   相等？", pwA == cL0)
print()
Ln = Lc + [w]
okA = rk(MM(Ln, Ac) + Ln + W) == rk(Ln + W)
print("原始 (A) 检验：", okA)
print("  rk[LA;L;C;CA] =", rk(MM(Ln, Ac) + Ln + W),
      " rk[L;C;CA] =", rk(Ln + W))
