# 证明清单与 Lean 覆盖（2026-11-04 复核）

> 本文件的用途：**逐条列出项目"已接受"的命题**，标出现在靠什么支撑（Lean / 纸面 / 精确验证），
> 以及"为什么还没 Lean"。用户 2026-11-01 的要求：**能 Lean 的一律 Lean，Lean 不了的要写明原因**。
>
> 配套：[tools/lean/](../tools/lean/README.md)（`check_lean.sh`，19 个文件）、[docs/02](../docs/02_theorems_proven.md)（命题登记表）。

---

## 0. 三级的含义（先说清"精确验证"是什么）

| 级 | 名字 | 是什么 | 能做什么 / 不能做什么 |
|---|---|---|---|
| L3 | **[Lean]** | 机器检查：`lake env lean` 退出码 0，0 error | 只要陈述写对，就是**定理**（在 Lean 的逻辑里）|
| L1 | **[已证-纸面]** | 完整的人工推导，可被别人逐行复核 | 是定理，但可能有人为疏漏；**不能**自动检查 |
| L2 | **[精确验证 n/N]** | 在**有限个实例**上用**有理/整数精确算术**（`fractions.Fraction`，无浮点、无舍入）算出结论，并与另一条独立实现/判据对照 | **只能证伪**（一个反例就够），**不能确认**全称命题——除非把全部实例枚举完 |

> $n/N$ 里 $N$ 是**被检实例数**、$n$ 是**通过的个数**。它和"抽样"的区别是：算术是精确的、
> 每个实例都可复现；它和"证明"的区别是：实例有限。项目纪律（CLAUDE §4/§7.18）要求：
> 任何 L2 结论**必须在同一处写明"还缺什么证明"**。

---

## 标签约定（2026-11-05 按专家 §Q5 采纳）

| 标签 | 含义 |
|---|---|
| **`[Lean-verified]`** | 陈述在 Lean 中由定义与已证结果完整证明（仅依赖 `propext`、`Classical.choice`、`Quot.sound`）。|
| **`[Lean-conditional]`** | Lean 只验证**推理**，一个或多个实质数学假设仍未证（原称 `[Lean 内核]`，已改名以免歧义）。|
| **`[Paper proof]`** | 完整纸面证明，未形式化。|
| **`[Exact verification n/N]`** | 有限实例上的精确算术检查（只能证伪）。|
| **`[Experimental]`** | 数值/随机证据，不能当证据。|

公理审计（2026-11-05）：`PsiImage`、`Criterion`、`Dims`、`Logic` 四个文件的 13 条中心声明
经 `#print axioms` 检查，均只依赖 `propext`、`Classical.choice`、`Quot.sound`，**无 `sorryAx`**。

---

## 1. 清单（按 docs/02 的编号）

"未 Lean 的原因"用六个码：

- **(α)** 需要 $(5a)/(5b)$ 的**行空间语义**（`rank[L;CA;C]` 这类"堆叠矩阵的秩" ↔ 子空间条件）——
  Mathlib 没有现成的"矩阵行空间"层——**2026-11-04 已建桥**：`RowSpace.rowSpace` / `rowSpace_fromRows` / `rank_le_rank_fromRows`（见 §2）；
- **(β)** 需要**多项式环**上的 gcd / Smith 形 / 行列式因子；
- **(γ)** 需要**特征值/代数闭域**上的 PBH、循环向量等判据；
- **(δ)** 需要**代数几何**（Grassmannian、Plücker、constructible）；
- **(ε)** 需要 $\exists\mathbb R$ 的语义（半代数编码）；
- **(ζ)** 需要**优化/最小维数**的递归（部分已 Lean）。

