# 项目现状（一页纸）

> **更新**：2026-11-27。**定位**：本文件只讲“现在在哪、手里有什么、下一步试什么”。
> 项目脉络与论文框架见 [HISTORY.md](HISTORY.md)；尝试总表见 [ATTEMPTS.md](ATTEMPTS.md)。
> **2026-11-27 进展**：算法侧主线迁到 `q1_false/feasibility_geometry`（545–662）：
> $K_\infty/T_\infty$ 秩界、实例级不可行反例（661，满足 651 必要条件）、仿射铅笔问题（659/660/662）；
> 硬度侧“自由行 gadget”路线关闭（627/628：自由行可任意满足门条件）。
> **2026-11-27 更正与现状**：$G$ 受 $(5a)$ 约束（$G_i\in S\cap(U-H_iZ')$），678/682 的表述已修正；
> 661 因 $T=0$ 对 $d>0$ 不可行（$q_{\min}=0$）；733 给出 $d'=2>s=t=1$ 的可行例（恢复 $\omega>s$）；734 给出方向性补偿秩引理；687 证明 $Z$ 的自由部分不影响铅笔；
> 677 证明 Sylvester 秩引理，故「一般 $d$：$(5b)\iff\operatorname{rank}M=2d$」成立；当前核心开放问题见 688。
> **当前裁决**：[83 号：q1 路线](workspace/for_expert/archive/83_project_consolidation_q1_roadmap.md) + [315 落实](workspace/q1_true/arm_reduction/attempts/315_83_verdict_roadmap.md)。
> **论文（2026-11-26 起）**：**Paper I / Paper II 只维护在 q1-functional-observer**
> （本地 `../q1-functional-observer`；引用约定见 [README §1.5](README.md)）。
> 本仓库不再保留这两篇的副本，也不复述其结果；需要时直接写 **Paper I** / **Paper II**。
> 本仓库 `paper/` 只保留 **Paper III（超平面层）** 与 **Paper IV（$c=2$）**；
> Paper I/II 的旧版、合并稿与拆分/Lean 计划已归档到 [archive/paper_drafts/](archive/paper_drafts/)。

---

## 0. 一句话

**$q1$ 仍开放。** 文献（Fernando 2026）已解决刻画、存在性、阶谱、逐阶充要、构造；
开放的是判定复杂度。83 号裁决：$\mathrm P$、$\exists\mathbb R$-完全、参数化中间三种都未被排除。

当前有两个**参数化算法结果**（固定 $q$ 的 XP、固定 $\ell=\operatorname{rank}(AN)$ 的 FPT），
都获专家 82/84/85 号审计；$r=0$ 的边界已由有限线性系统在多项式时间内判定（Prop 3c，c318 PASS）；
硬度方向没有 sound 乘法门，也没有归约。

---

## 1. 当前结果

### 1.1 算法侧（主线）

| 结果 | 依据 |
|---|---|
| 固定 $q$：$\mathrm{DEC}(q)\in\mathrm P$（XP，$\mathcal L^{O(q^2)}$）| **Paper I**, Theorem 1 |
| 固定 $\ell=\operatorname{rank}(AN)$：bit-model FPT（所有 $r\ge0$），$\exp(O(\ell^2\log(\ell+2)))\operatorname{poly}(\mathcal L)$，与 $r$ 无关；$r=0$ 为多项式 | **Paper I**, Theorem 2 + Proposition 4 |
| 固定 $(q,c)$ 有界维、左逆次数等局部推导 | 本项目独立结果（247/261/321）；Paper I 的 XP/FPT 与 Claim 16 覆盖更强版本，引用时优先论文 |

关键公式：
\[
G_H=H^{\mathsf T}H,\quad G_S=H^{\mathsf T}H+H_A^{\mathsf T}H_A,
\]
\[
(5a)\iff e_\omega(G_H)>0,\ e_{\omega+1}(G_S)=0;
\]
\[
(5b)\iff\exists x\in\mathbb R^{2\omega}:\ B^{\mathsf T}Bx=e_0,
\]
\[
K(\lambda,\mu)=\sum_{|J|=\omega}\det(P_J(\lambda)^{\mathsf T}P_J(\mu)).
\]

### 1.2 结构/复杂度

| 结果 | 依据 |
|---|---|
| 两次压缩、块判据 | **Paper I**, Claims 2 / 4 / 5 |
| $\mathrm{DEC}(q)\in\exists\mathbb R$ | **Paper I**, Theorem 5 |
| 全局刚性 $A(K_0)\subseteq K_0,\omega>0$ ⇒ 不可行 | 本地（203/205） |
| 提升判据 $(H_i,H_{A,i})\in\operatorname{row}[N\ AN]$ | 本地（288） |
| 低 $c$ 分类/求解器 | 本地（182–185、180） |

### 1.2b 子空间归约与 $\ell$-FPT（2026-11 新增，完整纸面证明）

把自由行从"有序向量组"改为"子空间"后，参数从 $\kappa_{\rm obs}=rd$ 降到
$\ell=\operatorname{rank}(AN)\le k$。这一支已是 **Paper II** 的内容（证明与 Lean 都在 Paper II）；
本仓库的过程材料（PROOF、PAPER_MAP、审计）已归档到
[archive/paper_drafts/workspace_2026-11/q1_subspace/](archive/paper_drafts/workspace_2026-11/q1_subspace/)。

| 结果 | 等级 | 位置 |
|---|---|---|
| 沙包 / 可实现性 / 条件只依赖 $W$ | M3（纸面）+ Lean | `Q1Subspace`、`Q1RowSpace`、`Q1Pencil` |
| 结构界 $\omega+1\le\dim W\le2\omega$ | M3（纸面，专家两次确认） | PROOF 引理 4 |
| $q_$q_{\min}=r_0+t_{\min}$，$t_{\min}\le2\ell$ | M3（纸面）+ 精确验证 36/36 | PROOF 引理 6 + `c322` |
| $\mathrm{DEC}\in\mathrm{FPT}(\ell)$，$f=\exp(O(\ell^2\log(\ell+2)))$ | M3（纸面 + 专家 92 审计） | PROOF §6 |
| $\mathrm{OPT}\in\mathrm{FPT}(\ell)$（二分，$O(\log\ell)$ 次判定） | M3 | PROOF §7 |
| $\mathrm{FIND}$ **算术**复杂度 $f(\ell)$ + 输出位长界 | M3 | PROOF §8 引理 9（BPR 2006 Thm 13.11） |
| $\mathrm{FIND}$ **位**复杂度 | ❌ **未证**：需"位模型的采样点定理"，BPR 只给算术复杂度 | PROOF §8 |

**范围**：只对**行槽模型**（$q$ = $L$ 的行数，允许冗余/零行）成立；控制论文献的
约化阶 $\operatorname{rank}[C;L]-\operatorname{rank}C$ 是另一个问题，本文未解决。

**专家裁决链**：89（归约与结构界确认）→ 90（五处修正，含 $2^k\to2^\ell$）→ 92（三处客观错误 +
FIND 位复杂度缺口）。全部归档在 `workspace/for_expert/archive/`。

**Lean**：`Q1Subspace`、`Q1Compression`、`Q1RankInclusion`、`Q1RowSpace`、`Q1Pencil`、
`Q1Projection`、`Q1Step3` 七个模块入全图（9116 jobs，公理仅三条）。

### 1.2c 超平面层（$c=1$）的研究状态（新增，attempts 322–326）

| 环节 | 结论 | 位置 |
|---|---|---|
| 坏集闭 | 射影入射簇 + 紧合；**旧稿的"秩不等式 ⟹ 闭"已被专家 94 号的反例否定**（矩阵非包含不是闭条件） | [322](workspace/q1_false/c_stratification/attempts/322_hyperplane_determinism_components.md)、[323](workspace/q1_false/c_stratification/attempts/323_expert94_verdict.md) |
| 分量 | $Z=Z^\circ\cup\bigcup_\lambda F_\lambda$（一般闭包 + 各特征 locus 上的**满纤维**），$\#\le1+\delta$，每项显式参数化 | [324](workspace/q1_false/c_stratification/attempts/324_hyperplane_component_theorem.md) |
| 判据 | 分量可行 $\iff$ generic gcd $=1$（**代数闭域**；$\mathbb Q/\mathbb R$ 点未论） | [322](workspace/q1_false/c_stratification/attempts/322_hyperplane_determinism_components.md) |
| 成本（定理 C） | S1 分量 ✓、S2 Type I（精确除法）✓、**S3（移动根）= 唯一的 PIT** | [325](workspace/q1_false/c_stratification/attempts/325_theorem_c_cost_model.md) |
| 谱形式 | 坏 $\iff\exists\lambda,u\notin\operatorname{span}(v)$：$(\lambda I-A)u\in\operatorname{span}(v,Av)$（**非特征层自动 $V=U^\perp$，双向；特征层只充分**；初版的 $\ker L_0\cap U$ 形式已更正）。c334/c335 核对通过；$Z^\circ$ 上可用 $(n-2)\times k$ 铅笔替代 $q\times k$ | [326](workspace/q1_false/decision_algorithms/attempts/326_eigenvector_form_of_badness.md) |
| 商铅笔（328） | 非特征层：基取最后一列 $\propto v$ ⟹ $M=[\widetilde M\,0]$、$\widetilde M=\lambda X-G$、$\operatorname{rank}X=k-1$；坏 $\iff\exists\lambda:\operatorname{rank}\widetilde M<k-1$；处处满列秩 $\iff$ $(G_1,G_2)$ 可观测。**还要削 $p$ 行**：$\operatorname{rank}\widetilde M\le n-2-p$（$C$ 的行落在 $U^\perp$），故 $\operatorname{rank}[C;CA]=p$ 时该层自动不可行 | [328](workspace/q1_false/decision_algorithms/attempts/328_quotient_pencil_theorem.md)、[329](workspace/q1_false/c_stratification/attempts/329_forced_relations_quotient_pencil.md) |
| 三分（$\lambda$ 随 $v$） | **第 3 类存在**（c335：10 个 $v$ 给出 8 个不同 gcd、零点各异）⟹ **S2 不能闭合定理 C**；但 E3 的"次数恒 2"已由 329 解释为**维度巧合**（$n-2-p=k-1$），**不是** H1b 的证据；三分本身按 95 号改为 H2′（根入射簇投影结构） | [327](workspace/q1_false/c_stratification/attempts/327_lambda_movement_experiment.md)、[329](workspace/q1_false/c_stratification/attempts/329_forced_relations_quotient_pencil.md) |
| 层可行性的两支（新增） | 同一族里 $Z^\circ$ **结构性全坏**（329）、特征纤维 $F_\lambda$ **生成好**（330：一个好点即证，40 组里 33 好）⟹ **该族层可行**，证书是显式行组。判据：**可行性用点证书，全坏才需泛型（S3）** | [330](workspace/q1_false/c_stratification/attempts/330_eigen_fibre_feasibility.md) |
| $c=1$ 的正式结论（97 号审计后） | **Theorem A**：坏集闭 + 块可行 $\iff$ generic gcd $=1$（判据只需**有限不可约覆盖**，[343](workspace/q1_false/c_stratification/attempts/343_stratified_cover_fix.md)）。**Theorem B**：$p=1,q=n-2,r_0=0$ 时非特征层点全部违反 $(5b)$。**Prop C**：$\operatorname{rank}H_A=\dim(AK_0)-\dim(AK_0\cap V^\perp)$；$\lambda=0$ 给必要条件；$\lambda_0\ne0$ 特征向量 ⟹ 需 $\dim(AK_0)\ge k$。**Prop D**：$K_0$ 含特征向量但整条纤维全坏。**两级判据**：零频筛（c343：反例 0/40、好实例 36/40）→ generic gcd | [344](workspace/q1_false/c_stratification/attempts/344_three_theorems_and_two_level_criterion.md)、[342](workspace/q1_false/decision_algorithms/attempts/342_expert97_audit.md) |
| **$c=1$ 的关键结构（350/351）** | **可容许核方向 $v$ = 压缩 $M=(\pi\|_{K_0})\circ A\|_{K_0}$ 的特征向量**（$\operatorname{proj}_{K_0}(Av)\parallel v$）⟹ 层 = **有限个纤维** $\mathbb P^r$（$r=\dim U^\perp-\omega$），$v$ 不再连续。**判定流程**：分解 $M$ 的特征多项式 → 每个（代数）特征值取特征向量 → 各纤维 generic gcd → 有一个 $=1$ 即**可行**。**教训**：可容许 $v$ 是**代数数**特征向量，**有理采样会系统性错过**（349 就因此误判 4245 不可行）。已判：4242 可行（Bézout 证书）、4245 可行（$\mathbb Q(\sqrt2)$ 上 gcd $=1$）、4246 **未判定** | [350](workspace/q1_false/c_stratification/attempts/350_admissible_v_are_eigenvectors.md)、[351](workspace/q1_false/c_stratification/attempts/351_retract_instance_infeasibility.md) |

> **注意**：现在**不能**说"$c=1\in\mathrm P$"。94 号拆的三定理里只有 **A（分量判据）、B（有限归约）可声称**，
> **C（多项式时间）未证**——缺口恰是上表的 S3（[323](workspace/q1_false/c_stratification/attempts/323_expert94_verdict.md)）。

### 1.3 sound gadget（硬度侧）

| gadget | 状态 |
|---|---|
| 非零：$(5b)\iff f\ne0$ | **sound**，完整观测器（296）|
| 输入非零：$\exists R:(5a)\wedge(5b)\iff x\ne0$ | **sound**，完整观测器（303C）|
| 乘法 $z=xy$ | full-observer realization，**不 sound**（$R=0$ 反例，306）|
| 直和/压缩块（297/299/300）| unsound 或未分析 |
| wiring/port | 条件性 no-go，未解决（304–310）|

---

## 2. 可靠性说明

- “精确验证/PASS”只表示脚本对**所示矩阵**做了精确秩/gcd 检查，不是 Lean 证明，也不是一般定理。
- 固定 $q$ 与固定 $\ell$ 的算法均已闭合到论文级；剩余是**审计性**工作（系数高度逐项核对、$r=0$ 的位复杂度细则、FIND 的位复杂度）。
- 296 与 303C 是完整观测器且 sound；303B 只是 realization。
- 297/299/300 是压缩块；297 直和对 unrestricted $R$ 不 sound。

---

## 3. 当前尝试方向

### 方向 1（主，Phase A）：把两条算法写成完整定理

- 固定 $q$：$H=XB$、$G=FX$、秩一致性消去、谱证书；补枢轴覆盖、$\omega=0$、比特复杂度。
- 固定 $\ell$：系数尺寸界（$f(\ell)\operatorname{poly}(\mathcal L)$ 的常数）、系数高度、Renegar 界的系数审计；
  $r=0$ 已关闭（85 号：$2\omega-2$ 次数界 ⟹ 有限线性系统，Prop 3c），剩余只是 Hadamard/消元界常数。
- 显式化 $q1\in\exists\mathbb R$ 的 polynomial left-inverse 证书。
- 目标：论文三定理 + 两推论（Theorem 1 固定 $q$、Theorem 2 固定 $\kappa_{\rm obs}$、Theorem 3 $\exists\mathbb R$；Corollary 2a real-RAM、Corollary 4 组合上界）。

### 方向 2（硬度，Phase B）：一个 ARM(3) 翻译实验

- 暂停局部 row-copy/gate；
- 读并验证 ARM(3) 的 gauge/composition；
- 尝试用固定行做 gauge、用 $\mathcal T$ 编码仿射约束；
- 里程碑是一个翻译引理，不是完整归约。

### 方向 3（参数化，Phase C）：只做 $q$ 的 W[1]-hard

- 固定 $q$ 是 XP；$q$-W[1]-hard 与 XP 相容；
- $\kappa_{\rm obs}$ 的 W[1]-hard 会与 FPT 冲突，不做；
- 源：Multicolored Clique，要求 $q=O(t)$、$\kappa_{\rm obs}$ 增长。

---

## 4. 下一步

1. **83 号送审**：请专家判断 q1 的可能复杂度与下一步路线；
2. 按 82 号的 submission checklist 补两条算法的完整证明；
3. 若专家建议硬度：只做全局 $\mathcal T$/matroid 方向，不再局部 gate；
4. 若专家建议算法：优先 FPT 定理，固定 $q$ 作为第二定理。

---

## 5. 论文与 Lean

- **Paper I / Paper II**：见 q1-functional-observer（引用约定见 [README §1.5](README.md)）。
  该仓库自带 Lean、精确验证、证明地图与公理审计；**本仓库不再重复维护这些内容**。
- **本仓库的论文**：Paper III [paper/current/paper_III_hyperplane.tex](paper/current/paper_III_hyperplane.tex)、
  Paper IV [paper/current/paper_IV_c2.tex](paper/current/paper_IV_c2.tex)。两篇都是唯一 `.tex` 源。
- 项目推进用的 Lean 验证树仍在 WSL `~/WorkSpace/lean4/MyProof`（不进论文）。
- 论文只含算法与结构；硬度 / gadget 不进入论文。

## 6. 验证状态

- `c296`：完整非零 gadget，PASS。
- `c278`：244 铅笔 Gram 证书，PASS。
- `c311`：秩一致性 200 例，PASS。
- `c312`：$H=XB$、$B_J=I$、$H_A=FH$，PASS。
- `c313`：索引公式、$e_0\in\operatorname{row}B$，PASS。
- `c314`：$G=FX$、$H_A=GB$、秩恒等式，PASS。
- `c318`：$r=0$ 线性系统 ⟺ 极大子式 gcd（135 例 + 反例对照 + 薄集构造 + 端到端 29/29），PASS。
- `c319`：Lemma D2 行空间 + $\exists\mathbb R$ 编码见证 + 数据约束必要性 + 负对照，PASS。
- 四道门全绿。

---

## 7. 资产入口

| 内容 | 位置 |
|---|---|
| 工作区结构（两个方向 + 子方向四件套） | [workspace/README.md](workspace/README.md)、[ATTEMPTS_INDEX.tsv](workspace/ATTEMPTS_INDEX.tsv) |
| 项目脉络/论文框架 | [HISTORY.md](HISTORY.md) |
| 尝试总表 | [ATTEMPTS.md](ATTEMPTS.md) |
| 最近送审/裁决 | [85 送审](workspace/for_expert/archive/85_r0_exact_kronecker.md) + [答复](workspace/for_expert/archive/85_r0_exact_kronecker-answer.md) |
| 可靠命题 | [docs/02](docs/02_theorems_proven.md) |
| 文献综述 | [docs/07](docs/07_literature_review.md) |
| 开放问题 | [docs/05](docs/05_open_questions.md) |
| 工作清单/路线 | [09](workspace/support/project_management/09_work_inventory.md)、[11](workspace/support/project_management/11_usable_and_route.md) |
