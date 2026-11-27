r"""Stage 2（专家第七轮 §4.7 的配方）：最小案例 $n=4,p=1,q=2,r=1$ 的**精确**几何。

**CAS 使用说明**：本文件用 sympy 做**精确有理**符号运算（无浮点）。它给出的是
"给定具体有理数据后可行集的显式描述"，**不是**对一般 $n$ 的定理。

设定：$\mathcal L(R)=\begin{bmatrix}L_0\\R\end{bmatrix}$（$2\times4$），$R=(r_1,r_2,r_3,r_4)$ 取符号；
$K=\ker[C;CA]$（$\dim K=2$）；$N_K$ 为 $K$ 的有理基（$4\times2$）；
$H(R)=\mathcal L(R)N_K$（$2\times2$），$\omega=\operatorname{rank}H$；
$H_A(R)=\mathcal LA(R)N_K$，且 $\Phi_K(Hc)=H_Ac$（$v=N_Kc$ 时 $\mathcal Lv=Hc$、$\mathcal LAv=H_Ac$）。

按专家的三条结论分情形：
* $\omega=2$（$H$ 可逆）：**自动不可行**；
* $\omega=0$：**自动可行**（但 $(5a)$ 仍须单独满足）；
* $\omega=1$：可行 $\iff$ $w=Hc\ne0$ 时 $\det[w,\ H_Ac]\ne0$（$\Phi_K$ 在 $1$ 维 $W_K$ 上无特征值）。

最后对若干具体 $R$ 用 `consistency_checks.check_candidate` 交叉核对 $(5a)/(5b)$。
"""

import os
import sys

import sympy as sp

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import consistency_checks as CC   # noqa: E402


def build(A, C, L0):
    n = A.shape[0]
    M = C.col_join(C * A)
    NK = sp.Matrix.hstack(*M.nullspace()) if M.nullspace() else sp.zeros(n, 0)
    r = sp.symbols('r1:%d' % (n + 1))
    Rrow = sp.Matrix([[r[i] for i in range(n)]])
    L = L0.col_join(Rrow)                 # 2 x n
    H = L * NK                            # 2 x k
    HA = (L * A) * NK
    return NK, r, Rrow, L, H, HA


def stratum_report(H, HA, r):
    H = sp.simplify(H)
    HA = sp.simplify(HA)
    print('  H =', H.tolist())
    print('  det H =', sp.factor(H.det()))
    print('  H_A =', HA.tolist())
    return H, HA


def main():
    # ---- 具体有理数据：C=e1^T, A 的第一行 = e2^T（使 rank[C;CA]=2），L0=e3^T ----
    A = sp.Matrix([[0, 1, 0, 0],
                   [0, 0, 0, 1],
                   [0, 0, 0, 0],
                   [1, 0, 1, 0]])
    C = sp.Matrix([[1, 0, 0, 0]])
    L0 = sp.Matrix([[0, 0, 1, 0]])

    print('A =', A.tolist(), ' C =', C.tolist(), ' L0 =', L0.tolist())
    M = C.col_join(C * A)
    print('rank[C;CA] =', M.rank(), '  dim K =', 4 - M.rank())

    NK, r, Rrow, L, H, HA = build(A, C, L0)
    print('K 的基 N_K =', NK.tolist())
    print('  L0*N_K =', (L0 * NK).tolist())
    stratum_report(H, HA, r)

    detH = sp.expand(H.det())
    print('\n结论 1：det H =', detH, ' ⟹ 可行（$\omega\\le1$）需', sp.solve(detH, r[0])) 

    # ---- 在 det H = 0 上取 rank H = 1 的情形，解 w、Phi_K(w) ----
    # 令 r4 = 0（即 det H = 0），其余 r1,r2,r3 自由
    sub = {r[3]: 0}
    Hs = sp.simplify(H.subs(sub))
    HAs = sp.simplify(HA.subs(sub))
    print('\n在 r4=0 上：H =', Hs.tolist(), '  rank =', Hs.rank())
    print('            H_A =', HAs.tolist())

    # 取 c=(1,0)：w = H 的第 0 列；若为 0 则取 c=(0,1)
    for cidx in (0, 1):
        c = sp.Matrix([1, 0]) if cidx == 0 else sp.Matrix([0, 1])
        w = sp.simplify(Hs * c)
        if sp.simplify(w) != sp.zeros(2, 1):
            phi = sp.simplify(HAs * c)
            det2 = sp.simplify(sp.Matrix.hstack(w, phi).det())
            print(f'  取 c={c.T.tolist()[0]}：w = {w.T.tolist()[0]}，Phi_K(w) = {phi.T.tolist()[0]}，'
                  f'det[w,Phi_K(w)] = {sp.factor(det2)}')
            break

    print('\n结论 2（该组数据）：谱条件在 r4=0 上要求上述行列式 ≠ 0；'
          '若它不恒为 0，则可行集是超平面 r4=0 去掉一个真子集（开稠密）。')

    # ---- (5a) 的精确检查（在 r4=0 上，对若干有理点）----
    print('\n结论 3：逐点核对 (5a)/(5b)（用 consistency_checks）')
    CA = C * A
    for trial in ([(0, 0, 1, 0), (1, 0, 0, 0), (0, 1, 0, 0), (1, 1, 1, 0), (0, 0, 0, 1)]):
        Lr = sp.Matrix([[L0[j] for j in range(4)]] + [[sp.Integer(trial[j]) for j in range(4)]])
        try:
            res = CC.check_candidate(A.tolist(), C.tolist(), L0.tolist(), Lr.tolist())
            five_a = res.get('five_a')
            five_b = res.get('five_b')
        except Exception as e:                     # 接口不符时打印异常，便于对齐
            five_a = five_b = f'异常: {type(e).__name__}: {e}'
        print(f'  R={trial}: (5a)={five_a}, (5b)={five_b}')


if __name__ == '__main__':
    main()