| # | 命题 | 现在等级 | Lean？ | 未 Lean 的原因 / 备注 |
|---|---|---|---|---|
| A.1 | $q=\rho+c$（$\rho=\dim\pi\mathcal V$、$c=\dim(\mathcal V\cap\mathcal J)$）| [已证] | **✓** | `A3sem.finrank_inter_add_finrank_map_mkQ`（$\dim(T\sqcap B)+\dim(T/B)=\dim T$）就是它的全部内容 |
| A.2 | $c\ge\max(c_0,1)$ | [已证] | **✓（$c\ge1$ 那半）** | `Eigen.c_pos_of_five_b`（$V\ne0$、$V\cap J=\bot$、$AV\le V\sqcup J$ 与 $(5b)$ 矛盾）$+$ `Eigen.exists_eigenvector`、`Eigen.finrank_lt_of_eigenvector_mod`；$c\ge c_0$ 是 $S\subseteq\mathcal V$ 的定义性事实 |
| A.3 | $q_{\min}\ge\max(r+\varepsilon,\rho+\max(c_0,1))$ | [已证] | **✓（维数部分）** | `A3Bound.a3_rows`（$q\ge r$）、`a3_epsilon`（$q\ge r+\varepsilon$）、`a3_rho`（$c\ge1\Rightarrow q\ge\rho+1$）$+$ `Eigen.c_pos_of_five_b`；**未覆盖**：$\max(c_0,1)$ 里的 $c_0$（需 $P$ 的语言）|
| A.4 | $q_0$ 下界 + 多项式可算 | [引用] + [精确验证 20/20] | ✗ | 文献结果（P1），本项目未重证——**不应标成本项目定理** |
| B.1 | $(5b)\iff\operatorname{rank}Q_{\mathcal V}(\lambda)=\rho\ \forall\lambda$ | [已证] | **✓** | `PencilEquivalence.pencil_rank_eq` / `pencil_rank_forall`（$+$ `pe_finrank_inter_add`、`finrank_sup_eq_add_quotient` 支撑）|
| B.2 | $\rho=d$ 时 $(5b)\iff(D_W,T_W)$ 可观测 | [已证] | **✓（内核）** | `B2Block.block_on_J` / `block_on_W` / `block_on_W_compression`：分块形式的**逐点版**（坐标无关）；组装成矩阵接秩条件是 (α)，仍纸面 |
| B.3 | $\rho=0$ 层的刻画 | [已证] | **✓** | `Rho0Layer.rho_zero_iff`（$\pi_J V=\bot\iff V\le J$）、`five_a_of_le`（$V\le J$ 时 $(5a)\iff AV\le J$）、`five_b_auto` |
| B.4 | $V=\mathbb C^n$ 的谱判据 | [已证-纸面] | ✗ —— 现有 `B4FullSpace` 内核编码的是**对偶写法 (D)**，与铅笔秩降不等价（`b4_convention_test.py`：117 个反例）；按 (P) 重述待办 | `B4FullSpace.b4_iff_no_eigenvector`（陈述）+ `b4_finrank_iff`（对偶维数判据）；存档 `proof/b4_full_space/` |
| B.5 | 循环向量判据 | [已证] | **✓** | `CyclicVector.isCyclic_iff`、`cyclic_iff_no_left_eigen`、`not_cyclic_of_left_eigen`、`exists_left_eigen_of_not_cyclic`（双向）$+$ `CyclicStructural.b5_five_b_fails_imp_not_cyclic`、`b5_converse` |
| B.6 | 右最小指标为零（$(5a)\Rightarrow$ 归纳核心）| [已证-纸面] + [精确验证 150/150] | **✓（内核）** | `KronCoeff.kron_coeff_chain_strong`、`kron_coeff_mem_N`；多项式↔系数序列的翻译与 Kronecker 结论仍纸面 |
| B.7 | 无穷初等因子全是 1 次（descriptor 约化）| [已证-纸面] + [精确验证 151/151] | **✓（内核）** | `KronFactor.kron_block_factor`（$LA=XL+Y_1CA+Y_2C\Rightarrow\lambda L-LA=(\lambda I-X)L-\dots$）；局部 Smith 形与 $\mu$-赋值未 Lean 化 |
| B.19 | 顶层与等号互斥：$V\subseteq\mathcal Z\Rightarrow h<q+r_1$ | [Paper proof] | ✗ | 可 Lean（行空间对偶 + B.11c 的 Type I 判据），【待办】|
| B.20 | 等号情形的结构记账：常值右零空间 $=S$；$W\cap\mathcal Z^\perp=C$ | [Paper proof] | **✓ [Lean-conditional]**（同上：`inf_bot_of_finrank_sup_eq` / `inf_bot_of_rank_fromRows_eq`。差异：矩阵翻译由 `RowSpace` 桥完成） | 可 Lean（核/秩的直接计算），【待办】|
| B.21 | 右零空间与指标：$s=n-h$、$\sum_j\eta_j=0$ | [Paper proof] | **✓ [Lean-conditional]**（`B21.dim_inf_ker`：$\dim(\ker f\cap\ker g)=\dim X-\operatorname{rank}(f\times g)$；差在矩阵翻译）|
| B.8a | Smith 判据：$(5b)\iff d_{\rm fin}=0$ | [Paper proof] | ✗ | 需多项式矩阵 Smith 层（Mathlib 缺）|
| B.8b | 观测器铅笔的 Kronecker 恒等式 $h=\sum\varepsilon_i+d_{\rm fin}+d_\infty$（右指标全零次，$\sum\eta=0$）| [Paper proof] + 650/650 | ✗ | 需 Smith/Kronecker 层；2026-11-05 按专家 §Q3 更正（原版漏 $d_\infty$）|
| B.23 | 谱侧统一因子化 $Q=P(\lambda)H_0$；$(5b)$ 失败 $\iff\exists\lambda:\ker P\cap\operatorname{im}H_0\ne0$ | [Paper proof] + 8128/8128 | **✓ [Lean-conditional]**（`WorkA.finrank_range_comp` 秩公式、`B22.det_blockIdentity` 方块行列式、`B22.exists_root_of_pos_natDegree` 正次数有根）| 差在矩阵实例化与 $\lambda$-依赖运算 |
| B.24 | **B.24'（内蕴形式）**：偏算子 $\Phi:W=\mathcal LV\to\mathbb C^q$，$(5b)$ 失败 $\iff\exists0\ne u\in W:\Phi(u)\in\operatorname{span}\{u\}$；$\Phi=K_1|_W$ 唯一、$\dim W=h-r_1$ | [Paper proof] + **3453/3453** | ✗ | 可 Lean（良定义性 + 矩形铅笔判据），【待办】|
| B.25 | 矩形铅笔 $D-\lambda U$ 判据：$(5b)$ 失败 $\iff\exists\lambda:\operatorname{rank}(D-\lambda U)<k$ $\iff$ gcd 有正次数 | [Paper proof] + 3453/3453 | **✓ [Lean-conditional]**（`B25_Family`：`gcd_eval_eq_zero_of_common_root`、`gcd_is_const_of_no_common_root`、`no_common_root_iff_gcd_const`。差异：多子式与矩阵秩翻译是纸面） | 可 Lean（核/秩计算），【待办】|
| B.26 | Class I：$\mathcal V=\mathcal Z^\perp=\operatorname{row}[\mathcal L;c]$、$h=\dim(\mathcal V+\langle cA\rangle)\in\{q+1,q+2\}$、$(5a)\iff\mathcal VA\subseteq\mathcal V+\langle cA\rangle$（$cA\in\mathcal V$ 时即 $\mathcal V$ $A$-不变）| [Paper proof] + 2954/2954 | ✗ | 可 Lean（行空间/维数记账），【待办】|
| B.28 | 一般 $(p,r)$ 的子空间归约：$\mathcal V=\operatorname{row}[\mathcal L;C]$、$(5a)\iff\mathcal VA\subseteq\mathcal V+W_0$、$h=q+p+r_1-\dim(\mathcal V\cap W_0)$、以及不变子空间排除 $q+p<n\Rightarrow\operatorname{row}(CA)\not\subseteq\mathcal V$ | [Paper proof]（专家给出）| **✓ [Lean-conditional]**（`RowSpaceLayer.map_sup_le_iff`：分裂等价即分部 (a)。差异：其余分部（$\delta$ 记账、Class I 特例）见 `B31_32_33`/`B27`） | 可 Lean（行空间/维数 + 归纳），【待办】|
| B.28b | 分层参数 $\delta$：$h=q+p+\delta$，等号对应 $\delta=r_1-p$、不变排除 $\delta=0$、未决 $1\le\delta<r_1-p$ | [Paper proof] + [观察] | ✗ | 推导可 Lean；"未决=中间层"是问题定位 |
| **B.29** | $p=1$、**任意** $r$：$q_{\min}=n-1$（两情形：B.22 或 不变性+可观测性矛盾）| [Paper proof] + 精确验证（597/593/589 全失败）| **✓ [Lean-conditional]**（同 B.27 的 `B27.lean` 内核；差异：行空间实例化与 $r_1=2$ 的界）|
| B.30 | $\delta$ 三分（**修正后**）：$\delta=\rho$ 绝不可行（B.22）、$\delta=0$ 且 $q+p<n$ 绝不可行（B.28(3)）、$\delta=0$ 且 $q+p=n$ 可行（终阶）、中间层 **1107/1107 可行** | [Paper proof]（边界层）+ [精确验证]（中间层）| ✗ | 边界层可 Lean；中间层"可行"仍是经验 |
| **B.31** | **可行性的必要条件**：$(5b)$ 且 $q+p<n$ ⟹ $1\le\delta<r_1-p$ | [Paper proof] + 显式证书 + 0 反例（3400 候选）| **✓ [Lean-conditional]**（`B31.logic`/`B31.necessary` 逻辑骨架、`B32.no_intermediate` 的算术；差在行空间推导与两层不可行性）|
| **B.32** | **终端唯一区**：$r_1\le p+1\Rightarrow q_{\min}=n-p$（$p=1$ 即 B.29）| [Paper proof] + **385/385** | **✓ [Lean-conditional]**（`B32.terminal_only` + `B32.no_intermediate`；差在"次终端不可行"由 B.31 推出那一步）|
| B.33 | 分层与铅笔尺寸：$\dim(V/S)=q+\delta-\rho$，约化铅笔 $(p+q)\times(q+\delta-\rho)$ | [Paper proof] | **✓ [Lean-conditional]**（`B33.dim_quotient` 商维数 + `B33.dim_arith` 算术）|
| B.34 | 最窄中间层 $r_1=p+2$：$\delta=2$ 层 0/742（B.22）、$\delta=1$ 层 745/745 可行、$q_{\min}-q_0\in\{0,1,2\}$、$q_{\min}<n-p$ 745/745 | [精确验证] | ✗ | 经验结论，非定理 |
| B.35 | 两阶段流程（几何筛选对 B.31 可靠、省 44% 谱检验）+ $\Delta$ 剖面与阶差初步数据 | [精确验证] | ✗ | 工程性+统计性结论 |
| B.36 | 控制变量实验：同 $A$、同 $L_0$、只变 $C$ 支撑 ⟹ 剖面 $(2,2)$ 与 $(2,1,1)$ 的 $q_{\min}$ 相同（$\rho$-only）；$\rho=1$ 时 $q_{\min}=n-p$（B.32 独立确认）；$q_{\rm geom}=q_{\rm spec}$（谱延迟 0）| [精确验证]（单族四例）| ✗ | 经验结论 |
| B.37 | 谱可行性的统一刻画（四等价）| [Paper proof] | ✗ | 组装型：组分 B.1/B.17/B.24 有内核、B.8 纸面；两处识别（(ii)⟺B.17 的 $\ker=S$；(iii)⟺(iv) 即 B.8 取 $h=\rho$）未形式化 |
| **B.27** | **Class I 的 $q_{\min}=n-1$（定理）**：$p=r=1$、$(c,A)$ 可观测、$1\le q\le n-2$ ⟹ 任何可容许 $\mathcal L$ 都失败；$q=n-1$ 可行 | [Paper proof] + **2454/2454** | **✓ [Lean-conditional]**（`B27.krylov_le`/`eq_top_of_krylov` 情形 B 的归纳与 $\mathcal V=\top$、`B27.no_caseB` 维数矛盾；情形 A 用 `B22` 的 `exists_root_of_pos_natDegree`）| 差在行空间实例化与"$(5a)\Rightarrow$ 右乘 $A$ 封闭"|
| B.22 | 等号障碍：$h=q+r_1$, $q\ge1$ ⟹ $(5b)$ 必失败；$d_{\rm fin}=q$、$d_\infty=r_1$ | [Paper proof]（专家证明）| **✓ [Lean-conditional]**（B22.det_blockIdentity + exists_root_of_pos_natDegree）| 差在 $H_0$ 满行秩 ⟹ 秩不变、$K$ 存在性、秩化归三步（纸面 + 精确验证）|
| B.9 | 必要条件 $h<q+r_1$ | [已证-纸面] + [精确验证 56/56] | **✓ [Lean-conditional]**（`finrank_sup_lt_of_inf_ne_bot`、`inf_bot_of_finrank_sup_eq`；字面矩阵版 `MatrixBridge.rank_fromRows_lt_of_inf_ne_bot`、`inf_bot_of_rank_fromRows_eq`。差异：Kronecker 指标那半仍是纸面） | (β)：要用**非零左指标个数** $=q+r_1-h$（Kronecker 指标），Smith/Kronecker 未 Lean 化。**矩阵级前提已 Lean**：`RowSpace.rank_le_rank_fromRows₂`（$r_1\le h$）|
| B.9b | Type II 是空类（$k\le s$）| [已证-纸面] + [精确验证 93/93] | **✓** | `TypeII.typeII_rank_mono`、`typeII_vacuous`、`typeII_vacuous_geometric`；$h\ge r_1$ 由行堆叠（`finrank_mono`）给出，$s=q$ 作为假设 |
| B.10 | 谱障碍的定域（$\lambda\notin\operatorname{spec}\Lambda$）| [已证-纸面] + [精确验证 3/3] | ✗ | (β)：要 $\mathbb C[\lambda]$ 上矩阵秩与 $D(\lambda)$ 的可逆性（多项式矩阵层）|
| B.11 | $h=\dim(\mathcal Z^\perp+W)$、$h=q+r_1-\delta$ | [已证-纸面] + [精确验证 240/240] | **✓** | `TypeIGeom.B11_dim`：$\dim((C\sqcup R)\sqcup W)+(\dim((C\sqcup R)\sqcap W)-\dim C)=\dim R+\dim W$ |
| B.11b | $h=q+r_1-\dim(\pi R\sqcap\pi W)$（Type I 的几何形式）| [已证-纸面] + [精确验证 21/21] | **✓** | `TypeIGeom.mkQ_map_inf_eq`、`typeI_dim`、`typeI_geometric` |
| C.1 | $S=\mathcal J$ 闭包族 $\Rightarrow q_{\min}=n$ | [已证] | **✓** | `C1Closure.c1_of_closure_top`（$A$-不变闭包 $=\top\Rightarrow V=\top$）+ `C1Closure.c1_finrank`（$q_{\min}=n$）|
| D.1 | $P(A,B,S)\ge\dim S+\dim\frac{AS+S+B}{S+B}$ | [已证] | **✓** —— `D1Core.d1_P_lower_bound`（下界，专家已复核成立）；`PRecusion` 系列：`PRec.exists_sigma`（$\sigma=-\gamma\circ\beta$ 的线性构造，差异：无）、`PRecursionLift.lift_admissible`（构造步，差异：无）、`PRecursion.step_le`（$(\le)$ 半的组装）；空的可行族约定 $P=+\infty$ 已在卷宗写明 | `D1Core.d1_P_lower_bound` = 本条陈述（$P$ 的定义 `D1Core.P`）；逐 $W$ 版 `d1_lower_bound`；假设可行集非空 |
| D.2 | 递归定理 $\mathcal P=\dim T+\mathcal P'$ | [已证] | **部分 ✓** | `PRecursionStep`（$\le$ 半）+ `A3sem`（商维数）；$\sigma$ 区间包含仍纸面 |
| D.3 | $P\in\mathbf P$（$O(n^4)$）| [已证] | ✗ | 算法复杂度不是 Lean 的对象（需要可计算性/复杂度形式化）|
| D.4 | —— | [Lean] | **✓** | 见 tools/lean |
| E.1 | $\rho_{ci}=P(T,B,U_0)$ | [已证] | ✗ | (α)+(ζ) |
| E.2 | $\rho_{ci}\in O(n^4)$ | 由 D.3 | ✗ | 同上（复杂度）|
| F.1 | **秩屏障** $\rho\le r(\lambda_0)$ | [已证-纸面] + [精确验证 1484+113] | **✓ [Lean-conditional]**（`RankBarrier.rank_barrier` + `F1_Matrix` 前置四条。差异：F.1 的**字面矩阵**主体尚未拼装，见 `proof/F.1`） | `RankBarrier.rank_barrier`：$\dim(VM+J)\le j+\dim\pi_J(\text{range}M)$；"$(5b)$ 要求左端 $=j+\rho$"那一步是 (α)，仍纸面 |
| F.2 | $\min_\lambda r<\rho_{ci}\Rightarrow$ 无解 | [已证-纸面] | ✗ | 由 E.1（纸面）+ F.1 的算术；E.1 未 Lean |
| G.1 | $\mathrm{DEC}(q)\in\exists\mathbb R$ | [已证-纸面] + 精确 + 部分 Lean | **部分 ✓** | (ε)：编码的**规模/次数**不是 Lean 的对象；`CoreLemma`、`ExistsRLemmas` 已覆盖关键引理 |
| H.1 | 商等价定理 | [已证-纸面] + [精确验证] | **✓** | `QuotientEquivalence.qe_colspace / qe_finrank / qe_well_defined` |
| H.2 | 方阵 $\iff q=t$；$r+t=w-q+v-2s$ | [已证-纸面] + 精确 | **✓** | `DimArithmetic.no_truncation`、`r_add_t`、`square_iff`、`m_iff_h`（$\mathbb N$ 无截断前提由 `no_truncation` 支撑）|
| H.3 | $d=0$ 边界 | [已证-纸面] + [精确验证 40/40] | **✓** | `proof/d0_boundary/lean/MyProof/D0Boundary.lean`：`d0_rank_iff`（逐 $\lambda$）+ `d0_forall`（$\forall\lambda$）|
| I | 判据矩阵 | 汇总表 | ✗ | 不是单一命题（表的每一行各自有等级）|
| J | 行列式因子判据 | [已证-纸面] + [精确验证] | ✗ | (β)：$\mathbb Q[\lambda]$ 上的 gcd/Smith |
| K.1 | $m=3$：每个非零双向量可分解 | [已证-纸面] | ✗ | (δ)：需 $\Lambda^2\mathbb C^3$ 与 Plücker 的建模（Mathlib 有 `ExteriorAlgebra`，但"$\mathrm{Gr}(2,3)=\mathbb P(\Lambda^2\mathbb C^3)$"未形式化）|
| K.2 | $m=4,\ \ell\ge2$：必有可分解元（二次型零点）| [已证-纸面] + 精确 20/20 | **✓（内核）** | `Isotropy.K2_isotropic`（限制到 $\ge2$ 维仍各向同性）、`exists_ne_zero_quadraticMap_eq_zero`；"Klein 二次型 $=0\iff$ 可分解"未形式化 |
| K.3 | $\ell\ge N-(2m-4)$：射影维数计数 | [已证-纸面] | ✗ | (δ)：射影维数定理（只给**复**交点，实点需另证）|
| B.10b | 谱失败轨迹在**层内**闭（$\Lambda$ 正则 + 固定 $(\rho,h)$ 层）| [已证-纸面]（紧合性）| ✗ | (δ)：需要 $\mathbb P^1$ 紧合性与层上正则选取的代数几何语言；Mathlib 无 proper morphism/closed-map 的代数几何层 |
| B.11c | 计数恒等式 $h=s_0+q-\dim(R\cap S)$ 与 Type I 判据 | [已证-纸面] + 精确验证 | **✓ [Lean-conditional]** | `Dims.b11c_modular` + `Dims.b11c_add`（模格恒等式 + 维数相加）；差在 $h,s_0$ 的矩阵实例化 |

