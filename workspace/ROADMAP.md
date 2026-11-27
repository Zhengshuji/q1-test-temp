# 项目路线图（2026-11-08 整理）

> 目的：把"**已证 / 待证 / 该 Lean / 该纸面+专家 / 只算实验**"分开，作为继续推进的底座。
> 规范见 [CLAUDE.md](../CLAUDE.md)，现状见 [STATUS.md](../STATUS.md)，尝试总表见 [ATTEMPTS.md](../ATTEMPTS.md)。

> **当前优先级（专家 98 号审计后；取代 93–97 号的排序与本文 §5 的旧顺序）**：
> ⓪ **候选线性原理（CLP）**：固定 $(A,C,L_0)$ 与秩 $\omega$，在每个秩 $\omega$ 的可行轨迹的不可约分量上，
> 可行集要么空、要么在某个**线性子空间**中 Zariski 稠密。**已化归**为"$P_\omega$ 的分量是否线性"
> （$P_\omega=\{\operatorname{rank}H=\omega\}\cap(5a)$）；**$m=1$ 已证成立**（定理 A，[357](q1_true/multiplication_gate/attempts/395_clp_single_row.md)）；
> $m\ge2$ 是当前主问题——若假，反例指出乘法的几何藏身处。见 [356](q1_true/multiplication_gate/attempts/394_expert98_audit.md)。
> ① **pinned no-go 定稿**：四假设（钉住 / 固定行协调 / 可行集非空 / 仿射线性解码）下，
> 钉住实例不能强加新的乘法恒等式——**可写进论文**，见 [354](q1_true/multiplication_gate/attempts/392_pinned_gadgets_cannot_multiply.md)。
> ② **修 Claim 1（分量分解）**：计数 $\le1+\delta$ 成立，但"每项是不可约分量"未证——
> 要显式化行空间入射簇与其 Grassmann 层，证极限行空间构成**可容许特征纤维的真闭子集**（Plücker），
> 且族在常秩意义下是丛。见 [342](q1_false/decision_algorithms/attempts/342_expert97_audit.md)。
> ② **立 Theorem B**：$p=1$、$q=n-2$、$r_0=0$ 时非特征层点全部违反 $(5b)$（对 $A$ 一致）。
> ③ **立 Prop D**（$K_0$ 含特征向量但整条纤维全坏的反例）与 **Prop C**（零频秩恒等式）。
> ④ **把 Prop C 当预处理**：每个特征纤维先算 $\dim(AK_0)-\dim(AK_0\cap V^\perp)$，不满足直接丢弃。
> ⑤ **特征纤维的两级判据**：零频秩 ＋ generic gcd（$\overline{\mathbb Q(Y)}[\lambda]$）。
> ⑥ **富余档（Claim 11）**：无约束高铅笔的 codimension 论证是标准的；缺的是**结构族不落在坏铅笔簇内**
> （用结构化系数映射 $\Phi_v:r\mapsto(rN,rAN)$，Step 3 未做）。
> ⑦ 左逆次数（已完成，[321](q1_false/decision_algorithms/attempts/321_expert93_verdict_and_degree_theorem.md)）；
> ⑧ 全局秩解码翻译引理；⑨ 型控制（长期）。
> 本文 §5 的"$k=\omega+1$ 投影定理…"是 2026-11-08 的旧排序，保留作历史，**不要**再按它排任务。

## 0. 一句话

文献（Fernando 2026）已完成**刻画**；唯一开放的是

$$\boxed{q1:\ \exists\Theta\ (\text{图卡}\times\text{半代数})\ \text{的判定复杂度}}$$

本文件不重复刻画，只整理"复杂度地图"的现状与分工。

## 1. 主线现状

- **上界**：$\mathrm{DEC}(q)\in\exists\mathbb R$（chart-free 编码，G.1）；$k=\omega\in\mathbf{RP}$（M2）；
  fixed-$(q,\omega)$ 是 $\mathbf P$（有界次数消元）。
- **下界**：**零**——没有 NP-hard / $\exists\mathbb R$-hard 归约。
- **战场**：$\omega\ge2$ 且 $k>\omega$。自由区 $q=3,\omega=2$ 已有充要判据（M2）；
  约束区只有一个 $n=5$ 层定理（M2）；**一般分量描述**与**约束纤维的谱行为**开放。
- **教训（已写死）**：层 ≠ 阶；"某层全坏"不推出"该阶不可行"。
  2026-11-07 与 2026-11-08 各踩一次（后者见 attempts/103 的撤回）。

## 2. 已完成（M3，30 份卷宗）

- `docs/02` **30 条主条目**；`proof/` **30 份卷宗**；**22 条有 Lean**（8 字面 + 14 内核）、**8 条可接受纸面**；
  未完成 **0**（[proof/UNFINISHED.md](../proof/UNFINISHED.md)）。
- 与 $q1$ 的关系：绝大多数是**结构 / 工具**（块判据、闭性、层分解、计数判据），
  不是 $q1$ 本身；写作时必须按 `CLAUDE.md §3` 降级为"对接 / 重新发现"。

