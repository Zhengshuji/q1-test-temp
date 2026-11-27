# 02 · 已证命题

> **只收有纸面证明或 Lean 内核的命题**。Python 精确复核只算"验证"，位于 `proof/<claim>/verify.py`；
> 经验性结论在 `workspace/`，不在本文件（见 §0.2）。
> 每条：陈述 → 证明 → 等级 → 位置。
>
> **2026-11-26 依赖规则**：本表是**本地框架的证明与 Lean 索引**。Paper I / Paper II 覆盖的结论
> （压缩、沙包、结构界、$\exists\mathbb R$ 上界、固定阶与 FPT、最小阶与谱下界）在对外写作中优先引论文；
> 但本表的条目**不因此失效**：论文未覆盖的部分、以及本地进一步探索得到的固定成果，仍是本项目的
> 独立结果，按各自的等级保留。只有与论文冲突时才以论文为准。

## §0 编号与归并

**§0.1 本文件按"主条目 + 分部"组织**：`B.18（b）〔原 B.18b〕` 表示该主条目的第 (b) 分部，原编号仍可检索。
旧编号与新主条目的完整对应：

| 旧编号（可继续引用）| 新主条目 | 分部 |
|---|---|---|
| A.0 | A.1 · 维数分解与下界 | （a）|
| A.1 | A.1 · 维数分解与下界 | （b）|
| A.2 | A.1 · 维数分解与下界 | （c）|
| A.3 | A.1 · 维数分解与下界 | （d）|
| A.4 | A.1 · 维数分解与下界 | （e）|
| B.1 | B.1 · 商铅笔等价 | — |
| B.2 | B.2 · 顶层可观测与 PBH | （a）|
| B.5 | B.2 · 顶层可观测与 PBH | （b）|
| B.3 | B.3 · $\rho=0$ 层 | — |
| B.4 | B.4 · $V=\mathbb C^n$ 的判据 | — |
| B.6 | B.6 · 右最小指标与无穷初等因子 | （a）|
| B.7 | B.6 · 右最小指标与无穷初等因子 | （b）|
| B.8a | B.8 · 铅笔的 Smith/Kronecker 结构 | （a）|
| B.8b | B.8 · 铅笔的 Smith/Kronecker 结构 | （b）|
| B.9 | B.9 · 边界与等号结构 | （a）|
| B.9b | B.9 · 边界与等号结构 | （b）|
| B.19 | B.9 · 边界与等号结构 | （c）|
| B.20 | B.9 · 边界与等号结构 | （d）|
| B.10 | B.10 · 谱障碍的定域 | （a）|
| B.10b | B.10 · 谱障碍的定域 | （b）|
| B.11 | B.11 · Type I/II 的几何形式 | （a）|
| B.11b | B.11 · Type I/II 的几何形式 | （b）|
| B.11c | B.11 · Type I/II 的几何形式 | （c）|
| B.11d | B.11 · Type I/II 的几何形式 | （d）|
| B.12 | B.12 · 谱条件的可观性归约 | — |
| B.13 | B.13 · 计数判据族 | （a）|
| B.13b | B.13 · 计数判据族 | （b）|
| B.13c | B.13 · 计数判据族 | （c）|
| B.13d | B.13 · 计数判据族 | （d）|
| B.13e | B.13 · 计数判据族 | （e）|
| B.13f | B.13 · 计数判据族 | （f）|
| B.14 | B.14 · 投影铅笔满列秩类 | — |
| B.15 | B.15 · 避免性引理 | — |
| B.16b | B.16 · 分层判据 | （b）|
| B.16 | B.17 · 统一商铅笔定理 | （a）|
| B.17 | B.17 · 统一商铅笔定理 | （b）|
| B.21 | B.17 · 统一商铅笔定理 | （c）|
| B.18 | B.18 · $p=r=1$ 的结构 | （a）|
| B.18b | B.18 · $p=r=1$ 的结构 | （b）|
| B.18c | B.18 · $p=r=1$ 的结构 | （c）|
| B.18d | B.18 · $p=r=1$ 的结构 | （d）|
| B.18e | B.18 · $p=r=1$ 的结构 | （e）|
| B.22 | B.22 · 等号障碍（独立引理） | — |
| B.23 | B.23 · 统一分块因子化 | — |
| B.24 | B.24 · 内蕴形式 $\Phi$ | — |
| B.25 | B.25 · 矩形铅笔与 gcd 判据 | — |
| B.26 | B.28 · 子空间归约与分层参数 | （a）|
| B.28 | B.28 · 子空间归约与分层参数 | （b）|
| B.28b | B.28 · 子空间归约与分层参数 | （c）|
| B.33 | B.28 · 子空间归约与分层参数 | （d）|
| B.37 | B.37 · 谱可行性的统一刻画 | — |
| B.31 | B.31 · 可行性的必要条件（独立引理） | — |
| B.27 | B.32 · 终端唯一区 | （a）|
| B.29 | B.32 · 终端唯一区 | （b）|
| B.32 | B.32 · 终端唯一区 | （c）|
| C.1 | C.1 · 特殊族的精确值 | — |
| D.1 | D.1 · $P$ 的多项式可解性 | （a）|
| D.2 | D.1 · $P$ 的多项式可解性 | （b）|
| D.3 | D.1 · $P$ 的多项式可解性 | （c）|
| D.4 | D.1 · $P$ 的多项式可解性 | （d）|
| E.1 | D.1 · $P$ 的多项式可解性 | （e）|
| E.2 | D.1 · $P$ 的多项式可解性 | （f）|
| F.1 | F.1 · 秩屏障 | （a）|
| F.2 | F.1 · 秩屏障 | （b）|
| G.1 | G.1 · 判定问题的复杂度上界与编码 | （a）|
| G.2 | G.1 · 判定问题的复杂度上界与编码 | （b）|
| H.1 | H.1 · 商等价、方阵条件与 $d=0$ 边界 | （a）|
| H.2 | H.1 · 商等价、方阵条件与 $d=0$ 边界 | （b）|
| H.3 | H.1 · 商等价、方阵条件与 $d=0$ 边界 | （c）|
| K.1 | K.1 · 双向量可分解性 | （a）|
| K.2 | K.1 · 双向量可分解性 | （b）|
| K.3 | K.1 · 双向量可分解性 | （c）|
| K.4 | K.1 · 双向量可分解性 | （d）|

**§0.2 不在本文件的内容**

| 内容 | 位置 | 理由 |
|---|---|---|
| B.30 / B.34 / B.35 / B.36（$\delta$ 三分与阶差）| `workspace/augmentation_family/attempts/99_delta_program.md` | 纯 `[精确验证]`/经验，按 CLAUDE §2 不进 docs |
| 判据矩阵（I.1–I.5）| 同上（附录 B）| 参考表，不是命题 |
| 复核记录（附：复核）| 同上（附录 C）| 过程记录 |
| $(3,1)$ 层的四条格子级判据（旧 `## C.`）| 同上（附录 D）| 属于 C.1 族的细化，条目里已有指针 |

**§0.3 合并原则**：同一主题的多条（如 `B.18b`–`B.18e` 都是 $p=r=1$ 的推论、`B.13b`–`B.13f` 都是计数判据的变体）
合为一个主条目的分部；**每条分部保留自己原来的陈述、证明、等级与位置**，不重写证明。
`B.22`（等号障碍）与 `B.31`（可行性必要条件）保持独立——两者被后续结果反复引用。


**§0.4 证明等级与验收规则（2026-11-06 确立）**

| 级别 | 含义 | 计入"完成证明"？ |
|---|---|---|
| **L4 · Lean（字面）** | Lean 内核覆盖**命题的字面陈述**（`lake build` 0 error，登记在 `STATEMENT_MAP`）| **是** |
| **L3 · 可接受纸面 + Lean** | 纸面证明经专家复核或来源于可信文献，且非平凡部分有 Lean 内核 | **是** |
| **L2 · 可接受纸面（无 Lean）** | 专家复核过、或来源可信（论文/经典教材）的纸面证明 | 是（M≥3 即可；Lean 为加分项）|
| **L1 · 仅纸面（自检）** | 只有本项目自写的纸面证明，未经外部复核 | 否 |
| **E · 实验** | 精确算术/数值复核、随机实例测试 | **不计入证明**（只用于筛假与找方向）|

**验收规则（2026-11-07 修订）**：**能用 Lean 就用 Lean；不能或不方便用 Lean 的，接受可信度高的纸面证明**
（专家复核或论文/教材来源）。纸面证明**可以含 Lean 也可以不含**，含 Lean 更好。
因此"完成"= M≥3 且（Lean 可行则已形式化）；**L2 也可以是完成**，只需注明"Lean 不可行/不便"或"待补"。
E 类证据**永远**不能替代证明（CLAUDE §4/§18）。


---

---

### B.1 · 商铅笔等价

**B.1（商铅笔）** $(5b)\iff\operatorname{rank}Q_{\mathcal V}(\lambda)=\rho\ \forall\lambda$，$Q_{\mathcal V}(\lambda)=\lambda\pi(\mathcal L)-\pi(\mathcal LA)$。

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.1/](../proof/B.1/README.md)。
**等级**：[已证] $+$ **[Lean]**（`PencilEquivalence.pencil_rank_forall` = 本条原句；逐 $\lambda$ 版 `pencil_rank_eq`；核心恒等式 `finrank_sup_eq_add_quotient`：$\dim(W\sqcup J)=\dim J+\dim\pi_J(W)$。$\operatorname{rank}$ 用 $\dim$ 行空间写，依据 `AlphaBridge.alpha_matrix_rank_row`）。


---

### B.2 · 顶层可观测与 PBH