| B.12 | 谱条件的可观性归约（$(5b)\iff(E,\Lambda)$ 可观测 $\iff\operatorname{rank}\mathcal O=q$）| [已证-纸面] + [精确验证 44/44] | **✓ [Lean-conditional]**（`B12_Observability`：`pow_finrank_eq_neg_sum`、`observable_iff_krylov`、`observable_iff_rank_krylov`，Cayley–Hamilton。差异：$\ker[C;CA]$ 归约是纸面） | (γ)：需要特征向量/PBH 语言；Mathlib 有代数闭域特征值存在性，但"PBH + 观测性矩阵"这一层未建；【待办】|
| G.2 | 紧凑可观性编码（$s$ 分层 + 零化子 + 观测性左逆）| [已证-纸面] + [精确验证（2 见证 × 16 约束）] | ✗ | 编码规模不是 Lean 的对象；可 Lean 的部分是 B.12（已列）与维数记账 |
| B.13 | incidence 维数（已证）+ 覆盖判据（**条件性**，两处未修）| [已证-纸面]（维数）/ [条件性]（覆盖）| ✗ —— **B.13a（入射/纤维/维数估计）已完整纸面证明**（卷宗内）；覆盖定理仍缺。无 Lean | (δ)：射影维数定理与 incidence variety 未在 Mathlib 建模 |
| B.13b | 比例性轨迹余维 $\varepsilon$ 与必要条件 $q-r+\varepsilon\le n-r_1-1$ | [已证-纸面] + 四实例核验 | ✗ | (δ)：同上；四实例的比例性核验是脚本（`attempts/60`）|
| B.11d | CSS 归约：CSS 下 $\exists(5a)\wedge(5b)\iff\exists(5a)\wedge$计数侧 | [已证-纸面] | **✓ [Lean-conditional]** | `Logic.b11d_css`（逻辑骨架）+ `Logic.typeI_kills`（Type I 的算术内核）；差在 $\operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]\le q+r_1$ 的矩阵秩不等式 |

