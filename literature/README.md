# literature/ — 参考文献

> **只放参考文献**（论文、教材、抽取文本、阅读笔记）。不放本项目的结论。
> 文件级索引见 **[INDEX.md](INDEX.md)**；文献总表见 **[REFERENCES.md](REFERENCES.md)**。

| 目录 | 内容 |
|---|---|
| [pdf/](pdf/) | 18 篇 PDF，按主题分五个子目录：`foundations/`（BPR、Renegar I/II、Trentelman、最小多项式、Verdier）、`observer/`、`pencils/`、`algebra/`、`complexity/`；命名 `Author_Year_短标题.pdf` |
| [txt/](txt/) | 抽取/转写的文本（`tsh.txt` 403 页教材、`fernando2010.txt`、`wonham_morse_1972.txt`、`willems1981.txt`、`verdier2012.txt` 等）|
| [papers/](papers/) | 2026 年 arXiv 论文，**pdf 与 txt 成对**，按 arXiv id 命名（Fernando 两篇的**正本在此**）|
| [notes/](notes/) | 阅读笔记：`LITERATURE_2026.md`、`LITERATURE_COMPLEXITY.md`、`LITERATURE_COVER.md` 等 |

## 与项目的关系

| 文献 | 用法 | 详见 |
|---|---|---|
| Fernando–Trinh–Jennings 2010 | 问题的真身（Condition 1/2 = $(5a)/(5b)$）| [docs/03](../docs/03_theorems_cited.md) 引用 1 |
| Wonham–Morse 1972 | $D\subseteq B$ 时 $(A,B)$-不变 = c.s. | 引用 2 |
| Warren–Eckberg 1975 | c.s. 版最小维数 **open** | 引用 3 |
| Karcanias–Vafiadis 1993 | cover 版 open | 引用 4 |
| **Emre–Hautus 1980** | **待读**（决定 $P\in\mathbf P$ 是否新结果）| 引用 5 |
| Kleiman–Krener | 闭包算法（$B=0$ 端点）| 引用 6 |
| Trentelman–Stoorvogel–Hautus 2002 | 标准教材（无最小维数结果）| 引用 7 |

## 缺口

- **Emre–Hautus (SIAM JCO 18(4), 1980)** 全文未取；项目只在其引用里见过它（`txt/tsh.txt` 参考文献第 43 条）。
- Warren–Eckberg 1975 的 PDF 未入库（只有转写/摘录）。

## 待补 / 已知问题（2026-10-27 审计）

| 项 | 状态 |
|---|---|
| Wonham–Morse? 不需要 | — |
| **self-bounded 论文**（2009）| ❌ **缺**：`pdf/self_bounded_2009.pdf` 只有 229 B 的 HTML 跳转壳，已移入 `trash/`。`archive/expert_correspondence/GAP_追问_self-bounded与多值情形.md` 需要它的定义原文 |
| 两篇 Fernando 新论文 | ⚠️ **重复**：`papers/2609.33615.pdf` = `pdf/A Minimum-Order ... .pdf`；`2609.37992.pdf` = `pdf/Complete Characterization ... .pdf`（内容 hash 相同）|
| `txt/` 下两篇是 `.md` 而非 `.txt` | 命名不一致（内容正确）|
| `archive/data/p1..p3*.txt` | 同一批论文的**早期抽取版本**（尺寸不同），与 `txt/` 重复 |

## 关键复杂度参照（2026-10-28 新增）

| 论文 | 结论 | 对本项目的意义 |
|---|---|---|
| **Löfberg, _Static output-feedback stabilization is NP-hard_**（arXiv:2609.16886, 2026-09）| SOF1（$\exists K\!:A+BKC$ Hurwitz）**NP-hard**（归约自 Betweenness；$D=6(m+n)$）；推论 3.3：仿射参数化多项式族含 Hurwitz 成员问题是 NP-hard | **否定了"NP-hard 只在结构型问题上"的启发式**——数值型控制问题也能 NP-hard；且给出可迁移的归约模板（三次源 + Routh 符号 + 频率分离 + anchor）。见 [workspace/q1_true/attempts/08_sof_betweenness.md](../workspace/q1_true/attempts/08_sof_betweenness.md) |

## 参考文献总表

**唯一**的文献索引：[REFERENCES.md](REFERENCES.md)（作者/出处/用途/全文位置）。

## 综述与检索（先读这两份，避免重复劳动）

| 文件 | 内容 |
|---|---|
| [notes/SURVEY_2026-10-28.md](notes/SURVEY_2026-10-28.md) | 四条线（设计算法 / 几何理论 / 铅笔-Kronecker / 复杂度）的综述 + "不要重复做"索引 + 待读清单 |
| [SEARCH_LOG.md](SEARCH_LOG.md) | 检索查询式、日期、命中；含检索缺陷反思 |
| [notes/LOFBERG_2026_GADGETS.md](notes/LOFBERG_2026_GADGETS.md) | Löfberg 2026 的六个可迁移归约 gadget |

## ⚠️ 文件名勘误

`txt/On_the_Dimensions_of_Controllability_Subspaces.md` 的**真实作者是 Warren–Eckberg**（SIAM J. Control 13(2), 1975），
**不是** Emre–Hautus。Emre–Hautus 1980（SIAM JCO 18(4)）**仍未获取**——它是判断 $P\in\mathbf P$ 新颖性的关键。
另外 `pdf/Feedback_invariants_of_linear_multivaria.pdf` 实为 **Varga, MTNS 2004（minimal dynamic covers）**。
