# literature/ 索引

> 只放参考文献（论文、教材、抽取文本、阅读笔记），不放本项目结论。
> 全库唯一的文献总表仍是 [REFERENCES.md](REFERENCES.md)；本文件只管**目录里的文件**。

## 目录约定

| 目录 | 放什么 | 命名 |
|---|---|---|
| [pdf/foundations/](pdf/foundations/) | 教材与经典：BPR 实代数几何、Renegar 1992 两篇、Trentelman 教材、最小多项式、Verdier 铅笔标准形 | `Author_Year_短标题.pdf` |
| [pdf/observer/](pdf/observer/) | 功能观测器主文献 | `Author_Year_短标题.pdf` |
| [pdf/pencils/](pdf/pencils/) | 矩阵铅笔、几何系统理论、子空间不变性 | `Author_Year_短标题.pdf` |
| [pdf/algebra/](pdf/algebra/) | 子空间覆盖、Schubert 簇参数空间 | `Author_Year_短标题.pdf` |
| [pdf/complexity/](pdf/complexity/) | 复杂度类与点计算 | `Author_Year_短标题.pdf` |
| [papers/](papers/) | 2026 年 arXiv 论文，pdf 与 txt 成对 | **arXiv id**（`2609.33615.pdf`）|
| [txt/](txt/) | 抽取/转写文本 | 与来源同名或保留历史名 |
| [notes/](notes/) | 阅读笔记与专题摘录 | 大写专题名 |

新增文件请按上表命名；旧文件里的历史名（如 `tsh.txt`）保留，因为它们被多处引用。

## PDF

| 文件 | 是什么 | 用在哪 |
|---|---|---|
| `foundations/Basu_Pollack_Roy_2006_ARAG.pdf` | Basu–Pollack–Roy, *Algorithms in Real Algebraic Geometry*, 2nd ed., 2006 | 实代数可行性/样本点的复杂度（**Theorem 13.12** 用于 FIND 的见证抽取） |
| `foundations/Renegar_1992_JSC_PartII.pdf` | Renegar, JSC 13(3):301–327, Part II（一般判定问题） | 判定界 $B(\log B)(\log\log B)(sD)^{O(N)}$ |
| `foundations/Renegar_1992_JSC_PartIII.pdf` | Renegar, JSC 13(4):329–352, Part III（量词消去） | 备用（QE 路线） |
| `foundations/Control_Theory_of_Linear_System.pdf` | Trentelman–Stoorvogel–Hautus 教材 | 标准术语 |
| `foundations/Minimum_Polynomials_and_Control.pdf` | 最小多项式与控制 | 背景 |
| `observer/Fernando_2010_min_order_functional_observers.pdf` | Fernando–Trinh–Jennings, IEEE TAC 2010 | 问题来源：条件 (5a)(5b) |
| `pencils/Dodig_2008_matrix_pencils_completion.pdf` | Dodig, LAA 428 (2008) | 铅笔补全背景 |
| `pencils/Reduction_and_Normal_Forms_of_Matrix_Pencils.pdf` | Verdier | 铅笔标准形 |
| `pencils/On_computing_root_polynomials_and_minimal_bases.pdf` | LAA 658 (2023) | 极小基/根多项式 |
| `pencils/Karcanias_Vafiadis_1993_cover.pdf` | Karcanias–Vafiadis 1993 | 覆盖版最小维数（open） |
| `pencils/Matrix_pencil_almost_AZ_invariant_subspaces.pdf` | 几乎 $AZ$-不变子空间的分类 | 几何背景 |
| `pencils/Matrix_pencil_approach_to_geometric_systems.pdf` | 几何系统理论的铅笔方法 | 几何背景 |
| `pencils/A_polynomial_characterization_AB_invariant.pdf` | $(A,B)$-不变子空间的多项式刻画 | 几何背景 |
| `pencils/Feedback_invariants_of_linear_multivariable.pdf` | 实为 **Varga, MTNS 2004**（见下方勘误） | 动态覆盖 |
| `algebra/Covering_by_complements_of_subspaces_II.pdf` | Proc. AMS 125 (1997) | 子空间覆盖（open 的来源） |
| `algebra/Parameter_spaces_of_Schubert_varieties.pdf` | JPAA 216 (2012) | Schubert 参数空间 |
| `complexity/Lofberg_2026_SOF_stabilization_NP_hard.pdf` | Löfberg, arXiv:2609.16886 | 静态输出反馈 NP-hard |
| `complexity/Berthomieu_2026_sample_points.pdf` | Berthomieu–Gillot–Safey El Din, arXiv:2605.18110 | 单不等式样本点的当前最好复杂度（对照用） |

