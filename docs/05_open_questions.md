# 05 · 开放问题

> 只列**真的开放**的。已解决的见 [docs/02](02_theorems_proven.md)；已死的见 `proof/refuted/` 与 `workspace/q1_true/attempts/`。

---

## Q1（主问题）· 可达性的复杂度

> **2026-10-30 定位更新**：$q_{\min}$ 的**刻画**已由文献完成（[P1] arXiv:2609.33615、[P2] arXiv:2609.37992）：
> 阶谱 $\Sigma_{FO}\subseteq[q_0,n_0-p]$、每阶充要（P2 Thm 5 的 $\exists Z$；Thm 6 的图卡 $Z_I(\Theta)$）、$\nu_{\min}=\min\Sigma_{FO}$。
> **本项目唯一还开放的问题**（= $q1$）：
> $$\textbf{DEC-}\Theta:\quad \text{给定 }(A,C,L)\ \text{与阶 }q,\ \text{判定 }\exists\ \text{图卡 }I,\ \Theta\in\mathbb R^{d(m_L-d)}\ \text{使 }(14a)(14b)\ \text{成立}$$
> 这是**图卡 × 半代数**的可行性问题：多项式 ⟹ $q1$ = 假；$\exists\mathbb R$-hard ⟹ $q1$ 强 hard。
> 现状：两篇论文只给存在性刻画、只在例子中精确求值；**复杂度类无人给出**（[docs/07 §5.2](07_literature_review.md)）。
> 下面的旧文字保留作历史；"$\rho,c$ 层程序"已被 P2 Thm 9 覆盖（写作时必须引用）。

$$\text{给定 }(\rho,c)\text{，判定 }"\exists\,\mathcal V\supseteq S:\ \rho(\mathcal V)=\rho,\ c(\mathcal V)=c,\ (5a)\wedge(5b)"\text{ 的复杂度？}$$

**已证可判的层**：$\rho=0$（B.3）、$\rho=d$（B.2）、以及 $\mathcal V=\mathbb C^n$ 的可行性（B.4）。
**未证**：$0<\rho<d$ 的一般层。$(2,1)$ 层（$\rho=2,c=1$）曾有一个"经可控性"的判据，但那条桥（Q5）**已否决**（见下），所以该层现在只有**铅笔形式**的刻画（三个 $2\times2$ 子式的 $\gcd$）。已证：子式对 $(\lambda,\tau)$ 次数 $\le2$、"有公根"的 $\tau$ 集是闭集 ⟹ 判定**可判定**；$w\ne0$ 时 $\tau$-量词已由**线性代数**解决（坏集仿射，[proof/rho1_layer/theorem.md](../proof/rho1_layer/theorem.md) 定理 9.10）；$w=0$ 时恒不可行（定理 9.12）；可行还需 一个模 $B$ 的特征方向（定理 11.1-更正版，随机 216 例 0 命中 ⟹ 该层稀有）。最终形式是 $\exists\mathcal U$ 的维数比较（定理 10.1）；模 $B$ 特征方向必要但不充分（猜想 11.4 已否）。

**两种结局**（**2026-10-30 更正**，专家 QA9 §7）：$\mathrm{NP}\subseteq\exists\mathbb R$ ⟹ **$\exists\mathbb R$-hard 蕴含 NP-hard**，两者不是互斥的。
正确的目标表述是：**固定阶判定的精确复杂度**（在 P / NP-hard / $\exists\mathbb R$-complete 之间），
以及**决策版的优化问题** $q_{\min}\le k$（固定阶判定与优化是两个问题，需单独的归约）。
- 若固定阶判定 $\in\mathbf P$（且图卡可避开枚举）⟹ $q_{\min}$ 多项式 ⟹ **$q1$ = 假**；
- 若固定阶判定 $\exists\mathbb R$-complete ⟹ **$q1$ 强 hard**（且自动 NP-hard）。
- 已知上界（本轮）：$\mathrm{DEC}\text{-}\Theta\in\exists\mathbb R$（[proof/spectral_locus/README.md](../proof/spectral_locus/README.md) 引理 3）；
  **2026-10-31 加强**：chart-free 的 $\mathrm{DEC}(q)\in\exists\mathbb R$（[proof/dec_q_existsR/](../proof/dec_q_existsR/README.md)）——
  变量/方程 $O(n^3)$、次数 $\le n$、只有 $O(n)$ 个 $s$ 分支、无图卡析取；核心引理与"左逆⟹单射"已 Lean 验证。
  **这仍是上界**：下界（$\exists\mathbb R$-hard 或 NP-hard）与多项式算法都未知。

> **2026-11-26 对齐**：Paper I 已给出固定 $q$ 的 XP（Theorem 1）、固定 $\ell=\operatorname{rank}(AN)$ 的
> FPT（Theorem 2）与 $\mathrm{DEC}(q)\in\exists\mathbb R$（Theorem 5）；这些**不解决 $q1$**——
> $q1$ 里 $q$ 随输入增长，固定参数的结果不能直接给出 $q_{\min}$ 的多项式算法。
> 本节以下文字保留为历史；引用上界时用 **Paper I**, Theorem 5，不再引本地 `proof/`。

