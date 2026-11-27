# Fernando 2026（两篇）对本项目意味着什么

> 1. T. Fernando, *A Minimum-Order Functional Observer Beyond the Darouach and Luenberger Constructions*, arXiv:2609.33615v1（2026-09）
> 2. T. Fernando, *Complete Characterization of Minimum-Order Functional Observers from Darouach to Luenberger*, arXiv:2609.37992v1（2026-09-29）
> 全文在 `literature/papers/2609.33615.{pdf,txt}`、`2609.37992.{pdf,txt}`。

## 1. 它们给了什么（确切结论）

### 2609.37992（**与本项目重合度最高**）

| 结果 | 内容 |
|---|---|
| **阶谱端点** | $r\le q_0\le \nu_{\min}\le n_0-p\le n-p$，其中 $q_0=\sum_{j=1}^r\eta_j$（功能可观测指标），$n_0=\operatorname{rank}O_C$ |
| **Thm 5/9（完整性）** | 每个阶 $q$ 的存在性 ⟺ 存在一个 **matrix chart** $Z_I(\Theta)$ 与参数 $\Theta$ 使 (14a)(14b) 成立 |
| **Thm 4（谱条件的铅笔形式）** | condition (S) $\iff \operatorname{rank}[(\lambda I-A)VZ]=\operatorname{rank}[VZ]$，$\lambda\in\Omega_S$ |
| **gcd 判据** | (14b) $\iff g_{I,\Theta}(\lambda):=\gcd_\lambda\{\Delta_j(\lambda)\}\ne0$（$\Delta_j$ 为 $P_{I,\Theta}$ 的极大子式）|
| **Thm 9（阶谱完整刻画）** | $\Sigma_{FO}=\{q_k: \mathcal Z^{AS}_{d_k}\ne\varnothing\}$，$\nu_{\min}=q_0+\min\{k:\mathcal Z^{AS}_{d_k}\ne\varnothing\}$ |

### 2609.33615

给出"介于 Darouach 与 Luenberger 之间"的最小阶框架：功能可观测指标决定最小代数阶；刻画"达到该维数的全部 augmentation 族"；给出谱可行性充要条件；并含**中间阶**（两种经典观测器都不存在时仍可能存在）。

## 2. 与本项目的关系：**大量重合**

| 本项目 | 他们的对应物 |
|---|---|
| $(5b)\iff$ 全部 $k\times k$ 子式的 $\gcd$ 为常数（[docs/02](../../docs/02_theorems_proven.md) B.1）| $g_{I,\Theta}\ne0$ 判据（Thm 6）|
| 铅笔形式 $\operatorname{rank}Q_{\mathcal V}(\lambda)=\rho$ | Thm 4 的 $\operatorname{rank}[(\lambda I-A)VZ]=\operatorname{rank}[VZ]$ |
| 可达集的阶谱 $\{q_0,q_0+1,q_0+2,d,d+1\}$ | $\Sigma_{FO}=\{q_0+k\}$、端点 $n_0-p$ |
| $q=\rho+c$ 分解、层程序 | 阶 $q$ + augmentation 的 $k$ |
| $(2,1)$ 层（$\rho=2,c=1$）| $k=1$（中间阶）的 $q_0$ 以上一阶 |
| 我们的"中间层稀有"观察 | 他们：中间阶"may exist even when neither classical observer is available" |

## 3. 关键问题：**复杂度解决了吗？**

**没有。** 依据：

1. 两篇里 **"complexity" 出现 0 次**，**没有任何多项式时间声明**；
2. 判定条件是"**存在某个 chart $I$ 与某个连续参数 $\Theta\in\mathbb R^{(m_L-d)\times d}$** 使 (14a)(14b) 成立"——
   - chart 的个数是 $\binom{m_L}{d}$（组合数，指数级）✗；
   - 每个 chart 里 $\Theta$ 是**连续自由参数** ⟹ 这是一个**半代数可行性问题**，不是一个有限检验 ✗；
3. 他们自己把 Thm 9 称为 **"completeness statement"**（在每个阶上，所有 chart 都失败才证明不存在）——这是**完备性**，不是**可计算性** ✓；
4. Algorithm 1 的中间阶分支正是"Parameterize $Z=K_LW_I(\Theta)$ 并检验谱条件"，没有给出"如何判定 $\exists\Theta$"的算法 ✗。

$$\\boxed{\\ \\text{所以：}\\textbf{完整刻画已有（2026）}，}\\textbf{复杂度问题仍开放}\\ \\checkmark$$

## 4. 对本项目的影响（必须记下）

1. **新颖性收窄**：项目的 (a) gcd 判据、(b) 阶谱观察、(c) 中间层存在性，
   在 Fernando 2026 里都有更强的（已证）版本 ⟹ **不能声称这些是项目的新发现** ✗。
2. **项目仍可能有的独立贡献**：
   - 算术侧 $P\\in\\mathbf P$（最小维数 $(A,B)$-不变子空间）——与"阶谱"无关 ✓；
   - §21/§22 的"容器唯一 ⟺ $\\dim\\beta(\\mathcal H)=\\rho-1$"与 $\\dim\\mathrm{Bad}<\\dim\\mathcal A$ 判据 ✓（文献里没有这个形式）；
   - **复杂度**的正面或反面结论（若做出）。
3. **技术上有用的东西**：他们把 $Z$（nullspace 矩阵）作为参数，我们用 $(\\mathcal U,\\mathcal H,\\tau)$——
   两种参数化可以对照；他们的 chart 思路（用行指标子集把 $W$ 规范化）可能正是我们缺的"有限化"手段 ✓。

## 5. 下一步的调整（建议）

1. **先做一次"重合清单"**：把 2609.37992 的每个定理与我们 `docs/02` 的每条比对，标出"已被覆盖/仍独立"；
2. 然后决定主攻方向：
   - 若项目要保"复杂度"贡献 ⟹ 目标应是"**判定 $\\exists\\Theta$ 是否多项式**"，即把他们的半代数可行性化成有限检验（这正是我们 T11 的对应物 ✓）；
   - 若转向 ⟹ 回到算术侧 $P$ 与 S1 的结构定理（不重合的部分）。