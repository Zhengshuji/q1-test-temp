# q_now.md — 当前问题的精确陈述

> 本文件回答一个问题：**"现在到底要证什么？"**
>
> 它取代 `q.txt`（表述不完整）与 `q2.txt`/`q3.txt`（局部变体），
> 反映一个关键事实：**论文方法不保证 $q_0$ 阶可行，必须扩维。**

---

## 0. 一句话

> **给定满足 H1–H4 的系统 $(A,C,L_0)$，在阶谱 $[q_0,\ n_0-p]$ 中求最小的谱可行阶 $\nu_{\min}$ ——
> 这个计算问题的复杂度是什么（多项式，还是 NP-hard / $\exists\mathbb R$-hard）？**

---

## 1. 为什么不能直接用 `q.txt`

`q.txt` 的原文：

> 找到行数最小的 R，使得将矩阵 L 变成矩阵 [L;R] 时，方程 (5a) 和 (5b) 得到满足，这个问题是 NP-hard。

它有两个缺陷：

| # | 缺陷 | 后果 |
|---|---|---|
| **D1** | **未写前提**（H1–H4） | 命题可能在违例实例上无定义（$\nu_{\min}$ 不存在） |
| **D2** | **隐含假设"$q_0$ 处有解"** | ⚠️ **这个假设不成立**：$\nu_{\min}$ 可能严格大于 $q_0$ |

**D2 是本轮的关键更正**（由用户指出）：

- $q_0=\sum_j\eta_j$ 只是 **(A) 的最小行数**（P1 Theorem 2），它**不保证 (S)**；
- 因此"在 $q_0$ 下搜索 $R$"**不一定能找到**；
- 必须**扩维**到 $q_0+1,\dots,n_0-p$ —— 这正是 **P2**（*Complete Characterization of
  Minimum-Order Functional Observers from Darouach to Luenberger*）的主题。

P2 的原话（`data/p2.txt:59–62`）：

> "The question addressed in this paper is what lies between the algebraic lower endpoint $q_0$
> and the functional-observability upper endpoint $n_0-p$. In particular, **if every algebraically
> admissible realization at order $q_0$ fails the spectral condition, at which subsequent orders
> can a functional observer exist?**"

---

## 2. 问题的精确形式

### 2.1 输入

$(A,C,L_0)$，满足：

| 编号 | 假设 |
|---|---|
| **H1** | $\mathrm{rank}(C)=p$ |
| **H2** | $\mathrm{rank}(L_0)=r$ |
| **H3** | $\mathrm{rank}[L_0;C]=r+p$（排除 $L_0$ 落在 $\mathrm{row}(C)$ 的成分） |
| **H4** | **功能可观**：$\mathrm{row}(O_{L_0})\subseteq\mathrm{row}(O_C)$ |

### 2.2 派生量（多项式可算）

$$n,\ p,\ r;\qquad \eta_1,\dots,\eta_r;\qquad q_0=\sum_j\eta_j;\qquad n_0=\mathrm{rank}(O_C)$$

N_C (ker  C 的基),   M_C (左逆),   T (使 L_0N_CT=[I_r 0] ),
bar A=M_CAN_C,   B_A=CAN_C,   bar A_T=T^-1bar A T,   B_A,T=B_AT,   N_CA (ker [C;CA] 的基)

### 2.3 单阶可行性 $\mathrm{Feas}(q)$

对 $q\in[q_0,\,n_0-p]$，记 $k:=q-r$（额外功能行数）。

**参数化**（P1 Theorem 3）：所有 $q$ 维的 (A)-增广的行空间由

$$Y_J(\Theta)=\begin{bmatrix}I_k&\Theta\end{bmatrix}\Pi_J^{\mathsf T}\in\mathbb R^{k\times s},
\qquad J\subseteq\{1,\dots,s\},\ |J|=k,\ \Theta\in\mathbb R^{k\times(s-k)},\quad s:=n-p-r$$

给出（$J$ 是**离散**选择，$\Theta$ 是**连续**参数）。

构造 $\mathcal L=\begin{bmatrix}L_0\\ X_J(\Theta)M_C+KC\end{bmatrix}$（$K$ 任取，不影响谱条件）。

**两个条件**：

(A)   Θ ∈ Ω^*_A,J  （一个秩等式，binomsk 种 J 各自的条件）

