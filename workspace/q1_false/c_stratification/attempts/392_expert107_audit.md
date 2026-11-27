# 392 专家 107 号审计：我的纤维公式是错的；层号定为 $c=k-\rho$；先做 $K$-split 子类

> 送审件 [107](../../../for_expert/archive/107_c_ge_2_roadmap.md)（已归档），
> 答复 [107-reply](../../../for_expert/archive/107_c_ge_2_roadmap-reply.md)（851 行）。
> 总评：方向对（"the report identifies the right mathematical obstruction"），但**II.4 的纤维公式有根本矛盾**，
> 且"层号/层定义"必须先分开两套问题。

## 目标

1. 记录专家对 Q1–Q6 的裁决。
2. 承认并修正 **II.4 的纤维错误**（$D\subseteq V$ 与 $D\perp V$ 矛盾）。
3. 把反例补成**可独立核对的证书**（专家 §6 要求七项数据）。
4. 落实术语与路线（$K$-split 子类、$\mathcal I_2(M)$、rank 分层、六阶段路线）。

## 设想与理由

我在 107 里提出的两件事（层号用 $c_{\rm new}$、方向定理需要维度假设）方向被认可，但
**纤维公式写错了**：$D=\ker H=K\cap V^\perp$ 满足 $D\perp V$，所以 $V_0+D\subseteq V$ 不可能是对的。
专家的修法把这一点变成了一个更干净的结构：在 $K$-split 情形，$V$ 在 $K$ 内的分量由 $D$ **决定**，
自由的只有 $K^\perp$ 方向。

## 做法

1. 逐条读答复；2. 按其 §6 的七项要求重算反例（`c394`，修正交集的维数公式——我此前漏了 $\ker U$）；
3. 把两套纤维公式（full 与 $K$-split）写成正式陈述；4. 记录六阶段路线。

## 进展

### 1. Q1–Q6 的裁决

| 问 | 裁决 |
|---|---|
| Q1 层号 | **用 $c=k-\rho$**（几何层号）；把旧量改记为 **$t=q-\rho$**（环境行多余维数）；$q=\rho+t$、$t=q-k+c$。若行相关，则 $t:=\dim V-\rho$（用 $\dim V$ 而非 $q$） |
| Q2 维度假设 | **保留，但它是另一个问题**。分两个问题：**A**（完整 $c$-层，$D$ 不必不变）与 **B**（$K$-split $c$-层）。先做 B；**不要**用 B 的定义改掉 A，除非有归一化定理（可行解可换成 $K$-split 且不升阶、不破预设行）——**该定理未证** |
| Q3 $c=2$ 的底 | 对 B 而言正确：$\mathcal I_2(M)=\{D\in\operatorname{Gr}(2,K):M(D)\subseteq D\}$，再按 $r(D)=\rank(A_{21}|_D)\in\{0,1,2\}$ 分三层，$\dim(D+AD)=2+r(D)$ |
| Q4 纤维 | **错**（$D\subseteq V$ vs $D\perp V$）。正确：full 用 (9)，$K$-split 用 (14)（见下） |
| Q5 分量/次数 | 有行列式表述但**没有通用公式**：$\mathcal D_s$ 的映射 $(d_1,d_2)\mapsto d_1+Ad_2$ 不是一般丛映射；$\mathcal I_2(M)$ 依赖 $M$ 的 Jordan 结构。$c=2$ 的实用路线：先算 $M$ 的实 Jordan 型 → 逐个谱型写不变 2-平面 → 加 $A_{21}$ 的秩条件 → 算分量与实点 |
| Q6 我的 II.3 | **正确、证明完整**（非退化用欧氏内积）；但要把它写成 $K$-splitting 条件，并**用完整的 $A_{21}$ 块核验反例** |

### 2. 我的错误与修正（最重要的部分）

**II.4 的纤维** $\{V : V_0+D\subseteq V\subseteq(D+AD)^\perp\}$ **是错的**：$D=\ker H=K\cap V^\perp$ 蕴含 $D\perp V$，
所以 $D\subseteq V$ 只在 $D=0$ 时可能。

**正确的两个纤维**：

- **full 问题**：$\mathcal F_D=\{V\in\operatorname{Gr}(q,(D+AD)^\perp):\ V_0\subseteq V,\ K\cap V^\perp=D\}$，
  其中"精确核"条件 $K\cap V^\perp=D$ 等价于 **$K\cap(D+AD)=D$**（必要性由 $(5a)$ 给出），
  非空还要求 $V_0\subseteq(D+AD)^\perp$、$\dim(D+AD)\le n-q$。
- **$K$-split 问题**（更强、几何更干净）：若 $V=(V\cap K)\oplus(V\cap K^\perp)$，则
  $$V\cap K=D^{\perp_K},\qquad V=D^{\perp_K}\oplus W,\quad W\subseteq T_D:=K^\perp\cap(A_{21}D)^\perp,$$
  $$\text{纤维}=\operatorname{Gr}\bigl(t-\dim W_0,\ T_D/W_0\bigr),\qquad W_0:=P_{K^\perp}(V_0),$$
  非空 $\iff\dim W_0\le t\le\dim T_D=\rho-r(D)$。

**术语修正**：不要叫 $A_{21}$ "nilpotent-like"——它是**从 $K$ 到 $K^\perp$ 的非对角耦合**（长方块、不是自同态）。

