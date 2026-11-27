# -*- coding: utf-8 -*-
"""
验证 T12：
  情形 II 且 k=1 时，若 π(L0·A) ∦ π(L0)，则**不存在**满足 T5a ∧ (A) 的 L
  ⟹ 由 T6，(S) 必失败 ⟹ 判定恒 NO（多项式可判，chart-free）

验证方法：对每个实例
  · 判 rank[π(L0); π(L0A)] 是 1（平行）还是 2（不平行）
  · 随机造大量含 L0 的 (k+1) 行 L，统计其中 rank(L·N_CA) < q0 的个数
  · 预期：不平行 ⟹ 恒为 0；平行 ⟹ 可能有 >0
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


rng = random.Random(556677)
print("验证 T12：π(L0A) ∦ π(L0)  ⟹  不存在满足 T5a ∧ (A) 的 L")
print()
print(f"{'#':>2} {'q0':>3} {'k':>2} {'d_CA':>4} {'r[πL0;πL0A]':>11} {'πL0=0?':>7} | "
      f"{'断言':>10} | {'含(A)的样本':>10} {'其中秩降':>8} {'符合?':>6}")
print("-" * 96)
shown = 0
bad = 0
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
    W = Cc + mm(Cc, Ac)                       # [C; CA]
    NCA = ker_basis(W)
    dCA = len(NCA[0])
    L0 = Lc[0]; L0A = mm(Lc, Ac)[0]

    def pv(v):
        return [sum(v[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]

    pL0 = pv(L0); pL0A = pv(L0A)
    pL0_zero = all(x == 0 for x in pL0)
    rpar = rk([pL0, pL0A]) if not pL0_zero else 1
    par = (rpar == 1)
    # 随机造含 L0 的 q0 行 L，只保留满足 (A) 的
    nA = 0; nlt = 0
    for _ in range(200):
        rows = Lc[:]
        for _i in range(k):
            rows.append([F(rng.randint(-4, 4)) for _ in range(n)])
        L = rows
        if rk(mm(L, Ac) + L + W) != rk(L + W):     # 不含 (A)，跳过
            continue
        nA += 1
        H = mm(L, NCA)
        if rk(H) < q0:
            nlt += 1
    shown += 1
    # 断言：不平行 且 πL0≠0 ⟹ 秩降数应为 0
    if (not par) and (not pL0_zero):
        expect_zero = True
    else:
        expect_zero = None                     # 不设断言
    ok = (expect_zero is None) or ((nlt == 0) == expect_zero)
    if not ok: bad += 1
    print(f"{shown:>2} {q0:>3} {k:>2} {dCA:>4} {rpar:>11} {str(pL0_zero):>7} | "
          f"{('秩降应为0' if expect_zero else '不设断言'):>10} | "
          f"{nA:>10} {nlt:>8} {str(ok):>6}")

print()
print(f"=== 不符合数：{bad} ===")
print()
print("判读：")
print("  · 全部符合 ⟹ T12 成立（不平行 ⟹ 无秩降 ⟹ (S) 必失败 ⟹ 判定恒 NO）")
print("  · 出现不符合 ⟹ T12 有误，需撤回")