$$(\text{S})\quad \mathrm{rank}\,P_{\mathcal L}(\lambda)=\mathrm{rank}\,H,\ \ \forall\lambda\in\mathbb C,
\qquad P_{\mathcal L}(\lambda)=\lambda H-F,\ \ H=\mathcal L N_{CA},\ \ F=\mathcal L A N_{CA}$$

**定义**：

Feas(q):= ∃  J ⊆ 1,…,s, |J|=k:  ∃ Θ ∈ Ω^*_A,J 使 (S) 成立

### 2.4 目标与问题

$$\nu_{\min}:=\min\{q\in[q_0,\ n_0-p]:\ \mathrm{Feas}(q)\}$$

> **问题 q_now**：计算 $\nu_{\min}$ 的复杂度是什么？

---

## 3. 已知的分解（哪些已解决）

| 情形 | 状态 | 依据 |
|---|---|---|
| **仅 (A)**，任意 $q$ | ✅ **多项式**：$q_0$ 是最小可行；$q\ge q_0$ 时 (A) 可满足 | P1 Theorem 2；本项目定理 2 |
| **$\mathrm{rank}[C;CA]=n$** | ✅ **多项式**：$N_{CA}$ 为空 ⟹ $H=P=0$ ⟹ (S) 自动成立 ⟹ $\nu_{\min}=q_0$ | `problems/q3.txt`（已证 + 120/120） |
| **$\mathrm{rank}[C;CA]<n$ 且 $\mathrm{Feas}(q_0)$ 为真** | ⚠️ **未知** | —— |
| **$\mathrm{Feas}(q_0)$ 为假（需扩维）** | ❌ **未知，且这是 P2 的核心** | P2 算例：$q_0=3<\nu_{\min}=5$ |

**证据（扩维确实必要）**：

- **P2 的算例**：$r=2<q_0=3<\nu_{\min}=5<n_0-p=6$；
- **本项目小规模复现**：$n=3$ 的 5 个实例，$q_0=1$ 处 (A)∧(S) 命中 **0/10**，
  而 $d=2$ 处 **10/10**（脚本 `scripts/core/verify_corollary.py`）。

---

## 4. 核心难点（为什么难）

### 4.1 三重结构叠加

J_离散，binomsk 种  ×  Θ_连续，半代数  ×  q_阶数扫描，最多 n_0-p-q_0+1 次

### 4.2 (S) 的全局性

$(\text{S})$ 要求 $\mathrm{rank}P_{\mathcal L}(\lambda)=\mathrm{rank}H$ **对所有 $\lambda\in\mathbb C$**，
等价于 $\gcd_\lambda\big(\Delta_1(\lambda),\dots,\Delta_{N_h}(\lambda)\big)=1$（无公共根）。

它**不是**逐点条件，而是"矩阵束是否常秩"的判定。

### 4.3 复杂度类的不确定性

| 若… | 则复杂度可能是 |
|---|---|
| 只由 $\Theta$ 的可行性决定 | **$\exists\mathbb R$**（介于 NP 与 PSPACE 之间），**不是** NP-hard |
| 可由"一般点"取代 $\Theta$（如 0/1 现象成立） | 退化为纯组合：C(s,k) 个 $J$ 的搜索 → **可能 NP-hard** |
| (A)∧(S) 的解集是开集 | 单点检验即可 → **多项式** |

**本命题最容易被审稿人击穿的地方**：含糊地称 NP-hard，而实际落到 $\exists\mathbb R$。

### 4.4 已观测到但未证明的结构

| 现象 | 数值证据 | 状态 |
|---|---|---|
| **(S) 只依赖 $\dim\mathcal R$，不依赖 $\mathcal R$ 的具体选择**（"0/1 现象"） | 62/62 实例 × 4 种采样方式 | ❌ 未证 |
| **$d=q_0$ 处 (A) 对所有 $\mathcal R$ 成立** | 670/670 | ❌ 未证 |
| $\mathrm{im}(H)$ 含 $\Lambda$ 的特征向量 ⟺ (S) 失败 | 108/120 | ⚠️ 需改用广义特征向量 |

若"0/1 现象"成立，则每阶**取一个随机点检验**即可，$\nu_{\min}$ 就是最小的"单点通过"的阶——
问题落在 **BPP**，命题为**假**。

