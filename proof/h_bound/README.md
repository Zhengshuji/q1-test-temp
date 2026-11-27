# 方阵情形的谱障碍：$\ker C=\mathcal V\oplus Z$ 时 $(S)$ 必失败（更正版 2026-10-30，含宽矩阵数据）

> **对应 docs 条目**：B.9（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

> 本文件经历过一次更正：原先把结论写成"$h=n-p\Rightarrow(S)$ 失败"（无条件），**错了**；
> 宽矩阵反例见 [proof/refuted/README.md](../refuted/README.md) **R13**。
> 正确的形式是下面的"互补障碍"，它要求**同时**满足列数 $N_c=h$ 与 $h=n-p$。

## 记号

$L$ 为 $q$ 行增广、$\operatorname{rank}[C;L]=p+q$（P2 的假设，[../l0_reduction/README.md](../l0_reduction/README.md) 可保证），
$d=n-p-q$，$Z$ 的列张成 $\ker[C;L]$，$V$ 的列张成 $\ker[C;CA]$（$\dim n-r_1$），
$h=\operatorname{rank}[V\mid Z]$，铅笔 $P(\lambda)=[(\lambda I-A)V\mid Z]$，列数 $N_c=(n-r_1)+d$。

## 定理（互补障碍）

**若 $V\cap Z=0$ 且 $V+Z=\ker C$（即 $\ker C=\mathcal V\oplus Z$）且 $\dim V\ge1$，则 $(S)$ 失败**（对满足 $(A)$ 的 $Z$）。

注意这两个条件是 $N_c=h$（即 $V\cap Z=0$）与 $h=n-p$（即 $V+Z=\ker C$）的合取；由 $d=r_1-p$ 得它只在 $q=n-r_1$ 时可能发生。

*证明*：
1. $P(\lambda)$ 的列全在 $\ker C$ 里（$C(\lambda I-A)V=\lambda CV-CAV=0$、$CZ=0$）。
2. $\ker C=\mathcal V\oplus Z$ 且 $N_c=h=\dim\ker C$ ⟹ 取 $\ker C$ 的基，$P$ 是**方阵** $\tilde P(\lambda)$（$h\times h$），唯一极大子式是 $\det\tilde P(\lambda)$。
3. $\det\tilde P$ 的 $\lambda$-次数 $=n-r_1=\dim V\ge1$，首项系数 $=\det[V\mid Z]\ne0$ ⟹ **非常数** ⟹ 有复根 ⟹ 秩降 ⟹ $(S)$ 失败。∎

## 宽矩阵数据（[c218_wide_case.py](../layer_program/c218_wide_case.py)，随机 $n=5,6$、$p=1,2$、所有 $q$）

| 情形 | 采样 | $(S)$ 成立 |
|---|---|---|
| **方阵**（$N_c=h$）且 $h=n-p$ | 88 | **0** ← 定理 |
| 方阵且 $h<n-p$ | 54 | 54 |
| 宽（$N_c>h$），$h=n-p$ | 114 | 114 |
| 宽，$h<n-p$ | 2 | 2 |

即：在这些采样里，**唯一的谱障碍就是"互补"情形**；其余情形 $(S)$ 都成立。
（这是 `[精确验证]`，不是证明；"其余情形恒成立"未证。）

## 实例

- **P2 例子 $q=4$**：$n=8,p=2,q=4$，$n-r_1=4$ ⟹ $q=n-r_1$，且 $N_c=6=h=n-p$ ⟹ **互补障碍** ⟹ $(S)$ 必失败；
  配合 [c216_rdivisor.py](../layer_program/c216_rdivisor.py)（$r<d$ 除子上 $(A)$ 0/240），得 $q=4$ 的 all-bad 是确定的 ✓。
- **P2 例子 $q=5$**：$q\ne n-r_1$ ⟹ 不可能是互补情形 ⟹ 无障碍（且确实可行）✓。

## 状态

- 定理（互补障碍）：**[已证-纸面]**（方阵 + 互补，本文件）。
- 宽矩阵：**[精确验证 246/246 通过]**；"宽矩阵恒通过"是**猜想**，未证。
- "可行 $\Rightarrow h<n-p$"：**已推翻**（R13）。
- 推论：**只有阶 $q=n-r_1$ 可能被互补障碍挡住**（因为 $d=r_1-p$ 是唯一的相容条件）。

## 猜想（唯一障碍）—— **已被 R14 推翻**（2026-10-30）

曾经的猜想：$(S)$ 失败仅当 $\ker C=\mathcal V\oplus Z$（互补）。**错。**

**反例**（[c219_wide_failure.py](../layer_program/c219_wide_failure.py)）：$n=5$、$p=1$、$C=e_1$、$L_0=e_5$，
$A$ 让 $W=\operatorname{span}(e_2,e_3,e_4)$ 不变、$Z=W$：$(A)$ 成立、$h=4=n-p$、但 $N_c=7>h$（非互补），
精确 gcd 次数 $=1$ ⟹ $(S)$ 失败。

**为什么上一轮的 528 点数据没发现**：那些点用**随机** $Z$ 采样；失败点落在"$Z\subseteq\mathcal V$ 且 $A|_Z$ 有结构"的**薄集**上
（CLAUDE §7.12：薄集不许采样）。

**现在的图景**：已确认的 $(S)$ 失败机制至少两种：
1. **互补障碍**（定理）：$\ker C=\mathcal V\oplus Z$ ⟹ 必失败；
2. **$Z\subseteq\mathcal V$ 且有 $A$-结构**（R14）：宽矩阵也可失败。

⟹ 无前提的"唯一障碍"**不成立**；$(S)$ 的失败集比互补位置大。

**但注意**：R14 的实例**不满足 P2 的前提**（不是功能可观测，$\operatorname{row}L_0
ot\subseteq\operatorname{row}\mathcal O_C$）。
所以"**在功能可观测前提下** $(S)$ 只可能在互补位置失败"**仍是未决问题**（不是已推翻）。

## 谱失败的干净判据（把"失败"还原成维数）

$P(\lambda)$ 的列就是 $(\lambda I-A)\mathcal V$ 与 $Z$ 的列，因此
$$\operatorname{rank}P(\lambda)=\dim\big((\lambda I-A)\mathcal V+Z\big),\qquad
(S)\iff \dim\big((\lambda I-A)\mathcal V+Z\big)=\dim(\mathcal V+Z)\ \ \forall\lambda.$$
"失败" $\iff$ 存在 $\lambda$ 使这个和空间**塌缩**。两种典型塌缩：
- 互补障碍：$\dim(\mathcal V+Z)=n-p$ 已占满 $\ker C$，行列式必为零；
- **特征方向未被覆盖**：$\lambda$ 是 $A|_{\mathcal V}$ 的特征值、特征向量 $v\in\mathcal V$，而 $Z$ 不含 $v$ 的方向
  ⟹ $(\lambda I-A)\mathcal V$ 掉一维、（$Z$ 不够大时）和空间随之塌缩。

