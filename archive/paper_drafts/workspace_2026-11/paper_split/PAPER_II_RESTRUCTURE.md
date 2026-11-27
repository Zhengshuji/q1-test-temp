# Paper II 重构规格（2026-11-20）

对象：`paper/current/paper_II_minorder.tex`。旧版已归档（只读）：
`archive/paper_drafts/paper_II_minorder_v1_2026-11-20.tex`。

**原则**：搬移与引用，不重写数学。凡能整段搬的**逐字复用**；只改标题、过渡句、引言、以及明确要求的几处文字。

## 目标结构

```
I    Introduction         ¶1 问题 / ¶2 文献与缺口 / ¶3 成果+思路+结构（合并原 Contributions，删 Roadmap）
II   Preliminaries        A Notation / B The observer conditions / C The three problems
                          D Standing results from the companion paper   ← 新增（取代原 §III.A–C）
III  The minimum order and its spectral bound
     A Monotonicity, saturation, and the minimum order
     B The spectral lower bound, and when it is attained
IV   Computing and constructing
     节体：接口思想 + Theorem 1（Interface）
     A Minimum order by binary search        Algorithm 1 + Corollary（OPT）
     B Constructing a minimum-order observer Procedure FIND + Remark（witness system）+ Corollary（FIND）
     节尾：2–3 句散文（bit / arithmetic / open）
V    Discussion and conclusion   A Limitations / B Reproducibility
A    A published value corrected（原 §VI 整节移入）
```

## 逐项动作

### 1. 引言
- ¶1 保留。
- ¶2 重写为"文献与缺口"：①刻画已完备（fer10、dar25、fer26a、fer26b）；②现有下界只有代数一侧 $q_0=\sum_j\eta_j$，谱条件只被当作逐阶检验；③因此留下"阶集合结构 + $q_0$ 与 $q_{\min}$ 的阶差"两个问题。
- ¶3 = 原 Contributions + 原 Roadmap 合并：先给链（结构 → 单调/饱和 → $q_{\min}=r_0+t_{\min}$ → 谱下界 → 取等刻画 → 接口定理），再逐条给结论带位置；最后一句"附录 A 给出一个已发表值的更正"。
- 删除 `\paragraph*{Contributions and organization}` 与 `\paragraph*{Roadmap}` 两块。

### 2. §II 新增 D
- 新子节 `\subsection{Standing results from the companion paper}\label{sec:standing}`，开篇一句："This section restates, without proof, the setting and the four results of the companion paper [companion1] on which everything below rests."
- 用 `\begin{claim}` 逐条陈述（**不证**，每条末尾注明对应条目，如 "(Lemma 5 of [companion1])"）：
  - D.1 压缩与 pencil 形式：(5a) ⟺ row H_A ⊆ row H；(5b) ⟺ rank(λH−H_A)=ω ∀λ；两者 ⟹ rank H_A = rank H
  - D.2 可达行对：$M=[N\ AN]$、$\mathcal T=\operatorname{row}M$、$d_0=\operatorname{rank}[N\ AN]$、自由行由 $d_0$ 个坐标描述
  - D.3 沙包：DEC(q) ⟺ 存在 W 使 $W_0\subseteq W\subseteq\mathcal T$、$\dim(W/W_0)\le r$，且两条件只依赖 W
  - D.4 结构界：$\omega+1\le\dim W\le2\omega$，且 $\pi_1(W)=\pi_2(W)\subseteq S$
- 这些陈述的**原文**来自现 §III-A/B/C/D 的对应片段，逐字搬移（去掉各自的 proof）。
- 删掉现 §III 的 `\section{Setting and the reduction}` 及其四个子节（内容已上移）；原 §III-D 末尾的 `\paragraph*{The projection lies in S}` 内容可并入 D.4。

### 3. 新 §III
- `\section{The minimum order and its spectral bound}\label{sec:minorder}`
- 节首 2 行总起："Two things are proved here: that the set of feasible orders has a simple shape, and that the spectral condition alone yields a lower bound on its minimum."
- `\subsection{Monotonicity, saturation, and the minimum order}\label{sec:monotone}`：原 monotonicity claim + Prop（minimum order），原样搬移；小标题里的 label 保留 `sec:monotone`。
- `\subsection{The spectral lower bound, and when it is attained}\label{sec:lowerbound}`：原 lower-bound Prop + 其后的"与文献下界的关系"段 + 原 tightness Prop + 原 tightness Remark，原样搬移。
- **在该关系段里补一句**（新内容，仅一句）："When $\operatorname{rank}[U_0;V_0]\le s_0$ the bound is vacuous while $q_0$ may be positive, so neither bound dominates the other." （这是审稿人会问的缺口，必须补）
- 节尾一句小结，指向 §IV。

### 4. 新 §IV
- `\section{Computing and constructing}\label{sec:compute}`
- 节首 3–4 行总起 + 直接放 `\begin{thm}[Interface]`（原样）。原 §IV 的 `\subsection{An interface...}` 之类的标题删掉，定理进节体。
- `\subsection{Minimum order by binary search}`：Algorithm（OPT）+ 其 Corollary，原样。
- `\subsection{Constructing a minimum-order observer}`：Procedure FIND + `\paragraph*{The witness system}`（原附录"witness system"整段搬入，作为该子节的一段，五项约束逐条列出）+ Corollary（FIND）原样。
- **删除原 §IV 的 `\subsection{Two models, and what is open}`**，改为节尾 2–3 句散文：
  "Deciding the minimum order is bounded in the bit model; the construction is bounded only in the arithmetic model, and its bit complexity is open." + 一句条件性说明（引用 §II-D 的 DEC 谓词）。

### 5. 结论与附录
- `\section{Discussion and conclusion}\label{sec:conclusions}`（原 `\section{Conclusions}`），保留其两个子节（Limitations / Reproducibility）。
- 原 §VI（`An incorrect published minimum-order value`）整节移入附录：在文件末尾放 `\appendices` + `\section{A published value corrected}\label{app:example}`，内容逐字搬移；把节内所有 `Section~\ref{sec:example}` 改为 `Appendix~\ref{app:example}`。
- 若原文件有 `\appendices` 与 witness-system 附录，删除那一个（内容已进 §IV-B）。

## 验收
两遍 `pdflatex`（scratch 副本）：`Output written`、`!`=0、`Reference ... undefined`=0、`Citation ... undefined`=0、`Overfull`=0。目标 **8 页**。
另报：最终 section/subsection 树、环境统计（thm/prop/claim/cor/remark）、以及新 §II-D 里四条 Claim 的编号。
