# $c=1,2,3$ 的区别，以及“型控制归纳”为什么不可行

> 2026-11-08。回答两个问题：(1) $c=1,2,3$ 的几何/参数空间到底差在哪；
> (2) 之前试图按 $c$ 归纳（型控制定理，attempts 129–133）为什么走不通。
> 状态：**M2（结构说明；含实现中发现的 $W_L$ 更正）**。

## 目标

把 $c=1$（超平面）、$c=2$、$c=3$ 的**可容许 locus**、**参数空间**、**分量/可行性**放在同一框架下比较，
并说明归纳失败的具体环节。

## 设想与理由

统一设定：$V=\ker H$（$\dim c$），$H=LN_K$，$H_A=LAN_K$，顶部 $r$ 行固定为 $L_0N$、$L_0AN$。
可容许 $V$ 必须满足
$$V\subseteq W_L:=\ker[L_0N_K;\ L_0AN_K]$$
（因为 $H$ 与 $H_A$ 的顶部行都湮灭 $V$，且 $\ker H\subseteq\ker H_A$）。这是实现 $c=2$ 算法时发现的
关键约束：**$V$ 不在 $\operatorname{Gr}(c,K_0)$ 里自由，而在 $\operatorname{Gr}(c,W_L)$ 里**。
$\dim W_L\ge k-\operatorname{rank}[L_0N;L_0AN]\ge k-2r$。

## 做法

### $c=1$：射影直线上的特征向量分类

$k=\omega+1$，$V=\ell$ 是 $W_L$ 中的一条线，底空间
$$\mathbb P(W_L),\qquad \dim W_L\ge k-2r.$$
对 $v=N\sigma$，约束是线性的 $Rv=0,Rav=0$；$\rho(v)=\operatorname{rank}[v,Av]\in\{1,2\}$，
$\rho=1\iff v$ 是 $A$ 的特征向量。分量：
$$\mathcal B_1=\bigcup_\lambda\mathbb P(W_L\cap\ker(A-\lambda I)),\qquad
\mathcal B_2=\mathbb P(W_L)\setminus\mathcal B_1.$$
每个特征子空间不可约、不同特征值不交；$\mathcal B_2$ 是开集。故分量 $\le\delta+1$（$\delta=\dim\ker T$），
每分量是向量丛的开子集；秩恒等式
$\operatorname{rank}[P;Q]+(2-\operatorname{rank}[v,Av])=\delta$。
**$c=1$ 的本质**：$V$ 是一条线，Jordan 型只有“特征/非特征”，分类是射影的、离散的。

### $c=2$：$W_L$ 中的 2-平面与六层

$k=\omega+2$，$V$ 是 $W_L$ 中的 2-平面，底空间
$$\operatorname{Gr}(2,W_L),\qquad \dim W_L\ge k-2r.$$
在 $r=1$ 时 $\dim W_L\ge\omega$；**当 $\omega=2$（seeds 10/16/21）时 $\dim W_L=2$，$V$ 被唯一确定**；
当 $\omega\ge3$ 时 $V$ 在 $\operatorname{Gr}(2,\omega)$ 中有连续族。
分类按 $t=\dim(V\cap A^{-1}V)$ 与 $A|_V$ 的 Jordan 型（$t=2$ 时）：
六层（不同特征值 / 标量 / Jordan 链；$t=1$ 的不变线 / 非不变线；$t=0$ 开）。
分量界（对参数空间）$\le\binom{s}{2}+3s+2$，但**必须先在 $\operatorname{Gr}(2,W_L)$ 里数**；
$W_L$ 限制会减小参数空间，也可能改变非空性。
**$c=2$ 的本质**：2 维 Jordan 型有限（3 种），但 $t=1$ 的“线 + 追加方向”和 $t=2$ 的链提升
引入了连续参数（$x$、链的提升），且 $V$ 只在 $W_L$ 中。

### $c=3$：$W_L$ 中的 3-平面与十一层

$k=\omega+3$，$V$ 是 $W_L$ 中的 3-平面，底空间 $\operatorname{Gr}(3,W_L)$。
分类按 $t=0,1,2,3$ 与 $A|_V$ 的 Jordan 型：十一层（$t=3$ 六种：不同特征值、$1+1+1$、$1+1$+$\mu$、
$2+1$、$2$+$\mu$、$3$；$t=2$ 两种；$t=1$ 两种；$t=0$ 一种）。
$t=2$ 的 $S_{2,3}=\{W\in\operatorname{Gr}(2,D):\dim(W+A_0(W))=3\}$ 是 exact-rank 确定性子层，
**可能可约**；$t=3$ 的六种 Jordan 型也各自需要不可约性证明。
**$c=3$ 的本质**：3 维 Jordan 型有 6 种（含不同特征值的混合），且 $t=2$ 的确定性子层不再是
“Grassmannian/射影空间”这种显然不可约的对象；分量界**未证**。

