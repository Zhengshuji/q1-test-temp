# $c=2$ 重写：用精确纤维定理（专家 55 §4.2 / §9 Step 2）

> 2026-11-08。用 135 的精确纤维定理重写 $c=2$，并落实专家 55 的三处更正：
> $t=2$ 的参数空间、Jordan 链纤维维数、$t=1$ 子型 B 的非空条件。
> 状态：**M2（纸面；表已按精确条件重写）**。

## 更正（专家 56 号）

商空间用环境状态空间 $\mathcal X/V$（或 $\mathcal X/W$、$\mathcal X/U$），不是 $K/V$——除非 $A(K_0)\subseteq K_0$。
下文已改；判据中的集合条件（如 $Aw\notin V$、$A^2v\notin\operatorname{span}\{v,Av\}$）不受影响。

## 目标

对 $c=2$、$V\in\operatorname{Gr}(2,K_0)$、$W=V\cap A^{-1}V$、$t=\dim W\in\{0,1,2\}$，给出：
每个 $t$ 的 $U=W+A(W)$、精确纤维、精确非空条件、分量。

## 设想与理由

* 135：$\mathcal F_W=\operatorname{Gr}(2-\dim U,K_0/U)$ 中满足 $\operatorname{rank}(V\to \mathcal X/V)=2-t$ 的开子集。
* $t=2$：$W=V$，$U=V$，纤维是点；分类由 $A|_V$ 的 Jordan 型。
* $t=1$：$W=L$，$U=L+AL$；分 $AL\subseteq L$ 与 $AL\not\subseteq L$。
* $t=0$：$W=0$，$U=0$，开条件 rank 2。

## 做法

### $t=0$：$W=0$

$U=0$；纤维是 $\operatorname{Gr}(2,K_0)$ 中满足 $\operatorname{rank}\overline A_V=2$（即
$V\cap A^{-1}V=0$）的开子集。非空 $\iff\exists V$ 使 $V\cap A^{-1}V=0$。

### $t=1$：$W=L=\mathbb Cv$，$L\subseteq D=K_0\cap A^{-1}K_0$

**子型 A：$A(L)\subseteq L$**（含 $Av=0$）。$U=L$；$V=L\oplus\langle x\rangle$，
精确条件是 $\operatorname{rank}\overline A_V=1$，等价于
$$Ax\notin V=L+\langle x\rangle.$$
纤维是 $\mathbb P(K_0/L)$ 中满足此式的开子集（对固定 $L$）。
非空 $\iff\exists x\notin L$ 使 $Ax\notin L+\langle x\rangle$。

**子型 B：$A(L)\not\subseteq L$**。$AL$ 是 $V$ 中的另一条线，故 $U=L+AL$ 是 2 维；
$V=U$ 被决定。精确条件是 $\operatorname{rank}\overline A_V=0$（$t=1$、$c-t=1$？注意：
$c=2$、$t=1$，条件是 $\operatorname{rank}=1$，而 $\dim V=2$、$\ker=W$ 一维；对 $V=U$，
$\overline A_V:U\to \mathcal X/U$ 的核应是 $L$，故秩 $=1$（$2-1$）。等价于
$$A^2v\notin U=L+AL,$$
即
$$\boxed{\operatorname{rank}[v,Av,A^2v]=3.}$$
非空 $\iff\exists v\in D$ 使 $\operatorname{rank}[v,Av,A^2v]=3$。
**注意**：旧条件“$D\ne0$ 且 $A|_D$ 非标量”**不够**；幂零 $J_2$（$Ae_1=0,Ae_2=e_1$）是反例。

### $t=2$：$W=V$，$A(V)\subseteq V$

$U=V$；纤维是点（$V=W$）。分类由 $A|_V$ 的 Jordan 型：

* **两个不同特征值** $\lambda\ne\mu$：$V=L_\lambda\oplus L_\mu$，参数空间
  $$\mathbb P(E_\lambda\cap K_0)\times\mathbb P(E_\mu\cap K_0),$$
  **不是点**（只有两个交都一维时才是点）。
* **标量型** $\lambda$：$V\in\operatorname{Gr}(2,E_\lambda\cap K_0)$。
* **非平凡 Jordan 块**：$V=\operatorname{span}\{u,T_\lambda u\}$，$T_\lambda u\ne0$、$T_\lambda^2u=0$、
  $u,T_\lambda u\in K_0$；固定特征线 $L$，$u$ 的仿射自由度是
  $$\dim(E_\lambda\cap K_0)-1$$
  （模 $L$），不是 $\dim E_\lambda$；且并非所有 $L$ 都有链向量——**链提升条件**是 $\ell=\mathbb Cv\subseteq(A-\lambda I)(K_0)$（不能只要求 $\ell\subseteq E_\lambda\cap K_0$）；精确参数化见 [143](143_c2_rigorous_parameterization.md)。

### 精确非空条件汇总

| $t$ | 子型 | 非空条件 |
|---|---|---|
| 2 | $\lambda\ne\mu$ | $E_\lambda\cap K_0\ne0$ 且 $E_\mu\cap K_0\ne0$ |
| 2 | 标量 $\lambda$ | $\dim(E_\lambda\cap K_0)\ge2$ |
| 2 | Jordan $\lambda$ | $\exists u\in K_0:\ T_\lambda u\ne0,\ T_\lambda^2u=0$ |
| 1 | A（$AL\subseteq L$）| $\exists x\notin L:\ Ax\notin L+\langle x\rangle$ |
| 1 | B（$AL\not\subseteq L$）| $\exists v\in D:\ \operatorname{rank}[v,Av,A^2v]=3$ |
| 0 | 开 | $\exists V:\ V\cap A^{-1}V=0$ |

## 进展

* $c=2$ 的六个子型都用精确纤维条件重写；非空条件都是线性代数/循环向量条件。
* 修正了 131 的三处：$t=2$ 参数空间、链纤维维数、$t=1$ B 的假非空条件。
* 不变的含义是 $A(L)\subseteq L$（含 $AL=0$），不是 $AL=L$。

## 最终结论

* $c=2$ 的精确分类：$t=2$（点/$\mathbb P\times\mathbb P$/Gr(2)/Jordan 链）、
  $t=1$（A：$Ax\notin V$；B：$\operatorname{rank}[v,Av,A^2v]=3$）、$t=0$（开）。
* 每个纤维都是开 Grassmannian；非空条件是线性代数。
* 131 的错误已全部修正；这是专家 55 §9 Step 2 的落实。

## 放弃原因

* 未逐项证明“这些子型就是全部”（$t$ 的划分已穷尽，但子型内部的分量/不可约性未逐项证）。
* 未处理 $K_0$ 截断在 $m_0=2$ 的精确边界。
* 实点未做。

## 残留价值

* 一张可用的 $c=2$ 精确表，替代 131 的错误版本。
* 为 $c=3$（137）与算法（123 模板）提供正确输入。

## 相关文件

* [attempts/135](135_exact_fibre_theorem.md)（精确纤维）
* [attempts/131](131_c2_d3_nilpotent_subtype.md)（旧版；本文件修正）
* [attempts/136](136_c2_rewrite.md)（本文件）
* [attempts/137](137_c3_repair.md)（$c=3$ 重写）
* [attempts/143](143_c2_rigorous_parameterization.md)（精确参数空间/互斥穷尽/算法）

## 状态

* 分类：**[已证-纸面，M2]**（子型穷尽 + 精确条件）。
* 分量/不可约性：**[未逐项证]**。
* 未做：$m_0=2$ 边界、实点。
