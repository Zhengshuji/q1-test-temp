# 中间层（$\delta=1$）**可行**的显式证书

> **对应 docs 条目**：B.31（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

## 陈述

存在 $p=r=2$、$n=6$、$r_1=4$ 的实例、阶 $q=3$（代数最小阶 $q_0=2$）与可容许 $\mathcal L$，使得

* $(5a)$ 成立；
* $\operatorname{rank}[C;\mathcal L]=p+q=5$、$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$；
* $\delta(\mathcal V)=1$（**中间层**：$1\le\delta<r_1-p=2$）；
* **$(5b)$ 成立**（即该候选**可行**）。

## 为什么这条重要

由 **B.22**（等号障碍）与 **B.28(3)**（不变子空间排除），两个**边界层**永远不可行：

$$\delta=r_1-p\ \Longrightarrow\ \text{失败};\qquad \delta=0\ \Longrightarrow\ \text{失败}\ (\text{当 } q+p<n).$$

**B.31** 把它们合成一个统一必要条件：

$$(5b)\ \text{成立},\ q+p<n\ \Longrightarrow\ 1\le\delta(\mathcal V)<r_1-p .$$

本证书证明该条件**不是空的**：中间层确实有可行候选。于是

$$\boxed{\text{可行性恰好住在中间层}}$$

（两个边界层绝不可行已证；中间层非空且可行由本证书给出。）

## 证书数据

$n=6$，$p=r=2$，$q=3$，$q_0=2$，$r_1=4$，$\delta=1$。

$$A=\begin{pmatrix}-2&0&1&2&-1&-2\\2&1&-1&1&-2&0\\2&1&-2&2&0&-2\\-2&2&0&2&-1&2\\-2&-1&0&1&0&-1\\0&0&0&2&0&-2\end{pmatrix},\quad
C=\begin{pmatrix}0&2&1&1&1&-2\\1&-1&-1&1&1&-1\end{pmatrix},\quad
L_0=\begin{pmatrix}2&1&-2&2&-1&0\\1&-2&-2&-2&2&1\end{pmatrix},$$

$$\mathcal L=\begin{pmatrix}2&1&-2&2&-1&0\\1&-2&-2&-2&2&1\\ \tfrac16&1&0&0&0&0\end{pmatrix},\qquad
\mathcal Z=\left\langle\left(-6,\ 1,\ -\tfrac92,\ \tfrac32,\ 1,\ 0\right)\right\rangle .$$

## 复现

```
python tools/verification/certificate_delta1.py
```

输出逐条断言：$(5a)$ 成立；$\operatorname{rank}[C;\mathcal L]=5$；$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$；
$\delta=1$ 落在中间层；$(5b)$ 成立（B.12 判据：$\operatorname{rank}\mathcal O=3=q$）。

## 等级

**[精确验证]**（有理算术，逐条断言；脚本随机搜索后固定在上述数据上可复现）。
本文件是**存在性**证书，不是定理；定理是 B.31 的必要条件方向。