**例子**（对角）：$A=\operatorname{diag}(0,1,2,3)$、$C=e_1$、$\ker[C;L_0]=\operatorname{span}(e_2,e_3)$（$d=2$）：
$\mathcal V=\operatorname{span}(e_2,e_3,e_4)$、$h=3$；在 $\lambda=3$（$e_4$ 的特征值，$e_4
otin Z$）处
$(3I-A)\mathcal V=\operatorname{span}(e_2,e_3)$，加 $Z$ 仍是 $\operatorname{span}(e_2,e_3)$，维数 $2<3$ ⟹ $(S)$ 失败（精确 gcd 次数 $=1$ ✓）。

**注意**："$Z\subseteq\mathcal V$ 且 $A$-不变 ⟹ 失败"**没有**被证明；上例的失败来自"特征方向未被覆盖"，
而不是单凭不变性。R14/R15 的族里 $(A)$ 恰好只对不变 $Z$ 成立，所以才看起来像"不变性导致失败"。

## 顶层定律（定理 + 数据，2026-10-30）

**定理**：在**顶层**（$\operatorname{rank}(CAZ)=d$）上，
$$\mathcal V\cap Z=0,\qquad h=\operatorname{rank}[\mathcal V\mid Z]=N_c=(n-r_1)+d .$$
*证明*：若 $0\ne z\in\mathcal V\cap Z$，则 $CAz=0$ ⟹ $\operatorname{ord}(CAZ)<d$，矛盾 ⟹ $\mathcal V\cap Z=0$ ⟹ $h=\dim\mathcal V+d=N_c$ ✓。

**推论**：顶层上"互补" $\iff h=n-p\iff N_c=n-p\iff q=n-r_1$。于是
- 若 $q=n-r_1$：顶层**整个**落在互补位置 ⟹ 由互补障碍定理，$(S)$ 在顶层**处处失败**；
- 若 $q\ne n-r_1$：顶层不是互补 ⟹ 由互补障碍定理不能结论；若 $A$ 在 $\mathcal V$ 里没有特征向量，则 $(S)$ 在顶层**成立**。

**数据**（随机 $n=5,6$、$p=1,2$、全部 $q$、只取顶层点）：

| $q$ 与 $n-r_1$ | 点 | $(A)$ | $(S)$ |
|---|---|---|---|
| $q=n-r_1$ | 104 | 全成立 | **0**（全失败）✓ 与定理一致 |
| $q\ne n-r_1$ | 84 | 全成立 | **84**（全成立）|

⟹ **"顶层上 $(S)$ 失败 $\iff q=n-r_1$"**（在"$A$ 在 $\mathcal V$ 内无特征向量"的随机样本里 188/188 成立）。
注意这与 R14/R15 不矛盾：那些失败点**不在顶层**（$r=\operatorname{rank}(CAZ)<d$）。

**对判定的含义**：顶层（占 $(A)$-可行点的"厚"部分）上，$(S)$ 的判定**只看 $q=n-r_1$**——一个纯整数条件；
薄层（$r<d$）才是真正需要 $\Theta$ 的地方。

## 商铅笔恒等式与维数障碍（Theorem D，2026-10-30，据专家 QA10 的建议）

记 $S=\mathcal V\cap Z$、$s=\dim S$、$t=\dim(\mathcal V/S)=\dim\mathcal V-s$、$q=n-p-d$。

**引理（商铅笔恒等式）**：在 $(A)$ 下
$$\operatorname{rank}P_\Theta(\lambda)=d+\operatorname{rank}T_\lambda,\qquad
T_\lambda:\ \mathcal V/S\to\ker C/Z,\quad T_\lambda(v+S)=(\lambda I-A)v+Z .$$

*证明*：由 $(A)$（$\operatorname{rank}[Z,AZR_Z]=d$）得 $AZR_Z\subseteq\operatorname{im}Z$；
对 $x\in S$ 有 $x=Z\alpha$、$CAZ\alpha=0$ ⟹ $\alpha=R_Z\beta$ ⟹ $Ax=AZR_Z\beta\in\operatorname{im}Z$。
于是对 $x\in S$：$(\lambda I-A)x=\lambda x-Ax\in\operatorname{im}Z$ ⟹ $v\mapsto(\lambda I-A)v+Z$ 在 $S$ 上为零，
下降到 $\mathcal V/S$。而 $P$ 的列是 $(\lambda I-A)\mathcal V$ 与 $Z$，故
$\operatorname{rank}P=\dim((\lambda I-A)\mathcal V+Z)=d+\operatorname{rank}T_\lambda$ ✓。

**等级**：**部分 [Lean]** —— [tools/lean/MyProof/QuotientPencil.lean](../../trash/lean_removed_2026-11-19/tools/lean/MyProof/QuotientPencil.lean)
机器验证了第一步：`range_coprod_eq`（$[T\mid Z]$ 的像 $=\operatorname{range}T\sqcup Z$），退出码 0（2026-10-30）。
**第二步**（$\operatorname{finrank}(\operatorname{range}T\sqcup Z)=\operatorname{finrank}Z+\operatorname{finrank}(\operatorname{range}(q_Z\circ T))$）
仍是纸面。**2026-10-30 的 Lean 尝试**（草稿 [trash/lean_scratch/QuotientPencil2.lean](../../trash/lean_scratch/QuotientPencil2.lean)）：
证明骨架已完整（设 $U'=\operatorname{range}T\sqcup Z$，对 $q_Z$ 限制到 $U'$ 用秩-零化度），
只剩两个 Mathlib 名字没对上：

| 需要的事实 | 实际存在的引理（实测）|
|---|---|
| $\operatorname{map}q_Z\,Z=\bot$ | ✗ 无 `Submodule.map_mkQ_eq_bot`；但 `Submodule.map_mkQ_eq_top` 存在（$=\top$ 版本）|
| $\operatorname{finrank}(Z\text{ 在 }U'\text{ 中的原像})=\operatorname{finrank}Z$ | ✗ 无 `finrank_submoduleOf`；有 `Submodule.map_comap_subtype`（$\operatorname{map}p.\mathrm{subtype}\,(\operatorname{comap}p.\mathrm{subtype}\,p')=p\sqcap p'$）|
| 秩-零化度 | ✓ `LinearMap.finrank_range_add_finrank_ker` |
| 子空间维数公式 | ✓ `Submodule.finrank_sup_add_finrank_inf_eq`（注意**不是** `finrank_sup_add_finrank_inf`）|

