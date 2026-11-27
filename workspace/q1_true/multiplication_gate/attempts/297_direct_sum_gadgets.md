> **306 更正**：本文件的“直和=合取”只对显示的块对角压缩矩阵成立；无限制 $R$ 可把零自由行变成生成元，交叉项使两个块自动可行 ⇒ 不是 q1 实例的合取。

# 非零 gadget 的直和组合：$(5b)\iff f_1\ne0\ \wedge\ f_2\ne0$

> 2026-11-10。296 给出单个 $(5b)\iff f\ne0$ gadget。本文件做第一个组合：
> 两个 296 的块对角直和，得到
> $$(5b)\iff f_1\ne0\ \text{且}\ f_2\ne0.$$
> 这是“非零条件的合取”，是算术电路组合的第一步（但还不是乘法门）。
> 状态：**M2 + 精确验证**。

## 目标

把两个非零 gadget 组合成“同时非零”的 gadget，并验证 $(5a)(5b)$ 的块分解。

## 设想与理由

若 $(A_i,C_i,L_{0,i})$ 是 296 的 gadget，取块对角
$$A=\operatorname{diag}(A_1,A_2),\quad
C=\operatorname{diag}(C_1,C_2),\quad
L_0=\operatorname{diag}(L_{0,1},L_{0,2}),\quad
R=\operatorname{diag}(R_1(f_1),R_2(f_2)).$$
则
$$K_0=K_{0,1}\oplus K_{0,2},\quad
H=\operatorname{diag}(H_1,H_2),\quad
H_A=\operatorname{diag}(H_{A,1},H_{A,2}),\quad
P=\operatorname{diag}(P_1,P_2).$$
$(5a)$ 与 $(5b)$ 都按块分解。

## 做法：两个 296 的直和

单块（296）：
$$A_1=\begin{bmatrix}0&0&0\\1&0&0\\0&1&0\end{bmatrix},\quad
C_1=\begin{bmatrix}0&0&1\end{bmatrix},\quad
L_{0,1}=\begin{bmatrix}1&0&0\end{bmatrix},\quad
R_1(f_1)=\begin{bmatrix}0&f_1&0\end{bmatrix}.$$
$K_{0,1}=\operatorname{span}(e_1)$，$H_1=(1,0)^{\mathsf T}$，$H_{A,1}=(0,f_1)^{\mathsf T}$，$P_1=(\lambda,-f_1)^{\mathsf T}$。

直和（$n=6$，$p=2$，$q=4$，$k=2$，$\omega=2$）：
$$A=\begin{bmatrix}A_1&0\\0&A_1\end{bmatrix},\quad
C=\begin{bmatrix}C_1&0\\0&C_1\end{bmatrix},\quad
L_0=\begin{bmatrix}L_{0,1}&0\\0&L_{0,1}\end{bmatrix},\quad
R=\begin{bmatrix}R_1(f_1)&0\\0&R_1(f_2)\end{bmatrix}.$$

## 验证（c297）

- $K_0=\operatorname{span}(e_1,e_4)$（两个块的 $e_1$）；
- $H=\begin{bmatrix}1&0\\0&0\\0&1\\0&0\end{bmatrix}$，$\operatorname{rank}H=2$；
- $H_A=\begin{bmatrix}0&0\\f_1&0\\0&0\\0&f_2\end{bmatrix}$，$(5a)$ 恒成立；
- $P=\operatorname{diag}(P_1,P_2)$，$\operatorname{rank}P=\operatorname{rank}P_1+\operatorname{rank}P_2$；
- 因此
  $$(5b)\iff f_1\ne0\ \wedge\ f_2\ne0.$$

## 进展

* 直和组合定理（块对角）；
* 两个非零条件的合取；
* 精确验证。

## 最终结论

* 非零 gadget 可以直和组合，得到“多个非零条件同时成立”；
* 这仍不是乘法门：缺少等式约束 $z=xy$；
* 下一步要么做“非零 + 等式”的混合组合，要么找共享变量的串联组合。

## 放弃原因

* 未组合出等式；
* 未共享变量；
* 未接硬度归约。

## 残留价值

* 一个可复用的直和构造；
* 合取语义；
* 下一步混合组合的基础。

## 相关文件

* [attempts/296](296_nonzero_gadget_observer.md)
* `tools/verification/c297_direct_sum_gadgets.py`

## 状态

* 直和：**[M2 + 精确验证]**。
* 乘法/共享变量：**[未做]**。
