# 715 $d'=1$：可行 $\Rightarrow U\subseteq T$

> 2026-11-27。把 710 的论证抽象为 $d'=1$ 的一般必要条件：秩一的可行解必须满足 $v\in T$（即 $T\cap U=U$）。
> 状态：**[已证-纸面]**。

## 定理

设 $d'=1$、$H=uv^{\mathsf T}$、$U=\operatorname{span}\{v\}$、$T=\{lW:lN=0\}$。若可行，则
$$\boxed{v\in T\quad(\text{即 }U\subseteq T).}$$

**证明**：记 $w=v^{\mathsf T}Z'$。相容性要求 $w\in U+T$（$H_iZ'=u_iw\in U+T$）。

若 $v\notin T$，则 $w=\mu v+t$（$t\in T$）。又 $G=ZH-HZ'=(Zu)v^{\mathsf T}-u\,w^{\mathsf T}$，其第 $i$ 行
$$G_i=\big((Zu)_i-\mu u_i\big)v^{\mathsf T}-u_i t^{\mathsf T}\in T .$$
因 $v\notin T$：若 $u_i\ne0$，$v^{\mathsf T}$ 系数必须为零 ⇒ $(Zu)_i=\mu u_i$；若 $u_i=0$，同一条件给 $(Zu)_i=0=\mu u_i$。故 $Zu=\mu u$，于是
$$P(\mu)=(\mu u-Zu)v^{\mathsf T}=0,$$
与 $(5b)$ 矛盾。故 $v\in T$。$\square$

## 推论

- $d'=1$ 时，$T\cap U=0$（即 $v\notin T$）⇒ 不可行；
- 693 的 \(d'=1\) 可行解正是 $v=e_1\in T$；
- 657 的 $v=e_1\in T$ 也满足。

## 与 $d'\ge2$ 的关系

- $d'=1$ 的证明依赖“$v\notin T$ 时系数必须为零”；
- $d'\ge2$ 时 $U$ 可能部分落在 $T$ 内、部分在外（$0<\dim(T\cap U)<d'$），需要更细的分解；
- 638 的 $d'=2$ 不可行证明（709）走的是另一条路（$U\cap T=0$ 时的投影唯一性）。

## 待办

1. $d'\ge2$ 时，$\dim(T\cap U)$ 的精确作用；
2. 是否可行 ⇒ $U\subseteq T+\ker$ 某物？
3. 与 714（$Z'=0$）合并成“方向性必要条件”的一般形式。

## 状态

- 定理：**[已证-纸面]**；
- $d'=1$ 的方向条件：**[成立]**；
- $d'\ge2$：**[开放]**。
