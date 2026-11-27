# F — 待办任务 A 与 B（本项目的剩余全部工作）

> **本项目的唯一目的：证明或证伪命题 q（`q.txt`）。** 其余一切（文档整理、清理、脚本）都是衍生物。
> 本文件把剩余工作立为两个**精确规格**的任务，含已知事实、目标、第一步与禁区。

---

## 任务 A：对"情形 II ∧ 平行"做 NP-hard 归约

### A.0 目标

$$\text{证明}：\text{判定}\ \exists\,\mathcal L\ (q_0\ \text{行},\ \supseteq L_0):(\text{A})\wedge(\text{S})\ \text{为}\ \textbf{NP-hard}$$
（若成功 ⟹ **命题 q 为真** ✓ —— 这是本项目的最大成果）

### A.1 为什么锁定"情形 II ∧ 平行"

| 事实 | 来源 |
|---|---|
| 硬度的唯一可能来源在 (5b)/(S) 侧（仅 (5a) 是多项式的） | T3/T4 |
| q3（$\operatorname{rank}[C;CA]=n$）是多项式 | q3 |
| 情形 I₁（$d_{CA}=1$）判定 ∈ BPP | T7 |
| 情形 I₂：无条件二分 | T8 |
| **情形 II 不平行**（$\pi(L_0A)\not\parallel\pi(L_0)$）⟹ 判定**恒 NO**（多项式、chart-free） | **T12** |
| **情形 II 平行** ⟹ T5a 被 (A) 蕴含 ⟹ **无简化** | **T12″** |

$$\Longrightarrow\quad\textbf{情形 II ∧ 平行}\ \text{是唯一未被任何多项式算法覆盖的区域}$$

### A.2 归约目标问题的精确形式

> 🚨🚨 **第 17 处：最重要的技术警告（务必先读）**
>
> **我的 (I)∧(II) 表述只对 $q_0=2$（即 $\Lambda$ 为 $2\times2$）成立** ✗
> —— (A) 的分解 $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$ 要求 $\Lambda$ 为 $q_0\times q_0$ ⟹
> **$\mathcal L$ 的每一行都对应一条行条件**，共 **$q_0$ 条** ✓
>
> **凡 $q_0\ge3$ 的实例，本文档前面所有基于 (I)∧(II) 的结论都无效** ✗
> （这解释了第 15、16 处的失败：平行实例是 $q_0=3$ ✓）
>
> **正确的通用表述**（$\pi$ = 到 $\operatorname{row}(C,CA)^\perp$ 的投影）：
> $$(\text{A})\iff\exists\Lambda\in\mathbb{Q}^{q_0\times q_0}:\quad
> \forall i=1..q_0:\ \ \pi\big((\mathcal LA)_i\big)=\sum_{j=1}^{q_0}\Lambda_{ij}\,\pi(\mathcal L_j)$$
> | 项 | 内容 |
> |---|---|
> | 未知量 | $R$（$k\times n$）、$\Lambda$（$q_0^2$）|
> | 方程 | $q_0\cdot d_{CA}$ 条 |
> | **难点** | **双线性**（$\Lambda_{ij}\mathcal L_j$）—— 但**只与 $\Lambda$ 的最后一列**相乘 ✓ |
>
> **线性化**：固定 $\Lambda$ 的最后一列 $\ell\in\mathbb{Q}^{q_0}$ ⟹ 对每个 $\ell$ 是**一次线性求解** ✓；
> 但 $\ell\in\mathbb{P}^{q_0-1}$ 是**连续参数** ✗ ⟹ **这正是"情形 II 平行"难度的技术根源** ✓
>
> ✅ **已在 $q_0=2$ 上校准**（`attack_chart_rigorous.py` 用的正是 $q_0=2$ ✓ ⟹ 那些结论**有效** ✓）

**输入**：满足 H1–H4 的 $(A,C,L_0)$，且
$$\pi(L_0A)\parallel\pi(L_0)\ (\pi=\text{到}\operatorname{row}[C;CA]^\perp\ \text{的投影}),\qquad d_{CA}\ge q_0$$

**判定**：$\exists\,\mathcal L$（$q_0$ 行，含 $L_0$）使 $(\text{A})\wedge(\text{S})$？

