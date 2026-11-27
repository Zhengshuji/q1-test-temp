# 654 另一个 $r_0=1$ 的不可行实例：$T_\infty=\mathbb C^3$

> 2026-11-27。构造幂零 $Z'$ 的实例，$T_\infty$ 直接为全空间，$H_0=e_1^{\mathsf T}$ 不可行。
> 状态：**[已证-纸面]** + **[精确验证]**（$K_0$、$W$）。

## 数据

$n=6$、$k=3$、$q=3$、$r_0=1$；$N$ 前 3 坐标嵌入；
$$A e_1=e_4,\quad A e_2=e_1,\quad A e_3=e_2,\quad A e_4=e_6,\quad A e_5=e_6,\quad A e_6=0,$$
$$C=\begin{bmatrix}e_5^{\mathsf T}\\ e_6^{\mathsf T}\end{bmatrix},\qquad
Z'=\begin{bmatrix}0&1&0\\0&0&1\\0&0&0\end{bmatrix}\ (\text{幂零 Jordan}),\qquad
W=A N-NZ'=e_4\,e_1^{\mathsf T}.$$
sympy 验证：$K_0=\operatorname{span}\{e_1,e_2,e_3\}$，$\operatorname{row}(W)=\operatorname{span}\{e_1\}=S$。

固定行 $H_0=e_1^{\mathsf T}$（$L_0=(1,0,0,0,0,0)$，$r_0=1$）。

## $T_\infty$

$K=S^\perp=\operatorname{span}\{e_2,e_3\}$；$Z'e_1=0,\ Z'e_2=e_1,\ Z'e_3=e_2$。

- $(Z')^{-1}K=\{x:Z'x\in K\}$：$Z'x=(0,x_1,x_2)$，首坐标为 0 ⇒ 恒在 $K$ ⇒ $(Z')^{-1}K=\mathbb C^3$；
- $K_\infty=K\cap\mathbb C^3=K=\operatorname{span}\{e_2,e_3\}$；
- $T_1=K+Z'(K)=K+\operatorname{span}\{e_1,e_2\}=\mathbb C^3$。

故
$$T_\infty=\mathbb C^3,\qquad d=0 .$$

## 不可行

651 给 $\operatorname{rank}H\le0$ ⇒ $H=0$；但 $H$ 的第一行是 $H_0=e_1^{\mathsf T}\ne0$——矛盾。**实例不可行**。

（$r_0=0$ 时 $L=0$ 可行；不可行性完全来自 $H_0\ne0$。）

## 与 650 的对比

| 实例 | $T_\infty$ | $d$ | 机制 |
|---|---|---|---|
| 650（循环 $Z'$） | $\mathbb C^3$ | 0 | $G$ 列零化 ⇒ $He_2=He_1=0$ |
| 654（幂零 $Z'$） | $\mathbb C^3$ | 0 | $T_\infty$ 递推直接给 $H=0$ |

两者都是 $r_0=1$ 的严格不可行实例，说明可行性确实数据依赖。

## 状态

- 数据与 $T_\infty$：**[已证-纸面]** + **[精确验证]**；
- 不可行：**[已证-纸面]**。