**B.2（a）〔原 B.2〕（顶层）** 若 $\rho=d$，则 $(5b)\iff(D_W^{\mathsf T},T_W)$ **可观测**。

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.2/](../proof/B.2/README.md)。
**等级**：[已证]（**完整证明**：[proof/top_layer_observability/theorem.md](../proof/top_layer_observability/theorem.md)）$+$ **[Lean-conditional]**（`PBH.pbh_iff` = 第三步 PBH；`PBH.Observable` = 可观测性定义。**差异**：分块形式已有**逐点版**（`B2Block.block_on_J`/`block_on_W`）；未做的是"组装成矩阵 + 接秩条件"的建模）。
**等级**：[已证] $+$ **[Lean-conditional]**（`CyclicVector.isCyclic_iff` = 事实 1（循环 $\iff$ 无含 $v$ 的真不变子空间）；`not_cyclic_of_left_eigen` + `exists_left_eigen_of_not_cyclic` = **双向**；`CyclicStructural.b5_five_b_fails_imp_not_cyclic` = **$(5b)$ 秩降 $\Rightarrow$ $v_W$ 不循环**（经 `ProjW` 的桥梁与 `exists_functional_of_rank_drop`））。**双向都已 Lean**：`b5_five_b_fails_imp_not_cyclic`（$(5b)$ 失败 $\Rightarrow$ 不循环）$+$ `b5_converse`（不循环 $\Rightarrow$ 存在 $\lambda$ 使秩降）。"循环"写成 $\operatorname{span}\{T_W^kv_W\}=W$，秩形式由 $\alpha$ 桥翻译）。

---


---

### B.3 · $\rho=0$ 层

**B.3（$\rho=0$ 层）** $\rho=0\iff\mathcal V\subseteq\mathcal J$；此时 $(5a)\iff S\subseteq\mathcal J$ 且 $SA\subseteq\mathcal J$，且 $(5b)$ 自动。

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.3/](../proof/B.3/README.md)。
*专家意见（2026-11-06）*：$\rho=0$ 的等价**不需要** $L_0\ne0$。
**等级**：[已证] $+$ **[Lean]**（`Rho0Layer.rho_zero_iff`：$\pi_J V=\bot\iff V\le J$；`Rho0Layer.five_a_of_le`：$V\le J$ 时 $(5a)\iff AV\le J$；`Rho0Layer.five_b_auto`：$V\le J$ 且 $AV\le J$ ⟹ 每个 $\lambda$ 的 $(5b)$ 自动）。


---

### B.4 · $V=\mathbb C^n$ 的判据

**B.4（$V=\mathbb C^n$ 的可行性判据；2026-11-06 按专家意见更正）** $\mathcal V=\mathbb C^n$ 满足 $(5b)$ $\iff$ **$A$ 在 $K=\ker[C;CA]$ 里没有（右）特征向量**，即
$$\nexists\,0\ne x:\quad Cx=0,\quad CAx=0,\quad \exists\lambda:\ (\lambda I-A)x=0 .$$
*更正说明*：原表述写作"$A^{\mathsf T}$ 没有落在 $K$ 里的特征向量"，与推导不符——使铅笔降秩的是**右**特征向量（$(\lambda I-A)x=0$ 且 $Cx=CAx=0$），不是对偶侧的 $A^{\mathsf T}$ 特征向量。相应的 Lean 陈述（`B4FullSpace.b4_iff_no_eigenvector`）需按本更正复核。 **等级**：[已证] $+$ **（内核写法待重述）**（`B4FullSpace.b4_iff_no_eigenvector` = 本条陈述；`B4FullSpace.b4_finrank_iff` = 对偶维数判据 $\dim(ME+J)=n\iff\ker M^{\mathsf T}\cap J^{\perp}=0$）。归档：[proof/b4_full_space/](../proof/b4_full_space/README.md)。

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.4/](../proof/B.4/README.md)。

*约定*：本项目用**行约定**，故正确形式是**右**特征向量（见卷宗的「约定与核验」一节）；对偶写法（$A^{\mathsf T}$）与铅笔秩降**不等价**——精确核验 3962 例，对偶写法有 117 个反例。`B4FullSpace` 的现有内核编码的是对偶写法，**不再算作本条内核**。**等级**：[已证]。
*论文写法（专家建议）*：设 $\mathcal V=\mathbb C^n$、$K=\ker[C;CA]$，则全空间铅笔的列秩恒为 $n$ $\iff$$\ker(A-\lambda I)\cap K=\{0\}$ 对一切 $\lambda$，即 $A$ 的右特征向量都不在 $K$ 里。`B4FullSpace` 的原内核作为**独立辅助引理**保留（对偶形式的零化子恒等式），不再计入本条覆盖。


---

### B.6 · 右最小指标与无穷初等因子

**B.6（a）〔原 B.6〕（右最小指标为零）** 设 $L$ 满足 $(5a)$。则观测器铅笔 $Q_L(\lambda)=[\lambda L-LA;CA;C]$ 的**右最小指标全为 $0$**
（右零模有常值基）。只用 $(5a)$，不需要 $(5b)$。

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.6/](../proof/B.6/README.md)。
**等级**：[已证-纸面] $+$ **[Lean-conditional]**（`KronCoeff.kron_coeff_chain_strong`：系数方程的倒向归纳；`KronCoeff.kron_coeff_mem_N`：系数全在 $N$ 里。**差异**：多项式←→系数序列的翻译、以及"右零模有常值基 ⟹ 右最小指标为 0"的 Kronecker 步骤在纸面，未 Lean 化）$+$ **[精确验证 150/150]**（$n=6,7,8$，每维 50 个满足 $(5a)$ 的铅笔）。
**等级**：[已证-纸面] $+$ **[Lean-conditional]**（`KronFactor.kron_block_factor`：分解恒等式 $LA=XL+Y_1CA+Y_2C\Rightarrow\lambda L-LA=(\lambda I-X)L-\dots$，仍用于第 2 步起点的写法；**差异**：行列式因子的 $\mu$-赋值未 Lean 化）$+$ **[精确验证 151/151]**（$n=6,7,8,9,10$，含 43 个不可行；反例 0）。


---

### B.8 · 铅笔的 Smith/Kronecker 结构

**B.8（a）〔原 B.8a〕（Smith 判据；(5b) $\iff$ 无有限初等因子）** 设 $L$ 满足 $(5a)$、$h=\operatorname{rank}[L;CA;C]$。则
$$(5b)\iff d_{\rm fin}=0,$$
其中 $d_{\rm fin}$ 是 $Q_L(\lambda)$ 的 Smith 形中**非零不变因子的次数之和**（等价地：有限初等因子的总大小）。

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.8/](../proof/B.8/README.md)。

*T1/T2/T3（专家第七轮定理包）*：**T1** 有界次数 Bézout（$D=d-1$，乘子次数 $\le d-1$，已给完整证明）；**T2** 可容许层 $\mathcal A_k=\{\operatorname{rank}B=k,\ \operatorname{rank}[\mathcal LA;B]=k\}$ 上 $\mathcal C_k=\{R\in\mathcal A_k:\Delta_k\in\mathbb C^\times\}$ 是**构造集**（经 T1 化为秩条件）；**T3** $\mathrm{FEAS}=\bigcup_{k=0}^{\min(m,n)}\mathcal C_k$，每层法秩固定、判据固定尺寸。限定：$R$ 取实数时只得实构造集，复情形另列；规模 $\sim k\binom{m}{k}\binom{n}{k}$（中间层指数），是结构性定理而非多项式算法；且构造性**不**削弱硬度目标。
*第三接口（专家第五轮 Q3）*：$(5b)\iff\Delta_h(\lambda)\in\mathbb C^\times$ —— **精确**判据，不需要 $\mathcal B=\varnothing$（对比 B.13c 只充分、F.1 只必要）；Bézout 形式 $\sum_i u_i p_i=1$ 给出更适合 $\exists\mathbb R$ 编码的有限系数方程组。与 $d_{\rm fin}=0$ 的等价待按 Kronecker 记账恒等式核（B.6/B.8b/专家 §3.1 三处尚未在本文记号下对齐）。*专家意见（2026-11-06）*：矩形情形用**正规秩** $h$ 的 $\Delta_h$（不是任意第 $b$ 个行列式因子）。
*等级*：**[已证-纸面]**（初等；专家 2026-11-05 §Q3 确认此半正确）。


---

### B.9 · 边界与等号结构

**B.9（a）〔原 B.9〕（必要条件 $h<q+r_1$）** 设 $\mathcal L$ 行满秩、含 $L_0\ne0$，$h=\operatorname{rank}[\mathcal L;CA;C]$、$r_1=\operatorname{rank}[C;CA]$、$s=\operatorname{rank}\mathcal L$。则 $Q_{\mathcal L}=[\lambda\mathcal L-\mathcal LA;CA;C]$ 有 $2p-r_1$ 个零左指标，非零左指标个数为 $q+r_1-h$；因此
$$(5b)\ \Longrightarrow\ h<q+r_1 .$$

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.9/](../proof/B.9/README.md)。
*专家意见（2026-11-06）*：本质假设是 $q\ge1$；$L_0\ne0$ 只是保证 $q\ge1$ 的一种方式。
*Lean 内核（2026-11-06 登记）*：**[Lean-conditional]** —— `finrank_sup_lt_of_inf_ne_bot`、`inf_bot_of_finrank_sup_eq`（子空间层）+ `MatrixBridge.rank_fromRows_lt_of_inf_ne_bot`、`inf_bot_of_rank_fromRows_eq`（字面矩阵层）；差异见 [proof/B.9/](../proof/B.9/README.md) 的 `## Lean` 一节。
*等级*：$h>q+r_1$ 半 **[已证-纸面]**；$h=q+r_1$ 半 **[已证-纸面]**（由 B.22）。$+$ **[精确验证 56/56]**、**[精确验证 698/698]**、**[精确验证 22877/22877]（等号处全部失败）**。
*等级*：**[已证-纸面]** + **[Lean]**（`TypeII.typeII_rank_mono`：$\dim J\le\dim(V\sqcup J)$；`TypeII.typeII_vacuous`：$s=q$ 与 $r_1\le h$ 之下 $\neg(s<q+r_1-h)$；`TypeII.typeII_vacuous_geometric`：维数版。**差异**：$h\ge r_1$ 与 $s=q$ 作为假设给入——前者由 `typeII_rank_mono` 提供，后者即 $\operatorname{rank}\mathcal L=q$）$+$ **[精确验证 93/93]**（$k>s$ 的违例 0；`tools/verification/failure_types.py` 的分类计数中 Type II 恒为 0）。
*等级*：**[已证-纸面]**。
*等级*：**[已证-纸面]**（1、2、3 都只是秩/核的直接计算）。


