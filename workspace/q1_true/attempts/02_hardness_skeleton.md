# Phase III 硬度归约：骨架

## 目标

把 $\mathrm{DEC}\text{-}\Theta$（给定 $(A,C,L_0)$ 与阶 $q$，是否存在图卡与 $\Theta$ 使 $(14a)\wedge(14b)$）归约到已知 $\exists\mathbb R$-hard 问题，
从而证明 $q1$ 强 hard。专家（QA9 §6）警告：**$(A)$ 不是任意多项式条件**，必须两段式。

## 设想与理由

$\mathrm{DEC}\text{-}\Theta$ 的自由量是 $\Theta$（图卡参数），约束是：
$$(A)\ \text{：秩条件（多项式等式）};\qquad (S)\ \text{：极大子式无公根（开条件）}.$$
$(S)$ 等价于"消元多项式 $R(\Theta)\ne0$"。若能把 ETR 的可行性编码成"$R$ 不恒为零"或"$R$ 在 $\Theta_0$ 处非零"，就得到归约。

## 做法（两段式）

**Stage 1：抽象铅笔。** 取 2 个极大子式
$$f_1(\Theta,\lambda)=\lambda+a(\Theta),\qquad f_2(\Theta,\lambda)=\lambda b(\Theta)+c(\Theta).$$
则 $\gcd(f_1,f_2)$ 非常数 $\iff c(\Theta)-a(\Theta)b(\Theta)=0$（公根 $\lambda=-a$）。**这是一个双线性方程**，可作为编码基元。

**Stage 2：把铅笔实现成 $[(\lambda I-A)\mathcal V\mid Z]$。**
注意 $\lambda[V\mid0]+[B\mid Z]$ 型铅笔**总能**实现：取 $A$ 满足 $A V=B$（$V$ 列满秩时总有解：在 $\operatorname{im}V$ 上按 $B$ 定义、其余任意）。
难点在 $(C,L_0)$ 把 $V=\ker[C;CA]$ 与 $Z=\ker[C;L_0]$ 钉死；以及 $(A)$ 条件 $\operatorname{rank}[Z,AZR]=d$ 必须可满足。

**可满足性的普查**（随机 $n=4,p=1,r=1$）：$(\dim V,\dim\ker[C;L_0],\ker[C;L_0]\subseteq V)$ 的分布
为 $(2,2,\text{否})$：595、$(3,2,\text{是})$：1（596 个实例）——即**一般情形 $Z\not\subseteq V$**。

### Stage 2 的部分刻画（已核验）

1. $V=\ker[C;CA]$、$Z=\ker[C;L_0]$；两者都含于 $\ker C$。
2. **$Z\subseteq V\iff\operatorname{row}[C;CA]\subseteq\operatorname{row}[C;L_0]$**
   （等价地 $\operatorname{rank}[C;CA;L_0]=\operatorname{rank}[C;L_0]$）—— **[精确验证 300/300]**。
   ⟹ 我们可以**通过选 $L_0$ 来控制 $Z\subseteq V$**（例如取 $L_0$ 含 $CA$ 的行模 $C$ 的分量）。
3. 铅笔的 $\lambda$-部分是 $[V\mid0]$；$A$ 只通过 $AV=B$ 进入，$V$ 列满秩时**恒可解**。
⟹ **可控的自由度**：$(V,Z)$ 的包含关系、$B$、以及 $Z$ 在 $\ker[C;L_0]$ 里的 $d$ 维子空间（$W$）。
**不可控**：$V$ 必须恰是 $\ker[C;CA]$（不是任意子空间）。

### Lemma（$Z\subseteq\mathcal V$ 时 $(A)$ 等价于不变性）

**若 $Z\subseteq\mathcal V$，则** $\operatorname{rank}[Z,AZR_Z]=d\iff AZ\subseteq Z$（$Z$ 是 $A$-不变子空间）。

*证明*：$Z\subseteq\mathcal V=\ker[C;CA]$ ⟹ $CAZ=0$ ⟹ $\ker(CAZ)=\mathbb R^d$ ⟹ $R_Z=I_d$ ⟹ $AZR_Z=AZ$；
于是 $\operatorname{rank}[Z,AZ]=d\iff AZ$ 的列落在 $\operatorname{im}Z$ 里 ✓。$\square$

这条解释了 $L_0=CA$ 的实例里"$(A)$ 恰好只对 $A$-不变的 $Z$ 成立"的现象（[c223](../../../proof/layer_program/c223_stage2_probe.py) 的探针：网格上 $(A)$ 全为假、$(S)$ 全为真）。

### Stage 2 探针（$L_0=CA$，$n=5,p=1,q=2$）的观察

- $Z\subseteq\mathcal V$ 由构造保证 ✓；
- 网格点上 $(A)$ **全部为假**（$Z$ 不是 $A$-不变的），而 $(S)$ 全部为真（gcd 次数 $0$）；
- 即：这个实例在探测范围内"$(A)$-空"，不能用它测试"坏集的多项式形状"——需要**构造 $A$-不变的 $Z$**（与 R14/R15 同法）。

### $d$ 与 $p$ 的分层（[c224](../../../proof/layer_program/c224_d_vs_p.py)，随机实例、精确 gcd）

$d>p$ 时 $\operatorname{rank}(CAZ)\le p<d$，"顶层自动"永远不适用 ⟹ $(A)$ 只能靠薄层满足。数据：

| 组 | $(A)$ 成立 | 其中 $(S)$ 成立 | 结论 |
|---|---|---|---|
| $d\le p$ | 124 | 48 | $(A)$ 在顶层**自动**成立（非薄）|
| $d>p$ | **0**（随机 $Z$ 采不到）| — | $(A)$ 是**薄条件**，随机采样必错过（CLAUDE §7.12）|

⟹ 对硬度归约的含义：**$d>p$ 的阶**是"薄 (A)"的天然场所；若 Stage 1 的 gadget 要在薄集上生效，
必须像 R14/R15 那样**显式构造**（利用 $A$ 的不变子空间），而不能靠随机 $\Theta$。

## 进展

- 骨架成形：Stage 1 的基元（双线性）与 Stage 2 的自由度（$A$ 可解 $AV=B$）都已明确；
- 尚未找到"用 $(C,L_0)$ 控制 $V,Z$ 同时让 $(A)$ 可满足"的构造。

## 最终结论

**未完成**：Stage 2 的构造（$(C,L_0)$ 的钉死效应）是缺口；Stage 1 的基元只给双线性方程，要编码一般二次系统需要更多子式且仍需 Stage 2。

## 放弃原因（若失败：具体到哪一步过不去）

（未放弃；本文件是设计稿。）

## 残留价值

- 记录了"$\lambda[V|0]+[B|Z]$ 恒可实现"这一自由度（Stage 2 的正面部分）；
- 普查给出随机实例中 $(V,Z)$ 的典型配置（$Z\not\subseteq V$），提示"钉死"约束可能很强。

## 相关文件

- [proof/h_bound/README.md](../../../proof/h_bound/README.md)（$(S)$ 的判据与障碍）
- [proof/spectral_locus/README.md](../../../proof/spectral_locus/README.md)（$\mathrm{DEC}\text{-}\Theta\in\exists\mathbb R$）
- [archive/expert_correspondence/QA9_2026-10-30.md](../../../archive/expert_correspondence/QA9_2026-10-30.md)（专家的 Phase III 建议）
