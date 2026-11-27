# $\mathrm{DEC}(q)\in\exists\mathbb R$（chart-free 编码，按 QA15 修订）

> **对应 docs 条目**：G.1（见 [docs/02](../../../../../docs/02_theorems_proven.md) §0.1 归并表）

**状态**：**[已证-纸面]**（编码、充要性、规模）+ 两实例精确验证 + 部分 Lean（见 §6）。
**修订依据**：[QA15](../../../../../archive/expert_correspondence/QA15_2026-10-31.md)（专家对本文档上一版的审阅）。

## 0. 位置

本目录证的是 $(5b)$ 的**下界方向**（$=\ h$，谱条件）的**判定复杂度上界** $\mathrm{DEC}(q)\in\exists\mathbb R$。
上界方向（$\le$，由 $(5a)$ 免费）在 [../5b_upper_bound/](../../../../../proof/5b_upper_bound/README.md)；命题间的整体关系见 [../README.md](../../README.md)。

## 1. 命题

给定有理矩阵 $A\in\mathbb Q^{n\times n}$、$C\in\mathbb Q^{p\times n}$（**行满秩**）、$L_0\in\mathbb Q^{r\times n}$
与整数 $q$，判定是否存在 $d=n-p-q$ 维子空间 $Z\subseteq H=\ker[C;L_0]$ 使
$$(A)\ \operatorname{rank}[Z,AZR_Z]=d,\qquad (S)\ \operatorname{rank}P_\Theta(\lambda)=h\ \ \forall\lambda\in\mathbb C .$$
记该判定问题为 $\mathrm{DEC}(q)$。**定理**：$\mathrm{DEC}(q)\in\exists\mathbb R$。

## 2. 核心引理（独立命名，QA15 建议）

**引理 1**：$Z\subseteq W=\ker C$ 时 $\ker(CAZ)=Z\cap\mathcal V=S$，故 $\operatorname{rank}(CAZ)=d-\dim S$，且
$$(A)\iff A(S)\subseteq Z .$$
**等级**：**[Lean]** —— [tools/lean/MyProof/CoreLemma.lean](../../../../../trash/lean_removed_2026-11-19/tools/lean/MyProof/CoreLemma.lean)（$\ker$ 部分，退出码 0）。

**引理 2（多项式左逆）**：$P(\lambda)=\lambda E-F$、$\operatorname{rank}E=t$。则
$$\operatorname{rank}P(\lambda)=t\ \forall\lambda\in\mathbb C\iff\exists X(\lambda):\ X(\lambda)P(\lambda)=I_t,\ \deg X\le t-1 .$$

**证明路线 A（主，QA21 §4.5）**：**Noferini–Van Dooren**（LAA 658, 2023）Lemma 5.2 给出矩阵铅笔的
**右逆**判据与次数界 $m-1$（$m$ = 行数）。对 $P(\lambda)^{\mathsf T}$（$t\times q$，在有限 $\lambda$ 满行秩）应用：
存在多项式 $R$ 使 $P^{\mathsf T}R=I_t$ 且 $\deg R\le t-1$。转置得
$$R(\lambda)^{\mathsf T}P(\lambda)=I_t,\qquad \deg R^{\mathsf T}\le t-1\ ✓$$
**已核对**（2026-10-31，读原文）：Lemma 5.2 的条件是"**无有限特征值、无左极小指标**"，对 $L=P^{\mathsf T}$
（$t$ 行、$q$ 列）逐条对应：无有限特征值 $=$ $P$ 在**有限 $\lambda$** 上秩恒为 $t$（即 $\mathbb C$ 上处处满列秩 ✓）；
无左极小指标 $=$ $\operatorname{rank}P=t$ over $\mathbb C(\lambda)$（满列秩自动成立 ✓）。次数界 $\le m-1=t-1$ ✓。
**路线 A 不再是"未经核对的引用"。**

**证明路线 B（备选，QA15 §5，保留作独立验证）**：归一化 $E\to\binom{I_t}{0}$，得 $\binom{\lambda I-B}{-D}$；
用**不可观测子空间** $\mathcal N=\bigcap_j\ker(DB^j)$（Cayley–Hamilton 保证 $B$-不变）证明与
$\operatorname{rank}[D;DB;\dots;DB^{t-1}]=t$ 等价；再取 $G_j$ 使 $\sum G_jDB^j=I_t$，用望远镜恒等式构造 $X$。

