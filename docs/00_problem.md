# 00 · 问题

> 只写**确定的东西**：定义、已证的等价形式、与文献的对应。
> 经验性/未证的等价形式不在本文件（见 [docs/05](05_open_questions.md) 与 `workspace/q1_false/notes_data_shapes.md`）。

---

## 0.1 定义（MIN-ROWS）

给定 $A\in\mathbb C^{n\times n}$、$C\in\mathbb C^{p\times n}$、$L_0\in\mathbb C^{r\times n}$。求最小 $q$，使存在 $R\in\mathbb C^{(q-r)\times n}$ 令 $\mathcal L=\binom{L_0}{R}$（$q$ 行、行满秩）满足

$$(5a)\quad \operatorname{rank}\begin{pmatrix}\mathcal LA\\ \mathcal L\\ CA\\ C\end{pmatrix}=\operatorname{rank}\begin{pmatrix}\mathcal L\\ CA\\ C\end{pmatrix},\qquad
(5b)\quad \operatorname{rank}\begin{pmatrix}\lambda\mathcal L-\mathcal LA\\ CA\\ C\end{pmatrix}=\operatorname{rank}\begin{pmatrix}\mathcal L\\ CA\\ C\end{pmatrix}\quad\forall\lambda\in\mathbb C .$$

记最优值 $q_{\min}$。**q1**：计算 $q_{\min}$ 是多项式可解还是 NP-hard？

> **不是每个实例都有解**（2026-10-30 补）：若 $\min_\lambda\dim\pi(\mathbb C^n(\lambda I-A))<\rho_{ci}$，
> 则不存在任何 $\mathcal L$（[docs/02 F.2](02_theorems_proven.md)；实例见
> [proof/rank_barrier/no_solution_certificate.py](../proof/rank_barrier/no_solution_certificate.py)）。
> 这种实例上 $q_{\min}=\infty$；论文里必须先声明"对**可解**实例求 $q_{\min}$"。

### 0.1.1 底域（2026-10-30 补记，专家指出）

上面的定义取 $A,C,L_0,R$ 都在 $\mathbb C$ 上。**复杂度问题**的常规约定是输入为有理数、输出量要求有理数；
两者**不等价** ✗：例如 $A=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}$ 在 $\mathbb C^2$ 上有一维不变子空间（$\pm i$ 的特征向量），
在 $\mathbb Q^2$ 上**没有**（$x^2+1$ 在 $\mathbb Q$ 上不可约）。

本项目的全部层判据都是在 $\mathbb C$ 上写的 ✓。若要做"$R\in\mathbb Q$"的版本，需要额外讨论有理性（未做 ✗）。


---

### 0.1.2 三种表述（DEC / OPT / FIND，2026-11-07 补记）

> 由用户指出：工程上的**原始问题**是**给出 $R$**（一个设计），不是一个数。
> 此前 `§0.1` 只陈述了 OPT，**漏了 FIND**。

三种表述：

$$\begin{aligned}
\mathrm{DEC}(q):\quad&\text{给定 }(A,C,L_0)\text{ 与 }q,\ \text{判定 }\exists R\in\mathbb C^{(q-r)\times n}\ \text{使 }(5a),(5b);\\
\mathrm{OPT}:\quad&\text{计算 }q_{\min}=\min\{q:\ \mathrm{DEC}(q)\ \text{为真}\};\\
\mathrm{FIND}:\quad&\text{在最小阶输出具体 }R\ \text{（并附最小性证书：连 }q_{\min}\text{ 一起给出）}.
\end{aligned}$$

**等价链**（$q\le n$，故候选只有 $n-r+1$ 个）：

$$\mathrm{FIND}\ \ge\ \mathrm{OPT}\ \equiv\ \mathrm{DEC}.$$

* $\mathrm{DEC}\Rightarrow\mathrm{OPT}$：**逐个扫**全部 $n-r+1$ 个候选 $q$（多项式多个），取最小可行者；
  **不要**用二分——二分需要"可行性对 $q$ 单调"，而这一点**未证**（专家 2026-11-07 明确指出）；
* $\mathrm{OPT}\Rightarrow\mathrm{DEC}$：比较 $q_{\min}\le q$；
* $\mathrm{FIND}\Rightarrow\mathrm{OPT}$：见证带最小性；
* **$\mathrm{OPT}\Rightarrow\mathrm{FIND}$ 不自动成立**——它要求判定算法**构造性**地返回层/图卡数据。
  本项目框架内 Grassmann 判据是构造性的（给出 $S$ $\Rightarrow$ 得 $B_1,B_2$ $\Rightarrow$ 解线性系统得 $R$），故
  $$\text{在 Grassmann 判据可用的范围内}\quad \mathrm{FIND}\equiv\mathrm{DEC}.$$
* 必须允许 $q_{\min}=+\infty$（不存在任何可行阶；实例见 `docs/02 F.2` 与本卷宗 `proof/B.24` 的 $n=4$ 全阶障碍）。

