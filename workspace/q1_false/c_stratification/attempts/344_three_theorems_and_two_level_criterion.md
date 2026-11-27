# 344 三个正式命题（B / C / D）与"两级判据"框架

> 承接 342（97 号建议把这三条立起来）与 343（判据只需有限不可约覆盖）。
> 本文件给三条**定稿陈述**（含证明与等级），并把它们拼成可执行的判定框架。

## 目标

1. 把散在 336/337/338 里的三条结果写成正式陈述（Theorem B、Proposition C、Proposition D）。
2. 给出两级判据（零频秩 + generic gcd）的**框架**。
3. 用 [c343](../../../../tools/verification/c343_zero_frequency_preprocessing.py) 证明第一级真能作预处理。

## 设想与理由

97 号的审计结论是：**Theorem A**（闭性 + generic-gcd 判据）、**Theorem B**、**Prop C**、**Prop D**
可以安全地写成定理，而 Claim 1（分量）与 Claim 11（富余档生成好）还不能。既然如此，就把能立的三条立定，
再谈框架。

## 做法

### Theorem A（复述，97 号确认）

设 $Y$ 是一个不可约参数块，$H,H_A$ 为其上的多项式族，$\operatorname{rank}H\equiv\omega$。则
$$\mathcal B=\{y:\exists\lambda,\ \operatorname{rank}(\lambda H-H_A)<\omega\}$$
在 $Y$ 中闭；且
$$Y\ \text{含可行点}\iff \gcd_I m_I=1\ \text{在}\ \overline{\mathbb Q(Y)}[\lambda].$$

### Theorem B（$p=1$ 的非特征层恒坏）

> **Theorem B.** 设 $p=1$、$q=n-2$、$r_0=0$。则在超平面层中，任何**非特征**核方向 $v\in K_0$ 的
> 可容许点都违反 $(5b)$。

*证明.* 记 $r=\operatorname{rank}[C;CA]$，$k=n-r$，$\omega=k-1$。
因 $p=1$，$[C;CA]$ 是 $2\times n$，故 $r\le2=p+1$，于是
$$n-2-p=n-3\le k-1 .$$
又 $q=n-2$ 且 $V\subseteq U^\perp$（$\dim U^\perp=n-2$）⟹ $V=U^\perp$。分两档：

- **严格**（$r<2$）：把 $C$ 的行放进 $U^\perp$ 的基，商铅笔有 $p=1$ 个恒零行，故
  $\operatorname{rank}\widetilde M\le n-3<k-1=\omega$ 对一切 $\lambda$ ⟹ 坏；
- **临界**（$r=2$）：$n-3=k-1$，删去零行后是 $(k-1)\times(k-1)$ 方阵 $\lambda X'-G'$；
  由 $\operatorname{rank}H=\omega$ 且 $V=U^\perp$ 得 $\operatorname{rank}X'=k-1$，即 $X'$ 可逆；
  故 $\deg\det(\lambda X'-G')=k-1\ge1$，在 $\mathbb C$ 上有根 ⟹ 该处降秩 ⟹ 坏。$\square$

**等级**：`[已证-纸面]`（M3：96 号 + 97 号两轮确认；前提 $q=n-2$ 由 97 号指出）。
**`[Lean]`（取根一步）**：`quadratic_has_root`（[Quad.lean](../../../../trash/lean_removed_2026-11-19/tools/lean/MyProof/Quad.lean)，
`lake env lean` 退出码 0）——代数闭域上非平凡二次必有根，即 $\det(\lambda X'-G')$ 首项系数可逆时的"必有复根"。
矩阵层的"$\det(\lambda X-G)$ 是首项系数 $\det X\ne0$ 的二次多项式"未形式化，已在 `STATEMENT_MAP` 的差异栏注明。

*备注*：$k=1$（$\omega=0$）时论证空转，需另行处理；本项目的模式 $k=3$ 不受影响。

### Proposition C（零频秩）

> **Proposition C.** 设 $V=\operatorname{row}L$ 是任一可容许行空间。则
> $$\operatorname{rank}H_A=\dim(AK_0)-\dim(AK_0\cap V^\perp).$$
> 特别地：
> 1. $(5b)$ 在 $\lambda=0$ 要求 $\operatorname{rank}H_A=\omega$；
> 2. 若 $v\in AK_0$，则 $\operatorname{rank}H_A\le\dim(AK_0)-1$，故**必要性**：
>    $$\dim(AK_0)\ge\omega+1 ;$$
> 3. 若 $v$ 是特征向量且 $\lambda_0\ne0$，则 $v=A(v/\lambda_0)\in AK_0$，故
>    $$\dim(AK_0)\ge\omega+1=k .$$

*证明.* $\operatorname{im}(AN)=AK_0$，故 $\operatorname{rank}(LAN)=\dim L(AK_0)$；对 $L|_{AK_0}$ 用秩-零化度，
$\ker L=V^\perp$，得恒等式。再由 $V\subseteq v^\perp$（自由行的条件）得 $v\in V^\perp$；
若 $v\in AK_0$ 则 $AK_0\cap V^\perp\ni v\ne0$，得 (2)。(3) 由 (2) 与 $v\in AK_0$。$\square$