**定理 D（维数障碍）**：若 $t>0$ 且 $(S)$ 成立，则 $q>t$。等价地 $q\le t$ ⟹ $(S)$ 失败。

*证明*：$T_\lambda$ 的值域在 $\ker C/Z$（$\dim=q$）里。
- $q<t$：值域维数 $<t$，$T_\lambda$ 永不单射 ⟹ $\operatorname{rank}P<d+t=h$ ⟹ 失败；
- $q=t$：方阵，$T_\lambda=\lambda\iota-\bar A$ 且 $\iota$ 可逆 ⟹ $\det T_\lambda=\det\iota\cdot\det(\lambda I-\iota^{-1}\bar A)$
  是次数 $t>0$ 的**首一**多项式 ⟹ 有复根 ⟹ 该处奇异 ⟹ 失败；
- $q>t$：无维数障碍。$\square$

**等级**：**[Lean]** —— [tools/lean/MyProof/TheoremD.lean](../../trash/lean_removed_2026-11-19/tools/lean/MyProof/TheoremD.lean)，
`lake env lean MyProof/TheoremD.lean` 退出码 0（2026-10-30 实测）。Lean 陈述：
`theoremD_dim_lt`（$\dim W<\dim V$ ⟹ 任何 $V\to W$ 的线性映射都不单射）与
`theoremD_dim_eq`（$\dim V=\dim W$、$\iota$ 单射、$K$ 代数闭 ⟹ $\exists\,lam$ 使 $lam\cdot\iota-A$ 不单射）。

**推论（顶层）**：顶层上 $\mathcal V\cap Z=0$ ⟹ $t=\dim\mathcal V=n-r_1$ ⟹ **$q\le n-r_1$ 时 $(S)$ 必失败**。

### 商铅笔的实例化（Q2 的第一步，2026-10-30）

专家指出抽象上 $\iota(x)=\binom{x}{0}$、$\bar A(x)=\binom{0}{x}$ 使 $\lambda\iota-\bar A$ 恒满列秩。
我们把它**实现成了真正的观察者实例**（[c231](../layer_program/c231_realize_abstract.py)）：
$n=5,p=1,r=1$、$C=e_1$、$L_0=e_2$、$A\colon e_1\mapsto e_2,\ e_2\mapsto e_5,\ e_5\mapsto e_1,\ e_3\mapsto e_3,\ e_4\mapsto e_4$；
$\mathcal V=\operatorname{span}(e_2,e_3,e_4)$、$Z=\operatorname{span}(e_3,e_4)$（$d=2$）、$q=2$、$s=2$、$t=1$、$q>t$；
$A\mathcal V\not\subseteq\mathcal V+Z$（$Ae_2=e_5$）、$(A)$ 成立、$(S)$ 成立、**功能可观测** ✓。
⟹ **定理 C 的假设 $A\mathcal V\subseteq\mathcal V+Z$ 不是必然的**：$\bar A$ 有落在 $\iota$ 像外的分量，$(S)$ 仍可成立。

**但它是终端阶**（$n_0=3$、$n_0-p=2=q$）。以下是结构性原因：

**引理**：$\ker\mathcal O_C\subseteq\mathcal V$，且若 $Z\subseteq\ker\mathcal O_C$ 则 $q\ge n_0-p$（因为 $d\le n-n_0$）。

*证明*：$\ker\mathcal O_C=\bigcap_k\ker(CA^k)\subseteq\ker C\cap\ker(CA)=\mathcal V$ ✓；
$Z\subseteq\ker\mathcal O_C$ ⟹ $d\le\dim\ker\mathcal O_C=n-n_0$ ⟹ $q=n-p-d\ge n_0-p$ ✓。

**推论**：由 P2 的阶范围 $q\le n_0-p$，若 $Z\subseteq\ker\mathcal O_C$ 则 **$q=n_0-p$（终端阶）**。
所以**非终端阶（$q<n_0-p$）必须 $Z\not\subseteq\ker\mathcal O_C$**——$Z$ 必须含"可观测方向"。
这解释了为什么我们的构造都落在终端阶，也给出下一步搜索的正确方向：$Z$ 要有可观测分量。

**进一步**（$Z\subseteq\mathcal V$ 时 $(A)\iff A$-不变，见上文引理）：$Z\subseteq\mathcal V$ 且 $A$-不变
⟹ $A^kZ\subseteq Z\subseteq\ker C$ ⟹ $Z\subseteq\ker\mathcal O_C$。所以
$$\boxed{\ \text{非终端阶}\ \Longrightarrow\ Z\not\subseteq\mathcal V\ }$$
即 $(A)$ 在非终端阶上**不可能**退化为"不变性"，必须是真正的秩条件。

**非终端薄层的搜索**（[c233](../layer_program/c233_nontrivial_search.py)，$n=6,7$、$p=2$、随机实例、全网格/采样）：
检查 **5504** 个 $(A)$-点，其中 $(A)\wedge(S)$ 成立 **1053** 个——但**全部**满足 $d\le p$（厚层）；
**非终端且薄（$q<n_0-p$ 且 $d>p$）的可行点：0 个** ✓ 无反例。

再用 Theorem D 收紧：非终端薄层需 $\dim(\mathcal V\cap Z)>p+d-r_1$（由 $q>t$ 推出），
而 $Z\not\subseteq\mathcal V$ 又要求 $\dim(\mathcal V\cap Z)\le d-1$ ⟹ 需要 $d-1\ge p+d-r_1+1$ ⟹ $r_1\ge p+2$。
所以 $p=1$ 时（$r_1\le2$）**非终端薄层不可能可行**——这解释了 $p=1$ 的搜索为何全在终端阶或厚层。

> **这修正了本文件之前的表述**："顶层失败 $\iff q=n-r_1$" 不完整——失败对所有 $q\le n-r_1$ 都成立；
> $q>n-r_1$ 才是"可能成立"的区域。我们之前 84 个顶层通过点应全在 $q>n-r_1$，与定理相容。

**实例核对**（[c230](../layer_program/c230_dimension_obstruction.py)，随机 $n=5,6$、$p=1,2$、随机 $\Theta$）：
$q\le t$ 的 40 个 $(A)$-点：$(S)$ 成立 **0** 个；$q>t$ 的 36 个：$(S)$ 成立 **36** 个 ✓ 与定理一致。
商铅笔恒等式本身在 P2 例子上逐 $\lambda$ 核对通过（[c229](../layer_program/c229_quotient_pencil.py)）：

