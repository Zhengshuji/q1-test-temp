# 三篇文献的确切帮助与局限（专家"目标 4"）

> 2026-10-29。**只读了 arXiv 摘要**（Fuhrmann–Helmke 未读）；全文未读 ✗。以下区分"文献说了什么"与"我能用它做什么"。

## 1. Rubei 2022

**Elena Rubei**, *Affine subspaces of matrices with constant rank*, Linear Algebra Appl. 644 (2022) 259–269（arXiv:2111.14997）。

**摘要要点**：对域 $K$、$m,n$ 与 $r\le m\le n$，定义
$$a^K(m\times n;r)=\max\{\dim S:\ S\subseteq M(m\times n,K)\ \text{仿射子空间，且每个矩阵秩为}\ r\}$$
则
$$a^{\mathbb R}(m\times n;r)=r(n-r)+\frac{r(r-1)}{2},$$
并对**对称**矩阵给出上界 $a^{\mathbb R}_{sym}(n;r)\le\lfloor r/2\rfloor\bigl(n-\lfloor r/2\rfloor\bigr)$。

**能用的地方（一条真推论）**：固定 $\lambda_0$，映射 $\tau\mapsto P(\tau,\lambda_0)$ 是**仿射**的 ✓。
若某个仿射子集 $\mathcal B\subseteq\mathcal A$ 上 $(5b)$ 成立，则对每个 $\lambda$（特别 $\lambda_0$）都有 $\operatorname{rank}P(\tau,\lambda_0)=\rho$ ✓，
故 $\tau\mapsto P(\tau,\lambda_0)$ 把 $\mathcal B$ 映入"常秩 $\rho$"的仿射子空间 ✓，于是由 Rubei 定理
$$\operatorname{rank}\bigl(\text{该仿射映射}\bigr)\ \le\ \rho(d-\rho)+\binom{\rho}{2}.$$

**局限** ✗：这是**秩的界**，不是判定算法；而且它约束的是"**全部** $\tau$ 都可行"这一极端情形下的秩，不是"存在可行 $\tau$"✓。
对我们的问题（$\exists\tau$）**不构成判据** ✗。

## 2. de Seguins Pazzis 2025

**Clément de Seguins Pazzis**, *On affine spaces of rectangular matrices with constant rank*, Linear Algebra Appl. 704 (2025) 58–76（arXiv:2405.02689）。

**摘要要点**：把 Rubei 的结果从 $\mathbb R$ 推广到**任意**（元素数 $>r+1$ 的）域，并**分类**达到最大维数的空间；
该分类依赖于 $M_s(\mathbb F)$ 中维数为 $\binom{s}{2}$ 的可逆矩阵仿射子空间的分类，而后者与非迷向二次型的合同分类相关。

**能用的地方**：它说明"常秩仿射子空间"的**结构**在任意域上都已清楚 ✓（包括极值情形）✓。
**局限** ✗：仍是"结构与维数"，**不是**判定算法；且分类依赖二次型分类，本身不便宜 ✗。

## 3. Fuhrmann–Helmke 2001

**P. A. Fuhrmann, U. Helmke**, *On the parametrization of conditioned invariant subspaces and observer theory*（Linear Algebra Appl., 2001；据专家转述）。

**据专家转述的内容**：系统研究 conditioned-invariant 子空间的**参数化**，联系多项式模型、Toeplitz 算子与观测器理论；
提供结构与参数化工具，但**不**给出"包含给定子空间 + 固定维数 + 固定交维数"的通用可达性判据。

**未读全文** ✗（本轮只按专家转述记录）。**局限**：参数化 ≠ 判定算法 ✗（与本文档 §1 的论点一致）。

## 4. 这三篇合起来告诉我们什么

1. "常秩"这类**结构**在矩阵空间层面已被充分研究（维数公式、极值分类）✓；
2. 但它们回答的是"**什么样的空间**具有常秩" ✗，不是"**给定的**仿射族是否含有常秩成员" ✗ ——
   后者才是本文档的问题（专家的 Q1）✓；
3. 唯一能直接引用的是第 1 节那条**秩的界** ✓，它只在"全部 $\tau$ 都可行"的极端情形下给出约束 ✓。

$$\boxed{\ \text{三篇都提供了结构/维数，没有一篇提供"}"\exists\tau"\text{" 的判定}\ }$$

## 5. 待补

- Fuhrmann–Helmke 2001 全文（未读 ✗）；
- Rubei 与 de Seguins Pazzis 的**证明技术**是否可用于"$\exists\tau$"（摘要看不出，需读全文 ✗）。

## 6. 本轮的阅读状态（诚实）

| 文献 | 读了什么 | 没读什么 |
|---|---|---|
| Rubei 2022 | **arXiv 摘要**（完整）| 正文与证明技术（arXiv HTML 抓取超时 ✗；PDF 抓取失败 ✗）|
| de Seguins Pazzis 2025 | **arXiv 摘要**（完整）| 正文与证明技术（同上）|
| Fuhrmann–Helmke 2001 | **专家转述的内容** | 全文未读 ✗ |

所以第 1、2 节里"能用的地方"只是**从摘要能推出的推论** ✓；"他们的证明技术能否用于 $\exists\tau$"这一条**没有依据** ✗，
不应作为结论使用 ✓。
