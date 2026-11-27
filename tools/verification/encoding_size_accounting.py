"""encoding_size_accounting.py —— G.2 编码的精确规模记账（专家 2026-11-04 §4.2 要求）

复杂度模型（先写明，再记账）：

1. **输入**：$A\\in\\mathbb Q^{n\\times n}$、$C\\in\\mathbb Q^{p\\times n}$、$L_0\\in\\mathbb Q^{r\\times n}$，
   每个元素的分子分母二进制长度 $\\le B$（输入比特数 $O(n^2B)$）。
2. **变量域**：实数。复变量按实部/虚部拆分：变量数与约束数各乘 2，次数不变（仍是双线性）。
3. **复杂度口径**：位复杂度。下面只数**变量数 / 约束数 / 次数上界**；位长由 Hadamard + Cramer 控制为
   $O(n^2(B+\\log n))$。
4. **秩层析取**：$s=\\operatorname{rank}\\mathcal L(V)$ 只有 $q+1$ 种取值。按"析取**计入**规模"处理：
   总规模 $\\le (q+1)\\times$单分支规模（析取可用"各分支违反量之积 = 0"编码，不引入指数）。

用法：python -u tools/verification/encoding_size_accounting.py
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(os.path.dirname(_HERE))


def count_branch(n, p, r, q, s, dV, k, d, use_W=False):
    """单分支（给定 s）的变量数与约束数。

    use_W=False（默认，推荐）：直接用 L 作变量；rank[C;L] = p+q 自动给出 dim ker[C;L] = d = n-p-q。
    use_W=True：另加 W (Z = K W) 与 Y_W；与 L 参数化冗余，只作对照。
    """
    V = {}
    if use_W:
        V['W (k×d)'] = k * d
        V['Y_W (d×k)'] = d * k
    V['L (q×n)'] = q * n
    V['T (q×(q+2p))'] = q * (q + 2 * p)
    V['Λ (q×q)'] = q * q
    V['G0 (q×p)'] = q * p
    V['G1 (q×p)'] = q * p
    V['A (q×s)'] = q * s
    V['B (s×dV)'] = s * dV
    V['Y_A (s×q)'] = s * q
    V['Y_B (dV×s)'] = dV * s
    mE = q - s
    V['E (mE×q)'] = mE * q
    V['Y_E (q×mE)'] = q * mE
    V['E_1..E_{q-1} ((q−1)·mE·q)'] = (q - 1) * mE * q
    V['Y_O (q×q·mE)'] = q * (q * mE)

    C = {}
    C['rank L = q（左逆证书）'] = q * q
    C['rank[C;L] = p+q（左逆证书）'] = (p + q) * (p + q)
    if use_W:
        C['Y_W W = I_d'] = d * d
    C['row L_0 ⊆ row L（S·L = L_0）'] = r * q
    C['(5a)：T·H = L A'] = q * n
    C['ΛL + G0C + G1CA = L A'] = q * n
    C['M = L V0 = A B'] = q * dV
    C['Y_A A = I_s'] = s * s
    C['B Y_B = I_s'] = s * s
    C['E M = 0'] = mE * dV
    C['E Y_E = I_mE'] = mE * mE
    C['E_0 = E'] = mE * q
    C['E_{j+1} = E_j Λ（j=0..q−2）'] = (q - 1) * mE * q
    C['Y_O Õ = I_q'] = q * q

    return {'vars': V, 'constrs': C, 'nvars': sum(V.values()),
            'nconstrs': sum(C.values()), 'deg': 2, 'mE': mE}


def table(use_W):
    print(f'=== 单分支规模（use_W={use_W}）===')
    print(f'{"n":>3} {"p":>2} {"r":>2} {"q":>3} {"dV":>3} {"s":>2} {"vars":>6} {"constrs":>8} {"(q+1)vars":>11}')
    for n in (6, 7, 8, 10, 12):
        for (p, r) in [(1, 1), (2, 1), (2, 2), (3, 2)]:
            if p + r > n:
                continue
            q = max(p + 1, n // 2)
            d = n - p - q
            if d < 0:
                continue
            dV = max(1, n - (p + r))
            s = max(0, q // 2)
            out = count_branch(n, p, r, q, s, dV, n - p - r, d, use_W=use_W)
            print(f'{n:>3} {p:>2} {r:>2} {q:>3} {dV:>3} {s:>2} '
                  f'{out["nvars"]:>6} {out["nconstrs"]:>8} {(q + 1) * out["nvars"]:>11}')
    print()


def main():
    table(use_W=False)
    table(use_W=True)
    print('=== 明细（n=8, p=2, r=2, q=4, dV=4, s=2, d=2, use_W=False）===')
    out = count_branch(8, 2, 2, 4, 2, 4, 4, 2)
    for kk, v in out['vars'].items():
        print(f'  变量  {kk:<34} {v:>6}')
    for kk, v in out['constrs'].items():
        print(f'  约束  {kk:<34} {v:>6}')
    print(f'  合计：变量 {out["nvars"]}，约束 {out["nconstrs"]}，次数 ≤ {out["deg"]}')
    print(f'  含 q+1 = 5 项析取：变量 ≤ {5 * out["nvars"]}，约束 ≤ {5 * out["nconstrs"]}')
    print()
    print('结论：单分支的变量/约束数都是 O(q^3 + qn)（最大项来自 E_j 与 Y_O 的 q^2·mE），'
          '乘 (q+1) 项析取仍是多项式；次数 ≤2（用递推，不用 EΛ^k 的展开）。')


if __name__ == '__main__':
    main()