---

### B.10 · 谱障碍的定域

**B.10（a）〔原 B.10〕（谱障碍的定域）** 设 $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$，$Q_{\mathcal L}=D(\lambda)H$（$H=[\mathcal L;CA;C]$）。则
$$\lambda\notin\operatorname{spec}\Lambda\ \Longrightarrow\ \operatorname{rank}Q_{\mathcal L}(\lambda)=h .$$

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.10/](../proof/B.10/README.md)。
*等级*：**[已证-纸面]** + **[精确验证 3/3]**（候选 #1 的坏根为复根，说明"扫有理 $\lambda$"不能当判据）。
*等级*：**[已证-纸面]**（用紧合性；不依赖任何计算）。**[未做]**：把该论证写成一维情形下的显式例子以交叉核对。


---

### B.11 · Type I/II 的几何形式

**B.11（a）〔原 B.11〕（$h$ 的几何公式）** 设 $\mathcal L$ 行满秩、$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$，
$\mathcal Z=\ker[C;\mathcal L]$、$W=\operatorname{row}[C;CA]$。则
$$h=\operatorname{rank}[\mathcal L;CA;C]=\dim(\mathcal Z^{\perp}+W),$$
且 $h=q+r_1-\delta$，$\delta=\dim(\mathcal Z^{\perp}\cap W)-p\ge0$。

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.11/](../proof/B.11/README.md)。
*专家意见（2026-11-06）*：Type I 的二分只是**数值**分类，不覆盖子空间相对位置的全部几何型。
*等级*：**[已证-纸面]** + **[Lean]**（`TypeIGeom.B11_dim`：$\dim((C\sqcup R)\sqcup W)+(\dim((C\sqcup R)\sqcap W)-\dim C)=\dim R+\dim W$；**差异**：$\delta$ 写成维数差，非负性由 $C\le(C\sqcup R)\sqcap W$ 保证）$+$ **[精确验证 240/240]**。
*等级*：**[已证-纸面]** + **[Lean]**（`TypeIGeom.mkQ_map_inf_eq`：$\pi((C\sqcup R)\sqcap W)=\pi R\sqcap\pi W$；`TypeIGeom.typeI_dim`：维数形式；`TypeIGeom.typeI_geometric`：$\dim((C\sqcup R)\sqcup W)+\dim(\pi R\sqcap\pi W)=\dim R+\dim W$。**差异**：写成等式而非"$\iff$"，"$h\ge q+r_1\iff\pi R\sqcap\pi W=0$"由等式直接读出）$+$ **[精确验证 21/21]**（恒等式 $h=q+r_1-\dim(\pi(R)\cap\pi(W))$ 无违例）。
*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`Dims.b11c_modular`、`Dims.b11c_add`） + **[精确验证 35/35]**（公式）$+$ **[精确验证 54/54]**（不等式与等号判据
*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`Logic.b11d_css` 逻辑骨架、`Logic.typeI_kills` 算术内核）（初等逻辑 + B.9b + B.12）。


---

### B.12 · 谱条件的可观性归约

**B.12（谱条件的可观性归约；专家 2026-11-04 §3 给出，本项目独立核验）** 设 $(5a)$ 成立，取
$$\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA\qquad(\Lambda\in\mathbb C^{q\times q}),$$
令 $V=\ker[C;CA]$、$U:=\mathcal L(V)\subseteq\mathbb C^q$。则
$$(5b)\iff U\ \text{不含}\ \Lambda\ \text{的非零特征向量}
\iff (E,\Lambda)\ \text{可观测}\ (\ker E=U)
\iff \operatorname{rank}\bigl[E;E\Lambda;\dots;E\Lambda^{q-1}\bigr]=q .$$

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.12/](../proof/B.12/README.md)。
*Lean 内核（2026-11-06 登记）*：**[Lean-conditional]** —— `pow_finrank_eq_neg_sum`、`observable_iff_krylov`、`observable_iff_rank_krylov`（Cayley–Hamilton）；差异见 [proof/B.12/](../proof/B.12/README.md) 的 `## Lean` 一节。
*等级*：**[已证-纸面]** + **[精确验证 44/44]**（`tools/verification/observability_test.py`：


---

### B.13 · 计数判据族

**B.13（a）〔原 B.13〕（incidence variety 的维数与"整族不可行"的覆盖判据；专家 2026-11-04 §5 的建议）**
记 $V=\ker[C;CA]$、$K=\ker[C;L_0]$，并设 $h=n$（此时 $(5a)$ 对**每个** $\mathcal Z\subseteq K$ 自动成立，见 3.4）。
考虑 incidence variety
$$\mathfrak I=\{([x],\lambda,[z]):\ x\in V\setminus0,\ L_0x\ne0,\ z=(\lambda I-A)x\ne0,\ z\in K\}\subseteq\mathbb P(V)\times\mathbb P^1\times\mathbb P(K),$$
及其到 $\mathbb P(K)$ 的投影像 $S$（"坏点直线"全体）。

*命题*：
1. **$\lambda$ 与 $z$ 被 $x$ 决定**：$x\in V$ 时 $C(\lambda x-Ax)=0$ 自动成立，而
   $L_0(\lambda x-Ax)=\lambda L_0x-L_0Ax$，故 $z\in K\iff\lambda L_0x=L_0Ax$。
   * $r=1$：$\lambda=L_0Ax/L_0x$ 唯一确定；* $r\ge2$：仅当 $L_0Ax\in\operatorname{span}\{L_0x\}$（比例性）时有解，
   且解唯一。故 $\mathfrak I$ 是 $\mathbb P(V)$ 上某个**开子集与比例性轨迹之交**上的图，特别地
   $$\dim\mathfrak I\le\dim\mathbb P(V)=n-r_1-1,\qquad \dim S\le\min(n-r_1-1,\ n-p-r-1).$$
2. **覆盖判据**：设 $d=n-p-q$。若 $\dim S\ge q-r$，则 $S$ 与 $\mathbb P(K)$ 的**每个** $\mathbb P^{d-1}$ 相交
   （射影维数定理：$\mathbb P^{d-1}$ 与 $s$ 维子簇在 $\mathbb P^{N}$ 中必交当 $s+(d-1)\ge N$，
   $N=\dim\mathbb P(K)=n-p-r-1$，代入得 $s\ge q-r$）。于是**每个** $\mathcal Z\in\mathrm{Gr}(d,K)$ 都含一条坏点直线，
   $\mathcal Z$ 上必有掉秩 $\lambda$ ⟹ 该阶**整族不可行**。（这正是"遮蔽/incidence"判据，见 §4.6。）
3. **对"$r_1=p+r$"的更正**：$\Phi$ 的**支配性**只要求 $n-r_1-1\ge n-p-r-1\iff r_1\le p+r$，
   **等号不是必要的**；且 Type III 的**逐候选**出现并不要求等号——实测 $n=8,p=3,r=2,q_0=3$ 的实例
   （$r_1=6>p+r=5$，$\dim\mathbb P(V)=1<\dim\mathbb P(K)=2$）**也有** Type III 候选（30 个候选里 1 个）。
   真正需要的是上面的**余维条件** $\dim S\ge q-r$；$r_1=p+r$ 只是使 $\mathbb P(V)$ 与 $\mathbb P(K)$ 等维的特例
   （C4 与另一 $n=7,p=2,r=2$ 实例均属此列）。

*等级*：**第 1 条 [已证-纸面]；第 2 条（覆盖判据）降级为 [条件性]** —— 专家 2026-11-04 §2 指出两个未解决的点：

1. **像未必射影闭**：$\mathfrak I$ 的定义排除了 $L_0x=0$ 与 $(\lambda I-A)x=0$，故其像 $S$ 只是**可构造集**；
   射影维数定理只对**闭**子簇成立。取闭包 $\overline S$ 不修复论证：某个 $\mathbb P^{d-1}$ 可能只与
   $\overline S\setminus S$ 相交，而边界点不给出真正的有限 $\lambda$ 障碍。修法：或证像闭，或证边界点也对应真实障碍。
2. **被排除的两个轨迹不能直接丢掉**：$u\ne0$ 而 $z=0$（此时 $x$ 不在 $K$ 里、对任何 $\mathcal Z$ 都是障碍，
   但没有射影直线 $[z]$）；以及 $u=0$（此时 $\lambda$ 不再被确定，若还有 $v=0$ 则对一切 $\lambda$ 成立，
   是一族 $z$）。二者必须或加假设排除、或作为额外的 incidence 分量计入维数。

**因此**：$P=\{x\in V:v\wedge u=0\}$、$\varepsilon=\dim V-\dim P$、$\dim S\le n-r_1-1-\varepsilon$ 作为
**代数观察**保留；覆盖判据与"整族不可行"的推论标为**条件性**，在主结果中不出现（专家 §Q6 同意见）。
$+$ **[精确验证]**（C4 上 $\dim S=1=q-r$；$n=8,p=3,r=2,q_0=3$ 实例上 $r_1=6$、$\dim\mathbb P(V)=1$、
30 个候选中 1 个 Type III）——这些是**实例核对**，不修复上述两个一般性问题。

**B.13（b）〔原 B.13b〕（比例性轨迹的维数与整族不可行的**精确余维条件**；关于 $\varepsilon$ 的结构按专家 2026-11-04 §Q3 重述）**
记 $U_0=L_0|_V$、$U_1=L_0A|_V$，$\Phi(x)=\begin{pmatrix}U_0x\\U_1x\end{pmatrix}$（$2\times r$ 的线性形式矩阵），则
$$P=\{x\in V:\operatorname{rank}\Phi(x)\le1\},$$
即 $P$ 是**行列式簇 $\{\operatorname{rank}\le1\}\subseteq\mathbb C^{2r}$ 在 $x\mapsto(U_0x,U_1x)$ 下的原像**——
一个**线性截面**。故 $\varepsilon$ 是"比例性行列式轨迹"的余维，可用 Gröbner 基 / Hilbert 多项式**实际计算**
（在 $V$ 的坐标环里计算 $2\times2$ 子式的理想之维数），但**不能**只从 $V$ 上某个算子的 Kronecker 数据读出：
$V=\ker[C;CA]$ 未必 $A$-不变，且该不变量依赖 $U_0,U_1$ 的**联合位置**（专家 §Q3）。
命名建议：称 $\varepsilon$ 为"比例性行列式轨迹的余维"，不用未证实的标准名。

