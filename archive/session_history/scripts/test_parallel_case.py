# -*- coding: utf-8 -*-
"""
平行情形的检验：
  猜想（T12 的逆）：若 π(L0·A) ∥ π(L0)，则**存在**满足 (A)∧T5a 的 L
  做法：构造线性系统
        π(w)  ∈ span(π(L0))        （d_CA − 1 个线性方程）
        π(w·A) ∈ span(π(L0))       （d_CA − 1 个线性方程）
      （等价于 (A)∧T5a，见推导）
  解出 w 后**精确**验证 (A) 与秩降。
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


def find_parallel(Ac, Cc, Lc, q0, tries=4000, seed=1):
    """在平行情形下寻找满足 (A)∧T5a 的 w"""
    n = len(Ac)
    W = Cc + mm(Cc, Ac)
    NCA = ker_basis(W)
    d = len(NCA[0])
    L0 = Lc[0]; L0A = mm(Lc, Ac)[0]

    def pv(v):
        return [sum(v[i] * NCA[i][j] for i in range(n)) for j in range(d)]

    pL0 = pv(L0)
    rng = random.Random(seed)
    # 线性系统： (I') π(w) = t·π(L0)  —— 消去 t：对所有 i<j，π(w)_i·pL0_j − π(w)_j·pL0_i = 0
    #           (II') π(wA) = t'·π(L0) —— 同理
    ANA = mm(Ac, NCA)
    rows, rhs = [], []
    for i in range(d):
        for j in range(i + 1, d):
            r = [F(0)] * n
            for a in range(n):
                r[a] = NCA[a][i] * pL0[j] - NCA[a][j] * pL0[i]
            rows.append(r + [F(0)]); rhs.append([F(0)])       # w 的系数 + t 的系数(0)
    for i in range(d):
        for j in range(i + 1, d):
            r = [F(0)] * n
            for a in range(n):
                r[a] = ANA[a][i] * pL0[j] - ANA[a][j] * pL0[i]
            rows.append(r + [F(0)]); rhs.append([F(0)])
    if not rows:
        # d_CA = 1：条件自动成立
        for _ in range(tries):
            w = [F(rng.randint(-4, 4)) for _ in range(n)]
            if rk(mm(Lc + [w], Ac) + Lc + [w] + W) == rk(Lc + [w] + W):
                return w
        return None
    sol = solve(rows, rhs)
    if sol is None:
        return None
    y, ns = sol
    # 在解空间里找满足 (A) 的点
    for _ in range(tries):
        w = y[:]
        for v in ns:
            c = F(rng.randint(-3, 3))
            w = [w[i] + c * v[i] for i in range(n)]
        if all(x == 0 for x in w): continue
        L = Lc + [w]
        if rk(mm(L, Ac) + L + W) == rk(L + W):          # (A)
            H = mm(L, NCA)
            if rk(H) < q0:                               # 秩降
                return w
    return None


rng = random.Random(9090909)
print("平行情形检验：π(L0A) ∥ π(L0) 时，是否存在满足 (A)∧T5a 的 L？")
print()
print(f"{'#':>2} {'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'k':>2} {'d_CA':>4} | "
      f"{'r[πL0;πL0A]':>11} | {'找到':>5} {'(A)':>5} {'秩降':>5}")
print("-" * 74)
shown = 0
found_cnt = 0
for t in range(200000):
    if shown >= 8:
        break
    n = rng.randint(4, 6); p = 1; r = rng.randint(1, n - 1)
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
    W = Cc + mm(Cc, Ac)
    dCA = n - rk(W)
    NCA = ker_basis(W)
    if dCA < q0: continue                       # 只要情形 II
    L0 = Lc[0]; L0A = mm(Lc, Ac)[0]
    pL0 = [sum(L0[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]
    pL0A = [sum(L0A[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]
    rpar = rk([pL0, pL0A])
    if rpar != 1: continue                      # 只要平行
    w = find_parallel(Ac, Cc, Lc, q0, tries=3000, seed=100 + t)
    shown += 1
    if w is not None: found_cnt += 1
    print(f"{shown:>2} {n:>2} {p:>2} {r:>2} {q0:>3} {k:>2} {dCA:>4} | {rpar:>11} | "
          f"{('是' if w is not None else '否'):>5} "
          f"{('通过' if w is not None else '—'):>5} "
          f"{('是' if w is not None else '—'):>5}")

print()
print(f"=== 平行实例中找到 (A)∧T5a 的比例：{found_cnt} / {shown} ===")
print()
print("判读：")
print("  · 找到 ⟹ 平行时秩降确实可能 ⟹ 支撑『T12 是充分条件而非必要条件』")
print("  · 找不到 ⟹ 平行也可能不够，需要更强条件")
