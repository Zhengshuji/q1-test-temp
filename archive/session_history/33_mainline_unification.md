# 33 — 主线的关键统一：**支 B 与情形 II 归结为同一个问题**

> 承接 [history/32](32_branchB_witness_found.md)。本文给出本轮最重要的**概念性结果**。

---

## 0. 一句话

$$\boxed{\ \textbf{支 B 的可满足性}\ \Longleftrightarrow\ \exists\Theta:\ (A)\ \wedge\ \operatorname{rank}\big(\mathcal L(\Theta)N_{CA}\big)<q_0\ }$$

$$\text{而右边正是}\ \textbf{情形 II 的判定条件}\ \Longrightarrow\ \textbf{分支 A 与支 B 归结为同一个数论-代数问题}\ ✓$$

---

## 1. 结构发现（`scripts/core/mainline_structure.py`）

对支 B 实例收集全部 $(A)$-点，按"是否有 $(S)$ 见证"分类：

| 类别 | $\operatorname{rank}H$ | $q_0$ | $d_{CA}$ | 计数 |
|---|---|---|---|---|
| **有 $(S)$ 见证** | **2**（$<q_0$）| 3 | 4 | **321** |
| 无见证 | **3**（$=q_0$）| 3 | 4 | 214 |
| 无见证 | 2（$=q_0$）| 2 | 4 | 6 |

$$\boxed{\ (A)\wedge(S)\ \text{可满足}\ \Longleftrightarrow\ \text{存在}\ (A)\text{-点使}\ \operatorname{rank}H<q_0\ }$$

### 1.1 为什么这成立（两方向）

| 方向 | 依据 | 状态 |
|---|---|---|
| $\operatorname{rank}H=q_0\ \Longrightarrow\ (S)$ 失败 | 项目 **T6**（满射 $H$ + 非零核 $\Rightarrow\operatorname{rank}(M\circ H)<\operatorname{rank}H$）| ✅ **已机器验证**（`MyProof/Theorems/CaseII.lean`）|
| $\operatorname{rank}H<q_0\ \Longrightarrow\ (S)$ 可满足 | 项目 **猜想 c3 / (C2)**（$\{\operatorname{rank}H<q_0\}$ 上 $(S)$ 恒成立）| ⚠️ **猜想**（486/486 实证）|

$$\Longrightarrow\ \text{该等价关系}\ \textbf{条件于 c3}\ \text{（但数值 486/486 + 本轮 321/321 支持）}$$

---

## 2. ⭐ 统一：两个分支是**同一个判定问题**

| 分支 | 判定条件 | 本轮的等价形式 |
|---|---|---|
| **情形 II**（$d_{CA}\ge q_0$，分支 A 内）| $\exists\Theta:(A)\wedge(S)\wedge\operatorname{rank}H<q_0$ | $\Longleftarrow$ **完全相同** |
| **支 B**（$2p+q_0<n$）| $\exists\Theta:(A)\wedge(S)$ | $\Longleftrightarrow\ \exists\Theta:(A)\wedge\operatorname{rank}H<q_0$ |

$$\boxed{\ \textbf{分支 A（情形 II）与支 B 的判定条件\textbf{完全相同}：}\ \exists\Theta:\ (A)\wedge\operatorname{rank}H<q_0\ }$$

### 2.1 这是一个**重要的简化**

- 以前：两个分支、两个不同的判定问题、分别分析
- 现在：**一个**判定问题

$$\Longrightarrow\ \textbf{q1 的复杂度}\ \text{归结为}\ \textbf{单一问题}\ \mathcal P:\quad \exists\Theta:\ (A)(\Theta)\ \wedge\ \operatorname{rank}\big(\mathcal L(\Theta)N_{CA}\big)<q_0\ ?$$

### 2.2 $\mathcal P$ 的精确形式

$$(A)(\Theta):\quad \text{全部}\ (\rho{+}1)\ \text{阶子式}\ \det M(\Theta)[r,c]=0,\qquad M(\Theta)=\big[\bar W(\Theta);\bar B;\bar W(\Theta)\bar A\big]$$

$$\text{退化}:\quad \operatorname{rank}\big(\mathcal L(\Theta)N_{CA}\big)<q_0$$

$$\text{变量}\ \Theta\in\mathbb{R}^{k(s-k)},\qquad \text{子式次数}\le2$$

$$\Longrightarrow\ \mathcal P\ \text{是}\ \textbf{ETR 型实代数存在性问题}$$

---

## 3. 这对 q1 的意义

### 3.1 逻辑结构