记 $u=L_0x$、$v=L_0Ax$，比例性条件是
$v\wedge u=0$，即**二次形式族**
$$q_{ij}(x):=v_iu_j-v_ju_i=0\quad(i<j)$$
的公共零点集 $P\subseteq V$（仿射锥）。令 $\varepsilon:=\dim V-\dim P\ge0$（比例性条件削减的维数；$r=1$ 时无此条件，$\varepsilon=0$）。
则

$$\dim S\le\dim\mathbb P(P)=\dim P-1=n-r_1-1-\varepsilon,$$
故 B.13 的覆盖判据（$\dim S\ge q-r$，且 $h=n$）成立的必要条件是
$$\boxed{\ q-r+\varepsilon\ \le\ n-r_1-1\ }$$

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.13/](../proof/B.13/README.md)。

*B.13d（Theorem C，专家第六轮 §4）*：固定候选的谱障碍是射影集 $\mathcal E_K=\{[w]\in\mathbb P(W_K):\Phi_K(w)\in\mathbb Cw\}$（齐次二次方程，故为射影代数集），$(5b)\iff\mathcal E_K=\varnothing$。投影 $\pi:\mathbb P(K)\setminus\mathbb P(D)\to\mathbb P(W_K)$、$[v]\mapsto[\mathcal Lv]$ 的**纤维维数 $=d=k-\omega$**（$D=K\cap\ker\mathcal L$）。因此旧覆盖估计**不能**把 $k$ 换成 $\omega$，须重推（族内 $\omega$ 可能跳变，需分层）。
**[部分修复]** —— 入射构造已射影化；**B.13a 已完整证明**：齐次入射簇 $\mathfrak I$ 闭（引理 1）、$\mathcal B$ 外纤维 $\le0$ 维（引理 2）、$\mathcal B$ 上纤维 $=\mathbb P(K)$ 维数 $k-1$（引理 3），由此得 $\dim\mathfrak I\le\max\{v,\ \dim\mathcal B+k-1\}$，以及"$A$ 在 $V$ 中无特征向量 $\Rightarrow\dim\mathfrak I\le v$"。**仍缺**：把维数估计转成"整族不可行覆盖判据"的那一步（投影 $\mathfrak I\to\mathbb P(K)$ 的维数比较）。详见卷宗。*等级*：**[已证-纸面]** $+$ **[精确验证]**（四实例的比例性与维数见上表；C4 上已有 $\dim S=q-r=1$ 的独立核验）。
*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`Criterion.b13c_factor`：$F\circ(cI-A)=(cI-\Lambda)\circ F$，即上式"$\mathcal L(\lambda x-Ax)=(\lambda I-\Lambda)\mathcal Lx$"的抽象版）$+$ **[精确验证]**（6 个显式证书）。
*等级*：**[已证-纸面]**（三行推导）$+$ **[精确验证]**：C4 的 $q_0=3$ 阶上对 6 个图卡/参数显式构造 $(x,\lambda_0)$
*等级*：**[已证-纸面]** $+$ **[精确验证 5983/5983]**（`tools/verification/epsilon_zero_characterization.py`；
*等级*：**[已证-纸面]**（三行）+ **[精确验证]**：在新实例的单参数族 $A_{00}=t$ 上，
*等级*：**[已证-纸面]** $+$ **[精确验证 2676/2676]**（`tools/verification/scalar_gadget.py`：$n=3,p=r=1,q=1$、


---

### B.14 · 投影铅笔满列秩类

**B.14（一个可判的多项式时间可解类：投影铅笔满列秩）** 设 $B_V$ 为 $V=\ker[C;CA]$ 的基，$P_K$ 为满行秩、
$\ker P_K=K$ 的矩阵（$K=\ker[C;L_0]$）。若
$$\operatorname{rank}\bigl(P_K(\lambda I-A)B_V\bigr)=\dim V\qquad\forall\lambda\in\mathbb C, \tag{T*}$$
则该实例**在每一阶都谱可行**：任何 $\mathcal Z\subseteq K$、任何 $x\in V$，若 $(\lambda I-A)x\in\mathcal Z\subseteq K$
则 $P_K(\lambda I-A)x=0$，由 (T*) 得 $x=0$，与 B.13c 要求的 $x\in V\setminus\mathcal Z$ 矛盾。$\square$

*判据实现*：$P_K(\lambda I-A)B_V$ 是 $\lambda$ 的一次多项式矩阵；对每个 $\lambda$ 满列秩 $\iff$ 其
$\dim V$ 阶极大子式的 gcd 为**非零常数**（且至少一个子式非零）。

*等级*：**[已证-纸面]** $+$ **[精确验证]**（`tools/verification/t_star_coverage.py`：595 个随机可观测实例中
**56** 个满足 (T*)（约 $9.4\%$），且这 56 个在 $q_0$ 阶**全部**找到显式可行见证；其余 539 个不满足）。
*注（专家 2026-11-04 §1.4 的提醒）*：(T*) 只用于**充分性**。其**否定**并**不**蕴含失败：
失败要求同时有 $P_{\mathcal Z}(\lambda I-A)B_Vu=0$ 且 $P_{\mathcal Z}B_Vu\ne0$；
仅"压缩不满列秩"时，$u$ 可能落在 $\ker(P_{\mathcal Z}B_V)$ 里，那**不是**谱障碍。
*注*：(T*) 与候选 $\mathcal L$ 无关，故它给出的是**实例级**可解性证书；它**强于**单-$\lambda$ 证书所需
（(T*) 成立时必有 $(\lambda I-A)V\cap K=0$，故单-$\lambda$ 证书**不可能**成立——两者互补）。
这是专家 2026-11-04 §Q5 建议的"可验证可解类"的第一个实例。

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.14/](../proof/B.14/README.md)。


---

### B.15 · 避免性引理

**B.15（阶差无界：$k$ 个同型副本的直和把阶差乘以 $k$）** 设单副本 $(A_1,C_1,L_{0,1})$ 满足
$$V_1\cap K_1=0\quad\text{且}\quad\exists\lambda_0:\ (\lambda_0I-A_1)V_1=K_1\qquad(\dim V_1=\dim K_1),$$
并设它在某阶 $q_1$ 有可行的增广 $\mathcal L_1$（如 $q_1=q_{\min}$），且 $d_1=n_1-p_1-q_1=0$。
取 $k$ 重直和 $(A,C,L_0)=(A_1,C_1,L_{0,1})^{\oplus k}$（于是 $n=kn_1$、$p=kp_1$）。则

1. $V=V_1^{\oplus k}$、$K=K_1^{\oplus k}$、$V\cap K=0$，且 $(\lambda_0I-A)V=K$（**同一个** $\lambda_0$）；
2. 由 B.13e，**每个**阶 $q$ 只要 $d=n-p-q\ge1$ 就整族不可行（无例外，因 $V\cap K=0$）；
3. 在 $q=kq_1$（即 $d=0$）处，块对角增广 $\mathcal L=\mathcal L_1^{\oplus k}$ 满足 $(5a)$ 与 $(5b)$
   （两者都按块相加）。

于是
$$\boxed{\ q_{\min}\big((A_1,C_1,L_{0,1})^{\oplus k}\big)=k\,q_{\min}(A_1,C_1,L_{0,1}),\qquad
\text{阶差}=k\cdot(\text{单副本阶差})\ }$$

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.15/](../proof/B.15/README.md)。
*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`LemmaA.exists_witness_not_mem` / `_not_mem'`：若 $V\cap K=0$、


---

### B.17 · 永久核与商铅笔

**B.17（永久核与商铅笔判据；专家 2026-11-04 §2.1/§5 给出，本项目核验）** 设 $\mathcal L$ 满足 $(5a)$、
$\mathcal Z=\ker[C;\mathcal L]$、$S=V\cap\mathcal Z$、$N_{\mathcal Z}(\lambda)=T_{\mathcal Z}-\lambda J_{\mathcal Z}$。则

1. **永久核**：$S\subseteq\ker N_{\mathcal Z}(\lambda)$ 对**一切** $\lambda$ 成立；
2. **商判据**：
$$(5b)\ \text{成立}\iff\ker N_{\mathcal Z}(\lambda)=S\ \ \forall\lambda
\iff \overline N_{\mathcal Z}(\lambda):V/S\to X/\mathcal Z\ \text{对一切}\ \lambda\ \text{单射};$$
3. **可计算形式**：取 $V'$ 为 $S$ 在 $V$ 中的补（$\dim\rho=\dim V-s$）、$P_{\mathcal Z}$ 满足 $\ker P_{\mathcal Z}=\mathcal Z$，则
$\overline N_{\mathcal Z}(\lambda)$ 的矩阵为 $P_{\mathcal Z}(A-\lambda I)V'$（$(n-d)\times\rho$），它对**一切有限** $\lambda$ 单射
$\iff$ 其 $\rho$ 阶极大子式的 gcd 为**非零常数**（$\rho=0$ 时条件空、自动可行）。

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.17/](../proof/B.17/README.md)。
*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`Criterion.permanent_kernel` 永久核、`Criterion.ker_eq_iff` 判据的核形式；差在"诱导映射 $W/S\to W$ 单射"的商空间表述）$+$ **[精确验证]**（**1513/1513** 个随机可容许 $(\mathcal Z,q)$ 样本上"商铅笔单射"与 B.12 可观性判据完全一致，`tools/verification/quotient_pencil.py`）。


---

