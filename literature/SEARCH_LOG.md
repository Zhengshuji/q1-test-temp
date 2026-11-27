# 文献检索日志与我的检索缺陷（2026-10-28）

> 触发：用户指出 `literature/pdf/complexity/Lofberg_2026_SOF_stabilization_NP_hard.pdf`（Löfberg 2026）
> 是本项目的**关键**文献，而我此前**从未找到它**。本文记录原因、教训与补救。

## 1. 我为什么会漏掉它（四条具体缺陷）

### D1 把"文献综述"当成一次性的、已完成的继承物

项目的 `literature/` 是 2026-10-24 冻结的；我这几十轮里**没有一次**重新检索，
只是反复引用已有笔记（`LITERATURE_2026.md` / `LITERATURE_COMPLEXITY.md` / `LITERATURE_COVER.md`）。
$$\text{后果：任何 2026-10-25 之后出现的结果都不可能被发现。}$$

### D2 按"对象名"检索，而不是按"决策问题形状"检索

我搜的是 "minimum order functional observer"、"min-rank"、"copositivity" 这类**对象名**。
但 Löfberg 的论文标题里**没有** observer / functional / minimum order（全文 0 命中）——
它讲的是 **static output feedback stabilization**。

$$\text{而我真正要检索的是"\ }\exists K:\ A+BKC\ \text{Hurwitz}\text{"这个**形状**，不是"functional observer"这个词。}$$

### D3 "已知 NP-hard 邻居"表只收了**结构型**问题

项目笔记里的邻居表（sensor placement、min input selection）全是 0/1 结构型；
它**系统性遗漏**了"控制论里的判定问题"这一整条线：Blondel–Tsitsiklis、Toker–Özbay、Fu–Luo、**Löfberg 2026**。

### D4 没有"复查日期"机制

我没有任何"每隔 N 天重搜一次"的机制，也没有查询日志，所以无法发现覆盖缺口。

## 2. 补救：检索协议（已写入 CLAUDE.md 纪律 19）

1. **每次动一个命题之前，先做一轮检索**（不是每个会话一次，而是每个命题一次）；
2. **按问题形状检索**：把待证/待否的命题写成"$\exists$ 参数 + 条件"的形状，再用形状里的术语检索
   （例：`"∃ gain" "Hurwitz" NP-hard`，而不是 `functional observer NP-hard`）；
3. **固定查询清单**（每次至少跑一遍）：
   - `"<对象名>" NP-hard / complexity / polynomial`
   - `static output feedback NP-hard`, `simultaneous stabilization NP-hard`, `BMI feasibility NP-hard`
   - `complexity of <相邻设计问题>`（observer / sensor / actuator selection）
   - `arXiv <年份> complexity control hardness`
4. **记录到本文件**：查询式、日期、命中的新文献、判定（相关/不相关/待读）；
5. **复核"邻居表"**：每次新增一条复杂度文献，都要问"我们能不能从它归约/被它归约"。

## 3. 本次检索记录（2026-10-28）

| 查询式 | 命中 | 判定 |
|---|---|---|
| `minimum order functional observer computational complexity NP-hard` | Fernando 2024/2026 系列、Montanari 等 | 都只给**算法**，不谈复杂度类 |
| `functional observability design complexity NP-hard polynomial` | Zhang–Fernando（sensor placement）、Montanari（target observability）| **结构型**硬度（已知）|
| `Löfberg static output feedback NP-hard arXiv 2026` | **arXiv:2609.16886** | **关键命中**（本项目最重要）|
| `hardness results for structured linear systems` | FOCS 2017 | 结构型硬度（已知一类的总纲）|
| `A Polynomial Characterization of (A,B)-Invariant and Reachability Subspaces` | SIAM JCO **1978** | **Emre–Hautus**（这正是 Q3 要读的那篇！）|
| `minimum order observers for discrete-time systems` | Springer 2011 | 工程算法，谈复杂度无关 |
| `almost (A,B)-invariant subspace minimum dimension complexity` | Willems 1981 类 | 无复杂度结论 |