$$\underbrace{\mathcal P\ \text{是 NP-hard}}_{\text{归约}}\ \Longrightarrow\ \textbf{q1 是 NP-hard}\ \checkmark$$
$$\underbrace{\mathcal P\ \text{有多项式算法}}_{\text{或证结构特殊}}\ \Longrightarrow\ \textbf{q1 不是 NP-hard}\ \checkmark$$

**即：q1 的复杂度 $\equiv$ $\mathcal P$ 的复杂度**（在本参数化范围内）。

### 3.2 为什么 $\mathcal P$ 可能是难的（**文献核实**）

$$\mathcal P:\ \text{"求仿射矩阵族中的\textbf{低秩/退化元}"}\ \text{型问题}\ \text{（bounded-rank-perturbation / minrank）}$$

**文献核实**（[Blondel–Tsitsiklis, *A survey of computational complexity results in systems and control*, Automatica 36(9):1249–1274, 2000](https://perso.uclouvain.be/vincent.blondel/publications/99BT-survey-full.html)）：

| 事实 | 出处 / 内容 |
|---|---|
| **ETR 可判定** | 多项式系统 $(=,\ >,\ \ge)$ 的非空性**可判定**；复杂度 $m(n{+}1)d^{O(n)}$ 算术运算（Basu–Pollack–Roy；Tarski/Seidenberg 消元）|
| **秩-1 仿射族** | 其判定 **NP-hard**；而 $m{=}1$（单个参数）时**多项式可解**（Fu–Barmish 1988）|
| **「族中存在稳定矩阵」** | **NP-hard**（Blondel–Tsitsiklis 1997；用 Max-Cut 归约）|
| **静态输出反馈**（$\exists K:\ A+BKC$ 稳定）| ⚠️ **长期未解**：算法上可判定（Tarski），但 **NP-hard 性未知** —— 综述称其为"控制领域著名难题" |

$$\Longrightarrow\ \textbf{我们的}\ \mathcal P\ \text{落在"可判定 + NP-hard 性未定"这一类}\ \text{（与静态输出反馈同类）}$$

### 3.3 为什么 $\mathcal P$ 可能是容易的

$$\text{本轮的频率数据：支 B 上}\ (A)\wedge(S)\ \text{非空}\ \approx\ 1/40\ (n{=}6)\ \text{—— 稀疏}$$

$$\text{但}\ \textbf{稀疏}\ \ne\ \textbf{易}：\text{稀疏的 ETR 仍可能 NP-hard}$$

$$\text{另一条线索}：\mathcal P\ \text{的约束次数}\le2\ \text{且变量只出现在 } k\ \text{行} \Longrightarrow\ \text{结构高度特殊，可能有线性代数判据}$$

---

## 4. 我的结论与建议

### 4.1 结论

$$\boxed{\ \textbf{主线的靶子现在是一个单一、明确、可攻击的问题}\ \mathcal P\ \text{（而非分散的两个分支）}\ }$$

### 4.2 建议的下一步（按价值）

| 序 | 动作 | 预期 |
|---|---|---|
| **1** | **核实 $\mathcal P$ 的复杂度文献**（minrank / bounded-rank-perturbation over $\mathbb{R}$）| 可能直接给出答案 |
| **2** | 用 **Lean 形式化** "$\operatorname{rank}H=q_0\Rightarrow(S)$ 失败"（T6 已有 ✓）并组装"$(A)\wedge(S)\Leftrightarrow\exists\Theta:(A)\wedge\operatorname{rank}H<q_0$"（条件于 c3）| 巩固等价 |
| **3** | **尝试归约**：从 SAT / 独立集编码到 $\mathcal P$ | 证 NP-hard |
| **4** | **尝试算法**：$\mathcal P$ 是否有多项式解法（如低秩的线性代数判据）| 证伪方向 |

---

## 5. 本轮更正/教训

| # | 内容 |
|---|---|
| 1 | 我在 `mainline_B2.py`/`mainline_claim.py` 里因 `max_l` 耗尽**只测了一个实例**就下结论 ✗ → 已更正（[history/32](32_branchB_witness_found.md) §2）|
| 2 | 结构分析（`mainline_structure.py`）**一次性**给出了清晰的机制：$(S)$ 可满足 $\iff$ 退化点在 $(A)$-轨迹上 |
| 3 | $$\textbf{教训}：\text{先做}\textbf{结构分析}（分类）\text{再做}\textbf{频率统计}\ \text{—— 前者信息量更大}\ \checkmark$$ |