| B.13c | 失败的精确判据 $\exists x\in V\setminus\mathcal Z,\lambda:(\lambda I-A)x\in\mathcal Z$ | [已证-纸面] + 6 个显式证书 | **✓ [Lean-conditional]** | `Criterion.b13c_factor`（因子化恒等式）；差在 $x\notin\mathcal Z\iff\mathcal Lx\ne0$ 与全称量词的组装 |

| B.13d | $\varepsilon=0$ 三情形刻画（$\iff$ 纯秩条件）| [已证-纸面] + 5983/5983 | ✗ | (β)：可 Lean（线性代数），【待办】|
| B.13e | 单-$\lambda$ 覆盖证书：$\exists\lambda:(\lambda I-A)V=K\Rightarrow$ 整族不可行（除有限例外）| [已证-纸面] + 探针族 10 点核验 | ✗ | (β)：可 Lean（线性同构 + 反证），【待办】|
| B.13f | 标量情形：不可行 $\iff$ 二次方程（$\dim V=\dim K=1$ 时该式**恒零**，判据退化为 $V\ne K$）| [已证-纸面] + 2676/2676 | ✗ | (β)：可 Lean（叉积恒等式），【待办】|
| B.14 | 可解类 (T*)：$\operatorname{rank}(P_K(\lambda I-A)B_V)=\dim V\ \forall\lambda\Rightarrow$ 各阶谱可行 | [已证-纸面] + 56/595 覆盖、56/56 有见证 | ✗ | (β)：可 Lean（(T*) ⇒ 无掉秩，一行反证），【待办】|
| B.15 | 阶差无界：$k$ 个同型副本的直和把阶差乘 $k$ | [已证-纸面] + [**Lean 内核**] (`LemmaA.exists_witness_not_mem` 避免性；`LemmaB.finrank_range_prodMap` 秩可加) + $k=1,2,3$ 精确核验 | ✓ | **差异**：Lean 证的是两个抽象核（满射+交集为零 ⟹ 见证；直和映射的秩可加），分块直和/矩阵 `fromBlocks` 的实例化是纸面 |
| B.16 | 分层判据（按 $s=\dim(V\cap\mathcal Z)=\dim V-\operatorname{rank}(J_{\mathcal Z}|_V)$ 分三层）| [已证-纸面] + $s{=}0$ 层 402/402 | ✗ | (β)：可 Lean（层上核判据），【待办】|
| B.16b | 中间层结构限制 $(5a)\Rightarrow A(V\cap\mathcal Z)\subseteq\mathcal Z$；"铅笔不满列秩 $\ne$ 失败"的显式反例 | [已证-纸面]（条件）+ [精确验证]（反例）| **✓ [Lean-conditional]** | `Criterion.b16b_mapsTo`（抽象映射层面；矩阵实例化见 RowSpace）；反例部分是实例 |

