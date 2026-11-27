# 693 $t<s$ 的实例：690 的 $t$-版本是紧的

> 2026-11-27。构造 $t=\dim T<\dim S=s$ 的数据，验证 692 的更正：$d'\le t$ 是真正的上界；同一数据下 $H_0$ 的方向决定可行/不可行。
> 状态：**[已证-纸面]** + **[精确验证]**（$K_0,T,S$）。

## 数据

$n=4$、$k=2$、$N$ 前 2 坐标嵌入，
$$A e_1=e_3,\quad A e_2=e_1,\quad A e_3=e_4,\quad A e_4=0,\qquad C=e_4^{\mathsf T}.$$
sympy 验证：$K_0=\operatorname{span}\{e_1,e_2\}$（$N$ 正确），
$$W=AN=\begin{bmatrix}0&1\\0&0\\1&0\\0&0\end{bmatrix},\qquad
S=\operatorname{span}\{e_1,e_2\}\ (s=2),\qquad T=\operatorname{span}\{e_1\}\ (t=1).$$
$Z'=0$（标量，$\mu=0$、$\operatorname{rank}(0I-Z')=0$）。

## 690 的 $t$-版本

可行 ⇒ $0=\operatorname{rank}(0I-Z')\ge d'-t=d'-1$ ⇒
$$\boxed{d'\le1 .}$$

## $H_0=e_2^{\mathsf T}$：不可行（任何 $q$）

$d'=0$ 不可能（$H_0\ne0$）；$d'=2$ 被 690 排除。若 $d'=1$：$H$ 的行空间 $\ni e_2$，故 $U=\operatorname{span}\{e_2\}$。
$(5a)$ 要求 $G_i\in U$（$Z'=0$），而 $G_i\in T=\operatorname{span}\{e_1\}$，故
$$G_i\in\operatorname{span}\{e_1\}\cap\operatorname{span}\{e_2\}=0\ \Rightarrow\ G=0 .$$
于是 $P(\lambda)=\lambda H$，在 $\lambda=0$ 处秩 0 $<1$ ⇒ 失败。故**该数据对任何 $q$ 都不可行**。

## $H_0=e_1^{\mathsf T}$：可行（$d'=1$）

取 $H=u e_1^{\mathsf T}$（$u_1=1$）、$Z=-I$：$G=ZH-HZ'=-H=-u e_1^{\mathsf T}$，行在 $T=\operatorname{span}\{e_1\}$ ✓。
$P(\lambda)=\lambda H-ZH=(\lambda+1)H$，秩 1 对一切 $\lambda$ ✓。故可行。

## 意义

- 690 的 $t$-版本（而非 $s$-版本）是正确且**紧的**：$t=1$ 时 $d'=2$ 确实不可行；
- 同一数据、同一 $Z'$，$H_0$ 的方向决定可行/不可行，说明固定行约束与 $T\cap U$ 的交互是关键；
- 这是第一个 $t<s$ 的显式实例，验证 692 的更正不是形式上的。

## 与 692 的关系

692 指出 $G$ 的行空间是 $T$；本例中 $T=\operatorname{span}\{e_1\}\subsetneq S=\operatorname{span}\{e_1,e_2\}$，若误用 $S$ 会得到错误的“$d'=2$ 可能可行”结论。

## 待办

1. 用本例检验 678/682 的 $T$-版本实现；
2. 研究 $H_0$ 方向与 $T\cap U$ 的一般交互（可能是新的预筛选条件）；
3. 与 ChatGPT 讨论这个 $t<s$ 例子的意义。

## 状态

- 数据与 $t<s$：**[精确验证]**；
- 不可行/可行证明：**[已证-纸面]**。
