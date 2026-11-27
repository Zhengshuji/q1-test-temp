# -*- coding: utf-8 -*-
"""
严格判定任务 A 的靶子：平行 ∧ 情形 II 的实例是否存在秩降的 (A)-可行解？

(A) ⟺ ∃Λ: L·A = Λ L + G0 C + G1 CA，其中 L=[L0;w]（k=1），
投影形式（π = 到 row[C;CA]^⊥）：
   (I)  π(L0A) − λ11 π(L0) = λ12 π(w)
   (II) π(wA) − λ21 π(L0) − λ22 π(w) = 0
T5a（= 有秩降）⟺ π(L0)=0 或 π(w) ∥ π(L0)

分两支（λ12 归一）：
  分支1 (λ12=1)：需扫 λ11（相容性是 λ11 的多项式条件）
  分支2 (λ12=0)：λ11 = λ* 被强制；π(w) 自由 ⟹ 加上 T5a ⟹ **单一线性系统**
       未知量 w(n), t, mu   （mu := λ21 + λ22·t 消去双线性）
       方程   π(w) = t·π(L0)            （d 个，T5a）
              π(wA) = mu·π(L0)          （d 个，(II)）
       —— 无 λ11 参数 ⟹ **可直接、严格判定** ✓
"""
import random
from fractions import Fraction as F

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


def branch2(Ac, Cc, Lc, W, NCA, verbose=False):
    """
    分支 λ12=0：解线性系统
      未知量 x = [w(0..n-1), t, mu]
      π(w)   − t·π(L0)      = 0
      π(wA)  − mu·π(L0)     = 0
    返回 w 或 None
    """
    n = len(Ac)
    d = len(NCA[0])
    L0 = Lc[0]
    L0A = MM(Lc, Ac)[0]

    def pv(v):
        assert len(v) == n
        return [sum(v[i] * NCA[i][j] for i in range(n)) for j in range(d)]

    pL0 = pv(L0)
    ANA = MM(Ac, NCA)                 # n × d : π(wA) = w·(A NCA)
    nv = n + 2
    rows, rhs = [], []
    for j in range(d):                # π(w) = t π(L0)
        r = [F(0)] * nv
        for i in range(n):
            r[i] = NCA[i][j]
        r[n] = -pL0[j]                # t
        rows.append(r); rhs.append([F(0)])
    for j in range(d):                # π(wA) = mu π(L0)
        r = [F(0)] * nv
        for i in range(n):
            r[i] = ANA[i][j]
        r[n + 1] = -pL0[j]            # mu
        rows.append(r); rhs.append([F(0)])
    sol = solve(rows, rhs)
    if sol is None:
        return None
    y, ns = sol
    # 解空间里找一个非零 w
    for v in [y] + list(ns):
        w = [v[i] for i in range(n)]
        if all(t == 0 for t in w):
            continue
        if rk(MM(Lc + [w], Ac) + Lc + [w] + W) == rk(Lc + [w] + W):
            return w
    return None


rng = random.Random(11223344)
print("严格判定：平行 ∧ 情形 II 的实例，分支 λ12=0 是否存在秩降解")
print()
print(f"{'#':>2} {'n':>2} {'r':>2} {'q0':>3} {'k':>2} {'d_CA':>4} | "
      f"{'λ*':>6} | {'分支2 解':>8} {'(A)':>5} {'秩降':>5} {'(S)':>7} | {'结论':>18}")
print("-" * 92)
shown = 0
for t in range(200000):
    if shown >= 8:
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
    if rk([pL0, pL0A]) != 1: continue          # 只要平行
    # λ*
    lam = None
    for j in range(dCA):
        if pL0[j] != 0:
            lam = pL0A[j] / pL0[j]; break
    w = branch2(Ac, Cc, Lc, W, NCA)
    shown += 1
    if w is None:
        print(f"{shown:>2} {n:>2} {r:>2} {q0:>3} {k:>2} {dCA:>4} | {str(lam):>6} | "
              f"{'无':>8} {'—':>5} {'—':>5} {'—':>7} | {'分支2 无秩降解':>18}")
        continue
    Ln = Lc + [w]
    okA = rk(MM(Ln, Ac) + Ln + W) == rk(Ln + W)
    H = MM(Ln, NCA)
    rd = (rk(H) < q0)
    Fm = MM(MM(Ln, Ac), NCA)
    okS = S_holds(H, Fm) if rd else False
    print(f"{shown:>2} {n:>2} {r:>2} {q0:>3} {k:>2} {dCA:>4} | {str(lam):>6} | "
          f"{'有':>8} {str(okA):>5} {str(rd):>5} {str(okS):>7} | "
          f"{('**YES！**' if okS else '有解但(S)失败'):>18}")

print()
print("判读：")
print("  · 出现 YES ⟹ 该实例判定为 YES（严格，因分支2 是单一线性系统）")
print("  · 分支2 无解 ⟹ 需再看分支1（λ12=1，需插值）")