**已知的等价改写**（减少工作量）：
- $(\text{S})\iff\operatorname{im}H$ 不含 $\Lambda$ 的特征向量，$H=\mathcal L N_{CA}$ ✓（T5）
- 情形 II 下 $(\text{S})$ 要求 $\operatorname{rank}H<q_0$ ✓（T6，逐点）
- 平行情形下 $(\text{A})\Rightarrow\operatorname{rank}H<q_0$ ✓（T12″）⟹ **只需处理 (S)**

### A.3 建议的归约方向（未验证，供试探）

#### ⭐⭐ 本轮关键进展：**猜想 A\* 很可能为假 ⟹ 任务 A 有靶子**

**猜想 A\***：情形 II ∧ 平行 ⟹ 判定恒为 YES

**检验结果（`settle_Astar.py`，6 个平行 ∧ 情形 II 的 $k=1$ 实例）**：
400 个 $\lambda_{11}$ × 25 个**解空间采样**（不只是特解）× 6 实例 ⟹ **0/6 找到秩降点** ✗

**诊断（`diag_search_space.py`）给出实例级的硬事实**：

| 检查 | 结果 |
|---|---|
| `p1` 给出的 $L_x$：前 $r$ 行 $=L_0$ ✓、(A) 成立 ✓ | ✓ |
| $\operatorname{rank}(L_xN_{CA})$ | **$=q_0$（无秩降）** ✗ |
| $\pi(L_0A)$ vs $\pi(L_0)$ | 比值全为 $-2$ ⟹ **平行** ✓（$\lambda^*=-2$）|
| $\pi(w)$ | **不平行** ✗ |

$$\boxed{\ \text{平行 ∧ 情形 II 中存在 (A)-可行}\ \mathcal L\ \text{其}\textbf{无秩降}\ \Longrightarrow\ (\text{S})\ \text{失败（T6）}}$$

$$\Longrightarrow\quad\textbf{A* 很可能为假}\ \Longrightarrow\ \text{该区域}\textbf{可能藏真硬度}\ \Longrightarrow\ \textbf{任务 A 有靶子}\ ✓$$

> ⚠️ **不严格**：6 实例 × 400 $\lambda_{11}$ 的"未找到"**不等于**"不存在" ✗
> **严格化路径**：用第 ② 项的**子式插值技术**（(I)∧(II) + T5a 约束，把相容性化为 $\lambda_{11}$ 的多项式）
> 证明"无秩降" ✓ —— 这正是下一轮该做的事 ✓

#### ⭐⭐ 分支分解与**严格判定**（本轮完成一半）

**(A) 的两个分支**（$\lambda_{12}$ 归一）：

| 分支 | (I) 的形式 | 处理方式 |
|---|---|---|
| $\lambda_{12}\ne0$（WLOG $=1$）| $\pi(w)=\pi(L_0A)-\lambda_{11}\pi(L_0)$ | 需扫 $\lambda_{11}$ ⟹ 相容性是 $\lambda_{11}$ 的**多项式**条件 ⟹ 插值 |
| **$\lambda_{12}=0$** | $\lambda_{11}=\lambda^*$ **被强制**，$\pi(w)$ **自由** | ⟹ **单一线性系统** ⟹ **可直接严格判定** ✓ |

**分支 2 的线性系统**（用 $s:=\lambda_{22}t$ 消去双线性 ✓）：
$$(\text{T5a})\ \pi(w)=t\,\pi(L_0)\qquad(\text{II})\ \pi(wA)=(\lambda_{21}+s)\,\pi(L_0)$$
未知量 $w(n),t,\lambda_{21}+s$ ✓；方程 $2d$ 个 ✓；**无 $\lambda_{11}$ 参数** ✓

**判定结果**（`taskA_branch2.py`，8 个平行 ∧ 情形 II 实例）：
$$\boxed{\ \textbf{分支 2 全部无 T5a-相容解}\ (8/8)\ ✗}$$

**关键配套事实**：$\lambda_{12}=1$ 时 T5a **自动成立**（因 $\pi(L_0A)\parallel\pi(L_0)$ ✓）
$$\Longrightarrow\quad\text{只要分支 1 有 (A)-解，就有秩降}$$

**而 `p1` 给出的 (A)-解属于分支 2**（$\pi(w)$ 不平行 ✓）⟹ **无秩降** ⟹ **与上述自洽** ✓

$$\Longrightarrow\quad\boxed{\ \text{若分支 1 亦（严格）为空}\ \Longrightarrow\ \text{该实例是 NO 实例}\ \Longrightarrow\ \textbf{任务 A 的靶子被严格建立}\ }$$