### B.18 · $p=r=1$ 的结构

**B.18（a）〔原 B.18〕（$p=r=1$ 的结构与降维）** 设 $p=r=1$（$C=c^{\mathsf T}$、$L_0=\ell^{\mathsf T}$）且 $(c,A)$ 可观测。则

1. $r_1=\operatorname{rank}[c;cA]=2$（若 $=1$，则 $cA=\alpha c$，故 $cA^k=\alpha^kc$，观测性矩阵秩为 $1$，矛盾），
   $\dim V=\dim K=n-2$，$\dim(V\cap K)=\dim\ker\{c,cA,\ell\}\ge n-3$；
2. $s_0=\dim(\operatorname{row}[c;\ell]+W)\in\{2,3\}$，且 $s_0=3\iff\ell\notin\operatorname{span}\{c,cA\}$；
3. 因 $r_1+r=3$：若 $\ell\in\operatorname{span}\{c,cA\}$ 则 $s_0=2<3$，**该实例任何阶都无 Type I**（B.11c）；
4. **降维**：若 $\mathcal Z\subseteq V\cap K$（当 $d=n-1-q\le\dim(V\cap K)$，即 $q\ge2$ 时可行），则 $S=\mathcal Z$，
$$\rho=\dim(V/S)=\dim V-d=q-1,$$
故商铅笔 $\overline N_{\mathcal Z}$ 的尺寸为 $(q+1)\times(q-1)$——形状只由 $q$ 决定；$q=2$ 时为 $3\times1$（单列）。

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.18/](../proof/B.18/README.md)。
*Lean 内核（2026-11-06 登记）*：**[Lean-conditional]** —— `finrank_range_prod_le`（$r_1\le2p$）；差异见 [proof/B.18/](../proof/B.18/README.md) 的 `## Lean` 一节。
*等级*：**[已证-纸面]** $+$ **[精确验证]**（第 4 条的 $\rho=q-1$ 在 **714/714** 个 $(n,q,\mathcal Z\subseteq V\cap K)$ 样本上成立；
*等级*：**[已证-纸面]** $+$ **[精确验证 589/589]**（$n=4..8$ 各约 120 个实例，$(5a)$ 与 $(5b)$ 全部成立）。
*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`Dims.b18c_annihilate`：第 1 条）（1、2、3 的结构部分）$+$ **[精确验证]**（在一个 $n=6$ 实例上 12 个随机
*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`PsiImage.recX_natDegree_and_ne` 等三条） $+$ **[精确验证 300/300]**（伴矩阵实例 $n=4,5,6$ 上，公式刻画与精确 gcd 判据完全一致；
*等级*：三条均 **[已证-纸面]**；第 3 条的**内核**已 **[Lean-conditional]**（`PsiImage.recX_natDegree_and_ne`、


---

### B.22 · 等号障碍：$h=q+r_1$ 时 $(5b)$ 必失败

**B.22（等号障碍：$h=q+r_1$ 时 $(5b)$ 必失败；专家 2026-11-05 给出证明）** 设 $\mathcal L$ 满足 $(5a)$、
$\operatorname{rank}\mathcal L=q\ge1$、$h=\operatorname{rank}[\mathcal L;CA;C]=q+r_1$，其中 $r_1=\operatorname{rank}[CA;C]$。则
$$\exists\lambda_0\in\mathbb C:\ \operatorname{rank}Q_{\mathcal L}(\lambda_0)<h,$$
故 $(5b)$ 失败。更强地：$Q_{\mathcal L}$ 严格等价于 $\operatorname{diag}(\lambda I_q-K_1,\ I_{r_1})$，于是
$$d_{\rm fin}=q,\qquad d_\infty=r_1 .$$

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.22/](../proof/B.22/README.md)。
*等级*：**[已证-纸面]**（专家证明）$+$ **[Lean-conditional]**（`B22.det_blockIdentity` 方块行列式、`B22.exists_root_of_pos_natDegree` 正次数有根；差在 $H_0$ 满行秩 ⟹ 秩不变、$K$ 存在性、秩化归三步）。


---

### B.23 · 统一分块因子化

**B.23（谱侧的统一因子化：$Q_{\mathcal L}(\lambda)=P(\lambda)H_0$）** 设 $\mathcal L$ 满足 $(5a)$、$\operatorname{rank}\mathcal L=q$；
取 $B\in\mathbb C^{r_1\times n}$ 满行秩且 $\operatorname{row}B=\operatorname{row}[CA;C]$，令 $H_0=[\mathcal L;B]$。由 $(5a)$ 的
$\operatorname{row}(\mathcal LA)\subseteq\operatorname{row}H_0$ 得 $\mathcal LA=KH_0$，记 $K=[K_1\ K_2]$（$K_1$ 为 $q\times q$、$K_2$ 为 $q\times r_1$）。则
$$Q_{\mathcal L}(\lambda)=\begin{bmatrix}\lambda\mathcal L-\mathcal LA\\ B\end{bmatrix}
=P(\lambda)\,H_0,\qquad P(\lambda)=\begin{bmatrix}\lambda I_q-K_1&-K_2\\ 0&I_{r_1}\end{bmatrix},$$
且对每个 $\lambda\in\mathbb C$：
$$\operatorname{rank}Q_{\mathcal L}(\lambda)=\operatorname{rank}H_0-\dim\bigl(\ker P(\lambda)\cap\operatorname{im}H_0\bigr),\qquad
\det P(\lambda)=\det(\lambda I_q-K_1).$$
于是
$$(5b)\ \text{失败}\iff\exists\lambda:\ \ker P(\lambda)\cap\operatorname{im}H_0\ne0,$$
且这样的 $\lambda$ **必是 $K_1$ 的特征值**（因 $\det P(\lambda)=\det(\lambda I_q-K_1)$）。

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.23/](../proof/B.23/README.md)。
*专家意见（2026-11-06）*：$\det P=\det(\lambda I_q-K_1)$ 只由块三角性得到；不需要 $K_1$ 可对角化。
*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`WorkA.finrank_range_comp` 秩公式、`B22.det_blockIdentity` 方块行列式、`B22.exists_root_of_pos_natDegree`；差在矩阵实例化与 $\lambda$-依赖运算） $+$ **[精确验证 8128/8128]**（因子化、秩一致、行列式一致；


---

### B.24 · 内蕴形式 $\Phi$

**B.24（内蕴形式：偏算子 $\Phi$ 的特征向量；专家 2026-11-05 §2.1 的改进）** 设 $\mathcal L$ 满足 $(5a)$、
$\operatorname{rank}\mathcal L=q$，$W:=\mathcal LV\subseteq\mathbb C^q$。定义**偏算子**
$$\Phi:W\longrightarrow\mathbb C^q,\qquad \Phi(\mathcal Lx):=\mathcal LAx\quad(x\in V).$$
则

1. **$\Phi$ 良定义**：若 $\mathcal Lx_1=\mathcal Lx_2$（$x_i\in V$），则 $s=x_1-x_2\in S=V\cap\ker\mathcal L$；由 $(5a)$ 的因子化
   $\mathcal LA=K_1\mathcal L+K_2B$ 得 $\mathcal LAs=K_1\mathcal Ls+K_2Bs=0$，故 $\mathcal LAx_1=\mathcal LAx_2$。
2. **$\Phi=K_1|_W$**（对任何因子化）：$K_1$ 的选取只影响它在 $W$ 外的延拓，**在 $W$ 上的限制唯一**。
3. **判据**：
$$\boxed{(5b)\ \text{失败}\iff\exists\,0\ne u\in W:\ \Phi(u)\in\operatorname{span}\{u\}}$$
4. **维数**：$\dim W=\dim V-s=(n-r_1)-(n-h)=h-r_1$；Class I（$r_1=2$）时 $\dim W=h-2$。
5. **推论（谱维数上界）**：若 $(5b)$ 成立，则
   $$\boxed{\dim W\le q-1.}$$
   *证明*：$\Phi:W\to\mathbb C^q$ 是方阵（在 $W$ 上），在 $\mathbb C$ 上有特征值 $\lambda_0$，
   $E_{\lambda_0}(\Phi)\ne0$；$(5b)$ 等价于 $W\cap E_{\lambda_0}(\Phi)=0$，故 $\dim W\le q-1$。$\square$

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.24/](../proof/B.24/README.md)。
*内蕴谱刻画（B.23+B.24）*：$(5b)$ 失败 $\iff$ $\Phi=K_1|_W$ 在 $W$ 上有特征向量；与"商铅笔 $\overline N_{\mathcal Z}(\lambda)$ 逐点单射"是同一障碍的两种写法。详见卷宗。
*专家意见（2026-11-06）*：$\Phi$ 的良定义只需 $(5a)$，**不需要** $L$ 行满秩。
*等级*：**[已证-纸面]** $+$ **[精确验证 3453/3453]**（把 $\Phi$ 具体算成矩形铅笔 $D-\lambda U$，其极大子式 gcd 有正次数


---

### B.25 · 矩形铅笔与 gcd 判据

**B.25（Workstream A：矩形铅笔 $D-\lambda U$ 与 gcd 判据）** 设 $\mathcal L$ 可容许、$W=\mathcal LV\subseteq\mathbb C^q$、$\Phi$ 如 B.24。
取 $U\in\mathbb C^{q\times k}$ 列满秩、$\operatorname{col}U=W$（$k=\dim W=h-r_1$），并令 $D\in\mathbb C^{q\times k}$ 的第 $i$ 列为 $\Phi(u_i)$
（$u_i$ 为 $U$ 的第 $i$ 列），则 $\Phi(Ua)=Da$。于是

1. **矩形广义特征值判据**：
$$(5b)\ \text{失败}\iff\exists\lambda\in\mathbb C:\ \operatorname{rank}(D-\lambda U)<k ;$$
2. **gcd 判据**：$\iff$ 矩形铅笔 $D-\lambda U$（$q\times k$，法秩 $k$）的 $k$ 阶极大子式的 gcd 是**正次数**多项式
   （等价地：它在 $\mathbb C[\lambda]$ 上的 Smith 形有非常数不变因子，即 B.8a 的 $d_{\rm fin}>0$）；
