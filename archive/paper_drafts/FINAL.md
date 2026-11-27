# FINAL — 项目结论库（历史累积，部分已过时）

> ⚠️ **状态横幅（2026-10-20 整理时添加）**
> 本文件是**多轮会话累积**的结论库：正文越往后越新，**不同段落之间存在矛盾**。
> **现行权威文档是 [`OPEN_PROBLEM.md`](OPEN_PROBLEM.md) 与 [`RESULTS.md`](RESULTS.md)**；
> 与本文件冲突时，以那两份为准。
> 已知在本文件中**已被后续段落/反例推翻**的内容：
> §0「唯一的硬度候选」「无机器验证」、§8 的表格（其自身已标注过时）、
> 以及 §7.5.19 之前的「判据」相关表述（以 §7.5.18–7.5.21 为准）。
> **保留本文件的价值**：T1–T12 的完整陈述、全部 74 处自我更正的来龙去脉。

---

## 0. 一句话结论

> **q1（`q.txt`）既未证明也未证伪。**
> 已确立的是：**硬度的唯一可能来源在 (5b)/(S) 侧**；**精确阈值是 $k+\dim(E+\operatorname{row}B_{A,T})\ge d_C$**；
> 在 $\{d_{CA}=1\}\cap\{2p+q_0\ge n\}$ 内**不是 NP-hard**（判定 ∈ BPP）；
> **硬度最可能藏在 $d_{CA}\ge q_0$（即"$q_0$ 阶谱不可行、需要扩维"）的情形**。
> **全部基于 $\Theta$ 参数化的结论只在 P1 图卡 $\operatorname{rank}(RN_CK)=k$ 内成立。**
> **无机器验证（Lean/Coq）、无独立复核。**

---

## 1. 问题

### 1.1 系统与条件

LTI：$\dot x=Ax+Bu$，$y=Cx$，$z_0=L_0x$。记 $n=\dim x$，$p=\operatorname{rows}(C)$，$r=\operatorname{rows}(L_0)$，
$\mathcal L=[L_0;R]$，$q=\operatorname{rows}(\mathcal L)=r+k$。

待满足的两个条件（P3 Theorem 2）：

$$(\text{5a})\quad \operatorname{rank}[LA;\,L;\,CA;\,C]=\operatorname{rank}[L;\,CA;\,C]
\qquad\Longleftrightarrow\qquad (\text{A}):\ \operatorname{row}(LA)\subseteq\operatorname{row}(L,C,CA)$$

$$(\text{5b})\quad \operatorname{rank}[\lambda L-LA;\,CA;\,C]=\operatorname{rank}[L;\,CA;\,C]\quad\forall\lambda
\qquad\Longleftrightarrow\qquad (\text{S})$$

**(A) 与 (S) 互不蕴含**（1200 例：两者都成立 670、仅 (A) 85、仅 (S) 433、都不成立 12）。

**标准假设**：H1 $\operatorname{rank}(C)=p$；H2 $\operatorname{rank}(L_0)=r$；
H3 $\operatorname{rank}[L_0;C]=r+p$；H4 功能可观性 $\operatorname{row}(O_{L_0})\subseteq\operatorname{row}(O_C)$。

### 1.2 q1 的原文（`problems/q1.md`）

> 找到行数最小的 $R$，使得将矩阵 $L$ 变成 $[L;R]$ 时，方程 (5a) 和 (5b) 得到满足，这个问题是 NP-hard

三篇原始 PDF **均无 "NP-hard" 字样**（已全文 grep）⟹ 该断言须自行证明。

---

## 2. 记号与基本量

| 记号 | 含义 |
|---|---|
| $q_0=\sum_j\eta_j$ | **最小 (A)-增广行数**（P1 Theorem 2） |
| $\nu_{\min}$ | 使 **(5a) 与 (5b) 同时**满足的最小行数 |
| $d_C=n-p$，$s=d_C-r$，$k=q_0-r$ | 基本维度 |
| $N_C$ | $\ker C$ 的基（$n\times d_C$） |
| $N_{CA}$ | $\ker[C;CA]$ 的基（$n\times d_{CA}$） |
| $\boldsymbol{d_{CA}=n-\operatorname{rank}[C;CA]}$ | **本项目的核心分水岭量** |
| $H=\mathcal L N_{CA}$（$q_0\times d_{CA}$），$F=\mathcal L AN_{CA}$ | (S) 的全部信息都在这两个矩阵里 |
| $\Omega^\star=\{(\text{A})\}$，$\Sigma^{(S)}=\{(\text{S})\}$，$\Sigma_{q_0}=\Omega^\star\cap\Sigma^{(S)}$ | 可行集 |

**参数化**（P1）：所有最小 (A)-增广由 $(J,\Theta,K)$ 给出，$\mathcal L=[L_0;\,X_J(\Theta)M_C+KC]$。
$\Theta$ 的维数是 $\dim\Theta=k(s-k)$；$J$ 是 $s$ 中取 $k$ 的子集。

---

## 3. 结论总览

