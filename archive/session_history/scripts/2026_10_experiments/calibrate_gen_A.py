# -*- coding: utf-8 -*-
"""
A 的校准：从 p1 给出的 Lx 反解 Λ*（线性方程组），再用 Λ* 的后 k 列驱动通用构造器

反解：  Lx·A = Λ·Lx + G0·C + G1·CA       （Lx 已知 ⟹ 对 (Λ,G0,G1) 线性 ✓）
校验：  取 ℓ* = Λ* 的后 k 列，跑通用构造器 ⟹ **应能找回一个 (A)-可行解** ✓
"""
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\exact_count_thm7.py",
           encoding="utf-8").read()
head = src.split("rng = random.Random")[0]
exec(head)
gen = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\gen_A_system.py",
           encoding="utf-8").read()
gh = gen.split('if __name__ == "__main__":')[0]
gh = gh.split("import random")[1].split("def MM", 1)[1]
exec("def MM" + gh)


def matpow(M, k):
    n = len(M)
    R = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = MM(R, M)
    return R


def extract_Lambda(Ac, Cc, Lx):
    """解 Lx·A = Λ·Lx + G0·C + G1·CA，返回 Λ (q0×q0)"""
    q0, n = len(Lx), len(Ac)
    p = len(Cc)
    CA = MM(Cc, Ac)
    LxA = MM(Lx, Ac)
    # 未知量 x = [ Λ (q0*q0) , G0 (q0*p) , G1 (q0*n) ]
    nLam = q0 * q0; nG0 = q0 * p; nG1 = q0 * p   # CA 是 p × n
    nv = nLam + nG0 + nG1
    rows, rhs = [], []
    for a in range(q0):            # 行 a
        for c in range(n):         # 列 c
            row = [F(0)] * nv
            for j in range(q0):    # Λ[a][j] · Lx[j][c]
                row[a * q0 + j] += Lx[j][c]
            for b in range(p):     # G0[a][b] · C[b][c]
                row[nLam + a * p + b] += Cc[b][c]
            for b in range(p):     # G1[a][b] · CA[b][c]
                row[nLam + nG0 + a * p + b] += CA[b][c]
            rows.append(row); rhs.append([LxA[a][c]])
    sol = solve(rows, rhs)
    if sol is None:
        return None
    x = sol[0]
    return [[x[a * q0 + j] for j in range(q0)] for a in range(q0)]


rng = random.Random(13572468)
print("A 的校准：反解 Λ* ⟹ 用 ℓ* 驱动通用构造器 ⟹ 应找回 (A)-可行解")
print()
print(f"{'#':>2} {'q0':>3} {'k':>2} {'d_CA':>4} | {'反解 Λ*':>8} {'ℓ*':>16} | "
      f"{'构造器可解?':>11} {'(A) 精确':>9} | {'结论':>14}")
print("-" * 96)
shown = 0
ok_cnt = 0
for t in range(200000):
    if shown >= 6:
        break
    n, p, r, m = 5, 1, 1, 2
    Amat = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
    Cmat = [[rng.randint(-2, 2) for _ in range(n)]]
    Ac, Cc = toF(Amat), toF(Cmat)
    if rk(Cc) != p: continue
    Lc = MM(Cc, matpow(Ac, m))
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
    if k < 1: continue
    W = Cc + MM(Cc, Ac); dCA = n - rk(W)
    Lam = extract_Lambda(Ac, Cc, Lx)
    shown += 1
    if Lam is None:
        print(f"{shown:>2} {q0:>3} {k:>2} {dCA:>4} | {'失败':>8} {'—':>16} | "
              f"{'—':>11} {'—':>9} | {'反解失败':>14}")
        continue
    ell = [[Lam[i][r + a] for a in range(k)] for i in range(q0)]      # Λ 的后 k 列
    rows, rhs, nv, meta = build_general(Ac, Cc, Lc, ell)
    sol = solve(rows, rhs)
    n_, r_, k_, q0_, d_, N_, W_ = meta
    got = False
    if sol is not None:
        for cand in [sol[0]] + list(sol[1])[:0]:
            R = [[cand[a * n_ + j] for j in range(n_)] for a in range(k_)]
            Lnew = [row[:] for row in Lc] + R
            if check_A_raw(Ac, Cc, Lnew):
                got = True
                break
    if got: ok_cnt += 1
    el_s = "[" + ",".join(str(x) for a in range(k) for x in [ell[i][a] for i in range(q0)]) + "]"
    print(f"{shown:>2} {q0:>3} {k:>2} {dCA:>4} | {'成功':>8} {el_s[:16]:>16} | "
          f"{str(sol is not None):>11} {str(got):>9} | "
          f"{('**校准通过**' if got else '未找回'):>14}")

print()
print(f"=== 校准通过：{ok_cnt} / {shown} ===")
print()
print("判读：")
print("  · 通过 ⟹ 通用构造器正确 ⟹ 可上 q0=3")
print("  · 未通过 ⟹ 构造器或反解仍有错，须继续查")
