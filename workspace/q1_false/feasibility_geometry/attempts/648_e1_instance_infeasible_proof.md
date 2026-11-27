# 648 严格证明：$S=e_1$、$Z'=C_3$ 时秩 1、秩 2 都不可能（$\omega=0$ 可行）

> 2026-11-27。把 645/646 的数值证据升级为严格证明。
> **更正**：该实例并非不可行——$r_0=0$ 时 $L=0$ 给出 $\omega=0$ 的可行解。
> 状态：**[已证-纸面]**。

## 数据（可实现的 q1 实例）

$n=6$、$k=3$、$q=3$、$r_0=0$；$N$ 前 3 坐标嵌入；
$$A e_1=e_3+e_4,\quad A e_2=e_1,\quad A e_3=e_2,\quad A e_4=e_6,\quad A e_5=A e_6=0,$$
$$C=\begin{bmatrix}e_5^{\mathsf T}\\ e_6^{\mathsf T}\end{bmatrix}\ (2\times6).$$
则 $K_0=\ker[C;CA]=\operatorname{span}\{e_1,e_2,e_3\}$（sympy 验证），
$$Z'=\begin{bmatrix}0&1&0\\0&0&1\\1&0&0\end{bmatrix},\qquad W=A N-NZ'=e_4\,e_1^{\mathsf T},$$
$S=\operatorname{row}(W)=\operatorname{span}\{e_1\}$。

## $K_\infty$

$Z'e_1=e_3,\ Z'e_2=e_1,\ Z'e_3=e_2$。
$K=S^\perp=\operatorname{span}\{e_2,e_3\}$；$(Z')^{-1}K=\{x:x_2=0\}=\operatorname{span}\{e_1,e_3\}$，
$$K_\infty=K\cap(Z')^{-1}K=\operatorname{span}\{e_3\},\qquad d=2 .$$

## 引理

$G$ 的每行在 $S$ 内 ⇒ $G$ 的第 2、3 列都是零向量。特别地
$$G e_3=-HZ'e_3=-H e_2\ \Rightarrow\ He_2=0 .$$

## 秩 2 不可能

$H|_{K_\infty}=0$（639）且 $\operatorname{rank}H=2$ ⇒ $\ker H=\operatorname{span}\{e_3\}$。
但 $He_2=0$ ⇒ $e_2\in\ker H$——矛盾。

## 秩 1 不可能

$H=uv^{\mathsf T}$，$\ker H=v^\perp\supseteq\operatorname{span}\{e_3\}$ ⇒ $v_3=0$。
$He_2=0$ ⇒ $(v\cdot e_2)u=0$ ⇒ $v_2=0$ ⇒ $v\propto e_1$。
再由 $G e_2=ZHe_2-HZ'e_2=-H e_1$（$Z'e_2=e_1$）为零 ⇒ $He_1=0$ ⇒ $v_1=0$——与 $u\ne0$ 矛盾。

## $\omega=0$ 可行

$r_0=0$ ⇒ 取 $L=0$：$H=H_A=0$，$(5a)(5b)$ 成立。所以实例**可行**（$q_{\min}=0$）。

## 结论

- 秩 1、秩 2 不可能（严格证明）；
- 实例可行于 $\omega=0$；
- 644 的猜想**未被反驳**；
- **$r_0=0$ 的实例恒可行**（$L=0$）⇒ q1_true 必须用 $r_0\ge1$。

## 状态

- 秩 1/2 不可能：**[已证-纸面]**；
- 实例可行（$\omega=0$）：**[已证-纸面]**；
- 645/646 的“不可行”解读：**更正**（仅指秩 $\ge1$）。