### 2026-11-02 重述：$(5a)$ 已解决，DEC 是"完备增广族上的谱条件"

> 依据：[literature/notes/FERNANDO_2026_BEYOND_DL.md](../literature/notes/FERNANDO_2026_BEYOND_DL.md)
> （Fernando, arXiv:2609.33615 = [P1]）§2–§3。

1. **$(5a)$ 不是硬度来源**：P1 给出 $q_0=\sum_j\eta_j$（functional observability indices）、
   **Theorem 1** 显式构造满足 $(5a)$ 的增广、**Theorem 2** 最小性、**Theorem 3（§V）** 给出
   **最小条件-(A) 增广的完备族**（up to row equivalence）。
2. **本项目的 B.8** 把谱条件 $(5b)$ 换成**离散等式**：
   $$(5b)\iff d_{\rm fin}=0\iff \sum_j\varepsilon_j=\operatorname{rank}L$$
   （左最小指标之和 $=$ 增广矩阵的秩）；而左指标 $=$ descriptor 系统 $(-E,-EX^{\mathsf T},B)$ 的可控性指标
   （[proof/descriptor_reduction](../proof/descriptor_reduction/README.md)）。
3. **所以 $q1$ 的精确形状**：
   $$\textbf{DEC}:\quad \exists\,R\in\{\text{P1 的完备增广族}\}:\ \textstyle\sum_j\varepsilon_j(R)=\operatorname{rank}L\ ?$$
   即"**在一个离散可参数化的族里，找一个让可控性指标之和达到 $\operatorname{rank}L$ 的成员**"。
4. **仍然未知**：该问题的复杂度（P？NP-hard？$\exists\mathbb R$-complete？）。
   下一步应直接在 P1 的完备族上做，**不要**再按图卡 $\Theta$ 枚举。

**入口建议**：从 $\rho=\rho_{ci}$ 层开始（$\rho_{ci}=P(T,B,U_0)$ 已可算，但它 $\le q_0$，只是弱下界）。若该层可行性等价于"某多项式在仿射空间上不恒零"，则层判定是线性的 ⟹ $q1$ 假。

---

### 专家复核 2026-11-02 之后的进展（Q1 的三个子项）

| 子项 | 状态 | 位置 |
|---|---|---|
| **Toeplitz 判据**（固定 $\mathcal L$ 判 $(5b)$，不必算 Smith 形）| **[已证-纸面]** $+$ **[精确验证 66/66]** | [proof/toeplitz_criterion](../proof/toeplitz_criterion/README.md) |
| **同族内 $(5b)$ 会变**（$\mathrm{DEC}(q)$ 是真存在性问题）| **[精确验证 3/23 组]**（显式证据） | [workspace/kronecker/attempts/02](../workspace/kronecker/attempts/02_family_sequences.md) |
| **编码规模 $O(n^2(B+\log n))$** | **[已证-纸面]** $+$ **[精确验证 12/12（常数部分）]** | [proof/dec_q_existsR/bitsize.md](../proof/dec_q_existsR/bitsize.md) |

仍未解决的仍是：$\mathrm{DEC}(q)$ 的**复杂度**（下界/多项式算法）。

**2026-11-02 晚的实验（含一次推翻）**：在**功能可观测**实例上，$q_{\min}$ 与闭包
$\operatorname{cl}=\min\{\dim V:\operatorname{row}L_0\subseteq V,VA\subseteq V+\operatorname{row}[C;CA]\}$ 的关系：

* ~~$q_{\min}=\operatorname{cl}+1$~~：**已推翻**（[C1](../proof/refuted/C1_closure_plus_one.md)，40/56 反例）；
* 幸存（未证）：$q_{\min}\in\{\operatorname{cl},\operatorname{cl}+1\}$，54/56 个实例成立，2 个未定。

**该弱形式也已推翻**：Fernando 2026（arXiv:2609.37992）§VII 的例子给出 $q_0=3$、$\nu_{\min}=5$（间隔 **2**），
本项目已复现（[proof/fernando_2gap](../proof/fernando_2gap/README.md)、[C3](../proof/refuted/C3_gap_can_be_two.md)）。
幸存的界：$q_0=\sum_j\eta_j\le q_{\min}\le n_0-p$（上端点保证可行）。

> **2026-11-03：猜想 T 已被推翻**（[C4](../proof/refuted/C4_type3_counterexample.md)）：
> 结构化 $A$（Jordan 块，$n=6,p=r=2$）下存在 $q_0$ 阶、$(5a)$ 成立、$h=6<7=q_0+r_1$、
> 但 $d_{\rm fin}=2>0$ 的增广 ⟹ 最小阶上的失败**不**总能由零指标障碍解释。
>
> **三个层次要分开**（专家 2026-11-03 §技术注 4）：
> ①候选验证（给定 $\mathcal L$ 判 $(5b)$，已解决）；②阶可行性（存在某个 $q$ 阶 $\mathcal L$）；
> ③最小阶确定（最小的这样的 $q$）。
>
> **关于"若 T 成立则多项式"**：即使 T 成立，也只是把谱条件换成"秩可达性"问题，
> **不自动**给出多项式算法（专家 §技术注 3）。

