# 604 单块可靠性：$(5b)$ 强制 $\operatorname{rank}H\le1$，配合常数列得到门

> 2026-11-27。检验 603 的“可靠性”在单块乘积门上的情形。
> **结论：单块下 $(5b)$ 迫使 $\operatorname{rank}H\le1$；$H$ 含固定常数行 $[1,r_2,0]$ 时，
> 秩 1 等价于 $z=r_1r_2$——单块可靠性成立。**
> 状态：**[已证-纸面]**。

## 单块设定

$H=\begin{bmatrix}r_1&z&0\\1&r_2&0\\0&0&0\end{bmatrix}$、$Z'=\operatorname{diag}(0,1,0)$、$H_A=HZ'$。

$(5b)$：$\operatorname{rank}(H(\lambda I-Z'))=\operatorname{rank}H=\omega$ 对所有 $\lambda$。

## 关键：$\lambda=0$ 与 $\lambda=1$

- $\lambda=0$：$\lambda I-Z'=\operatorname{diag}(0,-1,0)$，$H(\lambda I-Z')$ 只保留 $H$ 的第 2 列（乘以 $-1$）。
  所以 $\operatorname{rank}\le1$，而它要等于 $\omega$ ⇒ $\omega\le1$；
- $\lambda=1$：$\operatorname{diag}(1,0,1)$，只保留第 1、3 列；秩 $\le2$ 要等于 $\omega$。

## 秩 1 情形

$\omega=1$ 时 $H$ 秩 1。$H$ 的第二行是固定常数行 $[1,r_2,0]$，故
$$H=\begin{bmatrix}r_1&z&0\\1&r_2&0\\0&0&0\end{bmatrix}\ \text{秩 1}
\iff (r_1,z,0)=r_1(1,r_2,0)\iff z=r_1r_2 .$$
（其余行已为零。）

所以 $(5b)$（在单块上）$\iff z=r_1r_2$——与 598 的门一致。

## 对多块的意义

- 单块可靠性依赖“固定常数行”作为参照；
- 多块时，$\lambda$ 取某个块的特征值时，$(\lambda I-Z')$ 只保留**其它块**的列/行，
  条件变成对其它块的秩约束——块之间可能通过共享行（$L_0$ 的常数行）相互影响；
- 需要证明：这些 λ 约束的合取仍强制每块的门。

## 下一步

1. 写出两块情形 $\lambda=\lambda_1,\lambda_2$ 的显式秩条件；
2. 检查是否存在“非块对角但满足所有 λ 约束”的 $H$；
3. 若不存在，可靠性成立，归约闭环。

## 状态

- 单块可靠性：**[已证-纸面]**；
- 多块：**[未做]**。
