# 专家的 $(*)$ 判据落地：Bézout 系数矩阵的秩等式（C4 的第三个证明）

## 目标

落实专家 2026-11-03 §6 的建议：**把谱条件写成"系数矩阵的秩等式"**，从而把"gcd 跌落"自动纳入，
不再靠"典型 gcd + 猜例外点"。

## 设想与理由

设 $m_1,\dots,m_N$ 为 $P_{\mathcal Z}(\theta,\lambda)$ 的极大子式，$D=\max_i\deg_\lambda m_i$。定义
$$\Phi_\theta:\bigoplus_i\mathbb C[\lambda]_{\le D-1}\to\mathbb C[\lambda]_{\le 2D-1},\qquad (u_i)\mapsto\sum_i u_i m_i,$$
系数矩阵 $M(\theta)\in\mathbb C[\theta]^{2D\times ND}$（列 $=\lambda^k m_i$，$k<D$），$e_0$ 为常数 1 的系数向量。则
$$(5b)\ \text{在 }\theta\text{ 处}\iff \operatorname{rank}M(\theta)=\operatorname{rank}[M(\theta)\mid e_0]
\iff e_0\in\operatorname{col}M(\theta).$$
**关键**：$\deg u_i\le D-1$ 已足够（专家给的论证：先取非零的 $m_j$，用其余子式的常系数组合 $g$ 使 $\gcd(m_j,g)=1$，
再用二元 Bézout 展开）。

**证书（本模块的做法）**：取 $M(\theta)$ 在 $\mathbb Q(\theta)$ 上的左零空间基 $y_1,\dots,y_k$（清分母成多项式），
令 $C_j=y_j^{\mathsf T}e_0\in\mathbb Q[\theta]$。由多项式恒等式 $y_j^{\mathsf T}M\equiv0$：
$C_j(\theta_0)\ne0\implies e_0\notin\operatorname{col}M(\theta_0)$。故
$$(C_1,\dots,C_k)=(1)\ \Longrightarrow\ \text{无任何 }\theta\ \text{可行（记作 certified_infeasible）}.$$
这自动处理"子式在特殊 $\theta$ 处降次/消失"的情形。

## 做法

[bezout_rank_test.py](../../../../tools/verification/bezout_rank_test.py)：
逐图卡建 $M(\theta)$、求左零空间、清分母、得 $C_j$、算 Gröbner；另加**守卫**：抽样核验
$\operatorname{rank}[V|Z]$ 在图卡上恒定（否则需按秩做析取，未实现，报 `unknown`）。

## 进展

**C4 反例（$q_0=3$，两图卡，$D=2$，$M$ 为 $4\times8$，左零维数 2）**：

| 图卡 | $C_1$ | $C_2$ | 理想 | 结论 |
|---|---|---|---|---|
| $(0)$ | $3(96\theta^2-224\theta+133)$ | $-2(4\theta-5)(10\theta-11)$ | $(1)$ | **certified_infeasible** |
| $(1)$ | $3(133\theta^2-224\theta+96)$ | $-2(5\theta-4)(11\theta-10)$ | $(1)$ | **certified_infeasible** |

两个二次式都无实根且与另一因子无公共零点 ⟹ 每个 $\theta$ 上都有某个 $C_j\ne0$ ⟹ $e_0\notin\operatorname{col}M$ ⟹ $(5b)$ 处处失败。
这是 C4 的**第三个**独立证明（前两个：射影满射、符号 gcd + 例外点），且是专家推荐的那一个。

**发现的一个真实复杂度问题**：对 seed 3003 的网格见证（$\theta=0$），$\operatorname{rank}[V|Z]$ 从 4 **掉到** 3
（$V\cap\mathcal Z\ne0$），此时"极大子式"的尺寸也应当从 4 变成 3——本模块固定用 $\dim V+d$ 的尺寸，
故在该点给出错误的 `certified_infeasible`。已加秩恒定守卫；对 C4（秩恒为 3）不受影响。
这正是专家所说"必须对 $j$ 与**专门的次数**做有限析取"的那一点。

## 最终结论

1. **$(*)$ 判据已实现**，并在 C4 上给出**第三个独立证书**（理想为 $(1)$，纯代数、无需例外点猜测）；
2. **可靠性条件**：要求 $\operatorname{rank}[V|Z]$ 在图卡上恒定；不恒定时需按秩析取（未实现，工具报 `unknown`）；
3. 该判据同时把"跌落"问题**消解**了——它不需要知道 gcd 的典型次数，只看 $e_0$ 是否落在列空间；
4. 也印证了专家的判断：**决策对象是专门的 Bézout 恒等式，而不是典型 gcd**。

## 放弃原因

不适用（判据落地）。**未做**：按秩析取（处理 $\operatorname{rank}[V|Z]$ 不恒定的图卡）；
真实的可行性方向（$I\ne(1)$ 时如何解出 $\theta$ 并给见证）。

## 残留价值

* 专家推荐判据的**可运行实现**与一个真证书（C4 的第三证）；
* 明确的适用条件与一个**新发现的复杂度来源**（秩跌落需析取）；
* 与既有三个工具（Toeplitz / gcd / 零空间铅笔）的关系已理清：本判据是"存在性"层面的精确形式。

## 相关文件

- [tools/verification/bezout_rank_test.py](../../../../tools/verification/bezout_rank_test.py)
- [workspace/for_expert/07_programme_report_and_open_problems-answer.md](../../../for_expert/archive/07_programme_report_and_open_problems-answer.md)（专家 §6）
- [workspace/q1_false/feasibility_geometry/attempts/41_symbolic_chart_gcd.md](41_symbolic_chart_gcd.md)（第二证）
- [workspace/q1_false/feasibility_geometry/attempts/26_c4_proof.md](26_c4_proof.md)（第一证）