**加强的必要条件（已证）**：$q+r_1-s\le h<q+r_1$，且 $d_{\rm fin}\le s-(q+r_1-h)$
（[proof/left_index_count](../proof/left_index_count/README.md)）。

### 专家复核 2026-11-01 的补充（针对 Q1）

> 完整记录：[archive/expert_correspondence/expert_review_2026-11-01/README.md](../archive/expert_correspondence/expert_review_2026-11-01/README.md)。
> 原文 §1/§9/§12/§13。

1. **目标类**：首要目标是 **$\exists\mathbb R$-completeness**（不是 NP-hardness 本身；$\mathrm{NP}\subseteq\exists\mathbb R$）。
   上界 $\mathrm{DEC}(q)\in\exists\mathbb R$ 已有，但**编码规模三项未证**（约束条数、系数比特长、多项式表示）——见 G.1 待补。
2. **DEC 与 MIN 必须分开**：$\mathrm{MIN}(k)\iff\bigvee_{q\le k}\mathrm{DEC}(q)$；P2 的无间隙性质只对 $(A)$，
   **不含** $(S)$ ⟹ **不能**假设 $\mathrm{DEC}(q)\Rightarrow\mathrm{DEC}(q+1)$，**不能二分**，$\mathrm{DEC}(q)\not\iff\mathrm{MIN}(q)$。
3. **"$\rho_{ci}$ 可算"不推出"该层可多项式判定"**：需要
   (i) 证明可行参数集是仿射空间或其**非空 Zariski 开子集**（后者在无限域上稠密）；
   (ii) 显式构造被测试的多项式（$\gcd$ 条件用 resultant/subresultant）；
   (iii) 注意 **PIT 本身不自动是多项式时间**（算术电路上的确定性 PIT 未知）。
4. **中间层 $0<\rho<d$ 是真正的开放数学**：建议走 **Kronecker 标准形 / 最小指标 / 不变子空间** 的结构路线，
   而不是继续行列式展开。
5. **硬度归约**：rank 保持条件**不是闭条件**（含非零条件），须按**半代数**处理；
   先研究 Liu（arXiv:2610.00390，SOF 的 $\exists\mathbb R$-completeness）的算术编码，再改造。

### Workstream B（专家 2026-11-02 指定）：Kronecker 结构

> 记录：[workspace/kronecker/README.md](../workspace/kronecker/README.md)。

**问题**：观测器诱导的铅笔 $Q_{\mathcal V}(\lambda)=[\lambda L-LA;CA;C]$ 能实现哪些 **Kronecker 型**？
若有受限刻画，是否像 Dodig 的行/列补全那样是**有限条关于不变量（次数、最小指标）的不等式**？

**已知**：$(5b)\iff$ 无正则初等因子（左右奇异块都允许，2026-10-30 专家更正）；
Dodig 的行/列补全只给**必要**条件（我们自由度是子空间，不是独立行）。

**已有工具（2026-11-02）**：`kronecker_pencil.py`（精确 Kronecker 数据）、`observer_pencils.py`（构造真实观测器铅笔）、
`kron_struct_scan.py`（五步扫描）。小样本（37 个铅笔）观察：可行铅笔的**左**最小指标非空、无"只含右奇异块"的可行铅笔。

## Q2 · $\sigma$ 存在性的 Lean 化

[proof/p_is_polynomial/theorem.md](../proof/p_is_polynomial/theorem.md) 的 $({\le})$ 用到 $\sigma$ 存在性（纸面已证）。
已有 [Lean]：通用提升引理 `exists_lift_of_range_le`（[tools/lean/PRecursionSigma.lean](../trash/lean_removed_2026-11-19/tools/lean/PRecursionSigma.lean)）。
**缺**：解包 level-1 可行性得到区间包含 $\operatorname{range}\varphi\le\operatorname{range}\psi$。

---

## Q3 · 文献核查（决定"是否新结果"）

$$\textbf{Emre–Hautus (SIAM JCO 18(4), 1980)}\ \text{已读（2026-10-28）——只给 supremal，不抢占。}$$

它给 $(A,B)$-不变与可达子空间的多项式矩阵刻画；若其中已有"最小维数"的多项式算法，则 $P\in\mathbf P$ 不是新结果（递归定理仍是独立证明）。见 [docs/03](03_theorems_cited.md) 引用 5。

---

## Q4 · $q_{\min}$ 的下界能否收紧

$q_{\min}\ge\max(r+\varepsilon,\ \rho_{ci}+\max(c_0,1))$（A.3）已知**不紧**（$n{=}4$ 反例：下界 3、真值 4）。缺的是对 $c$ 的上估计：
$$c\ \le\ ?\quad(\text{在 }\rho\text{ 最优的层上})$$

---

## Q5 · "可控性"提法 —— **已否决**（2026-10-27）

$$\text{旧提法：}(5b)\iff(S_\tau,\beta|_{\mathcal H})\ \text{可控}$$

**已否决**（[proof/controllability_equivalence/theorem.md](../proof/controllability_equivalence/theorem.md) §8）：
$B=\pi(\mathcal J A)=\operatorname{span}\{\beta(J_k)\}$，故 $\beta(\mathcal H)\subseteq B$ 恒成立；放到 $(\mathcal U+B)/B$ 上，"输入"恒为零，
"可控"退化为 $\mathcal U\subseteq B$，不是 $(5b)$。c191 的"可控 63/65"正是这个错误的实证。

