# 03 · 引用的定理（文献）

> 只列**本项目实际用到**的文献结论。全文/摘录见 `literature/`。

---

## 引用 1 · Fernando–Trinh–Jennings (2010)

**文献**：J. A. Fernando, H. Trinh, L. Jennings, *Functional observability and the design of minimum order linear functional observers*, IEEE TAC 55(5):1268–1273, 2010.
**全文**：`literature/txt/fernando2010.txt`（转写）、`literature/pdf/Functional Observability ... .pdf`。

**结论**：存在 $q$ 阶功能观测器 $\iff$ 存在 $\mathcal L=[L_0;R]$（$q$ 行）满足 $(5a)$ 与 $(5b)$（其 Condition 1/2 **逐项相同**）。他们给**构造算法**（需枚举 $\binom{n-a}{j}$ 个子集，指数级），**不讨论复杂度**。

**本项目用法**：$q1$ 就是问这个阶数问题是否 NP-hard。已核：其条件与 $(5a)/(5b)$ 一致（项目早期已做等价性验证）。

---

## 引用 2 · Wonham–Morse (1972), Thm 2.1

**文献**：W. M. Wonham, A. S. Morse, *Decoupling and pole assignment in linear multivariable systems: a geometric approach*, SIAM J. Control 8(1):1–18, 1970；及 **Automatica 8 (1972)** 的相关定理。
**摘录**：`literature/txt/wonham_morse_1972.txt`。

**结论（Thm 2.1 一系）**：$D\subseteq \operatorname{im}B$ 时，"最小维数 $(A,B)$-不变子空间" $=$ "最小维数 controllability subspace"。

**本项目用法**：**只在 $D\subseteq B$ 时**我们的 $P$ 与 c.s. 版本重合；一般情形 $P$ 是 $(A,B)$-不变版本。

---

## 引用 3 · Warren–Eckberg (1975)

**文献**：A. E. Warren, A. E. Eckberg Jr., *On the dimensions of controllability subspaces: a characterization via polynomial matrices and Kronecker invariants*, SIAM J. Control 13(2):434–445, 1975. DOI [10.1137/0313026](https://epubs.siam.org/doi/abs/10.1137/0313026).
**摘录**：`literature/txt/`（若无则见 `archive/process_logs/REVIEW_LOG.md` 记录 5）。

**结论**：§5 明确写——"finding minimal dimension c.s. containing arbitrary subspaces **remains an open issue**"。$D\subseteq\operatorname{im}B$ 情形由 Kronecker 不变量解决（他们 Thm 2）。

**本项目用法**：文献的 open 是 **c.s. 版**；本项目解决的是 **$(A,B)$-不变版**（$P$），二者只在 $D\subseteq B$ 时重合（见引用 2）。

---

## 引用 4 · Karcanias–Vafiadis (1993)

**文献**：N. Karcanias, D. Vafiadis, *On the cover problems of geometric theory*, Kybernetika 29(3):211–230, 1993.
**全文**：`literature/pdf/pencils/Karcanias_Vafiadis_1993_cover.pdf`、`literature/txt/Karcanias_Vafiadis_1993_cover.txt`。

**结论**：cover 问题（我们的 $(5a)$ 部分）的**最小维数仍 open**；他们处理的是"按包含"的极值。

**本项目用法**：cover 只对应 $(5a)$，不含 $(5b)$；所以 cover 理论不能直接回答 $q1$。

---

## 引用 5 · Emre–Hautus (1980) —— **待读**

**文献**：E. Emre, M. L. J. Hautus, *A polynomial characterization of $(A,B)$-invariant and reachability subspaces*, SIAM J. Control Optim. 18(4):420–436, 1980.

**状态**：项目**只读过它在 Trentelman 书里的引用**（`literature/txt/tsh.txt` 参考文献第 43 条），正文未读。

$$\boxed{\ \text{在声称 }P\in\mathbf P\ \text{是新结果之前必须读它}\ }$$

---

## 引用 6 · Kleiman–Krener（闭包算法）

**文献**：D. L. Kleiman, A. J. Krener, 相关闭包迭代（见任何几何控制教材）。
**结论**：$B=0$ 时 $P=\dim\langle S\rangle_A$ 可用 $A$-不变闭包迭代 $O(n^3)$ 算出。

**本项目用法**：$P$ 的**端点情形**；现在整个 $P$ 都多项式（[proof/p_is_polynomial](../proof/p_is_polynomial/README.md)），故它降级为"端点校验"。

---

## 引用 7 · Trentelman–Stoorvogel–Hautus (2002)

**文献**：*Control Theory for Linear Systems*, Springer, 2002（403 页）。
**全文**：`literature/txt/tsh.txt`、`literature/pdf/foundations/Control_Theory_of_Linear_System.pdf`。

**结论**：受控不变/conditioned invariant 的标准理论；$\mathcal V^*,\mathcal S^*$ 等。**没有**"最小维数含给定子空间"的算法或复杂度结果（项目已逐章核过）。

**注意**：书里的 "no zeros" 20 处**全部**指传递矩阵零点，不是 $(5b)$ 的铅笔无零点。

---

## 引用 8–12（复杂度与铅笔理论，2026-10-28 补）

| # | 文献 | 我们引它的哪一条 |
|---|---|---|
| 8 | **Dodig**, *Matrix pencils completion problems*, LAA 428 (2008) 259–304 | **行/列补全**下铅笔的 Kronecker 不变量能被赋成什么（解 Loiseau 等人的挑战问题）——支撑路线 F12 |
| 9 | **Varga**, *Reliable algorithms for computing minimal dynamic covers*, MTNS 2004 | 最小维动态覆盖的**低复杂度算法**（服务于最小阶功能观测器设计）——决定我们对 $P\in\mathbf P$ 的**新颖性声明** |
| 10 | **Jaffe–Karcanias**, IJC 33(1) 1981, 51–93 | almost $(A,Z)$-不变子空间的**铅笔刻画**与几何概念分类 |
| 11 | **Löfberg**, *Static output-feedback stabilization is NP-hard*, arXiv:2609.16886 (2026) | SOF1 **NP-hard**（Betweenness 归约）；by-product：仿射多项式族含 Hurwitz 成员 NP-hard |
| 12 | *Hardness Results for Structured Linear Systems*, FOCS 2017 | **结构型**（0/1）线性系统的硬度总纲——说明"结构型硬度不能直接搬到数值型" |

> 全表与"能给我们什么/不能给什么"见 [literature/notes/SURVEY_2026-10-28.md](../literature/notes/SURVEY_2026-10-28.md)。
