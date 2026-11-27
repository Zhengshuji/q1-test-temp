# 可允许格子：精确规格，以及层归约

> 这是专家（QA6）建议的 **Step 1**：把"$(3,1)$ 格子可允许"写成**充要**规格，并把每条约束的
> **依赖对象**（$\\mathcal U$ / $\\mathcal H$ / 提升）标清 ✓。

---

## 1. 规格 $\\mathfrak A_{3,1}$

一个有序对 $(\\mathcal U,\\mathcal H)$ 属于 $\\mathfrak A_{3,1}$，当且仅当下列**全部**成立 ✓：

| # | 约束 | 依赖 |
|---|---|---|
| **A1** | $\\mathcal U\\subseteq X$，$\\dim\\mathcal U=3$ | $\\mathcal U$ |
| **A2** | $\\pi(\\operatorname{row}L_0)\\subseteq\\mathcal U$ | $\\mathcal U$ |
| **A3** | $\\pi(\\operatorname{row}(L_0A))\\subseteq\\mathcal U$ | $\\mathcal U$ |
| **A4** | $\\mathcal H\\subseteq\\mathcal J$，$\\dim\\mathcal H=1$ | $\\mathcal H$ |
| **A5** | $\\beta(\\mathcal H)\\subseteq\\mathcal U$ | $\\mathcal U,\\mathcal H$ |
| **A6** | $(N)$：$f(\\mathcal U)\\subseteq q_B(\\mathcal U)=(\\mathcal U+B)/B$ | $\\mathcal U$ |
| **A7** | $\\exists\\,\\mathcal V\\subseteq\\mathbb C^n$：$\\dim\\mathcal V=4$、$\\operatorname{row}(L_0)\\subseteq\\mathcal V$、$\\pi(\\mathcal V)=\\mathcal U$、$\\dim(\\mathcal V\\cap\\mathcal J)=1$、且 $(5a)$ | $\\mathcal U,\\mathcal H$、提升 |

**关于 A7 的化简**（已证，[RCP §27.1b](../layer_program/RESTRICTED_COMPLETION_MODEL.md)）：

> 在 A2、A6 成立、且**固定行相容**（A3）的前提下，**自由行**的提升总能选到使 $\\pi(\\ell_iA)\\in\\mathcal U$ ✓
> （每行可各自平移 $B$ 中任意元素 ✓，因为 $\\beta$ 满射 ✓）。

⟹ A7 中"新"的要求只有两条 ✓：**类型** $\\dim(\\mathcal V\\cap\\mathcal J)=1$ ✓ 与 $(5a)$ 的**固定行部分** ✓（由 A3 保证 ✓）。

**重要**：$\\mathfrak A_{3,1}$ **不是**格 ✗ —— 条件不变子空间对 $\\cap$ **不**封闭 ✗
（$\\mathbb C^3$ 上 $U=\\operatorname{span}(e_2,e_3)$、$V=\\operatorname{span}(e_2,e_1+e_3)$ 都条件不变，但 $U\\cap V$ 不是 ✓）。
对**和**封闭只对满足 $(N)$ 的族成立 ✓，**不**自动传递到含 A2、A3、A7 的族 ✗。
**不要**假设有最小元 ✗ —— "最小元存在"是**已撤回**的结论 ✗（反例见 RCP §30 ✓）。

---

## 2. 层归约定理

定义
$$\\mathfrak G_{3,1}=\\{(\\mathcal U,\\mathcal H)\\in\\mathfrak A_{3,1}:\\ \\text{该格子未被覆盖}\\}.$$

> **定理（归约）**：$(3,1)$ 层可行 $\\iff$ $\\mathfrak G_{3,1}\\ne\\varnothing$ ✓。

*证明*：
(⇐) 若 $(\\mathcal U,\\mathcal H)\\in\\mathfrak G_{3,1}$：由"未被覆盖"存在 $s$ 使 $(5b)$ 成立 ✓；
由 A7 存在 $\\mathcal V$ 使 $(5a)$ 成立 ✓ ⟹ $\\mathcal V$ 是层见证 ✓。
(⇒) 若层的 $\\mathcal V$ 存在：取 $\\mathcal U=\\pi(\\mathcal V)$ ✓、$\\mathcal H=\\mathcal V\\cap\\mathcal J$ ✓ ⟹ A1–A7 逐条成立 ✓，
且该格子未被覆盖（$\\mathcal V$ 本身就是使 $(5b)$ 成立的 $s$ ✓）✓。$\\square$

**注意**：这个等价是"按定义"的 ✓。它的价值在于把层问题变成**受约束的存在性问题** ✓，
而不是去构造一个**不存在的** $X$ 上自同态 ✗（$f:X\\to X/B$ 不是自同态，见 §3）。

---

## 3. 两条必须记住的事实

1. **$A$ 在 $X$ 上没有诱导自同态** ✗。$\\pi(xA)$ 在 $X$ 上不良定义 ✓（偏差恰是 $B$ ✓）；
   良定义的只有 $f:X\\to X/B$ ✓，且 $f$ **不**下降到 $X/B$ ✗。
   $$\\therefore\\ \\text{"}f\\text{ 的特征向量"、"}\\mathcal U\\text{ 是 }f\\text{-不变"、"用 }f\\text{ 的广义特征空间" 都无意义}\\ ✗$$