**机器核对（`c283`，2026-10-31）**：对铅笔 $P(\lambda)=P_0+\lambda P_1$，令 $X(\lambda)=\sum_j\lambda^jX_j$，
逐次幂解线性系统，求**最小可行次数** $D$：

| 实例 | $t$ | 最小 $D$ | 理论界 $t-1$ | 是否紧 |
|---|---|---|---|---|
| R17 商铅笔（`c268` 例 1）| 2 | **1** | 1 | ✓ 紧 |
| `c282` 实例 | 3 | **2** | 2 | ✓ 紧 |
| $t=1$ 简单铅笔 | 1 | **0** | 0 | ✓ 紧 |

⟹ 存在性与次数界在这三个实例上都被**精确算术**验证，且界是**紧**的。

> **等级**：引理 2 是 **[已证-纸面]**（路线 A 为标准定理的直接推论 + 转置论证；路线 B 为独立复核）。
> 它是承重引理，按 QA21 §3.1 的政策，**不应**只以"引用"形式出现——本文档的两条路线就是它的完整论证。

## 3. 编码（修订版）

记 $W=\ker C$（$\dim w=n-p$）、$V=\ker[C;CA]$（$\dim v$）、$H=\ker[C;L_0]$、$G=V\cap H$、$d=w-q$。
对 $s$ 取值 $0\le s\le\min(d,\dim G)$ 逐个析取（$O(n)$ 项）。

| 变量 | 尺寸 | 含义 |
|---|---|---|
| $S$ | $n\times s$ | $S=Z\cap\mathcal V$ 的基 |
| $Q$ | $n\times(v-s)$ | $\mathcal V$ 中 $S$ 的补 |
| $Y$ | $n\times(d-s)$ | $Z/S$ 的方向 |
| $K$ | $(v+d-s)\times n$ | 辅助左逆 |
| $G_A$ | $d\times s$ | $A(S)=[S\,Y]G_A$ |
| $R$ | $q\times w$ | 商映射（$W$ 坐标）|
| $J$ | $w\times q$ | $R$ 的右逆 |
| $A_Q^W$ | $w\times(v-s)$ | $AQ$ 在固定基 $W_0$ 下的坐标（**新增，QA15 §1.4**）|
| $X_0,\dots,X_{t-1}$ | $t\times q$ 各 | 左逆证书 |

### 约束

1. $K[S\,Q\,Y]=I_{v+d-s}$（列满秩；配合下面 2、3 得 $\mathcal V=S\oplus Q$、$Z=S\oplus Y$、$Z\cap\mathcal V=S$）；
2. $\operatorname{im}S,\ \operatorname{im}Q\subseteq\mathcal V$（**QA15 §1.1 要求显式写出**）；
3. $\operatorname{im}S,\ \operatorname{im}Y\subseteq H$；
4. $AS=[S\,Y]G_A$（$=A(S)\subseteq Z$，即 $(A)$）；
5. $R Z_W=0$、$RJ=I_q$（$\ker R=\operatorname{im}Z_W$）；
6. $W_0A_Q^W=AQ$（$AQ$ 的 $W$-坐标，**QA15 §1.4**）；
7. $X(\lambda)P(\lambda)=I_t$，$P(\lambda)=R(\lambda Q_W-A_Q^W)$（按 $\lambda$ 系数逐项相等）。

> **两条简化（QA15 §1.3）**：$\operatorname{rank}(RQ_W)=t$ **不必**列为约束——由 1、2、5 自动成立
> （若 $RQ_Wa=0$ 则 $Qa\in\ker R=Z$，又 $Qa\in\mathcal V$，故 $Qa\in Z\cap\mathcal V=S$，而 $\mathcal V=S\oplus Q$ ⟹ $a=0$）。
> **$t=0$ 情形（QA15 §6.1）**：$\mathcal V/S$ 零维、谱条件空，公式中不出现 $X_j$；$q\le t$ 的分支直接判假（QA15 §6.2）。

### 规模（**按 QA15 §7 更正**）

| 项 | 数量 |
|---|---|
| $S,Q,Y$ | $O(n^2)$ |
| $K$ | $O(n^2)$ |
| $G_A$ | $O(n^2)$ |
| $R,J,A_Q^W$ | $O(n^2)$ |
| **$X_0,\dots,X_{t-1}$** | \(t\cdot t\cdot q=t^2q=\) **$O(n^3)$** |
| 总变量 | **$O(n^3)$** |
| 方程（含 $X P=I_t$ 的系数匹配） | **$O(n^3)$** |
| 次数 | $\le t\le n$（$X P=I$ 的每个系数方程对 $X$ 线性、对其它变量二次）|