**替代**：用**铅笔形式**（[docs/02](02_theorems_proven.md) B.1/B.2/B.5），它们都只涉及 $Q_{\mathcal V}(\lambda)$，没有"输入算子"这一层。

## Q6 · 退化情形（写论文时要交代）

| 情形 | 事实 | 等级 |
|---|---|---|
| $d=0$（$K=0$）| $q_{\min}=r$（$(5a)(5b)$ 自动）| [已证]（$(5a)$ 自动：$\mathcal J=\mathbb C^n$）|
| $\mathcal J=\mathbb C^n$ | 同 $d=0$ | [已证] |
| $A=0$ | $q_{\min}$ 由 $L_0$ 的支撑决定 | [精确验证] 多例，非定理 |

> **层程序与 $q1$ 的关系**（自省笔记）：[workspace/q1_false/mainline_logic.md](../workspace/q1_false/mainline_logic.md)
> —— 每层可多项式判定 ⟹ $q1$ 假；某层出现二次型障碍 ⟹ $q1$ 是 $\exists\mathbb R$-hard。
> $\rho=2$ 恰好是"秩降 = 一次条件"的唯一情形，所以 **$(3,1)$ 是分水岭**。

> **$(3,1)$ 是要证的具体命题**（[proof/rho1_layer/theorem.md](../proof/rho1_layer/theorem.md) §14.4）：
> 判定 $\exists[x]\in\mathbb P(X/\langle w\rangle)$ 使 $\mathcal A\not\subseteq\pi_\tau(\mathfrak S_{\langle w,x\rangle})$ 且 $\mathcal A\ne\varnothing$，
> 是否等价于次数 $\le2$ 的多项式系统在射影空间上有解？若是 ⟹ $\exists\mathbb R$ 型（$q1$ 多半强 hard）；若否 ⟹ 层程序可推广（$q1$ = 假）。

> **$q1$ 的"结"已被定位到一个具体问题**（[proof/rho1_layer/theorem.md](../proof/rho1_layer/theorem.md) §15，纯证明）：
> $(k,1)$ 层的失败条件是"某个 $k\times k$ 子式组在 $\lambda$ 上恒有公根"，子式对 $(\lambda,\tau)$ 次数 $\le k$。
> $k=2$ 时坏集是**仿射**的（$W_0$ 唯一）⟹ 线性代数；$k\ge3$ 时是**投影**⟹ $\forall\exists$ 型。
> 于是
> $$q1\ \text{的难度}\iff\ \text{"}\mathrm{Bad}\text{ 是投影时，}\mathcal A\subseteq\mathrm{Bad}\text{ 能否多项式判定"},
> 而 $\mathrm{Bad}$ 是不是投影 **只取决于 $W_0$ 是否唯一**（$k=2$ 时唯一；$k\ge3$ 时不唯一），**与子式次数无关**。
> （更正：§15 曾说"难度 $\iff$ 次数 $\ge3$"，那是错的——次数只影响"能否写成二次方程"，不影响判定形状。）$$

> **重大进展（2026-10-27 深夜，[theorem.md §17](../proof/rho1_layer/theorem.md)）**：$(k,1)$ 层的判定可以**绕过**"$\mathrm{Bad}$ 是投影"这个障碍：
> 用 Bézout 线性化 $\Phi_D(\tau)$，层可行 $\iff$ **某个极大子式在 $\mathcal A$ 上不恒为零**（系数比较，线性代数，与次数无关）。
> 条件是要一个**次数界引理（17.2）**：$\gcd=1\Rightarrow$ 某 $D$ 使 $\Phi_D$ 行满秩。该引理现在 **$m=2$ 已完整证明**（定理 18.1/推论 18.2：$\operatorname{rank}\Phi_D=D+\max\deg p_j+1$）；**$m\ge3$ 仍缺**（需要 syzygy 模的 Hilbert 函数）。
> 若 17.2 成立 ⟹ 所有 $(k,1)$ 层多项式可判 ⟹ 层程序在 $c=1$ 时成立 ⟹ $q1$ = 假（在 $c=1$ 这部分上）。

> **$c=1$ 一支的总览**（含 T1–T11 与唯一缺口）：[proof/layer_program/](../proof/layer_program/README.md)。
> 一句话：$(2,1)$ **已完全可判**；$(k\ge3,1)$ 只差一个 syzygy 模的 Hilbert 函数（$m\ge3$ 的次数界）。

> **拆分（[theorem.md §20](../proof/rho1_layer/theorem.md)）**：$(5b)=(\mathrm{b})\wedge(\mathrm{a})$。
> $(\mathrm{b})$（全部 $(k+1)\times(k+1)$ 子式 $\equiv0$）**在 $(5a)$ 之下自动成立**（[proof/5b_upper_bound/](../proof/5b_upper_bound/README.md)，[已证]+[Lean]）⟹ 只剩
> $(\mathrm{a})$（$k\times k$ 子式无公根）是开条件，需 T11。
> 由此得到一个**完全证明的充分判据**：某两个 $k\times k$ 子式互素 ⟹ 层可行（定理 20.2）。

