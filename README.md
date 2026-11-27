# 最小增广行数问题（q1）—— 项目入口

> 最后更新：2026-11-27。规范见 [CLAUDE.md](CLAUDE.md)，现状见 [STATUS.md](STATUS.md)，项目脉络见 [HISTORY.md](HISTORY.md)，方向总表见 [ATTEMPTS.md](ATTEMPTS.md)，阶段论文见 [paper/](paper/README.md)，
> 证明 / Lean / 专家审的分工与下一步见 [workspace/ROADMAP.md](workspace/ROADMAP.md)。
> **2026-11-27 主线**：算法侧活跃方向已迁到 [workspace/q1_false/feasibility_geometry](workspace/q1_false/feasibility_geometry/README.md)（编号 545–662）；
> 硬度侧的“自由行 gadget”路线已关闭（见 [workspace/q1_true/multiplication_gate](workspace/q1_true/multiplication_gate/STATUS.md) 的 627/628）。

---

## 1. 问题

给定 $(A,C,L_0)$（$L_0$ 为 $r\times n$），求最小 $q$，使存在 $R$ 令 $\mathcal L=[L_0;R]\in\mathbb C^{q\times n}$ 满足

$$(5a)\ \operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]=\operatorname{rank}[\mathcal L;CA;C]\quad\forall\lambda .$$

**q1**：计算 $q_{\min}$ 是否 NP-hard？—— **仍开放**。

这等价于 Fernando–Trinh–Jennings（IEEE TAC 2010）最小阶功能观测器的阶数问题；他们给的是指数级枚举算法，不谈复杂度。详见 [docs/00_problem.md](docs/00_problem.md)。

### 1.5 论文引用约定（2026-11-26 起）

本仓库把两篇论文当作**参考文献**引用，**不复制、不复述**其内容：

