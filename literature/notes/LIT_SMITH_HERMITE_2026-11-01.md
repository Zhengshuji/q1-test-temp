# 文献笔记：多项式矩阵的 Smith/Hermite 形与 adapted basis（E-1，2026-11-01）

> 目的：支撑 A-1（adapted basis）与 QA24 的"多项式标架"问题。**只记与本项目相关的**。

## 1. Wilkening & Yu, *A local construction of the Smith normal form of a matrix polynomial*

**出处**：[arXiv:0809.2978](https://arxiv.org/abs/0809.2978)（v2, 2010；26 页；cs.SC）。

**摘要要点**（原文）：给出域上**正则矩阵多项式**的 Smith 形**及其乘子**的算法；与其他算法不同，
它先对行列式的**每个不可约因子分别算局部 Smith 形**，再合成全局 Smith 形，而不是直接对原矩阵做一串
幺模行/列变换；报告了精确算术下的性能。

**对本项目的用处**：
- 若将来回到 QA24 的"多项式标架"，这是实现路线（乘子 = 幺模矩阵 $U,V$）；
- **但**：我们已在 A2 §33/§34 绕开了标架问题（判据只用 $[U\mid P]$ 的子式），
  所以这篇现在是**备用**，不是主线。

**局限**：只读摘要（PDF 未取），未核对它的"正则（regular）"假设与我们铅笔的匹配。

## 2. Forney, *Minimal bases of rational vector spaces*（SIAM J. Control 13, 1975, 493–520）

**经典文献**：有理向量空间的**极小多项式基**；$\mathbb C(\lambda)$ 子空间 → $\mathbb C[\lambda]$ 基的标准语言。

**对本项目的用处**：QA24 里"$C(\lambda)$-基 ≠ 多项式框架"的**标准术语**就在这篇里：
- 极小基 = 行/列既约的多项式基；
- 同一子空间的两组多项式基相差一个幺模矩阵（这正是我们 A2 §29.3 的命题 3）。

**状态**：**未读原文**（只有标题/被引信息）。若 A-1 需要严格化"框架不变性"，应补读。

## 3. Wei Zhou, *Fast Order Basis and Kernel Basis Computation*（PhD thesis, Waterloo, 2013）

**主题**：多项式矩阵的 kernel basis、column basis、**unimodular completion**、Hermite/Popov 形。

**对本项目的用处**：`poly_frame.unimodular_row_completion` 的单行情形就是这里的"unimodular completion"；
若要推广到多行（Smith 形），这是最直接的算法参考。

**状态**：**未读原文**。

## 4. Adapted basis 定理（子模在 PID 上的标准结论）

在某个讲义/论文里以 **Theorem 1.1.1 (Adapted basis)** 出现：PID 上自由模的子模有**适配基**
（存在环境基使子模的矩阵呈三角/对角形）。

**对本项目的用处**：
- 我们的 A-1 需要的是**向量空间**版本（域上），只需**高斯消元**，不需要 Smith 形 ✓；
- `coeff_of_S.adapted_basis` 已实现并**在 c282 上验证通过**（$T^{-1}(H/S)=\operatorname{span}(e_1..e_m)$ ✓）。

## 5. 本轮的实质发现（与文献无关，但由这次核对发现）

**单行列式判据要求方阵**：$[U\mid P]$ 是 $(w-s)\times(r+t)$ 矩阵；只有在 $r+t=w-s$ 时它才是方阵、
"一个行列式"才等于"全部极大子式"。

$$r+t=w-s\ \text{（方阵）}\quad\text{vs}\quad r+t=m\ \text{（我此前误用的条件）}$$

c282：$r+t=4$、$w-s=5$ ⟹ **非方阵**，有 5 个极大子式；单行列式只是其中之一 ⟹
$a_j$ 判据只在**其余子式冗余**时才对（c282 的 80 个点上恰好如此）。

**正确判据**（与 QA25 §4 一致）：$\gcd$ of **all** $(r+t)$-minors —— 即 §27 的 `feasible_by_minors` ✓。

## 6. 结论与下一步

| 文献 | 状态 | 是否主线 |
|---|---|---|
| Wilkening–Yu | 摘要 | 备用（若回到多项式标架）|
| Forney | 未读 | A-1 的术语来源 |
| Zhou | 未读 | unimodular completion 的算法参考 |
| adapted basis | 标准结论 | **已实现并验证** ✓ |

**下一步（分支 4 的剩余）**：
1. 补读 Forney（极小基与幺模关系）——支撑 A2 §29.3 的严格化；
2. 把"单行列式只在 $r+t=w-s$ 时够"写成 A2 的一条**更正**（现在只在 A3 任务页）；
3. 若走 Smith 路线：用 Wilkening–Yu 的乘子构造。