| 阶 | $d$ | $t$ | $q>t$ | rank 恒等式 | $(S)$ |
|---|---|---|---|---|---|
| $q=4$ | 2 | 4 | 否 | ✓ | 失败 ✓（定理 D 预测）|
| $q=5$ | 1 | 4 | 是 | ✓ | 成立 ✓ |

## 公根的两种来源（[c222_root_origin.py](../layer_program/c222_root_origin.py)）

$\lambda_0$ 是公根 $\iff\exists x\ne0$：$(\lambda_0I-A)\mathcal V x_{\mathcal V}+Zx_Z=0$。按 $x_Z$ 分两类：

| 类型 | 条件 | 依赖 | 例子 |
|---|---|---|---|
| **结构型** | $x_Z=0$ ⟹ $\lambda_0$ 是 $A\|_{\mathcal V}$ 的特征值（$v\in\mathcal V$ 是特征向量）| **与 $Z$ 无关** | 对角例子：根 $=3$ = $e_4$ 的特征值 |
| **耦合型** | $x_Z\ne0$ ⟹ 由 $\mathcal V$ 与 $Z$ 的耦合产生 | 依赖 $Z$（因而依赖 $\Theta$）| P2 例子 $q=4$：4 个根全是耦合型（$-1.93\pm0.36i$、$-1.52\pm0.72i$，非 $A$ 的特征值）|

**结构型的推论**：若 $A$ 在 $\mathcal V$ 里有特征向量，则对**任意** $Z$ 都有 $\operatorname{rank}P(\lambda_0)\le N_c-1$；
当 $N_c=h$（方阵）时这直接给出 $(S)$ 失败 —— 与互补障碍相容。
**耦合型**：根随 $Z$ 变，是"广义特征值"问题，$(S)$ 的判定要靠 gcd（或 Smith 形式），不能只在 $A$ 的谱上检验。

## 可行性图景（判定流程，2026-10-30）

综合以上，给定 $(A,C,L_0)$ 与阶 $q$（$d=n-p-q$）：

| 情形 | 判定 | 依据 |
|---|---|---|
| $q=n_0-p$（终端阶）| **可行** | P2 Thm 7；[精确验证 40/40] 独立复核 |
| $d\le p$、$q\ne n-r_1$、且 $A$ 在 $\mathcal V$ 内无特征向量 | **可行**（见证 = 任一顶层 $\Theta$）| 顶层定律：$(A)$ 自动 + $(S)$ 成立（数据 84/84）|
| $q=n-r_1$（$\ne$ 终端阶）| 顶层**全坏**；可行性只能来自**薄层**（$r<d$）| 互补障碍 + 顶层定律 |
| $d>p$ | 没有顶层；全部是薄层 | $\operatorname{rank}(CAZ)\le p<d$ |

**意义**：`DEC-$\Theta$` 里"$\exists\Theta$"真正需要搜索的只剩**薄层**（$r<d$）——顶层的情形被两个纯整数条件
（$q=n_0-p$ 或 $q\ne n-r_1$）直接决定。这与专家 Phase II 里"族维数决定难度"的判断一致。

## 阶谱"猜想"（**2026-10-30 已被 R17 推翻**，见 [R17](../refuted/README.md)）

**猜想**（功能可观测前提下）：
$$\text{可行阶}\ =\ \{n_0-p\}\ \cup\ \{q:\ d\le p\ \text{且}\ q\ne n-r_1\}.$$
（$d=n-p-q$；"$d\le p$"即 $q\ge n-2p$，此时顶层非空。）

> **已被 R17 推翻**（[R17](../refuted/README.md)、[c235](../layer_program/c235_order_refute_v2.py)）：
> $n=8$、$p=2$、$r_1=4$ 的构造性实例在 $q=2$（$d=4$）与 $q=3$（$d=3$）上都有 $(A)\wedge(S)$ 的点，
> 满足 $q<n_0-p=4$、$d>p$、$Z\not\subseteq\mathcal V$、功能可观测。
> 下面列出的证据只说明"多数情形如此"，**不再是断言**。

**证据**：

| 检验 | 结果 |
|---|---|
| P2 例子（$n=8,p=2,r_1=4,n_0=7$）：预测可行 $=\{5\}$ | 与 $\nu_{\min}=5$ 一致 ✓ |
| R15 例子（$n=5,p=1,r_1=2,n_0=2$）：预测可行 $=\{1\}$ | 与"只有 $q=1$ 可行"一致 ✓ |
| 随机实例逐阶比对（[c225](../layer_program/c225_order_conjecture.py)）| **一致 53、不一致 0**；薄层（$d>p$）69 个跳过 |

**新族（幂零不可观测块，全阶穷举）**：$n=5$、$p=1$、$C=e_1$、$A=\operatorname{diag}\!\big(\binom{0\ 1}{0\ 0},J_3\big)$、$L_0=e_2$。
$r_1=2$、$n_0=2$ ⟹ $n_0-p=1$、$n-r_1=3$；$d=4-q$。猜想预测可行阶 $=\{1\}\cup\{q: d\le1,\ q\ne3\}=\{1,4\}$。

| 阶 | $d$ | $(A)$ | $(S)$ | 猜想 | 一致？ |
|---|---|---|---|---|---|
| 1（$=n_0-p$）| 3 | ✓ | ✓ | 可行 | ✓ |
| 2 | 2（$>p$）| ✓ | ✗ | 不可行 | ✓ |
| 3（$=n-r_1$）| 1 | ✓ | ✗ | 不可行 | ✓ |
| 4 | 0 | ✓ | ✓ | 可行 | ✓ |

⟹ 该族**全阶穷举**与猜想 4/4 一致；且 $q=2,3$ 的薄层 $(A)$-点存在但 $(S)$ 全失败（"薄层可 $(A)$ 但谱坏"）。

**薄层大搜索**（块对角族、30 个随机实例、所有 $d>p$ 的阶、所有图表网格点）：
检查 **675** 个 $(q,Z)$ 点，$(A)\wedge(S)$ 成立 **0** 个 ⟹ 阶谱猜想的"薄层不可行"部分**无反例** ✓
（这是 `[精确验证]`，不是证明；薄层 $(A)$ 极稀，网格可能不全）。

**安全版复搜**（[c228](../layer_program/c228_thin_bigsearch.py)，用 `apply_col` 的列作用、**排除终端阶** $q=n_0-p$）：
$n=5,6$、块对角族 14 个实例、$d>p$ 的非终端阶：$(A)$-点 **38** 个，$(A)\wedge(S)$ 成立 **0** 个 ✓。
（过程记录：未排除终端阶时曾命中 1 个点，但那是 $q=n_0-p$（P2 Thm 7 保证可行），**不构成反例**。）