- **Paper I** —— *Deciding functional observer feasibility: compression, certificates, and parameterized algorithms*（判定复杂度）。唯一来源：[q1-functional-observer](https://github.com/Zhengshuji/q1-functional-observer)。
- **Paper II** —— *Minimum order and minimum-order construction for functional observers*（最小阶与构造）。唯一来源同上。

下文写 "Paper I" / "Paper II" 时即指这两篇；需要核对时直接打开论文，**不再给仓库内的文件、章节或行号**。本仓库的 `paper/` 只保留 Paper III（超平面层）与 Paper IV（$c=2$）。

**依赖规则（2026-11-26）**：Paper I / Paper II 是它们**所覆盖结论**的可靠基准（压缩与块判据、沙包与结构界、
$\mathrm{DEC}\in\exists\mathbb R$、固定阶 XP、固定 $\ell$ 的 FPT、$q_{\min}=r_0+t_{\min}$、谱下界）。
本地材料**不因此一律降级**：论文未覆盖的、或本地进一步探索得到的固定成果，仍是本项目自己的结果，
按各自的 M/F 等级标注；只有本地陈述与论文**冲突**时，才以论文为准并就地改正。

---

## 2. 当前图景（一句话，2026-10-30 更新）

> **刻画已完成（文献）**：Fernando 2026 两篇（[P1] arXiv:2609.33615、[P2] arXiv:2609.37992）给出**逐阶完整刻画**：
> 阶谱 $\Sigma_{FO}\subseteq[q_0,n_0-p]$、每阶充要条件、$\nu_{\min}=\min\Sigma_{FO}$、构造；$q_0=\sum_j\eta_j$ 多项式可算。
> 其中 P2 Thm 5 的 $\exists Z$ **就是**本项目的 $\exists(\mathcal U,\mathcal H)$（换坐标）。
> 对照：[literature/notes/FERNANDO_2026_TWO_PAPERS_vs_PROJECT.md](literature/notes/FERNANDO_2026_TWO_PAPERS_vs_PROJECT.md)。

$$\boxed{\ \textbf{唯一还开放的}：\ \exists\Theta\ \text{（图卡}\times\text{半代数）的判定复杂度}\ \text{——这就是 }q1\ }$$

- **已被文献解决（不要重复"证明"）**：存在性、阶谱、逐阶充要、最小阶 = 最小谱可行阶、构造、$q_0$。
- **本项目的既有结果**（写作时必须降级为"对接/重新发现"，引用 P1/P2）：$\rho_{ci}=P(T,B,U_0)$（弱于 $q_0$）、
  层分解 $(\rho,c)$、格判据 C.1–C.5（Thm 5 的特例）、$\tau$ 消除（同 Thm 6 的 gcd 检验）。
- **可能独有**（先查文献再声称）：秩屏障 $\rho\le\min_\lambda r(\lambda)$、$\exists\mathbb R$ 框架、$d=4$ 的有限性观察。
- **已死**：四个闭式（[proof/refuted/](proof/refuted/README.md)）、拟阵/TAP 归约、**"可控性"刻画**（$\beta(\mathcal H)\subseteq B$ 恒为零）。

> **2026-11-08 最近（M2，未升 M3）**：$k=\omega\in\mathbf{RP}$、自由区 $q=3,\omega=2$ 的充要判据、
> 约束区一个 $n=5$ 层的全坏定理（其 $q_{\min}=4$ 结论已撤回，正确值 $q_{\min}=2$）。
> 三件的 Lean / 纸面 / 专家审分工见 [workspace/ROADMAP.md](workspace/ROADMAP.md)。

---

## 3. 目录

```
docs/        问题、记号、已证命题、引用定理、结构、开放问题、术语（只放正确的）
proof/       历史证明卷宗（2026-11-26 起不再维护；可复用的已复制到 workspace/q1_*/<子方向>/proof/）
tools/       按类别 + 场景索引：exact_linalg/ verification/ ledger/ layer_search/ p_algorithm/
             certificates/ lean/ hygiene/ presets/（见 tools/README.md 的“场景索引”）
literature/  仅参考文献：pdf/ txt/ papers/ notes/
archive/     按内容归档（不改、只读）：handovers/ expert_correspondence/ paper_drafts/ proof_audits/ …
trash/       回收站（登记后移入，不删除）
workspace/   核心工作空间
  q1_true/     硬度侧：README/STATUS/RESULTS/LESSONS + 子方向
               multiplication_gate/ rank_gates/ arm_reduction/
  q1_false/    算法侧：README/STATUS/RESULTS/LESSONS + 子方向
               c_stratification/ decision_algorithms/ feasibility_geometry/
  ATTEMPTS_INDEX.tsv  501 篇 attempts 的分层索引
  support/     功能目录：project_management/ fer26b_example_audit/ chatgpt_notes/
  _exchange/   Windows ↔ WSL 临时交换区（不入 git）
paper/       只放 Paper III / IV；Paper I/II 在 q1-functional-observer
HISTORY.md   项目脉络（怎么走到 q1；已撤回结论、论文叙述框架）
```

---

## 4. 两条方向

> **2026-11-26 整理**：下表是**历史方向表**。当前活跃工作只有
> [workspace/q1_false/](workspace/q1_false/README.md) 与 [workspace/q1_true/](workspace/q1_true/README.md) 两个大方向，
> 以及 [workspace/for_expert/](workspace/for_expert/)（对外材料）；
> Paper I/II 已迁到 [q1-functional-observer](https://github.com/Zhengshuji/q1-functional-observer)，
> `parametrization` 已归档（[archive/workspace_notes/](archive/workspace_notes/)）。
> 现状、任务分工与验收标准见 [workspace/ROADMAP.md](workspace/ROADMAP.md)。

| 方向 | 目标 | 现状 |
|---|---|---|
| [workspace/q1_true/](workspace/q1_true/README.md) | 证 MIN-ROWS 是 NP-hard | 6 条路线：拟阵/TAP（已死）、min-rank/覆盖、Z 形式、谱切割、图归约、线性截面 |
| [workspace/q1_false/](workspace/q1_false/README.md) | 证 $q_{\min}$ 多项式可算 | 8 条路线：$\dim V+1$（已推翻）、层公式、中间层、$\rho_{ci}$、贪心闭包、两值假设、二次型判据（有效）、$P$ 定理（已成功） |

---

## 4.5 复杂度类与底域（写论文前**必须**先钉住）

> 2026-10-30 补（HANDOVER2 的 Q4/Q5，作者与接手者一致同意）。

**（a）目标类：NP-hard 还是 $\exists\mathbb R$-hard？**
"层 $(\rho,c)$ 可行"是 $\exists(\mathcal U,\mathcal H,\tau)$ 的**半代数可行性**
（$\mathcal U$ 在 Grassmannian 上、$\tau$ 在仿射空间上，条件为多项式等式/不等式），
所以它**自然落在 $\exists\mathbb R$**。要得到 **NP-hard**，必须把连续量词显式消掉
（Grädel–Vorobjov 型的坑；旧笔记 `archive/session_history/proof/01_初始审查.md` 已警告过两次）。

$$\boxed{\ \text{两种结局都算 }q1\text{ 的答案：NP-hard；或 }\exists\mathbb R\text{-hard（"强 hard"但不是 NP-hard）}\ }$$

**（a'）已取得的上界（2026-10-31）**：$\mathrm{DEC}(q)\in\exists\mathbb R$ —— chart-free 编码，
变量与方程 $O(n^3)$、次数 $\le n$、只有 $O(n)$ 个 $s$ 的分支，见 [proof/dec_q_existsR/](proof/dec_q_existsR/README.md)。
其中核心引理 $\ker(CAZ)=Z\cap\mathcal V$ 与"左逆 ⟹ 单射"已 **Lean 验证**（`~/WorkSpace/lean4/MyProof/` (WSL)）。
**注意**：这是**上界**，不是 $q1$ 的答案；下界（硬度）或多项式算法仍未知。

**（b）底域：$\mathbb C$ 还是 $\mathbb Q$？**
$q1$ 的存在性是在 $\mathbb C$ 上问的（所有判据都按 $\mathbb C$ 写 ✓），而复杂度的输入/输出约定是 $\mathbb Q$。
二者**不等价**（docs/00 §0.1.1 的 $x^2+1$ 反例）。论文里必须先声明：
"**输入在 $\mathbb Q$ 上给、存在性在 $\mathbb C$ 上问**"，否则"可判定"与"复杂度"两句话不能并列。

---

## 5. 怎么读

> 框架的五个目标（方便接手 / 基础坚实 / 不重复研究 / 不重复错误 / 查找方便）与对应机制见
> [CLAUDE.md §0](CLAUDE.md)。**第一次接手请先读那一节。**

1. 想快速知道"到哪了" → [STATUS.md](STATUS.md)
2. 想查"某条路线试过没有" → [ATTEMPTS.md](ATTEMPTS.md)
3. 想做数学 → [docs/](docs/00_problem.md) + [proof/](proof/p_is_polynomial/README.md)
4. 想复现 → 各目录的 `README.md` 里有命令
5. 想知道"下一步做什么、谁该 Lean、谁该专家审" → [workspace/ROADMAP.md](workspace/ROADMAP.md)

## 交接

> 2026-11-01 的三步交接已完成（第 3 步确认见 `HANDOVER2` §10），两份文档已归档。日常接手读 README → STATUS → CLAUDE；历史交接见下。

- [archive/handovers/HANDOVER_2026-11-01.md](archive/handovers/HANDOVER_2026-11-01.md) —— **最新交接**（五分支、三条更正、开放问题、下一步）。
- [archive/handovers/HANDOVER2_2026-11-01.md](archive/handovers/HANDOVER2_2026-11-01.md) —— 接手方的**复核与三项异议**；§10 是第 3 步确认。
- [archive/handovers/HANDOVER_2026-10-31_final.md](archive/handovers/HANDOVER_2026-10-31_final.md) —— 上一份（2026-10-30：一句话现状 / 三张表 / 阅读顺序 / 八个坑）。
- [archive/handovers/HANDOVER2_2026-10-30.md](archive/handovers/HANDOVER2_2026-10-30.md) —— 第二任接手者的独立复核（10 个问题 + §82 证书的更正）。
- [archive/handovers/HANDOVER_2026-10-29.md](archive/handovers/HANDOVER_2026-10-29.md) —— 更早的一页速览（30 秒速览 / 已证 / 已否定 / 剩余两条路 / 复现命令）。

## 专家问答

- [archive/expert_correspondence/REPORT_FOR_EXPERT_2026-11-01_v2_EN.md](archive/expert_correspondence/REPORT_FOR_EXPERT_2026-11-01_v2_EN.md) —— **最新修订规格**（英文、自包含）：接受专家复核；改正商维数（秩是 $r+t$，不是 $h-s$）、证明商等价定理、重写 C0/C1/C2（删 C3）、**永久撤回**第二实例的 $q_{\min}=5$。
- [archive/expert_correspondence/REPORT_FOR_EXPERT_2026-11-01_EN.md](archive/expert_correspondence/REPORT_FOR_EXPERT_2026-11-01_EN.md) —— 被复核的 v1（保留作记录；§1 的维数句与 C2/C3 定义以 v2 为准）。
- [archive/expert_correspondence/REPORT_FOR_EXPERT_2026-10-30_EN.md](archive/expert_correspondence/REPORT_FOR_EXPERT_2026-10-30_EN.md) —— 上一份：项目现状 + 文献裁决（P1/P2 已完成刻画）+ 唯一靶子 DEC-$\Theta$ + 研究计划 + 5 个问题。
- [archive/expert_correspondence/QA_2026-10-29.md](archive/expert_correspondence/QA_2026-10-29.md) —— 提问 + 专家回复 + 更正记录（含 R4"多项式"说法的重要更正）。

## 技术报告

- [archive/paper_drafts/TECHNICAL_REPORT_2026-10-29.md](archive/paper_drafts/TECHNICAL_REPORT_2026-10-29.md) —— 已证结果、已否定路线、$q1$ 的精确剩余内容（一页可读的汇总）。
