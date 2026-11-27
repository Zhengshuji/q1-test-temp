# 710 638 的 $d'=1$ 也不可行

> 2026-11-27。补上 638 的 $d'=1$ 情形：任意秩 1 的 $H$ 都不可行；结合 709，638 在正秩下完全不可行。
> 状态：**[已证-纸面]**。

## 设定

$H=u v^{\mathsf T}$（$u\in\mathbb C^3$、$v\in\mathbb C^3\setminus0$），$U=\operatorname{span}\{v\}$，$T=\operatorname{span}\{e_1\}$，$Z'$ 3-循环。
$P(\lambda)=(\lambda I-Z)H=(\lambda u-Zu)v^{\mathsf T}$，故 $\operatorname{rank}P(\lambda)=1$ 对所有 $\lambda$ $\iff$
$$\lambda u-Zu\ne0\quad\forall\lambda .$$

$(5a)$：$G=ZH-HZ'=(Zu)v^{\mathsf T}-u\,(v^{\mathsf T}Z')^{\mathsf T}$ 的行必须在 $T$；且相容性要求 $v^{\mathsf T}Z'\in U+T$。

## 分析

记 $w:=v^{\mathsf T}Z'$（行向量）。$Z'$ 循环，$v=(a,b,c)$ 时
$$w=(c,a,b).$$
相容性：$w\in\operatorname{span}\{v\}+T$。

**(1) $v\in T$**（$v=\lambda e_1$）：$w=\lambda e_2\notin T$ ⇒ 不相容。

**(2) $v\notin T$**：$w\in\operatorname{span}\{v\}+T$ ⇒ $w=\mu v+t$（$t\in T$）。
$G_i=(Zu)_i v^{\mathsf T}-u_i w^{\mathsf T}=((Zu)_i-\mu u_i)v^{\mathsf T}-u_i t^{\mathsf T}$ 必须在 $T$。
因 $v\notin T$，须 $(Zu)_i=\mu u_i$ 且 $u_i t=0$ 对所有 $i$。

- 若 $t\ne0$：$u_i=0$ 对所有 $i$ ⇒ $u=0$，矛盾；
- 若 $t=0$：$w=\mu v$，即 $v$ 是 $Z'^{\mathsf T}$ 的特征向量；此时 $Zu=\mu u$，故 $\lambda u-Zu=(\lambda-\mu)u$ 在 $\lambda=\mu$ 为零 ⇒ $(5b)$ 失败。

## 结论

$d'=1$ 不可行。结合 709（$d'=2$ 不可行）与 $d'=0$（$r_0=0$ 时 $L=0$ 可行，$q=0$）：

- 638 的**正秩解不存在**；
- $q_{\min}=0$（由 $r_0=0$ 的平凡解），故 638 不是 q1 意义上的难题实例，只是“正秩不可行”的结构例子。

## 意义

- 638 的正秩不可行性现在由 709（$d'=2$）与 710（$d'=1$）合起来完整；
- 它与 $\omega>s$ 无关（$\omega>s$ 由 661 保证）；
- 结构上，638 的 $Z'$ 循环与 $T=e_1$ 的组合使所有正秩候选都退化。

## 状态

- $d'=1$ 不可行：**[已证-纸面]**；
- 638 正秩不可行：**[已证-纸面]**；
- $q_{\min}=0$：**[已证-纸面]**（$r_0=0$）。
