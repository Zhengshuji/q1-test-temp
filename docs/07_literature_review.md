# 研究进展综述：最小阶功能观测器（MIN-ROWS / $q1$ 的文献面）

> 2026-10-28 整理。本文件放在 `docs/` 是按用户要求；它是**文献综述**，
> 每条都指向 `literature/` 里的全文/摘要，**不含本项目自己的新结论**（那些在 `proof/` 与 `docs/02`）。
> 文献总表：[literature/REFERENCES.md](../literature/REFERENCES.md)；检索日志：[literature/SEARCH_LOG.md](../literature/SEARCH_LOG.md)。

---

## 0. 问题

给定 $(A,C,L_0)$，求最小 $q$ 使存在 $R$（$\mathcal L=[L_0;R]$，$q$ 行）满足

$$(5a)\ \operatorname{rank}[\mathcal L A;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda\mathcal L-\mathcal L A;CA;C]=\operatorname{rank}[\mathcal L;CA;C]\ \ \forall\lambda .$$

这正是**最小阶线性功能观测器**的存在性问题（[Fernando–Trinh–Jennings 2010](https://ieeexplore.ieee.org/document/4303853/) 的 Condition 1/2 与 $(5a)/(5b)$ 逐项相同）。
$q1$ 问：计算 $q_{\min}$ 的**复杂度**。（**截至 2026-10-28 仍开放**，见 §5。）

### 记号对照

| 本项目 | 文献（Fernando 2026）| 含义 |
|---|---|---|
| $q$ | $q$（order）| 观测器行数 |
| $c_0=r$ | $r$ | 待估功能数（$L_0$ 的独立行数）|
| $\mathcal J=\operatorname{row}[CA;C]$，$j=\dim\mathcal J$ | $p$ = 独立测量数；$n_0=\operatorname{rank}O_C$ | 可测/可观测部分 |
| $X=\mathbb C^n/\mathcal J$，$d=n-j$ | $d=n-p-q$（每个阶对应的 nullspace 维数）| 商/零空间维数 |
| $\rho=\dim\pi(\mathcal V)$，$c=\dim(\mathcal V\cap\mathcal J)$ | —（他们用 $q$ 与 augmentation）| 本项目的分解 |
| $\mathcal A$（$\tau$ 的仿射可行集）| condition (A) 的解族 | 代数条件 |
| $\mathrm{Bad}$（$\lambda$ 的坏集）| condition (S) 的失效集 | 谱条件 |

---

## 1. 时间线

| 年 | 工作 | 贡献 |
|---|---|---|
| 1994 | **Darouach** 等 | 低阶功能观测器的经典存在条件（$q=r$ 的情形）|
| 2006–2009 | **Fernando–Trinh** 系列（含 *On the existence and design of functional observers for linear systems*）| 把存在性化为秩条件；给出构造 |
| **2010** | **Fernando–Trinh–Jennings**, IEEE TAC 55(5) | **与 $(5a)/(5b)$ 逐项相同**的 Condition 1/2；枚举子集的构造算法 |
| 2014 | **Pequito–Kar–Aguiar** | **结构型**最小输入/传感器选择 —— NP-hard |
| 2024 | **Fernando**（arXiv:2411.xxxx 系列）、**Montanari** 等 | 新的构造；结构功能可观测 + 最优传感器配置 |
| **2026-09** | **Fernando**, arXiv:2609.33615 | 介于 Darouach 与 Luenberger 之间的最小阶框架 |
| **2026-09-29** | **Fernando**, arXiv:2609.37992 | **阶谱完整刻画**（下节详述）|
| **2026-09** | **Löfberg**, arXiv:2609.16886 | 相邻判定问题 **SOF1 NP-hard** |

---

## 2. 最小阶问题目前的"最强结果"（Fernando 2026）

### 2.1 阶谱（arXiv:2609.37992, Thm 7/9）

$$r\ \le\ q_0=\sum_{j=1}^{r}\eta_j\ \le\ \nu_{\min}\ \le\ n_0-p\ \le\ n-p,$$

其中 $\eta_j$ 是**功能可观测指标**；$q_0$ 是"代数上允许的最小阶"（Darouach 阶是 $q_0=r$ 的特例；$n_0-p$ 是 Luenberger 端点）。
阶谱 $\Sigma_{FO}(L)=\{q_k=q_0+k\}$，$\nu_{\min}=q_0+\min\{k:\mathcal Z^{AS}_{d_k}\neq\varnothing\}$。

### 2.2 两个条件的矩阵形式（Thm 4、Thm 6）

- **代数条件（A）**：秩检验（$\operatorname{rank}[Z\ AZ\ RZ]=d$，$R$ 取自 $\ker(CAZ)$）；
- **谱条件（S）**：
$$\operatorname{rank}\big[(\lambda I-A)VZ\big]=\operatorname{rank}[VZ],\qquad \lambda\in\Omega_S ;$$
等价地 $$g_{I,\Theta}(\lambda):=\gcd_\lambda\{\Delta_j(\lambda)\}\neq0,$$ 其中 $\Delta_j$ 是 $P_{I,\Theta}(\lambda)=(\lambda I-A)VZ_I(\Theta)$ 的极大子式。

> 这正是本项目 [docs/02](02_theorems_proven.md) B.1 的 $\gcd$ 判据（**独立发现，已被覆盖**）。

### 2.3 完整性的形式

> **Thm 6/9**：阶 $q$ 存在功能观测器 $\iff$ **存在某个 matrix chart** $Z_I(\Theta)$（$I$ 是 $d$ 个行指标，$\Theta\in\mathbb R^{(m_L-d)\times d}$ 自由）
> 使 (14a)(14b) 成立。$\Sigma_{FO}$ 由所有这样的 $q$ 组成。

$\Theta$ 的自由度：每个 chart 有 $d(m_L-d)$ 个实参数；chart 个数 $\binom{m_L}{d}$。

---

## 3. 五条研究线

### A. 设计/构造线（工程主流）

Darouach → Fernando–Trinh → Fernando 2010/2024/2026。
给**条件**与**构造算法**；**从不谈复杂度类**。

### B. 结构型线（图论/网络）

Pequito–Kar–Aguiar 2014、Olshevsky 2013、Zhang–Fernando（最优传感器配置）、Montanari（结构功能可观测）。
结论多为 **NP-hard**，但数据是 **0/1 结构模式**，与本文的**数值**问题模型不同。

### C. 复杂度线（判定问题）

Blondel–Tsitsiklis（综述；区间约束 NP-hard，无约束当时开放）→ Toker–Özbay（BMI/同时镇定）→ Fu–Luo（固定阶矩阵不等式）
→ **Löfberg 2026（SOF1 无约束、数值数据、**NP-hard**）**。
**没有任何一条**给出"最小阶功能观测器"的复杂度结论。

### D. 几何线（子空间语言）

Wonham–Morse（$(A,B)$-不变、可控性子空间）、Warren–Eckberg 1975（可控性子空间维数由不变量决定）、
Willems 1981（almost invariant）、Jaffe–Karcanias 1981（almost $(A,Z)$-不变的**铅笔刻画**）、
Emre–Hautus 1980（**多项式刻画** + supremal 的构造；**不涉及最小维数**）。

### E. 铅笔/Kronecker 线（判据语言）

Verdier 2012（标准形）、**Dodig 2008**（行/列补全下 Kronecker 不变量的可达集 = **有限条不等式**）。
→ 支撑"$(5b)$ 是 Kronecker 型条件"的看法（$Q_{\mathcal V}(\lambda)=\pi(\mathcal L(\lambda I-A))$）。

---

## 4. 与本项目的关系

| 本项目结论 | 文献状态 |
|---|---|
| $\gcd$ 判据（$(5b)\iff$ 极大子式 $\gcd$ 为常数）| **已被覆盖**（Fernando 2026 Thm 6）|
| 阶谱观察 $\{q_0,q_0+1,\dots\}$ | **已被覆盖且更强**（Thm 7/9，含 $n_0-p$ 端点）|
| 中间层/中间阶存在性 | **已被覆盖**（2026 两篇）|
| $\rho$ 一侧的多项式性 $P\in\mathbf P$ | **未被覆盖**（Emre–Hautus 只做 supremal）|
| §21/§22 的"容器唯一 $\iff\dim\beta(\mathcal H)=\rho-1$"与维数比较判据 | **未被覆盖**（文献无此形式）|
| $(5b)$ 的 Kronecker 型解释 | 与 Jaffe–Karcanias/Dodig 同族，但未见同款陈述 |
| **复杂度**（$q1$）| **无人做过**（见 §5）|

---

## 5. 复杂度问题的现状（2026-10-28）

$$\boxed{\ q1\ \text{仍开放}\ }$$

依据：

1. 两篇 2026 论文里 **"complexity" 出现 0 次**，无任何多项式时间/硬度声明；
2. 其判定条件是"**某个 chart + 连续参数 $\Theta$** 使 (14a)(14b) 成立"——**半代数可行性**，非有限检验：
   - chart 数 $\binom{m_L}{d}$ 是指数级；
   - 每个 chart 里 $\Theta$ 连续自由；
3. 他们自称 Thm 9 是 **"completeness statement"**（完备性），不是可计算性；
4. 相邻问题的硬度（Löfberg 2026）**不蕴含**本问题的硬度（条件不同：Hurwitz vs 常数秩）。

### 缺的那一步（两种坐标，同一困难）

| 他们 | 我们 |
|---|---|
| $\exists\Theta$（连续）使 $\gcd_\lambda\{\Delta_j\}\ne0$，某个 chart | $\exists\tau$（仿射）使 $\gcd=1$，即"某极大子式在 $\mathcal A$ 上不恒零"（Bézout 化）|

$$q1\ \text{等价于}\ \text{"这类 }\exists\text{-代数条件能否化成有限（多项式）检验"}$$

### 5.1 2026-10-30 复核：又一篇 Fernando 2026，但仍无复杂度结论

**arXiv:2609.33615**（submitted 27 Sep 2026）：*A Minimum-Order Functional Observer Beyond the Darouach and Luenberger Constructions*。
要点（逐字核对）：$q_0=\sum_j\eta_j$、**"minimum condition-(A) augmentations 的完整族"**、$\nu_{\min}=q_0$ 的**充要谱条件**；
条件 (A)/(S) 与本项目的 $(5a)/(5b)$ 逐项相同，**摘要里没有任何复杂度类声明**。

⟹ ① $q1$ 仍开放 ✓（第三次确认，2026-10-28 → 2026-10-30）；
⟹ ② 但它**直接对着本项目的开放量词** $\exists(\mathcal U,\mathcal H)$（"完整族"），**必须读**：
它对族上的 $(S)$ 给的是**判定算法**还是**存在性刻画**？若是前者，则层判定可判、$q1$ 可能为假。
检索记录：[../literature/SEARCH_LOG.md](../literature/SEARCH_LOG.md) §5。

**已读后的结论（2026-10-30，逐项对照见 [../literature/notes/FERNANDO_2026_2609_33615.md](../literature/notes/FERNANDO_2026_2609_33615.md)）**：
它的"完整族"是
$$\mathcal L=\binom{L}{X_J(\Theta)M_C+KC},\quad J\subseteq\{1..s\},\ |J|=k,\ \Theta\in\Omega^\star_{A,J},\ K\in\mathbb R^{k\times p},$$
即**同一种 chart + 连续参数 $\Theta$** 的参数化；$(S)$ 在族上的判定被留成"$\exists(J,\Theta)$"，**不是算法**；
全文 `complexity`/`algorithm`/`polynomial time`/`NP` 命中 **0**。它的例子（$n=8$、$r=2$、$q_0=4$、$\nu_{\min}=4$）
把 $(S)$ 化成参数的一个显式不等式 $b\ne0$ —— 与项目在 $d=4$ 上"可行 $\varphi$ 至多 2 个"是同一现象（**难度在族的维数**）。

### 5.2 第二篇 **[P2] arXiv:2609.37992** 与项目的总对照（2026-10-30）

[P2] 给出**逐阶**的完整刻画：$\Sigma_{FO}(L)=\{q\in[q_0,\,n_0-p]:\ \exists$ 图卡与 $\Theta$ 使 $(14a)(14b)$ 成立$\}$，
$\nu_{\min}=\min\Sigma_{FO}$（Thm 9 + Algorithm 1）；其中 Thm 5 的判据是
$$\exists Z\ (\operatorname{im}Z\triangleleft\text{某 Grassmannian 点}),\quad CZ=0,\ LZ=0,\ \operatorname{rank}[Z,AZR_Z]=d,\ \operatorname{rank}[( \lambda I-A)V\ |\ Z]=\operatorname{rank}[V\ |\ Z]\ \forall\lambda.$$
**这就是本项目的 $\exists(\mathcal U,\mathcal H)$**（换了一套坐标）。

$$\boxed{\ \text{“刻画 }q_{\min}\text{、逐阶充要、构造”已被 P1+P2 完成；\textbf{复杂度}没人做}\ }$$

逐项对照与"项目还剩什么"见 [../literature/notes/FERNANDO_2026_TWO_PAPERS_vs_PROJECT.md](../literature/notes/FERNANDO_2026_TWO_PAPERS_vs_PROJECT.md)。
复现：[c206](../proof/layer_program/c206_paper_example.py)（P1 例子全过）、[c207](../proof/layer_program/c207_q0_eta.py)、[c209](../proof/layer_program/c209_paper2_example.py)（P2 例子 $q_0=3,n_0=8$）。

---

## 6. 开放问题清单

| # | 问题 | 现状 |
|---|---|---|
| O1 | 最小阶功能观测器判定问题的**复杂度类** | 完全开放（$q1$）|
| O2 | "$\exists\Theta$ 使 $\gcd=1$"是否有**多项式**判定 | 开放（对应本项目的 T11）|
| O3 | 最小维数 $(A,B)$-不变子空间（$P$）的算法是否已有人给出 | 未见（Emre–Hautus 只做 supremal）|
| O4 | 数值型 vs 结构型的硬度边界 | Löfberg 2026 表明数值型也能 NP-hard |
| O5 | 中间阶的**构造**（不只存在性）| Fernando 2026 给出参数化，未给多项式构造 |

---

## 7. 一句话总结

$$\underbrace{\text{存在性刻画}}_{\substack{\text{2026 已完整}\\[1pt]\text{(Fernando 2026)}}}\quad\Longrightarrow\quad
\underbrace{\text{判定/构造的复杂度}}_{\substack{\text{仍完全开放}\\[1pt]\text{(q1)}}}$$

文献把"什么时候存在"讲清楚了，把"能否多项式地决定/构造"留空了。

---

## 8. 相邻的 NP-hardness 结果（2025，必须引用）

**Zhang et al., IEEE TAC 2025**，"Functional Observability, Structural Functional Observability, and Optimal
Sensor Placement"：证明**最优传感器选择**（达到功能可观测性/结构功能可观测性所需的最少传感器数）是 **NP-hard**，
并给出超模函数与贪心近似。

**与我们的问题不同**：

| 本项目的 q1 | Zhang 2025 |
|---|---|
| 给定 $(A,C,L)$，选**增广** $\mathcal L$（连续矩阵）| 给定系统结构与候选传感器，选**子集**（组合）|
| 最小化**观测器维数** | 最小化**传感器数** |
| 代数 + 谱条件 | 功能可观测性（结构/数值）|

**不能**直接迁移：需要保持 yes/no 的多项式归约；目前没有。
**这条结果对我们是"相邻"而非"覆盖"**——专家（QA11）也持同样判断。
详见 [archive/expert_correspondence/QA11_2026-10-30.md](../archive/expert_correspondence/QA11_2026-10-30.md)。

---

## 9. 2026 的复杂度结果（专家 2026-11-01 提供，**必须引用**）

| 文献 | 结果 | 与我们 q1 的关系 |
|---|---|---|
| **Liu, arXiv:2610.00390**（2026-09-30）| **静态输出反馈稳定化**的 $\exists\mathbb R$-completeness（含可控可观测、双输入、有理数据）；并给出"有效增益维数"，超过该维数时问题多项式可解 | **我们目标类的直接先例**（$\exists\mathbb R$-complete 不是 NP-hardness 本身）；归约的模版；"有效维数"是值得对照的概念 |
| **Löfberg, arXiv:2609.16886**（2026-09-15）| 静态输出反馈稳定化 **NP-hard**（Betweenness 的多项式归约，单输入多输出）| 中间里程碑；编码离散选择的技术参考 |

**关键差异（为什么不能直接迁移）**：

| 静态输出反馈 | 功能观测器 DEC(q) |
|---|---|
| 找增益 $K$ | 找可容许子空间/图卡参数 |
| 要求 Hurwitz 稳定（根在左半平面）| 要求**谱秩保持**（极大子式无公根）|
| 多项式**不等式**（半代数）| 秩 + 铅笔条件（**也含非零条件**，见专家 §8.1）|

**已读（2026-11-01/02，见 [literature/notes/](../literature/notes/)) 的要点**：

