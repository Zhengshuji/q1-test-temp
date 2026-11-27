# 332 为什么特征纤维逃得掉：强制关系 $\iff C\in\operatorname{row}L$

> 承接 329（非特征层因强制关系全坏）、330/331（特征纤维生成好）。
> 本文件给出两支差异的**结构原因**，并把 H4 的本族版本压缩成一个"构造一个好行空间"的问题。

## 目标

解释 329 与 330 的不对称：为什么非特征层被强制关系杀死，特征纤维却能生成好？

## 设想与理由

329 的强制关系是：若 $c\in\operatorname{row}L$ 且 $c$ 消去 $\hat N$ 与 $A\hat N$，则
$c(\lambda I-A)\hat N\equiv0$，商铅笔掉一行。而 $C$ 的每一行都消去 $K_0$ 与 $AK_0$（因为 $K_0=\ker[C;CA]$），
所以

$$\text{强制关系}\iff C\ \text{的某行}\in\operatorname{row}L .$$

能不能发生，取决于 $\operatorname{row}L$ 有多少空间：$\operatorname{row}L\subseteq U^\perp$，而 $\dim U^\perp=n-\dim U$。

## 做法

| | 非特征 $v$ | 特征 $v$ |
|---|---|---|
| $\dim U$ | $2$ | $1$ |
| $\dim U^\perp$ | $n-2$ | $n-1$ |
| 本族（$n=5$） | $3$ | $4$ |
| 层里 $\operatorname{row}L$ 的维数 | $q=3$ | $q=3$ |
| 结果 | $\operatorname{row}L=U^\perp$（**被迫取满**）⟹ $C\in\operatorname{row}L$ ⟹ **强制关系** | $\operatorname{row}L$ 是 $U^\perp$ 里的**超平面**，一般**避开** $C$ ⟹ 无强制关系 |

**命题（机制）.** 设 $\dim U^\perp=q$（非特征、本族即如此）。则层里 $\operatorname{row}L=U^\perp$，
于是 $C\in\operatorname{row}L$，强制关系成立，$\operatorname{rank}\widetilde M\le n-2-p$。

**推论.** 只要 $\dim U^\perp>q$（特征、本族即如此），就可以选 $\operatorname{row}L\not\ni C$，强制关系消失。

## 进展

- 两支差异的**结构原因**已定位：不是"特征与否"本身，而是 $\dim U^\perp$ 与 $q$ 的**大小关系**——
  相等则被迫取满、必含 $C$；严格大则能避开。
- 所以"特征纤维生成好"不是一个关于特征向量的神秘性质，而是**有足够自由度避开 $C$**。
- 但"避开 $C$"只排除了 329 的那**一条**坏机制，不直接给出 $\gcd=1$。
  要证生成好，仍需**给一个显式好行空间**——330 的做法，配 322 的闭性。

## 最终结论

1. 329 与 330 的不对称有干净的结构解释（$\dim U^\perp$ 与 $q$ 的比较）。
2. H4 的本族版本因此归结为：**在 $U^\perp$（$\dim>q$）里构造一个行空间使 $\gcd=1$**。
   我们已经能"找到"（采样即中，33/40），但还没有**构造**——这是唯一剩下的缺口。
3. 这也解释了为什么 324 的分量结构里 $F_\lambda$ 与 $Z^\circ$ 性质不同：它们的行空间维数不同。

## 放弃原因

- 没有给出"构造一个好行空间"的显式公式（只有随机命中）；
- 只处理 $\dim U^\perp\ge q$ 的本族情形；$q>\dim U^\perp$ 时层本身可能不存在；
- 没有把"避开 $C$"与"$\gcd=1$"之间的充分条件补上（需要额外论证）。

## 残留价值

- 一条解释性命题（强制关系 $\iff C\in\operatorname{row}L$）及其推论，把 H4 的本族版本压成一个具体构造问题；
- 修正了"特征纤维好是因为特征性"的直觉：真正的原因是**自由度**；
- 为其它维度模式提供判据：先算 $\dim U^\perp$ 与 $q$ 的比较，再谈层的可行性。

## 相关文件

- [attempts/329](329_forced_relations_quotient_pencil.md)（强制关系）
- [attempts/330](330_eigen_fibre_feasibility.md)（一个好点即证）
- [attempts/331](331_eigenvector_criterion.md)（本族判据）
- [attempts/324](324_hyperplane_component_theorem.md)（分量）

## 状态

- 机制命题：**[已证-纸面]**（$\dim U^\perp=q\Rightarrow\operatorname{row}L=U^\perp$）。
- "构造好行空间"：**[未做]**（只有随机命中）。
