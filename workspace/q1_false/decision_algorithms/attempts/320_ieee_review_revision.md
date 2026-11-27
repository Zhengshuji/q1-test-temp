# 87 号评审（学术版）落实：版式、摘要、措辞与若干修正

> 2026-11-10。第二轮学术评审（基于 13 页 IEEEtran 版）：**major revision**，但明确
> "不建议放弃或根本改变研究方向"，并把贡献排序为：有效自由维数（最高）→ FPT（最高）→
> $r=0$ 多项式判定（高）→ 压缩（高）→ 固定 $q$ XP（中）→ $\exists\mathbb R$ 归属（中）。
> 本轮只做**版式与表述**类（用户明确要求的三项 + 低成本修正），数学审计类留待后续。

## 目标

按用户要求完成三件事：去掉作者块；节标题改罗马数字；修表格排版。并采纳评审中
"低成本、不动数学"的表述修改。

## 设想与理由

评审列了 10 条 issue，其中 4 条是 Critical/Major 的**数学审计**（Bézout 证明、Gram/Cauchy–Binet
推导、固定 $q$ 编码的 soundness/completeness、FPT 位长审计），这些需要逐条重写证明，
不是一轮能做且做对的事。其余是版式、摘要、措辞、文献、记号冲突——可以当场落实。

先把版式做对（用户直接要求），再改表述（低风险、提升可读性），最后记录剩余清单。

## 做法

### 1. 用户要求的三项

* **作者块**：`\author{}` 留空（评审建议保留匿名；用户说暂不需要真实信息）。
* **罗马数字节号**：把 `\section*{1. Introduction}` 之类的**手写编号**换成 IEEEtran 计数器
  （`\section{Introduction}`），于是显示 `I. INTRODUCTION`、子节 `A. The problem`。
  正文里 12 处 `\Sx.y` 引用改为 `\ref`：例如 `\S8.1` → `Section~\ref{sec:zero}`，编译后显示
  "Section VIII-A"。附录仍用 `\appendices` + `\section{...}`（显示 APPENDIX A），
  附录内的 `A.1`、`A.5.1` 保持手写（正文大量按这些标号引用）。
* **表格**：此前 `\caption` 放在 `\toprule` **之后、tabular 之内**，结果落进第一列表格单元。
  现在改为 `\centering → \caption → \small → \begin{tabular}`，并加 `\label{tab:N}`。

### 2. 评审中可当场落实的表述项

| 评审条目 | 落实 |
|---|---|
| 摘要"像定理清单" | 按评审给的模型重写：问题 → 第一个结果 → 主结果 → $r=0$ → $\exists\mathbb R$ → 限制 |
| "self-contained stage report" | 改为"本文处理规定阶可行性的计算复杂度，而非再给一次刻画" |
| "None of these is new" | 改为"各成分是经典的；贡献在于它们的算法组合" |
| "monomer by monomer" | 改为 "term by term" |
| "The cheapest first step" | 改为 "A natural first refinement" |
| "A word on the size of $f$" | 改为 "Growth of the parameter-dependent factor"，并去掉口语化收尾 |
| "Kronecker reading (corrected)" + 草稿史括注 | 改为 "Interpretation in Kronecker canonical form"，删去历史括注 |
| "residual obligation is bookkeeping" | 改为"剩余问题是完成显式的位复杂度审计" |
| "secondary XP-type result" | 改为"complementary XP-type upper bound" |
| 阈值与 $q\le n$ 不一致 | `\bigvee_{q=r_0}^{Q}` → `\bigvee_{q=r_0}^{\min(Q,n)}` |
| 文献细节 | Darouach–Fernando 补卷 173/文号 112115/DOI；Renegar、Emiris–Mourrain 补 DOI |
| 两栏下 `DEC(q)` 定义式溢出并与右栏重叠 | 改为 `aligned` 两行 |

### 3. 编译与检查

`pdflatex` 两遍：13 页，0 error，0 overfull hbox，0 undefined reference。
抽查第 1、2、7 页：标题页（无作者、新摘要、I./A.）、TABLE I/IV（caption 在表上方、booktabs 线）、
Lemma 8.1 与 Corollary 2a 环境。

### 4. 工具问题（记录）

`paper/current/others/q1_parametric_algorithms.pdf` 被预览进程独占，`Copy-Item`/`del` 均被拒绝。
用 `git hash-object -w` + `git update-index --cacheinfo` 把新 PDF 直接写入索引并提交
（HEAD 中的 blob 已是新版，373046 字节）；worktree 里的旧文件暂时保留并标
`--assume-unchanged`，待锁释放后 `git checkout -- <pdf>` 同步。

## 进展

* 三项用户要求全部完成；
* 12 处节引用、4 张表、摘要、9 处措辞、2 处文献、1 处阈值、1 处溢出公式已改；
* 提交 `6b41ef7`；PDF 的新 blob 已在 HEAD 中。

## 最终结论

版式已达到 IEEE 期刊的样子（罗马数字节号、无作者块、表格 caption 在上、编号文献）。
**数学审计类 issue 未做**，它们才是评审判 "major revision" 的原因，清单见下。

## 剩余（评审的数学审计，按优先级）

1. **Bézout 度界（Lemma D1）**：把"两个组合、有限个真子空间不能覆盖"写成正式命题。
2. **Gram 证书**：显式区分行向量与其转置列表示；说明实代数（共轭转置需另处理）。
3. **Cauchy–Binet**：给 $\omega=2$ 的完整小例子（子式 → 系数向量 → $B$ → $B^\top B$ → 由 $K$ 复原）。
4. **固定 $q$ 编码**：把 soundness/completeness 拆成独立命题（评审给了建议的命题形式）。
5. **FPT 位长审计**：把 $N,s,D,B$、构造代价集中成一条参数化复杂度引理。
6. **记号冲突**：$B$ 同时是秩因子与系数矩阵——建议改为 $H=XR$ 与 $Z$（评审强烈建议）。
7. **验证状态表**（附录 C）：区分 Lean / 纸面 / 精确验证。
8. **文献对比**：Table II 需要实质技术比较，而不只是"分工"。

## 放弃原因

不适用。本轮有意不做 1–8：它们各自需要重写证明段落，混在版式修改里会难以核对。

## 残留价值

* 版式可复现（`.tex` 唯一来源，两遍 `pdflatex`）；
* 一份可直接照着做的 8 项审计清单（含评审给出的命题形式与表格样式）；
* 记录了 PDF 被占用时的 git index 变通做法。

## 相关文件

* [论文](../../../../archive/paper_drafts/pre_split_baseline_2026-11/others/q1_parametric_algorithms.tex) · [PDF](../../../../archive/paper_drafts/pre_split_baseline_2026-11/others/q1_parametric_algorithms.pdf)
* [REVIEW_NOTES](../../../../trash/paper_root_2026-11-21/REVIEW_NOTES.md)（第一轮风险说明，仍有效）
* [86 号报告](../../../for_expert/archive/86_referee_report_paper.md)（上一轮）
* [STATUS](../../../../STATUS.md)
