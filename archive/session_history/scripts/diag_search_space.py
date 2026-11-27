# -*- coding: utf-8 -*-
"""
诊断：p1 给出的 Lx 的额外行 w = Lx[-1]，是否满足 (I)∧(II)（即是否在搜索空间内）？
若不在 ⟹ 我的 (I)∧(II) 表述不完备
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


rng = random.Random(97531)
found = None
for t in range(200000):
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
    NCA = ker_basis(W)
    dCA = n - rk(W)
    if dCA < q0: continue
    L0 = Lc[0]
    L0A = MM(Lc, Ac)[0]
    pL0 = [sum(L0[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]
    pL0A = [sum(L0A[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]
    if rk([pL0, pL0A]) != 1: continue
    found = (Ac, Cc, Lc, Lx, eta, W, NCA, dCA, q0, k, pL0, pL0A)
    break

if found is None:
    print("没找到平行实例")
else:
    Ac, Cc, Lc, Lx, eta, W, NCA, dCA, q0, k, pL0, pL0A = found
    n = len(Ac); r = len(Lc)
    print(f"实例：n={n} r={r} eta={eta} q0={q0} k={k} d_CA={dCA}")
    print()
    print("Lx 的前 r 行 == L0 ?", Lx[:r] == Lc)
    w = Lx[-1]
    Ln = Lc + [w]
    print("(A) 对 Lx 成立 ?", rk(MM(Lx, Ac) + Lx + W) == rk(Lx + W))
    print("(A) 对 [L0;w] 成立 ?", rk(MM(Ln, Ac) + Ln + W) == rk(Ln + W))
    H = MM(Lx, NCA)
    print(f"rank(Lx·N_CA) = {rk(H)}  (q0 = {q0})")
    print()

    def pv(v):
        return [sum(v[i] * NCA[i][j] for i in range(n)) for j in range(dCA)]

    pL0_ = pv(Lc[0]); pL0A_ = pv(MM(Lc, Ac)[0]); pw = pv(w)
    print("π(L0)   =", [str(x) for x in pL0_])
    print("π(L0A)  =", [str(x) for x in pL0A_])
    print("π(w)    =", [str(x) for x in pw])
    # 检查 (I)：∃λ11,λ12: π(L0A) − λ11 π(L0) = λ12 π(w)
    # 即 [π(L0), π(w)] 的线性组合能否表示 π(L0A)
    M = [[pL0_[j], pw[j]] for j in range(dCA)]
    print()
    print("π(L0A) ∈ span(π(L0), π(w)) ?",
          rk(M) == rk([row[:] for row in M] ) and
          (lambda: (lambda s: s is not None)(solve([M[j] + [pL0A_[j]] for j in range(dCA)],
                                                   [[F(0)] for _ in range(dCA)])))())
    solI = solve([M[j] + [pL0A_[j]] for j in range(dCA)], [[F(0)] for _ in range(dCA)])
    print("  (I) 可解 ?", solI is not None, solI[0] if solI else "")
    # 检查 (II)：π(w·A) ∈ span(π(L0), π(w))
    wA = MM([w], Ac)[0]
    pwA = pv(wA)
    M2 = [[pL0_[j], pw[j]] for j in range(dCA)]
    solII = solve([M2[j] + [pwA[j]] for j in range(dCA)], [[F(0)] for _ in range(dCA)])
    print("  (II) 可解 ?", solII is not None, solII[0] if solII else "")
    print()
    print("π(w) ∥ π(L0) ?", rk([pL0_, pw]) == 1)