> **一个更干净的等价说法（2026-10-28）**：由恒等式 $Q_{\mathcal V}(\lambda)=\pi(\mathcal L(\lambda I-A))$，
> $$(5b)\iff\text{铅笔 }\mathcal L(\lambda I-A)\ \text{的 Kronecker 型只含零块与行最小指标（无有限/无穷初等因子）}.$$
> 即"$\mathcal V$ 在 $\mathrm{mod}\ \mathcal J$ 意义下无剩余特征结构"。型条件是多面体式不等式
> （Dodig 2008 的 Theorem 4），但我们的自由部分是**子空间**而非任意行 ⟹ 只是必要条件。
> 见 [literature/notes/DODIG_2008_row_completion.md](../literature/notes/DODIG_2008_row_completion.md)。

> **2026-10-28 文献核查（重要）**：Fernando 的两篇 2026 预印本给出了**最小阶功能观测器的完整刻画**
> （阶谱端点 $q_0\le\nu_{\min}\le n_0-p$、每阶的 chart 参数化、Thm 4 铅笔形式、Thm 6 的 $\gcd$ 判据、Thm 9 的完备性），
> 因此本项目若干"判据/观察"**已被覆盖**（见 [literature/notes/FERNANDO_2026_min_order.md](../literature/notes/FERNANDO_2026_min_order.md) §2）。
> 但两篇**均无任何复杂度声明**："complexity" 出现 0 次；判定条件是"某个 chart + 连续参数 $\Theta$ 使 (14a)(14b) 成立"，
> 是**半代数可行性**而非有限检验 ⟹ $$\boxed{\ q1\ \text{（复杂度）}\ \textbf{仍开放}\ }$$

> **2026-10-28 深夜（重要）**：本项目曾把 S1 区（$c\ge\rho-1$）的充要判据写成 $\dim K\ge\rho$（$K=\{b\in B:T(b)\in B\}$），
> **已被精确反例反驳**（[proof/refuted/S1_criterion_iff.md](../proof/refuted/S1_criterion_iff.md)）。仍成立的只有**充分方向**（定理 22.1）。
> 教训：维数计数只能给单向结论，把"$\dim\mathrm{Bad}<\dim\mathcal A$"的逆否当充要是错的。

> **2026-10-29 进展（L2 的 T11 闭合）**：定理 27.2（[proof/rho1_layer/theorem.md](../proof/rho1_layer/theorem.md) §27）**证明了**
> 引理 17.2 的 $m\ge3$ 情形：$\gcd=1$ $\Rightarrow$ 存在 $D_0\le 2d(m-1)$ 使乘法映射 $\Phi_D$ 行满秩（对 $m$ 归纳；$m{=}2$ 用 Sylvester）。
> 于是 [精确验证 195/195]。
> **由此**：$\tau$ 量词在**每个固定** $(\mathcal U,\mathcal H)$ 上被消掉（"某个极大子式在 $\mathcal A$ 上不恒为零"，系数比较；这是**有限**代数判据，$\rho$ 固定时才是多项式 ✗）。
> **但**：层的可行性还需要 $\exists(\mathcal U,\mathcal H)$（Grassmannian 上），那一步仍未解决 ⟹ **$q1$ 仍开放**。


## Q7 · 论文架构、投稿条件与研究路线（专家第四/五轮建议的固化）

> 本节把专家的建议固定下来，供写作与后续会话对照；结果本身见 `02` 与 `08`。

## 中央定理（专家建议的形式，五层逻辑）

设 $\mathcal L$ 满足 $(5a)$，取商空间 $V,S,W$ 与偏映射 $\Phi:W\to\mathbb C^q$，$\iota:W\hookrightarrow\mathbb C^q$，
$P_\Phi(\lambda)=\lambda\iota-\Phi$。则以下等价：

1. $(5b)$ 成立（原秩形式）；
2. 商铅笔 $\overline N_{\mathcal Z}(\lambda)$ 对每个有限 $\lambda$ 满列秩；
3. 不存在非零部分特征向量：$\nexists\,0\ne w\in W:\ \Phi(w)\in\mathbb Cw$（即 $\mathcal E_\Phi=\varnothing$）；
4. $P_\Phi(\lambda)$ 的全部 $\rho\times\rho$ 极大子式的 $\gcd$ 是非零常数；
5. 加上 B.17 的永久核结构（$S$ 决定的那一部分）。

**四层叙述**（专家给的分层）：

| 层 | 内容 | 本文条目 |
|---|---|---|
| 1 商结构 | 去掉永久核 $S$ | B.17 |
| 2 块结构 | 隔离谱块 $\lambda I_q-K_1$ | B.23 |
| 3 几何障碍 | 部分特征向量 | B.24 |
| 4 代数判据 | 行列式因子（极大子式 gcd） | B.8 |

## 论文五部分（专家给的骨架）

| Part | 内容 | 本文条目 |
|---|---|---|
| I | 代数可容许性与商归约（含文献已给的阶刻画，明确区分新旧） | A.1、B.1、B.2、B.3 |
| II | 商铅笔的谱结构（本文主要结构部分） | B.17、B.6、B.22、有限初等因子 |
| III | 内蕴部分特征向量刻画（本文核心） | B.23、B.24、B.8 |
| IV | 附加的不可行判据 | F.1、B.9、B.31、B.32、B.13a–c |
| V | 计算复杂度（$\exists\mathbb R$ 上界 + 明确标注未解决部分） | G.1、D.1 |

