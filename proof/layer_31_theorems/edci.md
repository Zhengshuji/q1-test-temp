# 定维数条件不变子空间存在性（EDCI）—— 独立的问题表述

> 专家 QA8 第 3 项：把"定维数条件不变性"作为**独立子问题**表述清楚，
> 并说明它相对经典理论多了什么约束、以及它在 MIN-ROWS 里的位置。
> 本文件**只表述问题**，不解它 ✓。

---

## 1. 问题（EDCI）

**输入**：有限维复向量空间 $X$、线性算子 $A:X\to X$、子空间 $B\subseteq X$、固定子空间 $W_0\subseteq X$、
整数 $k$。

**记**：$f(x)=\pi(xA)$，$\pi:X\to X/B$ 是商映射。称 $\mathcal U\subseteq X$ **条件不变**（conditioned
invariant，模 $B$）若
$$f(\mathcal U)\subseteq \pi(\mathcal U)=\frac{\mathcal U+B}{B}.$$

**问**：是否存在条件不变的 $\mathcal U$ 使
$$\dim\mathcal U=k,\qquad W_0\subseteq\mathcal U\ ?$$

记这个判定问题为 $\mathrm{EDCI}(X,A,B,W_0,k)$。

---

## 2. 经典理论覆盖到哪里、没覆盖到哪里

| # | 问题 | 经典 |
|---|---|---|
| 1 | 算满足包含约束的**最大**条件不变子空间（supremal）| **有算法**（几何控制；Marro 等的综述）|
| 2 | 条件不变子空间**可达的全部维数** | 部分：**Warren–Eckberg**（SIAM J. Control Optim.）用多项式矩阵 / Kronecker 不变量刻画**可控子空间**的维数，**含指定子空间**的构造 |
| 3 | **指定维数 + 指定固定子空间 + MIN-ROWS 的额外约束** | **没有** ✗ |

**关键区别** ✓：问题 1 给的是 supremal ✓，而 supremal 与"恰好 $k$ 维"之间没有必然联系 ✗ ——
本项目的家族对 $+$ 封闭 ✓、最大元 $=X$ ✓（RCP §59 ✓），所以 supremal 恒为 $X$ ✗，对"恰好 3 维"毫无信息 ✗。

$$\\boxed{\\ \\text{supremal} \\ne \\text{定维数}\\ ——\\ \\text{这是 }\\mathrm{EDCI}\\ \\text{的全部困难所在}\\ }$$

---

## 3. MIN-ROWS 相对经典条件不变性多出来的约束（重要 ✓）

1. **$\mu$ 进入层号** ✓：层号是 $q=\rho+c$，其中 $c=\dim(\mathcal V\cap\mathcal J)$ ✓、$\rho=\dim\pi(\mathcal V)$ ✓；
   而 $\mu=\dim(B\cap\mathcal U)$ 决定 $(N)$ 的强度 ✓ —— **不是**纯维数条件 ✗。
2. **提升的类型约束** ✓：$\mathcal V$ 必须 $\dim=4$、$\dim(\mathcal V\cap\mathcal J)=1$、$\mathrm{row}(L_0)\subseteq\mathcal V$。
3. **$(5a)$ 不是免费的** ✓：$(5a)\\iff\\widetilde{\\mathcal U}A\\subseteq\\widetilde{\\mathcal U}+\\mathcal K$（$\mathcal K=\\mathcal J+\\mathcal J A$）✓ ——
   也**正好是**一个条件不变性（模 $\mathcal K$ 而非模 $\mathcal J$）✓ ✓。所以 $\mathrm{EDCI}$ **出现两次** ✓：
   一次在 $(N)$（模 $B$）✓、一次在 $(5a)$（模 $\mathcal K$）✓。
4. **域** ✓：$X$ 与 $B$ 由 $(A,C_0)$ 经**有理运算**得到 ✓ ⟹ 问题是在 $\mathbb Q$ 或 $\mathbb C$ 上问的 ✓；
   若要求**实**子空间/实见证 ✓，那是**另一个**判定问题 ✗（专家 QA8 的提醒 ✓）。

---

## 4. 与 P2 / P3 的关系 [已证]

- **P2**（存在结构可允许 $\mathcal U$ 且 $\mu\ge1$）⟸ 是 $\mathrm{EDCI}$ 的一个**特例** ✓
  （取 $k=3$、$W_0\subseteq\mathcal U$、并要求 $\mu\ge1$）✓；
- **P3**（层可行）**不**由 P2 蕴含 ✗ —— 反例见 RCP §81–§82 ✓（$\mu=1$ 但整族被覆盖 ✓）。

$$\\boxed{\\ \\text{P2}\\ \\Longleftarrow\\ \\mathrm{EDCI}\\ ;\\qquad \\text{P3}\\ \\Longleftarrow\\ \\mathrm{EDCI}+\\text{谱条件}\\ }$$

---

## 5. 三条可尝试的路线（未做 ✗）

1. **Grassmann + 秩条件**（专家给 ✓）：在图坐标下取 $\mathcal U$ 的满列秩基 $Z$ ✓，把条件不变性写成
   $[Z,AZ,\\text{人}]$ 的秩条件 ✓、$W_0\\subseteq\\mathcal U$ 写成另一个秩条件 ✓ ⟹ 多项式方程/不等式 ✓ ⟹
   **可判定**（消元 ✓），但**不给**多项式时间 ✗。
2. **可行维数集的结构**（专家建议的"定维数定理"候选 ✓）：确定 $\\{k:\\mathrm{EDCI}\\ \\text{可行}\\}$ 是**区间**、
   **区间之并**、还是由**可控性指数/Kronecker 数据**描述 ✓。**不要假设是区间** ✗ ——
   和封闭**不**证明中间维数可达 ✗。
3. **本项目的特殊结构** ✓：$\mathcal K=\mathcal J+\mathcal J A$ 是二步对象 ✓、$B=\pi(\mathcal J A)$ ✓ ⟹
   两个条件不变性**共享** $\mathcal J$ ✓ ⟹ 可能存在把两者**合并**的表述 ✗（未做 ✗）。

---

## 6. 明确的开放问题

> **Q-EDCI**：$\mathrm{EDCI}$ 是否可判定？复杂度如何？可行 $k$ 的集合有什么结构？

已知 ✓：可判定性"应当"由路线 1 给出 ✓（前提是域与"可行"定义精确 ✓）；
多项式时间 / NP-hard / $\\exists\\mathbb R$-hard 全部**未定** ✗（专家 QA8 §4 ✓）。