---

## 5. 关键追问：扩维时能否沿用相同的方法？

> **问**：若 $q_0$ 不满足，用 $q_0+1$ 等逐阶搜索确定 $R$ 是否存在，
> 是不是可以直接使用相同的方法进行搜索？

### 5.1 答案：**可以沿用"同类型"的方法，但参数每阶都变**

**可以沿用**，因为 P1 §V-A 的参数化推导只用到两个事实：

| # | 事实 | 是否与 $k$ 有关 |
|---|---|---|
| (i) | $L$ 的前 $r$ 行是 $L_0$ $\Longrightarrow$ $L N_C T=\begin{bmatrix}I_r&0\end{bmatrix}$ | ❌ 无关 |
| (ii) | $Y$ 满秩，$Y\in\mathbb R^{k\times s}$，$s=n-p-r$ | ❌ 无关（只要 $k\le s$） |

**因此 $Y_J(\Theta)=\begin{bmatrix}I_k&\Theta\end{bmatrix}\Pi_J^{\mathsf T}$ 对每个 $k$（即每个 $q=r+k$）都适用。**

**$k\le s$ 自动满足**：$q\le n_0-p\le n-p$ $\Longrightarrow$ $k=q-r\le n-p-r=s$。
（数值检查：286 次逐阶验证，0 次违反。）

### 5.2 但**参数每阶都变**

| 量 | 随 $q$ 的变化 |
|---|---|
| $k=q-r$ | 变（$Y$ 的行数） |
| $J\subseteq\{1,\dots,s\},\ \|J\|=k$ | 变（子集数量 $\binom{s}{k}$ 与内容） |
| $\Theta\in\mathbb R^{k\times(s-k)}$ | 变（维数） |
| $\Omega^\star_{A,J}$ 的秩等式 | 变（因 $W_J(\Theta)$ 变） |
| $(S)$ 的 $H,\ F,\ P_{\mathcal L}(\lambda)$ | 全都变（因 $\mathcal L$ 变） |

> 所以是"**同类型的方法**"，**不是**"同一套参数"。

### 5.3 这正是 P2 的工作

P2 明确说（`data/p2.txt` 约 77–83 行）：

> "For each order $q$, a full-column-rank matrix $Z$ is used to represent the nullspace
> associated with a reduced order-$q$ realization. … a finite matrix-chart parameterization
> covers all admissible nullspaces at a prescribed order."

即 P2 对**每个阶** $q$ 用类似的（Grassmann 型 / matrix-chart）参数化——
P2 用 $Z$，P1 用 $Y_J(\Theta)$，本质同源。

### 5.4 ⭐ 关键简化：$(J,\Theta)$ 是 Grassmann 图卡，**不需要枚举 $J$**

这是本轮最重要的认识，它把"指数级搜索"**直接消掉**。

**P1 原话**（§V-A）：

> "as $J$ ranges over all $k$-element subsets of $\{1,\dots,s\}$ and $\Theta$ ranges over
> $\mathbb R^{k\times(s-k)}$, the matrices $Y_J(\Theta)$ represent **all $k$-dimensional
> row spaces in $\mathbb R^s$**."

即
cup_J,ΘY_J(Θ) = Gr(k,s)   (作为集合).

**维数校验**（完全匹配）：

| $s$ | $k$ | $\dim\mathrm{Gr}(k,s)=k(s-k)$ | $\Theta$ 的参数数 | 图卡数 $\binom{s}{k}$ |
|---|---|---|---|---|
| 10 | 5 | 25 | 25 | 252 |
| 20 | 10 | 100 | 100 | 184,756 |
| 40 | 20 | **400** | **400** | **1.38×10¹¹** |

**结论**：

∃ (J,Θ) 使条件成立   ⟺   ∃ R ∈ Gr(k,s) 使条件成立

**枚举 $J$ 只是"换图卡"，不是必需的分支。** 于是总搜索规模从

Σ_kbinomsk  (指数级)   降为   (n_0-p-q_0+1) 次单点判定.

### 5.5 剩下的唯一问题

在 Gr(k,s) 上，判定 (A) ∧ (S) 的解集是否非空。

其复杂度**完全取决于该解集的几何性质**：

