# 650 反例：649 的必要条件不充分（$H_0\ne0$ 的不可行实例）

> 2026-11-27。在 648 的数据上取固定行 $H_0=e_1^{\mathsf T}$（满足 649 的两个条件），证明实例不可行。
> 状态：**[已证-纸面]**。

## 数据

与 648 相同（$n=6$、$k=3$、$q=3$、$r_0=1$）；
$$A e_1=e_3+e_4,\ A e_2=e_1,\ A e_3=e_2,\ A e_4=e_6,\ \text{其余 }0,\qquad
C=\begin{bmatrix}e_5^{\mathsf T}\\ e_6^{\mathsf T}\end{bmatrix},$$
$$Z'=\begin{bmatrix}0&1&0\\0&0&1\\1&0&0\end{bmatrix},\qquad S=\operatorname{span}\{e_1\}.$$
固定行 $H_0=e_1^{\mathsf T}$（$L_0=(1,0,0,0,0,0)$）。

## 649 的条件

$K_\infty=\operatorname{span}\{e_3\}$（648），$d=2$：
$$H_0e_3=0\ ✓,\qquad \operatorname{rank}H_0=1\le2\ ✓ .$$

## 不可行的证明

设 $H$ 为可行扩展，$H_0=e_1^{\mathsf T}$ 是第一行；$He_3=0$（$K_\infty\subseteq\ker H$）。
$G$ 的每行在 $S$ 内 ⇒ $G$ 的第 2、3 列为零。

- 第 3 列：$Ge_3=ZHe_3-HZ'e_3=-H e_2$（$Z'e_3=e_2$）⇒ $He_2=0$；
- 第 2 列：$Ge_2=ZHe_2-HZ'e_2=-H e_1$（$Z'e_2=e_1$）⇒ $He_1=0$。

但 $H_0=e_1^{\mathsf T}$ ⇒ $(He_1)_1=e_1^{\mathsf T}e_1=1\ne0$，矛盾。

（秩 0 不可能因 $H_0\ne0$；秩 1 同被上述两式排除。）

## 结论

$$\boxed{H_0|_{K_\infty}=0,\ \operatorname{rank}H_0\le d\ \not\Rightarrow\ \text{可行}}$$

- 649 的**充分性被推翻**；
- 第一个 $r_0\ge1$、$W\ne0$ 的严格不可行实例；
- 机制：$G$ 在 $S^\perp$ 列上的零化 + $Z'$ 的循环作用，把 $He_2,He_1$ 逐一逼零。

## 意义

- 可行性确实**数据依赖**（同 $Z',S$，$H_0$ 不同则可行性不同）；
- 这是实例级不可行，不等于 NP-hard；
- 需要把“$H_0$ 能否嵌入”写成新的不变量（ChatGPT 的 $\bar H_0$ 嵌入问题）。

## 状态

- 反例：**[已证-纸面]**；
- 649 充分性：**推翻**。