**系数比特长度**：基 $W_0$ 及 $\mathcal V,H$ 的有理基由有理 Gauss 消元给出；标准精确线性代数界保证其比特长度对输入比特长度多项式。
（QA15 §7：这句话要写出来，不能只说"有理基变换"。）

## 4. 充要性

- **必要性**：给定可行 $Z$，取 $S=Z\cap\mathcal V$、$Q$ 为补、$Y$ 为 $Z/S$ 的方向；1、2、3 成立；4 由引理 1；
  5 取 $R$ 为商映射；6 为坐标定义；7 由引理 2。
- **充分性**：给定满足 1–7 的变量，令 $Z=\operatorname{im}[S\,Y]$；由 1、2、3 得 $Z\subseteq H$、$\dim Z=d$、$Z\cap\mathcal V=S$；
  由 4 得 $(A)$；由 7 与引理 2 得 $(S)$。

## 5. 验证记录

| 实例 | 参数 | 检查 |
|---|---|---|
| R17 | $n=8,p=2,q=3,s=2,r=1,t=2$ | 3 个族点 × 7 项结构（[c260](../../../../../proof/layer_program/c260_encoding_check.py)）；左逆 1 点（[c259](../../../../../proof/layer_program/c259_chartfree_full.py)）|
| 第二实例 | $n=6,p=1,q=2,s=3,r=0,t=1$ | **10/10**（[c264](../../../../../proof/layer_program/c264_general_check.py)，含 $(S)$ 与左逆）|

**边界用例目录**（QA15 §8）：

| 用例 | 实例 | 状态 |
|---|---|---|
| $t=0$（谱条件空、无 $X_j$）| R15 型、$q=1$（[c265](../../../../../proof/layer_program/c265_boundary_cases.py)）| ✓ |
| $V\cap H=0$、$s=0$、$Z=H$、$q=t$（剪枝）| $n=5,p=2$（[c266](../../../../../proof/layer_program/c266_s0_case.py)）| ✓ |
| $q<t$ | **分支为空**（见下）| ✓ 已证 |
| $q=0$ | 需 $H=W$（即 $L_0\subseteq\operatorname{row}C$），此时 $t=0$ | ✓ 归入 $t=0$ |

**两条边界事实**（[已证-纸面]）：因 $\mathcal V,Z\subseteq W=\ker C$，
$$\dim(\mathcal V\cap Z)\ \ge\ \dim\mathcal V+\dim Z-\dim W\ =\ v-q,$$
故 $t=v-s\le q$。于是：

- **$q<t$ 的分支为空**（自动被 Theorem D 剪掉，无需单独处理）；
- **$q=t$** 只在 $s=v-q$ 时发生——正是 [c266](../../../../../proof/layer_program/c266_s0_case.py) 的实例（$(A)$ 成立、$(S)$ 失败，与 Theorem D 一致）。

数值核对：60 个随机实例上 $s_{\min}=v+d-w=v-q$ 无反例。

## 5.5 编码规模（G-2）

**[bitsize.md](bitsize.md)**：常数比特长 $O(n^2(B+\log n))$、变量/方程 $O(n^3)$、次数 $\le n$、
无除法电路表示；**[已证-纸面]** $+$ **[精确验证 12/12]**（[verify_bitsize.py](verify_bitsize.py)，只覆盖常数）。
依据：专家 2026-11-02 答复 §4.5 的四项要求。

## 6. Lean 覆盖

| 命题 | 文件 | 退出码 |
|---|---|---|
| 引理 1（$\ker(CAZ)=Z\cap\mathcal V$）| `CoreLemma.lean` | 0 ✓ |
| 左逆 ⟹ 单射、$\operatorname{rank}P=\dim V$ | `ExistsRLemmas.lean` | 0 ✓ |
| Theorem D/E/C 核心、商铅笔第一步 | `TheoremD/E/C.lean`、`QuotientPencil.lean` | 0 ✓ |

**未 Lean 化**：引理 2（PBH + 望远镜恒等式）、编码本身的完整形式化。
QA15 明确：**Lean 不是 ∃R 定理的前提**，但报告中**不能**说"整个编码已机器验证"。

## 7. 复现

```bash
python proof/layer_program/c260_encoding_check.py    # R17 三个族点
python proof/layer_program/c259_chartfree_full.py    # R17 左逆证书
python proof/layer_program/c264_general_check.py     # 第二实例（10 项）
wsl -e bash tools/lean/check_lean.sh                # Lean 回归
```
