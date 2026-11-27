# A.1 · 维数分解与下界

> **对应 docs**：[docs/02](../../docs/02_theorems_proven.md) 的 `A.1` 条目（§0.1 归并表）。

## 命题

**A.1（a）〔原 A.0〕（$(5a)$ 的商形式——**再次校正**）** 记 $\mathcal J=\operatorname{row}[C;CA]$、$U=\pi(\mathcal V)$、$B=\pi(\mathcal J A)$。
则
$$(5a)\iff \pi(\mathcal V A)\subseteq\pi(\mathcal V).$$

## 纸面证明

*证明*：$(5a)\iff\operatorname{row}(\mathcal L A)\subseteq\operatorname{row}\mathcal L+\mathcal J$，两边取 $\pi$。$\square$

**要点（曾两次写错）**：$\pi(xA)$ 在 $X=\mathbb C^n/\mathcal J$ 上**不是良定义的单值映射**，因为 $A(\mathcal J)\not\subseteq\mathcal J$；
这里的偏差恰好是 $B=\pi(\mathcal J A)$。因此正确说法是：

**与此相关的只有单向蕴含**：令 $\overline T:X/B\to X/B$ 由 $A$ 诱导（良定义，因为 $B=\pi(\mathcal J A)$）、
$\overline U=(U+B)/B$，则

$$\overline T(\overline U)\subseteq\overline U\iff\pi(\mathcal V A)\subseteq U+B,$$

而 $(5a)$ 是 $\pi(\mathcal V A)\subseteq U$ —— **更强**。于是只有
$$(5a)\ \Longrightarrow\ \overline T(\overline U)\subseteq\overline U .$$
**反向不成立**：此点由专家 2026-10-30 指出，但**本项目从未复现其反例**；按专家 2026-11-04 §8 的建议，
该否定陈述**先从证明链中撤下**，仅作为"待复核的记录"保留（若复现出来再写回）。
因此本文只使用上面的**单向蕴含**；"枚举 $\overline T$-不变子空间能否替代 $(5a)$"这个问题**保持开放**，
不作断言。$(5a)$ 依赖 $\mathcal V$ 的提升（在层框架里等价于 $\tau\in\mathcal A$，$\mathcal A$ 仿射）✓ ——
这一点不依赖上述否定陈述（它来自 $(5a)\iff\pi(\mathcal V A)\subseteq U$ 与 $U$ 只记录 $\pi(\mathcal V)$ 的维数）。



---

**A.1（b）〔原 A.1〕** 对任何解 $\mathcal L$：$q=\rho+c$，$\rho=\dim\pi(\mathcal V)$、$c=\dim(\mathcal V\cap\mathcal J)$。
*证明*：$0\to\mathcal V\cap\mathcal J\to\mathcal V\to\pi(\mathcal V)\to0$ 正合。

**A.1（c）〔原 A.2〕** $c\ge\max(c_0,1)$。（**$c_0$ 是项目内下界参数**，与文献 $q_0$ 的恒等式**未证**：$\min(f+g)\ne\min f+\min g$，需证同一配置同时达到两个最小值——专家 2026-11-01 §Q5.5。）
*证明*：$c\ge c_0$ 因 $S\subseteq\mathcal V$；$c\ge1$ 因若 $c=0$，$A$ 在 $\mathcal V$ 上诱导 $\varphi$，其特征向量 $v$ 给 $(\lambda I-A)v\in\mathcal J$，于是 $\dim((\lambda I-A)\mathcal V+\mathcal J)\le q-1+j<q+j$，与 $(5b)$ 矛盾。

（`Eigen.c_pos_of_five_b`：$V\ne0$、$V\cap J=\bot$、$AV\le V\sqcup J$ 与"$(5b)$ 对所有 $\lambda$ 成立"矛盾——
即 $c\ge1$ 那半；用 `Eigen.exists_eigenvector` 与 `Eigen.finrank_lt_of_eigenvector_mod`。
$c\ge c_0$ 是 $S\subseteq\mathcal V$ 的定义性事实）。