3. **次数界**：极大子式是次数 $\le k$ 的多项式，故失败判据是"有限个次数 $\le k$ 的多项式有公根"。

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.25/](../proof/B.25/README.md)。
*Lean 内核（2026-11-06 登记）*：**[Lean-conditional]** —— `gcd_eval_eq_zero_of_common_root`、`gcd_is_const_of_no_common_root`、`no_common_root_iff_gcd_const`；差异见 [proof/B.25/](../proof/B.25/README.md) 的 `## Lean` 一节。
*等级*：**[已证-纸面]** $+$ **[精确验证 3453/3453]**（`tools/verification/partial_operator.py`：gcd 有正次数 $\iff$ B.12 判据失败）。


---

### B.28 · 子空间归约与分层参数

**B.28（a）〔原 B.26〕（Class I：$\mathcal V=\mathcal Z^\perp$ 决定一切）**
*约定*：$\mathcal Z^\perp$ 指**代数零化子**（$\{y: y^{\mathsf T}z=0\ \forall z\in\mathcal Z\}$），不是 Hermite 正交补；行空间恒等式在该约定下成立（专家 2026-11-05 §1.1）。
 设 $p=r=1$、$\mathcal L$ 可容许、$\mathcal Z=\ker[C;\mathcal L]$、$\mathcal V:=\mathcal Z^\perp$。
则

1. **$\mathcal V=\operatorname{row}[\mathcal L;c]$**（故 $\dim\mathcal V=q+1$，且 $\mathcal V$ **只依赖 $\mathcal Z$**）；
2. **$h=\dim(\mathcal V+\langle cA\rangle)$**（同理只依赖 $\mathcal Z$），故 $h\in\{q+1,q+2\}$，且
   $$h=q+2\iff cA\notin\mathcal V ;$$
3. **$(5a)\iff \mathcal VA\subseteq\mathcal V+\langle cA\rangle$**；
4. 特别地：若 $cA\in\mathcal V$（即 $h=q+1$），则 $(5a)\iff\mathcal V$ 是 $A$-不变子空间。

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.28/](../proof/B.28/README.md)。
*Lean 内核（2026-11-06 登记）*：**[Lean-conditional]** —— `map_sup_le_iff`（分裂等价，即分部 (a)）；差异见 [proof/B.28/](../proof/B.28/README.md) 的 `## Lean` 一节。
*等级*：**[已证-纸面]** $+$ **[精确验证 2954/2954]**（`tools/verification/b26_class_I_only_Z.py`：1、2、3 与情形判别全部成立）。
*等级*：**[已证-纸面]**（专家给出，本项目复核；Class I 的 $p=1$ 特例即 B.26，已 2954/2954 精确验证）。
*等级*：**[已证-纸面]**（$h=q+p+\delta$ 的推导）+ **[观察]**（"未决=中间层"是问题定位，不是定理）。
*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`B33.dim_quotient` 商维数公式、`B33.dim_arith` 算术）。


---

### B.31 · 可行性的必要条件：$\delta$ 落在中间层

**B.31（可行性的必要条件：$\delta$ 必须落在中间层）** 设 $(p,r)$ 任意、$\mathcal L$ 可容许、$q+p<n$（即低于终阶）。则
$$\boxed{(5b)\ \text{成立}\ \Longrightarrow\ 1\le\delta(\mathcal V)<r_1-p ,}$$
其中 $\delta(\mathcal V)=\dim\bigl(\operatorname{row}(CA)/(\operatorname{row}(CA)\cap\mathcal V)\bigr)$、$\mathcal V=\mathcal Z^\perp$。

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.31/](../proof/B.31/README.md)。
*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`B31.logic` / `B31.necessary` 的逻辑骨架（两极端层不可行 ⟹ 可行时 $1\le\delta<\rho$））（必要条件）+ **[精确验证]**（锐利性证书）。


---

### B.37 · 谱可行性的统一刻画（统一定理）

**B.37（四等价）** 设 $\mathcal L$ 满足 $(5a)$，$V=\operatorname{row}[\mathcal L;C]$、$S=V\cap\mathcal Z$、$W=\mathcal LV$、$\rho=\dim W$；
设 $\Phi:W\to\mathbb C^q$ 为偏映射（B.24）、$\iota:W\hookrightarrow\mathbb C^q$ 为包含，
$P_\Phi(\lambda)=\lambda\iota-\Phi$、$\overline N_{\mathcal Z}(\lambda):V/S\to X/\mathcal Z$。则以下四条等价：

1. $(5b)$ 成立；
2. $\overline N_{\mathcal Z}(\lambda)$ 对每个有限 $\lambda$ 单射；
3. $\nexists\,0\ne w\in W$ 与 $\lambda$ 使 $\Phi(w)=\lambda w$（无部分特征向量）；
4. $P_\Phi$ 的全部 $\rho\times\rho$ 极大子式的 $\gcd$ 是非零常数。

**核结构**（B.17）：$\bigcap_\lambda\ker\overline N_{\mathcal Z}(\lambda)=S$、$\ker_{\mathbb C[\lambda]}\overline N_{\mathcal Z}(\lambda)=S\otimes\mathbb C[\lambda]$；
（B.6）$(5a)$ 下 $(5b)\iff d_{\rm fin}=0\iff\sum_j\varepsilon_j=\operatorname{rank}\mathcal L$。

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.37/](../proof/B.37/README.md)。

*Task 1 的部分结果（等号情形）*：块因子化 $Q=PH$（$P$ 方阵、$H$ 行满秩）下，Cauchy–Binet 给出 $\Delta_Q=\det P$（相差非零常数）；故 $h=q+r_1$ 时$\Delta_{Q_{\mathcal L}}=\det(\lambda I_q-K_1)$——即 B.8 的 $\Delta_h$。一般情形待证。

*参数化结构（Task 2 第一步）*：$(5a)$ 的等价形式 $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$ 关于 $R$ 与 $(\Lambda,G_0,G_1)$ 分别线性；固定 $R$ 时是仿射线性方程组，故 $\Lambda$、$\Phi_R$ 是 $R$ 的有理函数，可容许集是**构造集**（秩条件）。这与 G.1 的 $\exists\mathbb R$ 编码一致，但构造性不等于可判定性。**等级**：[已证]（组装：B.1、B.17、B.24、B.8 均已复核；两处识别 (A)(B) 为本轮新写）。

### B.32 · 终端唯一区：$r_1\le p+1\Rightarrow q_{\min}=n-p$

**B.32（a）〔原 B.27〕（Class I 的 $q_{\min}=n-1$ —— 定理，不再是猜想）** 设 $p=r=1$（$C=c^{\mathsf T}$、$L_0=\ell^{\mathsf T}$）、
$(c,A)$ **可观测**、$\operatorname{rank}[c;\ell]=2$（保证终阶可行；**不需要** $(\ell,A)$ 可观测，专家 2026-11-05 §2）、$\mathcal L$ 可容许（$(5a)$、$\operatorname{rank}[C;\mathcal L]=1+q$、含 $L_0$）。若 $1\le q\le n-2$，则
$$(5b)\ \text{失败};\qquad\text{而 } q=n-1 \text{ 可行（B.18b）}\ \Longrightarrow\ \boxed{q_{\min}=n-1 .}$$

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/B.32/](../proof/B.32/README.md)。
*等级*：**[已证-纸面]** $+$ **[Lean-conditional]**（`B27.krylov_le`、`B27.eq_top_of_krylov` 给出情形 B 的归纳与 $\mathcal V=\top$；`B27.no_caseB` 给维数矛盾；情形 A 由 `B22` 的 `exists_root_of_pos_natDegree`；差在行空间实例化与"$(5a)\Rightarrow$ 右乘 $A$ 封闭"）$+$ **[精确验证 2454/2454]**


---

### A.1 · 维数分解与下界

**A.1（a）〔原 A.0〕（$(5a)$ 的商形式——**再次校正**）** 记 $\mathcal J=\operatorname{row}[C;CA]$、$U=\pi(\mathcal V)$、$B=\pi(\mathcal J A)$。
则
$$(5a)\iff \pi(\mathcal V A)\subseteq\pi(\mathcal V).$$

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/A.1/](../proof/A.1/README.md)。

*下界的联合剖面改进*：$q_{\min}=\min_{(\rho,c)\in\mathfrak P}(\rho+c)$，且$q_{\min}\ge\min_\rho\{\rho+c_{\min}(\rho)\}$（$c_{\min}(\rho)=\min\{c:(\rho,c)\in\mathfrak P_{\rm spec}\}$)；由 F.1 可再加 $\rho\le r_*=\min_\lambda r(\lambda)$。加法界仍成立但可能不紧——当"$\rho$ 最小"与"$c$ 最小"不可同时达到时严格弱于剖面界。*专家意见（2026-11-06）*：把"商等价"（不需 $\mathcal L$ 行满秩或含 $L_0$）与"下界可达性"分开陈述；$c\ge\max(c_0,1)$ 的**同时可达**不作为本命题的一部分。
*等级*：**[已证-纸面]** + **[Lean]**（`A0Row.five_a_row_iff`：$\operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C]\iff\operatorname{row}(\mathcal LA)\le\operatorname{row}[\mathcal L;CA;C]$，即本条的第一步；`A0Row.rank_eq_of_rowSpace_le`：包含 $\Rightarrow$ 秩等式。**差异**：不含再往后的商形式 $\pi(\mathcal V A)\subseteq\pi(\mathcal V)$）。
**等级**：定义性 $+$ **[Lean]**（`A3sem.finrank_inter_add_finrank_map_mkQ`：$\dim(T\sqcap B)+\dim(T/B)=\dim T$）。
**等级**：[已证]（**完整证明**：[proof/lower_bound/theorem.md](../proof/lower_bound/theorem.md) §3）$+$ **[Lean]**
**等级**：[已证] $+$ **[Lean]**（维数部分：
*等级*：**[引用]**（arXiv:2609.33615, §II–III：$q_0=\sum_j\eta_j$ 是 $(A)$ 下的最小维数；本项目复核了它的算法与例子）+ **[精确验证 20/20]**（所有见证 $q_{\text{wit}}\ge q_0$；其中 **6/20 个实例 $q_0$ 比 A.3 更紧**）。

