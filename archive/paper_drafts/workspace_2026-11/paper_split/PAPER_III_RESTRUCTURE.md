# Paper III 重构规格（2026-11-21）

源：`paper/hyperplane/hyperplane_layer.tex`（1877 行，由 `build_single.py` 从 `hyperplane/src/` 合成）。
目标：`paper/current/paper_III_hyperplane.tex`。

**决策**：以合成后的 `.tex` 为**唯一事实源**（项目规范 §5.6）；`hyperplane/src/` 与 `build_single.py` 移入
`trash/hyperplane_src_2026-11-21/`，今后只维护 `paper/current/paper_III_hyperplane.tex`。

**原则**：搬移与引用，不重写数学。能整段搬的逐字复用；只改标题、过渡句、引言，以及明确指定的几处。

## 目标结构

```
I    Introduction            ¶1 问题 / ¶2 文献与缺口 / ¶3 成果+思路+结构
II   Standing results and notation
     A Results taken from Paper I
     B Results taken from Paper II
     C Notation specific to this paper
III  The hyperplane layer
     A The layer, its direction, and the direction theorem
     B Directions compatible with the prescribed rows, and the fibre
     C The complete parameterization
IV   The decision procedure
     A Charts, and the leading-coefficient claim
     B Certificates and the decision algorithm
V    Fixed-p bit complexity
     A The model and the bounds
     B The fixed-p theorem
     （收尾段落 The repeated case，2–3 句，指向附录 B）
VI   Discussion and conclusion
     A Limitations and what is not claimed
     B Reproducibility and evidence
A    Proofs of the estimates            （原附录 A，三段同源，不拆）
B    A repeated-eigenspace counterexample   （原 §6 整节 + 其展开数据）
```

## 动作

1. **文件头**：复制到 `paper/current/paper_III_hyperplane.tex`；`\title` 保留；前导区若缺
   `\newtheorem{claim}{Claim}` 则补上；删除原 `\section*` 或无编号的 Introduction 结构。

2. **Introduction**（原 57–171 行共 115 行，4 个子节）压成 3 段：
   - ¶1 = 原 "Problem, and what the companion papers settle"（26 行）压缩为约 10 行；
   - ¶2 = 文献与缺口（若原稿没有独立文献段，就从 ¶1 里拆出"companion papers settle / 缺口是什么"）；
   - ¶3 = 原 "Contributions"（35 行）+ "Strength of the claims"（9 行）合并，逐条给结论与位置；
   - 原 "Notation"（45 行）**整段移入 §II-C**，引言不再有记号。

3. **§II** 新建：
   - `A Results taken from Paper I`：原 §2 的 "The compressed criterion"（19 行）+ §4 的
     "Inherited tools"（37 行）+ §4 的 "Standing notation"（17 行）合并；每条写成**不带证明**的
     Claim/引文，注明 "Claim 2 / Claim 8 / Claim 11 / Theorem 1 of [companion I]"。
     **DEC 与 fixed-order 界的陈述放这里；若原稿的 fixed-p 位复杂度问题本质上是 [I] 的定理，
     只写"问题与已知答案"，不重复证明。**
   - `B Results taken from Paper II`：沙包与子空间图像、结构界、最小阶与谱下界，同样只陈述、
     注明 "Claim 3/4/6, Prop 2/3 of [companion II]"。
   - `C Notation specific to this paper`：原 §2 的 "Basic notation"、"Standing assumptions"、
     "Direction and the two functionals"、"Quantities used below"、"Parameter space and chart
     conventions" + 原 intro 的 "Notation" 合并；保留各自的定义，按"系统与块结构 → 方向与泛函 →
     参数量与图卡"三段顺序排列，段间各一句过渡。

4. **§III**：原 §3（299–606）六个子节 → 三个：
   - A = 原 "Notation added here"（12 行，并入 A 的开头）+ "The layer, its direction, and the
     direction theorem"（87 行）；
   - B = 原 "Directions compatible with the prescribed rows"（30 行）+ "The fibre over a
     direction"（79 行）；
   - C = 原 "The complete parameterization"（45 行）+ "Duality with the compressed formulation"
     （40 行，降为 C 的末尾一段，标题改 `\paragraph*{Duality with the compressed formulation}`）。
   - 节首加 2–3 行总起。

5. **§IV**：原 §4（607–916）六个子节 → 两个：
   - 先删掉已移入 §II-A 的 "Standing notation" 与 "Inherited tools"；
   - A = "Charts and their size"（94 行）+ "The full-rank leading-coefficient lemma"（47 行），
     后者降为 Claim；
   - B = "Real designs and certificates"（50 行，降为 Claim）+ "The decision algorithm"（52 行，
     Theorem 保留）；
   - 节首 2 行总起；节尾一句小结。

6. **§V**：原 §5（917–1171）六个子节 → 两个 + 收尾段：
   - A = "Geometric simplicity"（17 行）+ "Arithmetic model for the number field"（35 行）+
     "The bounds"（114 行，三条界降为 Claim）；
   - B = "Main theorem"（43 行，Theorem 保留）+ "Standard facts used"（13 行，并入 B 末尾段落）；
   - 收尾段 = "The repeated case: what the counterexample does and does not show"（23 行），
     标题改 `\paragraph*{The repeated case}`，末尾指向附录 B。
   - 节首 2 行总起。

7. **§VI**：原 §6（1172–1606）整节移入附录 B，保留其子节结构（Notation / The instance /
   Direction geometry / Decisions for six directions / Certificates / The precise wording /
   Relation to the fixed-parameter theorem / 展开数据 / Reproduction），只做三件事：
   - `\section{A repeated-eigenspace counterexample}\label{app:example}`；
   - "The precise wording of the conclusion" 与 "Relation to the fixed-parameter theorem" 合并为
     一个子节 `What the counterexample does and does not show`（若后者确实在批评 [I] 的 FPT 定理，
     把其中属于"限定"的内容移入 §VI-A Limitations，并在附录保留一句指针）；
   - 正文所有 `Section~\ref{sec:counterexample}` 改为 `Appendix~\ref{app:example}`。

8. **§VI（Discussion and conclusion）**：原稿若有 Conclusions 节则改名；若无则新建两个子节
   （Limitations / Reproducibility），内容从原稿的"strength of claims"与"reproduction"两处搬。
   附录 A 保留 `\section{Proofs of the estimates}`（272 行，三段不拆）。

9. **环境政策**：Theorem 保留 4 个（方向定理、参数化、判定、位复杂度）；Proposition 最多 2 个
   （纤维维数、首项系数——若它们本质是引理则降 Claim）；其余 `lem` 全部改 `claim`；4 个
   `definition` 保留。每个 Claim 前加一句用途句（统一句式 "The purpose of this step is …"）。

10. **过渡**：每个 section 开头 2–3 行总起；§III/§IV/§V 各子节末尾一句承前启后；§II-C 三小段之间
    各一句过渡。

## 验收
两遍 `pdflatex`：`Output written`、`!`=0、`Reference ... undefined`=0、`Citation ... undefined`=0、
`Overfull`=0。目标 **12–16 页**。
另报：最终 tree、环境统计、四条 [I]/[II] 引用的实际条目名、以及原稿中与新结构冲突、需要你判断的地方。
