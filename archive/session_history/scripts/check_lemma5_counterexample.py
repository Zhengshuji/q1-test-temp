# -*- coding: utf-8 -*-
"""
核验引理 5 的反例：(S) <=> im H 不含 T 的特征向量。
若 rank H = q0（行满秩），则 im H = C^{q0}，故 (S) 必然失败。
本脚本在真实系统数据上核验：
  (i)  (S) <=> im H ∩ ker(λI−T) = 0 对所有 λ
  (ii) 当 rank H = q0 时 (S) 是否恒假
"""
import random
from fractions import Fraction as F

src = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\exact_count_thm7.py",
           encoding="utf-8").read()
exec(src.split("rng = random.Random(112233)")[0])


def rank_H_and_S(A, C, L):
    """返回 (d_CA, rank H, (S) 是否成立)"""
    n = len(A)
    # N_CA = ker[C; CA]
    M = C + mm(C, A)
    NCA = ker_basis(M)
    dCA = len(NCA[0]) if (NCA and NCA[0]) else 0
    H = mm(L, NCA) if dCA > 0 else [[F(0)] for _ in range(len(L))]
    rkH = rk(H) if H and H[0] else 0
    if dCA == 0:
        return 0, 0, True                      # N_CA 为空 => (S) 自动成立
    # (S): rank[λL − LA; CA; C] == rank[CA; C; L]  对所有 λ
    CA = mm(C, A)
    rhs = rk(CA + C + L)
    cand = set()
    try:
        import numpy as np
        ev = np.linalg.eigvals(np.array([[float(x) for x in r] for r in A]))
        for e in ev:
            if abs(e.imag) < 1e-7:
                cand.add(F(float(e.real)).limit_denominator(5000))
    except Exception:
        pass
    for kk in range(-10, 11):
        cand.add(F(kk))
    # T 的特征值（用 H 的广义逆构造不出来，退而用 A 的特征值 + 一批有理数）
    for lam in sorted(cand):
        LL = [[lam * L[i][j] - mm(L, A)[i][j] for j in range(n)] for i in range(len(L))]
        if rk(LL + CA + C) != rhs:
            return dCA, rkH, False
    return dCA, rkH, True


rng = random.Random(918273)
print("核验：(S) 与 rank H = q0 的关系")
print(f"{'n':>2} {'p':>2} {'r':>2} {'q0':>3} | {'d_CA':>4} {'rankH':>5} {'rankH==q0?':>10} | {'(S)':>6}")
print("-" * 62)
cnt_full = 0
cnt_full_S = 0
cnt_part = 0
cnt_part_S = 0
shown = 0
for trial in range(400):
    n = rng.randint(3, 5)
    p = rng.randint(1, n - 1)
    r = rng.randint(1, n - p)
    for _ in range(200):
        Am = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(n)]
        Cm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(p)]
        Lm = [[rng.randint(-2, 2) for _ in range(n)] for _ in range(r)]
        Ac, Cc, Lc = toF(Am), toF(Cm), toF(Lm)
        if rk(Cc) != p or rk(Lc) != r: continue
        if rk(Lc + Cc) != r + p: continue
        Z = orb(Lc, Ac, n) + orb(Cc, Ac, n); OC = orb(Cc, Ac, n)
        if rk(Z + OC) != rk(OC): continue
        try:
            Lx, eta = p1(Ac, Cc, Lc)
        except Exception:
            continue
        if not condA(Ac, Cc, Lx): continue
        q0 = sum(eta)
        dCA, rkH, S = rank_H_and_S(Ac, Cc, Lx)
        if rkH == q0:
            cnt_full += 1
            if S: cnt_full_S += 1
        else:
            cnt_part += 1
            if S: cnt_part_S += 1
        if shown < 14:
            print(f"{n:>2} {p:>2} {r:>2} {q0:>3} | {dCA:>4} {rkH:>5} {str(rkH==q0):>10} | {str(S):>6}")
            shown += 1
        break

print()
print("=== 汇总 ===")
print(f"  rankH == q0 的实例: {cnt_full} 个，其中 (S) 成立 {cnt_full_S} 个")
print(f"  rankH <  q0 的实例: {cnt_part} 个，其中 (S) 成立 {cnt_part_S} 个")
print()
print("预期：rankH == q0 时 im H = C^{q0} => (S) 必假 => 应有 cnt_full_S = 0")
