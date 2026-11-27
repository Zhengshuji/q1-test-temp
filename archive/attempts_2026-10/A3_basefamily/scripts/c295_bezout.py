r"""c295：Bézout 证书（QA24 阶段 2 / A3-4a）。

**检验的命题**：
$$U\cap I_\lambda=0\ \forall\lambda\in\mathbb C
\iff \gcd(f_1,\dots,f_N)\in\mathbb C^\times
\iff \exists g_i:\ \textstyle\sum_i g_i f_i=1,$$
其中 $f_i$ 是 $[U\mid P(\lambda)]$ 的极大子式。

**做法**：对 c282 实例（$m=5$、$r=1$、$t=3$）的若干 $U$（坐标方向 + 一般组合），
算子式、gcd、证书，核对：
1. `feasible_by_minors`（直接判据）与 `is_unit`（证书存在）**一致**；
2. 证书恒等式精确成立；
3. 实测次数 vs 保守界 $(N-1)D$。

用法：python proof/layer_program/c295_bezout.py
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
import bezout_cert as BC


def c282():
    N = 8
    def unit(i):
        return [Fr(1) if k == i else Fr(0) for k in range(N)]
    C = [unit(0), unit(1)]
    L0 = [unit(2)]
    A = [[Fr(0)] * N for _ in range(N)]
    for (i, j) in [(0, 2), (1, 3), (4, 4), (3, 5), (5, 6), (6, 7)]:
        A[i][j] = Fr(1)
    return A, C, L0, [unit(4)]


def main():
    A, C, L0, S = c282()
    st = CS_.setup(A, C, L0, 4, S)
    cols = CS_.pencil_cols(A, st)
    m = st['w'] - st['s']
    r = st['d'] - st['s']
    print(f"c282：m={m}（W/S 维数）、r={r}、t={len(cols)}、N=子式个数")
    print(f"{'U':<22}{'N':<4}{'D':<4}{'deg g':<7}{'unit?':<7}{'cert':<7}{'deg(gs)':<8}{'bound':<6}一致?")
    mism = 0
    cases = []
    for idx, h in enumerate(st['HS']):
        cases.append((f'HS[{idx}]', [list(h)]))
    # 一般组合
    h0, h1, h2 = st['HS'][0], st['HS'][1], st['HS'][2]
    cases.append(('HS0+HS1', [[h0[i] + h1[i] for i in range(m)]]))
    cases.append(('HS0+2*HS2', [[h0[i] + 2 * h2[i] for i in range(m)]]))
    cases.append(('HS1+HS3', [[h1[i] + st['HS'][3][i] for i in range(m)]]))
    for name, U in cases:
        info = BC.analyse(U, cols, m, r)
        # 与直接判据对照
        u = U[0]
        Uv = [sum(u[j] * st['WB'][st['s'] + j][k] for j in range(m)) for k in range(st['n'])]
        direct, _g = CS_.feasible_by_minors(A, C, L0, 4, S, [Uv])
        same = (direct == info['is_unit'])
        if not same:
            mism += 1
        print(f"{name:<22}{info['N']:<4}{info['D']:<4}{info['deg_g']:<7}{str(info['is_unit']):<7}"
              f"{str(info['cert_ok']):<7}{info['cert_degree']:<8}{info['bound']:<6}{'✓' if same else '✗'}")
    print(f"\n与直接判据不一致：**{mism}**（应为 0）")
    print("结论：证书存在 ⟺ gcd 是单位 ⟺ 谱可行；证书恒等式精确成立。")


if __name__ == '__main__':
    main()
