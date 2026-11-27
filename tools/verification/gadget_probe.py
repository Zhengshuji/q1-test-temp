"""gadget_probe.py —— 在构造族上做"参数化探针"：把 $A_{00}$ 换成符号 $t$，看跌落 locus 是否出现

**动机**（专家 §D1 的"小 gadget 先试"）：若某个数据参数的变动能**破坏**整族失败，则"在该阶可行"
就是参数空间里的一个非平凡代数条件——这正是把二次方程编码进观测器设计的入口。
反之，若整族失败在参数扰动下**稳定**（跌落 locus 仍为空），说明该失败是"开性质"，
那么可行性判定就只能从别的地方（计数条件）获得难度。

**做法**：把新实例（`proof/type3_second_example/`）的 $A_{00}$ 换成符号 $t$，
对 $q=3$ 的两张图卡重算 $M(t,\\theta,\\lambda)=(I-P_z)(\\lambda I-A(t))V$ 的 15 个 $2\\times2$ 子式，
在 $\\mathbb Q(t,\\theta)[\\lambda]$ 上求 gcd：

* 若 $\\gcd=\\lambda+2$（与 $t,\\theta$ 无关）⟹ 对**一切** $(t,\\theta)$ 都失败 ⟹ 该阶整族失败是**开**性质；
* 若 gcd 依赖 $t$ ⟹ 存在"好"的 $t$（在该阶可行），给出一个由多项式方程定义的可解集 ⟹ 可作为 gadget 的雏形。

用法：python -u tools/verification/gadget_probe.py
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

F = Fraction
t, th, lam = sp.symbols('t theta lam')

A0 = [[F(2), F(1), F(2), F(-1), F(2), F(-1)],
      [F(2), F(-2), F(1), F(-2), F(1), F(1)],
      [F(12), F(-8), F(-1), F(0), F(1), F(-1)],
      [F(6), F(-4), F(-2), F(2), F(2), F(-1)],
      [F(-2), F(1), F(0), F(2), F(1), F(2)],
      [F(1), F(-1), F(0), F(1), F(0), F(-1)]]
C = [[F(0), F(0), F(0), F(1), F(2), F(-2)],
     [F(0), F(0), F(-1), F(1), F(-2), F(2)]]
L0 = [[F(-6), F(9), F(8), F(-11), F(-2), F(-28)],
      [F(7), F(-8), F(-4), F(11), F(25), F(20)]]
n, p, r = 6, 2, 2


def sym(M):
    return sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in M])


def main():
    # V 用原实例（t=2）的 V：注意 V 依赖 A，若 A 随 t 变，V 也变。
    # 为保持"结构不变"，这里固定 V（即假设 V 在 t 附近不变），并在 t=2 处校对结果。
    V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ.mul(C, A0)])
    Vs = sym(V)
    print(f'dim V = {len(V[0])}（固定用 t=2 处的 V）')
    Kc = ZG.ker_cols([list(x) for x in C] + [list(x) for x in L0])
    k = len(Kc[0])
    Ks = sym(Kc)
    for rows in [(0,), (1,)]:
        W = sp.zeros(1, k)
        rest = [i for i in range(k) if i not in rows]
        for a, r0 in enumerate(rows):
            W[a, r0] = 1
        for c in rest:
            W[0, c] = th
        z = Ks * W.T
        ztz = sp.simplify((z.T * z)[0, 0])
        P = z * z.T / ztz
        At = sym(A0)
        At[0, 0] = t
        M = sp.expand((sp.eye(n) - P) * (lam * sp.eye(n) - At) * Vs)
        mins = []
        for rs in itertools.combinations(range(n), 2):
            m = sp.cancel(sp.together(M[list(rs), :].det()))
            num = sp.expand(sp.numer(m))
            if num != 0:
                mins.append(num)
        print(f'\n图卡 {rows}：非零子式 {len(mins)} 个（符号含 t；注意：sympy 在双变量分式域上的 gcd '
              f'不可靠，本节结果为**不可判定**，以数值探针为准）')
        field = sp.QQ.frac_field(t, th)
        polys = []
        for m in mins:
            try:
                polys.append(sp.Poly(sp.cancel(sp.expand(m)), lam, domain=field))
            except Exception as e:
                print('   转多项式失败：', type(e).__name__)
                polys = []
                break
        if not polys:
            continue
        g = polys[0]
        for pp in polys[1:]:
            g = g.gcd(pp)
        ge = sp.factor(sp.cancel(g.as_expr()))
        print(f'   gcd = {ge}')
        deg = sp.degree(sp.cancel(g.as_expr()), lam)
        print(f'   gcd 的 λ-次数 = {deg}（期望 1，且不依赖 t）')
        # 在 t=2 处核对（应与之前的结果一致：gcd = λ+2）
        g2 = sp.simplify(g.as_expr().subs(t, 2))
        print(f'   t=2 时 gcd = {sp.factor(g2)}')




def numeric_probe():
    """对整数 t 逐个重建实例 A(t)（V(t) 也随之变），在 q=3 阶枚举图卡×θ，看是否存在可行点。"""
    import decide_symbolic as DS
    import toeplitz_criterion as TC
    print('\n=== 数值探针：A_{00} = t，逐 t 重建实例 ===')
    k = n - p - r          # dim K = n - p - r（L0 行满秩）
    print(f'{"t":>3} {"q0":>3} {"dimV":>5} {"r1":>3} {"候选":>4} {"可行":>4} {"h 取值":>10}')
    for tv in range(-3, 7):
        At = [row[:] for row in A0]
        At[0][0] = F(tv)
        try:
            import c208_q0_lower_bound as Q0
            import qmin_scan_pr as QR
            import linalg_q as LQ2
            if LQ2.rank(QR.observability_matrix(At, C)) != n:
                print(f'{tv:>3}  （(C,A) 不可观测，跳过）')
                continue
            if LQ2.rank(QR.observability_matrix(At, L0)) != n:
                print(f'{tv:>3}  （L0 不可观测，跳过）')
                continue
            q0 = Q0.eta_and_q0(At, C, L0)[0]
            V = ZG.ker_cols([list(x) for x in C] + [list(x) for x in LQ2.mul(C, At)])
            dV = len(V[0]) if (V and V[0]) else 0
            r1 = LQ2.rank([list(x) for x in C] + [list(x) for x in LQ2.mul(C, At)])
            d = n - p - q0 - 1          # 探针固定在 q0+1 阶
            q = q0 + 1
            if d <= 0 or d > k:
                print(f'{tv:>3} {q0:>3} {dV:>5} {r1:>3}  （q0+1 阶无参数，跳过）')
                continue
            tot = feas = 0
            hs = set()
            for rows2 in __import__('itertools').combinations(range(k), d):
                for b in range(-6, 7):
                    Z = DS.Z_from_theta(At, C, L0, q, rows2, [F(b)] * (d * (k - d)))
                    if ZG.bool_rank(ZG.cols_to_rows(Z)) != d:
                        continue
                    L = ZG.L_from_Z(At, C, L0, Z, q)
                    if L is None or not LQ2.condA(At, C, L):
                        continue
                    tot += 1
                    try:
                        res = TC.analyse(At, C, L)
                    except AssertionError:
                        continue
                    hs.add(res['h'])
                    if res['five_b']:
                        feas += 1
            print(f'{tv:>3} {q0:>3} {dV:>5} {r1:>3} {tot:>4} {feas:>4} {str(sorted(hs)):>10}')
        except Exception as e:
            print(f'{tv:>3}  失败：{type(e).__name__} {e}')


if __name__ == '__main__':
    main()
    numeric_probe()
