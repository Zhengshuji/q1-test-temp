# 34 — 主线：$\mathcal P$ 的最终形式与频率数据

> 承载 [history/33](33_mainline_unification.md)。本文给出主线的**最终靶子**与量化数据。

---

## 0. 最终靶子（**单一问题**）

$$\boxed{\ \mathcal P:\quad \exists\,\Theta:\ (A)(\Theta)\ \wedge\ \operatorname{rank}\big(\mathcal L(\Theta)N_{CA}\big)<q_0\ }$$

$$(A)(\Theta):\ \text{全部}\ (\rho{+}1)\ \text{阶子式}=0,\qquad \text{子式次数}\le2,\qquad \Theta\in\mathbb{R}^{k(s-k)}$$

$$\text{即：}\ \textbf{(A)-轨迹与退化簇}\ \{\operatorname{rank}H<q_0\}\ \text{是否相交？}$$

$$\textbf{q1 的复杂度}\ \equiv\ \mathcal P\ \text{的复杂度}\qquad(\text{支 B 与情形 II 归结为同一问题}\ ✓)$$

---

## 1. 量化数据（`scripts/core/mainline_quant_fast.py`）

| 形状 | 实例 | 有 $(A)$ 点 | **有退化点** | 有 $(S)$ | $\operatorname{rank}H$ 分布 |
|---|---|---|---|---|---|
| $n{=}6,\ p{=}1,\ r{=}1$ | 12 | 12 | **0** | 0 | $\{3\}$（$=q_0$）|
| $n{=}7,\ p{=}1,\ r{=}1$ | 12 | 12 | **0** | 0 | $\{4\}$（$=q_0$）|
| $n{=}8,\ p{=}1,\ r{=}1$ | 12 | 0 | 0 | 0 | — |

（$\ell$ 预算 60；$\operatorname{rank}H$ 分布统计了全部 $(A)$-点，$n{=}6$ 时 552 个）

### 1.1 判读

$$\text{(A)}\ \textbf{几乎总成立}\ ✓\qquad\text{但}\ \operatorname{rank}H\ \textbf{几乎总}=q_0\ \text{（非退化）}$$

$$\text{退化点}\ \textbf{稀有}\ \text{—— 但\textbf{存在}}（[history/33](33_mainline_unification.md)：用更大样本找到 321 个退化点）$$

$$\Longrightarrow\ \mathcal P\ \text{的可行集}\ \textbf{非空但稀疏}$$

### 1.2 为什么"$(A)$ 常见而退化罕见"

$$\text{(A)}:\ \operatorname{rank}\big[\bar W(\Theta);\bar B;\bar W(\Theta)\bar A\big]=\rho\quad\text{—— 一般位置成立}\ \checkmark$$
$$\text{退化}:\ \operatorname{rank}\big(\mathcal L(\Theta)N_{CA}\big)<q_0\quad\text{—— 要求秩降，是\textbf{闭条件中的薄集}}\ ✗$$

---

## 2. $\mathcal P$ 的复杂度（文献地位）

来自 [Blondel–Tsitsiklis 综述（Automatica 2000）](https://perso.uclouvain.be/vincent.blondel/publications/99BT-survey-full.html)：

| 相关事实 | 内容 |
|---|---|
| **ETR 可判定** | 复杂度 $m(n{+}1)d^{O(n)}$ 算术运算（Basu–Pollack–Roy）|
| **秩-1 仿射族**的判定 | **NP-hard**；$m{=}1$ 时多项式可解（Fu–Barmish 1988）|
| **"族中含稳定矩阵"** | **NP-hard**（Blondel–Tsitsiklis 1997）|
| **静态输出反馈** | ⚠️ **长期未解**（可判定但 NP-hard 性未知）|

$$\Longrightarrow\ \mathcal P\ \text{属于"}\textbf{可判定但 NP-hard 性未定}\text{"这一类}\ \text{—— 与静态输出反馈同类}\ ⚠️$$

---

## 3. q1 的最终状态（诚实汇总）

$$\underbrace{\textbf{情形 II}}_{\text{分支 A 内}}\ \xrightarrow{\ \text{T12 已证不平行}\ }\ \text{平行侧 (c6′)}\ \searrow$$
$$\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\ \ \Big\}\ \Longrightarrow\ \mathcal P\ \text{（同一问题）}$$
$$\underbrace{\textbf{支 B}}_{\text{本轮确证可非空}}\ \xrightarrow{\ \text{见证已找到}\ }\ \text{退化点稀但存在}\ \nearrow$$