## papers_2026（arXiv 正本，pdf + txt）

| arXiv | 内容 | 用在哪 |
|---|---|---|
| `2609.33615` | Fernando, *A Minimum-Order Functional Observer Beyond the Darouach and Luenberger Constructions* | 精确刻画（阶谱、增广族） |
| `2609.37992` | Fernando, *Complete Characterization of Minimum-Order Functional Observers…* | 逐阶刻画 + **Grassmann 图算法（Algorithm 1）**、gcd 谱检验 |
| `2307.08923` | Zhang–Fernando–Darouach, IEEE TAC 2025 | 功能可观测性与传感器选择；**论文版式的参照** |
| `2602.14037` | Majumdar, 仿射秩最小化 $\exists\mathbb R$ | 相邻硬度 |
| `2609.38728` | Barkai–Shames, SOF NP-hard | 相邻硬度 |
| `2610.00390` | Liu, SOF $\exists\mathbb R$-complete + 有效增益维数 FPT | 邻近复杂度方向 |
| `2609.20636` | （按需查） | — |

## txt/

| 文件 | 说明 |
|---|---|
| `tsh.txt` | Trentelman–Stoorvogel–Hautus 教材转写（403 页） |
| `fernando2010.txt`、`fernando2010_p4.txt` | Fernando 2010 的抽取 |
| `dodig2008_matrix_pencils_completion.txt` | Dodig 2008 |
| `emre_hautus_1980.txt` | Emre–Hautus 1980（**长期缺口**，只有摘录） |
| `Karcanias_Vafiadis_1993_cover.txt` | Karcanias–Vafiadis |
| `lofberg2026_static_output_feedback.txt` | Löfberg 2026 |
| `trentelman2002.txt`、`verdier2012.txt`、`willems1981.txt`、`wonham_morse_1972.txt` | 各自来源 |
| `*.md` 三份（Fernando 两篇 + Warren–Eckberg）| 抽取，命名未统一（内容正确） |

## notes/

`LITERATURE_COMPLEXITY.md`（复杂度综述）、`LITERATURE_COVER.md`（覆盖与子空间）、
`LITERATURE_2026.md`、`SURVEY_2026-10-28.md`（四条线综述）、`LOFBERG_2026_*`、`LIU_2026_SOF_EXISTS_R.md`、
`BARKAI_2026_SOF_NP_HARD.md`、`MAJUMDAR_2026_ARM_ER.md`、`FERNANDO_2026_*`（四份）、
`DODIG_2008_row_completion.md`、`AHMADI_2026_OUTPUT_FEEDBACK.md`、`DESCRIPTOR_CONTROLLABILITY_INDICES.md`、
`LIT_SMITH_HERMITE_2026-11-01.md`、`LIT_REVIEW_2026-10-31_QA21_refs.md`、`P1P2_ASSUMPTIONS_CHECK.md`、
`OBSERVABILITY_REDUCTION_VS_LITERATURE.md`、`01_概念总结.md`、`02_文献摘录_证明相关.md`、`03_网络检索来源表.md`、`05_相关工作检索.md`。

## 已知勘误与缺口

- `pencils/Feedback_invariants_of_linear_multivariable.pdf` 的真实出处是 **Varga, MTNS 2004**（minimal dynamic covers），不是文件名暗示的作者。
- `txt/On_the_Dimensions_of_Controllability_Subspaces.md` 的作者是 **Warren–Eckberg**（SIAM J. Control 13(2), 1975），不是 Emre–Hautus。
- **Emre–Hautus (SIAM JCO 18(4), 1980) 全文仍缺**；Warren–Eckberg 1975 的 PDF 也缺。
- `self_bounded_2009.pdf` 曾是一个 229 B 的 HTML 跳转壳，已移入 `trash/`；该论文仍缺。
