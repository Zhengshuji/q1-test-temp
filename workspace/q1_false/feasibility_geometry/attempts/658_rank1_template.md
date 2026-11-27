# 658 秩一模板：$H=uv^{\mathsf T}$，$v\in S\cap\ker(Z'^{\mathsf T})$ 的构造

> 2026-11-27。按 ChatGPT 的建议，把 657 的构造抽象成秩一模板，并给出条件。
> 状态：**[已证-纸面]**。

## 模板

设 $v\in\mathbb C^k$ 满足
$$v^{\mathsf T}Z'=0\quad(\text{即 }Z'^{\mathsf T}v=0),\qquad v\in S .$$
取 $H=u v^{\mathsf T}$（$u\in\mathbb C^q$）。则：
$$HZ'=u\,(v^{\mathsf T}Z')=0,\qquad G=ZH=(Zu)\,v^{\mathsf T}.$$
$G$ 的行 $\in\operatorname{span}\{v\}\subseteq S$ ✓。

铅笔：
$$P(\lambda)=\lambda H-ZH=(\lambda u-Zu)\,v^{\mathsf T},$$
$$\operatorname{rank}P(\lambda)=1\ \forall\lambda\iff \lambda u-Zu\ne0\ \forall\lambda .$$
后者等价于：$Zu\ne0$ 且 $u$ 不是 $Z$ 的特征向量（若 $Zu=0$，$\lambda=0$ 时为零；若 $Zu=\mu u$，$\lambda=\mu$ 时为零）。

**取 $Z=e\,a^{\mathsf T}$**（秩一，$a\cdot u=1$）：$Zu=e$，只需 $e\notin\operatorname{span}\{u\}$ 且 $e\ne0$。

## 固定行

$H=uv^{\mathsf T}$ 的第 $i$ 行是 $u_i v^{\mathsf T}$；所以 $H_0$ 的各行必须都是 $v^{\mathsf T}$ 的倍数，
即
$$\operatorname{row}(H_0)\subseteq\operatorname{span}\{v\}\subseteq S\cap\ker(Z'^{\mathsf T}).$$

## 657 的实例

$k=2$、$Z'=\begin{bmatrix}0&0\\1&0\end{bmatrix}$、$S=\operatorname{span}\{e_1\}$、$v=e_1$：
$v^{\mathsf T}Z'=(0,0)$ ✓、$v\in S$ ✓；$u=(1,0,1)$、$Z=e_3e_1^{\mathsf T}$：$Zu=e_3\notin\operatorname{span}\{u\}$ ✓。
与 657 一致。

## 推广（待证）

秩 $d$：$H=\sum_{i=1}^d u_iv_i^{\mathsf T}$，要求 $v_i\in S$、$v_i^{\mathsf T}Z'=0$、$\operatorname{row}(H_0)\subseteq\operatorname{span}\{v_i\}$，
并让 $Z$ 在每个 $u_i$ 上产生外部耦合（$Zu_i\notin\operatorname{span}\{u_1,\dots,u_d\}$？）。
避让条件变为 $\operatorname{im}H\cap\ker(Z-\lambda I)=0$，需要更细的构造。

## 意义

- 给出一个**可构造的充分条件族**：若 $S\cap\ker(Z'^{\mathsf T})$ 足够大且包含 $H_0$ 的行空间，则可行；
- 解释了中间情形可行的一个来源；
- 与 651/655 的必要条件互补。

## 下一步

1. 证明秩 $d$ 模板的避让条件（选 $u_i$、$Z$）；
2. 检查 $S\cap\ker(Z'^{\mathsf T})$ 的维数与 $H_0$ 行空间的关系，写出可判定的充分条件；
3. 与 ChatGPT 核对秩 $d$ 推广。

## 状态

- 秩一模板：**[已证-纸面]**；
- 秩 $d$ 推广：**[开放]**。
