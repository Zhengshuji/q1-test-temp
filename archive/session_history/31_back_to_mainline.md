# 31 — 回到主线：B2 的结果如何改变支 B 的复杂度问题

> 承接 [history/30](30_B2_proof_skeleton.md)。本文把"$\Omega^\star_J$ 正维数"这一新事实
> **接回 q1**，重新陈述支 B 的判定问题，并给出下一步的攻击路线。

---

## 0. 一句话

$$\text{原表述"支 B 解集是有限孤立点 $\Rightarrow$ 可枚举 $\Rightarrow$ 非硬度源"}\ \textbf{失效}\ ✗$$
$$\text{正确表述：}\ \Omega^\star_J\ \text{是\textbf{零测的实代数集}（}k\ge2\text{ 时\textbf{正维数}}）\ \Longrightarrow\ \text{判定其非空} = \text{ETR 型存在性问题},$$
$$\text{其复杂度}\ \textbf{重新开放}\ ⚠️$$

---

## 1. 主线的逻辑骨架（重新陈述）

### 1.1 q1 是什么

$$(\text{原}\ q.txt)\quad \text{找行数最小的 } R\in\mathbb{Q}^{k\times n}\ \text{使}\ \begin{bmatrix}L_0\\R\end{bmatrix}\ \text{满足}\ (5a)\wedge(5b)\ \text{——此问题是 NP-hard？}$$

**等价形式**（[history/28](28_problem_reading_and_branchB_counterexample.md) §2.2 已核实）：

$$\textbf{q1}\ =\ \text{判定}\ \nu_{\min}=q_0\ \text{是否成立}\quad(\nu_{\min}=\text{最小的"谱可行"阶})$$

### 1.2 为什么"硬度只能来自 (S)"

| 条件 | 复杂度 | 依据 |
|---|---|---|
| $(5a)$ / $(A)$ 单独 | **多项式** | $q_0=\sum_j\eta_j$ 有闭式；$(A)$ 的可行性可判 |
| $(5b)$ / $(S)$ | **未定** | 谱条件，须在全部 $(A)$-增广中找谱可行的 |

$$\Longrightarrow\ \textbf{判定}\ \nu_{\min}=q_0\iff (S)\ \text{在}\ q_0\ \text{处是否可行}$$

### 1.3 分 A/B 的动机

$(A)$-增广的**参数化**（P1 Thm 3）：$\mathcal L=W_J(\Theta)$，$J\subseteq\{1,\dots,s\}$，$|J|=k$，$\Theta\in\mathbb{Q}^{k\times(s-k)}$。
记 $m:=k(s-k)$。

$$(\text{S})\ \text{是}\ \Theta\ \text{的代数条件}\ \Longrightarrow\ \text{可行集}\ \Omega^\star_J\subseteq\mathbb{Q}^m$$

| 分支 | 条件 | $\Omega^\star_J$ 的几何 |
|---|---|---|
| **支 A** | $2p+q_0\ge n$ | 一般**正维数**（$(A)$ 几乎无约束）⟹ 采样可判 ⟹ 易 |
| **支 B** | $2p+q_0<n$ | **测度 0** ⟹ 采样必失败 ⟹ 须精确方法 |

---

## 2. ⭐ 本轮新事实对支 B 的影响

### 2.1 旧论证（**失效** ✗）

$$\text{旧：}\ \Omega^\star_J\ \text{是\textbf{有限}孤立点}\ \Longrightarrow\ \#\Omega^\star_J\le\text{poly}\ \Longrightarrow\ \text{枚举可行}\ \Longrightarrow\ \text{非硬度源}\ ✗$$

**失效原因**（[history/30](30_B2_proof_skeleton.md)）：

$$\boxed{\ \dim\Omega^\star_J=0\ \text{仅当}\ k=1\ ;\qquad k\ge2\ \text{时}\ \dim\Omega^\star_J>0\ }$$

| 支 B，$k=1$ | 支 B，$k\ge2$ |
|---|---|
| $\Omega^\star_J$ 是**单点** ✓ | $\dim\Omega^\star_J>0$（**无限集**）✗ |
| 线性系统 $\Rightarrow$ **多项式可判** ✓ | 二次系统 $\Rightarrow$ **ETR 型** ⚠️ |

