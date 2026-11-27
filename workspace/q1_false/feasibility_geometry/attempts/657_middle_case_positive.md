# 657 中间情形的第一个正面例子（$k=2$，$T_\infty=0$）

> 2026-11-27。656 的 $k=2$ 小例子：构造出显式可行解，验证条件化充分性在中间情形（$0<s<k$）可以成立。
> 状态：**[已证-纸面]** + **[精确验证]**。

## 数据

$n=4$、$k=2$、$q=3$、$r_0=1$；$N$ 前 2 坐标嵌入；
$$A e_1=e_2+e_3,\quad A e_3=e_4,\quad \text{其余 }0,\qquad C=e_4^{\mathsf T},$$
$$Z'=\begin{bmatrix}0&0\\1&0\end{bmatrix},\qquad S=\operatorname{row}(W)=\operatorname{span}\{e_1\}.$$
sympy：$K_0=\operatorname{span}\{e_1,e_2\}$、$W=e_3e_1^{\mathsf T}$。
固定行 $H_0=e_1^{\mathsf T}$（$r_0=1$）。

## $T_\infty$

$K=S^\perp=\operatorname{span}\{e_2\}$；$Z'e_2=0$ ⇒ $(Z')^{-1}K=\mathbb C^2$ ⇒ $K_\infty=K\cap\mathbb C^2=K$？再算：
$Z'e_2=0\in K$ ⇒ $e_2\in(Z')^{-1}K$；$Z'e_1=e_2\in K$ ⇒ $e_1\in(Z')^{-1}K$ ⇒ $(Z')^{-1}K=\mathbb C^2$。
$K_\infty=K=\operatorname{span}\{e_2\}$；$T_1=K+Z'(K)=K+Z'e_2=K$ ⇒ $T_\infty=\operatorname{span}\{e_2\}$，$d=1$？

（注意：$Z'e_2=0$，$Z'(K)=\{0\}$；$T_1=K$。）所以 $T_\infty=\operatorname{span}\{e_2\}$、$d=1$。
$H_0e_2=0$ ✓、$\operatorname{rank}H_0=1\le1$ ✓——条件全满足。

## 构造（秩 1）

$$H=\begin{bmatrix}1&0\\0&0\\1&0\end{bmatrix}=u\,e_1^{\mathsf T}\ (u=(1,0,1)^{\mathsf T}),\qquad
Z=\begin{bmatrix}0&0&0\\0&0&0\\1&0&0\end{bmatrix}.$$

- $HZ'=u\,(e_1^{\mathsf T}Z')=u\cdot(0,0)=0$；
- $ZH=(Zu)e_1^{\mathsf T}=e_3e_1^{\mathsf T}$，故 $G=ZH-HZ'=e_3e_1^{\mathsf T}$，行在 $S$ 内 ✓；
- $(5a)$：$H_A=ZH$ ⇒ 自动；
- $(5b)$：$P(\lambda)=(\lambda u-e_3)e_1^{\mathsf T}$，秩 1 对所有 $\lambda$（$\lambda u\ne e_3$，因 $u=(1,0,1)$ 与 $e_3=(0,0,1)$ 不成比例）✓。

sympy：$\operatorname{rank}P(0)=\operatorname{rank}P(1)=\operatorname{rank}P(2)=1=\omega$。

## 结论

- 中间情形（$T_\infty\ne0$ 且 $T_\infty\ne\mathbb C^k$）**可以可行**；
- 构造要点：取 $H=ue_1^{\mathsf T}$ 使 $HZ'=0$，$G=(Zu)e_1^{\mathsf T}$ 自动落在 $S$ 内；
  再取 $Z$ 使 $Zu$ 不在 $\operatorname{span}\{u\}$ 内（避免特征值）；
- 这验证了条件化充分性在至少一个中间例子中成立（还不是一般证明）。

## 与 ChatGPT 的交流

它给出的 $Z$ 均不满足扩展方程；本构造给出反例：取 $H=ue_1^{\mathsf T}$ 时，$G$ 的行约束自动满足，
只需 $Zu$ 不平行于 $u$。已准备把该反例发回。

## 状态

- 构造：**[已证-纸面]** + **[精确验证]**；
- 一般充分性：**[开放]**。
