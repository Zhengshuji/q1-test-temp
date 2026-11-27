# $c=2$ 分类修正：$\mathcal D_3$ 的幂零子型

> **55 号更正见 [attempts/134](134_55_corrections_exact_fibre.md)**（专家裁决）：
> $t=2$ 不同特征值的参数空间是 $\mathbb P(E_\lambda\cap K_0)\times\mathbb P(E_\mu\cap K_0)$，不是点；
> Jordan 链的仿射自由度是 $\dim(E_\lambda\cap K_0)-1$，不是 $\dim E_\lambda$；
> 不变的含义是 $A(W)\subseteq W$（含 $A(L)=0$），不是 $A(W)=W$；
> $t=1$ 子型 B 的精确条件是 $\operatorname{rank}[v,Av,A^2v]=3$，本文件的非空条件
> “$D\ne0$ 且 $A|_D$ 非标量”**被幂零 $J_2$ 反例推翻**。
>
> 2026-11-08。130 的反例说明 125 的“$\mathcal D_3$ = 含不变线”漏了 $AW\ne W$ 的子型。
> 本文件把 $c=2$ 的 $\mathcal D_3$ 分成 (a) 不变线、(b) 幂零 2-步，并修正非空条件与分量界。
> 状态：**M2（纸面）**。

## 目标

对 $c=2$、$V\in\operatorname{Gr}(2,K_0)$、$W=V\cap A^{-1}V$、$t=\dim W=1$（即 $\mathcal D_3$），
证明：

1. 两个子型：(a) $AW=W$（不变线）；(b) $AW\ne W$（幂零 2-步）；
2. 各自的非空条件（含 $K_0$ 截断）；
3. 修正后的分量界。

## 设想与理由

* $t=1$ 时 $W=L$ 是一条线，$A L\subseteq V$。
* 若 $A L=L$：$L$ 是不变线（125 的情形），$V=L\oplus\langle w\rangle$，$Aw=\alpha u+\beta w$；
  这是以特征线为底的丛。
* 若 $A L\ne L$：$A L$ 是 $V$ 中的另一条线（因为 $A L\subseteq V$、$\dim A L=1$），故 $V=L\oplus A L$；
  且 $A(A L)\notin V$（否则 $A L\in V\cap A^{-1}V=L$，矛盾）。这是**幂零 2-步**：
  $L\mapsto A L\mapsto A^2 L\notin V$。$V$ 由 $L$ 唯一决定：$V=L+A L$。
* 所以 $\mathcal D_3$ 的第二个子型是“$L$ 的像”，不是“$L$ 上的纤维”。

## 做法

### 1. 子型 (a)：$AW=W$（不变线）

$L=\langle u\rangle$、$Au=\lambda u$，$V=L\oplus\langle w\rangle$，$Aw=\alpha u+\beta w$。
固定 $L$，$w$ 的解空间模 $L$ 是以 $L$ 为底的丛（125 的 $J$ 型/线性条件）。
非空：$e_\lambda=\dim(E_\lambda\cap K_0)\ge1$（同 126）。

### 2. 子型 (b)：$AW\ne W$（幂零 2-步）

$L=\langle u\rangle$、$Au\notin L$，但 $Au\in K_0$（因为 $V\subset K_0$）。则
$$V=L\oplus\langle Au\rangle.$$
**$V$ 由 $L$ 唯一决定**。$L$ 的条件：
* $L\subseteq K_0$；
* $Au\in K_0$，即 $L\subseteq A^{-1}K_0$；
* $Au\notin L$，即 $L$ 不是 $A$ 的特征线。

所以 $L$ 跑遍
$$\mathbb P(D)\setminus\bigcup_\lambda\mathbb P(E_\lambda\cap D),\qquad D=K_0\cap A^{-1}K_0,$$
其中 $E_\lambda=\ker(A-\lambda I)$（特征线 locus）。这是**开集**（去掉有限个射影子空间），
故不可约；其像 $L\mapsto V=L+AL$ 是构造集，**一个分量**（若像的纤维有限；$\dim V=2$ 时
至多两个 $L$ 给出同一 $V$，故像是不可约的）。

