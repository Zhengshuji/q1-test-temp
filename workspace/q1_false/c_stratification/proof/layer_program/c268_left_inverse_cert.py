r"""R17 两个例子的显式左逆证书 $X(\lambda)T_\lambda=I_t$（专家 QA19 §2.2 要求）。

例 1（$t=2$）：$S=\operatorname{span}(e_5,e_6)$、$U=\operatorname{span}(e_4+e_7)$。
  $W/S$ 的基 $(e_3,e_4,e_7,e_8)$，$Z/S=\operatorname{span}(e_4+e_7)$；
  在 $W/Z$ 的基 $(e_3,e_4,e_8)$ 下
  $$T_\lambda=\begin{pmatrix}-\lambda&0\\-1&-\lambda\\0&1\end{pmatrix},\qquad
  X(\lambda)=\begin{pmatrix}0&-1&-\lambda\\0&0&1\end{pmatrix},\qquad \deg X=1=t-1 .$$

例 2（$t=1$）：$S=\operatorname{span}(e_4,e_5,e_6)$、$Z/S=\operatorname{span}(e_8)$。
  $W/S$ 的基 $(e_3,e_7,e_8)$，$W/Z$ 的基 $(e_3,e_7)$；
  $$T_\lambda=\begin{pmatrix}-\lambda\\1\end{pmatrix},\qquad X=(0\ \ 1),\qquad \deg X=0\le t-1 .$$

用法：python proof/layer_program/c268_left_inverse_cert.py
"""
from fractions import Fraction as Fr

I2 = [[Fr(1), Fr(0)], [Fr(0), Fr(1)]]
Z2 = [[Fr(0), Fr(0)], [Fr(0), Fr(0)]]


def mm(A, B):
    assert len(A[0]) == len(B), '维数不匹配'
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
            for i in range(len(A))]


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def check(name, T0, T1, X0, X1, t, target):
    C0 = mm(X0, T0)
    C1 = add(mm(X0, T1), mm(X1, T0))
    C2 = mm(X1, T1)
    Zt = Z2 if t == 2 else [[Fr(0)]]
    ok = (C0 == target) and (C1 == Zt) and (C2 == Zt)
    print(f'{name}: X*T 常数项 = {C0}, lam 项 = {C1}, lam^2 项 = {C2}')
    print(f'  => 证书成立: {ok}；deg X = {1 if any(any(v) for v in X1) else 0} (t-1 = {t-1})')
    return ok


def main():
    # 例 1：t=2
    T0 = [[Fr(0), Fr(0)], [Fr(-1), Fr(0)], [Fr(0), Fr(1)]]
    T1 = [[Fr(-1), Fr(0)], [Fr(0), Fr(-1)], [Fr(0), Fr(0)]]
    X0 = [[Fr(0), Fr(-1), Fr(0)], [Fr(0), Fr(0), Fr(1)]]
    X1 = [[Fr(0), Fr(0), Fr(-1)], [Fr(0), Fr(0), Fr(0)]]
    ok1 = check('例1 (t=2)', T0, T1, X0, X1, 2, I2)
    # 例 2：t=1
    T0b = [[Fr(0)], [Fr(1)]]
    T1b = [[Fr(-1)], [Fr(0)]]
    X0b = [[Fr(0), Fr(1)]]
    X1b = [[Fr(0), Fr(0)]]
    ok2 = check('例2 (t=1)', T0b, T1b, X0b, X1b, 1, [[Fr(1)]])
    print('\n两个证书都成立:', ok1 and ok2)


if __name__ == '__main__':
    main()
