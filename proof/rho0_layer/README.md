# 命题：$\rho=0$ 层

> **对应 docs 条目**：B.3（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

## 陈述

$$\rho=0\iff\pi(\mathcal V)=0\iff\mathcal V\subseteq\mathcal J .$$

此时：
1. $(5a)\iff S\subseteq\mathcal J$ 且 $SA\subseteq\mathcal J$（即 $L_0$ 的行及其像都落在 $\mathcal J$ 里）；
2. $(5b)$ **自动成立**（$\lambda\mathcal L-\mathcal LA$ 的每一行都落在 $\mathcal J=\operatorname{row}[C;CA]$ 里，秩恒为 $\dim\mathcal J$）；
3. $q_{\min}=r$（取 $\mathcal V=S$）。

## 证明

- $\rho=0$ $\iff$ 商像为零 $\iff\mathcal V\subseteq\mathcal J$。
- 若 $S\subseteq\mathcal J$、$SA\subseteq\mathcal J$：取 $\mathcal V=S$，则 $\mathcal VA=SA\subseteq\mathcal J=\mathcal V+\mathcal J$ ✓ $(5a)$；$(5b)$ 见上。
- 反之若 $(5a)$ 成立且 $\mathcal V\subseteq\mathcal J$：$\mathcal VA\subseteq\mathcal V+\mathcal J=\mathcal J$，特别地 $SA\subseteq\mathcal J$ ✓。

**等级**：[已证]（项目早期已用可信基线做过 1935/1935 的精确复核）。

## 用途

这是"退化层"，常击败顶层公式（[proof/refuted/](../refuted/README.md) R1/R3 的反例多是这一层给出的）。
所以任何候选公式**必须先查 $c_0$ 项和这一层**。
