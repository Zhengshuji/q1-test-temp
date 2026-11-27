r"""c296：用**系数判据**扫基族（A3-3 的第一步）。

**判据**（A2 §33）：$q_U(\lambda)=\det[U\mid P_H(\lambda)]=\sum_j\lambda^j\langle a_j,p_U\rangle$，
$$\text{固定 }S\text{ 可行}\iff a_0(S)\notin\operatorname{span}\{a_1(S),\dots,a_d(S)\}.$$

**做法**：对每个 $S\in\operatorname{Gr}(s,D)$ 算 $a_j(S)$，做**一次秩判定**（比枚举 $U$ 便宜几十倍），
并与 `c293` 的直接判定对照。

**实例**：第二实例（$n=6,p=1$，$D=G$ 三维）+ R17 回归（应可行）。

用法：python proof/layer_program/c296_coeff_sweep.py
"""
import os
import sys
from fractions import Fraction as Fr

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'exact_linalg'))
sys.path.insert(0, os.path.join(_ROOT, 'tools', 'verification'))

import audit_independent as AI
import coeff_of_S as CS_
import coeff_space as CS2


def feasible_by_coeffs(A, C, L0, q, S):
    """算 $a_j(S)$，判 $a_0\notin\operatorname{span}\{a_j\}$."""
    a, P, info = CS_.coeff_forms_of_S(A, C, L0, q, S)
    forms = [a[j] for j in range(1, len(a)) if any(x != 0 for x in a[j])]
    rk1 = AI.rank(forms) if forms else 0
    rkall = AI.rank(forms + [a[0]])
    return (rkall > rk1), info, a


def second_instance():
    N = 6
    def unit(i):
        return [Fr(1) if k == i else Fr(0) for k in range(N)]
    C = [[Fr(0)] * N]
    C[0][0] = Fr(1)
    A = [[Fr(0)] * N for _ in range(N)]
    A[0][5] = Fr(1); A[2][2] = Fr(1); A[3][3] = Fr(1)
    A[1][1] = Fr(1); A[4][4] = Fr(1)
    L0 = [[Fr(0)] * N]
    L0[0][1] = Fr(1)
    return A, C, L0


def r17():
    N = 8
    def unit(i):
        return [Fr(1) if k == i else Fr(0) for k in range(N)]
    C = [unit(0), unit(1)]
    L0 = [unit(2)]
    A = [[Fr(0)] * N for _ in range(N)]
    A[6][2] = Fr(1); A[7][3] = Fr(1); A[4][4] = Fr(1)
    A[5][5] = Fr(1); A[0][6] = Fr(1); A[1][7] = Fr(1)
    return A, C, L0


def lift(coefs, D, n):
    S = []
    for row in coefs:
        v = [Fr(0)] * n
        for j, c in enumerate(row):
            for i in range(n):
                v[i] += Fr(c) * D[j][i]
        S.append(v)
    return S


def main():
    print("=== R17 回归（$S=\\operatorname{span}(e_5,e_6)$，应可行）")
    A, C, L0 = r17()
    geo = CS_.setup(A, C, L0, 3, [])
    D = geo  # 只为拿 D 的基
    st0 = CS_.setup(A, C, L0, 3, [])
    # 直接构造 S = e5,e6
    N = 8
    def unit(i):
        return [Fr(1) if k == i else Fr(0) for k in range(N)]
    S = [unit(4), unit(5)]
    ok, info, a = feasible_by_coeffs(A, C, L0, 3, S)
    print(f"  可行={ok}  (m={info['m']}, r={info['r']}, deg={info['deg']})")

    print("\n=== 第二实例：系数判据扫 $S$")
    A, C, L0 = second_instance()
    geo = CS_.setup(A, C, L0, 1, [])
    Dv = geo['V']  # 占位；下面直接用 D
    # 取 D 的基
    Vt = [list(x) for x in geo['V']]
    Ht = [list(x) for x in geo['H']]
    G = AI.nullspace(Vt + Ht)
    Gt = [list(x) for x in G]
    Hperp = AI.nullspace(Ht)
    D = AI.nullspace(Gt + AI.mul(Hperp, A))
    print(f"  dim D = {len(D)}")
    for q in (4, 3):
        d = geo['w'] - q
        print(f"\n  q={q}（d={d}）")
        for s in range(1, min(d, len(D)) + 1):
            coords = CS2.enum_subspaces(len(D), s, bound=1) if False else None
            # 用 base_sweep 的枚举器
            import base_sweep as BS
            coords = BS.enum_subspaces(len(D), s, bound=1)
            nf = 0
            nt = 0
            for cf in coords:
                S = lift(cf, D, geo['n'])
                try:
                    ok, info, a = feasible_by_coeffs(A, C, L0, q, S)
                except Exception as e:
                    continue
                nt += 1
                if ok:
                    nf += 1
            print(f"    s={s}: 扫 {nt} 个 S，系数判据可行 {nf}")


if __name__ == '__main__':
    main()