**A.1（d）〔原 A.3〕（下界）** $q_{\min}\ge\max(r+\varepsilon,\ \rho+\max(c_0,1))$。
*证明*：$q\ge r$；$L_0$ 非解时 $q\ge r+1$；再由 A.1、A.2。
`A3Bound.a3_rows` 给 $q\ge r$；`A3Bound.a3_epsilon` 给 $q\ge r+\varepsilon$（把"$L_0$ 非解"写成 $V_0\ne V$）；
`A3Bound.a3_rho` 给 $c\ge1\Rightarrow q\ge\rho+1$；`Eigen.c_pos_of_five_b` 从 $(5b)$ 给 $c\ge1$。
**未覆盖**：$\max(c_0,1)$ 里的 $c_0$——它需要 $S$ 的 $A$-侧最小维数（A.4/$P$ 的语言））。
**不紧**：[proof/refuted/](../refuted/README.md) R4 给出下界 3、真值 4 的实例（本例 $q_0=4$，**A.4 能补上**）。

**A.1（e）〔原 A.4〕（$q_0$ 下界，比 A.3 紧）** 记 $q_0:=\min\{\dim\mathcal V:\ \operatorname{row}L_0\subseteq\mathcal V,\ (5a)\}$（即条件 $(A)$ 下的最小维数）。则
$$q_{\min}\ \ge\ q_0\ \ge\ \max\big(r+\varepsilon,\ \rho_{ci}+\max(c_0,1)\big)\quad(\text{后一个不等式见 A.3}).$$
**$q_0$ 多项式可算**：对生成行 $g=(C_1,\dots,C_p,L_1,\dots,L_r)$ 按 $g_iA^q$（$q$ 递增、同幂次按 $i$）做**全局秩保留**，$\eta_j$ = 第 $j$ 个 $L$-生成行被保留的次数，$q_0=\sum_j\eta_j$。

*位置*：[tools/ledger/c208_q0_lower_bound.py](../../tools/ledger/c208_q0_lower_bound.py)、[proof/layer_program/c207_q0_eta.py](../layer_program/c207_q0_eta.py)（外部例子）。
**注意**：$q_0$ 只用到 $(5a)$，所以它是**无条件**下界；$q_{\min}-q_0$ 才是 $(5b)$ 要付的代价 —— 这与项目的层分解 $\rho+c$ 互补。
**待核（2026-11-02）**：定义级计算（$(5a)$ 下的精确最小 $\dim\mathcal V$，即"闭包"，见
[tools/verification/omega_construct.py](../../tools/verification/omega_construct.py) 的 `closure`）
在 $2/12$ 个实例上**严格大于** $\sum_j\eta_j$（$n=7$ seed 1000：$4$ vs $3$；seed 1001：$5$ vs $3$）。
可能是 c208 的淘汰规则过早，或"最小功能维数"与"最小行数"不是同一量。**未定论**；
在此之前，$(5a)$ 侧的下界取两者中**较大者**（闭包）。

## Lean

* 等级行引用的 Lean 声明：`A0Row.five_a_row_iff`、`A0Row.rank_eq_of_rowSpace_le`、`A3sem.finrank_inter_add_finrank_map_mkQ`
* 差在哪里：见等级行括注（内核一般只覆盖代数/维数骨架，矩阵实例化多为纸面）

## 精确验证

* 见等级行给出的精确验证数字。

## 状态与历史

*等级*：**[已证-纸面]** + **[Lean]**（`A0Row.five_a_row_iff`：$\operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C]\iff\operatorname{row}(\mathcal LA)\le\operatorname{row}[\mathcal L;CA;C]$，即本条的第一步；`A0Row.rank_eq_of_rowSpace_le`：包含 $\Rightarrow$ 秩等式。**差异**：不含再往后的商形式 $\pi(\mathcal V A)\subseteq\pi(\mathcal V)$）。
**等级**：定义性 $+$ **[Lean]**（`A3sem.finrank_inter_add_finrank_map_mkQ`：$\dim(T\sqcap B)+\dim(T/B)=\dim T$）。
**等级**：[已证]（**完整证明**：[proof/lower_bound/theorem.md](../lower_bound/theorem.md) §3）$+$ **[Lean]**
**等级**：[已证] $+$ **[Lean]**（维数部分：
*等级*：**[引用]**（arXiv:2609.33615, §II–III：$q_0=\sum_j\eta_j$ 是 $(A)$ 下的最小维数；本项目复核了它的算法与例子）+ **[精确验证 20/20]**（所有见证 $q_{\text{wit}}\ge q_0$；其中 **6/20 个实例 $q_0$ 比 A.3 更紧**）。
* 2026-11-06：按 docs/proof 分工契约，从 docs/02 迁入本卷宗（证明逐字保留）。