**$c=2$ 的分类提醒**（专家 §11）：实不变 2-平面 $D$ 的 $M|_D$ 有三种谱型——
两个实特征值、重根带 Jordan 块、**不可约实二次（复共轭对）**。最后一种说明 $c=2$ **不只是** $c=1$ 实特征向量
理论的二维版本：$M$ 在没有相关实特征向量时也能有实不变 2-平面。

### 3. 反例的完整证书（`c394`，已按专家 §6 的七项输出）

实例：4242，$K_0$ 上块换成 $\operatorname{diag}(1,1,2,3)$，$n=8,k=4$。$M=\operatorname{diag}(1,1,2,3)$、
$A_{21}$ 为 $n\times k$ 矩阵（脚本已打印）。取 $D=\operatorname{span}\{e_1{+}e_2,\ e_3{+}e_4\}$（**非** $M$-不变），
$U=D+AD$，$V=U^\perp$：

| 项 | 值 |
|---|---|
| $\dim(D+AD)$ | 3（$=2+\rank(A_{21}|_D)=2+1$） |
| $K\cap(D+AD)$ | $=D$（维数 2）✔ 精确核成立 |
| $q=\dim V$ | 5 |
| $\dim(K\cap V^\perp)$ | **2**（$=c$） |
| $\dim(V\cap K)$ | **1**（而 $\rho=2$）⟹ **不 $K$-split** |
| $\rank H=\rho$ | 2 |
| $AD\perp V$ | ✔ |

对照：$D=\operatorname{span}\{e_1,e_2\}$（$M$-不变）同样的构造给出 $\dim(V\cap K)=2=\rho$ ⟹ $K$-split ✔。

**所以**：存在满足 $(5a)$、$c=2$、精确核成立的设计，其 $\ker H=D$ **不是** $M$-不变——
方向定理离开 $K$-split 假设确实是假的；反例的七项数据现在可独立复核。

### 4. 六阶段路线（专家 §15–§16、Part IX）

1. **修定义**：$c=k-\rho$、$t=q-\rho$；明确 $\dim V=q$ 是否假设；改 $\omega$ 与 $\dim(V\cap K)$ 的关系；把维度假设改称 $K$-split；检查 $c=1$ 论文里每处 $\omega=\dim(V\cap K)$ 是否有构造支撑。
2. **分开两个问题**（full / $K$-split），明确下一篇研究哪个（建议 $K$-split）。
3. **重建纤维**（用上面的 (9) 与 (14)）。
4. **补齐 $c=2$ 的底几何**：$\mathcal I_2(M)$ + rank 分层；先做三种谱情形（实单谱 / 对角重根 / Jordan 块或非实共轭对）。
5. **再引入 $(5b)$**：有限图卡覆盖（含方向变量）、分量/可约性、满秩首项系数条件、函数域 gcd、实点。
6. **最后才谈复杂度**：先有精确 $c=2$ 判定，再数图卡数、次数、高度。

**专家点名的"最有价值的下一步结果"**：

> **定理（$K$-split $c=2$ 设计族的结构）**：在 $K$-split 条件下，每个可容许压缩核 $D$ 是 $K$ 的
> $M$-不变 2-维子空间；在 $\rank(A_{21}|_D)$ 的每个常秩层上，与预设行相容的行空间选择构成相对
> Graßmann 丛，铅笔条件在其上选出可行子集。

## 最终结论

1. **我的纤维公式是错的**（$D\subseteq V$ 与 $D\perp V$ 矛盾），已按专家给的两个公式改正；
2. 层号定为 **$c=k-\rho$**，旧量改记 **$t=q-\rho$**；
3. 先把 **$K$-split 子类**做出来（问题 B），full 问题（A）保留为目标，需要归一化定理；
4. 反例已补成七项数据的证书；
5. 下一步 = 专家点名的"$K$-split $c=2$ 结构定理"。

## 放弃原因

- 没有动手证"$K$-split $c=2$ 结构定理"（本轮只做定义修正与证书）；
- 没有证明 $K$-split 归一化定理（专家明确说 107 没有建立它）；
- 没有算 $\mathcal I_2(M)$ 的分量（依赖 $M$ 的实 Jordan 型，下一步）。

## 残留价值

- **两个正确的纤维公式**（full 与 $K$-split），可直接进下一篇论文；
- **反例的七项数据证书**（可独立复核；并修正了交集维数的算法错误——漏了 $\ker U$）；
- **六阶段路线**与专家点名的下一步定理；
- 术语：非对角耦合（不是 nilpotent-like）、$K$-split 行空间、$\mathcal I_2(M)$、$t$ 与 $c$。

## 相关文件

- [attempts/391](../../decision_algorithms/attempts/391_c_gt_1_entry.md)（$c\ge2$ 入口：三个量、方向定理、对齐表）
- [attempts/390](390_hyperplane_lean.md)（$c=1$ 的 Lean）
- [c394](../../../../tools/verification/c394_c2_certificate.py)（反例证书）、[c392](../../../../tools/verification/c392_language_alignment.py)（三量对照）、[c391](../../../../tools/verification/c391_c2_direction_check.py)（四例）
- 专家问答：[107 与回复](../../../for_expert/archive/)