**R16 已撤回**（"$q=n-r_1$ 可行"的反例是行/列作用 bug；按列作用复检无反例）——见 [R16](../refuted/README.md)。

## 薄层谱坏的**定理**（$A\mathcal V\subseteq\mathcal V+Z$ 情形，2026-10-30）

**定理**：设 $Z\subseteq\mathcal V$、$A Z\subseteq Z$、且 $A\mathcal V\subseteq\mathcal V+Z$。若 $\dim\mathcal V>\dim Z$，则 $(S)$ 失败。

*证明*：考虑 $T_\lambda:\mathcal V/Z\to(\ker C)/Z$，$T_\lambda(v\bmod Z)=(\lambda I-A)v\bmod Z$。
由 $A\mathcal V\subseteq\mathcal V+Z$，$T_\lambda=\lambda I-\bar\Phi$，其中 $\bar\Phi$ 是 $\mathcal V/Z$ 上的**自同态**；
$(\lambda I-A)v\in Z$ 且 $v\notin Z$ $\iff T_\lambda$ 奇异 $\iff\lambda$ 是 $\bar\Phi$ 的特征值。
$\bar\Phi$ 在 $\mathbb C$ 上必有特征值 $\lambda_0$ ⟹ $T_{\lambda_0}$ 奇异 ⟹
$\dim\{v\in\mathcal V:(\lambda_0I-A)v\in Z\}>d$ ⟹ $\operatorname{rank}P(\lambda_0)<h$ ⟹ $(S)$ 失败 ✓。

**边界**：$\dim\mathcal V=\dim Z$（即 $Z=\mathcal V$）时 $T_\lambda$ 定义在零空间上，定理不适用——事实上此时 $(S)$ **成立**
（$P(\lambda)$ 的列空间恒为 $\mathcal V$）。这正是 R16 想说的"例外"，但它不在非终端阶、也不满足 $Z\subsetneq\mathcal V$。

**实例**（$n=6$、$p=1$、$q=2$、$V=\ker[C;CA]$、$Z=\ker[C;L_0]$、$AZ\subseteq Z$、$A\mathcal V\subseteq\mathcal V$）：
精确 gcd 次数 $=1$ ⟹ $(S)$ 失败 ✓ 与定理一致。

**等级**：**[Lean]**（端同态核心）—— [tools/lean/MyProof/TheoremC.lean](../../trash/lean_removed_2026-11-19/tools/lean/MyProof/TheoremC.lean)，
`lake env lean` 退出码 0（2026-10-30）。Lean 陈述：
`theoremC_endomorphism [IsAlgClosed K] [FiniteDimensional K U] [Nontrivial U] (B : U →ₗ[K] U) :
∃ lam, ¬ Function.Injective (lam • id - B)`。
**覆盖范围**：Lean 只覆盖"自同态 ⟹ 存在 $lam$ 使 $lam\cdot\mathrm{id}-B$ 不单射"这一步（代数核心）；
"$T_\lambda$ 何时是自同态（$A\mathcal V\subseteq\mathcal V+Z$）"与"奇异 ⟹ $\operatorname{rank}P<h$"两步仍是纸面。

### 开放：$A\mathcal V\not\subseteq\mathcal V+Z$ 的情形

此时 $T_\lambda=\lambda\iota-\Psi$ 不是自同态（$\Psi(v)=Av\bmod Z$ 可能落在 $\iota(\mathcal V/Z)$ 之外），
上述特征值论证失效。**判据变成**：
$$(S)\ \text{成立}\iff \forall v\in\mathcal V\setminus Z,\ \forall\lambda:\ Av-\lambda v\notin Z\iff \forall v\notin Z:\ Av\bmod Z\not\propto v\bmod Z .$$
即"$\Psi$ 没有与 $\iota$ 成比例的方向"。构造这样的例子需要 $\mathcal V\ne\ker C$（否则 $A\mathcal V\subseteq\ker C$ 会把结构锁死）；
**未找到例子、也未证明不存在** ⟹ 阶谱猜想的完整证明仍缺这一块。

**注意**：$d>p$ 的阶（薄层）不在本观察的覆盖内（那里 $(A)$ 是薄条件，随机采样测不到）；
R14/R15 的中间阶（$d>p$）全坏，与该猜想不矛盾但**未被它解释**。

**薄层探针**（[c226](../layer_program/c226_thin_probe.py)，块对角族：$n=5,n_1=2$、$C$ 杀掉块 2）：
枚举 $q=2$（$d=2>p$）与 $q=4$（$d=0$）的所有 $Z$，共 308 个点；找到 $(A)\wedge(S)$ 的点 **11 个**，
**全部在 $q=4$（$d=0\le p$）**，$q=2$ 的薄层点**一个也没有** ⟹ **不构成对猜想的反驳** ✓。
（过程更正：脚本第一版把"找到 11 个点"直接判成"猜想被推翻"，是把 $d=0\le p$ 的点误当薄层——已改。）

## R17 之后的图景（2026-10-30）

**R17 已推翻阶谱猜想**（[R17](../refuted/README.md)）：薄层的非终端阶**可以**可行。已知：

- **必要**：$q>t$（Theorem D）；
- **可行集很薄**：在 R17 实例上随机取 $Z$（每阶 80 个），**一个可行点都没有**（[c236](../layer_program/c236_spectrum_scan.py)）；
  之前找到的两个点是**特定构造**：$q=2$ 时 $Z=\operatorname{span}(e_4,e_5,e_6,e_8)$、
  $q=3$ 时 $Z=\operatorname{span}(e_4-e_7-e_8,\ e_5,\ e_6)$（3 个生成元，$d=3$；[c243](../layer_program/c243_r17_verify.py) 独立核对）。
- **共同机制**：$Z$ **避开 $\mathcal V$ 的"特征方向"** $e_3,e_7$——于是
  $T_\lambda(e_3)=(\lambda e_3-e_7)\bmod Z\ne0$ 对一切 $\lambda$ 成立 ⟹ $T_\lambda$ 恒单射。
  若 $Z$ 含 $e_3$（或 $e_7$），则 $\lambda=0$（或 $\lambda\to\infty$）处 $T_\lambda$ 塌缩 ⟹ $(S)$ 失败。

**待验证的新猜想**：$(S)$ 成立 $\iff$ $q>t$ 且 $T_\lambda$ 恒单射（等价地：$Z$ 不含 $\mathcal V/\mathcal V\cap Z$ 的特征方向）。
这需要写成不依赖 $\Theta$ 的判据。

### $(A)$-轨迹按 $r=\operatorname{rank}(CAZ)$ 分层（2026-10-31）

在 R17 实例、$q=3$（$d=3$）上采样 400 个 $Z$（[c246](../layer_program/c246_A_locus.py)）：