| 项 | 状态 |
|---|---|
| $(A)$ 部分 | ✅ 多项式（$q_0$ 有闭式）|
| 硬度唯一可能的来源 | $(S)$ / 退化条件 |
| 归结后的靶子 | ✅ **单一问题** $\mathcal P$ |
| $\mathcal P$ 的可满足性 | ✅ 非空（有见证）|
| $\mathcal P$ 的频率 | ⚠️ 稀疏（$\approx 1/40$ at $n{=}6$）|
| $\mathcal P$ 的复杂度 | ❌ **未定**（文献显示同类问题亦未定）|
| 支 B 是否硬度源 | ⚠️ **开放**（此前"已排除"不成立）|
| 情形 II 是否硬度源 | ⚠️ **开放**（c6′ 未证）|

---

## 4. 下一步（按价值，明确）

| 序 | 动作 | 预期产出 |
|---|---|---|
| **1** | **尝试归约**：把"低秩仿射族判定"（已知 NP-hard 的版本）**归约**到 $\mathcal P$ | 若成功 ⟹ **q1 是 NP-hard** ✓✓ |
| **2** | **尝试算法**：$\mathcal P$ 的约束次数 $\le2$ 且变量只在 $k$ 行 ⟹ 是否有线性代数判据？ | 若成功 ⟹ **q1 不是 NP-hard** ✓✓ |
| **3** | **Lean 形式化等价**："$(A)\wedge(S)\Leftrightarrow\exists\Theta:(A)\wedge\operatorname{rank}H<q_0$"（条件于 c3；T6 已机器验证 ✓）| 巩固逻辑 |
| **4** | 扩大频率样本（$n$ 更大、$p$ 更大）| 判断稀疏度是否随 $n$ 恶化 |

### 4.1 我对优先级的判断

$$\textbf{序 1（归约）最有价值}：\text{若成功，}\textbf{直接证明 q1 是 NP-hard}\ \text{—— 这是项目最初的目标}\ \checkmark$$

**归约的切入点**：综述指出"秩-1 仿射矩阵族的判定是 NP-hard"。
若能把**该问题**嵌入我们的 $(A)$-条件（$(A)$ 也是"仿射族的秩条件"），即得 NP-hard。
**需检查**：我们的族 $\{\bar W_J(\Theta)\}$ 是否有足够自由度（$\bar A,\bar B$ 可自由选择）来模拟一般秩-1 仿射族。

---

## 5. 本轮产出清单

| 文件 | 内容 |
|---|---|
| [history/33_mainline_unification.md](33_mainline_unification.md) | ⭐ **支 B 与情形 II 归约为同一问题** $\mathcal P$ |
| **本文** | $\mathcal P$ 的最终形式 + 频率数据 + 文献地位 |
| `scripts/core/mainline_structure.py` | ⭐ 结构分析（发现"$(S)$ 可满足 ⟺ 退化点存在"）|
| `scripts/core/mainline_quant_fast.py` | ⭐ 频率量化 |
| `scripts/core/mainline_witness2.py` | ⭐ 见证搜索 + 核验 |
| `scripts/core/witness_branchB.json` | 见证数据 |
| `scripts/core/mainline_S_sanity.py` | $(S)$ 检验器健全性 |