> **只差最后一步**：用**子式插值**证明分支 1 的 (I)∧(II) 对一切 $\lambda_{11}$ 不可解
> （技术已在第 ② 项验证过 ✓：插值出全部 $(\dim x+1)$ 阶子式，检查 gcd）

#### ⚠️⚠️ 最后一步执行后，得到**相反方向**的结果（第 15 处，任务 A 的靶子**未建立**）

`taskA_branch1_rigorous.py`（6 个平行 ∧ 情形 II 实例）：

| 检查 | 结果 |
|---|---|
| $M$（$6\times7$）的全部 $6\times6$ 子式 | **全 $\equiv0$** ⟹ $\operatorname{rank}M\le5$ **处处** |
| $[M\lvert b]$ 的全部 $6\times6$ 子式 | **也全 $\equiv0$** ⟹ $\operatorname{rank}[M\lvert b]\le5$ **处处** |

$$\Longrightarrow\quad \operatorname{rank}M\ \text{与}\ \operatorname{rank}[M|b]\ \text{都}\ \le5\ \text{且}\ \operatorname{rank}[M|b]\ge\operatorname{rank}M\ \text{恒成立}
\ \Longrightarrow\ \textbf{分支 1 的系统很可能}\textbf{相容}$$

$$\boxed{\ \textbf{这与"采样搜索未找到 (A)-解"矛盾}\ \Longrightarrow\ \textbf{"任务 A 有靶子"的推断}\textbf{不可靠，已撤回}\ ✗}$$

**三种可能解释（我无法在本轮确定是哪一种）**：
| # | 解释 | 后果 |
|---|---|---|
| (a) | 采样搜索的零空间采样不足（25 点 × 400 λ11 可能漏） | 靶子仍在 |
| (b) | 采样搜索的 (A)-判据有 bug ✗ | 靶子仍在 |
| (c) | 分支 1 确实相容 | **猜想 A\* 为真** ⟹ 该区域**恒 YES** ⟹ **无硬度** ✗ |

**⟹ 任务 A 的靶子**：❌ **未建立**（本轮撤回）

#### 🆕 T12″ 的更正（第 14 处）

T12″ 曾论证"平行 ⟹ (A) ⟹ T5a（$\pi(w)\parallel\pi(L_0)$）" ✗ ——
但 (I) 为 $(\lambda^*-\lambda_{11})\pi(L_0)=\lambda_{12}\pi(w)$：

| 分支 | 后果 |
|---|---|
| $\lambda_{12}\ne0$ | $\pi(w)\parallel\pi(L_0)$ ✓（论证成立）|
| **$\lambda_{12}=0$** | $\lambda_{11}=\lambda^*$，**$\pi(w)$ 自由** ✗ ⟹ **论证不成立** |

> ✅ **T12″ 的结论仍成立**（"平行情形无简化"），但**理由要改**：
> 不是"T5a 自动成立"，而是"**$\lambda_{12}=0$ 分支让 $\pi(w)$ 自由**" ✓

#### 三条候选归约方向

| 方向 | 理由 | 风险 |
|---|---|---|
| 从 **矩阵束/广义特征值** 问题归约 | (S) 本质是"$\operatorname{im}H$ 避开特征方向"，与广义特征值结构同型 | 中 |
| 从 **SAT / 3-SAT** 归约 | 需要把布尔选择编码进 $\Lambda$ 或 $H$ 的结构 | 高（控制 (A) 的同时编码布尔量很难） |
| 从 **$\exists\mathbb{R}$-完全问题** 归约 | 情形 II 的判定本身是 ETR 型 | 中（但结论会弱于 NP-hard）|

### A.4 第一步（具体、有限）

1. 用 `scripts/core/test_caseII_YES.py` 造**平行**的 YES 实例（已知存在 ✓：$n{=}4,p{=}1,r{=}1$ 的 3 个 ✓）
2. 分析这些实例的 $(S)$ 条件，看它是否等价于某个已知的 NP-hard 判定
3. 若发现等价 ⟹ 直接完成归约；否则换方向

### A.5 🚨 禁区

- ❌ 不可用"随机采样找不到"当"不存在"（本会话已两次吃亏）
- ❌ 不可声称"因为情形 II 是 ETR 就 NP-hard"——**ETR 本身 NP-hard 只说明不能排除**，不构成归约
- ❌ 不可跳过 (A) 的控制——归约必须保证目标实例落在"情形 II ∧ 平行"内