---


---

### C.1 · 特殊族的精确值

**C.1（$S=\mathcal J$ 闭包族）** 若 $\operatorname{row}(L_0)=\mathcal J$ 且 $\langle\mathcal J\rangle_A=\mathbb C^n$，则唯一可行解是 $\mathbb C^n$，$q_{\min}=n$。

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/C.1/](../proof/C.1/README.md)。
**等级**：[已证] $+$ **[Lean]**（`C1Closure.c1_of_closure_top`：$A$-不变闭包 $=\top$ ⟹ $V=\top$；`c1_finrank` 给 $q_{\min}=n$；闭包用"所有含 $J$ 的 $A$-不变子空间的交"定义）。

---


---

### D.1 · $P$ 的多项式可解性

**D.1（a）〔原 D.1〕（下界）** $P(A,B,S)\ge\dim S+\dim\frac{AS+S+B}{S+B}$。

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/D.1/](../proof/D.1/README.md)。
*递归 $({\le})$ 的显式构造*：$\gamma:C\'\to M$（$\widehat\pi\Phi(\gamma c)=c$）、$\beta:U\'\to C\'$（$U\'.\mathrm{mkQ}(\beta u)=U\'.\mathrm{mkQ}(\widehat\pi\Phi(su))$）、**$\sigma:=-\gamma\circ\beta$**，于是 $\widehat\pi\Phi(su+\sigma u)=\widehat\pi\Phi(su)-\beta u\in U\'$；三段均为 Lean 定理（`PRec.exists_sigma` 等）。

**[需额外假设 → 下界已复核成立；递归 $(\le)$ 已补显式 $\sigma$（待复核）]** —— 命题一节已写出 $\Phi$、$\mathcal F$、$P$ 的精确定义与 $\mathcal F=\varnothing\Rightarrow P=+\infty$；纸面证明已补 $\Phi'$ 良定义（像落在 $\frac{Y/M}{C'}$）、逐可行 $U$ 的下界证明、递归两半与空族一致性。详见卷宗的「专家复核意见」一节。**等级**：[已证] $+$ **[Lean]**（`D1Core.d1_P_lower_bound` = 本条陈述（$P$ 的定义 `D1Core.P` 在 `D1Core.lean`）；逐 $W$ 版 `d1_lower_bound`。假设"可行集非空"，空集时 $P=0$ 无意义）。
**等级**：[已证] $+$ **部分 [Lean]**（D.4 覆盖 $({\ge})$ 半、可行性下降、$\Phi'$ 良定义、截面与构造步；$({\le})$ 的实构造仍纸面）。
**等级**：[已证]。
**等级**：[Lean] `PRecursion` / `PRecursionLift` / `PRecursionSigma`（见 [tools/lean/](../tools/lean/README.md)）。
**等级**：[已证]（**完整证明**：[proof/p_is_polynomial/reduction.md](../proof/p_is_polynomial/reduction.md)，含 $T$ 的良定义）。
**等级**：由 D.3。

---


---

### F.1 · 秩屏障

**F.1（a）〔原 F.1〕（秩屏障）** 设 $\mathcal L$ 是层 $(\rho,c)$ 的任一候选（$\rho=\dim\pi(\mathcal V)$、$c=\dim(\mathcal V\cap\mathcal J)$）。
对 $\lambda_0\in\mathbb C$ 记
$$r(\lambda_0):=\dim\pi\big(\mathbb C^n(\lambda_0I-A)\big)=\operatorname{rank}[\lambda_0I-A;\,C;\,CA]-j .$$
则：**若 $(5b)$ 在 $\lambda_0$ 处成立，必有 $\rho\le r(\lambda_0)$。**
特别地，若 $\rho>\min_{\lambda}r(\lambda)$，该层**不可行**。

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/F.1/](../proof/F.1/README.md)。
*专家意见（2026-11-06）*：秩屏障只是**必要条件**；无其它定理时不得当充分条件用。
*Lean 内核（2026-11-06 登记）*：**[Lean-conditional]** —— `RankBarrier.rank_barrier`（陈述级）+ `F1_Matrix` 的四条前置；差异见 [proof/F.1/](../proof/F.1/README.md) 的 `## Lean` 一节。
**等级**：[已证-纸面] $+$ [精确验证 1484+113] $+$ **[Lean]**（`RankBarrier.rank_barrier_full`：$(5b)$ ⟹ $\rho\le\dim\pi_J(\operatorname{range}M)$，
**等级**：[已证-纸面]（由 E.1 + F.1）。

---


---

### G.1 · 判定问题的复杂度上界与编码

**G.1（a）〔原 G.1〕** $\mathrm{DEC}(q)\in\exists\mathbb R$（chart-free 编码；变量/方程 $O(n^3)$、次数 $\le n$、$O(n)$ 个 $s$ 分支）。
*证明要点*：$Z$-表述（无图卡析取）$+$ 核心引理 $\ker(CAZ)=Z\cap\mathcal V$（故 $(A)\iff A(S)\subseteq Z$）
$+$ 多项式左逆证书 $X(\lambda)P(\lambda)=I_t$（$\deg X\le t-1$）。
**等级**：[已证-纸面] $+$ 两实例精确验证 $+$ **部分 [Lean]**（`CoreLemma` 的核心引理、`ExistsRLemmas` 的左逆 $\Rightarrow$ 单射；$\exists\mathbb R$ 的**编码规模**不是 Lean 的对象）。
**完整证明**：[proof/dec_q_existsR/README.md](../proof/dec_q_existsR/README.md)。

**编码为什么是多项式规模（2026-11-04 澄清，此前被我们自己的"更正"误伤）**：编码**不用**"列出全部极大子式"的
非结构化 Bézout $\sum u_im_i=1$（那个变体的规模是指数的：$N=\binom{n}{\rho}\binom{\rho+d}{\rho}$），而是
* **结构化左逆** $X(\lambda)P(\lambda)=I_t$（对 $X$ 的系数线性，未知数 $t^2q=O(n^3)$、次数 $\le t-1\le n$），
  次数界来自 Noferini–Van Dooren（LAA 658, 2023）Lemma 5.2 的右逆判据（转置使用），本文档已逐条核对条件；
* **退化层（$Z\cap\mathcal V=S\ne0$）**由**对 $s=\dim S$ 的 $O(n)$ 项析取**处理，并在商 $V/S$ 上做左逆——
  故不需要"一般秩的广义逆"或 Smith 酉模的次数控制。
⟹ **每个固定阶 $q$ 的 $\mathrm{DEC}(q)$ 都在 $\exists\mathbb R$**，且编码为多项式规模；这一点从未被推翻。
**注**：这是 $q1$ 的**上界**，不是答案；下界（$\exists\mathbb R$-hard）与多项式算法**均未知**。

**G.1（b）〔原 G.2〕（用可观性归约的**紧凑秩分层编码**；专家 2026-11-04 §4/§7 的 work package 2）** 固定阶 $q$。下列系统
（对 $s\in\{0,\dots,q\}$ 作**有限析取**）与"存在 $(5a)\wedge(5b)$ 的 $\mathcal L$"等价：

| 变量 | 尺寸 | 约束 |
|---|---|---|
| $\mathcal L$（或 $W$：$\mathcal Z=KW$）| $q\times n$（$W$：$k\times d$）| $\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$；$Y_W W=I_d$；$\operatorname{rank}[C;\mathcal L]=p+q$（用 $\mathcal L$ 的行加 $C$ 的左逆证书）|
| $T$ | $q\times(q+2p)$ | $(5a)$：$\mathcal LA=T[\mathcal L;CA;C]$ |
| $\Lambda,G_0,G_1$ | $q\times q,\ q\times p,\ q\times p$ | $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$ |
| $A,B$ | $q\times s,\ s\times d_V$ | $M:=\mathcal LV_0=AB$（$V_0$ 为 $V=\ker[C;CA]$ 的固定基）|
| $Y_A,Y_B$ | $s\times q,\ d_V\times s$ | $Y_AA=I_s$、$BY_B=I_s$（$\operatorname{rank}M=s$ 的证书）|
| $E$ | $(q-s)\times q$ | $EM=0$ |
| $Y_E$ | $q\times(q-s)$ | $EY_E=I_{q-s}$（$\operatorname{rank}E=q-s$ 的证书）|
| $E_0,\dots,E_{q-1}$ | $q\times(q-s)$ 各 | $E_0=E$、$E_{j+1}=E_j\Lambda$（**递推**，见下）|
| $Y_O$ | $q\times q(q-s)$ | $Y_O\widetilde{\mathcal O}=I_q$，$\widetilde{\mathcal O}=[E_0;E_1;\dots;E_{q-1}]$ |

**规模**：变量 $O(q^3+qn)$、约束 $O(q^3+qn)$、次数 $\le2$（全部线性/双线性）；析取 $q+1$ 项。
**必须用递推（专家 2026-11-04 §4.1 的更正）**：若直接展开 $\mathcal O=[E;E\Lambda;\dots;E\Lambda^{q-1}]$，
则 $E\Lambda^k$ 的条目次数是 $k+1$，**破坏"次数 $\le2$"**。改为引入辅助变量 $E_j$ 与双线性约束
$E_0=E$、$E_{j+1}=E_j\Lambda$，观测性矩阵用 $\widetilde{\mathcal O}$ 代替，则每条约束都是双线性的，
变量增加 $O(q^3)$ 而阶数不变。脚本已按递推实现并核验 $E_{j+1}=E_j\Lambda$ 与 $Y_O\widetilde{\mathcal O}=I_q$。

