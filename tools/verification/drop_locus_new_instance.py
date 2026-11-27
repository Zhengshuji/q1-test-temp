"""drop_locus_new_instance.py —— 证明新实例（attempts/63）在 q=3 阶**处处**谱失败（跌落 locus 为空）

用 B.13c 的形式：失败 $\\iff\\exists x\\in V\\setminus\\mathcal Z,\\ \\lambda:\\ (\\lambda I-A)x\\in\\mathcal Z$。

因为 $\\dim V=2$、$\\dim\\mathcal Z=1$（$\\mathcal Z=\\langle z(\\theta)\\rangle$），
令 $M(\\theta,\\lambda)=(I-P_z)(\\lambda I-A)V$（$6\\times2$，$P_z$ 为到 $z$ 的投影），则
$$\\exists x\\in V\\setminus\\{0\\}:\\ (\\lambda I-A)x\\in\\langle z\\rangle\\ \\iff\\ \\operatorname{rank}M(\\theta,\\lambda)\\le1,$$
即 $M$ 的 15 个 $2\\times2$ 子式全为零。再核验 $V\\cap K=0$（于是 $x\\notin\\mathcal Z$ 自动）。

**关键**：把子式看成 $\\mathbb Q(\\theta)[\\lambda]$ 的元素，求 gcd。若 gcd 是 $\\lambda$ 的**一次**多项式
$$g=a(\\theta)\\lambda+b(\\theta),\\qquad a\\not\\equiv0,$$
且在 $\\lambda=-b/a$ 处**全部**子式的分子恒为零，则对每个使 $a(\\theta)\\neq0$ 的 $\\theta$ 都存在共同根 ⟹ 该阶普遍失败。
$a(\\theta)=0$ 的有限个 $\\theta$ 单独核验。

用法：python -u tools/verification/drop_locus_new_instance.py
"""

import os
import sys
import itertools
from fractions import Fraction

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import sympy as sp                        # noqa: E402
import linalg_q as LQ                     # noqa: E402
import z_generator as ZG                  # noqa: E402
import decide_symbolic as DS              # noqa: E402
import toeplitz_criterion as TC           # noqa: E402

F = Fraction
th, lam = sp.symbols('theta lam')

A = [[F(2), F(1), F(2), F(-1), F(2), F(-1)],
     [F(2), F(-2), F(1), F(-2), F(1), F(1)],
     [F(12), F(-8), F(-1), F(0), F(1), F(-1)],
     [F(6), F(-4), F(-2), F(2), F(2), F(-1)],
     [F(-2), F(1), F(0), F(2), F(1), F(2)],
     [F(1), F(-1), F(0), F(1), F(0), F(-1)]]
C = [[F(0), F(0), F(0), F(1), F(2), F(-2)],
     [F(0), F(0), F(-1), F(1), F(-2), F(2)]]
L0 = [[F(-6), F(9), F(8), F(-11), F(-2), F(-28)],
      [F(7), F(-8), F(-4), F(11), F(25), F(20)]]
n, p, r, q = 6, 2, 2, 3


def sym(M):
    return sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in M])


def z_symbolic(rows):
    """图卡给出的 z(θ)（n×1）：Z = K·W，W 在 rows 处置 1，其余位置为 θ。"""
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    Ksym = sym(Kc)
    d = 1
    W = sp.zeros(d, k)
    rest = [i for i in range(k) if i not in rows]
    for a, r0 in enumerate(rows):
        W[a, r0] = 1
    for c in rest:
        W[0, c] = th
    return Ksym * W.T


def check_chart(rows):
    As = sym(A)
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    Vs = sym(V)                                    # 6 × 2
    z = z_symbolic(rows)                           # 6 × 1
    # 投影 P = z zᵀ / (zᵀz)
    ztz = sp.simplify((z.T * z)[0, 0])
    P = z * z.T / ztz
    M = sp.expand((sp.eye(n) - P) * (lam * sp.eye(n) - As) * Vs)   # 6 × 2
    M = sp.Matrix([[sp.simplify(sp.together(M[i, j])) for j in range(2)] for i in range(n)])
    # 15 个 2×2 子式
    mins = []
    for rs in itertools.combinations(range(n), 2):
        m = sp.simplify(sp.together(M[list(rs), :].det()))
        num = sp.numer(sp.cancel(m))
        num = sp.expand(num)
        if num != 0:
            mins.append(num)
    Kfield = sp.QQ.frac_field(th)
    polys = []
    for m in mins:
        try:
            polys.append(sp.Poly(sp.cancel(sp.expand(m)), lam, domain=Kfield))
        except Exception:
            polys.append(None)
    polys = [x for x in polys if x is not None]
    if not polys:
        return None
    g = polys[0]
    for pp in polys[1:]:
        g = g.gcd(pp)
    deg = sp.degree(g.as_expr(), lam)
    out = {'rows': rows, 'nminors': len(mins), 'gcd_deg': deg}
    if deg == 0:
        return out
    co = sp.Poly(g.as_expr(), lam, domain=Kfield).all_coeffs()
    a_, b_ = co[0], co[-1]
    r = sp.simplify(-b_ / a_)
    out['root'] = sp.simplify(r)
    # 全部子式在 λ=r 处为零？（分子恒零）
    ok = True
    bad = None
    for m in mins:
        val = sp.simplify(sp.numer(sp.cancel(sp.together(m.subs(lam, r)))))
        if sp.simplify(val) != 0:
            ok = False
            bad = val
            break
    out['all_zero_at_root'] = ok
    if not ok:
        out['bad'] = bad
    # a(θ) 是否恒非零
    a_num = sp.numer(sp.cancel(a_)) if a_ is not None else None
    out['a_num'] = sp.expand(a_num) if a_num is not None else None
    out['a_identically_zero'] = (a_num is not None and sp.expand(a_num) == 0)
    return out


def main():
    print('=== 新实例（attempts/63）：q=3 的两张图卡 ===')
    # V ∩ K 的维数（决定 x∉Z 是否自动）
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)])
    VK = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A)] + [list(x) for x in L0])
    dV = len(V[0]) if (V and V[0]) else 0
    dVK = len(VK[0]) if (VK and VK[0]) else 0
    print(f'dim V = {dV}；dim(V∩K) = {dVK}（若为 0 则 x∉Z 自动）')
    for rows in [(0,), (1,)]:
        out = check_chart(rows)
        if out is None:
            print(f'  图卡 {rows}：构造失败')
            continue
        print(f'  图卡 {rows}：{out["nminors"]} 个非零子式；gcd 次数 = {out["gcd_deg"]}')
        if out['gcd_deg'] > 0:
            print(f'    共同根 r(θ) = {out["root"]}')
            print(f'    全部子式在 λ=r(θ) 处恒零：{out["all_zero_at_root"]}')
            print(f'    a(θ) 恒为零：{out["a_identically_zero"]}；a(θ) 的分子 = {out["a_num"]}')
    # 精确逐 θ 核验（θ 为整数 -8..8，两图卡）
    bad = []
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    for rows in [(0,), (1,)]:
        for t in range(-8, 9):
            Z = DS.Z_from_theta(A, C, L0, q, rows, [F(t)])
            if ZG.bool_rank(ZG.cols_to_rows(Z)) != 1:
                continue
            L = ZG.L_from_Z(A, C, L0, Z, q)
            if L is None or not LQ.condA(A, C, L):
                continue
            if TC.analyse(A, C, L)['five_b']:
                bad.append((rows, t))
    print(f'\n逐 θ 精确核验（θ=-8..8，两图卡）：可行点 = {bad if bad else "无"}')


if __name__ == '__main__':
    main()