**非空条件**：$D=K_0\cap A^{-1}K_0\ne0$，且 $A|_D$ **不是标量**（否则每条线都是特征线，
(b) 为空）。等价地：$\dim D\ge1$ 且 $A|_D$ 有非特征线。

### 3. 修正后的分量界

| 层 | 分量 | 数量 |
|---|---|---|
| $\mathcal D_2$ | 点（$\lambda\ne\mu$）| $\le\binom{s}{2}$ |
| $\mathcal D_2$ | $\operatorname{Gr}(2,E_\lambda)$ | $\le s$ |
| $\mathcal D_2$ | $J_\lambda$ | $\le s$ |
| $\mathcal D_3$ (a) | 每特征值一个（不变线）| $\le s$ |
| $\mathcal D_3$ (b) | 一个（幂零 2-步）| $\le1$ |
| $\mathcal D_4$ | 开 | $1$ |

$$\boxed{\#\le\binom{s}{2}+3s+2,}$$
只依赖 $s$（不同特征值个数）与 $A$ 在 $D$ 上的作用，**与 $k$ 无关**。

## 进展

* $\mathcal D_3$ 的两个子型已分开；反例 $J_4(0)$、$V=\langle e_2,e_3\rangle$ 落在 (b)。
* (b) 的非空条件是“$D\ne0$ 且 $A|_D$ 非标量”，是线性代数。
* 分量界从 $\binom{s}{2}+3s+1$ 修正为 $\binom{s}{2}+3s+2$（多一个 (b) 分量）。

## 最终结论

* $c=2$ 的 $\mathcal D_3$ 不是“含不变线”，而是两个子型：
  (a) 不变线丛；(b) 幂零 2-步 $V=L+AL$。
* (b) 的 $V$ 由 $L$ 唯一决定；分量是一个开集的像，不可约。
* 分量界 $\binom{s}{2}+3s+2$；所有非空条件都是线性代数（$e_\lambda$、$D$、$A|_D$）。
* 这修正了 125/126 的“不变线”过度简化。

## 放弃原因

* (b) 的像的纤维数（$L\mapsto V$ 的有限性）只做了粗略论证（$\dim V=2$ 时至多两个 $L$）；
* (b) 与 (a) 在边界（$A L=L$）的闭包关系未细究；
* $K_0$ 截断在 $m_0=2$ 的精确情形未重写；
* 没有实例验证。

## 残留价值

* $c=2$ 的**正确**分类（$\mathcal D_3$ 两子型），可直接替换 125/126 的相应段落。
* 幂零 2-步的结构（$V=L+AL$，$L$ 开集）是 130 的“型控制”在 $c=2$ 的具体化。
* 分量界与线性代数非空条件，为 $c=2$ 算法（127）提供正确输入。

## 相关文件

* [attempts/130](../../decision_algorithms/attempts/130_general_induction_map_type.md)（型控制；反例）
* [attempts/125](125_c2_structure_complete.md)（$c=2$ 分类；本文件修正 $\mathcal D_3$）
* [attempts/126](126_c2_k0_truncation.md)（非空条件；本文件补 (b)）
* [attempts/127](../../decision_algorithms/attempts/127_c2_algorithm.md)（$c=2$ 算法）

## 状态

* $\mathcal D_3$ 两子型：**[已证-纸面，M2]**。
* (b) 的非空条件：**[已证-纸面]**（$D\ne0$ 且 $A|_D$ 非标量）。
* 分量界：**[已证-纸面]**（$\binom{s}{2}+3s+2$，粗界）。
* 未做：像的纤维数、边界闭包、$m_0=2$ 精确、实例验证。