### 三者的区别（一张表）

| | $c=1$ | $c=2$ | $c=3$ |
|---|---|---|---|
| $V$ | 线 | 2-平面 | 3-平面 |
| 底 | $\mathbb P(W_L)$ | $\operatorname{Gr}(2,W_L)$ | $\operatorname{Gr}(3,W_L)$ |
| 类型 | 特征/非特征 | 3 种 Jordan 型 + $t=1$ 二分 | 6 种 Jordan 型 + $t=2,1$ 子型 |
| 额外连续参数 | 无（$\rho$ 离散） | $x$、链提升 | $x$、2-平面扩张、链 |
| 分量 | $\le\delta+1$（已证） | $\binom{s}{2}+3s+2$（需不可约性证明） | 未证（$S_{2,3}$ 可能可约） |
| 可行性 | 向量丛 + 开条件 | 提升 $d'_C(V)$ + gcd | 未定 |

## 为什么“按 $c$ 归纳”（型控制）走不通

1. **$W_L$ 约束被漏掉**：归纳假设 $V$ 在 $\operatorname{Gr}(c,K_0)$ 自由，但 $V$ 实际在
   $\operatorname{Gr}(c,W_L)$ 内；$c=2,\omega=2$ 时 $V$ 甚至唯一。参数空间、非空性、分量数
   都必须在 $W_L$ 内重算，不能从 $c-1$ 的 $\operatorname{Gr}(c-1,K_0)$ 递归。
2. **$A|_V$ 的 Jordan 型在 $V$ 不不变时无定义**：$t<c$ 时 $A(V)\not\subseteq V$，$A|_V$ 不是自同态；
   正确对象是 $A|_V:V\to\mathcal X/V$（或 Kronecker 型 $(\iota|_W,A|_W)$），它不按 $c$ 递归。
   （这正是 129/130 的反例纠正过的点。）
3. **扩张 $V/W$ 的连续数据不被 $W$-型控制**：$t=1$ 的 $x$、$t=2$ 的链提升、以及提升 $L$ 的
   off-$K_0$ 分量，都是独立的仿射参数；型控制猜想断言它们由型决定，但提升定理（152）表明
   它们是另一个仿射空间（$d'_C(V)$），不由 $W$-型决定。
4. **确定性子层不自动不可约**：$S_{t,u}$ 是 exact-rank 层，可能可约（Springer 纤维、不变子空间簇
   是标准反例家族）；归纳要求“每层不可约”，这一步在 $c\ge3$ 不成立（或未证）。
5. **好性（谱条件）是额外的开条件**：即使分量数有限，每个分量内 good locus 是否非空、
   是否稠密，仍是独立问题；分量数不推出可行性算法。

**结论**：不能按 $c$ 做“型控制归纳”。可替代的路线是：
(a) 先把 $V$ 限制到 $W_L$（本文件）；
(b) 在 $\operatorname{Gr}(c,W_L)$ 内逐层分类（143/146）；
(c) 用提升定理（152）处理连续自由度；
(d) 只在能证不可约性的层上给分量界（147 的 $c=2$；$c=3$ 暂停）；
(e) 可行性用“枚举层 + 解提升仿射方程 + gcd”，不依赖分量枚举。

## 进展

* $c=1/2/3$ 的统一比较表已写出；
* $W_L$ 约束与“$V$ 被唯一确定”的典型情形（$\omega=2$）已指出；
* 归纳失败的五个具体环节已定位。

## 最终结论

* $c=1$ 是射影分类，$c=2$ 是 Grassmannian 上的有限层，$c=3$ 出现可约的确定性子层；
* 归纳失败不是因为“算得不够”，而是因为 $W_L$、扩张连续参数、确定性子层可约性、好性开条件
  这四件事都不按 $c$ 递归。

## 放弃原因

* 未对 $\operatorname{Gr}(c,W_L)$ 重做 147/148 的分量界（需逐层不可约性）；
* 实点/算法未做。

## 残留价值

* 明确了 $c=1/2/3$ 的结构差异与归纳失败的根因；
* 为“先算 $W_L$、再分类、再提升”的算法路线提供依据。

## 相关文件

* [attempts/121](121_hyperplane_vector_bundle.md)（$c=1$）
* [attempts/143](143_c2_rigorous_parameterization.md)、[147](147_c2_component_bound.md)（$c=2$）
* [attempts/146](146_c3_rigorous_parameterization.md)、[148](148_c3_component_bound.md)（$c=3$）
* [attempts/152](152_lift_completion_fixed_l0.md)（提升）

## 状态

* 结构说明/归纳失败的定位：**[已证-纸面，M2]**。
* $W_L$ 内的分量界/算法：**[未做]**。
