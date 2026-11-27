# 参考文献总表（canonical）

> 每条：作者 / 标题 / 出处 / 我们用它做什么 / 全文在仓库哪里。
> 本表是**唯一**的参考文献索引；`docs/03` 只列"我们引用的命题"，`literature/notes/` 放读后摘要。

## A. 本项目的问题来源与设计算法

| # | 文献 | 用它的什么 | 全文 |
|---|---|---|---|
| 1 | **Fernando, Trinh, Jennings**, *Functional observability and the design of minimum order linear functional observers*, IEEE TAC 55(5), 2010, 1268–1273 | Condition 1/2 与 $(5a)/(5b)$ **逐项相同**；构造算法（枚举子集）| `pdf/Functional Observability and the Design of Minimum order linear functional observers.pdf`；`txt/fernando2010.txt` |
| 2 | **Fernando**, *A Minimum-Order Functional Observer Beyond the Darouach and Luenberger Constructions*, arXiv:2609.33615 (2026) | 最小阶框架：功能可观测指标决定最小代数阶；谱可行性充要条件；含中间阶 | `papers/2609.33615.{pdf,txt}`; 摘要见 [notes/FERNANDO_2026_min_order.md](notes/FERNANDO_2026_min_order.md) |
| 3 | **Fernando**, *Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger*, arXiv:2609.37992 (2026) | **阶谱完整刻画**（$q_0\le\nu_{\min}\le n_0-p$）、Thm 4 铅笔形式、Thm 6 的 gcd 判据、Thm 9 的 chart 完备性。**无复杂度声明** | `papers/2609.37992.{pdf,txt}`; 详见 [notes/FERNANDO_2026_min_order.md](notes/FERNANDO_2026_min_order.md) |
| 4 | **Varga**, *Reliable algorithms for computing minimal dynamic covers for descriptor systems*, MTNS 2004 | **最小维动态覆盖**的低复杂度算法（服务于最小阶功能观测器）| `pdf/Feedback_invariants_of_linear_multivaria.pdf`（⚠️ 文件名误导）|
| 5 | **Karcanias, Vafiadis**, *On the cover problems of geometric theory*, Kybernetika 29(6), 1993 | cover 问题：只覆盖 $(5a)$ 一侧 | `pdf/Karcanias_Vafiadis_1993_cover.pdf`；`txt/Karcanias_Vafiadis_1993_cover.txt` |

## B. 几何理论

| # | 文献 | 用它的什么 | 全文 |
|---|---|---|---|
| 6 | **Wonham, Morse**, *Decoupling and pole assignment in linear multivariable systems: a geometric approach*, SIAM J. Control 8, 1970 | $(A,B)$-不变子空间、可控性子空间、$F$-补 | 书 `txt/trentelman2002.txt`（§ 几何理论）|
| 7 | **Warren, Eckberg**, *On the dimensions of controllability subspaces: a characterization via polynomial matrices and Kronecker invariants*, SIAM J. Control 13(2), 1975, 434–443 | 可控性子空间的**可能维数由不变量决定** | `txt/On_the_Dimensions_of_Controllability_Subspaces.md`（⚠️ 文件名声称 Emre–Hautus，实为本文）|
| 8 | **Willems**, *Almost A(mod B)-invariant subspaces*, 1981 | almost 不变性 | `txt/willems1981.txt` |
| 9 | **Jaffe, Karcanias**, *Matrix pencil characterization of almost (A,Z)-invariant subspaces: a classification of geometric concepts*, IJC 33(1), 1981, 51–93 | almost 不变子空间的**铅笔刻画** | `pdf/Matrix pencil characterization of almost ... .pdf` |
| 10 | **Trentelman, Stoorvogel, Hautus**, *Control Theory for Linear Systems*, Springer 2001 | 几何控制标准参考（已核：**无**我们需要的引理）| `pdf/Control Theory of Linear System.pdf`；`txt/trentelman2002.txt`、`txt/tsh.txt` |

## C. 铅笔 / Kronecker 理论

| # | 文献 | 用它的什么 | 全文 |
|---|---|---|---|
| 11 | **Verdier**, *Reduction and normal forms of matrix pencils*, arXiv:1205.1138, 2012 | 铅笔约化与标准形、Kronecker 理论 | `txt/verdier2012.txt`；`pdf/Reduction and Normal Forms of Matrix Pencils.pdf` |
| 12 | **Dodig**, *Matrix pencils completion problems*, LAA 428, 2008, 259–304 | **行/列补全**下 Kronecker 不变量的可达集 = 有限条不等式（Theorem 4）| `pdf/Matrix pencils completion problems.pdf`；`txt/dodig2008_matrix_pencils_completion.txt`；摘要 [notes/DODIG_2008_row_completion.md](notes/DODIG_2008_row_completion.md) |
| 13 | **Hearon**, *Minimum polynomials and control in linear systems*, J. Res. NBS 82(2), 1977 | 最小多项式与可控性指数的关系（背景）| `pdf/Minimum Polynomials and Control in Linear System.pdf` |

## D. 复杂度