## 3. 待整理（M2，`workspace/augmentation_family/attempts/`）

| # | 结果 | 位置 | M | 需要什么 | 优先级 |
|---|---|---|---|---|---|
| A | $k=\omega\in\mathbf{RP}$ | [101](q1_false/c_stratification/attempts/101_rp_k_omega.md) | M2 | **纸面 + 专家**：Smith 步要写成"矩形行列式因子"引理（KKS 1987 确定性；SL 1997 仅方阵非奇异/Las Vegas）；Lean **不适用**（复杂度/随机算法）| 高 |
| B | 自由区 $q=3,\omega=2$ 充要判据 | [102](q1_false/c_stratification/attempts/102_free_fibre_criterion.md) | M2 | **纸面 + 专家**：incidence 维数与整行秩已补；把 $\operatorname{rank}L_0=r$、任意 $k\ge2$ 写进陈述；Lean **不便**（generic choice / incidence 维数）| 高 |
| C | 约束层全坏（$n=5$，$q=3,\omega=2$）| [103](q1_false/c_stratification/attempts/103_constrained_all_bad_proof.md) | M2 | **Lean 内核已完成**（`LayerAllBad.lean`，整图 exit=0）；再请专家复核 | 中 |
| D | 同 $S$ 一好一坏（$n=9$）| [100](q1_false/c_stratification/attempts/100_q_omega_plus_1_w2.md) | 精确验证 | 作论文例子；专家 49 号已确认"决定性"；Lean 可选（显式矩阵）| 低 |
| E | 约束例 $q_{\min}$ 更正 | 103 + [50 答复](for_expert/archive/50_rp_free_fibre_and_all_bad-answer.md) | 已撤回 | $q_{\min}=4$ 作废；正确值 **$q_{\min}=2$**（$L=[e_4;e_5]$ 过七条检查）| 已完成 |

## 4. Lean / 纸面+专家 / 文献 / 精确验证 的分工

### 4.1 该 Lean（或值得 Lean）

| 对象 | 可行性 | 目标 |
|---|---|---|
| C（约束层全坏） | ✅ 已完成 | `LayerAllBad.lean`：`rank_le_one_of_rows_zero` + `rowForm_rank_le`；整图 `lake build` exit=0 |
| B.24 块判据内核 | 中 | 补 $(5a)\Rightarrow\ker(\cdot L)\subseteq\ker(\cdot\Lambda)$ 的实例化（B.24 现 F1）|
| B.24 $q=\omega+1$ 行列式 | 中 | 2×2 行列式判据的内核 |
| D（同 $S$ 例）| 低价值 | 显式 3×3 矩阵的秩/gcd；专家已确认，不必优先 |

### 4.2 该纸面 + 专家

| 对象 | 缺什么 | 送审形式 |
|---|---|---|
| A（RP）| Smith 引理 + 位长记账 | 一页修正说明（或 51 号）|
| B（自由区）| incidence/整行秩已补，待复核 | 与 A 合并 |
| C（层定理）| 纸面已完整，待复核 | 与 A/B 合并 |

### 4.3 文献

- **Smith/行列式因子**：Kaltofen–Krishnamoorthy–Saunders 1987（确定性，**但显式定理是方阵非奇异**）；
  Storjohann–Labahn 1997（方阵非奇异/$\mathbb Z[x]$ 的 Las Vegas）；矩形来源：
  Storjohann–Labahn（rectangular Hermite）、Beckermann–Labahn–Villard 2006。
- **矩形行列式因子**：桥接引理（[attempts/106](q1_false/c_stratification/attempts/106_rectangular_determinantal_divisor.md)）$\Delta_k(P)=\det D$（$UP=[D;0]$，$U$ 幺模）；
  矩形 Hermite 来源：Storjohann–Labahn 矩形预处理、Beckermann–Labahn–Villard 2006。
- **仿射矩阵空间/奇异性**：Buss–Frandsen–Shallit 1999；Ivanyos–Karpinski–Qiao–Santha 2015；
  Recht–Fazel–Parrilo 2010（affine rank minimization）——只作**源问题候选**，归约必须保留共享 $R$。
- **刻画**：Fernando 2026（arXiv:2609.33615 / 2609.37992）；见 [literature/notes/FERNANDO_2026_TWO_PAPERS_vs_PROJECT.md](../literature/notes/FERNANDO_2026_TWO_PAPERS_vs_PROJECT.md)。

### 4.4 只算实验（不计证明）

| 工具 | 数字 | 复现 |
|---|---|---|
| `proof/B.24/check_block_criterion.py` | 738 例 | `python proof/B.24/check_block_criterion.py` |
| `tools/verification/free_fibre_criterion_check.py` | 1200 例 | `python tools/verification/free_fibre_criterion_check.py` |
| `tools/verification/constrained_all_bad_check.py` | 790 点 + $q=2$ 见证 | `python tools/verification/constrained_all_bad_check.py` |
| `tools/verification/rp_k_omega_check.py` | 39/39 一致 | `python tools/verification/rp_k_omega_check.py` |

