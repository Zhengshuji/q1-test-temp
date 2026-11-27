"""verify_prefilter_733_638.py

对 638 与 733 两个实例计算 744 的预筛选量，并计算 Bézout 秩。
纯精确算术（sympy 有理数/根式），不含浮点。

注意：638 的 G 不能取 0——$(5a)$ 要求 $H_A=ZH$ 的行在 $U$ 内，
脚本显式构造满足该约束的 $Z$，并断言 $G=ZH-HZ'$ 的行在 $T$。

用法：python verify_prefilter_733_638.py
"""

import itertools

import sympy as sp

lam = sp.symbols('lam')


def minors_and_rank_M(H, Z, d):
    """P(lambda)=lam*H - Z*H；返回非零 d-子式列表与 Bezout 矩阵的秩。"""
    P = lam * H - Z * H
    rows = list(range(H.rows))
    ms = []
    for comb in itertools.combinations(rows, d):
        Msub = P.extract(list(comb), list(range(P.cols)))
        if Msub.cols >= d:
            for cols in itertools.combinations(range(Msub.cols), d):
                f = sp.expand(Msub.extract(list(range(d)), list(cols)).det())
                if f != 0:
                    ms.append(f)
    if not ms:
        return ms, 0
    m = len(ms)
    M = sp.zeros(2 * d, m * d)
    for i, f in enumerate(ms):
        cs = sp.Poly(f, lam).all_coeffs()[::-1]
        for s, c in enumerate(cs):
            for t in range(d):
                if s + t < 2 * d:
                    M[s + t, i * d + t] += c
    return ms, M.rank()


def cls_rank(H, Zp, mu, T):
    M = mu * sp.eye(Zp.rows) - Zp
    HM = H * M
    U = H.rowspace()
    dU = len(U)
    B = sp.Matrix.vstack(*([r for r in U] + [T.row(i) for i in range(T.rows)]))
    dUT = B.rank()
    dV = dU + T.rows - dUT
    if HM.rank() == 0:
        cls = 0
    else:
        cls = sp.Matrix.vstack(*([r for r in HM.rowspace()] + U)).rank() - dU
    return HM.rank(), dV, cls


def rows_in_U(H, Z):
    U = H.rowspace()
    dU = len(U)
    ZH = Z * H
    ok = True
    for i in range(ZH.rows):
        aug = sp.Matrix.vstack(*U, ZH.row(i))
        ok = ok and (aug.rank() == dU)
    return ok


def g_rows_in_T(G, T):
    # T 由 e1 张成时：G 的每行第二列之后全为 0
    return all(all(sp.simplify(G[i, j]) == 0 for j in range(1, G.cols)) for i in range(G.rows))


def report(name, H, Zp, Z, T, mu, d):
    R, dV, cls = cls_rank(H, Zp, mu, T)
    G = Z * H - H * Zp
    ms, rM = minors_and_rank_M(H, Z, d)
    print(f"== {name} ==")
    print("  d'=", d, " rank(HM)=", R, " dim(U∩T)=", dV, " cls=", cls,
          " R+dV+cls=", R + dV + cls)
    print("  #minors=", len(ms), " rank M=", rM, " bound(2d)=", 2 * d)
    if ms:
        print("  gcd(minors)=", sp.factor(sp.gcd_list(ms)))
    print("  ZH rows in U:", rows_in_U(H, Z), " G rows in T:", g_rows_in_T(G, T))
    print()


# ---- 638: k=3, Z' 3-cycle, H rows e2,e3, T=e1
Zp638 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
H638 = sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
T638 = sp.Matrix([[1, 0, 0]])
# 由 (5a): Z_iH ∈ U 且 Z_iH - H_iZ' ∈ T；解得 ZH 的行为 0, e3, 0
Z638 = sp.Matrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
report("638", H638, Zp638, Z638, T638, sp.Integer(1), 2)

# ---- 733
H733 = sp.Matrix([[2, 2], [-1, -1], [2, 1]])
Zp733 = sp.Matrix([[1, 2], [1, 1]])
Z733 = sp.Matrix([[4, -3, -5], [-2, -3, -2], [sp.Rational(7, 2), -3, -5]])
T733 = sp.Matrix([[1, 0]])
report("733", H733, Zp733, Z733, T733, 1 + sp.sqrt(2), 2)