| # | 文献 | 结论 | 全文 |
|---|---|---|---|
| 14 | **Blondel, Tsitsiklis**, *A survey of computational complexity results in systems and control*, Automatica 36, 2000（及 1997 论文）| 区间约束镇定 NP-hard；**无约束静态输出反馈当时开放** | 待获取 |
| 15 | **Toker, Özbay**, *On the NP-hardness of solving bilinear matrix inequalities and simultaneous stabilization with static output feedback*, ACC 1995 | BMI 可行性、多对象同时镇定 NP-hard | 待获取 |
| 16 | **Fu, Luo**, fixed-order 输出反馈的矩阵不等式 NP-hard | 同族 | 待获取 |
| 17 | **FOCS 2017**, *Hardness Results for Structured Linear Systems* | **结构型**（0/1）线性系统的硬度总纲 | 待获取 |
| 18 | **Pequito, Kar, Aguiar** 2014；**Olshevsky** 2013 | 结构型最小输入/传感器选择 NP-hard | `notes/05_相关工作检索.md` 有引 |
| 19 | **Löfberg**, *Static output-feedback stabilization is NP-hard*, arXiv:2609.16886, 2026 | **SOF1（数值数据）NP-hard**；by-product：仿射多项式族含 Hurwitz 成员 NP-hard | `pdf/Static output-feedback stabilization is NP-hard.pdf`；`txt/lofberg2026_static_output_feedback.txt`；gadget 清单 [notes/LOFBERG_2026_GADGETS.md](notes/LOFBERG_2026_GADGETS.md) |
| 20 | **Majumdar**, *Affine Rank Minimization is ER Complete*, arXiv:2602.14037, 2026 | **ARM(3) 是 ∃R-完全**；rank-forcing gadget（违反 $z=xy$ ⇒ $4\times4$ 满秩）、gauge block、composition lemma | `papers/2602.14037.{pdf,txt}`；笔记 [notes/MAJUMDAR_2026_ARM_ER.md](notes/MAJUMDAR_2026_ARM_ER.md) |
| 21 | **Liu**, *Computational complexity of static output feedback stabilization*, arXiv:2610.00390, 2026 | **SOF 稳定化是 ∃R-完全**；有效增益维数 $\kappa$ 固定时多项式可解；单输入族强 NP-hard | `papers/2610.00390.{pdf,txt}`；笔记 [notes/LIU_2026_SOF_EXISTS_R.md](notes/LIU_2026_SOF_EXISTS_R.md) |
| 22 | **Ahmadi, Chaudhry, Narang, Tang**, *Complexity of Output Feedback Stabilization*, arXiv:2609.20636, 2026 | **输出反馈稳定化 NP-hard**（除非 P=NP 无多项式/伪多项式算法；连续+离散）；与 Liu 的 ∃R-完全区分 | `papers/2609.20636.{pdf,txt}`；笔记 [notes/AHMADI_2026_OUTPUT_FEEDBACK.md](notes/AHMADI_2026_OUTPUT_FEEDBACK.md) |
| 23 | **Barkai, Shames**, *On the NP-Hardness of Unconstrained Static Output Feedback Stabilization*, arXiv:2609.38728, 2026 | 从 Subset Sum 归约 ⇒ 无约束 SOF **NP-hard**；频率分离 + Rouché + 增益有界/modulus margin | `papers/2609.38728.{pdf,txt}`；笔记 [notes/BARKAI_2026_SOF_NP_HARD.md](notes/BARKAI_2026_SOF_NP_HARD.md) |

## E. 待获取

| 文献 | 为什么需要 |
|---|---|
| **Emre, Hautus**, *A polynomial characterization of (A,B)-invariant and reachability subspaces*, SIAM JCO 18(4), 1980 | 决定 $P\in\mathbf P$ 的**新颖性**（可能已有多项式算法）|
| **Blondel–Tsitsiklis** 综述原文 | "哪些控制判定问题已定/开放"的全表 |
| **Toker–Özbay**、**Fu–Luo** 原文 | 更贴合的 gadget |

> 检索记录与"不要重复做"的索引见 [SEARCH_LOG.md](SEARCH_LOG.md) 与 [notes/SURVEY_2026-10-28.md](notes/SURVEY_2026-10-28.md)。

## 铅笔补全（专家 2026-10-30 提供，待读）

| # | 条目 |
|---|---|
| 1 | **M. Dodig**, *Matrix pencils completion problems*, Linear Algebra Appl. 428(1) (2008) 259–304. DOI 10.1016/j.laa.2007.08.029 —— 行/列补全指定 Kronecker 不变量 |
| 2 | **M. Dodig**, *Matrix pencils completion problems II*, Linear Algebra Appl. 429(2–3) (2008) 633–648. DOI 10.1016/j.laa.2008.03.021 —— 含**指定子铅笔**的补全，必要充分条件 |
| 3 | **M. Dodig, M. Stošić**, *The general matrix pencil completion problem: a minimal case*, SIAM J. Matrix Anal. Appl. 40(1) (2019) 347–369. DOI 10.1137/17M1155041 —— 经典补全问题的最小规模情形 |
| 4 | **M. Dodig**, *Matrix pencils completions of size two*, Linear Algebra Appl. 737 (2026) 119–145. DOI 10.1016/j.laa.2026.02.005 —— 补全规模为二的完整 Kronecker 不变量描述 |

> 状态：**未读** ✗（仅据专家转述登记）。与本项目的关系：它们的自由度是"新增行/列"，本项目是"子空间 $\mathcal V$ + $(5a)$ + 维数型"，
> 三项耦合；专家意见：没有找到能直接覆盖的现成定理 ✗。