## 可以放进当前论文的断言（专家列）

1. 谱条件的商空间表示；2. 永久核的精确描述；3. 有限谱障碍的结构刻画；
4. 部分特征向量刻画；5. 固定候选的极大子式 gcd 判据；6. 右最小指标与无穷初等因子结构；
7. 等号障碍；8. 秩屏障与入射型充分不可行判据；9. chart-free 的 $\exists\mathbb R$ 上界（**需把编码审计做完**）。

## 必须留作开放问题的断言（专家列）

1. $q_{\min}$ 的 NP-hardness；2. DEC-Θ 的 $\exists\mathbb R$-hardness；3. DEC-Θ 的多项式算法；
4. 全部可行阶的完整内蕴分类；5. 可容许增广存在性的多项式判据。

## 新颖性分类（专家逐条评估，需逐条再核）

| 评估 | 条目 |
|---|---|
| **最可能新**：主定理 | B.17、B.22、B.24、F.1、B.31、G.1 |
| 可能有补充 | A.1（下界）、B.9、B.6、B.31–B.32 |
| 可能只是重述（须与 $\exists Z$ 判据对照） | B.1（商铅笔）、H.1（Theorem Q）、B.8（gcd 判据，标准多项式矩阵原理） |
| 标准/推论 | B.2（PBH，顶层）、B.3（$\rho=0$）、C.1（特殊族） |
| 标准方法 + 具体应用 | B.13a–c（入射/维数法） |
| 独立算法贡献 | D.1（$P\in\mathbf P$） |
| 独立复杂度贡献 | G.1（$\exists\mathbb R$ 上界） |

## 专家给的五个立即可做的任务

1. **行列式因子等价**：由 B.17 构造 $P(\lambda)=\lambda\iota-\Phi$，证其极大子式 gcd 就是有限谱障碍（接上 B.8）。
2. **可容许族的更简单参数化**：图卡 $Z_I(\Theta)$ 利于存在性证明但掩盖几何；找内蕴参数空间，暴露对 $\Phi$ 的代数限制。
3. **族的表达力**：给定一般矩形铅笔 $\lambda E-F$（$\operatorname{rank}E=\rho$），能否等变地实现为 $\lambda\iota_R-\Phi_R$？
   是 ⟹ 硬度更可信；否 ⟹ 刻画障碍。**这是路线 A 的关键一问。**
4. **加强 B.13**：把"覆盖整个 $\mathbb P(K)$"换成"覆盖**可容许轨迹** $\mathcal Z_{\mathrm{adm}}$"，
   即 $\operatorname{pr}_K(\mathfrak I)\cap\mathcal Z_{\mathrm{adm}}\ne\mathcal Z_{\mathrm{adm}}$。
5. **固定候选与族存在分离**：把固定候选的精确算法做到最好，再研究族约束能否带来更快的搜索；**不要**假设前者蕴含后者。

## 优先级（专家排）

1. 完成统一定理（B.17 + B.23 + B.24 + B.8 的等价，接上 B.6）——**最高**
2. 参数化铅笔：**最高**
3. 加强入射法（相对可容许轨迹的覆盖）——高
4. 硬度：尝试实现多项式入射系统——高
5. 多项式可解性——长期

## 第五轮修订后的路线图（专家 30 号答复 §9）

1. **先定域**：证或反证 $\mathcal LK=\mathcal L(V\cap K)$；不成立则以 $W_K=\mathcal LK$ 为准。
2. 证内在偏映射定理（$\Phi_K$、与 $(5b)$ 的精确等价，用永久核定理）。
3. 调和两个铅笔表示：B.17 的商铅笔 vs $\lambda\iota_K-\Phi_K$。
4. 重核行列式因子结果（维数、极大子式、次数界）。
5. 完成不可行理论：F.1 + B.13 + B.22 + B.31 + 有限初等因子判据。
6. 复杂度：参数化行列式因子 + 可容许偏铅笔的实现问题。

**发表条件（专家 §8.3 五条）**：域定死；永久核陈述精确；与 Fernando 两篇逐条比较；系数域与退化情形约定；把机检部分与纸面部分分开。

**Q3 新增接口**：$(5b)\iff d_{\rm fin}=0\iff\Delta_h$ 常数；并有**有界 Bézout 证书**$\sum_i u_i(\lambda)p_i(\lambda;R)=1$（$u_i$ 次数可多项式界定）。

**Q4 下界改进**：用联合剖面 $q_{\min}=\min_{(\rho,c)\in\mathfrak P_{\rm spec}}(\rho+c)$，并定义 $c_{\min}(\rho)$；F.1 再加 $\rho\le r_*=\min_\lambda r(\lambda)$。

## Q8 · $q1$ 的四阶段研究计划（专家第七轮 §7.3 定的顺序）

专家明确：**先做等价/屏障（(c)），再做定向硬度（(a)），一般算法（(b)）最后**；
并且给出四阶段。本项目的下一步照此执行。

