# -*- coding: utf-8 -*-
"""
任务 A 的第一步（决定性）：检验猜想 A*
    情形 II ∧ 平行  ⟹  判定恒为 YES？

⚠️ 本脚本**全程断言维数匹配**（第 13 处的教训：mm 不检查维数）
⚠️ 可靠 (S) 判据取自 reliable_S_test.py
"""
import random
from fractions import Fraction as F

srcS = open(r"C:\Users\26074\Desktop\工作 学习（待办）\？？？\scripts\core\reliable_S_test.py",
            encoding="utf-8").read()
headS = srcS.split("# ---------- 主实验 ----------")[0]
exec(headS)


def MM(X, Y):
    """带维数断言的矩阵乘法"""
    assert len(X[0]) == len(Y), f"维数错配: {len(X)}x{len(X[0])} 乘 {len(Y)}x{len(Y[0])}"
    return mm(X, Y)


def matpow(M, k):
    n = len(M)
    R = [[F(1) if i == j else F(0) for j in range(n)] for i in range(n)]
    for _ in range(k):
        R = MM(R, M)
    return R


def build_L(Ac, Cc, Lc, l11, pw_is_free=False, pw=None):
    """
    解 (I)∧(II)（投影形式）求额外行 w（k=1）。
    未知量：w(n), λ21, λ22；固定 λ12=1；扫 λ11。
    返回 w 或 None。
    """
    n = len(Ac)
    L0 = Lc[0]
    L0A = MM(Lc, Ac)[0]
    W = Cc + MM(Cc, Ac)                       # [C; CA]
    NA = ker_basis(W)                         # n × d_CA
    d = len(NA[0])

    def pv(v):
        assert len(v) == n
        return [sum(v[i] * NA[i][j] for i in range(n)) for j in range(d)]

    pL0, pL0A = pv(L0), pv(L0A)
    if pw is None:
        pw = [pL0A[j] - l11 * pL0[j] for j in range(d)]
    ANA = MM(Ac, NA)                          # n × d
    rows, rhs = [], []
    for j in range(d):                        # (I): π(w) = pw
        rows.append([NA[i][j] for i in range(n)] + [F(0), F(0)])
        rhs.append([pw[j]])
    for j in range(d):                        # (II): π(wA) − λ21 π(L0) − λ22 pw = 0
        r = [ANA[i][j] for i in range(n)] + [F(0), F(0)]
        r[n] = -pL0[j]
        r[n + 1] = -pw[j]
        rows.append(r); rhs.append([F(0)])
    sol = solve(rows, rhs)
    if sol is None:
        return None
    x = sol[0]
    return [x[i] for i in range(n)]


rng = random.Random(19283746)
print("任务 A 第一步：检验『情形 II ∧ 平行 ⟹ 判定恒 YES』")
print()
print(f"{'#':>2} {'n':>2} {'p':>2} {'r':>2} {'q0':>3} {'k':>2} {'d_CA':>4} | "
      f"{'平行?':>6} | {'试 w 数':>7} {'(A)∧秩降':>9} {'(S) 成立':>8} {'结论':>16}")
print("-" * 96)
shown = 0
yes = 0
for t in range(120000):
    if shown >= 8:
        break
    n = rng.randint(4, 6); p = 1; r = rng.randint(1, n - 2)
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
    if k != 1: continue                        # 只做 k=1（脚本支持）
    W = Cc + MM(Cc, Ac)
    dCA = n - rk(W)
    if dCA < q0: continue                      # 情形 II
    NCA = ker_basis(W)
    L0 = Lc[0]; L0A = MM(Lc, Ac)[0]
    pL0 = [sum(L0[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]
    pL0A = [sum(L0A[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]
    rpar = rk([pL0, pL0A])
    if rpar != 1: continue                     # 只做平行
    # 搜索 (A)∧秩降∧(S) 的 w
    tried = 0; gotA = None; gotS = False
    for q in range(1, 11):
        for pnum in range(-16, 17):
            w = build_L(Ac, Cc, Lc, F(pnum, q))
            if w is None: continue
            tried += 1
            Ln = Lc + [w]
            if rk(MM(Ln, Ac) + Ln + W) != rk(Ln + W):   # (A)
                continue
            H = MM(Ln, NCA)
            if not H or not H[0]: continue
            if rk(H) >= q0: continue                     # 需秩降
            # 由 (A) 得到 Λ，再算 F
            # 这里用可靠 (S) 判据：直接用 (Ln, Ac, NCA) 构造 H、F
            # F = Ln·A·NCA
            Fm = MM(MM(Ln, Ac), NCA)
            gotA = w
            if S_holds(H, Fm):
                gotS = True
                break
        if gotS: break
    shown += 1
    if gotS: yes += 1
    print(f"{shown:>2} {n:>2} {p:>2} {r:>2} {q0:>3} {k:>2} {dCA:>4} | {rpar:>6} | "
          f"{tried:>7} {('是' if gotA else '否'):>9} {str(gotS):>8} "
          f"{('**YES**' if gotS else ('有(A)∧秩降但(S)失败' if gotA else '未找到')):>16}")

print()
print(f"=== 平行 ∧ 情形 II 的实例中，找到 (A)∧(S) 见证的有 {yes} / {shown} ===")
print()
print("判读：")
print("  · 全部 YES ⟹ 猜想 A* 成立 ⟹ 该区域多项式可判（恒 YES）⟹ q 的硬度不在那里")
print("  · 出现 NO ⟹ A* 不成立 ⟹ 该区域确实可能藏硬度 ⟹ 值得做归约")