| $r$ | $(A)$ 成立的点 | 其中 $(S)$ 成立 | $Z\subseteq\mathcal V$ |
|---|---|---|---|
| 1 | 0（3 个点全失败）| — | — |
| 2 | **54** | **0** | 否 |

而 R17 的可行点 $Z=\operatorname{span}(e_4-e_7-e_8,e_5,e_6)$ 的 $r=1$ ⟹ 它落在**另一个层**。
⟹ **$(A)$-轨迹在不同 $r$ 层上的 $(S)$ 行为不同**：$r=2$ 层上采样点全坏，$r=1$ 层上存在可行点。
这支持专家的观点："不能假设非空就是整个分支"，必须**分层**讨论。

**R17 可行点是否孤立？**（[c247](../layer_program/c247_r17_perturb.py)，在 $K_L$ 内加 $\pm2/7$ 的扰动，60 次）：

| 扰动后 | 个数 | $(A)$ | $(S)$ |
|---|---|---|---|
| $r=1$ | 2 | 否 | 是 |
| $r=2$ | 54 | 否 | 否 |
| $r=2$ | 4 | 是 | 否 |

$\operatorname{rank}(CAZ)$ 一扰动就跳到 2，而 $r=2$ 层上 $(A)$ 点全坏 ⟹ **R17 的可行点在样本范围内是孤立的**
（不构成正维族）。这与"薄层可行集是薄集"的图景一致，但也意味着它是**特殊点**而非一般现象。

### 有限域点计数：$(A)$-轨迹的维数分层（2026-10-31，[c249](../layer_program/c249_finite_field.py)）

在 R17 实例、$q=3$、$d=3$ 的一个 chart（6 个参数）上，于 $\mathbb F_p$ 枚举全部参数点：

| $p$ | 参数点 | $(A)$ 成立 | 其中 $r=1$ | 其中 $r=2$ |
|---|---|---|---|---|
| 3 | 729 | 256 | 16 | 240 |
| 5 | 15625 | 3408 | 48 | 3360 |
| 7 | 117649 | 18240 | 96 | 18144 |

按 $p^D$ 拟合：**$r=2$ 部分 $D\approx5$（chart 的 6 维里一张超曲面）**，**$r=1$ 部分 $D\approx2$**。

⟹ **$(A)$-轨迹是可约的**，至少两层：大的 $r=2$ 超曲面 + 的 $r=1$ 二维族；
这与 c246 的观察（$r=2$ 层全坏、可行点在 $r=1$ 层）吻合，也印证专家"不同分支行为不同"的判断。

### **更正**：R17 的可行点**不孤立**——它是一个**二维族**（2026-10-31）

边界 chart（$c=0$）的符号计算（[c251](../layer_program/c251_boundary_chart.py)）：$(A)$ 的 $4\times4$ 子式化为
$\pm ab,\ \pm b^2,\ \pm b(a\mu+1)$ ⟹ **$(A)\iff b=0$**。于是得到显式族
$$Z(a,\mu)=\big[e_4+a e_7+\mu a e_8,\ \ e_5,\ \ e_6\big],\qquad (a,\mu)\ne(0,0),$$
其商铅笔 $T_\lambda=\begin{pmatrix}\lambda&0\\0&\lambda+\frac1{a\mu}\\-1&1/\mu\end{pmatrix}$ 的极大子式 gcd $=1$ ⟹ **$(S)$ 恒成立**。

**数值核对**（5 组 $(a,\mu)$）：全部 $r=1$、$(A)$ ✓、$(S)$ ✓。

> **这推翻了本文件上一节的"孤立"结论**（c247）：c247 的扰动同时动了 $z_2=e_5$、$z_3=e_6$，把 $(A)$ 破坏了；
> 真正的族固定 $e_5,e_6$，只让 $z_1$ 在 $e_7,e_8$ 方向动。**薄层可行集可以含正维族**。

**族的边界（2026-10-31 探测）**：形式不能随意换。

| 形式 | $(A)$ | 说明 |
|---|---|---|
| $[e_4+a(e_7+\mu e_8),\ e_5,\ e_6]$ | ✓ | 已知族（$z_1$ 带外界分量，$e_5,e_6$ 是 $A$-不变方向）|
| $[e_4,\ e_5+a(e_7+\mu e_8),\ e_6]$ | ✗ | 外界列换成 $z_2$ 后，$\ker(CAZ)$ 变成 $\operatorname{span}(z_1,z_3)$，而 $A z_1=Ae_4=e_8\notin\operatorname{im}Z$ |
| $[e_4,e_5,e_6,\ e_4+a(e_7+\mu e_8)]$（$q=2,d=4$）| ✗ | 同上：$A e_4=e_8\notin\operatorname{im}Z$ |

⟹ 族的存在依赖"哪些列落在 $\ker(CAZ)$ 里"与"它们的 $A$-像是否留在 $\operatorname{im}Z$ 内"，
不是简单的"一列在外、其余在内"。

> **更正（QA13，专家指出）**：上文"该 chart 内 $r=1$ 的 $(A)$-点恰好是这族"**错误**。
> 漏掉了分支 $a=b=c=0$、$(d,e,f)\ne(0,0,0)$（chart 分析里假设了 $(a,b,c)\ne0$）。
> 该分支的 $(A)$ 条件是 $d\ne0$、$e(d+1)=0$、$f(d+1)=0$（[c253](../layer_program/c253_missing_branch.py) 逐点验证 ✓），
> 且该分支上所有 $(A)$-点**全部 $(S)$ 失败**。反例 $Z_*=\operatorname{span}(e_4-e_8,e_5,e_6+e_8)$ 已验证：
> $CAZ_*=\begin{pmatrix}0&0&0\\-1&0&1\end{pmatrix}$、$(A)$ ✓、gcd 次数 1。
> 所以 $r=1$ 的 $(A)$-轨迹 = 二维可行族 $\cup$ 该谱坏分支。

**专家的核心引理**（已验证）：$Z\subseteq W=\ker C$ 时
$$\ker(CAZ)=Z\cap\mathcal V=S,\qquad \operatorname{rank}(CAZ)=d-\dim S,\qquad (A)\iff A(S)\subseteq Z .$$
它把辅助的 $R_Z$ 从几何问题里消掉，应作为后续的核心工具。

### 关联分层纤维维数公式（专家 QA13，**QA14 更正**）

> **更正（QA14）**：一般 $V\not\subseteq H$（R17 中 $\dim(V+H)=6\ne5$），所以 $V/S$ **不是** $H/S$ 的子空间；
> 横截对象应为 $B_S=(V\cap H)/S$（[c256](../layer_program/c256_incidence_fix.py) 核实）。