**两处真实差别（FIND 独有）**：

1. **输出表示**：DEC 只回答"是/否"；FIND 要输出矩阵，必须声明**输出域**与位长。
   且"实见证存在"$\not\Rightarrow$"有理见证存在"（见 §0.1.1 的旋转例子）⟹ 输出域不同答案可能不同。
2. **构造性**：非构造的判定算法不产生见证。

**结论**：$q1$ 的正式陈述应写三行；声称 NP-hardness 时须指明是**哪一版**（复杂度惯例指 $\mathrm{DEC}$）。
现状：$\mathrm{OPT}$ 版是项目原来的陈述；$\mathrm{FIND}$ 版是用户指出的原始问题，此前未陈述。

---

## 0.2 两个条件的含义

$(5a)$：$\mathcal V=\operatorname{row}\mathcal L$ 在 $A$ 作用下"模 $\mathcal J$"稳定。
$(5b)$：商铅笔无零点。
二者合起来正是"存在 $q$ 阶功能观测器"的代数条件（$[\mathcal L;CA;C]$ 的核不随 $\lambda$ 变化）。

---

## 0.3 已确认的等价形式

记 $\mathcal J=\operatorname{row}[C;CA]$，$j=\dim\mathcal J$，$K=\ker[C;CA]$，$d=n-j$，$\pi:\mathbb C^n\twoheadrightarrow\mathbb C^n/\mathcal J$。

**E1**（$A$-桥形式）$(5a)\iff\exists A'$ 使 $\mathcal LA=A'\mathcal L$ 且 $\operatorname{row}(A')\subseteq\cdots$；
**等级**：[Lean] `proof/5a_archive/lean/ABridge.lean`、`Factor.lean`（机器检查，早期阶段）。

**E2**（商铅笔）置 $Q_{\mathcal V}(\lambda)=\lambda\,\pi(\mathcal L)-\pi(\mathcal LA)$（$q\times d$），$\rho=\dim\pi(\mathcal V)$。则
$$(5b)\iff\operatorname{rank}Q_{\mathcal V}(\lambda)=\rho\quad\forall\lambda .$$
**等级**：[已证]（证明在 [proof/pencil_equivalence/](../proof/pencil_equivalence/README.md)）。

**E3**（交维数）令 $F_\lambda=\{v:\ v(\lambda I-A)\in\mathcal J\}$。则
$$(5b)\iff\dim(\mathcal V\cap F_\lambda)=\dim(\mathcal V\cap\mathcal J)\quad\forall\lambda .$$
**等级**：**[精确验证 1128/1128]**（逐 $\lambda$ 比较，[proof/pencil_equivalence/verify_E3.py](../proof/pencil_equivalence/verify_E3.py)）。
**不是 [已证]** ✗：纸面证明在 `archive/expert_correspondence/Q1_FOR_EXPERT_7.md` 定理 1，
**本项目从未复核**（2026-10-30 补标：原写 [已证] 是过高的等级）。

**E4**（约化坐标）$\mathcal V$ 由 $(U,H,\tau)$ 参数化：$U=\pi(\mathcal V)$、$H=\mathcal V\cap\mathcal J$、$\tau$ 为提升自由度，且
$$q=\rho+c,\qquad \rho=\dim U,\ c=\dim H .$$
$(5a)\iff\beta(H)\subseteq U$ 且 $T(U)\subseteq U+B$。**等级**：定义性 + [已证]（[docs/04](04_structure.md) 引理 4.2.1）。

> **注意**：本文件**不**包含"$(5b)\iff(S_\tau,\beta|_H)$ 可控"这一条——它**已被否决**（输入算子恒为零），见 [docs/05](05_open_questions.md) Q5。

---

## 0.4 与文献的对应

- **Fernando, Trinh, Jennings**, IEEE TAC 55(5):1268–1273, 2010：其 Condition 1/2 与 $(5a)/(5b)$ **逐项相同**；给的是枚举子集的构造算法（指数级），**不谈复杂度**。全文：`literature/txt/fernando2010.txt`。
- **min-dimension $(A,B)$-不变子空间**：Warren–Eckberg（SIAM J. Control 13, 1975）§5 列为 open（对象是 **controllability subspace**）；$(A,B)$-不变版本即本文的 $P$。见 [docs/03](03_theorems_cited.md) 引用 3。
- **cover 问题**（Karcanias–Vafiadis 1993）：只覆盖 $(5a)$，最小维数仍 open。见引用 4。

---

## 0.5 判定版本

$$\textbf{MIN-ROWS}(A,C,L_0,k):\quad \exists\,\mathcal L=[L_0;R],\ \operatorname{rank}\mathcal L\le k,\ (5a)\wedge(5b)\ ?$$

显然 MIN-ROWS $\in$ NP（给定 $\mathcal L$ 可多项式核验）。$q1$ 就是问它是否 NP-hard。
