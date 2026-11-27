"""verify_prefilter_733_638.py

对 638 与 733 两个实例计算 744 的七条预筛选量，并计算 Bézout 秩。
纯精确算术（sympy 有理数/根式），不含浮点。

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
        Msub = P.extract(list(comb), list(range(H.cols)))
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


def report(name, H, Zp, Z, T, mu, d):
    R, dV, cls = cls_rank(H, Zp, mu, T)
    ms, rM = minors_and_rank_M(H, Z, d)
    print(f"== {name} ==")
    print("  d'=", d, " rank(HM)=", R, " dim(U∩T)=", dV, " cls=", cls,
          " R+dV+cls=", R + dV + cls)
    print("  #minors=", len(ms), " rank M=", rM, " bound(2d)=", 2 * d)
    if ms:
        g = sp.gcd_list(ms)
        print("  gcd(minors)=", sp.factor(g))
    print()


# ---- 638: k=3, Z' 3-cycle, H rows e2,e3, T=e1
Zp638 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
H638 = sp.Matrix([[0, 1, 0], [0, 0, 1], [0, 0, 0]])
T638 = sp.Matrix([[1, 0, 0]])
# 638 的 Z 由 709 的证明存在性给出；这里只检验 rank M 与筛选量，取一个满足 ZH=HZ'+G 的 Z 即可
# 用最小二乘/线性求解：每行 z 满足 z H = H_i Z' + g_i（g_i ∈ T）
Z638 = sp.zeros(3, 3)
for i in range(3):
    row = H638.row(i) * Zp638
    # 解 z H = row + g e1
    z = sp.symbols(f'z{i}_0:3')
    g = sp.symbols(f'g{i}')
    eqs = [sp.Eq(sum(z[j] * H638[j, c] for j in range(3)) - g * T638[0, c],
                 row[0, c]) for c in range(3)]
    sol = sp.solve(eqs, list(z) + [g], dict=True)
    if sol:
        s0 = sol[0]
        free = [v for v in list(z) + [g] if v not in s0]
        vals = {v: 0 for v in free}
        for j, vv in enumerate(z):
            Z638[i, j] = sp.simplify(s0.get(vv, vv).subs(vals))

report("638", H638, Zp638, Z638, T638, sp.Integer(1), 2)

# ---- 733
H733 = sp.Matrix([[2, 2], [-1, -1], [2, 1]])
Zp733 = sp.Matrix([[1, 2], [1, 1]])
Z733 = sp.Matrix([[4, -3, -5], [-2, -3, -2], [sp.Rational(7, 2), -3, -5]])
T733 = sp.Matrix([[1, 0]])
report("733", H733, Zp733, Z733, T733, 1 + sp.sqrt(2), 2)