- **Liu Thm 1**：SOF 是 $\exists\mathbb R$-complete（含双输入最小整数系统）；**Thm 2**：有效增益维数
  $\kappa=mp-\dim\mathcal N_{\rm pole}$ 固定时，判定与有理综合都是多项式时间（$\mathcal N_{\rm pole}$ = 不改变特征多项式的增益方向）；
  **Thm 3**：单输入最小系统上强 NP-hard，且可行实例有 $\{-1,1\}$ 增益与统一扰动裕度。
  其 §4.1 的技术是 $\det\begin{pmatrix}s^q+a&b\\-1&s^q-a\end{pmatrix}=s^{2q}+b-a^2$，把方程残差 $h_j-\ell_j^2$ **编进系数**。
- **Löfberg Thm 1.1**：SIMO 的 SOF **NP-hard**（Betweenness，$D=6(m+n)$）；技术是通用三次式的 Routh 行列式
  $\Delta=Nuv-1$，把"$x_b$ 在 $x_a,x_c$ 之间"化成一个多项式不等式；再频率分离聚合成单个仿射多项式。

**对我们最有用的一条观察**：方阵情形（$q=t$）下 $(5b)\iff\det[U\mid P(\lambda)]\in\mathbb C^\times$，
即"**全部非首项系数为零 +常数项非零**"——这正是 Liu 的"残差进系数"形状（等式组 + 一个非零条件）。
**尚未验证**这个桥能否走通（见 [workspace/q1_true/attempts/](../workspace/q1_true/attempts/)）。