## 验证状态

| 维度 | 状态 |
|---|---|
| 数学 M | M3 |
| 形式 F | F3 |
| 导出等级 | **L4** |
| 完成判定 | **完成**（标准 2026-11-07：M≥3 即可；Lean 为加分项）—— Lean 已覆盖（字面） |


## 支撑目录

[lower_bound/](../lower_bound/README.md)、[base_family/](../base_family/README.md)

（本卷宗只汇总证据；支撑目录里的脚本与文档保持原位。）

## 专家复核意见（成立）

把"商等价"与"下界可达性"拆成两条：$(5a)\iff\pi(\mathcal VA)\subseteq\pi(\mathcal V)$ 本身不需要 $\mathcal L$ 行满秩或含 $L_0$；而 $q\ge\rho_0+c_0$ 只在下界各自成立时有效，$c\ge\max(c_0,1)$ 的**同时可达**不可作为 A.1 的一部分。


## 下界的**联合剖面**改进（专家第五轮 Q4）

原来写的是"两个下界相加"：
$$q_{\min}\ge\max\{r+\varepsilon,\ \rho+\max(c_0,1)\}.$$
专家的意见：这个式子把若干**独立取最小**的量相加，可能严格弱于真实的联合最小。正确的对象是**剖面**：

$$\mathfrak P:=\{(\rho(\mathcal L),c(\mathcal L)):\ \mathcal L\ \text{可容许}\},\qquad
\mathfrak P_{\rm spec}:=\{(\rho,c)\in\mathfrak P:\ (5b)\ \text{成立}\},$$
$$q_{\min}=\min_{(\rho,c)\in\mathfrak P_{\rm spec}}(\rho+c)\qquad\Bigl(\le\ \min_{(\rho,c)\in\mathfrak P}(\rho+c)\ \text{若}\ \mathfrak P_{\rm spec}\subseteq\mathfrak P\Bigr).$$
**方向说明（专家第六轮 §6.2 的更正）**：因为 $\mathfrak P_{\rm spec}\subseteq\mathfrak P$，故
$\min_{\mathfrak P}\le\min_{\mathfrak P_{\rm spec}}$，**不能**反写。两种一致写法：
① 若 $\mathfrak P_{\rm spec}$ 是**谱可行**候选的剖面，则 $q_{\min}=\min_{\mathfrak P_{\rm spec}}(\rho+c)$（等式）；
② 若 $\mathfrak P$ 是**放宽**的可行集，则 $\min_{\mathfrak P}(\rho+c)\le q_{\min}$（下界）。

**定义** $c_{\min}(\rho):=\min\{c:(\rho,c)\in\mathfrak P_{\rm spec}\}$（无则 $+\infty$）。则
$$\boxed{\ q_{\min}\ \ge\ \min_{\rho}\bigl\{\rho+c_{\min}(\rho)\bigr\}.}$$
由 F.1（秩屏障）可再加约束 $\rho\le r_*:=\min_\lambda r(\lambda)$，于是
$$q_{\min}\ \ge\ \min_{\rho\le r_*}\bigl\{\rho+c_{\min}(\rho)\bigr\}.$$

**为什么比加法界强**（专家给的例子）：若 $\mathfrak P=\{(2,5),(3,2),(4,1)\}$，则加法界给
$\rho_{\min}+c_{\min}=2+1=3$，而真实的 $\min(\rho+c)=\min\{7,5,5\}=5$。差距来自"$\rho$ 最小"与"$c$ 最小"
**不可同时达到**。

**现状与限定**：
* 这是**表述上的改进**，不是新的数值界——只有当 $c_{\min}(\rho)$ 被算出或给出上界时才有数值意义；
* $c_{\min}(\rho)$ 的闭式目前未知（B.28 的分层参数给了部分信息）；
* 本节不声称"加法界是错的"：加法界仍然成立，只是可能不紧。