| B.17 | 永久核 + 商铅笔判据 | [已证-纸面] + 1513/1513 | **✓ [Lean-conditional]** | `Criterion.permanent_kernel`（永久核）+ `Criterion.ker_eq_iff`（判据的核形式）；差在"诱导映射 $W/S\to W$ 单射"的商空间表述 |

| B.18 | $p=r=1$ 的结构与降维：$r_1=2$、$s_0\in\{2,3\}$、$\rho=q-1$ | [已证-纸面] + 714/714 | **✓ [Lean-conditional]**（`RowSpaceLayer.finrank_range_prod_le`：$r_1\le2p$。差异：其余维数记账仍是纸面） | (β)：可 Lean（维数记账），【待办】|
| B.18b | $p=r=1$ 终阶（$q=n-1$，$d=0$）必然可行 | [已证-纸面] + 589/589 | ✗ | (β)：可 Lean（"$\ker c$ 无特征向量" + 秩），【待办】|
| B.18c | $p=r=1$ 的坏像落在 $\ker c$ 内；$d=1$ 判据 = 像包含 | [已证-纸面] + 229/229 + 240 样本 | **✓ [Lean-conditional]** | `Dims.b18c_annihilate`（第 1 条）；差在 $\operatorname{im}\psi\subseteq\ker c$ 的集合表述与"$z\in\operatorname{im}\psi$"判据 |