## 5. 下一步（按专家 52 号答复的顺序）

> **专家 52 号的顺序**：精确 $q=2$ 判据（已完成）→ 受限 $d=2,U_0=0$ 全坏定理（已完成，见 110）
> → **修正的 $k=\omega+1$ 投影定理**（下一步）→ 论文包。

1. **$k=\omega+1$ 的投影约束定理**（**最高优先**）：先做 $k=3,\omega=2,q=3$ 的 $\mathbb P^2$ 精确分量分析
   （admissibility、compatibility 矩阵的秩分层、$E+X_S=S$、逐分量 generic determinant divisor），
   再写 hyperplane-coordinate 下的定理。**进展**：正维 $\mathbb P^1$ 例
   （[attempts/104](q1_false/c_stratification/attempts/104_p2_constrained_locus.md)）——开层 gcd $=\lambda t$、例外点好（**混合**）；
   **族定理**（[attempts/109](q1_false/c_stratification/attempts/109_family_theorem_p1_mixed.md)）：$E=0,Z_1=0,Z_2=e_1,V_0\ne0$ 时同一模式成立（含 $ab=0$ 边界）；
   **$d=2$ 首例**（[attempts/110](q1_false/c_stratification/attempts/110_d2_all_bad_example.md)）：可容许轨迹两点、整层全坏（$\lambda_0=-1/0$），与 $d=1$ 相反；
   **$q_{\min}$ 检查**（[attempts/111](q1_false/c_stratification/attempts/111_qmin_check_and_d2_scan.md)）：四个实例的 $q_{\min}$ 都是 2（层 $\ne$ 阶）；
   **分层表**（[attempts/112](q1_false/c_stratification/attempts/112_incidence_table.md)）：$d=1$ 例外层好 + lift、开层全坏；$d=2$ 可容许层全坏；
   **修正版定理**（[attempts/113](q1_false/decision_algorithms/attempts/113_projective_theorem_corrected.md)）：$\widetilde E_S$、lifted incidence（含 $R$）、determinantal 分层；
   **lifting**（[attempts/114](q1_false/c_stratification/attempts/114_lifting_lemma.md)）：符号秩判据；**$k=3$ 秩层**（[attempts/115](q1_false/c_stratification/attempts/115_k3_component_decomposition.md)）：一般线性性**撤回**（专家 53 反例），112 表为逐实例数据；
   **$e>0$**（[attempts/116](q1_false/c_stratification/attempts/116_k3_e_positive.md)）：$d=1$ 混合稳健；$d=2$ 全坏仅 $U_0=0$；
   **$d=2,e=1$ 判据**（[attempts/117](q1_false/decision_algorithms/attempts/117_d2_e1_v0z2_criterion.md)）：**更正**——$V_0Z_2$ 证明撤回；正确充分条件 $\operatorname{row}Z_1\cap\operatorname{row}Z_2=0$；
   **$k>3$ 第一步**（[attempts/118](q1_false/c_stratification/attempts/118_k_omega_plus_1_d2_attempt.md)）：交集 $0\Rightarrow$ 全坏（任意 $k=\omega+1,d=2$）；
   **一般情形**（[attempts/119](q1_false/c_stratification/attempts/119_general_case_vs_enumeration.md)）：113 的定理 $k$-无关；逐 $k$ 只是例子；开放是分量/gcd 复杂度；
   **Q9**（[docs/05](../docs/05_open_questions.md)）：分量分解复杂度（分量界、族上 gcd、实点）——当前主线，不再逐 $k$；
   **Q9 第一步**（[attempts/120](q1_false/c_stratification/attempts/120_base_component_bound.md)）：$d=2$ 底空间分量 $\le16$；纤维开放；
   **超平面已解**（[attempts/121](q1_false/c_stratification/attempts/121_hyperplane_vector_bundle.md)）：$k=\omega+1$ 时 $\le\delta+1$ 分量（$\delta=2$ 时 $\le3$），每分量向量丛；
   **不变障碍**（[attempts/122](q1_false/c_stratification/attempts/122_invariant_eigenspace_obstruction.md)）：$\dim(K\cap\ker A)>k-\omega\Rightarrow$ 全坏；
   **超平面算法**（[attempts/123](q1_false/c_stratification/attempts/123_hyperplane_algorithm.md)）：分量 $\le\delta+1$，每分量随机点 + gcd；假阴性 $\le2^{-T}$；
   **专家 54 号的顺序**：每分量 gcd → $c=2$ → 实点 → 论文；
   **$c=2$ 首层**（[attempts/124](q1_false/c_stratification/attempts/124_c2_degeneracy_loci.md)）：$\mathcal D_2$（谱）/$\mathcal D_3$（特征线）/$\mathcal D_4$（开）；分量界只依赖谱；
   **$c=2$ 结构补完**（[attempts/125](q1_false/c_stratification/attempts/125_c2_structure_complete.md)）：$\mathcal D_2$ 的 $J_\lambda$、$\mathcal D_3$ 的投影丛；分量 $\le\binom{s}{2}+3s+1$；
   **$c=2$ 非空**（[attempts/126](q1_false/c_stratification/attempts/126_c2_k0_truncation.md)）：$e_\lambda$、$T_\lambda$、$m_0$ 决定的线性代数条件；
   **$c=2$ 算法**（[attempts/127](q1_false/decision_algorithms/attempts/127_c2_algorithm.md)）：分量表 + 非空 + 每分量随机点 + gcd；
   **$c=3$ 结构**（[attempts/128](q1_false/c_stratification/attempts/128_c3_structure.md)）：$\mathcal D_3/\mathcal D_4/\mathcal D_5/\mathcal D_6$ 递归到 $c=2$；
   **$c=3$ Jordan/截断**（[attempts/129](q1_false/c_stratification/attempts/129_c3_jordan_truncation.md)）：$1+1+1$/$2+1$/$3$、$K_0$ 条件、模型控制命题；
   **一般归纳**（[attempts/130](q1_false/decision_algorithms/attempts/130_general_induction_map_type.md)）：线性映射型控制（更正“不变子空间”说法）；固定 $c$ 型有限；
   **$c=2$ 修正**（[attempts/131](q1_false/c_stratification/attempts/131_c2_d3_nilpotent_subtype.md)）：$\mathcal D_3$ 分不变线/幂零 2-步；分量界 $\binom{s}{2}+3s+2$；
   **$c=3$ 修正**（[attempts/132](q1_false/c_stratification/attempts/132_c3_d4_d5_subtypes.md)）：$\mathcal D_4/\mathcal D_5$ 分不变/非不变；非不变型由 $W,A(W)$ 决定；
   **型控制定理**（[attempts/133](q1_false/c_stratification/attempts/133_type_control_theorem.md)）：分量 $=$ $W$-型层上的 Grassmannian 丛；$N(c)$ 有限、$k$-无关；
   **55 号 + Lean**（[for_expert/55](for_expert/archive/55_type_control_and_status.md)）：结果 + 状态表 + 七问；Lean 内核 `rank_lt_of_large_kernel` 独立编译；
   **55 裁决**（[attempts/134](q1_false/c_stratification/attempts/134_55_corrections_exact_fibre.md)）：精确纤维 $\operatorname{rank}(V\to K/V)=c-t$；Kronecker 替代 Jordan；$c=2/c=3$ 修正；型控制 = 猜想；
   **Step 1–5**（[135](q1_false/c_stratification/attempts/135_exact_fibre_theorem.md)–[139](q1_false/decision_algorithms/attempts/139_type_control_conjecture.md)）：精确纤维、$c=2$ 重写、$c=3$ 重写、Kronecker 表示、型控制猜想；
   **Lean**（[LiftKernel](../trash/lean_removed_2026-11-19/augmentation_lean/LiftKernel.md) · [CounterKernel](../trash/lean_removed_2026-11-19/augmentation_lean/CounterKernel.md) · [BlockKernel](../trash/lean_removed_2026-11-19/augmentation_lean/BlockKernel.md) · [RankQKernel](../trash/lean_removed_2026-11-19/augmentation_lean/RankQKernel.md) · [RankQFormula](../trash/lean_removed_2026-11-19/augmentation_lean/RankQFormula.md) · [PencilRank](../trash/lean_removed_2026-11-19/augmentation_lean/PencilRank.md) · [Splitting](../trash/lean_removed_2026-11-19/augmentation_lean/Splitting.md) · [BlockIff](../trash/lean_removed_2026-11-19/augmentation_lean/BlockIff.md)）：rank inequality、lifting、显式反例、块判据（核+秩+完整 iff）、rank Q 引理/公式、铅笔因子化、分裂引理均已过（axioms 干净；未入 build graph）；
   **内核 5c**（[attempts/140](q1_false/decision_algorithms/attempts/140_hyperplane_rank_identity.md)）：$\ker[P;Q]\cong\ker[v,Av]$，$\operatorname{rank}[P;Q]=\delta-2+\operatorname{rank}[v,Av]$（纸面 + Lean 5c-1–5 全过；$\delta\ge2$ 条件）；
   **优先级 6**（[attempts/141](q1_false/c_stratification/attempts/141_polynomial_certificate.md)）：多项式证书 $PYP=P$、$\deg Y\le2\omega-2$（纸面；**Lean 6a 常数矩阵恒等式已过** [CertKernel](../trash/lean_removed_2026-11-19/augmentation_lean/CertKernel.md)）；
   **一般 incidence 定理**（[attempts/142](q1_false/c_stratification/attempts/142_general_incidence_theorems.md)）：有限 $(t,u)$ 行列式分层 + 相对 Grassmannian 的开子簇；条件性分量推论；不给出分量数上界（专家 56 号建议的“先证明的两条一般定理”）；
   **严格 $c=2$**（[attempts/143](q1_false/c_stratification/attempts/143_c2_rigorous_parameterization.md)）：六层精确参数空间（链提升、$\operatorname{rank}[v,Av,A^2v]=3$）、互斥穷尽、非空条件、$O(n^3)$ 判定算法（M2；算法未实现）；
   **$c=2$ 好性**（[attempts/144](q1_false/c_stratification/attempts/144_c2_good_locus.md) → **更正 [145](q1_false/c_stratification/attempts/145_c2_good_locus_corrected.md)**）：正确块形式 + 完整坏条件（$\alpha=0$ 特征向量分支 + $\alpha\ne0$ 仿射分支）；$(2a)$ 提升判定未做（部分，M2）；
   **$c=3$ 严格参数化**（[attempts/146](q1_false/c_stratification/attempts/146_c3_rigorous_parameterization.md)）：八子型（$t=3$ 六种 Jordan 型、$t=2$ 的 $\dim U=2/3$、$t=1$ 的 $AL\subseteq L$ 与否、$t=0$），精确参数空间、互斥穷尽、可容许非空（M2）；
   **$c=2$ 分量上界**（[attempts/147](q1_false/c_stratification/attempts/147_c2_component_bound.md)）：六层不可约性 → 可容许 locus 分量 $\le\binom{s}{2}+3s+2$；好 locus 同界（M2）；
   **$c=3$ 分量上界**（[attempts/148](q1_false/c_stratification/attempts/148_c3_component_bound.md)）：八层不可约性 → 分量 $\le\binom{s}{3}+3s^2+6s+1$；好 locus 同界（M2）；
   **一般 $c$ 分量上界**（[attempts/149](q1_false/c_stratification/attempts/149_general_c_component_bound.md)）：**已按 57 号降级**——$p(c)n^c$ 只是标签数上界；
   **统一块判据**（[attempts/150](q1_false/decision_algorithms/attempts/150_universal_pencil_descent.md)）：$P$ 对所有可容许 $V$ 下降；145 两分支作为谱判据撤回；
   **提升完成定理**（[attempts/151](q1_false/decision_algorithms/attempts/151_lift_completion_theorem.md)）：$q-\omega\le d_C$ 判据；$q=\omega+1$ 只需 $d_C\ge1$；
   **提升完成定理（含固定 $L_0$）**（[attempts/152](q1_false/c_stratification/attempts/152_lift_completion_fixed_l0.md)）：定理 A（保持对）$q-\omega\le d'_C$；定理 B（只在 $V$ 上兼容）$q-\omega\le d'_C(V)$；构造 $L=L^{(0)}+G_b$；
   **$c=2$ 分类定理**（[attempts/153](q1_false/c_stratification/attempts/153_c2_complete_theorem.md)）：六层互斥且覆盖所有可容许 $V$；143+147+152 合并；给定 $q$ 的判定算法（纸面；未实现）；
   **$W_L$ 约束与 c=1/2/3 比较**（[attempts/154](q1_false/c_stratification/attempts/154_c1_c2_c3_and_induction_failure.md)）：$V\subseteq W_L=\ker[L_0N;L_0AN]$；归纳失败五因；
   **顶部铅笔约化**（[attempts/155](q1_false/c_stratification/attempts/155_c2_top_pencil_obstruction.md)）：$c=2,r=1,q=\omega+1$ 化为 $2\times k$ 铅笔 gcd（变量 $h_1,X$）；
   **$c=3$ 的 $S_{2,3}$ 审计**（[attempts/158](q1_false/c_stratification/attempts/158_c3_s23_audit.md)）：$S_{2,3}$ 开、不可约；可疑的是不变层；
   **$c=3$ 分量界修正**（[attempts/159](q1_false/c_stratification/attempts/159_c3_component_bound_corrected.md)）：$N_3\le\binom{s}{3}+\binom{s}{2}+2s^2+4s+3$（148 作废）；
   **$c=3$ 退化审计**（[attempts/160](q1_false/c_stratification/attempts/160_c3_degenerate_audit.md)）：每块空或不可约；159 界无需分段；
   **一般 $c$**（[attempts/161](q1_false/c_stratification/attempts/161_general_c_invariant_and_rank_strata.md)）：不变部分 $\sum_{\lambda\vdash c}s^{b(\lambda)}$；非不变部分归约到 $B_{u,v}$ 的分量数（逐 $(u,v)$，非逐 $c$）；
   **58 号裁决**（[attempts/163](q1_false/decision_algorithms/attempts/163_58_verdict_implementation.md)）：提升/∃R 关闭；$c=2$ 算法与 $c=3$ 界开放；两处分歧待 59 号；
   **59 号裁决**（[attempts/164](q1_false/c_stratification/attempts/164_59_verdict_implementation.md)）：$W_L$ 正确、$V$ 被迫；$S_{2,3}$ 开（$U\subseteq V$ 维度引理）；不变界降级；$c=2$ 判据 $\det[b;bA_*]\ne0$；
   **$c=2$ 被迫平面判据**（[attempts/165](q1_false/c_stratification/attempts/165_c2_forced_plane_criterion.md)）：$b_i$ 强制 0 的秩判定；16/21 $q=3$ 不可行、10 可行；
   **$c=2$ 一般算法**（[attempts/166](q1_false/decision_algorithms/attempts/166_c2_general_algorithm.md)）：$W_L$ 枚举 + $b$-判据 + 搜索，工具 `tools/verification/c2_q3_algorithm.py`；
   **$\dim W_L=3$ 判据**（[attempts/167](q1_false/c_stratification/attempts/167_dimWL3_existence_criterion.md)）：$\lambda_0$ 处 $P_1\notin W_\Gamma$；构造化为线性方程；
   **$\dim W_L=3$ 见证**（[attempts/168](q1_false/c_stratification/attempts/168_dimWL3_witness.md)）：$n=6$ 实例，七条检查通过；
   **不变层不可约性**（[attempts/169](q1_false/c_stratification/attempts/169_invariant_strata_irreducibility.md)）：循环向量参数化修复 161；$N_{\rm inv}(c)$ 恢复为分量界；
   **$c=3$ 十一层清单**（[attempts/170](q1_false/c_stratification/attempts/170_c3_strata_table.md)）：Deliverable 3；
   **$B_{u,v}$ 秩层**（[attempts/171](q1_false/c_stratification/attempts/171_Buv_rank_strata.md)）：不总不可约；二次 chart + Bézout 界；一般 $c$ 界形状；
   **forced-plane 证书**（[attempts/172](q1_false/decision_algorithms/attempts/172_forced_certificates.md)）：10/16/21 的短证书；
   **提升层传递**（[attempts/173](q1_false/c_stratification/attempts/173_lift_component_transfer.md)）：提升不增加分量数；
   **$B_{u,v}$ Lean 内核**（[attempts/174](q1_false/decision_algorithms/attempts/174_Buv_lean_kernel.md)）：核/秩恒等式 L4；
   **$c=3$ 严格界**（[attempts/175](q1_false/decision_algorithms/attempts/175_c3_bound_via_Buv.md)、[176](q1_false/c_stratification/attempts/176_incidence_fibre_argument.md)）：$s+s^2+s^3+1921$（$k=4$，$v=t$）；
   **chart 次数**（[attempts/177](q1_false/decision_algorithms/attempts/177_chart_degree_check.md)）：$F_A(X)$ 二次性验证 25/25；
   **行空间判据 Lean**（[attempts/178](q1_false/decision_algorithms/attempts/178_forced_criterion_lean.md)）：$\varphi\in\operatorname{range}f^{\mathsf T}\iff\varphi|_{\ker f}=0$，L4；
   **$c=2$ 算法范围**（[attempts/179](q1_false/decision_algorithms/attempts/179_c2_scope.md)）：forced-plane 完全；$\dim W_L>c$ 搜索；$q>3$ 未覆盖；
   **统一层求解器**（[attempts/180](q1_false/c_stratification/attempts/180_uniform_stratum_solver.md)）：一个工具覆盖任意 $(q,\omega,c)$；
   **复杂性定位**（[attempts/181](q1_false/c_stratification/attempts/181_solver_complexity_status.md)）：随机性 ≠ P/NP；工具的 FOUND/infeasible/none 三态；
   **$c=1$ 不可行引理**（[attempts/182](q1_false/c_stratification/attempts/182_c1_infeasibility_lemma.md)）：非特征线超平面维数论证；特征线待查；
   **特征线**（[attempts/183](q1_false/c_stratification/attempts/183_c1_eigenlines.md)）：21 两条有理线、16 两条复共轭线；
   **$q=4$ 全排除**（[attempts/184](q1_false/c_stratification/attempts/184_q4_excluded.md)）：16/21 $q_{\min}\ge5$；
   **16/21 全不可行**（[attempts/185](q1_false/c_stratification/attempts/185_seeds_infeasible_all_q.md)）：任意 $q$（项目约定）；
   **61 号裁决**（[attempts/186](q1_false/c_stratification/attempts/186_61_verdict_implementation.md)）：约定分层；压缩论证与约定无关；求解器四层；
   **证书包**（[attempts/187](q1_false/decision_algorithms/attempts/187_certificate_package.md)）：16/21 的精确数据；
   **$W_L\not\subseteq D$ 边界**（[attempts/188](q1_false/c_stratification/attempts/188_c1_outside_D.md)）：超平面机制失效；
   **$c=1$ 二分法**（[attempts/189](q1_false/c_stratification/attempts/189_c1_outside_D_feasible.md)）：$W_L\subseteq D$ 不可行、否则一般可行；
   **$c=1$ 判定树**（[attempts/190](q1_false/c_stratification/attempts/190_c1_decision_tree.md)）：O1/O2 开放；
   **O1 铅笔判据**（[attempts/191](q1_false/c_stratification/attempts/191_c1_pencil_criterion.md)）：$B_*=0$ 恒坏；$B_*\ne0$ 一般好；
   **O1 小算法**（[attempts/192](q1_false/decision_algorithms/attempts/192_c1_pencil_block_algorithm.md)）：块量 + gcd 验证；
   **O2 归约**（[attempts/193](q1_false/c_stratification/attempts/193_c1_O2_reduction.md)）：内点 + 开集；
   **62 号裁决**（[attempts/194](q1_true/multiplication_gate/attempts/194_62_verdict_implementation.md)）：O1 判据更正；硬度 ARM(3)；
   **个别/同时提升**（[attempts/195](q1_true/arm_reduction/attempts/195_lift_individual_vs_simultaneous.md)）：逐行可同时组装；
   **ARM(3) 归约计划**（[attempts/196](q1_true/arm_reduction/attempts/196_ARM3_reduction_plan.md)）：表达力引理与障碍；
   **表达力限制**（[attempts/197](q1_true/arm_reduction/attempts/197_ARM3_expressiveness_limit.md)）：$H$ 约束是行空间型；
   **$V$-chart 表达力**（[attempts/198](q1_true/arm_reduction/attempts/198_V_chart_expressiveness.md)）：二次/incidence；
   **incidence 线性化**（[attempts/199](q1_true/arm_reduction/attempts/199_incidence_linearization.md)）：Sylvester 型，非任意仿射；
   **乘法 gadget**（[attempts/200](q1_true/multiplication_gate/attempts/200_multiplication_gadget.md)）：$z=xy$ 验证；pair-space 更正；
   **pair-lift 定理**（[attempts/201](q1_true/multiplication_gate/attempts/201_pair_lift_theorem.md)）：$\mathcal L_V=(V+AV)^\perp$；
   **gadget 朴素嵌入**（[attempts/202](q1_true/multiplication_gate/attempts/202_gadget_naive_embedding.md)）：谱障碍；
   **不变性定理**（[attempts/203](q1_true/multiplication_gate/attempts/203_invariance_theorem.md)）：$A(K_0)\subseteq K_0$ ⇒ $V$ 不变；
   **谱 gadget 条件**（[attempts/204](q1_true/multiplication_gate/attempts/204_spectral_gadget_conditions.md)）：必要条件与扫描；
   **否定定理**（[attempts/205](q1_true/multiplication_gate/attempts/205_AinvK0_impossible.md)）：$A(K_0)\subseteq K_0$ ⇒ 不可行；
   **Lean 内核**（[attempts/206](q1_true/multiplication_gate/attempts/206_lean_pairlift_eigenvector.md)）：pair-lift + 不变特征向量；
   **64 号裁决**（[attempts/207](q1_true/multiplication_gate/attempts/207_64_verdict_implementation.md)）：刚性边界更正；局部泄漏刚性；泄漏 gadget；
   **局部泄漏更正**（[attempts/210](q1_true/multiplication_gate/attempts/210_local_leakage_correction.md)）：铅笔步骤不成立；gadget 未死；
   **泄漏 gadget 尝试**（[attempts/211](q1_true/multiplication_gate/attempts/211_leakage_gadget_attempt.md)）：谱失败；未完成；
   **65 号裁决**（[attempts/213](q1_true/multiplication_gate/attempts/213_65_verdict_implementation.md)）：更正确认；模板待更正；
   **66 号裁决**（[attempts/214](q1_true/multiplication_gate/attempts/214_66_verdict_template_valid.md)）：模板成立；uniformity 待研究；
   **67 号裁决**（[attempts/215](q1_true/multiplication_gate/attempts/215_67_verdict_uniform_spectral.md)）：一致谱=过滤链+单位子式；剩余实现；
   **单门正规形**（[attempts/216](q1_true/multiplication_gate/attempts/216_single_gate_normal_form.md)）：$H=C_0[h_0;g(X)]$；
   **单门下界**（[attempts/217](q1_true/multiplication_gate/attempts/217_single_gate_q_lower_bound.md)）：$q\ge\omega+2$；
   **$\omega=3$ 架构**（[attempts/218](q1_true/rank_gates/attempts/218_single_gate_omega3_architecture.md)）：移位 $A$ 失败；
   **零列障碍**（[attempts/219](q1_true/multiplication_gate/attempts/219_single_gate_zero_column.md)）：候选 $\omega\ge4$；
   **模板扰动**（[attempts/220](q1_true/multiplication_gate/attempts/220_template_perturbation_failure.md)）：$t\ne0$ 失败；
   **变量核族**（[attempts/221](q1_true/multiplication_gate/attempts/221_variable_kernel_family_test.md)）：离散性猜想；
   **168 族符号判据**（[attempts/222](q1_true/multiplication_gate/attempts/222_168_family_symbolic.md)）：只有 $t=0$；
   **提升参数不能编码**（[attempts/225](q1_true/multiplication_gate/attempts/225_lift_params_cannot_encode.md)）：算术须进核或行列式；
   **坐标平面**（[attempts/226](q1_true/multiplication_gate/attempts/226_coordinate_planes.md)）：只有 $V_{45}$；
   **Gr(2,3) 搜索**（[attempts/227](q1_true/multiplication_gate/attempts/227_gr23_systematic_search.md)）：18 平面唯一好核；
   **68/69 裁决**（[attempts/228](q1_true/multiplication_gate/attempts/228_68_69_verdict.md)）：10 维族；撤回 217；转向 $(5a)$ 门；
   **枚举约定问题**（[attempts/223](q1_true/multiplication_gate/attempts/223_enumeration_convention_issue.md)）：需用 `check_candidate` 重做；
   定理骨架（[attempts/105](q1_false/c_stratification/attempts/105_projective_constrained_theorem.md)）；
   **写实版**（[attempts/107](q1_false/c_stratification/attempts/107_projective_constrained_theorem_v2.md)）——
   四步（分层 / 闭性 / 二分 / gcd）+ $k=3,\omega=2,q=3$ 显式分层（$q\ne0$ / $q=0,p\ne0$ / $q=0,p=0$）。
   剩余：分量枚举、一般 $k$、实点（分层常值性已由 [attempts/108](q1_false/c_stratification/attempts/108_layer_constancy.md) 闭合）。
   **验收**：分量结构与逐分量好坏判定 + 精确验证/符号证书。
