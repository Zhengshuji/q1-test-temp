> **补（245）**：$\omega\le1$ 时门也退化（$x=0$），所以 $q=2,u=0$ 整体不可能；
> 本文件的 $\omega=2$ 是其中一半。

# $q=2$ 的完整门：$\\omega=2$ 不可能；最小单行列式 rank-4 是 $n=7,p=2$

> 2026-11-09。续 242。构造出第一个满足完整 $(5a)$、$D=xy-zw$（rank 4、signature $(2,2)$）的
> $q=2$ 实例（$n=7,p=2$）；但证明它的 $(5b)$ 恒失败，且这是**一般现象**：
> $u=0$ 时 $H_A$ 的 $L_0$ 行是 $H$ 的 $L_0$ 行的倍数，所以 $P(\\alpha)$ 第一行零；
> $\\omega=2$ 时 $(5b)$ 必然失败。$\\omega=1$ 是唯一可能的例外（门是否退化需另判）。
> 状态：**M2（纸面）+ 精确实例**。

## 目标

在完整 $(5a)$ 下构造 rank-4 门，并判定 $(5b)$。

## 设想与理由

242 的 $n=5$ rank≤3；$n=6,p=1$ 时 $Q$ 维 3（三个方程）。要单行列式 + rank4，
需要 $Q$ 维 2 且 $\\dim W=n-p-1\\ge4$；这给出 $n\\ge p+5$，而 $Q$ 维 2 要求
$n-2\\le 2p+1$，合并得 $p\\ge2$；最小是 **$n=7,p=2$**。

## 做法：$n=7,p=2,q=2$ 的显式构造

取 $C=e_5^*,e_6^*$、$L_0=e_7^*$，$A$ 满足
$$\\operatorname{col}_1=e_3,\\quad \\operatorname{col}_2=e_4,\\quad
\\operatorname{row}_5=e_3,\\quad \\operatorname{row}_6=e_4,\\quad \\operatorname{row}_7=0.$$
则
$$CA=\\begin{bmatrix}e_3\\\\e_4\\end{bmatrix},\\quad L_0A=0,\\quad
S=\\operatorname{row}[L_0;CA;C]=\\operatorname{span}\\{e_3,e_4,e_5,e_6,e_7\\},$$
$\\operatorname{rank}S=5$，$Q=(\\mathbb C^7)^*/S$ 维 2，坐标 $(l_1,l_2)$。
$L=[L_0;l]$，$l=(l_1,\\dots,l_7)$：
$$x=[l]=(l_1,l_2),\\qquad v=[lA]=(l_3,l_4),$$
所以
$$\\boxed{(5a)\\iff l_1l_4-l_2l_3=0.}$$
这是**完整** $(5a)$（$L_0A=0$ 已自动），不是漏行版本；$D=l_1l_4-l_2l_3$ 是 rank 4、
signature $(2,2)$ 的双曲形式（$x=l_1,y=l_4,z=l_2,w=l_3$）。

## $(5b)$：一般性失败

$K_0=\\ker[C;CA]=\\operatorname{span}\\{e_1,e_2,e_7\\}$，$N$ 取这三列：
$$H=LN=\\begin{bmatrix}0&0&1\\\\ l_1&l_2&l_7\\end{bmatrix},\\qquad
H_A=LAN=\\begin{bmatrix}0&0&0\\\\ l_3&l_4&(lA)_7\\end{bmatrix}.$$
在 $\\lambda=0$：
$$P(0)=-H_A=\\begin{bmatrix}0&0&0\\\\ -l_3&-l_4&-(lA)_7\\end{bmatrix},$$
$\\operatorname{rank}P(0)\\le1<2=\\operatorname{rank}H$（对一般 $l$）。所以 $(5b)$ 失败。

### 一般引理

$u=0$ 即 $L_0A\\in S=\\operatorname{row}[L_0;CA;C]$，故
$$L_0A=\\alpha L_0+\\beta CA+\\gamma C.$$
右乘 $N$（$N$ 的列张成 $\\ker[C;CA]$）：
$$H_A\\text{ 的第一行}=L_0AN=\\alpha L_0N=\\alpha\\,H\\text{ 的第一行}.$$
于是
$$P(\\alpha)\\text{ 的第一行}=(\\alpha H_1-H_{A,1})=0.$$
所以
$$\\boxed{\\omega=2\\ \\Rightarrow\\ \\operatorname{rank}P(\\alpha)\\le1<2\\ \\Rightarrow\\ (5b)\\text{ 失败}.}$$

**结论**：$q=2$、$u=0$、$\\omega=2$ 不可能同时满足 $(5a)$ 与 $(5b)$。
$\\omega=1$ 是唯一例外：此时第一行消失后，第二行仍可给 rank 1；但 $(5b)$ 要求整个铅笔秩恒 1
（两行对所有 $\\lambda$ 成比例），门是否退化需单独判定。

## 进展

* 第一个完整的 $q=2$ rank-4 门（$n=7,p=2$，$D=xy-zw$）；
* 证明 $\\omega=2$ 时 $(5b)$ 恒失败（一般引理）；
* 修正 242 的“最小 $n=6$”：单行列式 rank-4 的最小是 **$n=7,p=2$**；
  $n=6,p=1$ 时 $Q$ 维 3，是三方程。

## 最终结论

* $q=2$ 的 rank-4 门在 $\\omega=2$ 下**不可行**；
* 若 $q=2$ 还有希望，只剩 $\\omega=1$（强限制，门可能退化）；
* 自然的下一步是 **$q=3$**：$P(\\alpha)$ 第一行消失后，另外两行仍可给 rank 2，
  $(5b)$ 有可能成立。

## 放弃原因

* 未构造 $\\omega=1$ 的可行门；
* 未做 $q=3$；
* 未接谱守卫/边界。

## 残留价值

* 完整的 rank-4 门实例（可用于测试 $q\\ge3$ 扩展）；
* $H_A$ 第一行成比例的引理（对所有 $q=2$、$u=0$ 成立）；
* 最小维度 $n=7,p=2$。

## 相关文件

* [attempts/242](242_rank4_n5_impossible.md)
* [73 答复](../../../for_expert/archive/73_inventory_and_route-answer.md)
* `tools/verification/c243_q2_no_go.py`（已跑，PASS：signature (2,2)，P(alpha) rank 1）

## 状态

* $q=2,\\omega=2$ 不可能：**[M2 纸面]**。
* $q=3$：**[进行中]**。