2. $(N)$ 等价于经典**条件不变性** ✓：记 $\\mathcal K=\\mathcal J+\\mathcal JA$，则
   $$(N)\\iff\\widetilde{\\mathcal U}A\\subseteq\\widetilde{\\mathcal U}+\\mathcal K$$
   （$\\widetilde{\\mathcal U}$ 是 $\\mathcal U$ 在 $\\mathbb C^n$ 中的任一提升 ✓）。此为【已证-纸面】+ 28/28 精确验证 ✓。

---

## 4. P1 / P2 / P3 与开放问题

$$\\begin{aligned}\\text{P1}\\quad&\\exists\\ \\text{满足 A1,A2,A3,A6 的}\\ \\mathcal U\\\\
\\text{P2}\\quad&\\text{P1 且 }\\dim(B\\cap\\mathcal U)\\ge1\\\\
\\text{P3}\\quad&\\mathfrak G_{3,1}\\ne\\varnothing\\quad(\\text{即层可行})\\end{aligned}$$

$$\\text{P1}\\not\\Rightarrow\\text{P2}\\not\\Rightarrow\\text{P3}\\qquad(\\text{专家指出 ✓})$$

- $\\mu=0$ ⟹ 由 C.4 恒被覆盖 ✗ ⟹ **要可行必须有 $\\mu\\ge1$** ✓ ⟹ P1 是**必要**的门 ✓，不充分 ✗；
- **P2 是射影搜索** ✓：$B\\cap\\mathcal U\\ne0\\iff\\exists[b]\\in\\mathbb P(B):\\exists\\mathcal U\\ni b$ 满足 A1,A2,A3,A6 ✓
  —— **不是**对 $b$ 的线性检验 ✗（$\\{b:\\exists\\mathcal U\\}\\ $一般**不是**子空间 ✗，见 [RCP §47](../layer_program/RESTRICTED_COMPLETION_MODEL.md)）。

> **开放问题（本目录不含其解答）**：$\\mathfrak G_{3,1}\\ne\\varnothing$ 是否可判？对有理输入是否多项式时间？

**二分猜想（研究猜想，未证 ✗）**：每个结构可允许的 $(3,1)$ 层，
**要么**无 $\\mu\\ge1$ 的可允许格子，**要么**有未被覆盖的可允许格子 ✓。
若真 ⟹ 主问题塌缩为 P2 ✓；若假 ⟹ 反例给出层级别独立的谱障碍 ✓。

---

## 5. 精确规格的机器实现

[../../proof/rho1_layer/verify_cell_all_conditions.py](../rho1_layer/verify_cell_all_conditions.py) 逐条打印
A1–A3、A5–A7 与 $(5a)(5b)$（**十条**）✓ —— 它正是本规格的**字面实现** ✓。
它此前抓到过一次真实漏检（"$\\operatorname{row}(L_0)\\subseteq\\mathcal V$" 从未被检查 ✓），
所以规格与实现是**同一条** ✓，不是两套说法 ✓。

---

## 6. 完整枚举的一次尝试（$\mathbb F_p$）与它的**结论边界** ✗

按专家 Step 3 的要求 ✓（"枚举全部可允许格子，不要抽样" ✗），在 §55 的"好"实例**模 3** 之后
做了**完整枚举** ✓（[verify_dichotomy_fp.py](verify_dichotomy_fp.py)）：

| 量 | $\mathbb F_3$ |
|---|---|
| $X$ 的 3 维子空间总数 | 108 |
| 结构可允许（A2、A3、A6）| 12 |
| 其中有 $\mu\ge1$ | **1** |
| 其中"未覆盖"的 | **0** |

$$\text{字面上：}\mu\ge1\ \text{的格子存在但全被覆盖} \Longrightarrow \text{二分猜想在 }\mathbb F_3\text{ 上"不成立"}\ ✗$$

### 6.1 但这**不是**猜想的反例 ✗（重要）

判据"未覆盖"的实现是"铅笔最大子式的 $\gcd$ 为 1" ✓ —— 在 $\mathbb F_3$ 上这意味着
**在 $\overline{\mathbb F_3}$ 里没有公共根** ✗，与"在 $\mathbb C$ 里没有公共根"**不是**同一件事 ✗ ✓。

而**同一个实例在 $\mathbb Q/\mathbb C$ 上**：§55 的 $\mathcal V$ 明确满足 $(5a)\wedge(5b)$ ✓ ⟹
该层**可行** ✓ ⟹ 二分猜想的第二个分支成立 ✓ ✓。

$$\boxed{\ \text{有限域完整枚举得到的"反例"是}\textbf{域伪影}\ ✗\ ——\ \text{正是专家提醒过的那一点}\ ✓\ }$$

### 6.2 对下一步的意义

- **枚举方法本身可用** ✓（108 个子空间、12 个可允许，都在有理算术下完全枚举 ✓）；
- 但**判据的"覆盖"必须在 $\mathbb C$ 语义下判** ✓ —— 即 $\gcd$ 要在 $\mathbb Q[\lambda]$ 上算 ✓
  （这我们已经有 ✓：`CV.V.pgcd` 就是有理算术 ✓），而**子空间**的枚举在 $\mathbb Q$ 上是无限的 ✗；
- ⟹ 若要做有理语义下的完整枚举 ✗，只能：(a) 在**数域**上枚举（有限 ✗ 仍无限 ✗），或
  (b) 把 $\mathcal U$ 的族限制到**可证明有限**的部分（例如由不变子空间给出的 ✓）。

**因此**：二分猜想的检验需要一个新的思路 ✗ —— 见 [../layer_program/RESTRICTED_COMPLETION_MODEL.md §58](../layer_program/RESTRICTED_COMPLETION_MODEL.md)。
