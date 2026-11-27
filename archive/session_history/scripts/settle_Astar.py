# -*- coding: utf-8 -*-
"""
定论猜想 A*：情形 II ∧ 平行 ⟹ 判定恒 YES？

改进点（相对 taskA_conjecture.py）：
  ① 全程使用带维数断言的 MM（第 13 处教训）
  ② **在 (I)∧(II) 的整个解空间内采样**（不只是特解；相对 find_parallel 的做法）
  ③ λ11 网格扩大（p/q, |p|≤40, q≤16 ⟹ ~1300 点）
"""
import random
from fractions import Fraction as F

srcS = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\reliable_S_test.py",
            encoding="utf-8").read()
headS = srcS.split("# ---------- 主实验 ----------")[0]
exec(headS)


def MM(X, Y):
    assert X and Y, "空矩阵"
    assert len(X[0]) == len(Y), f"维数错配: {len(X)}x{len(X[0])} 乘 {len(Y)}x{len(Y[0])}"
    return mm(X, Y)


def matpow(M, k):
    n = len(M)
    R = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = MM(R, M)
    return R


def solve_space(Ac, Cc, Lc, l11):
    """返回 (特解 y, 零空间 ns)（未知量 = [w(n), λ21, λ22]）"""
    n = len(Ac)
    L0 = Lc[0]
    L0A = MM(Lc, Ac)[0]
    W = Cc + MM(Cc, Ac)
    NA = ker_basis(W)
    d = len(NA[0])

    def pv(v):
        assert len(v) == n
        return [sum(v[i] * NA[i][j] for i in range(n)) for j in range(d)]

    pL0, pL0A = pv(L0), pv(L0A)
    pw = [pL0A[j] - l11 * pL0[j] for j in range(d)]
    ANA = MM(Ac, NA)
    rows, rhs = [], []
    for j in range(d):
        rows.append([NA[i][j] for i in range(n)] + [F(0), F(0)])
        rhs.append([pw[j]])
    for j in range(d):
        r = [ANA[i][j] for i in range(n)] + [F(0), F(0)]
        r[n] = -pL0[j]
        r[n + 1] = -pw[j]
        rows.append(r); rhs.append([F(0)])
    return solve(rows, rhs), NA, W, n


def search(Ac, Cc, Lc, q0, nlam=1300, nsamp=40, seed=1):
    """找 (A)∧秩降∧(S) 见证；返回 (w, found_A, found_S)"""
    n = len(Ac)
    rng = random.Random(seed)
    lams = []
    for q in range(1, 17):
        for pnum in range(-40, 41):
            lams.append(F(pnum, q))
    if len(lams) > nlam:
        lams = rng.sample(lams, nlam)
    foundA = None
    for l11 in lams:
        res, NA, W, _ = solve_space(Ac, Cc, Lc, l11)
        if res is None:
            continue
        y, ns = res
        # 在解空间内采样
        for _ in range(nsamp):
            x = y[:]
            for v in ns:
                c = F(rng.randint(-3, 3))
                x = [x[i] + c * v[i] for i in range(n + 2)]
            w = x[:n]
            if all(t == 0 for t in w):
                continue
            try:
                Ln = Lc + [w]
                if rk(MM(Ln, Ac) + Ln + W) != rk(Ln + W):      # (A)?
                    continue
                H = MM(Ln, NA)
                if not H or not H[0]:
                    continue
                if rk(H) >= q0:                                 # 需秩降
                    continue
                Fm = MM(MM(Ln, Ac), NA)
                foundA = w
                if S_holds(H, Fm):
                    return w, True, True
            except AssertionError:
                continue
    return foundA, (foundA is not None), False


rng = random.Random(55661122)
print("定论 A*：情形 II ∧ 平行，大网格 + 解空间采样")
print()
print(f"{'#':>2} {'n':>2} {'r':>2} {'q0':>3} {'k':>2} {'d_CA':>4} | "
      f"{'λ11 试数':>8} {'(A)∧秩降':>9} {'(S)':>6} {'结论':>22}")
print("-" * 84)
shown = 0
yes = 0
for t in range(200000):
    if shown >= 6:
        break
    n = rng.randint(5, 6); p = 1; r = 2
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
    w, fa, fs = search(Ac, Cc, Lc, q0, nlam=400, nsamp=25, seed=7 * t + 1)
    shown += 1
    if fs: yes += 1
    print(f"{shown:>2} {n:>2} {r:>2} {q0:>3} {k:>2} {dCA:>4} | "
          f"{400:>8} {('是' if fa else '否'):>9} {str(fs):>6} "
          f"{('**YES**' if fs else ('有(A)∧秩降, (S)失败' if fa else '未找到')):>22}")

print()
print(f"=== 找到 (A)∧(S) 见证：{yes} / {shown} ===")
print()
print("判读：")
print("  · 有 YES ⟹ A* 得支持（平行区不可判 NO）⟹ 硬度证据减弱")
print("  · 有『(A)∧秩降 但 (S) 失败』⟹ 该实例是**真正的 NO 候选** ⟹ 值得进一步严格化")
print("  · 全『未找到』⟹ 搜索仍不彻底，需换方法")