---

## 任务 B：扩展 P1 的参数化，覆盖图卡外的最小增广

### B.0 目标

$$\text{给出一个覆盖}\ \textbf{所有最小 (A)-增广}\ \text{的参数化（或证明不存在这样的参数化）}$$

**为什么必需**：本项目的 §4 结论（引理 1–8、定理 A/B/C、D1/D2、486/486…）**全部只覆盖 P1 图卡内** ✓；
而**已严格证明存在图卡外的**最小**增广** ✓（P1 Thm 3 不完整）⟹ 要推广到全体实例必须先补这一步 ✓

### B.1 已知事实（严格）

#### ⭐⭐ 本轮新得到的最强形式（B-ii 第一步）

对反例实例（$n{=}5,p{=}1,r{=}1$，$\eta=[3]$，$q_0=3$，$k=2$），**随机采样 400 个含 $L_0$ 的 3 行 $\mathcal L$**
（几乎全部满足 (A) ✓），统计 $\operatorname{rank}(RN_CK)$：

| 实例 | (A) 命中 | $\operatorname{rank}(RN_CK)$ 取值 | 最大 |
|---|---|---|---|
| 1–6 | ~400/400 | **只有 $\{0,1\}$** | **1 < k = 2** |

$$\boxed{\ \text{对这些实例，}\textbf{每一个}\ (\text{A})\text{-可行的行空间}\ V\ \text{都在 P1 图卡之外}\ }$$

**⟹ 这比原先的结论强得多**：
- 原结论（第 ② 项）：**存在**图卡外的最小增广 ✗
- 现结论：**全部** (A)-可行增广都在图卡外 ✗ ⟹ **P1 参数化对这些实例完全失效**

#### ⚠️ 图卡条件的"线性刻画"——**验证失败，已撤回（第 13 处）**

曾提出：$\operatorname{rank}(RN_CK)<k\iff\exists0\ne y_R:\ y_R^{\mathsf T}RN_C\in\operatorname{row}(L_0N_C)$

**验证结果：失败** ✗（`verify_chart_linear.py`）

| 判据 | 结果 |
|---|---|
| A：$\operatorname{rank}(RN_CK)<k$ | 60/60 全 True |
| B：$\exists0\ne y:\ y^{\mathsf T}RN_C\in\operatorname{row}(L_0N_C)$ | **0/60**（全 False）|
| 一致？ | **False（8/8 实例全不一致）** ✗ |

$$\Longrightarrow\quad\textbf{该刻画不可靠，不得引用；原因待查（可能出在 }K\text{ 的取向或 }(\ker M)^\perp=\operatorname{row}M\text{ 的配对约定）}$$

> **注**：下面的**结构结论**（"全部 (A)-可行点在图卡外"）**不依赖**该刻画 ✓ ——
> 它是直接从代码算出的 $\operatorname{rank}(RN_CK)$ 取值（400×6 全部 $\le1<2$）✓ ⟹ **作为采样证据仍成立** ✓

#### ⭐⭐ 结构性解释（由上面的线性刻画 + 采样数据得出）

采样显示：**400 个 (A)-可行点全部满足 $\operatorname{rank}(RN_CK)\le1<k=2$** ✓

$$\Longrightarrow\quad\boxed{\ \textbf{对这些实例，}(\text{A})\ \text{本身就}\textbf{强制}\ \text{图卡条件失效}\ }$$

**⟹ 这解释了一切**：
- 不是"P1 参数化漏了某个分支"✗
- 而是**这些实例的任何 (A)-可行增广都自动落在图卡外** ✗
  ⟹ **P1 的 Theorem 3 对这些实例完全为空**（不是"不完整"，而是"覆盖集为空"）

> ⚠️ **待验证**：上述"线性刻画"是推导 ✓；"（A）强制失效"目前是**采样证据**（400 点 × 6 实例）
> ⟹ 严格化路径：证明 $(\text{A})\Longrightarrow wN_C\in\operatorname{row}(L_0N_C)$（$k=1$ 时）

#### 其它已知事实