固定 $S\subseteq V\cap H$（$s=\dim S$、$r=d-s$），$B_S=(V\cap H)/S$（$b=\dim B_S$）、
$T_S=(A(S)+S)/S\subseteq H/S$（$k=\dim T_S$）、$m=\dim(H/S)$。则纤维
$\{Z:\dim Z=d,\ Z\subseteq H,\ Z\cap\mathcal V=S,\ A(S)\subseteq Z\}$ 的维数为
$$\boxed{(r-k)(m-r)},\qquad\text{可非空条件}\ \boxed{r\le m-b}.$$

**R17 上的两个实例核对**（[c255](../layer_program/c255_incidence.py)、[c256](../layer_program/c256_incidence_fix.py)）：

| $S$ | $s$ | $r$ | $b$ | $k$ | $m$ | 公式 | 实际 |
|---|---|---|---|---|---|---|---|
| $\operatorname{span}(e_5,e_6)$（二维族）| 2 | 1 | 1 | 0 | 3 | **2** | 2 ✓ |
| $\operatorname{span}(e_5,e_4+e_6)$（专家反例）| 2 | 1 | 1 | 1 | 3 | **0** | 0 ✓ |

⟹ 公式与两个分支都吻合：$k=0$ 时族自由（2 维），$k=1$ 时被 $A(S)$ 钉死（0 维）。

> **再更正**：上文"该 chart 内 $r=1$ 的 $(A)$-点**恰好就是**这族"的说法**已被专家 $Z_*$ 反例否定**——
> 还有 $a=b=c=0$ 的分支（$d\ne0$、$e(d+1)=0$、$f(d+1)=0$，全部谱坏）。正确表述见本节上方的更正块。

**族在 $\mu=0$ 的边界仍可行**（$Z=[e_4+a e_7,\ e_5,\ e_6]$，$a=1,2,-1$ 全部 $(A)\wedge(S)$ ✓）。
所以在 $c=0$ 这个 chart 内，$r=1$ 的 $(A)$-点**恰好就是**这族 $\{(a,\mu):a\ne0\}$（2 维），
且 $(S)$ 在整族上成立 ⟹ **该 chart 内 $r=1$ 层的可行部分 = 全部 $(A)$ 点**。
这与 [c249](../layer_program/c249_finite_field.py) 的有限域计数（$r=1$ 部分 $\sim p^2$）一致。

**不同阶的对比（2026-10-31 探测）**：

| 阶 | $d$ | 可行情形 | $\dim$ |
|---|---|---|---|
| $q=3$ | 3 | 族 $[e_4+a e_7+\mu a e_8,\ e_5,\ e_6]$ | **2** |
| $q=2$ | 4 | 只有 $[e_4,e_5,e_6,e_8]$（变体 $[e_4,e_5,e_6,e_8+a e_7]$ 会破坏 $(A)$）| 0（单点）|
| $q=1$ | 5 | $[e_4,e_5,e_6,e_7,e_8]$：$(A)$ ✓ 但 $(S)$ 失败（gcd 次数 1）| — |

⟹ **维数随阶变化**，没有简单的统一公式：$q=3$ 时"外界列"在 $\ker(CAZ)$ 之外故自由，
$q=2$ 时 $\ker(CAZ)$ 含 $e_4$、而 $Ae_4=e_8$ 必须落在 $\operatorname{im}Z$ 里，于是外界列被钉死为 $e_8$。

**但 $(S)$ 在 $r=1$ 层上也非处处成立**：$\mathbb Q$ 上采样 3000 点，$r=1\wedge(A)$ 只有 2 个，**都 $(S)$ 失败**
（R17 的人造点在同一个 $r=1$ 层却成功）⟹ $(S)$ 在 $r=1$ 层上仍有正余维的坏集。

### $r=1$ 层的符号计算（sympy，[c250](../layer_program/c250_r1_stratum.py)）

在 chart $c\neq0$ 内（$Z$ 的第三列 = $e_6+c e_7+\lambda c e_8$），$r=1$ 参数化为 $(d,e,f)=\lambda(a,b,c)$，
$(A)$ 的 $4\times4$ 子式化简后只含因子
$$a,\quad b,\quad c,\quad a\lambda+1 .$$
由于 $c\neq0$ 与本 chart 矛盾，唯一自洽分支是 $a=b=0$，但此时 $a\lambda+1=1\ne0$ ⟹ **该 chart 内没有 $(A)$-点**。
这与 R17 的可行点位于 $c=0$ 的**边界 chart** 一致 ⟹ **$(A)$-轨迹的分支依赖 chart**，必须逐 chart 或整体处理。

### 算法：在**商铅笔**上做 gcd（比大铅笔小得多）

由商铅笔恒等式，$(S)\iff\operatorname{rank}(\lambda\iota-\bar A)=t\ \forall\lambda$。
所以可以把极大子式 gcd 从 $n\times((n-r_1)+d)$ 的**大铅笔**搬到 $t\times q$ 的**商铅笔**上：

- $T(\lambda)$ 的第 $j$ 列 = 把 $\lambda u_j-Au_j$ 在 $K_b$（$\ker C$ 的基，前 $d$ 个是 $Z$）下展开后的 $w$-分量；
- $T$ 的元素对 $\lambda$ 是**一次**的（$\lambda u - Au$ 插值两次即可精确得到）；
- $(S)\iff$ $T$ 的 $t\times t$ 极大子式 gcd 次数 $=0$。

**对拍**（[c238](../layer_program/c238_quotient_gcd_symbolic.py)）：

| 实例 | 大铅笔 | 商铅笔 | 一致？ |
|---|---|---|---|
| R17 的可行 $Z$（$q=2$）| gcd 次数 0 | $t=1,q=2$，次数 0 | ✓ |
| P2 例子 $q=4$（一个 $(A)$-点）| $8\times6$，次数 4 | $t=4,q=4$，次数 4 | ✓ |

⟹ 层判定可以用**更小的矩阵**做，且与原来的判据等价（这是 `[已证]` 恒等式的直接推论 + 实例对拍）。

### 阶谱扫描器（$q>t$ 剪枝 + 商铅笔 gcd）

[c239](../layer_program/c239_spectrum_via_quotient.py) 把两步合起来：先用整数条件 $q>t$ 剪枝（Theorem D），
再在 $t\times q$ 商铅笔上算 gcd。三个实例的扫描：