2. **矩形行列式因子引理**（并行技术收口）：**桥接已证**（[attempts/106](q1_false/c_stratification/attempts/106_rectangular_determinantal_divisor.md)）：
   若 $UP=[D;0]$ 且 $U$ 幺模，则 $\Delta_k(P)=\det D$（差单位）；矩形 Hermite 的引用**已核对**：
   Storjohann–Labahn（ISSAC 1995, pp. 119–125；Zbl 0914.65044）是 **Las Vegas**，RP 吸收。
   剩：$D$ 的次数/位长界（写作细节）。**验收**：位长界；RP 由此无条件。
3. **论文包**：修正后的 RP + 自由区判据 + 层定理（含 Lean 内核，注明 scope）——等 1/2 稳定后组装。
   **验收**：一份自包含稿件；不声称 hardness / 完整复杂度分类。
4. **硬度/等价**（推迟）：自由区先做 **two-compression 结式检验**（$f_i=\det(M_iP_t)$，
   $\operatorname{Res}_\lambda(f_1,f_2)\not\equiv0$），确认自由区可能可解；等价需保留
   共享 $R$、full-row-rank、rank-$\omega$、$\forall\lambda$、实/复 五条。
5. **$q1$**：等 1 出结果后再谈硬度/算法。

## 6. 验收标准（每条新结果）