| B.18d | 循环坐标下 $\operatorname{im}\psi$ 的精确刻画（$w\in\operatorname{im}\psi\iff P_w$ 不是非零常数）| [已证-纸面] + 300/300 | **✓ [Lean-conditional]** | `PsiImage.recX_natDegree_and_ne`、`natDegree_X_mul_add_of_lt`、`exists_root_of_natDegree_eq_two`；差在 $P_w$ 的显式组装 |

| B.18e | $d=1$ 三分解：$z\in V$ 不可容许（已证）、$z_2\ne0$ 自动可容许（已证）、$z_2\ne0\Rightarrow z\in\operatorname{im}\psi$（已证）| [已证-纸面] + **412/412** | ✓ [Lean-conditional] PsiImage.recX_natDegree_and_ne / natDegree_X_mul_add_of_lt / exists_root_of_natDegree_eq_two | 差在 $P_w$ 的显式组装（纸面 + 412/412）；另 `Logic.b18e_family` 给出整族不可行的逻辑骨架 |


| K.4 | $m\ge5,\ell\le3$ 的算法 | [精确验证] | ✗ | 算法正确性（gcd / 理想成员）不是 Lean 的对象 |
| A.0 | $(5a)$ 的商形式（$\pi(\mathcal V A)\subseteq U$）| [已证-纸面] | **✓（第一步）** | `A0Row.five_a_row_iff`：秩等式 $\iff$ 行空间包含（即 $(5a)\iff\operatorname{row}(\mathcal LA)\subseteq\operatorname{row}[\mathcal L;CA;C]$）；商形式那一步仍纸面 |
| C.1–C.5 | $(3,1)$ 层五条判据 | [已证-纸面]（三处有 Lean 支撑）| **部分 ✓** | `Theorem12`、`QuadraticMu2`、`Perturbation` 覆盖关键引理；闭包族 C.1 另有 `C1Closure.c1_of_closure_top`；判据本体仍是 (α) |