| 阶段 | 任务 | 状态 |
|---|---|---|
| **Stage 1 闭合表述** | ① 改正 $(5b)$ 写法（应为 $\lambda\mathcal L-\mathcal LA$，33 号误写 $\lambda\mathcal L-\lambda\mathcal LA$）；② 明确输入模型（有理数据、实 $R$、二进制编码、$q$ 是否入输入）；③ 证**层上图卡化**的族级判据 | ⬜ |
| **Stage 2 小案例几何** | $n=4,p=1,q=2,r=1$（$R\in\mathbb R^{1\times4}$）：按 $\omega=0,1,2$ 分层，给定有理数据**精确**求可行集的分支、维数、次数 | ⬜ |
| **Stage 3 等价搜索** | 与"多项式矩阵左互质补全"、"仿射矩形铅笔零排除"比较；判定观察器族是否是它们的**真子类** | ⬜ |
| **Stage 4 复杂度** | 有匹配谱谓词的归约；否则给等价或受限算法；分固定 $\omega$/固定 $q$/固定 $p$ 讨论 | ⬜ |

**三条"不要"的告诫（专家 §7.2）**
1. 不要由静态输出反馈 NP-hard 直接推本问题 NP-hard（谱谓词不同：Hurwitz vs 全 $\lambda$ 满列秩）；
2. 不要由构造性推"容易"（构造集的实点存在性仍可难）；
3. 不要由 $\binom{q}{\omega}$ 的子式数推族级编码规模（$W_K$ 随 $R$ 变 ⟹ 须分层 + 图卡化）。

**$\omega$ 的三个情形（专家 §4.2–§4.4，已核）**
* $\omega=q>0$：$P_K$ 是方阵 ⟹ 自同态必有特征向量 ⟹ **$(5b)$ 必失败** ⟹ 该层**直接排除**；
* $\omega=0$：**$(5b)$ 自动成立**（$(5a)$ 仍须单独满足）；
* $\omega=1$：判据退化为**单个行列式** $\det[w,\Phi_K(w)]\ne0$。

---

## Q9 · 投影约束定理：三个问题与超平面解（2026-11-08 更新）

> 专家 54 号：把“分量分解”拆成三个问题；超平面情形已有结构解（$\le\delta+1$ 分量），
> 一般余维才是新的几何。

### 三个问题

| # | 问题 | 数学任务 | 备注 |
|---|---|---|---|
| **A** | Synthesis decision | 是否存在好的满行秩 $R$？ | 真正的 yes/no；**不需要**分量枚举 |
| **B** | Generic classification | 哪些不可约分量一般好/坏？ | 解释几何与例外点 |
| **C** | Component enumeration | 全部分量及其方程？ | 更强，但 A 不必需 |

A 已有 $\exists\mathbb R$ 上界：多项式广义逆证书 $P(\lambda)Y(\lambda)P(\lambda)=P(\lambda)$，
$\deg Y\le2\omega-2$（专家 54 号 §5.5）。

### 超平面情形（$c=k-\omega=1$）：结构上已解

- 底空间 $\mathbb P(K_0)$；约束 $Rv=0,\ RAv=0$；$\rho(v)=\operatorname{rank}[v,Av]\in\{1,2\}$；
- $\rho=1\iff v$ 是 $A$ 的特征向量；$\mathcal B_1=\bigcup_\lambda\mathbb P(K_0\cap\ker(A-\lambda I))$；
- lifted incidence 的非空不可约分量 $\le\delta+1$（$\delta=\dim\ker T$），$\delta=2$ 时至多 3；
- 每分量是向量丛的开子集；$\operatorname{rank}[P;Q]=\delta-2+\rho(v)$；
  $\operatorname{rank}Q=\delta-1$（$v\in D_A$）或 $\delta$（$v\notin D_A$）。

见 [attempts/121](../workspace/q1_false/c_stratification/attempts/121_hyperplane_vector_bundle.md)。每分量的 generic gcd 仍是下一步，
但分量数与纤维结构已经清楚。

### 一般余维（$c>1$）：新的几何

- 用零化子 $V\subseteq K$（$\dim V=c$），底空间 $\operatorname{Gr}(c,K_0)$；
- 约束 $RV=0,\ RAV=0$；$\rho(V)=\dim(V+AV)$；
- 分量问题是 Grassmannian degeneracy locus
  $$\mathcal D_s=\{V\in\operatorname{Gr}(c,K_0):\ \dim(V+AV)\le s\};$$
- 最低层 $\dim(V+AV)=c\iff AV\subseteq V$（$A$-不变子空间）；中间层是 $V\cap A^{-1}V$ 的维数条件；
- $c=2$ 是第一个受控情形（$\rho$ 从 2 到 4；最低层 $=A$-不变的 2-子空间）。
- **精确纤维**（attempts/134，专家 55）：$W=V\cap A^{-1}V$、$U=W+A(W)$，纤维
  $$\mathcal F_W=\{V\in\operatorname{Gr}(c,K_0):\ U\subseteq V,\ \operatorname{rank}(V\to K/V)=c-\dim W\},$$
  是 $\operatorname{Gr}(c-\dim U,\ K_0/U)$ 的**开子集**（极大秩条件）；不是 $A(V)\cap V=A(W)$。