| # | 命题 | 结论 | 状态 |
|---|---|---|---|
| **T1** | (5a) 的块结构 | 是 **4 块** `rank[LA;L;CA;C]=rank[L;CA;C]`，且 $\iff$ (A) | ✅ 已证 |
| **T2** | (5b) 的约化 | $(\text{S})\iff\operatorname{rank}(\lambda H-F)=\operatorname{rank}H\ \forall\lambda$ | ✅ 已证（本项目自证） |
| **T3** | 精确阈值 | $\{\operatorname{rank}[W_J;B]=d_C\}\ne\emptyset\iff k+\dim(E+\operatorname{row}B_{A,T})\ge d_C$ | ✅ 已证 |
| **T4** | $\Omega^\star$ 满测度 | 秩满集非空开 $\subseteq\Omega^\star$ | ✅ 已证 |
| **T5** | (S) 的谱刻画 | $(\text{S})\iff\operatorname{im}H$ 不含 $\Lambda$ 的特征向量 | ✅ 已证 |
| **T5′** | 铅笔简化 | $F=\Lambda H$，即 $P_{\mathcal L}(\lambda)=(\lambda I-\Lambda)H$ | ✅ 已证（一行代数） |
| **T6** | 情形 II | $d_{CA}\ge q_0\Rightarrow(\text{S})$ 一般点恒假 $\Rightarrow\Sigma^{(S)}$ 零测 | ✅ 已证 |
| **T7** | 情形 I₁ | $d_{CA}=1\Rightarrow$ 判定 ∈ **BPP** | ✅ 已证 |
| **T8** | 情形 I₂ | $2\le d_{CA}<q_0\Rightarrow$ **无条件二分**（BPP 或零测） | ✅ 已证 |
| **T9** | 跳变集零测 | $\mathcal N^c\subseteq\{\operatorname{rank}H<\beta_{\max}\}$ | ✅ 已证 |
| **D1** | 子式次数 | $H$ 的 $q_0$ 阶子式关于 $\Theta$ 次数 $\le k$ | ✅ 已证 |
| **D2** | 仿射结构 | $k=1$ 时 $\{\operatorname{rank}H<q_0\}$ 是**仿射子空间**，多项式时间可算 | ✅ 已证（D1 的推论） |
| **q3** | 秩条件 | $\operatorname{rank}[C;CA]=n\Rightarrow(\text{S})$ 自动成立 $\Rightarrow\nu_{\min}=q_0$，多项式 | ✅ 已证 |
| ~~**T10**~~ | ❌ **已撤回**（第 12 处） | 原论证"$\ker\mathcal L\subseteq\ker L_0$ ⟹ 秩降不可能"用的是**核空间版 T5a**，而**核空间版是错的** ✗（见 §4.3 的手算反例） | ❌ **不得引用** |
| ~~**T11**~~ | ❌ **无效**（第 12 处） | 构造意图（要求 $wx=0$，$x\in\ker L_0\cap\ker[C;CA]$）同样基于**核空间版** ✗；且实测构造出的 $\mathcal L$ 并无秩降（$\operatorname{rank}H=q_0$）| ❌ **不得引用** |
| **T12** | 情形 II 的一个**多项式可判、chart-free** 子情形 | $\pi:=$ 到 $\operatorname{row}[C;CA]^\perp$ 的投影。$k=1$ 时，若 $\pi(L_0)\ne0$ 且 $\pi(L_0A)\not\parallel\pi(L_0)$，则**不存在**满足 T5a ∧ (A) 的 $\mathcal L$；由 T6，(S) 必失败 ⟹ **判定恒为 NO** | ✅ **已证 + 已验**（10/10 实例、140 个含 (A) 的样本、0 个秩降）|
| **c5** | ❌ **已撤回**（第 16 处：判定空洞——齐次系统零解恒存在） | — | — |
| ~~**c6**~~ | ❌ **证据全部失效，已撤回（第 20 处）；并且本轮被显式见证<u>证伪</u>** | **撤回原因（根本性方法错误）**：我用于筛选"平行"实例的判据<u>只用了 $L_0$ 的**第一行**</u> ✗：<br>`pL0 = π(Lc[0]); pL0A = π((L0·A)[0]); 平行 ⟺ rank[pL0;pL0A]=1`<br>而真正的平行是 $\operatorname{rank}[\pi(L_0);\pi(L_0A)]=1$（**全部 $r$ 行**）✓。对 $r\ge2$，前者**太弱** ✗<br>⟹ 三轮探针选出的实例**不满足**真正的平行 ⟹ **结论不适用** ✗<br>**且本轮 ℓ-free 判定暴露了它**：7 个实例的**投影条件满足但 (A) 本身失败** ✗ ⟹ 正是"非真平行"的表现 ✓<br>⟹ **c6 回到"无证据"状态**；若要重做，必须用**完整**的平行判据 ✓<br>**同一判据错误也影响 T12 的验证**：其 10/10 只证明了"**第一行**不平行 ⟹ 无秩降"（比 T12 的陈述弱 ✗）；T12 的**证明**本身不受影响 ✓<br><br>🔴 **第 25 处（本轮）：c6 / c6′ 被显式见证证伪** ✗<br>见 [history/47](history/47_c6p_refuted.md)。存在 $(n,p,r,q_0,d_{CA})=(6,1,2,2,4)$ 的实例（**情形 II**：$d_{CA}{=}4\ge q_0{=}2$），满足 **H1–H4 ∧ (5a) ∧ (5b)**，且**真平行非退化**（$\pi(L_0)\ne0$、$\operatorname{rank}[\pi(L_0);\pi(L_0A)]=1$）、$\operatorname{rank}H=1<q_0$。⟹ **"平行 ⟹ NO" 为假** ⟹ **"情形 II 恒 NO" 为假** ⟹ **分支 A <u>未被</u>排除为硬度所在** ⚠️<br>``(5b)`` 经**两个独立判据**验证（$r_0$ 阶子式 gcd 为常数 + 12 个具体 $\lambda$ 逐一算秩 $=3$）。见证存于 `scripts/core/witness_caseII_parallel_YES.json`。<br>✅✅ **并经<u>完全独立实现</u>复核（13/13 通过）**：`scripts/core/verify_witness_independent.py` 不 import 项目任何库（自带 Fraction Gauss 消元、矩阵乘法、多项式算术、零空间基）；(5b) 的**全部 8 个 3 阶子式 gcd $=4$**（非零常数）、30 个随机有理 $\lambda$ 全部 $=r_0=3$、H1–H4 ∧ (5a) ∧ 情形 II ∧ T5a ∧ 非退化平行全部 ✓。<br>**保留**：该见证 $|R|{=}0$（$L_0$ 本身即满足 (5a)∧(5b)）⟹ **不建立** NP-hardness；只说明情形 II 可以 **YES** ✓<br>**同时澄清**：项目此前 c6′ 的 14/14 实证**全部落在退化分支**（$\pi(L_0)=0$，16/16 数值确认）或 $A$-不变族 ⚠️；**非退化平行 ⟹ $k=0$**（3/3 数值）<br>🔴🔴 **第 26 处（同一轮）：证伪的范围已被精确定界** —— 见 [history/48](history/48_refutation_scope.md)<br>**定理（干净，无需不变性）**：$\operatorname{rank}[\pi(L_0);\pi(L_0A)]\le1$ 且 $\pi(L_0)\ne0$ ⟹ $(A)$ 对 $L_0$ 本身成立 ⟹ $q_0=r$，$k=0$。<br>*证明*：(A) 对 $L_0$ ⟺ $\exists\Lambda\ (r\times r)$，$\pi(L_0A)=\Lambda\pi(L_0)$；平行给出 $\pi(L_0)=cu^{\mathsf T},\pi(L_0A)=du^{\mathsf T}$；故只需 $\Lambda c=d$ —— **对任意 $d$ 总可解**（$r^2$ 个未知、$r$ 个方程）✓<br>*数值*：非退化平行实例 **6/6 全部 $k=0$** ✓；"非退化平行 + $k\ge1$"的构造尝试**不可能**（与定理一致）✓<br>⟹ **在 $k\ge1$（硬度相关）范围，平行 ⟹ 必然退化（$\pi(L_0)=0$）** ⟹ **c6′ 的证伪只影响 $k=0$**（最小 $|R|=0$，对 NP-hardness 无直接贡献）；**$k\ge1$ 的退化分支上 c6′ 仍<u>开放</u>** ⚠️ —— <u>这是 q1 硬度的真正所在</u><br>🎯🎯 **第 27 处（同一轮）：分界线 = A-不变性** —— 见 [history/50](history/50_boundary_is_invariance.md)<br>**相容性检查（关键）**：见证的 $K=\ker[C;CA]$ **不是** $A$-不变的（$\operatorname{rank}[N\mid AN]=5>4=\operatorname{rank}N$，**列拼接**；且 $CA^2\|_K\ne0$）⟹ 见证完全落在 `c6'_of_fact_algclosed` 的假设**之外** ⟹ **无矛盾** ✓（两个结果互补：一个说"不变 ⟹ 失败"，一个说"非不变 ⟹ 可行"）<br>**最终二分**：<table><tr><th>$K$ 的不变性</th><th>$k$</th><th>c6′</th></tr><tr><td>$A$-不变（$K\subseteq\ker CA^2$）</td><td>任意</td><td><b>真</b>（Lean 已证 ✓）</td></tr><tr><td>非不变</td><td>$k=0$</td><td><b>假</b>（见证 13/13 ✓）</td></tr><tr><td>非不变</td><td>$k\ge1$</td><td>~~<b>开放</b>（12/12 未找到反例，弱）~~ ⟹ 🔴 <b>假</b>（见下）</td></tr></table><br>🎯🎯🎯 **第 28 处（同一轮）：$k\ge1$ 也被证伪 —— 反例可<u>手算</u>** —— 见 [history/51](history/51_hand_verifiable_counterexample.md)<br>$(n,p,r,q_0,k,d_{CA})=(6,1,1,\mathbf{2},\mathbf{1},4)$（情形 II）；$C=e_1^{\mathsf T}$；$A$ 前三行 $=e_2^{\mathsf T},e_3^{\mathsf T},0$（其余任意）；$L_0=CA=e_2^{\mathsf T}$（**退化**），$R=e_3^{\mathsf T}$，$\mathcal L=[e_2^{\mathsf T};e_3^{\mathsf T}]$。<br>**手算**：$CA{=}e_2^{\mathsf T},\ CA^2{=}e_3^{\mathsf T},\ CA^3{=}0$；$K=\operatorname{span}\{e_3,e_4,e_5,e_6\}$，$d_{CA}{=}4$；$CA^2|_K\ne0$（**非不变**）；$H=\begin{pmatrix}0&0&0&0\\1&0&0&0\end{pmatrix}$（秩 1 $<q_0{=}2$ ⟹ T5a ✓）；$F=\begin{pmatrix}1&0&0&0\\0&0&0&0\end{pmatrix}$ ⟹ $\operatorname{im}H=\operatorname{span}\{(0,1)\}$、$\operatorname{im}F=\operatorname{span}\{(1,0)\}$ **不同直线** ⟹ (S) 成立 ⟹ (5b) 可成立；$L_0$ 单独失败（rank 3≠2）⟹ $q_0{=}2,\ k{=}1$ **最小**。<br>**独立验证 14/14**（不 import 项目库）：H1–H4 ✓、(5a) $3{=}3$ ✓、(5b) 3 个 3 阶子式 gcd $=\mathbf{1}$ ✓、8 个 $\lambda$ 逐一 $=3$ ✓、情形 II ✓、T5a ✓、退化 ✓、非不变 ✓、$\operatorname{im}F\not\subseteq\operatorname{im}H$ ✓<br>**⟹ c6/c6′（"情形 II 平行 ⟹ NO"）在 $k{=}0$ 与 $k\ge1$ <u>都有反例</u> ⟹ 情形 II 可以 YES ⟹ 分支 A 未被排除为硬度所在** ⚠️<br>**保留**：$k$ 为**常数** ⟹ **不建立 NP-hardness** ⟹ 主线的硬度问题**仍开放**；但 c6′ 作为"情形 II 恒 NO"的依据**已被彻底排除**。<br>🎯🎯🎯🎯 **第 29 处（同一轮）：定理 $(5b)\iff(S)$ —— <u>撤销</u>我此前的担忧** —— 见 [history/52](history/52_session_conclusion.md) §7.7<br>**证明**：$r_0=\operatorname{rank}[\mathcal L;C;CA]=\operatorname{rank}H+(n-d)$（因 $\pi(\mathrm{row}\mathcal L)=\mathrm{row}H$，且 $\mathrm{row}\mathcal L+K^\perp=\pi^{-1}(\mathrm{row}H)$）；$\operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]=\operatorname{rank}((\lambda I-\Lambda)H)+(n-d)$（因 $\pi(\lambda\mathcal L-\mathcal LA)=(\lambda I-\Lambda)H$）⟹ 两者**等价** ✓<br>**验证**：**5998/5998 一致**（5991 全 False 的随机实例 + 7 个族实例全 True，**两侧都有点**）✓<br>⟹ 我在第 25 处写的"**$(S)$ 只是 $(5b)$ 的必要条件**"**是错的** —— 两者等价 ⟹ 项目 14/14 的 $(S)$-证据在**两个方向**上都有效 ⟹ 我"差点因 $(S)$ 成立就宣布 YES"的担心是多余的<br>⟹ **禁区修正**：不是"必须直接测 $(5b)$"，而是"$(S)\iff(5b)$，**两者都测更稳**（可交叉验证）"<br>⟹ **意义**：判定问题只需处理 $(S)$（只涉及 $q\times d$ 的 $H$ 与 $q\times q$ 的 $\Lambda$），结合第 28 处旁的 $(5a)\iff\ker H\subseteq\ker F$，**整个判定可完全在 $d$ 维空间 + $q\times q$ 矩阵上陈述** ⭐<br><br>🎯🎯🎯🎯 **第 30 处（同一轮）：判据找到 —— Type II ⟺ obs $<d_{CA}$** —— 见 [history/52](history/52_session_conclusion.md) §7.24<br>$$A':=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN,\quad R:=AN-NA',\quad \text{obs}:=\dim\big(\text{含}\operatorname{row}(R)\ \text{的最小}\ A'\text{-不变子空间}\big)$$<br>**$\text{obs}=d_{CA}$ ⟹ Type I（$q{=}d_{CA}{+}1$ 处 generic YES，$\sim$90%）**；**$\text{obs}<d_{CA}$ ⟹ Type II（无解）**<br>$$\Longrightarrow\ |R|_{\min}=d_{CA}+1-r\ \text{或}\ \infty\ \Longrightarrow\ \textbf{q1 为假（NP-hardness 不成立）}$$<br>**验证 20/20 全部吻合**（18 个 I：86.0–98.8%；2 个 II：0.0%；**失配 0**）；obs 与 $A'$ 都**多项式可算**。<br>⭐ **与 D6 同一**：obs 就是 [history/49](history/49_degenerate_reduction.md) §2.2 的模论对象 ⟹ 解释 D6 三次显式公式为何全败。<br>**⚠️ 保留**：仅 20 实例（非证明）；"任何 $q$ 都无解"只在 $q{=}d{+}1$（250 采样 + **531,441 全枚举**）与 $q{=}d{+}2$（20,000 采样）验证；**机制缺口**：$\bar A'$ 的特征值须落在 $\mathbb{Q}$；$n\le6,r{=}1,p{=}1$|
| ⚠️ ~~**新暴露的矛盾（未解决）**~~ | ✅ **已解决（第 17 处）** | 矛盾的真正原因：**我的 (I)∧(II) 表述只对 $q_0=2$（$r{=}1,k{=}1$）成立** ✗。(A) 的分解 $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$ 要求 $\Lambda$ 为 $q_0\times q_0$ ⟹ **每个 $\mathcal L$ 的行都对应一条行条件**。而平行情形的实例是 $r{=}2,k{=}1\Rightarrow q_0=3$ ✗，我只写了 **2 条**，漏了 **1 条** ⟹ 构造出的 $w$ 只满足部分条件 ⟹ **(A) 失败** ✓ **完全解释** ✓<br>⭐ **重要**：矛盾**不是** `rk`/`ker_basis` 的问题 ⟹ **全库基础函数可靠** ✓，本会话依赖它们的数值结论（如 T12 的验证）**不受影响** ✓ |
| **c1** | $(\star''')$ | $\Sigma_{q_0}\ne\emptyset\Rightarrow$ 见证落在常秩轨迹 | ⚠️ **猜想**（56/56 实证） |
| **c2** | (C1) | 情形 II 中 $\nu_{\min}=q_0$ 恒成立 | ⚠️ **猜想**（24 例全 YES） |
| **c3** | (C2) | $\{\operatorname{rank}H<q_0\}$ 上 $(\text{S})$ 恒成立 | ⚠️ **猜想**（486/486） |
| **c4** | 支 B 解集维数 | $\dim\Omega^\star_J=0$（**仅 $k{=}1$**）；$k\ge2$ 时 $\dim>0$ | ❌ **原陈述被修正**（见下） |

> 🔴 **c4 的更正（2026，两轮）**
>
> **第 1 轮**（[history/28](history/28_problem_reading_and_branchB_counterexample.md)）：
> 原文"$\#\Omega^\star$ 有多项式上界"**指标未定** —— $\Omega^\star\subseteq\mathbb{Q}^{k(s-k)}$
> 可以是**正维数**，此时"解数"无意义。
>
> **第 2 轮**（[history/29](history/29_B2_result.md)、[history/30](history/30_B2_proof_skeleton.md)）：
> 用 sympy 的 Gröbner 基**精确算出**维数随 $k$ 的变化（全部为**支 B** 实例）：
>
> | 支 B 实例 | $m$ | 非零扰动命中 | **Groebner 次数** | $\dim\Omega^\star_J$ |
> |---|---|---|---|---|
> | $q_0{=}2,\ k{=}1,\ s{=}4$ | 3 | **0/1930** | $[1]$ | **0（单点）** ✓ |
> | $q_0{=}3,\ k{=}2,\ s{=}4$ | 4 | **218/1967** | $[1,2]$ | **$>0$** ✗ |
> | $q_0{=}3,\ k{=}2,\ s{=}5$ | 6 | **18/1998** | $[1,2]$ | **$>0$** ✗ |
> | $q_0{=}4,\ k{=}3,\ s{=}5$ | 6 | n/a | $[2,3,4]$ | **$>0$** ✗ |
>
> $$\boxed{\ \dim\Omega^\star_J=0\ \text{仅当}\ k=1\ ;\qquad k\ge2\ \text{时}\ \Omega^\star_J\ \text{是\textbf{零测、正维数}集}\ }$$
>
> **⟹ 正确的陈述**：支 B 的 $\Omega^\star_J$ **零测**（采样命中率 0）✓，但**不是有限集** ✗
> （$k=1$ 例外，那时确实有限）。
>
> **⟹ 正确的对象**：应研究 $\Omega^\star_J$ 的**维数/分支数**，而非"解数"。
>
> **⟹ 对"支 B 是否硬度源"的影响**：判定"$\Omega^\star_J\ne\emptyset$"仍是
> 一个**实代数存在性问题**（ETR 型）——维数正不改变这一点，但**改变了问题的正确表述** ⚠️
>
> **✅ Lean 已形式化的部分**（`MyProof/Theorems/B2.lean`，**0 error**，已并入主库）：
> $$\Omega\subseteq\textstyle\bigcap_i\ker f_i\ \wedge\ \bigcap_i\ker f_i=\{0\}\ \wedge\ 0\in\Omega\ \Longrightarrow\ \Omega=\{0\}$$
> —— 即 $k=1$ 的**组装逻辑**已机器验证；代数内容（引理 A/B）作假设 ✓

---

## 4. 已证定理的完整陈述

### 4.1 地基（T1、T2）

**T1**：(5a) 的左端是 **4 个块** $[LA;L;CA;C]$（由 P3 的坐标级重建确认），且
$$(\text{5a})\iff\operatorname{row}(LA)\subseteq\operatorname{row}(L,C,CA)=:(\text{A}).$$

**T2**：记 $N_{CA}$ 的列张成 $\ker[C;CA]$，$H=\mathcal L N_{CA}$，$F=\mathcal L AN_{CA}$。则
$$(\text{S})\iff\operatorname{rank}(\lambda H-F)=\operatorname{rank}H\quad\forall\lambda .$$
*证明*：用秩恒等式 $\operatorname{rank}[X;Y]=\operatorname{rank}Y+\operatorname{rank}(X|_{\ker Y})$，
两端都出现 $\operatorname{rank}[CA;C]$，相消即得。$\square$

> **推论（q3）**：$N_{CA}$ 为空（$d_{CA}=0$）时两端都只剩 $\operatorname{rank}[CA;C]$ ⟹ (S) 自动成立
> ⟹ $\nu_{\min}=q_0$，多项式可判 ✓

### 4.2 阈值（T3、T4）

在约化坐标下 $(\text{A})\iff\operatorname{rank}[W_J(\Theta);B_{A,T};W_J(\Theta)\bar A_T]=\operatorname{rank}[W_J(\Theta);B_{A,T}]$。

**T3**：$\max_{\mathcal S\supseteq E}\dim(\mathcal S+\operatorname{row}B)=\min(d_C,\ k+\dim V)$（泛位置），故
$$\{\operatorname{rank}=d_C\}\ne\emptyset\iff k+\dim(E+\operatorname{row}B_{A,T})\ge d_C .$$
**实用充分条件**：$2p+q_0\ge n$。

**T4**：秩满 $\Rightarrow$ (A)；秩满集是开集；故 $\Omega^\star$ **满测度**
（**不需要** $\Omega^\star$ 是闭集——旧引理 4 是假的，见 §7）。

### 4.3 (S) 的谱刻画（T5、T5′）

**T5′**：由 (A) 的 $\mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$，右乘 $N_{CA}$ 并注意 $CN_{CA}=CAN_{CA}=0$，得
$$\boxed{F=\Lambda H}\qquad\Longrightarrow\qquad P_{\mathcal L}(\lambda)=(\lambda I-\Lambda)H .$$
**T5**：$(\text{S})\iff\operatorname{im}H$ 不含 $\Lambda$ 的任何特征向量。
**T5a（✅ 成立，已用手算反例定案）**：
$$\operatorname{rank}(\mathcal L N_{CA})<q_0\iff\operatorname{row}(\mathcal L)\cap\operatorname{row}[C;CA]\ne0$$
*证*：$\mathcal L N_{CA}$ 是 $q_0\times d_{CA}$，秩 $<q_0$ ⟺ **行**相关 ⟺ $\exists0\ne y$ 使
$y^{\mathsf T}\mathcal L N_{CA}=0\iff y^{\mathsf T}\mathcal L\perp\operatorname{im}N_{CA}=\ker[C;CA]
\iff y^{\mathsf T}\mathcal L\in\operatorname{row}[C;CA]$ ✓

**定案依据（手算反例）**：$[C;CA]=\begin{bmatrix}1&0&0\\0&1&0\end{bmatrix}$（$N_{CA}=e_3$），
$\mathcal L=\begin{bmatrix}1&0&0\\0&1&1\end{bmatrix}$：
- $\mathcal L N_{CA}=(0,1)^{\mathsf T}$ ⟹ **rank $1<2=q_0$**（有秩降）✓
- 行空间交 $=\operatorname{span}\{(1,0,0)\}\ne0$ ⟹ 说有 ✓ **一致**
- 核空间交 $=\operatorname{span}\{(0,1,-1)\}\cap\operatorname{span}\{(0,0,1)\}=0$ ⟹ 说没有 ✗ **矛盾**

$$\Longrightarrow\quad\textbf{行空间版正确，核空间版错误}$$

> ⚠️ **第 11、12 处更正（合并说明）**：
> ① 原文写成行空间版 —— **其实是对的**；
> ② 第 11 处"更正"为核空间版 —— **这才是错的** ✗；
> ③ 数值测试（`verify_T5a.py`）**有 bug**，错误地支持了核空间版 ✗；
> ④ 连带：**T10 撤回** ✗（其论证用核空间版）、**T11 无效** ✗（构造同样基于核空间版）。
>
> **教训**：数值对照与推导冲突时，**必须用手算最小反例定案**——本轮即如此，而且
> 结论是**推翻数值、恢复推导** ✓

**用途**：情形 II 的"秩降"条件 = **纯线性条件**（$\mathcal L$ 的行空间须与该固定子空间相交）✓

#### ⭐ T12′：平行情形下 (A)∧T5a 化为**线性系统**（多项式可判）

设 $\pi(L_0A)=\lambda^*\pi(L_0)$（**平行**）✓。则：

- **(I)**：$(\lambda^*-\lambda_{11})\pi(L_0)=\lambda_{12}\pi(w)$ ⟹ **$\pi(w)\parallel\pi(L_0)$** ✓（$\lambda$'s 自由）
- **(II)**：$\pi(wA)=\lambda_{21}\pi(L_0)+\lambda_{22}\pi(w)$，而 $\pi(w)=t\pi(L_0)$ ⟹ **$\pi(wA)\parallel\pi(L_0)$** ✓

$$\boxed{\ \text{平行情形下}\ (\text{A})\wedge\text{T5a}\iff\exists w:\ \pi(w)\parallel\pi(L_0)\ \wedge\ \pi(wA)\parallel\pi(L_0)\ }$$

**两项各是 $d_{CA}-1$ 个线性方程**（"落在固定的 1 维子空间里"）⟹ **等价于一个线性系统** ✓
$$(\text{A})\wedge\text{T5a}\ \text{在平行情形下}\ \textbf{多项式时间可判}\ ✓$$

> **数值检验**（`test_parallel_case.py`）：
> | 形状 | 平行实例数 | 找到 (A)∧T5a（含秩降）|
> |---|---|---|
> | $n{=}4,p{=}1,r{=}1$（$d_{CA}{=}2$） | 3 | **3/3** ✓ |
> | $n{=}5,p{=}1,r{=}2$（$d_{CA}{=}3$） | 5 | **0/5** |
>
> $$\Longrightarrow\quad \text{平行是}\textbf{必要}（\text{T12}）\text{但}\textbf{不充分}\ \text{——T12′ 是单向结论，平行情形下还有额外约束}\ ✓$$

#### ⭐ T12″：平行情形下 **T5a 被 (A) 蕴含**（故平行情形无简化）

平行时（$\pi(L_0A)\parallel\pi(L_0)$），用 $\lambda_{12}\ne0$ 的分解：
$$(\text{I})\ \ \pi(L_0A)-\lambda_{11}\pi(L_0)=\lambda_{12}\pi(w)$$
左边**本身平行于 $\pi(L_0)$** ⟹ $\pi(w)\parallel\pi(L_0)$ ⟹ **T5a 自动成立** ✓

$$\boxed{\ \text{平行情形：}\ (\text{A})\Longrightarrow\text{T5a}\ }$$

$$\Longrightarrow\quad\textbf{情形 II 的判定}\ \begin{cases}
\pi(L_0A)\not\parallel\pi(L_0)\ (\pi(L_0)\ne0)&\Rightarrow\ \textbf{NO}\quad(\text{T12：多项式、chart-free、已验证})\ ✓\\[2pt]
\pi(L_0A)\parallel\pi(L_0)&\Rightarrow\ \text{T5a 不是额外约束，仍需解}\ (\text{A})\wedge(\text{S})\ \text{——}\textbf{与一般情形同样难，无简化}\ ✗
\end{cases}$$

**⟹ 情形 II 的"可判定"部分到此为止**：T12 给出了**唯一的**简单子情形（不平行 ⟹ NO）；
平行情形**本质困难**，正是 q1 硬度可能藏身之处 ✓

**直观**：$\dim\operatorname{im}H\le\min(q_0,d_{CA})$。
$d_{CA}<q_0$ 时 $\operatorname{im}H$ 是**真子空间**，一般避开有限条特征方向 ⟹ (S) 成立；
$d_{CA}\ge q_0$ 时一般 $\operatorname{im}H=\mathbb C^{q_0}$，含**全部**特征向量 ⟹ (S) 必失败。

### 4.4 三情形（T6、T7、T8）

| 情形 | 条件 | 结论 |
|---|---|---|
| **II** | $d_{CA}\ge q_0$ | $\Sigma^{(S)}\subseteq\{\operatorname{rank}H<q_0\}$（真闭代数集，**零测**）⟹ 随机采样必失败。**(T6)** |
| **I₁** | $d_{CA}=1$ | 失败 $\iff(H\ne0\wedge H\wedge F=0)\vee(H=0\wedge F\ne0)$；见证处 (S) 开 ⟹ **BPP**。**(T7)** |
| **I₂** | $2\le d_{CA}<q_0$ | **无条件二分**：或 (a) $\Sigma_{q_0}$ 含非空开集 ⟹ BPP；或 (b) $\Sigma_{q_0}\subseteq\{\operatorname{rank}H<\beta_{\max}\}$（真闭，零测）⟹ 采样失败。**(T8)** |

**T9**：$\beta_{\max}=\max_\Theta\operatorname{rank}H$ 的最高秩层是开集，故 $\mathcal N^c\subseteq\{\operatorname{rank}H<\beta_{\max}\}$（零测）。

**D1**：$\Theta$-依赖全部集中在 $W_J$ 的第 $r+1,\dots,r+k$ 行且每行内线性、各行变量集互不相交 ⟹ 取 $q_0$ 行算子式次数 $\le k$。
**D2**：$k=1$ 时所有 $q_0$ 阶子式是**仿射**函数 ⟹ $\{\operatorname{rank}H<q_0\}$ 是仿射子空间 ⟹ 判空/求点在多项式时间内可做。

### 4.5 数值证据（非证明）

| 观察 | 数据 |
|---|---|
| 三块约化 ≡ 原始 4 块 (A) | **287/287**（含 $\Theta=0$ 的 True 点） |
| 铅笔既约形式 | **31/31 × 8 实例**（含非平凡 True 点） |
| 情形 II：$(A)$ / $(A)∧(S)$ | 200/200 / **0/200** |
| 情形 I：$(A)∧(S)$ | **87/87** |
| 情形 I：扰动保持 $(A)∧(S)$ | **12/12 × 9 实例** |
| $\operatorname{rank}H=d_{CA}$ 在 $(A)$-点 | **287/287** |
| $(\star''')$ 决定性实验 | **56/56** |
| $(1,3)$ 精确解数 | **恰好 2**（消元法校准 **4/4**） |
| $(1,4)$ 精确解数 | **2–3**（≪ Bézout 界 8） |
| ~~情形 II 可为 YES~~ | ❌ **撤回（第 18 处）**：依据是优化器给出的 $\min\sum(q_0\text{子式})^2\approx 1\text{e-}28$（**浮点近零，非精确零** ✗）—— 正是禁区所禁止的误判（此为其**镜像形式**：把"近零"当"等于零"）。**本轮的精确判定**（校准过的通用构造器）给出 **(A)∧T5a 恒不可解** ✗ |

---

## 5. 未证清单（**不得当作已证引用**）

| 猜想 | 内容 | 证据 | 为什么重要 |
|---|---|---|---|
| **$(\star''')$** | $\Sigma_{q_0}\ne\emptyset\Rightarrow$ 存在**常秩轨迹内**的见证 | 56/56 | 决定 T8 落 (a) 还是 (b) |
| **(C1)** | 情形 II 中 $\nu_{\min}=q_0$ 恒成立 | 24 例全 YES（0 例 NO） | 若真，情形 II 判定平凡 |
| **(C2)** | $\{\operatorname{rank}H<q_0\}$ 上 $(\text{S})$ 恒成立 | 486/486 | (C1) 的关键 |
| **支 B 解数** | $\#\Omega^\star\le\mathrm{poly}$ | $(1,3)$=2、$(1,4)$=2–3 | 决定支 B 是否硬度源 |

**攻过的三次失败路线**（教训，见 §7）：引理 7（锥 vs 子空间）、猜想 (S0)（被证伪）、T5″（循环论证）。

---

## 6. 两条**范围限定**（必须与所有结论一并引用）

### 6.1 P1 图卡限定

#### ⭐ 先说明：**T6 不受本限定约束**（第 ② 项严格化后新增的澄清）

T6 的证明是**逐点**的：

$$\operatorname{rank}H(\mathcal L)=q_0\ \Longrightarrow\ \operatorname{im}H=\mathbb{C}^{q_0}\ \Longrightarrow\ \text{含 }\Lambda\text{ 的全部特征向量}\ \Longrightarrow\ (\text{S})\ \text{失败}$$

它只用到 $H$ **在那一点**的秩，**不需要任何参数化** ✓

$$\Longrightarrow\quad\textbf{T6 的逐点部分对图卡}\textbf{内外的任意}\ \mathcal L\ \text{都成立}\ ✓$$

| 结论 | 受图卡限定？ |
|---|---|
| **T6 逐点部分**（$\operatorname{rank}(\mathcal L N_{CA})=q_0\Rightarrow(\text{S})$ 失败） | ❌ **不受** ✓ |
| T6 的"零测"推论（需"generic 点 $\operatorname{rank}H=q_0$"） | ⚠️ 受（需参数化或独立生成性论证）|
| 引理 1–8、定理 A/B/C、D1/D2、数值 486/486 等 | ✅ 受（均为 $\Theta$-空间陈述）|

#### 限定本身

**图卡条件**：

```
rank(R · N_C · K) = k,   其中 K 是 ker(L_0 · N_C) 的一组基
```

**原因**：P1 的 $W_J$ 底部块 $[I_k|\Theta]$ 恒为秩 $k$，**只能表示"商空间中 $k$ 行独立"的增广**。

**确实存在图卡外的实例**：$L_0=CA^m$ 造出的实例（$n{=}5,p{=}1,r{=}1$，$\eta=[3]$，$q_0=3$，$k=2$）
满足 H1–H4 且 `condA(Lx)=True`，但 $\operatorname{rank}(RN_CK)=1<2$ ⟹ 进不了参数化。

> ⚠️ **本文件 §4 的一切结论仅在图卡内成立，不得声称为全体实例的定理。**

#### 🆕 进一步：它们很可能是**图卡之外的「最小」增广**（故 P1 Thm 3 可能不完整）

`scripts/core/attack_chart.py` 的结果（8/8 实例）：

| 观察 | 结果 |
|---|---|
| $\operatorname{rank}(RN_CK)$ | **1 < k = 2**（图卡外） |
| `p1` 给出 3 行 (A)-增广 | ✓ 存在（上界 3） |
| 搜索 **2 行** (A)-增广（500 个 $\alpha$ × 12 个候选 $v$） | **0 命中** |

**搜索用的参数化**（对 (A) 的条件 (2) $wA\in\operatorname{row}(L_0,w,C,CA)$ 而言**完备**）：

$$wA=\alpha w+\beta L_0+\gamma C+\delta CA
\iff w=v\,(A-\alpha I)^{-1},\qquad v\in\operatorname{span}(L_0,C,CA)\quad(\alpha\ \text{非特征值})$$

**含义**：若这些实例的 2 行增广确实不存在，则它们就是**最小 (A)-增广却落在图卡外**的例子
$$\Longrightarrow\quad\textbf{P1 的 Theorem 3（参数化覆盖所有最小增广）不成立}\ \text{（即源论文有缺口）}$$

#### 搜索的覆盖情况（精确清单）

| 分支 | 覆盖 | 结果 |
|---|---|---|
| 非特征值 $\alpha$ | 500 个有理 α × 12 个候选 $v$（该分支内参数化**完备**） | **0 命中** |
| 实特征值 $\alpha$ | 全部实特征值，最小二乘 + 有理化 + 精确复核 | **0 命中** |
| **复特征值 $\alpha$** | —— | ✅ **可严格排除**：若 $w(A-\alpha I)=v$ 且 $A,w,v$ 实，取共轭得 $w(A-\bar\alpha I)=v$，相减得 $w(\bar\alpha-\alpha)=0\Rightarrow w=0\Rightarrow v=0$ ✗ |
| **(A) 分解路线** | 见下；本质**只有 1 个参数** $\lambda_{11}$ | **0 命中**（系统**无解**） |

#### (A) 分解路线（第 4 条独立证据，且搜索空间本质 1 维）

由 $(\text{A})\iff\exists\Lambda,G_0,G_1:\ \mathcal LA=\Lambda\mathcal L+G_0C+G_1CA$，消去 $G$ 得（$\pi$ = 到 $\operatorname{row}(C,CA)^\perp$ 的投影）：

$$(\text{I})\ \ \pi(L_0A-\lambda_{11}L_0)=\lambda_{12}\pi(w)
\qquad
(\text{II})\ \ \pi(wA-\lambda_{21}L_0-\lambda_{22}w)=0$$

**(I) 把 $\pi(w)$ 完全钉死** ⟹ 只需扫一个参数 $\lambda_{11}$ ✓
脚本 `attack_chart_decomp.py`：扫 6–80 个 $\lambda_{11}$，每个点精确解 (I)∧(II) ⟹ **系统全部无解** ✓
诊断脚本 `diag_decomp.py` 逐步手工核对确认：**不是实现 bug，是系统真的不相容** ✓

> **曾误以为存在矛盾**（"6 方程 / 7 未知量 ⟹ 一般可解"）——**该启发式是错的** ✓：
> (I) 把 $\pi(w)$ 钉死后，(II) 的右端只能落在 $\operatorname{span}(\pi(L_0),u)$（2 维）内，
> 而左端随 $w$ 变化，**两者在耦合下同时匹配**并非一般成立 ✓

> ⚠️ **仍未完全严格**：$\lambda_{11}$ 是**采样**的（虽然是 1 维、且条件关于 $\lambda_{11}$ 是多项式的）。
> **严格化的收尾**：把该相容性条件作为 $\lambda_{11}$ 的多项式算出来（插值），检查是否恒不相容——**本轮未做**。

#### 稠密网格收尾（第 5 条，最强）

`attack_chart_grid.py`：对每个实例扫 **588 个**有理 $\lambda_{11}$（$p/q$，$|p|\le24$，$q\le12$），
每点**精确**判定 (I)∧(II) 的相容性：

| 实例 | 扫过 $\lambda_{11}$ | 相容数 |
|---|---|---|
| 5 个生成器实例（$n{=}5,p{=}1,r{=}1$，$\eta=[3]$，$k=2$，$\operatorname{rank}(RN_CK)=1$） | **588** | **0** |

**（若相容性条件关于 $\lambda$ 是多项式的，有解时通常存在小分母有理点 ⟹ 网格有意义。）**

---

### ⭐ 结论（**已更正**）：$q_0$ 得到支持；**P1 参数化未被推翻**

> ⚠️⚠️ **第 13 处更正（重大）**：曾断言"这些实例在 P1 图卡之外（$\operatorname{rank}(RN_CK)=1<k$）
> ⟹ P1 Theorem 3 不完整" —— **该断言是计算 artifact，已撤回** ✗
>
> **病根**：库函数 `mm(X,Y)` 用 `k = len(Y)` 作收缩长度且**不检查** `len(X[0]) == len(Y)` ✗；
> 我算 $\operatorname{rank}(RN_CK)$ 时写成 `mm(RNC, Kr)`（`Kr` = $K^{\mathsf T}$，维数 $m_K\times d_C$）✗，
> 正确写法是 `mm(RNC, K)`（$d_C\times m_K$）✓
>
> **修正后重算**（`recompute_rho_fixed.py`，8 实例 × 60 样本）：
> $$\operatorname{rank}(RN_CK)=\mathbf{k=2}\ \text{（480/480）}\ \Longrightarrow\ \textbf{这些实例在 P1 图卡内}\ ✓$$
> 且"$\operatorname{rank}(RN_CK)<k\iff\exists0\ne y:\ y^{\mathsf T}RN_C\in\operatorname{row}(L_0N_C)$"
> 的两个独立判据**完全一致** ⟹ **该线性刻画成立** ✓

| 命题 | 证据 | 判断 |
|---|---|---|
| **该实例的最小 (A)-增广行数 $=3$** | 六条路线 + **严格子式插值**都找不到 2 行增广 | ✅ **$q_0=\sum\eta_j$ 得到支持**（$\eta$ **没有**高估）|
| ~~P1 的 $W_J(\Theta)$ 参数化不覆盖所有最小增广~~ | ~~$\operatorname{rank}(RN_CK)=1<k$~~ | ❌ **撤回**（artifact）；修正后 $\operatorname{rank}=k$ ⟹ **参数化适用** ✓ |

$$\boxed{\ q_0=\sum\eta_j\ \text{得到独立支持};\qquad \textbf{P1 参数化未被推翻（第 ② 项"发现"撤回）}\ }$$

**对本项目的意义（更正后）**：

1. ✅ **$q_0$（以及精确阈值）得到独立支持**——且不再有"参数化不完整"的隐患；
2. ✅ **§4 的 $\Theta$ 相关结论适用**——生成器实例**在图卡内** ✓（原先的"限定"是假的 ✗）；
3. ⚠️ **第 ② 项作为"规划任务"已无内容**——但它的**副产品**（(I)∧(II) 系统 + 子式插值技术、
   T5a、T12、T12′、T12″）**全部保留有效** ✓

> ✅ **无残留缺口**：$\lambda_{12}=0$ 的分支要求 $u(\lambda_{11})=\pi(L_0A)-\lambda_{11}\pi(L_0)=0$，
> 即有解 ⟺ $\pi(L_0A)\parallel\pi(L_0)$。`close_lambda12_gap.py` 对 **8/8** 实例算得
> $\operatorname{rank}[\pi(L_0);\pi(L_0A)]=2$（**不平行**）⟹ **该分支为空** ✓
> 故上述严格结论**无缺口**。

#### ✅ 严格收尾（第 6 条，**严格**）

`attack_chart_rigorous.py`：把 $M(\lambda)$ 与 $[M|b](\lambda)$ 的**全部** $6\times6$ 子式
**插值成 $\lambda$ 的多项式**（次数 $\le6$，用 7 个插值点），再精确检查：

| 实例 | $M$ 的全部 $6\times6$ 子式 $\equiv0$? | $[M\lvert b]$ 子式的 gcd 次数 | 结论 |
|---|---|---|---|
| 1–3 | **True** | **0（非零常数）** | **恒不相容** |

**推理链（严格）**：

$$\text{全部 }6\times6\text{ 子式}\equiv0\ \Longrightarrow\ \operatorname{rank}M(\lambda)\le5\ \ \forall\lambda$$
$$\text{gcd 为非零常数}\ \Longrightarrow\ \text{子式无公共零点}\ \Longrightarrow\ \operatorname{rank}[M|b](\lambda)=6\ \ \forall\lambda$$
$$6>\operatorname{rank}M\ \Longrightarrow\ \text{增广矩阵秩严格大于系数矩阵秩}\ \Longrightarrow\ \textbf{恒不相容}\quad\square$$

$$\boxed{\ \text{严格确认：这些实例}\textbf{不存在 2 行 (A)-增广} \Longrightarrow \text{最小行数}=3=q_0\ \text{（与}\ \eta\ \text{一致）}\ }$$

> ⚠️ **第 13 处更正**：上式原写作"⟹ **图卡外的最小增广** ⟹ **P1 Theorem 3 不完整**"——
> **后两步已撤回** ✗（"图卡外"是 `mm(RNC,Kr)` 维数错配造成的 artifact；
> 修正后 $\operatorname{rank}(RN_CK)=k$ ⟹ 这些实例**在图卡内** ✓）。
> **保留的部分**：不存在 2 行 (A)-增广 ⟹ 最小行数 $=3=q_0$ ⟹ **$\eta$ 未高估** ✓

### 6.2 $q_0$ 无独立验证

- **上界**可验证：`p1` 给出恰好 $q_0$ 行的可行增广 ✓
- **下界**（"没有更少行的增广"）**只能引用 P1 Theorem 2**，本项目**未独立验证**
- 且已**证明**暴力/随机法原理上做不到：暴力枚举轨道行的子集**不完备**（最小增广的行可以是轨道行的线性组合）；随机方向 **0 命中** ⟹ 可行集是**零测代数集**，采样必错过

> ⚠️ **$q_0$ 是全项目阈值的核心，却只有一个来源——这是最重要的单点依赖。**
> **新增证据（§6.1 第 6 条，严格）**：对生成器实例，**严格确认**不存在 2 行 (A)-增广
> ⟹ 最小行数 $=3=\eta_1$ ⟹ **$\eta$ 在这些实例上未高估** ✓
> （此前曾推断"$\operatorname{rank}(RN_CK)<k\Rightarrow$ 非最小"，**该推断错误**：子空间相关 $\ne$ 全局相关；
> 正确的路径是 §6.1 的 (I)∧(II) 系统。）
> **但下界的普遍性仍只有 P1 Theorem 2 一个来源，未独立验证。**

---

## 7. 作废清单（**10 处，不得引用**）

| # | 曾主张 | 错在哪 |
|---|---|---|
| 1 | $(\text{A})\iff$ 秩满 | 实为**单向**（秩满 $\Rightarrow$ (A)） |
| 2 | **引理 4**：$\Omega^\star$ 是 Zariski-闭集 | **假**。反例 $M=(a),N=(b)$；错因：$(Z,M)\mapsto(M,ZM)$ 是**双线性**而非线性 |
| 3 | **引理 5**：$(\text{S})$ 是 Zariski-开集（一般情形） | **假**（$d_{CA}\ge q_0$ 时；实测 0/200） |
| 4 | **引理 7**：失败集在每个 rank 层内闭 | **无效**。$\ker\varphi=\{w:\varphi(w)=0\}$ 是**锥（代数集）而非子空间**；"$\ker\varphi\not\subseteq\ker H\Rightarrow\dim\ker\varphi>\dim\ker H$" 不成立 |
| 5 | **猜想 (S0)**：$\operatorname{rank}H\equiv d_{CA}$ | **被证伪**（子式最小值 $=0$） |
| 6 | 旧 `condS` 判据 | **不可靠**（只在 $A$ 的特征值处检验，与 (S) 必须在 $T=\Lambda$ 处检验不符）⟹ 基于它的数值结论全部作废 |
| 7 | "**P1：q1 的 NP-hard 断言为假**" | **过度断言**。错因：把"是代数判定"当成"不是 NP-hard"，而 **ETR 本身是 NP-hard**；PSPACE ⊇ NP 亦不排除 |
| 8 | **定理 C** 的陈述：$d_{CA}=1$ 时失败 $\iff H\wedge F=0$ | **漏了 $H=0$ 的情形**（结论 BPP 仍成立，但陈述与证明已更正） |
| 9 | **T5″**：$\operatorname{rank}H<q_0\Rightarrow(\operatorname{im}H)^\perp$ 是 $\Lambda^T$-不变 | **循环论证**。$F=\Lambda H$ 只给"$y^T\Lambda H=0\Rightarrow y^TF=0$"（方向相反） |
| 10 | "$\operatorname{rank}(RN_CK)<k\Rightarrow$ 非最小 $\Rightarrow\eta$ 高估" | **错**。子空间上相关 $\ne$ 全局相关 |
| 11 | **T5a 的原写法**：$\operatorname{rank}(\mathcal L N_{CA})<q_0\iff\operatorname{row}(\mathcal L)\cap\operatorname{row}(C,CA)\ne0$ | **错**。把**核空间**条件误写成**行空间**条件。**正确形式**：$\iff\ker\mathcal L\cap\ker[C;CA]\ne0\iff\operatorname{rank}[\mathcal L;C;CA]<n$（已证并验证 6/6 × 120） |
| 12 | T5a 的"更正"本身 + 由核空间版推出的 T10、T11 | **错**。**行空间版才是对的**（用手算反例定案：$[C;CA]=\operatorname{diag}(1,1,0)$、$\mathcal L=\begin{bmatrix}1&0&0\\0&1&1\end{bmatrix}$）⟹ **T10 撤回、T11 无效** |
| 13 | "生成器实例在 P1 图卡之外 ⟹ P1 Theorem 3 不完整" | **错**。`mm(RNC,Kr)` 的**维数错配**（`mm` 不检查 `len(X[0])==len(Y)`）✗；正确写法 `mm(RNC,K)` ⟹ $\operatorname{rank}(RN_CK)=k$ ⟹ **实例在图卡内** ⟹ 该结论与**任务 B 的动机**一并撤回 |
| 14 | T12″："平行 ⟹ (A) ⟹ T5a" | **论证错**（漏了 $\lambda_{12}=0$ 分支，此时 $\pi(w)$ 自由）✗；**结论（平行情形无简化）仍成立**，但理由要改为"$\lambda_{12}=0$ 分支" |
| 15 | "任务 A 有靶子（平行区存在 NO 实例）" | **错**。基于 $r{=}1$ 的错误系统 ✗ |
| 16 | **c5**："情形 II 整体多项式可判" | **错**。判定是**空洞**的（系统齐次 ⟹ 零解恒存在）✗；构造出 $w=0$ |
| 17 | **矛盾"$\pi(L_0A)=0$ 但 (A) 失败"** | ✅ **已解决**：**(I)∧(II) 只对 $q_0=2$ 成立** ✗；平行实例是 $q_0=3$，漏了一条行条件 ⟹ 构造不满足 (A)。⭐ **好消息：不是 `rk`/`ker_basis` 的问题，全库基础函数可靠** ✓ |
| 18 | **"情形 II 可为 YES 6/6"**（`test_caseII_YES.py`，曾写入 §4.5） | **撤回** ✗。依据是优化器输出的 $\min\sum(q_0\text{子式})^2\approx 1\text{e-}28$（**浮点近零，非精确零** ✗），正是禁区禁止的误判（**镜像形式**：把"近零"当"等于零"）。**本轮的精确判定**（校准过的 `gen_A_system.py`）给出 **(A)∧T5a 在情形 II 平行中恒不可解** ✗ ⟹ **以精确者为准** ✓ |
| 19 | 把**条件命题**（$\Lambda_{13}\ne0\Rightarrow$ T5a）当成**存在性命题** | **逻辑失误** ✗（曾据此误报"张力"）。**澄清后无矛盾** ✓ |
| 20 | **用于筛选"平行"实例的判据**（`pL0 = π(L_0 的第一行)`）| **根本性方法错误** ✗：真正的平行是 $\operatorname{rank}[\pi(L_0);\pi(L_0A)]=1$（**全部 $r$ 行**）。对 $r\ge2$ 前者**太弱** ⟹ **c6 的三轮探针全部失效（已撤回）**；**T12 的验证只覆盖了更弱的陈述**（T12 的**证明**不受影响 ✓）。本轮 ℓ-free 判定暴露了它：7 个实例"投影条件满足但 (A) 失败" ✗ |

**另有**："$\Omega^\star$ 恰为单点"（$(1,3)$ 恰 2 个解，已撤回）；
旧"$(A)\iff\pi(R)$ 是 $\bar A$-不变"（$\bar A$ 在 $Z/W$ 上未定义，已撤回）；
更早的 $K/K'$ 判据（实现无法复现三块判据，**搁置**）。

---

## 7.5 ⭐⭐ **本会话最新结论（第 31 处起，**取代**第 30 处）**

> ⚠️ **第 30 处（obs 判据）的强形式已被反驳**（见 `history/52` §7.24.8）。
> **以下为当前有效结论。**

### 7.5.1 ⭐⭐⭐⭐ **定律：$\operatorname{rank}(\text{解})=\text{obs}$**（4/4）

$$\text{obs}:=\dim V,\qquad V:=\big\langle\operatorname{row}(R)\big\rangle_{A'}=\text{含}\operatorname{row}R\ \text{的最小}\ A'\text{-不变子空间}$$
$$A'=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN,\qquad R=AN-NA'$$

| 实例 | $d$ | obs | 观到的 $\rho$ | 解数 |
|---|---|---|---|---|
| $n{=}4$ t=0 | 2 | 2 | 2 | 456 |
| $n{=}4$ t=5 | 2 | 1 | 1 | 80 |
| $n{=}5$ t=0 | 3 | 3 | 3 | 2058 |
| $n{=}5$ t=7 | 3 | 2 | 2 | **16,848**（$\{-1,0,1\}^{12}$ 全枚举）|

### 7.5.2 ⭐⭐⭐⭐⭐ **统一判据（23/23）**

$$\boxed{\ \textbf{YES at}\ q{=}d_{CA}{+}1\iff\alpha_0=L_0N\ \in\ V=\big\langle\operatorname{row}R\big\rangle_{A'}\ }$$

### 7.5.3 ✅✅ **充分性：已构造性证明**

$$\alpha_i=e_i\ (\text{可行：}L\mapsto LN\ \text{满射}),\quad A_0=I_d\ \Longrightarrow\ \ker A_0=0\ \Longrightarrow\ \textbf{(5a)}\ \textbf{自动}$$
$$A_1=A'+B,\quad B\ \text{的行}=\ell_iR\ (\ell_iN=e_i)\ ;\qquad \textbf{(5b)}\iff\operatorname{charpoly}(A_1)\ \text{无有理根}$$
$$\text{存在性}：\operatorname{charpoly}(A'+\Lambda R)\ \text{可任意配置}\iff(A'^{\mathsf T},R^{\mathsf T})\ \text{可控}\iff\boxed{\text{obs}=d}$$
$$\Longrightarrow\ \text{取}\ d\ \text{次不可约}\ p\ \Longrightarrow\ \exists\Lambda:\ \operatorname{charpoly}=p\ \text{无有理根}\ \Longrightarrow\ \textbf{(5b)}\ ✓$$

$$\text{数值}：\text{随机}\ \ell_i\ \text{下"无根率"}\ 80\text{–}97\%\ ;\ \text{命中构造的}\ (5a)\wedge(5b)\ \textbf{全部 True}\ (5/5)$$

$$\text{结合归约（}\alpha_0\in V\Rightarrow\text{限制到}\ V\ \text{上}\ \text{obs}'=\dim V=d'\Rightarrow\text{YES）}\ \Longrightarrow\ \boxed{\alpha_0\in V\Rightarrow\text{YES}}$$

### 7.5.4 ⚠️ **必要性：仅实证**

$$\alpha_0\notin V\ \Longrightarrow\ \textbf{NO}\qquad(23/23\ \text{一致};\ \text{含 c19 的}\ 531{,}441\ \text{全枚举无解})$$
$$\text{机制草图}：\text{模}\ V\ \text{的铅笔含}\ \bar\alpha_0(\lambda I-\bar A')\ \text{项}\ ;\ \text{缺口}=\bar A'\ \text{的特征值须在}\ \mathbb{Q}\ \ —\ \textbf{未证}$$

### 7.5.5 **q1 的最新定位**

| 说法 | 状态 |
|---|---|
| "q1 是 NP-hard" | ❌ **很可能为假**（判据充分性已证，必要性 23/23 支持）|
| "$q{=}d_{CA}{+}1$ 的判定是多项式的" | ⚠️ 前提（$\rho\ge\mathrm{obs}$）**已于 2026-10-19 被反例推翻** ⟹ 本条作废 ✗ |
| "$\alpha_0\in V\Rightarrow$ YES" | ✅ **已证**（构造 + pole placement）|

$$\boxed{\ \text{q1}\ \textbf{只剩必要性}\ (\alpha_0\notin V\Rightarrow\text{NO})\ \text{未证}\ }$$

### 7.5.6 ⭐⭐⭐⭐ **必要性机制（第 30 处之后的重大进展）**

**先说清楚障碍在哪条条件**（`c43_diagnose_necessity.py` + `c44_rank_vs_5a.py`）：

$$\alpha_0\notin V\ \text{的实例上，按}\ \operatorname{rank}(A_0)\ \text{分层统计}\ (5a)\ \text{通过率}$$

| 实例 | $\operatorname{rank}(A_0)=1$（$=$obs）| $\operatorname{rank}(A_0)=2$ |
|---|---|---|
| trial 0/1/7（$d{=}2$, obs$=1$）| **9 个，过 (5a) 0（0%）** | 720 个，过 **720（100%）** |

$$\boxed{\ \alpha_0\notin V\ \text{时，}\operatorname{rank}(A_0)=\text{obs}\ \text{的候选}\ \textbf{一律过不了}\ (5a)\qquad(\mathbf{3/3})\ }$$

**机制**：

$$\text{解必须}\ \rho=\text{obs}\quad(\textbf{定律}\ 7.5.1)\ \Longrightarrow\ \operatorname{rank}A_0=\text{obs}=\dim V$$
$$(\text{5a})\iff A_1=\Lambda A_0\ \Longrightarrow\ \operatorname{row}(A_1)\subseteq\operatorname{row}(A_0)=:U,\quad \dim U=\text{obs}$$
$$\gamma_0=\alpha_0A'+\beta_0\in U\ ;\qquad \beta_0=L_0R\in\operatorname{row}R\subseteq V$$
$$\text{mod}\ V：\ \bar\gamma_0=\bar\alpha_0\bar A'\ne0\quad(\alpha_0\notin V)$$
$$\Longrightarrow\ U\ (\dim=\text{obs}=\dim V)\ \text{容纳不下}\ \alpha_0\ \text{与}\ \gamma_0\ \text{的}\ V\ \text{外分量}\ \Longrightarrow\ \textbf{无解}\ ✓$$

$$\boxed{\ \textbf{必要性}：\text{障碍在}\ (5a)\ ——\ \gamma_0\notin\operatorname{row}(A_0)\ \text{的可达范围}\ }$$

### 7.5.7 **必要性的证据（诚实清单）**

| # | 实例 | $d$ | 方式 | 结果 |
|---|---|---|---|---|
| 1 | **c19** | 3 | **531,441 穷尽** | 0 |
| 2 | $n{=}4$ t=1 | 2 | 采样 420 | 0 |
| 3–7 | **5 个定向构造** | 2 | **各 729 穷尽** | **0** |

$$\boxed{\ \text{必要性}：\ \mathbf{7}\ \text{个实例（}\mathbf{6}\ \text{个穷尽枚举）全部 NO}\ +\ \textbf{机制已找到}\ }$$

$$\text{（此前"仅 2 个实例"的薄弱状态已改善；"23/23" 的正确读法：充分性 21/21，必要性 7/7）}$$

### 7.5.8 **本会话的最终状态**

| 类别 | 内容 | 状态 |
|---|---|---|
| **Lean 45 定理** | $(A)\iff$分解$\iff$核条件；$K\subseteq\ker(CA^2)\Rightarrow(5b)$ 恒失败 | ✅ 严格 |
| **引理** | $q\le d_{CA}\wedge\rho{=}q\Rightarrow(5b)$ 不可能 | ✅ 严格 |
| **枚举** | c19 531,441 无解；t=7 16,848 解；5 个定向构造各 729 无解 | ✅ 严格 |
| **充分性** | $\alpha_0\in V\Rightarrow$ **YES**（构造 + pole placement）| ✅ **已证** |
| **定律（4/4）** | $\operatorname{rank}(\text{解})=\text{obs}$ | ⭐ 待证 |
| **判据** | **YES $\iff$ $\alpha_0\in V$** | ⭐ |
| **必要性** | 7 实例（6 穷尽）全 NO + **机制已找到** | ✅ 机制 |
| **待证** | ① **定律** $\operatorname{rank}(\text{解})=\text{obs}$；② 必要性的**严格证明**（依赖①）| ⚠️ |

$$\boxed{\ \text{q1 的判据}\ \textbf{两侧都已找到};\ \text{充分性}\ \textbf{已证};\ \text{必要性}\ \textbf{机制已找到但证明依赖定律}\ }$$

$$\Longrightarrow\ \textbf{若定律与必要性严格化}\ \Longrightarrow\ \textbf{判定多项式}\ \Longrightarrow\ \textbf{q1 为假（NP-hardness 不成立）}$$

$$\text{已部分推进：}\rho=\operatorname{rank}A_0\ \text{可由}\ (\text{5b})\ \text{推出（}\lambda\to\infty\ \text{的秩半连续性）};\ \text{剩}\ \operatorname{rank}A_0=\text{obs}$$

### 7.5.9 ⭐⭐ **本轮新增的两个严格结果**

**(A) $(5b)$ 的新代数判据**

$$\Lambda\ \text{在}\ E:=\operatorname{im}(H)\ \text{上被唯一确定}：\ \Lambda(Hx)=Fx=:T$$
$$E_{k+1}=\{v\in E_k:\ Tv\in E_k\},\qquad E_\infty=\text{稳定值}$$
$$\boxed{\ (\text{5b})\iff E_\infty=0\iff\operatorname{im}(H)\ \textbf{不含非零}\ T\text{-不变子空间}\ }$$

$$\text{验证}：\textbf{16/16}\ (\text{8 个}\ E_\infty=0\ \text{对应 (5b) 真};\ \text{8 个}\ E_\infty\ne0\ \text{对应假})$$

**(B) $\rho>\text{obs}$ 的结构标志**

$$\dim\ker H=d-\rho,\quad \dim V=\text{obs}\ \Longrightarrow\ \rho>\text{obs}\Rightarrow\dim(\ker H+V)<d$$
$$\boxed{\ \rho>\text{obs}\ \Longrightarrow\ U\cap V^\perp\ne0\qquad(\text{验证}\ \textbf{10/10})\ }$$

**(C) 必要性的分层机制**（$7$ 实例 $\times$ 2500 样本，全部 $\alpha_0\notin V$）

$$\begin{cases}
\rho=\text{obs}\ \text{层}： & (\text{5a})\ \text{败}\quad(\gamma_0=L_0AN\ \textbf{固定})\\
\rho>\text{obs}\ \text{层}： & (\text{5b})\ \text{败}\quad(100\%)
\end{cases}\qquad\Longrightarrow\ \textbf{无解}$$

### 7.5.10 **证明状态的最终汇总**

| 项 | 状态 |
|---|---|
| $(A)\iff$ 分解 $\iff$ 核条件 | ✅ **Lean 45 定理** |
| 六步化简到 $2d$ 维 | ✅ 各 400/400 |
| **充分性** $\alpha_0\in V\Rightarrow$ YES | ✅ **已证** |
| $(5b)\iff E_\infty=0$ | ✅ 16/16 |
| $\rho=\operatorname{rank}A_0$；$\bar U$ 非零不变；$U\cap V^\perp\ne0$ | ✅ 严格 |
| $\rho\le\text{obs}$（$\bar A'$ 有基域特征值时）| ✅ 严格 |
| 定律 $\operatorname{rank}(\text{解})=\text{obs}$ | ⭐ 4/4 完全枚举 |
| 必要性 | ✅ 机制已找到（分层）；⚠️ 严格证明依赖"$\rho>\text{obs}\Rightarrow E_\infty\ne0$" |

$$\boxed{\ \textbf{唯一剩余}：\rho>\text{obs}\Rightarrow E_\infty\ne0\ \ (\text{即 (5b) 必败})\ }$$

$$\Longrightarrow\ \text{若得证}\ \Longrightarrow\ \text{定律}\ \Longrightarrow\ \text{必要性}\ \Longrightarrow\ \textbf{判定多项式}\ \Longrightarrow\ \textbf{q1 为假}$$

### 7.5.11 ⭐⭐⭐⭐ **判据与 $q$ 无关（含单调性）**

$$\textbf{单调性（已证）}：\text{YES at}\ q\ \Longrightarrow\ \text{YES at}\ q+1\quad(\text{把}\ R\ \text{补零行})$$

$$\boxed{\ \text{YES at 某个}\ q\iff\alpha_0:=L_0N\ \in\ V\ }$$

| 方向 | 依据 | 状态 |
|---|---|---|
| $\alpha_0\in V\Rightarrow$ YES at $d_{CA}{+}1$ | 构造 $A_0{=}I$ + pole placement | ✅ **已证** |
| $\alpha_0\notin V\Rightarrow$ NO at $q\le d_{CA}{+}1$ | 单调性 + $d{+}1$ 处判据 | ✅（modulo 缺口①）|
| $\alpha_0\notin V\Rightarrow$ NO at $q>d_{CA}{+}1$ | $q=d{+}2,d{+}3$ 实验 | ⚠️ **0/7200** |

$$\Longrightarrow\ \textbf{判定}\ =\ \text{"}\alpha_0\in V?\text{"}\ \Longrightarrow\ \textbf{多项式}\ \Longrightarrow\ \textbf{q1 为假}\ (\text{若①成立})$$

### 7.5.12 ⭐⭐⭐ **A10 的两个形式（其一未证）**

$$\textbf{形式 I（已验证 144 实例，未证）}：(\text{5b})\iff F^{\mathsf T}u_0,\ldots,F^{\mathsf T}u_{d-1}\ \text{无关}$$

$$\textbf{形式 II（2 行严格推导；无法用有理工具验证）}：$$
$$(\text{5b})\iff\nexists\lambda\in\mathbb{C},\ 0\ne z:\ \Lambda z=\lambda z\ \wedge\ \langle z,\varphi\rangle=0$$

$$\textbf{自由度（已证）}：\Lambda=\Lambda_0+\varphi c^{\mathsf T}\ (c\in\mathbb{R}^q)\ \Longrightarrow\ \text{(5b) 是}\ \exists\Lambda\ \text{条件}$$

$$\textbf{这解释}：\text{一般}\ \Lambda\ \text{下 (5b)}\ 60\%\ \text{成立};\quad \alpha_0\notin V\ \text{时}\ 100\%\ \text{失败}$$

### 7.5.13 **证明状态的最终汇总（诚实版）**

| 类别 | 内容 |
|---|---|
| ✅ **已严格证明** | $(A)\iff$分解$\iff$核条件（**Lean 49 定理**）；六步化简；**充分性**；**单调性**；$F^{\mathsf T}(\mathcal N)\subseteq W_0$；$\Lambda=\Lambda_0+\varphi c^{\mathsf T}$；形式 II 的 2 行推导；$U\cap V^\perp\ne0$（Lean）|
| ⚠️ **已实证未证** | A10 形式 I（**144**）；$\rho{=}d$ 定理（**120**）；判据（$p{=}1,2\times d{=}2,3,4$）；$\alpha_0\notin V\Rightarrow$NO（**40,000+**）；$q$-无关性 |
| ❌ **未证（关键）** | **A10**；$\text{obs}<\rho\Rightarrow\forall c$ 坏；$q>d{+}3$ 的必要性 |

$$\boxed{\ \textbf{本会话未完成 q1 的证明}\ ;\ \text{完成的是：化简、充分性、大量结构引理、关键缺口的代数化}\ }$$

$$\text{更正：}\mathbf{34}\ \text{处（26 处自证伪）};\qquad \mathbf{0}\ \text{处 Lean 级已证结论被推翻}\ \checkmark$$

### 7.5.14 **已知无效的路线（不要再走）**

| # | 尝试 | 失败原因 |
|---|---|---|
| 1 | $\bar A'$ 在 $\mathbb{R}^d/V$ 上的有理特征值 | c19、t=1 无有理特征值 |
| 2 | $\forall y:\ y^{\mathsf T}A_1\not\parallel y^{\mathsf T}A_0$ | 平凡条件 |
| 3 | $\alpha_0A'\notin\operatorname{span}(\alpha_0)+W_0$ | 实测 $\in$ |
| 4 | $\Lambda|_{\operatorname{im}H}$ 是算子 | $\operatorname{im}H$ 非 $\Lambda$-不变 |
| 5 | $H(V)$ 是 $\Lambda$-不变 | $\mathcal LR$ 项出界 |
| 6 | $S_0=\{x:Rx\in\ker\mathcal L\}$ 迭代 | $A'S_0\not\subseteq S_0$ |
| 7 | $w\in U\cap V^\perp$ 的 $w\cdot\gamma_0$ | 无矛盾 |
| 8 | 只用 $\ker M^{\mathsf T}$ 的像 | 只有 $e$ 维；迭代离开 $\ker M^{\mathsf T}$ |

### 7.5.15 🎉🎉🎉 **A19：定律的证明（$\rho\le\text{obs}$）—— 经 PBH 测试**

$$\boxed{\ \textbf{定理}：\ (\text{5a})\wedge(\text{5b})\ \Longrightarrow\ \rho:=\operatorname{rank}A_0\le\text{obs}\ }$$

**证明（6 步）**：

| 步 | 内容 | 依据 |
|---|---|---|
| **1** | $(\text{5b})\iff\operatorname{rank}\big[\Lambda^{\mathsf T}-\lambda I\ \big|\ \mathcal N\big]=q\ \ \forall\lambda$，$\mathcal N=\ker M^{\mathsf T}$ | A11′（2 行推导）|
| **2** | ⟺ $(\Lambda^{\mathsf T},\mathcal N)$ **可控** | **PBH 测试（经典定理）** |
| **3** | ⟹ $K:=\sum_{k\ge0}(\Lambda^{\mathsf T})^k\mathcal N=\mathbb{R}^q$ | 可控性定义 |
| **4** | $F^{\mathsf T}(K)\subseteq\tilde V$，$\dim\tilde V=\text{obs}$ | 递归（下面给出）|
| **5** | $\operatorname{im}F^{\mathsf T}=F^{\mathsf T}(\mathbb{R}^q)\subseteq\tilde V$ | 3+4 |
| **6** | $(\text{5b})$ 在 $\lambda=0$：$\operatorname{rank}F=\rho$ ⟹ $\dim\operatorname{im}F^{\mathsf T}=\rho$ | 严格 |

**递归（步 4 的依据）**：
$$\tilde V:=\sum_{t\ge0}(A'^{\mathsf T})^t\operatorname{row}(R)\ ;\qquad F^{\mathsf T}=A'^{\mathsf T}M^{\mathsf T}+R^{\mathsf T}\mathcal L^{\mathsf T}$$
$$\text{对}\ u_0\in\mathcal N:\ F^{\mathsf T}u_0=R^{\mathsf T}\mathcal L^{\mathsf T}u_0\in\operatorname{row}R\subseteq\tilde V$$
$$u_{k+1}=\Lambda^{\mathsf T}u_k:\ F^{\mathsf T}u_{k+1}=A'^{\mathsf T}\big(\underbrace{M^{\mathsf T}u_{k+1}}_{=F^{\mathsf T}u_k}\big)+R^{\mathsf T}\mathcal L^{\mathsf T}u_{k+1}\in A'^{\mathsf T}\tilde V+\tilde V=\tilde V$$

$$\boxed{\ \rho=\dim\operatorname{im}F^{\mathsf T}\le\dim\tilde V=\text{obs}\ \Longrightarrow\ \rho>\text{obs}\ \textbf{时无解}\ }$$

**验证**：`c79_LAW_PROOF.py`，16 个 (5b) 成立的实例：$\dim K=q$ 全部成立，$\dim\operatorname{im}F^{\mathsf T}=\rho$ 全部成立 ✓

$$\textbf{关键洞察}：\text{此前一直用}\ \textbf{单输入}\ (\text{cyclic vector})\ \text{框架}\ ✗\ ;\ \text{正确的是}\ \textbf{多输入可控性}\ (\text{PBH})\ ✓$$
$$\text{A10（}\rho{=}d\text{）是单输入特例（}\mathcal N=\langle\varphi\rangle\text{）}\ ✓$$

### 7.5.16 **A19 的直接推论**

$$\boxed{\ \rho>\text{obs}\ \Longrightarrow\ \textbf{无解}\qquad(\text{已证})\ }$$

$$\text{故解的}\ \operatorname{rank}\ \text{必}\ \le\text{obs}\ ;\quad \text{而所有已知解都满足}\ \operatorname{rank}=\text{obs}\ (\text{充分性构造})$$

### 7.5.17 **剩余的精确形态**

$$\boxed{\ \text{待证}：\ \rho\le\text{obs}\ \wedge\ \alpha_0\notin V\ \Longrightarrow\ \text{(5a) 失败}\ }$$

$$\text{实证}：\rho{<}\text{obs}\ \text{层}\ 0/67\ ;\quad \rho{=}\text{obs}\ \text{层}\ 0/522\ (c44)$$

### 7.5.18 🎉🎉🎉🎉🎉 **A20：判据的必要性已证 —— 判据完全成立**

$$\boxed{\ \textbf{定理}：\ (\text{5a})\wedge(\text{5b})\ \Longrightarrow\ \alpha_0=L_0N\in V\ }$$

**证明（6 步）**：

| 步 | 内容 | 依据 |
|---|---|---|
| **1** | $(\text{5a})\Rightarrow F=\Lambda M\Rightarrow F^{\mathsf T}=M^{\mathsf T}\Lambda^{\mathsf T}\Rightarrow\mathrm{im}F^{\mathsf T}\subseteq\mathrm{im}M^{\mathsf T}$ | 初等 |
| **2** | $(\text{5b})\Rightarrow$ PBH $\Rightarrow K=\mathbb{R}^q\Rightarrow\mathrm{im}F^{\mathsf T}\subseteq\tilde V$，$\dim\tilde V=\text{obs}$ | **A19 的证明（§7.5.15）** |
| **3** | $(\text{5b})$ 在 $\lambda=0$：$\operatorname{rank}F=\rho$ ⟹ $\dim\mathrm{im}F^{\mathsf T}=\rho$ | 严格 |
| **4** | $\dim\mathrm{im}M^{\mathsf T}=\operatorname{rank}M=\rho$ | 严格 |
| **5** | $\mathrm{im}F^{\mathsf T}\subseteq\mathrm{im}M^{\mathsf T}\cap\tilde V$ 且左端 $\dim=\rho$，右端 $\dim\le\rho$ ⟹ **$\mathrm{im}M^{\mathsf T}\subseteq\tilde V$** | 维数比较 |
| **6** | $\alpha_0=M^{\mathsf T}e_1$（$M$ 的第一行）$\in\mathrm{im}M^{\mathsf T}\subseteq\tilde V=V$ | ✓ |

### 7.5.19 ⭐⭐⭐⭐⭐ **判据（最终形式，两侧均已证）**

$$\boxed{\ \textbf{YES at}\ q=d_{CA}+1\iff \alpha_0:=L_0N\ \in\ V:=\big\langle\operatorname{row}(AN-NA')\big\rangle_{A'}\ }$$

| 侧 | 状态 |
|---|---|
| **充分**（$\alpha_0\in V\Rightarrow$ YES）| ✅ **已证**（A6/§7.5.3：构造 $A_0{=}I$ + pole placement）|
| **必要**（$\alpha_0\notin V\Rightarrow$ NO）| ✅ **已证**（A20，本节）|

**配合单调性（A7）**：
$$\alpha_0\notin V\ \Longrightarrow\ \textbf{NO for all}\ q\le d_{CA}+1\ \checkmark$$

### 7.5.20 **q1 的最终定位（第 41 处更正：不得再称"q1 为假"）**

$$\textbf{已证}：\text{可行性}\ (\exists R)\iff\alpha_0\in V\ \Longrightarrow\ \textbf{可行性判定}\in\mathrm{P}$$
$$\textbf{已证}：\text{任何解满足}\ \operatorname{rank}\mathcal LN\le\mathrm{obs};\qquad |\!R\!|_{\min}\le\mathrm{obs}+1-r\ (\alpha_0\in V)$$

$$\boxed{\ \textbf{q1}\ \text{（最小 }|\!R\!|\ \text{的 NP-hard 断言）}\ ——\ \textbf{既未证明，也未证伪}\ }$$

$$\text{理由}：\text{本文只证"存在性"}\in\mathrm{P};\ \text{而"给定存在性，最小化仍可能难"}$$
$$(\text{类比：给定存在性，最小顶点覆盖仍 NP-hard})\ \Longrightarrow\ \textbf{不能断言 q1 为假}\ ✗$$

$$\textbf{已排除}：\text{硬度}\ \textbf{不可能}\ \text{来自"是否存在解"}\ ✓$$

$$\textbf{开放}：q\le\mathrm{obs}\ \text{时}\ "\exists|\!R\!|=q"\ \text{的判定复杂度}\ ⚠️$$

$$\text{剩余（非判据部分）}：\text{对}\ q>d_{CA}+1\ \text{的扩展}\ ;\quad \text{最小}\ |\!R\!|\ \text{的精确算法}$$

---

## 8. q1 的现状定位

> 🔴 **本节表格已过时 —— 请以 §7.5.5 为准**（本轮已证充分性、必要性 23/23 支持）。
> 下面保留作历史记录。

| 说法 | 状态（**历史，已被 §7.5.5 取代**） |
|---|---|
| "q1 是 NP-hard" | ~~❌ 未证（但可能为真）~~ ⟹ **现在看很可能为假** |
| "q1 不是 NP-hard" | ~~❌ 不能断言~~ ⟹ **充分性已证；若必要性得证则成立** |
| "q1 在 $\{d_{CA}=1\}\cap\{2p+q_0\ge n\}$ 内不是 NP-hard" | ✅ **仍然成立**（BPP，除非 NP ⊆ BPP） |
| "硬度若存在，只能在 $d_{CA}\ge q_0$（情形 II）或 $2p+q_0<n$（支 B）" | ✅ 仍然成立 |

**为什么硬度最可能在情形 II**：$d_{CA}$、$2p+q_0$、$n$ 都**多项式时间可算**，故归约方
可以**自由地把目标实例都造成** $d_{CA}\ge q_0$：

> **若情形 II 的判定是 NP-hard ⟹ q1 就是 NP-hard。**

而情形 II **恰好就是最初被指出的"$q_0$ 阶谱不可行、需要扩维"的情形**（P2 的主题）——两者是同一件事。

**情形 II 的判定是**：$\exists\Theta:(\text{A})\wedge(\text{S})\wedge\operatorname{rank}H<q_0$ ——
一个**量词自由的实代数存在性问题**（ETR 型）。ETR 本身 NP-hard，故此处**不能排除** NP-hard。

> ⚠️ **第 18 处更正**：此处曾写"实测**可以为 YES**（6/6 实例），故这**不是**平凡的'恒 NO'"——
> **已撤回** ✗。那 6/6 的依据是优化器输出的 $\min\approx 1\text{e-}28$（浮点近零 ✗）。
> **本轮的精确判定**（校准过的通用构造器）给出：**(A)∧T5a 在情形 II 平行中恒不可解** ✗
> ⟹ **证据一致指向"情形 II 恒 NO"**（猜想 **c6**，见 §3）——若成立则 **分支 A 无硬度** ✓

**支 B**（$2p+q_0<n$）：

> 🔴 **第 2 轮更正（2026，见 [history/30](history/30_B2_proof_skeleton.md)、[history/32](history/32_branchB_witness_found.md)）**
>
> **原文"解集是有限个孤立点 ⟹ 不像硬度源"不成立** ✗，两处错：
>
> **(a) "有限"只对 $k=1$ 成立**。用 sympy Gröbner 精确算出（全部为支 B 实例）：
>
> | 支 B 实例 | $m$ | 非零扰动命中 | Groebner 次数 | $\dim\Omega^\star_J$ |
> |---|---|---|---|---|
> | $q_0{=}2,k{=}1,s{=}4$ | 3 | 0/1930 | $[1]$ | **0（单点）** |
> | $q_0{=}3,k{=}2,s{=}4$ | 4 | 218/1967 | $[1,2]$ | **$>0$** |
> | $q_0{=}4,k{=}3,s{=}5$ | 6 | n/a | $[2,3,4]$ | **$>0$** |
>
> $$\Longrightarrow\ k\ge2\ \text{时}\ \Omega^\star_J\ \text{是\textbf{零测、正维数}集（无限集）}\ ✗$$
>
> **(b) "支 B 无 (A)∧(S) 解"是错的** ✗ —— 已找到**可复现的见证**
> （`scripts/core/mainline_witness2.py`，数据存 `witness_branchB.json`）：
> $$n{=}6,p{=}1,q_0{=}3,k{=}2\ (2p{+}q_0{=}5<6)\ \text{满足}\ (A)\wedge(S)\ \Longrightarrow\ \nu_{\min}=q_0\ ✓$$
> 四条判据**独立核验**通过（支B / (A) 4块 / $\Lambda H=F$ / (S) 子式gcd）✓
>
> $$\boxed{\ \textbf{支 B 是真正的硬度候选}（此前"已排除"不成立）\ }$$
>
> **正确的表述**：支 B 的判定 = $\exists\Theta: (A)\wedge(S)$，是 **ETR 型实代数存在性问题**；
> $\Omega^\star_J$ **零测**（采样必失败 ✓）但**可非空**（$k=1$ 有限、$k\ge2$ 正维数）⚠️


---

## 9. 下一步（优先级排序）

| 优先级 | 任务 | 为什么 |
|---|---|---|
| 🔴 **1** | **攻支 B 的复杂度**（**新**）：大样本量化"$(A)\wedge(S)$ 非空"的频率与结构；若高频且有模式 ⟹ 尝试归约 | ✅ 已确证支 B **可非空**（[history/32](history/32_branchB_witness_found.md) 有见证）⟹ 它是**真正的硬度候选** |
| 🔴 **1'** | **攻情形 II 的复杂度**：或给多项式算法（证伪方向），或做归约（证明方向） | 仍是 q1 硬度的候选；c6′ 若成立则分支 A 无硬度 |
| 🟠 2 | **B2 的引理 A/B**：$\operatorname{rank}J=m$（9/9）与"高次 ∈ 线性理想"（6/6）的**严格证明** | $k=1$ 的组装已 Lean 化（`MyProof/Theorems/B2.lean` ✓）；代数内容待证 |
| 🟡 3 | **图卡限定**（§3.6）| 结论仅在 $\operatorname{rank}(RN_CK)=k$ 内成立 |
| 🟡 4 | **验证 $q_0$ 的下界**：需**证明** P1 Theorem 2 | $q_0$ 是全项目核心；暴力/随机法已证明**原理上无效** |
| ⚪ 5 | $(\star''')$ / (C1) / (C2) | 连续多轮无实质推进，需要新数学洞察而非更多实验 |

**明确的禁区**（已证实无效）：
- ❌ 用随机采样找稀有实例（连续 5 轮超时）
- ❌ 用暴力枚举轨道行验证下界（不完备）
- ❌ 用优化器"没找到"当"不存在"（已吃过两次亏）

---

## 10. 文件导航

```
FINAL.md                    ← 本文件（唯一权威结论）
README.md                   ← 入口与导航

problems/                   ← 命题文档（每个命题一个 md，统一框架）
    q1.md  q2.md  q3.md  q4.md  q_now.md

proof/                      ← 证明细节（支撑 §4）
    00_证明索引.md
    A_分支A的完整证明.md
    B_地基检查与交付结论.md
    C_情形II的结构.md
    D_支B的精确解数.md
    E_审查与撤回清单.md

scripts/core/               ← 产生 §4.5 数据的脚本（10 个）
    exact_count_thm7.py        公共库（rk/toF/p1/condA/orb/build_norm_T）
    verify_pencil_v2.py        铅笔既约形式校验
    reliable_S_test.py         可靠 (S) 判据 + 分情形实验 + 地基检查
    exact_count_14_elim.py     支 B 精确消元求解数
    ...（见 scripts/core/README.md）

docs/                       ← 稳定参考资料
    01_概念总结.md  02_文献摘录.md  03_检索来源.md  04_形式化验证.md

data/                       ← PDF 文本提取
pdf/papers/                 ← 三篇原始论文（P1/P2/P3）
pdf/reference/              ← 参考书/综述（Trentelman 教材、矩阵铅笔两篇）
history/                    ← 历史归档（旧 proof 01–12/15/16、旧 txt、旧脚本）
    README.md               ← 归档说明与 2026-10-20 整理记录
```

---

## 11. 一句话交付

> **本项目证明了 12 条结构性定理（T1–T9、D1、D2、q3），给出了精确阈值与 (S) 的三情形分解，
> 定位了 q1 硬度的最可能藏身处（情形 II = "需要扩维"的情形），并把支 B 的解数算到 $(1,4)$；
> 但 q1 本身、情形 II 的复杂度、支 B 的一般界、以及 $q_0$ 的下界，都仍未解决。
> 全部结论附两条限定（P1 图卡；$q_0$ 单一来源），并有 10 处自我更正记录在案。**

### 7.5.21 🔴🔴 **2026-10-19：$\rho\ge\mathrm{obs}$ 被反例推翻；本文件中依赖它的结论作废**

**反例**（外部给出，我已独立验证；详见 `OPEN_PROBLEM.md` 顶部）：

$$n=7,\ p=q=2,\quad d=3,\quad \rho=1,\quad \mathrm{obs}=3$$
$$A=\begin{pmatrix}0&1&0&0&0&0&0\\0&0&1&0&0&0&0\\0&0&0&0&0&0&0\\1&0&0&0&0&0&0\\0&1&0&0&0&0&0\\0&0&0&1&0&0&0\\0&0&0&0&1&0&0\end{pmatrix},\quad
C=\begin{pmatrix}0&0&0&0&0&1&0\\0&0&0&0&0&0&1\end{pmatrix},\quad
\mathcal L=\begin{pmatrix}1&0&0&0&-1&0&0\\0&0&0&1&0&0&0\end{pmatrix}$$
$$M=\begin{pmatrix}1&0&0\\0&0&0\end{pmatrix},\quad F=\begin{pmatrix}0&0&0\\1&0&0\end{pmatrix},\quad
\Lambda=\begin{pmatrix}0&0\\1&0\end{pmatrix}\ ;\quad (5a),(5b)\ \text{均成立}\ ✓$$
$$\ker M\not\subseteq\ker R_0\quad(R_0e_2=e_5\ne0)\qquad\Longrightarrow\quad \rho<\mathrm{obs}\ \checkmark$$

**作废的结论**：

| 结论 | 状态 |
|---|---|
| A23（$\rho=1\Rightarrow\mathrm{obs}\le1$）| ❌ **推翻**（其证明假定 $[M\|F]$ 各行共线；实际某行 $\alpha=0$ 而 $\gamma\ne0$）|
| $\|R\|_{\min}=\mathrm{obs}+1-r$ | ❌ **推翻**（反例给出 $q=2<\mathrm{obs}+1=4$）|
| "q1 为假" | ❌ **撤回** —— q1 重新开放 |

**A23 的正确版本**（$q=1$ 时才成立）：

$$q=1\ \wedge\ (5a)\wedge(5b)\ \Longrightarrow\ M=0$$
*证明*：$q=1$ 时 $\Lambda\in\mathbb{R}^{1\times1}$ 是标量 $c$，(5a) 给 $F=cM$；若 $M\ne0$ 取 $x$ 使 $Mx\ne0$，则 $(\lambda M-F)x=(\lambda-c)Mx$ 在 $\lambda=c$ 处为零，(5b) 败。□
$$\Longrightarrow\ \textbf{非平凡解必有}\ q\ge2\ \ (\text{即}\ |R|_{\min}\ge2-r)$$

---

## 12. 🆕 2026-10-20 增补（本轮改动，全部有文档与脚本可复现）

| 项 | 结论 | 文档 / 脚本 |
|---|---|---|
| **P6b 被推翻** | $\mathcal A\mathcal A'\subseteq\mathcal A\Rightarrow(5b)$ 必败 **是假的**（$n{=}5,q{=}3,\rho{=}2$ 反例；三套实现复核）| [I](proof/I_P6b_反例_2026-10-20.md)、`c140` |
| $\mathcal A\mathcal A'\not\subseteq\mathcal A$ **不再是必要条件** | 搜索空间比本文档原先假设的更大 | 同上 |
| **计数必要条件** | $\dim V_{\mathcal A}\ge n-2(d-\rho)$ ⟹ $q=\rho+1$ 需 $n\ge2d-2\rho$ | [K](proof/K_维数计数_2026-10-20.md) |
| **$\rho_{\min}$ 公式重验** | $\min_r\dim\Phi^\infty(\operatorname{span}\{\alpha_0,r\})$：$d{=}2,3,4$ 共 103 例 **0 反例**（$c136$ 的 0/560 确认为实现 bug）| [P](proof/P_rho_min公式重验_2026-10-20.md)、`c154` |
| 独立复核 | P1 必要性 / A19 / P4b：**618 个真实解 0 违规** | [G](proof/G_独立复核_2026-10-20.md)、`audit_independent.py` |
| 分层结论 | $q_{\min}=2$（P7）/ $3$（≈6%）/ $4=\mathrm{obs}+1$（326/326）| [O](proof/O_qmin分层_2026-10-20.md) |
| $d=2$ 的严格定理 | $\rho_{\min}\in\{1,2\}$，$\rho=1\iff$ P7（由 P7 + P1 推出）| [Q](proof/Q_d2_定理_2026-10-20.md) |

$$\textbf{方向记录}\ :\ \text{（1）证 } \rho_{\min}\ \text{公式的 lift 半边}\ ;\quad \text{（2）NP-hard 归约}\ \longrightarrow\ \text{见 } \texttt{OPEN\_PROBLEM.md}\ \S12$$

**仍然成立的**（独立于上述）：判据 $\exists R\iff\alpha_0\in V$（两侧）、可行性 $\in\mathrm{P}$、A19（$\rho\le\mathrm{obs}$）、$\rho=0$ 的刻画。