| 解集性质 | 判定方法 | 复杂度 |
|---|---|---|
| **开集**（Zariski-开）且非空 | 随机取一点 | **BPP**（去随机化后为 P） |
| 闭集 | 代数几何 / 结式 | 通常更难 |
| 局部闭（开 ∩ 闭） | 需要更细分析 | 未知 |

> **这正是"0/1 现象"的意义**：若每阶的 (S) 解集"全有或全无"（数值 62/62），
> 则每阶只需**单点检验** ⟹ 整个 $\nu_{\min}$ 的判定是 **BPP**，命题 q_now 为**假**。

**因此需要区分两件事**：

| | 是否多项式 |
|---|---|
| 参数化的**表示**（给定 $(J,\Theta)$ 生成/验证 $\mathcal L$） | ✅ 是（秩计算 + gcd 判据） |
| 参数化的**搜索**（找 $(J,\Theta)$） | ⚠️ **取决于上面解集的几何性质** |

---

## 6. 与历史版本的对应

| 文件 | 内容 | 与 q_now 的关系 |
|---|---|---|
| `q.txt` | 原始一句话 | 表述不完整（缺 H1–H4；隐含 $q_0$ 有解） |
| `q2.txt` | 加"候选族约束"的变体 | 已证：候选族约束**不提供**组合硬度（(5a) 只要求线性张成） |
| `q3.txt` | 加 $\mathrm{rank}[C;CA]=n$ | **已证**：$\nu_{\min}=q_0$，多项式 |
| `q_simp.md` | **MFOSP**：单阶可行性判定的精确形式化 | **q_now 的单阶子问题**（$\mathrm{Feas}(q)$） |
| **`q_now.md`（本文）** | **多阶搜索 + 复杂度问题** | **当前要攻的完整问题** |

---

## 7. 要证什么（三个明确的目标）

### 目标 A（最弱，可能可达）
> 证明或否证 **"0/1 现象"**：对每个 $q$，$\mathrm{Feas}(q)$ 的成立与否不依赖具体 $\mathcal R$ 的选择。
>
> 若成立 ⟹ 每阶单点检验 ⟹ $\nu_{\min}$ 在 **BPP** ⟹ 命题为**假**。

### 目标 B（中等）
> 对 $\mathrm{rank}[C;CA]<n$ 的情形，给出 $\mathrm{Feas}(q)$ 的多项式判定，
> 或证明它是 $\exists\mathbb R$-hard。

### 目标 C（最强）
> 给出完整的复杂度定论：$\nu_{\min}$ 是多项式可算，或证明整个问题 NP-hard / $\exists\mathbb R$-hard。

---

## 8. 边界条件与陷阱清单（写证明前必查）

- [ ] **H1–H4 全部满足**（尤其 H3、H4；曾因违反 H3 构造出无效反例）
- [ ] $q$ 的范围是 $[q_0,\ n_0-p]$，**不是** $[r,\ n_0-p]$（下界是代数最小可行阶）
- [ ] 扩维时 $k=q-r$ 变化，参数化 $Y_J(\Theta)$ 的维数随之变化（P2 处理了这个）
- [ ] (S) 的验证必须**双向**：所有 $(h{+}1)$ 阶子式恒零 **且** $h$ 阶子式 gcd 为常数
- [ ] 若主张 NP-hard，**必须消去连续参数 $\Theta$**，否则正确结论是 $\exists\mathbb R$-hard
- [ ] 不要声称是 matroid 最小基问题（matroid 基大小唯一确定，无优化内容）
- [ ] 数值实验必须用**精确有理数算术**（浮点 SVD 曾掩盖 31/387 反例）

---

## 9. 参考文献

1. **P1** T. Fernando, *A Minimum-Order Functional Observer Beyond the Darouach and Luenberger
   Constructions*, arXiv:2609.33615 —— $\eta_j$、$q_0$、Grassmann 参数化、构造性决策过程
2. **P2** T. Fernando, *Complete Characterization of Minimum-Order Functional Observers from
   Darouach to Luenberger*, arXiv:2609.37992 —— **阶谱 $[q_0,n_0-p]$**、逐阶刻画
3. **P3** T. L. Fernando, H. M. Trinh, L. Jennings, *IEEE TAC* **55**(5):1268–1273, 2010 —— (5a)(5b) 出处