| 实例 | 参数 | 可行阶（扫描） | 与已知一致？ |
|---|---|---|---|
| P2 例子 | $r_1=4$、$\dim\mathcal V=4$、$n_0=8$ | $\{5\}$ | ✓（$\nu_{\min}=5$）|
| R15 例子 | $r_1=2$、$\dim\mathcal V=3$、$n_0=2$ | $\{1\}$ | ✓ |
| R17 例子 | $r_1=4$、$\dim\mathcal V=4$、$n_0=6$ | $\{2\}$（$q=3$ 的可行点太薄，采样未命中）| 部分 ✓（$q=3$ 见 [c235](../layer_program/c235_order_refute_v2.py)）|

**注意**：扫描用随机/网格采样，**薄集会被漏掉**（R17 的 $q=3$ 点就是例子）；所以"未找到"不等于"不可行"。

## Theorem E（充分条件：横截 ⟹ $(S)$ 成立）

记 $\iota:\mathcal V/S\hookrightarrow\ker C/Z$、$\bar A:\mathcal V/S\to\ker C/Z$、$T_\lambda=\lambda\iota-\bar A$。

**定理 E**（在 $(A)$ 下）：若 $\bar A$ 单射且 $\operatorname{im}\bar A\cap\operatorname{im}\iota=0$，则 $(S)$ 成立。

*证明*：设 $T_\lambda x=0$。若 $\lambda\ne0$，则 $\lambda\iota(x)=\bar A(x)\in\operatorname{im}\iota\cap\operatorname{im}\bar A=0$ ⟹ $\iota(x)=0$ ⟹ $x=0$；
若 $\lambda=0$，则 $T_0=-\bar A$ 单射 ✓。$\square$

**等级**：**[Lean]** —— [tools/lean/MyProof/TheoremE.lean](../../trash/lean_removed_2026-11-19/tools/lean/MyProof/TheoremE.lean)，
`lake env lean MyProof/TheoremE.lean` 退出码 0（2026-10-30 实测）。
Lean 陈述：`theoremE (ι : V →ₗ[K] W) (A : V →ₗ[K] W) (hA : Function.Injective A)
(hdisj : Disjoint (LinearMap.range A) (LinearMap.range ι)) : ∀ lam, Function.Injective (lam • ι - A)`。

**与 Theorem C 的关系**：Theorem C 说 $A\mathcal V\subseteq\mathcal V+Z$（即 $\operatorname{im}\bar A\subseteq\operatorname{im}\iota$）且 $t>0$ 时必失败
——正是定理 E 条件的否定。于是
$$\operatorname{im}\bar A\subseteq\operatorname{im}\iota\ (t>0)\ \Rightarrow\ \text{必败};\qquad
\operatorname{im}\bar A\cap\operatorname{im}\iota=0\ \Rightarrow\ \text{必成};\qquad
\text{部分相交}\ \Rightarrow\ \text{未知（耦合型公根的来源）}.$$

**实例核对**（[c240](../layer_program/c240_theorem_E_check.py)，在 $\ker C/Z$ 的基下算 $\operatorname{im}\iota$ 与 $\operatorname{im}\bar A$）：

| 实例 | $t$ | $q$ | $\dim\operatorname{im}\iota$ | $\dim\operatorname{im}\bar A$ | $\bar A\subseteq\iota$？ | 横截？ | $(S)$ |
|---|---|---|---|---|---|---|---|
| c231（专家抽象例子）| 1 | 2 | 1 | 1 | 否 | **是** | 成立 ✓ |
| R17（$q=2$ 构造点）| 1 | 2 | 1 | 1 | 否 | **是** | 成立 ✓ |
| R15 族 $q=1$（$Z=\mathcal V$）| 0 | 1 | 0 | 0 | 平凡 | 平凡 | 成立 ✓ |

### 中间情形（部分相交）：抽象分析

**精确判据**（等价于 $(S)$ 本身）：$(S)$ 成立 $\iff$ 不存在 $x\ne0$ 使 $\bar A(x)\parallel\iota(x)$
（因为 $T_\lambda x=0\iff\bar A(x)=\lambda\iota(x)$，而 $\iota$ 单射故 $\lambda$ 由 $x$ 定）。

**两个抽象例子**（$t=2$、$q=3$、$\iota(x_1,x_2)=(x_1,x_2,0)$；[c241](../layer_program/c241_abstract_examples.py) 精确核对）：

| $\bar A(x_1,x_2)$ | $\operatorname{im}\bar A\cap\operatorname{im}\iota$ | $(S)$ | 原因 |
|---|---|---|---|
| $(x_1,\,0,\,x_2)$ | $\operatorname{span}(e_1)\ne0$ | **失败**（gcd 次数 1）| $\lambda=1$、$x=(1,0)$ 给 $T_1x=0$ |
| $(x_2,\,2x_1,\,x_2)$ | $\operatorname{span}(e_2)\ne0$ | **成立**（gcd 次数 0）| $\lambda x_1=x_2$、$\lambda x_2=2x_1$、$x_2=0$ 无 $x\ne0$ 解 |

> **更正**（2026-10-30）：本表最初把 $(x_1,0,x_2)$ 写成"成立"，是漏看了 $x_2=0$ 的方向（$T_1(x_1,0)=0$）。
> 精确复核后改为"失败"，并补上真正成立的例子 $(x_2,2x_1,x_2)$。

⟹ **部分相交并不决定成败**：要看 $\bar A$ 在"像落入 $\iota$"的子空间上是否与 $\iota$ 成比例。
所以 Theorem E 的横截条件是**充分不必要**；Theorem C 的包含条件是**充分**（在 $t>0$ 时）失败。

**观察者实例**（[c242](../layer_program/c242_partial_intersection.py)）：$n=6$、$p=1$、$C=e_1$、$Ae_6=e_1$（故 $\mathcal V=\operatorname{span}(e_2,e_3,e_4,e_5)$）、
$Z=\operatorname{span}(e_4,e_5)$（$s=2$、$t=2$、$q=3$）。两种情形都实现了：

| 例 | $Ae_2$ | $Ae_3$ | $\dim(\operatorname{im}\bar A\cap\operatorname{im}\iota)$ | $\bar A\subseteq\iota$？ | $(A)$ | $(S)$ |
|---|---|---|---|---|---|---|
| 失败 | $e_2$ | $e_3+e_6$ | **1** | 否 | ✓ | **失败**（gcd 次数 1）|
| 成立 | $2e_3$ | $e_2+e_6$ | **1** | 否 | ✓ | **成立**（gcd 次数 0）|

⟹ **中间情形在观察者问题里真实存在**，且两种结局都可能。
**注意**：这两例的 $q=3$ 超过了 $n_0-p=1$（P2 的阶范围之外）；所以它们证明的是"$(A)\wedge(S)$ 的代数结构"层面，
在 P2 的阶谱框架内是否允许这种 $q$ 仍需按他们的范围约定核对。