*必要性*：给定满足 $(5a)\wedge(5b)$ 的 $\mathcal L$——$T$ 由 $(5a)$ 存在；$\Lambda,G_0,G_1$ 由 $(5a)$ 的
行包含存在；$s=\operatorname{rank}M$、$A$ 取 $M$ 的 $s$ 个主元列、$B$ 取行最简形的 $s$ 行，则 $AB=M$；
$E$ 取 $\operatorname{im}M$ 的零化子则 $EM=0$、$\operatorname{rank}E=q-s$；$Y_O$ 存在由 B.12
（$(5b)\iff\operatorname{rank}\mathcal O=q$）。
*充分性*：由 $T$ 得 $(5a)$；由 $Y_W$ 得 $\dim\mathcal Z=d$；由 $EM=0$、$\operatorname{rank}E=q-s$、
$\operatorname{rank}M=s$ 得 $\ker E=\operatorname{im}M=\mathcal L(V)$；由 $Y_O\mathcal O=I_q$ 得
$\operatorname{rank}\mathcal O=q$ ⟹ $(E,\Lambda)$ 可观测 ⟹ 由 B.12 得 $(5b)$。$\square$

*等级*：**[已证-纸面]**（必要性 + 充分性如上一段）$+$ **[精确验证]**：`tools/verification/compact_obs_encoding.py`
在**两个已知可行见证**（C4 的 $q=4$ 见证、$n=5,p=2,r=1$ seed 3023 的 $q=2$ 见证）上**显式构造全部辅助变量**
并逐条核验 16 条约束（含 $Y_O\mathcal O=I_q$ 的数值验证），全部通过。
*注*：这是**编码**，不是算法；它把 $\exists\mathbb R$ 成员性做成"变量/约束多项式、次数 $\le2$"的形式，
* **规模记账（专家 2026-11-04 §4.2 的复杂度模型要求；脚本 `encoding_size_accounting.py`）**：
  模型为——输入有理、$\le B$ 比特；实数变量（复变量拆实/虚部，变量与约束各 $\times2$）；**位复杂度**；
  秩层析取**计入**规模（$\le(q+1)\times$单分支）。单分支在 $n=8,p=r=2,q=4,s=2$ 时为
  **变量 200 / 约束 208 / 次数 $\le2$**（含 $q+1=5$ 项析取：$\le1000$ / $\le1040$）；
  $n=12$ 时单分支约 570 / 515 ⟹ 均为 $O(q^3+qn)$，最大项来自 $E_j$ 递推与 $Y_O$（$q^2\cdot(q-s)$）。
  位长 $O(n^2(B+\log n))$（Hadamard + Cramer）。
与 G.1 的 Bézout 左逆编码相比更短（不需要 $t^2q$ 个左逆系数与 Noferini–Van Dooren 次数界）。
*位置*：本文件 B.12、G.1；专家 2026-11-04 §4/§7。
*位置*：本文件 B.10；[docs/08_results.md](08_results.md) §4.11.1。

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/G.1/](../proof/G.1/README.md)。
*专家意见（2026-11-06）*：须显式写出：多项式左逆次数界的**定理依据**、复到实的 realification、系数 bit-size 的多项式界。


---

### H.1 · 商等价、方阵条件与 $d=0$ 边界

**H.1（a）〔原 H.1〕（商等价定理 Theorem Q）** 设 $Z\subseteq H$、$S=Z\cap V$、$A(S)\subseteq Z$、$U=Z/S$、
$P(\lambda)=(A-\lambda I)|_{V/S}$。则
$$\operatorname{rank}\big[(\lambda I-A)V\mid Z\big]=\dim(V+Z)
\iff \operatorname{rank}\big[U\mid P(\lambda)\big]=r+t .$$

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/H.1/](../proof/H.1/README.md)。
*专家意见（2026-11-06）*：$A(S)\subseteq Z$ 作为**显式假设**保留（虽可由 $(5a)$ 推出）；$[U\mid P(\lambda)]$ 一般不必方阵，方阵性对应 $q=t$。
**等级**：[已证-纸面] $+$ [精确验证 18 个 $Z$] $+$ **[Lean]**（`QuotientEquivalence.qe_full` = 本条陈述；
**等级**：[已证-纸面] $+$ 精确验证 $+$ **[Lean]**（`DimArithmetic.r_add_t`、`square_iff`、`m_iff_h`；$\mathbb N$ 无截断前提 `no_truncation`）。归档：[proof/h2_dim_arithmetic/](../proof/h2_dim_arithmetic/README.md)。
**等级**：[已证-纸面] $+$ [精确验证 40/40] $+$ **[Lean]**（`D0Boundary.d0_forall` = 本条陈述的 $\forall\lambda$ 版；


---

### K.1 · 双向量可分解性

**K.1（a）〔原 K.1〕** $m=3$：每个非零双向量都可分解（$\mathrm{Gr}(2,3)=\mathbb P(\Lambda^2\mathbb C^3)$）。[已证-纸面]

**K.1（b）〔原 K.2〕** $m=4$ 且 $\ell\ge2$：$q|_K$ 是 $\ge2$ 元二次型，$\mathbb C$ 上必有非零零点 ⟹ 必有可分解元；
$\ell=1$ 时退化为 $q(p_0)=0$。[已证-纸面] $+$ [精确验证 20/20] $+$ **[Lean-conditional]**
（`Isotropy.exists_root_quadratic`：$a\ne0$ 时 $at^2+bt+c$ 在代数闭域有根；
`Isotropy.exists_ne_zero_quadraticMap_eq_zero`：$\dim\ge2$ 的二次型有非零零点；
`Isotropy.K2_isotropic`：限制到 $\ge2$ 维子空间仍成立。
**差异**：未形式化"Klein 二次型 $=0\iff$ 双向量可分解"这一步（需要 $\Lambda^2$ 与 Plücker 的建模）——所以这里是**内核**，不是整条 K.2）。

**K.1（c）〔原 K.3〕** $\ell\ge N-(2m-4)$：必有可分解元（由 $\mathbb P(K)$ 投影的维数计数）。[已证-纸面] **（复版本：$E=\mathbb C^m$、$K$ 复线性；若最终要求**实**观测器，需另加实点论证——专家 2026-11-01 §3.3 指出射影维数定理只给复交点。）**

**推论**：$m\le4$ 或 $\ell$ 大时"可分解性"**不构成障碍** ⟹ $r=2$ 的难度只能来自
可容许性的开条件（$U_p\cap B=0$）与 $\exists S$；$m\ge5,\ell\le3$ 时才是真约束（判定算法见 K.4）。

**K.1（d）〔原 K.4〕**（算法，$m\ge5$、$\ell\le3$）：$\ell=2$ 用 5 个一元二次式的 gcd；$\ell=3$ 用 $(x,y,z)^s\subseteq I$ 的理想成员判定
（可靠 NO）加有理点（可靠 YES），都不是则"未决"。
**等级**：[精确验证]（可靠性核对：65 True / 43 False / 0 未决，无"说谎"情形）。
**位置**：[proof/bivector_r2](../proof/bivector_r2/README.md)。

**实例观察**：构造的 $n=9,p=2,q=4,s=1$ 实例上 $\dim K=6$、加线性可容许后 $\dim K'=2$，
可分解点在**二次扩张**里（gcd 次数 2、无有理根），有理格点枚举 720 个可容许 $U$ 一个也没命中
⟹ "$\exists$ 可容许 $U$"的精确判定不能只靠有理搜索（CLAUDE §7.12 的又一实例）。

*证明与验证*：纸面证明、Lean 声明与精确验证**统一归档**在 [proof/K.1/](../proof/K.1/README.md)。

---
## 附录 A：铅笔的 Smith 判据

陈述、证明与复核记录见 [proof/B.8/](../proof/B.8/README.md) 的「附录：铅笔的 Smith 判据」一节
（原 `## J.`；判据矩阵里记为 I.5）。

---

## 附录 B：判据矩阵（原 `## I.`）

## I. 判据矩阵（判据 × 域 × 强度 × 证据）

> 这是交接文档 §3 的**固化版**。**不知道域就会用错判据**——上一阶段正是这样错的。

| # | 判据 | 适用域 | 对 $(S)$ 的强度 | 依据 | 等级 |
|---|---|---|---|---|---|
| I.1 | 全部 $(r+t)$-子式的 gcd 是非零常数 | 任意 $q$（$r+t\le w_m$；$r+t>w_m$ 恒不可行）| **充要** | B.1 + H.1 | [已证-纸面] |
| I.2 | 单个 $\det[U\mid P(\lambda)]$ 是非零常数 | **仅 $q=t$**（$r+t=w_m$，方阵）| **充要** | H.2 + Laplace 恒等式 | [已证-纸面] + [精确验证] |
| I.3 | 系数判据 C1：$p_U\in K$、$a_0(p_U)\ne0$，且 $p_U$ 可分解、$U$ 可容许 | $q=t$ | **充要** | §3.2 的 C1 | [已证-纸面]（$r\le3$）+ [精确验证] |
| I.4 | 线性松弛 C2：$a_0|_K\ne0$ | 任意 $q$ | **只必要**（C1 ⟹ C2）；$q\ne t$ 时对 $(S)$ 不必需 | §3.2 的 C2 | [已证-纸面] |
| I.5 | 行列式因子 $\Delta_{r+t}$ 是常数（Smith 形）| 任意 $q$ | 与 I.1 同一个量 | §J | [已证-纸面] + [精确验证] |

**三条容易踩的（每条都有实例）**

1. $q\ne t$ 时"单个 $\det$"**不存在**（非方阵）⟹ 用它否定可行性不合法（支 5 的 58 例，2026-11-01 撤回）。
2. $m=r+t$ **不是**方阵条件：方阵 $\iff r+t=w_m\iff q=t$；$m=r+t\iff h=w$（$L_0\subseteq\operatorname{row}C$ 的退化情形）。
   用 $m$ 行对象当 $\det[U\mid P]$ 只在 $H=W$ 时正确（H.2 与 CLAUDE §10.1）。
3. 均匀条件 $D_{\rm adm}(K)=K$ **不成立**：$q=t,r=2$ 上已有 $\dim K\ne0$ 而 $\dim D_{\rm adm}=0$ 的实例
   （12 个 $S$、60 个可容许 $U$），所以 I.4 不能替代 I.3。
