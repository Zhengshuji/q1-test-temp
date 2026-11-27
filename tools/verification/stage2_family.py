r"""Stage 2（续）：在 16 组小型有理数据上判定 $q=2$ 是否可行（精确符号，无浮点）。

对每组 $(A,C,L_0)$：$C=e_1^{\mathsf T}$、$\operatorname{rank}[C;CA]=2$（故 $\dim K=2$）、$L_0=e_i^{\mathsf T}$。
$\mathcal L(R)=\begin{bmatrix}L_0\\R\end{bmatrix}$，$H(R)=\mathcal L N_K$（$2\times2$），$H_A(R)=\mathcal LA N_K$。

分层（专家第七轮 §4.2–§4.4）：
  $\omega=2$：$(5b)$ **必失败**；
  $\omega=0$：$(5b)$ 自动成立（但 $(5b)$ 之外仍须 $(5a)$；此处 $h_0=L_0N_K\ne0$ 时不可能 $\omega=0$）；
  $\omega=1$（$\det H=0$、$H\ne0$）：需要
      ① $(5a)$：$\ker H\subseteq\ker H_A$（即 $\mathcal LA$ 在 $\ker(\mathcal L|_K)$ 上为零）；
      ② 非不变：$w=Hc\ne0$ 时 $\det[w,H_Ac]\ne0$。
输出每组的判定：可行 / 不可行 / 需进一步条件，以及理由。
"""

import os
import sys

import sympy as sp

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))


def analyse(A, C, L0, tag):
    n = A.shape[0]
    M = C.col_join(C * A)
    ns = M.nullspace()
    if len(ns) != 2:
        return f'{tag}: dim K={len(ns)}（跳过，本批要求 dim K=2）'
    NK = sp.Matrix.hstack(*ns)
    r = sp.symbols('r1:%d' % (n + 1))
    Rrow = sp.Matrix([[r[i] for i in range(n)]])
    L = L0.col_join(Rrow)
    H = sp.expand(L * NK)
    HA = sp.expand((L * A) * NK)
    detH = sp.factor(H.det())
    h0 = L0 * NK
    if sp.simplify(detH) == 0:
        return f'{tag}: det H ≡ 0（$\\omega<2$ 恒成立；需另一套分析）'

    # 在 det H = 0 上：取参数 r_j 解出最后一个变量
    vs = [v for v in r if detH.has(v)]
    if not vs:
        return f'{tag}: det H={detH} 为常数，退化'
    var = vs[-1]
    sol = sp.solve(sp.Eq(detH, 0), var)
    if not sol:
        return f'{tag}: det H={detH}，无法解出参数'
    sub = {var: sol[0]}
    Hs = sp.simplify(H.subs(sub))
    HAs = sp.simplify(HA.subs(sub))

    # (5a)：ker H 上的方向是否被 H_A 杀掉
    ker_vecs = Hs.nullspace()
    adm_conds = []
    for kv in ker_vecs:
        img = sp.simplify(HAs * kv)
        for expr in img:
            if sp.simplify(expr) != 0:
                adm_conds.append(sp.factor(expr))
    adm_conds = [c for c in adm_conds if sp.simplify(c) != 0]

    # 非不变条件：取 c 使 Hc ≠ 0
    noninv = None
    for c in (sp.Matrix([1, 0]), sp.Matrix([0, 1])):
        w = sp.simplify(Hs * c)
        if sp.simplify(w) != sp.zeros(2, 1):
            phi = sp.simplify(HAs * c)
            noninv = sp.factor(sp.Matrix.hstack(w, phi).det())
            break

    # 判定
    const_bad = any(c.is_number and sp.simplify(c) != 0 for c in adm_conds)
    if const_bad:
        verdict = '不可行（$(5a)$ 在 $\\det H=0$ 上无解：条件是某个非零常数）'
    elif sp.simplify(noninv) == 0:
        verdict = '不可行（$\\omega=1$ 时 Phi_K 必有不变线）'
    elif adm_conds:
        verdict = (f'需条件：$(5a)$ 要求 {" 且 ".join(map(str, adm_conds))} = 0，'
                   f'再要求 {noninv} ≠ 0')
    else:
        verdict = f'可行（$\\omega=1$ 层：仅需 {noninv} ≠ 0）'
    return (f'{tag}: det H={detH}，h0={h0.T.tolist()[0]}；'
            f'在 det H=0 上：ker 条件={adm_conds or "无"}，非不变行列式={noninv} ⟹ {verdict}')


def main():
    As = {
        'A1': sp.Matrix([[0, 1, 0, 0], [0, 0, 0, 1], [0, 0, 0, 0], [1, 0, 1, 0]]),
        'A2': sp.Matrix([[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0]]),
        'A3': sp.Matrix([[0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]),
    }
    C = sp.Matrix([[1, 0, 0, 0]])
    print('C = e1^T；对每个 A 与 L0=e1..e4 判定 q=2 可行性\n')
    for aname, A in As.items():
        if (C * A).rank() == 0:
            print(f'{aname}: rank[C;CA]=1（跳过）')
            continue
        for i in range(4):
            L0 = sp.zeros(1, 4)
            L0[i] = 1
            print(analyse(A, C, L0, f'{aname}/L0=e{i+1}'))
        print()


if __name__ == '__main__':
    main()