| 事实 | 内容 |
|---|---|
| **图卡条件** | $\operatorname{rank}(RN_CK)=k$，$K=\ker(L_0N_C)$；**内蕴**（不依赖 $T$ 的选取）|
| **P1 参数化** | $\mathcal L=[L_0;X_J(\Theta)M_C+KC]$，$W_J$ 底部块 $=[I_k|\Theta]$（恒秩 $k$）⟹ 只能表示图卡内的 |
| **反例** | $L_0=CA^2$、$n{=}5,p{=}1,r{=}1$、$\eta=[3]$、$q_0=3$、$k=2$：**全部** (A)-可行点在图卡外；且**不存在 2 行 (A)-增广**（严格：子式插值）|
| **无残留缺口** | `close_lambda12_gap.py` 确认 $\lambda_{12}=0$ 分支为空 |

### B.2 建议的技术路线（未验证）

#### 🆕 先记一个新观察（T13）：问题本质上是 **Grassmann 问题**

- **(A) 只依赖行空间** $V=\operatorname{row}(\mathcal L)$ ✓
- **$H=\mathcal L N_{CA}$ 模 $\operatorname{row}(C)$ 由 $V$ 决定** ✓：把 $\mathcal L$ 换成
  $\mathcal L+\text{(row}(C)\text{-行)}$ 不影响 $H$（因 $CN_{CA}=0$ ✓）；
  行变换 $S$ 使 $H\to SH$（改变具体子空间但保留全部秩/特征方向信息 ✓）
- ⟹ **整个判定问题是一个 Grassmann 问题**，变量是 $q_0$ 维子空间
  $$V\in Gr(q_0,n),\qquad \operatorname{row}(L_0)\subseteq V,\qquad
  (\text{A}):\ \operatorname{row}(VA)\subseteq V+\operatorname{row}(C,CA)$$
- ⟹ **P1 的参数化是 $Gr$ 上的一个坐标图**；
  "**图卡外的最小增广**" = **没有任何 P1 坐标图覆盖的 $V$** ✓
- ⟹ 任务 B 的正确提法：**在"有效 $V$ 的簇"上给出覆盖全部连通分支的坐标图** ✓

#### 三条路线

| 路线 | 内容 | 难点 |
|---|---|---|
| **B-i：分层参数化** | 按 $\operatorname{rank}(RN_CK)=\rho$ 分层，每层用不同参数化（$\rho=k$ 即 P1 图卡）| 需要刻画各层几何 |
| **B-ii：Grassmann 直接参数化** | 用上面的 $V$-描述，直接研究"有效 $V$ 的簇"| 需要把 (A) 写成 $V$ 的坐标方程 |
| **B-iii：证明图卡条件对最小增广必要** | ❌ **不可行** —— 已被 8/8 反例**严格否定** ✗ | — |

$$\Longrightarrow\quad\textbf{走 B-i 或 B-ii；B-ii 因 T13 而更有希望}$$

### B.3 第一步（具体、有限）

1. 对反例实例，**显式计算**其 3 行最小增广的约化数据 $W_J=\mathcal L N_CT$（用 `build_norm_T` ✓，它对这些实例工作正常 ✓）
2. 观察 $W_J$ 的形状（预期底部块 $\ne[I_k|\Theta]$ ✗）
3. 据此推测覆盖它的参数化形式

### B.4 🚨 禁区

- ❌ 不可再尝试"证明 $\rho=k$ 自动成立"（**已被 8/8 反例否定** ✗）
- ❌ 不可用采样代替证明（图卡条件是**代数条件**，采样会漏）

---

## 任务 C：记录（已完成部分）

| 项 | 状态 |
|---|---|
| 全库文档整理 | ✅ 顶层 3 文件；134 个旧文件归档并说明 |
| KaTeX 报错 | ✅ 218 处 / 42 文件已修 |
| [FINAL.md](../FINAL.md) | ✅ 唯一权威结论（13 条已证 + 4 条猜想 + 12 处作废 + 2 条限定）|
| [problems/](../problems/) | ✅ 5 个命题文档，统一框架 |
| 本文件（A/B 规格） | ✅ 任务已立项、含已知事实/路线/第一步/禁区 |

---

## 附：A、B 与命题 q 的关系

$$\textbf{命题 q 为真}\ \Longleftarrow\ \text{任务 A 成功（NP-hard 归约）}$$
$$\textbf{命题 q 的结论可推广到全体实例}\ \Longleftarrow\ \text{任务 B 成功（参数化扩展）}$$
$$\textbf{命题 q 为假}\ \Longleftarrow\ \text{给出情形 II ∧ 平行的多项式算法（目前无路可走）}$$