---

## 2. 本轮（2026-11-01）新增的 Lean

> **2026-11-01 第 12 轮清理**：维数引理以前在 7 个文件里各抄一份证明。现在抽到
> [`tools/lean/MyProof/Prelude.lean`](../trash/lean_removed_2026-11-19/tools/lean/MyProof/Prelude.lean)
> （`finrank_inter_add_finrank_map_mkQ`、`finrank_map_add_finrank_inf_ker`、`finrank_pos_of_ne_bot`），
> 其余文件 `import MyProof.Prelude`，本地保留**一行别名**（`:= finrank_inter_add_finrank_map_mkQ T B`），
> 证明只有一份。`check_lean.sh` 先 `lake build MyProof.Prelude` 生成 `.olean`，再逐文件 `lake env lean`。
> **教训**：这轮我先用脚本"整段删除"重复引理，误删了 `RankBarrier.rank_barrier` 与 `Eigen.exists_eigenvector`
> 等声明（docstring 与下一条声明粘连被一并切掉）；已 `git checkout` 回滚，改为"删证明、留别名"的保守做法。

| 文件 | 引理 | 对应命题 |
|---|---|---|
| `QuotientEquivalence.lean` | `qe_colspace` / `qe_finrank` / `qe_well_defined` / **`qe_full`** | H.1（商等价）；`qe_full` 就是**陈述本身** |
| `RankBarrier.lean` | `rb_finrank_inter_add` / `rank_barrier` / **`five_a_iff`** / **`rank_barrier_full`** | F.1 + $(5a)$ 的秩形式；`rank_barrier_full` 是 F.1 的**陈述本身** |
| `D0Boundary.lean` | `d0_rank_nullity` / `d0_rank_iff` / **`d0_forall`** | H.3（$d=0$ 边界）；`d0_forall` 是**陈述本身** |

`check_lean.sh`：**31 个文件全部 OK**（退出码 0）——本轮把此前**不在回归里**的 12 个 P 递归/$(3,1)$ 层文件也纳入了闸门。

### 2.1 陈述一致性（回答"Lean 与命题是否同一句话"）

新增 [tools/lean/STATEMENT_MAP.md](../tools/lean/STATEMENT_MAP.md)：**逐个 Lean 声明**登记
"对应哪条命题 / 差异在哪（弱在哪、强在哪）"，并由
[audit_lean_statements.py](../tools/hygiene/audit_lean_statements.py) 机械检查：
**每个声明都登记了**、**每个登记都真实存在**、**每条都写了"对应"和"差异"**。

当前：**154 个声明 / 142 条登记 / 0 问题**（2026-11-04 复核）。

