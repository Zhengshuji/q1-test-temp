r"""Stage 2（修正）：构造一个 $q=2$ **可行**的实例，并给出可行集的显式描述。

上一批 12 组数据全部不可行，但那是**这些具体 $A$ 太小**造成的，不是一般现象。
本文件按纸面推演构造一个可行实例：

$C=e_1^{\mathsf T}$、$L_0=e_2^{\mathsf T}$、$A$ 取
$$A=\begin{pmatrix}0&0&0&1\\ 0&1&0&0\\ 0&0&0&0\\ 0&1&0&0\end{pmatrix}$$
则 $CA=e_4^{\mathsf T}$，$K=\ker\{e_1,e_4\}=\langle e_2,e_3\rangle$（$k=2$），
$$H(R)=\begin{pmatrix}1&0\\ r_2&r_3\end{pmatrix},\qquad H_A(R)=\begin{pmatrix}1&0\\ r_2+r_4&r_3\end{pmatrix}.$$
$\omega=1$ 层：$r_3=0$，$W_K=\langle(1,r_2)\rangle$；
$(5a)$ 自动满足（$\ker H=\langle e_2\rangle$ 被 $H_A$ 杀掉，$A_{23}=0$ 且 $r\cdot c_3=r_3=0$）；
非不变条件：$\det\begin{pmatrix}1&1\\ r_2&r_2+r_4\end{pmatrix}=r_4$，故 $r_4\ne0$。
⟹ **可行集 = $\{r_3=0,\ r_4\ne0\}$**（在 $\mathbb R^4$ 中超平面 $r_3=0$ 去掉 $r_2=0$ 的超平面），维数 3、开稠密。

脚本对若干点逐条核对 $(5a)/(5b)$（精确有理），并用 `consistency_checks` 交叉验证。
"""

import os
import sys
from fractions import Fraction as Fr

import sympy as sp

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
for p_ in ('tools/exact_linalg', 'tools/verification', 'tools/ledger'):
    sys.path.insert(0, os.path.join(_ROOT, p_))

import consistency_checks as CC   # noqa: E402


def exact_check(A, C, L0, Rrow):
    """用 consistency_checks 逐条核对（转 Fraction）。"""
    conv = lambda M: [[Fr(int(x)) for x in row] for row in M.tolist()]
    L = L0.col_join(Rrow)
    try:
        res = CC.check_candidate(conv(A), conv(C), conv(L0), conv(L))
        return res
    except Exception as e:
        return f'异常 {type(e).__name__}: {e}'


def main():
    A = sp.Matrix([[0, 0, 0, 1],
                   [0, 1, 0, 0],
                   [0, 0, 0, 0],
                   [0, 1, 0, 0]])
    C = sp.Matrix([[1, 0, 0, 0]])
    L0 = sp.Matrix([[0, 1, 0, 0]])

    CA = C * A
    print('C =', C.tolist(), ' L0 =', L0.tolist())
    print('A =', A.tolist())
    print('CA =', CA.tolist())
    M = C.col_join(CA)
    NK = sp.Matrix.hstack(*M.nullspace())
    print('rank[C;CA] =', M.rank(), ' dim K =', 4 - M.rank(), ' N_K =', NK.tolist())

    r = sp.symbols('r1:5')
    Rrow = sp.Matrix([[r[0], r[1], r[2], r[3]]])
    L = L0.col_join(Rrow)
    H = sp.expand(L * NK)
    HA = sp.expand((L * A) * NK)
    print('H =', H.tolist(), '  det H =', sp.factor(H.det()))
    print('H_A =', HA.tolist())

    # 断言纸面推导的关键量
    assert sp.simplify(H.det() - r[2]) == 0, 'det H 应为 r3'
    assert sp.simplify(HA[0, 0] - 1) == 0 and sp.simplify(HA[0, 1]) == 0, 'H_A 第一行应为 (1,0)'
    print('断言通过：det H = r3；H_A 第一行 = (1,0)')

    # 非不变条件（r3 = 0 上）
    sub = {r[2]: 0}
    Hs, HAs = sp.simplify(H.subs(sub)), sp.simplify(HA.subs(sub))
    w = Hs * sp.Matrix([1, 0])
    phi = HAs * sp.Matrix([1, 0])
    det2 = sp.factor(sp.Matrix.hstack(w, phi).det())
    print('在 r3=0 上：w =', w.T.tolist()[0], ' Phi_K(w) =', phi.T.tolist()[0],
          ' det[w,Phi_K(w)] =', det2)
    assert sp.simplify(det2 - r[3]) == 0, '非不变行列式应为 r4'
    print('断言通过：非不变行列式 = r4 ⟹ 可行集 = {r3=0, r4≠0}')

    # 逐点核对
    print('\n逐点核对（精确有理）：')
    for trial in [(0, 1, 0, 1),      # 预测：可行（r3=0, r4=1 ≠ 0）
                  (0, 1, 0, 0),      # 预测：不可行（r4=0 ⟹ 平行）
                  (0, 1, 1, 1),      # 预测：不可行（r3=1 ⟹ ω=2）
                  (5, 0, 0, 3)]:     # 预测：可行（r1,r2 无关）
        Rr = sp.Matrix([[sp.Integer(t) for t in trial]])
        verdict = '可行' if (trial[2] == 0 and trial[3] != 0) else '不可行'
        res = exact_check(A, C, L0, Rr)
        print(f'  R={trial} 预测={verdict} → consistency_checks: {res}')


if __name__ == '__main__':
    main()