**专家建议的归约路线（2026-11-01 §2.4）**：
Stage A 抽出示例的算术编码 → Stage B 用观测器变量复现 → Stage C 证明双向等价。
优先 **Route A**（直接用观测器子空间变量编码 ETR 算术），把 SOF 论文当灵感而非模板。

## 2026-11-07 增补：与 REAL-AUG 形状匹配的两类已知结果

**1. 双线性矩阵不等式（BMI）的可行性是 NP-hard**
Toker & Özbay, *On the NP-hardness of solving bilinear matrix inequalities and simultaneous
stabilization with static output feedback*, American Control Conference 1995.
（同方向：Blondel & Tsitsiklis 的若干线性控制设计问题的 NP-hardness。）
本项目相关性：REAL-AUG 的 (A)+(B') 是**双线性等式组**（$H=UV$、$X_jU-X_{j-1}G=0$），
属 BMI 型可行性的一个特例 ⟹ 若能把一般 BMI 可行性编码进 REAL-AUG，则 $q1$ 的硬度**有来源**。

**2. 二次方程组（QES）的实可解性是 $\exists\mathbb R$-完全**
Blum–Shub–Smale 1998（$\exists\mathbb R$ 的提出）；Schaefer & Štefankovič；
Schaefer–Cardinal–Miltzow 的汇编 *The Existential Theory of the Reals as a Complexity Class: A Compendium*
(arXiv:2407.18006) 收录 QES 的 $\exists\mathbb R$-完全性。
本项目相关性：REAL-AUG 是**次数 $\le2$** 的实方程组 ⟹ 平凡地 $\in\exists\mathbb R$；
硬度需**归约**（把 QES 或 BMI 编码进 REAL-AUG）。

**3. 由此得到的形状定位**

| 问题 | 形状 | 已知复杂度 |
|---|---|---|
| 线性等式/不等式的实可解性 | 线性 | $\mathbf P$（LP）|
| **REAL-AUG** | 双线性等式（$H=UV$、$X_jU-X_jG=0$）| **未知**（$\in\exists\mathbb R$）|
| BMI 可行性 | 双线性矩阵不等式 | **NP-hard**（Toker–Özbay）|
| QES | 一般二次 | $\exists\mathbb R$-完全 |

⟹ REAL-AUG 落在"线性（易）"与"BMI（NP-hard）/QES（$\exists\mathbb R$-完全）"之间；
$q1$ 的答案取决于它更靠近哪一端。

---

## 10. 2026-11-09 读后更新：ARM(3)、SOF、output feedback

> 本轮读了 arXiv 全文（PDF/文本已入库 `literature/papers/`），要点如下。
> 四篇都**不解决** $q1$；它们提供的是硬度源与结构对照。

### 10.1 Majumdar 2026：ARM(3) 是 $\exists\mathbb R$-完全

**arXiv:2602.14037**，*Affine Rank Minimization is ER Complete*。

- 问题 ARM(k)：给定有理 $A_\ell\in\mathbb Q^{m\times n}$、$b_\ell$，问是否存在实 $X$ 使
  $\langle A_\ell,X\rangle=b_\ell$ 且 $\operatorname{rank}X\le k$；
- **ARM(k) ∈ ∃R**（常数大小因子见证 $X=UV$）；
- **ARM(k) 是 ∃R-完全的**，且 **ARM(3) 已完全**；
- 归约：ETR → 算术电路（gate-equality normal form）→ 每个门量放进 $X$ 的指定条目；
  加法/复制/取负用线性约束，乘法用**常数大小 rank-forcing gadget**；
- 关键机制：违反 $z=xy$ 会迫使某个 $4\times4$ 子矩阵满秩，与 $\operatorname{rank}X\le3$ 矛盾；
  可行时给出显式 rank-3 完成；
- **gauge block**：固定一个满秩 $3\times3$ 子块，消除 rank-3 分解的基变换歧义，使解码良定义；
- **composition lemma**：gadget 可嵌入而不产生非预期耦合，保持多项式规模/比特长。

**与本项目的关系**：这是最接近的代数源（仿射约束 + 单一全局秩约束）。
障碍仍是：观测器的 $H=LN$、$H_A=LAN$ 同源耦合，以及谱条件；ARM 的 $X$ 是自由的，
观测器的压缩对不是。

### 10.2 Liu 2026：SOF 稳定化是 $\exists\mathbb R$-完全

**arXiv:2610.00390**，*Computational complexity of static output feedback stabilization*。

- 有理 plant 的 SOF 稳定化是 **∃R-完全**（含可控可观测、双输入、整数数据）；
- **有效增益维数** $\kappa$：决定特征多项式所需的最小增益线性组合数；
  $\kappa$ 固定时，判定与有理增益构造都是**多项式时间**；
- 另有一族最小单输入整数 plant 上**强 NP-hard**，可行增益可取 $\{-1,1\}$，且有统一扰动裕度。

**与本项目的关系**：$\exists\mathbb R$-完全的直接先例；但它的条件是 **Hurwitz**（根在左半平面），
不是“所有 $\lambda$ 的铅笔满秩”。不过“固定有效维数 ⇒ 多项式”与本项目的“固定 $c$”思路可对照。

### 10.3 Ahmadi–Chaudhry–Narang–Tang 2026：output feedback stabilization 是 NP-hard

**arXiv:2609.20636**，*Complexity of Output Feedback Stabilization*。

- 除非 P=NP，输出反馈稳定化没有多项式（甚至伪多项式）算法；连续/离散都成立；
- 还给出“稳定但无法用标准表示多项式时间写出控制器”的族；
- 这是 **NP-hard**（不是 ∃R-完全），与 Liu 的 ∃R-完全结论是不同模型/不同陈述，不能混用。

### 10.4 Löfberg 2026：SOF 稳定化 NP-hard

**arXiv:2609.16886**，*Static output-feedback stabilization is NP-hard*。

- 从 Betweenness 多项式归约到单输入多输出 SOF；$D=6(m+n)$；
- 技术：通用三次式的 Routh 行列式 $\Delta=Nuv-1$ 编码“$x_b$ 在 $x_a,x_c$ 之间”；
  频率分离把多个条件聚成一个仿射多项式；
- 副产品：仿射参数化有理多项式族是否含 Hurwitz 成员是 NP-hard。

（注意：arXiv:2609.18844 是无关的 figure-reconstruction 论文；SOF 的编号是 **2609.16886**。）

### 10.5 Fernando 2026：刻画已解决，无复杂度声明

两篇（2609.33615、2609.37992）给出阶谱、逐阶充要、图卡/零空间表示、gcd 判据与构造；
**没有**讨论 $\exists\Theta$ 的判定复杂度。因此 $q1$ 仍是开放问题。

### 10.6 对项目的直接含义

1. **硬度源排序**：ARM(3) 第一，SOF 第二，一般算术电路第三；
2. **观测器侧的核心障碍**：把 ARM 的自由 $X$ 换成同源耦合对 $(LN,LAN)$，同时保持谱条件；
3. **可借鉴的技术**：rank-forcing gadget（违反性 ⇒ 满秩子式）、gauge block（解码良定义）、
   composition lemma（门组合）；
4. **可解性对照**：Liu 的“固定有效增益维数 ⇒ 多项式”与本项目“固定 $c$”是同一类现象，
   值得作为 Theorem A 的模板；
5. **判断不变**：$q1$ 仍开放，最可能“固定 $c$ 可解、整体困难”。

### 10.7 Barkai–Shames 2026：无约束 SOF 的 NP-hardness

**arXiv:2609.38728**，*On the NP-Hardness of Unconstrained Static Output Feedback Stabilization*。

- 从 **Subset Sum** 多项式归约到无约束 SOF 稳定化 ⇒ NP-hard；
- 一个输入、$N$ 个输出、$10N+3$ 状态；每个输出含带通标量原型（稳定增益在 1、2 附近），
  共享求和块强制 $\sum_i a_i k_i$ 落在窄区间；
- 频率分离（带通变换）+ Rouché 根计数，把解耦回路与耦合 plant 的稳定性严格连接；
- 构造给出**每个稳定增益的显式界**与 modulus margin，plant 数据多项式编码。

**与本项目的关系**：NP-hard（弱于 Liu 的 ∃R-complete）；但“增益有界 + 频率分离 + 近似离散选择”
对处理 spurious witness 与全 $\lambda$ 谱条件有技术参考价值。不能替代 ARM(3)/SOF 的完全性来源。

