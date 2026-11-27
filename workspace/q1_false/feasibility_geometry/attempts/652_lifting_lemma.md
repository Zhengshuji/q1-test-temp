# 652 提升引理：$H_0|_T=0$ ⇒ 存在秩 $d$ 的扩展 $H$（含固定行）

> 2026-11-27。ChatGPT 指出充分性证明分两步：先证“提升引理”（线性代数），再证“$Z$ 构造引理”。
> 本文件完成第一步。
> 状态：**[已证-纸面]**。

## 引理（提升）

设 $T=T_\infty\subseteq\mathbb C^k$，$d=k-\dim T$，$\pi:\mathbb C^k\twoheadrightarrow\mathbb C^k/T$ 为商映射。
给定 $H_0\in\mathbb C^{r_0\times k}$，满足
$$H_0|_T=0,\qquad \operatorname{rank}H_0=r_0\le d .$$
则对任意 $q\ge d$，存在 $H\in\mathbb C^{q\times k}$，使
$$H\text{ 的前 }r_0\text{ 行}=H_0,\qquad H|_T=0,\qquad \operatorname{rank}H=d .$$

## 证明

$H_0$ 在 $T$ 上为零 ⇒ 存在 $\bar H_0:\mathbb C^k/T\to\mathbb C^{r_0}$（$r_0$ 个线性泛函）使 $H_0=\bar H_0\circ\pi$。
$\operatorname{rank}\bar H_0=r_0\le d$。把 $\bar H_0$ 的行（$r_0$ 个线性无关泛函）扩充为 $(\mathbb C^k/T)^*$ 的一组基中的 $d$ 个泛函，
记为 $\bar H$；取
$$H=\begin{bmatrix}H_0\\ \text{其余 }d-r_0\text{ 行}\\ 0_{(q-d)\times k}\end{bmatrix}
=\begin{bmatrix}\bar H\\0\end{bmatrix}\circ\pi .$$
则 $H|_T=0$、前 $r_0$ 行等于 $H_0$、$\operatorname{rank}H=\operatorname{rank}\bar H=d$。$\square$

## 第二步（待证）：$Z$ 构造引理

$$\exists Z:\qquad ZH-HZ'\in\operatorname{Mat}_{q\times k}(S),\qquad
\operatorname{im}H\cap\ker(Z-\lambda I)=0\ \ \forall\lambda .$$

- 第一式是**关于 $Z$ 的线性方程组**（$H,H_A$ 固定时）；
- 第二式是“$Z$ 在 $\operatorname{im}H$ 上无特征向量”的开条件；
- 两者联立的存在性即充分性的核心。

## 已知特例

- 631（$T=0$，$d=k$）：取 $Z$ 一般位置即可；
- 638（$T=\operatorname{span}\{e_3\}$，$d=2$）：构造成功；
- 648/650（$T=\mathbb C^k$，$d=0$）：$H=0$，只有 $H_0=0$ 可行——与引理一致（$r_0\le0$）。

## 下一步

1. 固定 $H$（提升引理给出的），把 $ZH-HZ'\in S$ 写成 $Z$ 的线性系统；
2. 研究解空间是否包含“在 $\operatorname{im}H$ 上无特征向量”的矩阵（开条件，通常非空除非被方程强制）；
3. 若被强制，提炼出新的相容性条件（即充分性的额外要求）。

## 状态

- 提升引理：**[已证-纸面]**；
- $Z$ 构造引理：**[开放]**。