- **命题级**：M≥3（专家/文献复核）+（Lean 可行则已形式化）+（如适用）精确验证；实验永不替代证明。
- **新增/修改主条目**：更新 `docs/02 §0.1` 别名表、`proof/README.md` 索引、四道门。
- **状态双维**：卷宗写 `(M?, F?)` 与导出的 L；Lean 内核只能记 `[Lean 内核]` 并写明差在哪。
- **撤回**：进 `proof/refuted/` 或对应 attempt 的"撤回"节，保留陈述 + 反例 + 证书路径。

## 7. 本次整理修掉的文档不一致

| 位置 | 原问题 | 处理 |
|---|---|---|
| `proof/UNFINISHED.md` | 总表说 30/30、0 未完成，但 C 表还写"未完成 1（D.1(b)）"；纸面条数 6 与 30 条主条目对不上 | 改为 8 纸面（含 B.37、D.1）、0 未完成、合计 30；加口径说明 |
| `docs/02 §0.4` | L2 行写"否（待补 Lean）"，与紧随其后的"L2 也可以是完成"冲突 | 改为"是（M≥3 即可；Lean 为加分项）" |
| `proof/README.md` | 写"7 条可接受纸面"，漏了 B.37；B.16 与 docs/02 主条目 B.17 的命名未说明 | 改为 8 条（加 B.37）；加 B.16→B.17 的注 |
| 根 `README.md` | 停留在 2026-10-27，§4 仍把 q1_true/q1_false 当活跃方向 | 更新日期、§2 最近进展、§4 历史表说明、§5 加 ROADMAP |
| `attempts/103` / `STATUS` / 50 号 Reviewed | $q_{\min}=4$ 是错的 | 撤回；正确 $q_{\min}=2$（$L=[e_4;e_5]$）；写明两条原因（层≠阶；$(C,A)$ 不可观测）|

## 8. 相关文件

- [STATUS.md](../STATUS.md) · [ATTEMPTS.md](../ATTEMPTS.md) · [CLAUDE.md](../CLAUDE.md)
- [proof/UNFINISHED.md](../proof/UNFINISHED.md) · [proof/README.md](../proof/README.md)
- [attempts/100](q1_false/c_stratification/attempts/100_q_omega_plus_1_w2.md) · [101](q1_false/c_stratification/attempts/101_rp_k_omega.md) ·
  [102](q1_false/c_stratification/attempts/102_free_fibre_criterion.md) · [103](q1_false/c_stratification/attempts/103_constrained_all_bad_proof.md)
- [50 号答复](for_expert/archive/50_rp_free_fibre_and_all_bad-answer.md)