### 2.2 新的正确表述

$$\textbf{支 B 的判定问题}\ =\ \bigvee_{J}\ \Big[\ \exists\,\Theta\in\mathbb{R}^{k(s-k)}:\ (A)\wedge(S)\ \text{在}\ W_J(\Theta)\ \text{处成立}\ \Big]$$

对 $k\ge2$，这是一个**实代数存在性问题**：
- 约束是 $M_J(\Theta)$ 的 $(\rho{+}1)$ 阶子式 $=0$（$\Theta$ 的**次数 ≤2** 多项式）
- 加上 $(S)$ 的条件（$\operatorname{rank}((\lambda I-\Lambda)H)=\operatorname{rank}H$ 对某些 $\lambda$）

$$\text{变量个数}\ m=k(s-k),\qquad s=d_C-r=n-p-r$$

$$\Longrightarrow\ \text{参数空间维数多项式于 }n\ \text{——这正是 ETR 可能 NP-hard 的"温床"}\ ⚠️$$

### 2.3 两个方向的判据

| 要证 | 需要 |
|---|---|
| **支 B 难** | 从某个 NP-hard 问题**归约**到"$\Omega^\star_J\ne\emptyset$" |
| **支 B 易** | 给出多项式算法（或证明 $\Omega^\star_J$ 的结构足够特殊）|

---

## 3. 一个已知的强有力线索：**低秩扰动问题**

### 3.1 观察

$(A)$ 的条件在规范化坐标下是

$$\operatorname{rank}\big[\bar W_J(\Theta);\,\bar B;\,\bar W_J(\Theta)\bar A\big]\ \le\ \rho$$

而 $\bar W_J(\Theta)=\bar W_0+\Theta\text{-部分}$ 是 $\Theta$ 的**仿射**函数。

$$\Longrightarrow\ \textbf{这是"求仿射矩阵族中的低秩元"问题（bounded-rank-perturbation / minrank 型）}\ ✓$$

### 3.2 该问题的已知复杂度（需核实文献）

| 设定 | 复杂度 |
|---|---|
| 一般仿射族 + 有限域 | **NP-hard** |
| 一般仿射族 + $\mathbb{R}$ | ⚠️ 有量子化消元算法；**NP-hardness 需具体核查** |
| **本问题**：$M_J(\Theta)$ 的**特殊结构**（$\Theta$ 只出现在 $k$ 行） | **未定** ⚠️ |

$$\Longrightarrow\ \textbf{这是最值得攻的具体问题}：\text{本族的特殊结构是否使低秩检测变容易？}$$

---

## 4. 下一步（明确、可执行）

| 序 | 动作 | 预期 |
|---|---|---|
| **1** | **精确陈述**支 B 的判定问题（含 $(S)$ 的条件），写成"$\exists\Theta$"形式 | 明确靶子 |
| **2** | 实现**求解器**（$k$ 固定时的精确求解：$k=1$ 线性、$k=2$ 可消元）| 可做实验 |
| **3** | 在**大范围实例**上测"$\Omega^\star_J\ne\emptyset$ ∧ $(S)$ 可行"的频率与结构 | 找规律 |
| **4** | 若发现"总是空" ⟹ 支 B 无解 ⟹ 排除支 B（回到"无硬度"结论，但**这次有正确依据**）| 强结论 |
| **5** | 若发现"有解" ⟹ 仔细看是否有**组合爆炸**的迹象 ⟹ 尝试归约 | 硬度 |

---

## 5. 我的判断（诚实）

$$\text{本轮的结果}\ \textbf{把支 B 从"已排除"变成"重新开放"}\ ⚠️$$

**但**：这不等于"支 B 难"。正确的态度是：
- 旧论证失效 ⟹ 我们**失去了"支 B 不是硬度源"的依据**
- 但我们也**没有**"支 B 是硬度源"的依据
- $$\Longrightarrow\ \text{支 B 的复杂度}\ \textbf{回到未知}\ ✗$$

**最经济的下一步**是 §4 的 1–3：把问题陈述精确化并做大范围数值，看是否有"总是空"的强证据——
若是，则支 B 被（数值意义上）排除，主线的焦点回到**情形 II**（与之前一致，但依据更干净）。