**等级**：`[已证-纸面]`（M3：97 号逐项核过，无需额外假设）。**`[Lean]`**：
`propC_rank_identity` / `propC_consequence`（[PropC.lean](../../../../trash/lean_removed_2026-11-19/tools/lean/MyProof/PropC.lean)，
`lake env lean` 退出码 0；已登记 `tools/lean/STATEMENT_MAP.md` §PropC.lean）。
抽象核：$\operatorname{finrank}(\operatorname{range}g)=\operatorname{finrank}(\operatorname{range}(f\circ g))
+\operatorname{finrank}(\operatorname{range}g\sqcap\ker f)$，取 $g=AN$、$f=L$ 即得。

### Proposition D（纤维充分性不成立）

> **Proposition D.** 取 $n=5$、$p=1$、$C=e_5^{\mathsf T}$、
> $$A=\begin{pmatrix}2&2&-1&0&0\\0&-2&1&0&1\\0&1&-2&0&-1\\0&0&0&0&2\\0&-1&2&0&-1\end{pmatrix}.$$
> 则 $e_1$ 是 $K_0$ 的特征向量（$Ae_1=2e_1$），但**整条特征纤维**都违反 $(5b)$（在 $\lambda=0$ 处）。

*证明.* $K_0=\operatorname{span}\{e_1,w,e_4\}$（$w=(0,2,1,0,0)$），
$AK_0=\operatorname{span}\{(2,0,0,0,0),(3,-3,0,0,0)\}$，$\dim(AK_0)=2=\omega$，且 $e_1\in AK_0\cap V^\perp$；
由 Prop C，$\operatorname{rank}H_A\le1<\omega$ 对每个可容许 $V$。$\square$

**等级**：`[已证-纸面]` + `[精确验证 40/40]`（M3）。**`[Lean]`（核心抽象形式）**：
`rank_drop_of_mem_common`（[PropC.lean](../../../../trash/lean_removed_2026-11-19/tools/lean/MyProof/PropC.lean)，`lake env lean` 退出码 0）——
"$v\ne0$ 同时落在 $\operatorname{range}g$ 与 $\ker f$ ⟹ 复合秩至少降一"，取 $g=AN$、$f=L$ 即得
$\operatorname{rank}(LAN)+1\le\dim(AK_0)$；具体矩阵 $A$ 的秩计算仍未形式化。

### 两级判据（框架）

**第一级（零频，线性代数）**：对每个候选行空间 $V$，算 $\operatorname{rank}H_A$；若 $\ne\omega$，直接丢弃。
**第二级（谱，符号）**：在通过第一级的块上算 generic gcd；$=1$ 即可行。

**验证**（c343）：在 Prop D 的实例上 40 个层点**零频通过 0 个**（整条纤维在算 gcd 之前就被排除）；
在 333 的好实例上 40 个层点**通过 36 个**（保留了候选）。这正是预处理应有的行为。

## 进展

1. 三条陈述定稿（Theorem B / Prop C / Prop D），等级与前提都写明。
2. 两级判据框架成形；第一级的**预处理效果已被验证**（0/40 vs 36/40）。
3. 与 Theorem A 拼起来，得到一条完整的判定流程：
   $$\text{枚举块}\to\text{零频筛}\to\text{generic gcd}\to\text{决定}.$$

## 最终结论

1. $c=1$ 这条线现在有**三个无条件（或前提明确）的定理** + **一个判据框架**。
2. 框架里唯一还不可执行的是"generic gcd"那一步的**代价**（PIT）与**有理点**；
   而第一级已经把大量实例提前排除。
3. 未定的只剩：Claim 1 的"分量"（不需要）、Claim 11 的"富余档生成好"（未证）。

## 放弃原因

- 没有把两级框架写成**完整算法**（复杂度未分析）；
- 有理点问题仍未解决；
- Theorem B 只覆盖 $q=n-2$（97 号指出任意 $q$ 未证）。

## 残留价值

- 三条可引用的正式命题（含证明与等级）；
- 一个**可执行的第一级**（零频筛），有实验支持；
- 把"$c=1$ 的判定"从一堆猜想整理成"两级的、第一级已可跑"的流程。

## 相关文件

- [attempts/342](../../decision_algorithms/attempts/342_expert97_audit.md)（97 号裁决）
- [attempts/336](336_fibre_sufficiency_counterexample.md)（Prop D 的原始记录）
- [attempts/337](337_lambda0_obstruction.md)（Prop C 的原始记录）
- [attempts/338](338_dimension_map_p1.md)（Theorem B 的原始记录）
- [attempts/343](343_stratified_cover_fix.md)（有限不可约覆盖）
- [c343](../../../../tools/verification/c343_zero_frequency_preprocessing.py)、[c341](../../../../tools/verification/c341_fibre_sufficiency_counterexample.py)

## 状态

- Theorem A：`[已证-纸面]`（M3，97 号确认）。
- Theorem B：`[已证-纸面]`（M3，前提 $p=1,q=n-2,r_0=0$）。
- Proposition C：`[已证-纸面]`（M3）。
- Proposition D：`[已证-纸面]` + `[精确验证 40/40]`（M3）。
- 两级框架的第一级：`[精确验证]`（c343）；第二级的代价：`[未做]`。