- **型**：$A|_W$ 不是自同态，Jordan 型无定义；正确的是 Kronecker 型 of
  $(\iota|_W,A|_W):W\rightrightarrows W+A(W)$，环境 pair
  $(\iota,A_0):D\rightrightarrows K_0$，$D=K_0\cap A^{-1}K_0$（Berger–Trunk–Winkler 2016；
  Berger–Trenn 2012）。子空间簇是 quiver Grassmannian/incidence 问题（Caldero–Reineke 2008）。
- **型控制是猜想**（不是定理）：固定 $c$ 时，$(W,V)$ 的 incidence 簇有有限局部闭层，
  几何由受限 pair 的 Kronecker 型与环境嵌入数据控制；$N(c)$ 的统一界与 $k$-无关性未证。

### 已知 / 开放

* **超平面**：$\le\delta+1$ 分量（已证）；每分量 gcd 待算；实点按分量处理。
* **$c>1$**：$\mathcal D_s$ 的分量/次数界、复杂度、实点均开放；专家建议先 $c=2$，不要先做硬度。
* **硬度**：没有保持共享 $R$ 结构的归约；暂不做。
* 相关：determinantal rings（Bruns–Vetter）、degeneracy loci（Fulton Ch.14）、
  invariant-subspace varieties / quiver Grassmannians（Caldero–Reineke 2008）。

---

## Q10 · 固定 $(q,c)$ 与有效观测器维数（2026-11-09）

**来源**：专家 74 号建议把 Liu 的“有效增益维数”类比到观测器，得到
$$\kappa_{\rm obs}=r\operatorname{rank}[N,AN].$$

**已得（M2 纸面，attempts/247）**：
- 谱判据给出 $\omega\le q-1$，故 $k=\omega+c\le q-1+c$；
- 固定 $(q,c)$ 时 $k$ 有界，压缩矩阵 $H,H_A$ 尺寸有界；
- 自由行只通过 $RN,RAN$ 进入，$\kappa_{\rm obs}\le2rk$ 也有界；
- 因此固定 $(q,c)$ 的可行性可化为常数维实代数问题，用实量词消去在多项式时间判定（理论算法）。

**开放**：
1. 固定 $c$ **单独**不够：244 的 $c=1,\kappa_{\rm obs}=10$；228 的 $c=2,\kappa_{\rm obs}=14$，且 $k$ 随 $n$ 增长。
   需要 $q$ 或 $\kappa_{\rm obs}$ 作为额外参数。
2. 固定 $\kappa_{\rm obs}$ 是否足以给出 XP/FPT？**255 修正**：$N$ 满列秩 ⇒
   $\operatorname{rank}[N,AN]\ge k$ ⇒ $\kappa_{\rm obs}\ge rk$，所以固定 $\kappa_{\rm obs}$ **控制** $k$、$r$、$q$、
   子式个数与 249 证书的尺寸。249 的 $QPR=I$ 在固定 $\kappa_{\rm obs}$ 下是有限维系统；
   **277** 给出对 $q$ 稳健的 Gram 证书：$(5a)$ 用 $e_\omega(G_H)>0,e_{\omega+1}(G_S)=0$；$(5b)$ 用 $B^{\mathsf T}Bx=e_0$（$2\omega$ 变量），$B^{\mathsf T}B$ 由 Cauchy–Binet 的 $K(\lambda,\mu)$ 压缩；变量 $\kappa_{\rm obs}+2\omega$，$q$ 只进多项式。固定 $\kappa_{\rm obs}$ 的 FPT 以此为骨架（模实 QE 标准界）。
3. 实点 vs 复点、比特长、量词消去的实际复杂度。
4. 与 Liu 的 $\kappa$ 的精确对应：观测器的 $\mathcal N_{\rm obs}$ 是否就是“不影响 $(H,H_A)$ 的方向”。

**相关**：[attempts/247](../workspace/q1_true/multiplication_gate/attempts/247_fixed_qc_tractable.md)、
[attempts/246](../workspace/q1_true/rank_gates/attempts/246_74_verdict.md)。

---

## Q11 · 固定 $q$ 的多项式算法（2026-11-09）

**路线 C**：固定 $q$ 时，把自由变量从 $n$ 维的 $L$ 换成固定维的 $Z\in\mathbb C^{q\times q}$ 与
$U=\operatorname{im}H\in\operatorname{Gr}(\omega,q)$：
- $(5a)\iff H_A=ZH$；
- 固定 $Z,U$ 后，$L$ 的条件是线性方程 $L(AN-ZN)=0$、$(I-P_U)LN=0$ 加秩条件；
- $(5b)\iff U\cap E_\lambda(Z)=\{0\}\ \forall\lambda$，化为 $Z,U$ 的 gcd 条件；
- $Z,U$ 的维数只依赖 $q$，$L$ 的存在性用线性代数消去 ⇒ 固定 $q$ 时 $q1\in\mathrm{P}$（FPT in $q$）。

**开放**：变量 $q$；线性消去的显式秩判据；实/复与比特长细节。见
[attempts/274](../workspace/q1_false/decision_algorithms/attempts/274_fixed_q_polynomial.md)。