**结论**：截至 2026-10-28，**没有**查到"最小阶功能观测器"的复杂度类结果；
最近的判定问题是 Löfberg 的 SOF1（NP-hard）。所以 **$q1$ 开放**这一判断仍然成立 ✓，
但"用数值型数据 ⟹ 不易"这条启发式**已被证伪**。

## 4. 新增待读清单

| 文献 | 为什么必须读 |
|---|---|
| **Emre–Hautus**, SIAM J. Control Optim. 18(4), 1980（"A Polynomial Characterization of (A,B)-Invariant and Reachability Subspaces"）| 决定 $P\in\mathbf P$ 是否**新结果**；可能已有多项式算法 |
| **Hardness Results for Structured Linear Systems**（FOCS 2017）| 结构型硬度的总纲；判断我们能否借用其归约骨架 |
| **Toker–Özbay**（BMI feasibility / simultaneous stabilization NP-hard）| 与 SOF1 同族，可能含更贴合的 gadget |
| **Fu–Luo**（fixed-order output feedback 的矩阵不等式）| 同上 |
| **Blondel–Tsitsiklis** 综述（complexity of control）| 提供"哪些判定问题已定、哪些开放"的全表 |

## 5. 本次检索记录（2026-10-30，接手者；目标 = $q1$）

| 查询式 | 命中 | 判定 |
|---|---|---|
| `minimum order functional observer NP-hard complexity` | **arXiv:2609.33615**（Fernando，2026-09-27 提交）、Larroque 等（HAL）、IEEE 2021（分布参数）| 见下 |
| `functional observer minimal order computational complexity` | 同上 + 工程类实现（Springer 2011 一类）| 无复杂度类结论 |
| `minimum rows matrix augmentation functional observability complexity` | 同上，无新判定结果 | 无 |

**关键命中：arXiv:2609.33615**（T. Fernando, *A Minimum-Order Functional Observer Beyond the Darouach and Luenberger Constructions*, submitted 27 Sep 2026）。
摘要要点（**逐字核对过**）：给出 $q_0=\sum_j\eta_j$（= 本项目的 functional observability indices / $\eta_j$ 构造）、
**"minimum condition-(A) augmentations 的**完整族**"**、以及 $\nu_{\min}=q_0$ 的**充要谱条件**；
条件 (A)/(S) 与本项目的 $(5a)/(5b)$ 逐项相同。

$$\boxed{\ \text{它恰好覆盖本项目的开放量词：}\exists(\mathcal U,\mathcal H)\text{ 的"完整族"}\ }$$

**判定**：摘要里**没有**任何复杂度类声明（no NP-hard / no polynomial-time algorithm 的说法）；
所以 $q1$ **仍开放** ✓。但它**必须读**——需确认两件事：

1. 它对"完整族上的 (S)"给的是**判定算法**还是**存在性刻画**（若是前者，层判定就可判，$q1$ 可能为假）；
2. 它的"完整族"参数化是否与项目的 $(\mathcal U,\mathcal H,\tau)$ 同构（若是，可直接借用或对照）。

**结论（2026-10-30）**：截至今日，**没有**查到最小阶功能观测器的复杂度类结果；$q1$ 开放 ✓。
新增待读：**arXiv:2609.33615**（优先级最高，直接对着 $\exists(\mathcal U,\mathcal H)$）。
## 2026-10-30：矩形铅笔 rank-drop / ∃R 硬度（QA10 §6.3 的建议）

- 查询：exists R hardness matrix pencil rank drop / existential theory of reals complete matrix pencil / rational matrix pencil singular rank NP-hard
- 命中：均为一般矩阵铅笔文献（Kronecker 形、Ay=λBy 的根），**没有** ∃R-硬度结果
- 结论：抽象矩形铅笔的 rank-drop 是多项式可判的（见 [workspace/q1_true/attempts/03_hardness_pencil.md](../workspace/q1_true/attempts/03_hardness_pencil.md)）；硬度必须来自实现约束
## 2026-10-31 · A2.4 除子情形 → 共同补空间

**动机**：A2.4 把除子情形等价为"一族 $r$ 维子空间 $\{J_\lambda\}$（线性铅笔的对偶像，是一条有理曲线）
是否有共同补空间 $W$（$\dim m-r$）使 $W+J_\lambda=K^*$ 对一切 $\lambda$"。