> **2026-11-04 新增**：`TypeII.lean`（B.9b：`typeII_rank_mono`、`typeII_count`、`typeII_vacuous`、
> `typeII_vacuous_geometric`）与 `TypeIGeom.lean`（B.11b + B.11：`mkQ_map_inf_eq`、`typeI_dim`、
> `typeI_geometric`、`B11_dim`），WSL 下 `lake env lean` **0 error 0 warning**。
> 同时新增闸门 [`audit_lean_coverage.py`](../tools/hygiene/audit_lean_coverage.py)：
> 把 `docs/02` 的 `[Lean]` 标记与本表的 ✓/✗ **逐条对齐**（当前 35 条命题、35 行、0 不一致）。
> 另外新增 `RowSpace.lean`（(α) 桥）：`rowSpace`、`rank_eq_finrank_rowSpace`、
> `rowSpace_fromRows`（行堆叠的行空间 = 两个行空间之并）、`rank_le_rank_fromRows` 与
> `rank_le_rank_fromRows₂`（$r_1\le h$ 的矩阵级形式），WSL 下 0 error 0 warning。
> **作用**：把论文里"堆叠矩阵的秩"翻译成 `finrank`/`Submodule` 语言——这是 B.9、B.10 等
> 以矩阵秩陈述的命题的**共同前提**。
> 这一轮还更正了本表 8 处**陈旧行**（A.2、A.3、C.1、D.1、B.1、B.2、B.3、B.5、H.2 —— 早已有 Lean 却标 ✗）。

> 这就是用户 2026-11-01 要求的"避免因 Lean 描述不一致而误判"的机制：
> 今后 `[Lean]` 必须带**声明名**（CLAUDE §4 硬规则 6），而声明名必须能在 STATEMENT_MAP 里查到它的"差异"。

### 2.2 已知的"描述差异"（必须记住，别误读）

| 差异 | 影响 |
|---|---|
| 论文用**矩阵/秩**语言，Lean 用**子空间/维数**语言 | 共同前提；"矩阵行空间 = 相应子空间"未形式化（§0） |
| `rank_barrier_full` 的 $r(\lambda)$ 写成 $\dim\pi_J(\operatorname{range}M)$ | 与"$\operatorname{rank}[\lambda I-A;C;CA]-j$"的等同是纸面一步 |
| `qe_full` 的 $r+t$ 写成 $\dim((V+Z)/S)$ | 两者的相等是纸面维数记账 |
| `d0_forall` 未形式化"无特征向量"这个说法 | 该说法是 $\lambda$ 的定义层 |
| 单实例见证（R17A / R17Cert / G4） | **不是定理**，不能当 `[Lean]` 论证全称命题 |

---

## 3. 下一步"能 Lean 但还没做"的排序

| 序 | 目标 | 缺什么 | 量 |
|---|---|---|---|
| **0** | **α 桥**（矩阵/秩 ↔ 子空间/维数）| **已完成**：`alpha_colspace`（列空间）、`alpha_rank_dual`（行秩 = 列秩）、`alpha_row_mul`（$A^{\mathsf T}\ell=\ell\circ A$）、`alpha_five_a`（$(5a)$ 的秩形式）、`alpha_matrix_rank_row` / `alpha_matrix_rank_col`（**真矩阵的秩 = 行/列空间维数**）| — |
| 1 | **A.3**（下界）| **完成（维数部分）**：`A3Bound.a3_rows`（$q\ge r$）、`a3_epsilon`（$q\ge r+\varepsilon$）、`a3_rho`（$c\ge1\Rightarrow q\ge\rho+1$）+ `Eigen.c_pos_of_five_b`（$(5b)\Rightarrow c\ge1$）；**缺** $c_0$（属 A.4/$P$）| 小 |
| 2 | **B.1**（商铅笔）| **已完成**：`PencilEquivalence.pencil_rank_forall`（$\forall\lambda$ 原句）、`pencil_rank_eq`、`finrank_sup_eq_add_quotient` | — |
| 3 | **B.3**（$\rho=0$ 层）| **已完成**：`Rho0Layer.rho_zero_iff`（$\pi_J V=\bot\iff V\le J$）、`five_a_of_le`（$(5a)\iff AV\le J$）、`five_b_auto`（$(5b)$ 自动）| — |
| 4 | **K.2**（$m=4$ 各向同性）| **内核完成**：`Isotropy.exists_root_quadratic`、`exists_ne_zero_quadraticMap_eq_zero`、`K2_isotropic`；**缺**"Klein 二次型 $=0\iff$ 可分解"（$\Lambda^2$/Plücker 建模）| 中 |
| 5 | **D.1**（$P$ 的下界）| 先形式化 $P$ 的定义（`PVal` 已有）| 中 |
| 6 | **C.1**（闭包族）| **已完成**：`C1Closure.c1_of_closure_top`（$A$-不变闭包 $=\top$ ⟹ $V=\top$）+ `c1_finrank` | — |
| — | A.2/B.2/B.4/B.5（特征值类）| (γ)：需要把 PBH 建起来 | 大 |

**结论**：主线的三个**结构性**命题（H.1、F.1、H.3）现在都有**陈述级** Lean；
α 桥的"翻译"部分已 Lean（列空间 / 行秩=列秩 / 行乘 $A$ / $(5a)$ 的秩形式），
剩下的只是"把矩阵当数据"——那是**存量工程的桥**，不影响已有定理的正确性。