**查询式**：
- `common complement of a family of subspaces exists criterion`
- `family of subspaces common complement finite dimensional algebraic criterion`
- `rational curve Grassmannian avoids a subspace dimension count`

**命中**：
- [Common Complements of Linear Subspaces and the Sparseness of MRD Codes](https://pure.tue.nl/ws/portalfiles/portal/240233203/21m1428947.pdf) —— 有限域上的共同补空间，MRD 码语境；**不是**我们的有理曲线族。
- [Subspaces with a common complement in a Banach space](https://ar5iv.labs.arxiv.org/html/0805.4707) —— 无限维 Banach 空间，**不适用**。
- [Well-separating common complements ... Hilbert space are generic](https://ar5iv.labs.arxiv.org/html/1906.08514) —— Hilbert 空间、泛型性；与"是否存在"不同。
- [Subspace Arrangements (Björner)](http://www.math.ucdavis.edu/~deloera/MISC/LA-BIBLIO/trunk/Bjornner/Bjornersubspacearrangements.pdf) —— 子空间排列理论；相关但未给出本问题的判据。
- [Minimal Bases of Rational Vector Spaces (Forney 纪念文集)](https://www.math.uzh.ch/fileadmin/user/rosen/publikation/forneyfest_16.pdf) —— 有理向量空间的极小基；与我们"多项式基 + 次数界"相邻。

**结论**：**没有**找到直接适用"有理曲线族的共同补空间存在性"判据。文献集中在
(a) 有限域/MRD 码、(b) 无限维 Banach/Hilbert 空间、(c) 子空间排列的拓扑。
本问题的"线性铅笔诱导的有理曲线族"似乎不在这些框架内 —— 既不能说它可判，也不能说它难。

**可再查的方向**：`linear relation pencil common complement`、`Kronecker canonical form feedback`、
`subspace family transversal dimension count rational normal curve`。
## 2026-10-31 · QA21 提供的文献（专家给出，未逐篇核验）

| 主题 | 文献 | 用途 |
|---|---|---|
| 线性截面 / G3 | Harris《Algebraic Geometry: A First Course》；Eisenbud《Commutative Algebra》；Cox–Little–O'Shea《Ideals, Varieties, and Algorithms》；Aprodu–Spiridon, *Linear Sections of Grassmannians and Resonance of Vector Bundles* (2025) | $(\sqrt I)_1$ 判定 span(X) |
| Schubert 覆盖 | Abdelkerim–Coskun, *Parameter spaces of Schubert varieties in hyperplane sections of Grassmannians*, JPAA 216 (2012) 800–810 | 除子情形 |
| 共同补空间 | Clark–Shekhtman, LMA 49 (1995) 1–13；PAMS 125 (1997) 251–254（有限族最小 $k(n-k)+1$）| 对照：我们的问题是**无限族** |
| ∃R 硬度 | Kim–de Mesmay–Miltzow, *Representing Matroids over the Reals is ∃R-complete*, DMTCS 26:2 (2024)（含秩 3）| 潜在 gadget 源 |
| 铅笔次数界 | Forney, SIAM J. Control 13 (1975) 493–520；Noferini–Van Dooren, LAA 658 (2023) 86–115, Lemma 5.2 | 替代 PBH 的左逆次数界 |

**用法**：Noferini–Van Dooren Lemma 5.2 已写入 [proof/dec_q_existsR/README.md](../proof/dec_q_existsR/README.md) 的路线 A；
其余为待读。**注意**：专家提醒 matroid 可实现性**不直接**给出 DEC(q) 的硬度（须保持铅笔结构）。

## 2026-11-01/02（专家提供，待我们自行检索核对）

| 日期 | 查询 | 命中 | 备注 |
|---|---|---|---|
| 2026-11-01 | static output feedback stabilization complexity | Liu, arXiv:2610.00390（$\exists\mathbb R$-complete）| 专家引用；我们**尚未**独立读全文 |
| 2026-11-01 | static output feedback NP-hard | Löfberg, arXiv:2609.16886 | 专家引用；已在 docs/07 §9 登记 |

**2026-11-02 更新**：两篇均已读（HTML 版），笔记见 [notes/LIU_2026_SOF_EXISTS_R.md](notes/LIU_2026_SOF_EXISTS_R.md)、
[notes/LOFBERG_2026_SOF_NP_HARD.md](notes/LOFBERG_2026_SOF_NP_HARD.md)；docs/07 §9 已补定理级摘要。
**待办**：Barkai–Shames（Subset Sum）与 Ahmadi et al.（3-SAT）两篇尚未找到/读。

## 2026-11-02 · descriptor 可控性指标（Workstream B 优先级 4）

**动机**：把 $Q_L$ 的左最小指标识别成文献里的量（专家 2026-11-02 §4）。

| 查询式 | 命中/结论 |
|---|---|
| `descriptor system controllability indices right minimal indices pencil [sE-A B] Kronecker` | SLICOT AG08BZ 文档（**已取到全文**）、Varga 报告 PDF（无法取文本）|
| `"right minimal indices" "controllability indices" pencil [sI-A B]` | 片段；De Terán actas、Dopico LAA 2022 |
| `"left minimal indices" "observability indices" pencil system` | 无直接可引语句 |
| `descriptor system "controllability indices" definition "Kronecker indices" system pencil survey Lewis singular systems` | Iwata KCF 论文（PDF，未取文本）、SLICOT 文档 |

**已确认**（读到文档页）：SLICOT AG08BZ 把 $[A-\lambda E\ B]$ 的**右 Kronecker 指标**称为可控性指标
（示例里判据是"completely controllable"），把 $[A-\lambda E;C]$ 的左 Kronecker 指标称为可观性指标；
其引用为 Misra–Van Dooren–Varga, Automatica 30 (1994) 1921–1936。

**未确认**（需读原文）：右 Kronecker 指标是否**总**叫"可控性指标"（还是只在可控时）、零指标的约定、
以及"descriptor 系统的可控性指标序列可实现哪些划分"是否有现成刻画。

记录：`literature/notes/DESCRIPTOR_CONTROLLABILITY_INDICES.md`。


## 2026-11-04 · 可观性归约的新颖性核对（专家 §Q5 提示）

**动机**：专家在答复中指出，我们 II.3 的"谱条件 → 观测性"表述可能已有文献对应，要求先核对再声称新颖。

| 查询式 | 命中/结论 |
|---|---|
| 专家点名的两条：Darouach & Fernando, *On functional observability and functional observer design*, Automatica 173 (2025) 112115；T. Fernando, *Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger*（2026-09）| 后者即本项目已对接的 P1/P2（arXiv:2609.33615 / 2609.37992）；其 Thm 4 就是零空间铅笔判据 $\operatorname{rank}((\lambda I-A)V\mid Z)=\operatorname{rank}(V\mid Z)$ |
| 专家定向检索的结论 | **未**找到与 $\ker E=\mathcal L(V)$、$(E,\Lambda)$ 可观测这一**具体**表述完全一致的文献 |

**结论（采纳专家的措辞建议）**：零空间铅笔判据**不是**我们的新结果（已在 `docs/03` 引用为"文献 Thm 4"）；
新颖性只限于"从增广功能观测器方程**导出** $q$ 维对 $(E,\Lambda)$ 的观测性检验，以及由此得到的紧凑
$\exists\mathbb R$ 证书"。**不得**声称 PBH 判据本身是新结果。

记录：本条目；相关比较表见 `literature/notes/OBSERVABILITY_REDUCTION_VS_LITERATURE.md`。


## 2026-11-04 · 专家点名/本轮新知的文献（§D/§A）

| 文献 | 内容 | 对本项目的作用 |
|---|---|---|
| **Liu（2026-09）** | static output-feedback stabilization（有理数据、可控可观测、两输入）是 $\exists\mathbb R$-complete；固定有效增益维数时多项式时间 | 硬度源候选（专家：条件不匹配——Hurwitz 是实半代数条件，我们的谱条件是代数秩条件；不可直接等同）|
| **Guo（2024）** | variety-evasive subspaces（子空间与给定簇的交维数受控），连到多项式恒等测试与秩压缩 | 技术来源（Chow 形、incidence variety、维数估计），**不是**我们问题的复杂度定理 |
| **Darouach–Fernando, Automatica 173 (2025) 112115** | functional observability 与功能观测器设计 | related work（与 P1/P2 同一脉络）|

**行动**：把 Liu 2026 记入 `docs/07` 的硬度文献表（若走 D2 路线则必须引用）；Guo 2024 记入"技术工具"而非"复杂度"栏。


## 2026-11-04 · Q3 定型：正则子铅笔（regular subpencil）/ 压缩

**动机**：专家 §Q3 要求"认清确切的秩可行性问题"。

| 查询式 | 命中/结论 |
|---|---|
| `regular subpencil of a matrix pencil prescribed size Kronecker` | **Embedding a regular subpencil into a general linear pencil**（LAA 2000 前后，S002437959900049X）；经典概念"regular subpencil" |
| `compression of matrix pencils zero-free subpencil generalized eigenvalue avoidance` | 压缩/deflation 传统（Van Dooren staircase）；与 Kronecker 标准形配套 |

**结论**：我们的 AVOID = "**带约束的** regular subpencil"：行空间固定为 $V=\ker[C;CA]$、核固定落在
$K=\ker[C;L_0]$ 内。无约束版由 Kronecker 形多项式可解；受约束版才是我们的问题。
记录：`workspace/q1_false/feasibility_geometry/attempts/74_avoid.md`。

## 2026-11-09 · 读 2026 复杂度论文（ARM/SOF/output feedback）

**查询式/来源**：arXiv 编号直接读取；`arxiv.org/abs/2602.14037`、`/2610.00390`、`/2609.20636`、`/2609.16886`。

| 文献 | 命中/结论 | 入库 |
|---|---|---|
| **Majumdar 2026**（2602.14037）| ARM(3) 是 ∃R-完全；rank-forcing gadget（违反 ⇒ 4×4 满秩）、gauge block、composition lemma | `papers/2602.14037.{pdf,txt}`；笔记 `notes/MAJUMDAR_2026_ARM_ER.md` |
| **Liu 2026**（2610.00390）| SOF 稳定化 ∃R-完全；有效增益维数固定 ⇒ 多项式；单输入族强 NP-hard | PDF/txt 已补；笔记已有 `notes/LIU_2026_SOF_EXISTS_R.md` |
| **Ahmadi et al. 2026**（2609.20636）| 输出反馈稳定化 NP-hard（非 ∃R-完全）；连续+离散 | `papers/2609.20636.{pdf,txt}`；笔记 `notes/AHMADI_2026_OUTPUT_FEEDBACK.md` |
| **Löfberg 2026**（2609.16886）| SOF NP-hard（Betweenness）；注意 2609.18844 是无关论文 | 已有 PDF/txt |

**结论**：四篇都不解决 $q1$；ARM(3) 是最接近的硬度源，SOF 次之；观测器侧的障碍仍是 $(LN,LAN)$ 同源耦合 + 谱条件。
已写入 `docs/07` §10 与 `literature/REFERENCES.md` 第 20–22 条。

## 2026-11-09 · 补读 SOF NP-hard（Barkai–Shames）

**来源**：arXiv:2609.38728（PDF/txt 已入库）。

- 结论：从 Subset Sum 归约到无约束 SOF 稳定化 ⇒ **NP-hard**（弱于 Liu 的 ∃R-complete）；
- 技术：频率分离（带通变换）+ Rouché 根计数 + 增益有界/modulus margin；
- 用途：spurious witness 的界、全频条件的根计数、近似离散选择；不能替代 ARM(3)/SOF 完全性。
- 已写入 `docs/07` §10.7、`REFERENCES` 第 23 条。
## 2026-11-13 — 谱条件下界是否已有文献

**问题**：论文新命题 `prop:lowerbound`
（$q_{\min}\ge r_0+\max(0,\operatorname{rank}[U_0;V_0]-s_0+1)$，
由 (5b) 在 $\lambda=0$ 与结构界 $\omega+1\le\dim W$ 导出）是否已在文献中出现。

**查询**：
- `functional observer minimum order lower bound rank condition`
- `functional observability indices minimum order functional observer lower bound`
- `Darouach functional observer minimal order necessary condition rank`

**命中**：只命中本地已有的两篇（arXiv:2609.33615、arXiv:2609.37992）及相关综述；
没有独立来源给出由**谱条件**导出的阶下界。

**结论**：文献中的下界是 $q_0=\sum_j\eta_j$，由**代数条件 (A)** 的上下夹逼得到
（fer26a F.3.2 的上下界论证；fer26b 写 $\nu_{\min}\ge q_0$）。
没有文献对照过由 (5b) 导出的下界。本命题按"本文框架的推论"陈述，
注明与 $q_0$ 独立、取大者，未声称新颖性。

**本地相关**：`proof/lower_bound/README.md` 有一条旧框架下的下界
（$q_{\min}\ge\max(r+\varepsilon,\ \rho+\max(c_0,1))$，记号 $\rho,c_0,\mathcal J$），
与本文命题对象不同，当前论文未引用；若日后要统一，需先做记号对照。
### 追加检索（同日，第二轮）

**查询**：
- `Darouach 2010 functional observer existence conditions order r`
- `"functional observer" "necessary and sufficient" minimal order lower bound kernel [C;L]`
- `reduced order functional observer order bound structural observability index`

**命中**：Rotella–Zambettakis《A Note on Functional Observability》（两条秩条件的来源）、
Mendis 2008 综述、奇异系统的最小阶功能观测器文献。均为**存在性/设计条件**，未给出由谱条件导出的阶下界。

**本地核对**：`literature/pdf/observer/Fernando_2010_min_order_functional_observers.pdf`
（fer10）只把最小阶定义为"满足两条件的最小 $L$ 的行数"，并指出 $q\ge r$；无谱下界。

**结论（加强）**：文献中的阶下界只有 $q_0=\sum_j\eta_j$（代数条件），且都属 fer26a/fer26b 这条 2026 线；
由谱条件导出的阶下界未见于所查文献。论文按"to our knowledge"措辞陈述，不作强新颖性宣称。

## 2026-11-16 — 多项式左逆的次数界是否已有明文（$d_{\min}=\nu-1$）

**问题**：$Q(\lambda)=\lambda X-G$（$X$ 满列秩、$Q$ 处处满列秩）的多项式左逆最小次数 $d_{\min}$
是否等于可观测性指标 $\nu$ 减 1？项目原用初等伴随–Bézout 界 $2\omega-2$；本轮由 93 号的提示
（Hautus 形式 + 可观测性指标）得到一个自足证明。

**查询**：
- `polynomial matrix full column rank left inverse degree bound`
- `minimal degree polynomial left inverse linear pencil matrix`
- `Bezout identity degree observability index polynomial matrix`
- `minimal degree left inverse [lambda I - A; C] observability index`
- `polynomial observer Bezout identity degree bound observable pair n-1`

**命中**：
- **未命中**"$d_{\min}=\nu-1$"或"$[\,\lambda I-A;\,C\,]$ 的多项式左逆次数 $=$ 可观测性指标 $-1$"的明文陈述。
- 两条接近的线：(i) **标量 Diophantine/Bézout 的次数界**（互素 $A,B$ 的 Bézout 解满足 $\deg D=n_A-1$，
  见标准自适应控制讲义）；(ii) **最小次数多项式基与观测性指标**（多项式向量空间的最小次数基、
  可观测性矩阵的零化矩阵，日文综述与 Kuijper 1992 一路）。
- 一般多项式矩阵左逆的次数界：**Fabiano–Struppa 1990**（Multidim. Syst. Signal Process. 1(1):67–74），
  论文已引用为"经典界"，但其公式覆盖一般情形，未见对本情形（一次铅笔）的特化。

**结论**：新颖性按 **待核、倾向不新** 记（属"重新发现"一类）。本项目的贡献限定为：
(i) 一个 8 行的自足证明（逐项比较 $\lambda$ 的幂，不依赖 Bézout/伴随）；
(ii) 指出它把 $r=0$ 的系统规模从 $2\omega-1$ 降到 $\nu$；
(iii) 精确验证 255/255 + 构造证书 8/8。
**不得**当作独立新定理对外主张，不单独成节、不作里程碑。

记录：`workspace/q1_false/decision_algorithms/attempts/321_expert93_verdict_and_degree_theorem.md`（§重要性评估）。
