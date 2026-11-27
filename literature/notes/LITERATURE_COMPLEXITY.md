# 文献：NP-hardness 已经存在于相邻问题（2026-10-24 关键发现）

> 之前几轮我查"minimum order observer 复杂度"没结果，是因为关键词不对。
> 正确的关键词是 **sensor placement / functional observability**。

---

## 1. 两篇有硬度结果的文献

| 文献 | 结果 |
|---|---|
| **Dey, Balachandran, Chatterjee**, *Complexity of constrained sensor placement problems for optimal observability*, **Automatica 2021**（[arXiv:1711.08264](https://arxiv.org/abs/1711.08264)）| 对任意固定 $k>2$，**「放置最少传感器使结构可观测指数 $\le k$」是 NP-complete** |
| **Zhang, Fernando, Darouach**, *Functional Observability, Structural Functional Observability and Optimal Sensor Placement*, **IEEE TAC 2025**（[arXiv:2307.08923](https://arxiv.org/abs/2307.08923)）| **「最小传感器集使 $(A,C_S,F)$ 功能可观测 / 结构功能可观测」是 NP-hard**（P1/P2/P3），用 **set cover** 归约 |

Zhang–Fernando–Darouach 的 Proposition 5（原文）：

> *"By setting $F=I_n$, P1 collapses to the minimal observability problem ... NP-hard even when $C=I_n$. ... To prove the NP-hardness of P2, we reduce the **set cover** problem to an instance of P2."*

$$\boxed{\ \text{这是功能观测器领域}\textbf{第一批 NP-hardness 结果}\ \Longrightarrow\ \text{q1 = 真 不再显得不合理}\ }$$

---

## 2. 它们证明的是"传感器选择"，不是"最小阶"

| 问题 | 变量 | 目标 |
|---|---|---|
| P1/P2（文献）| 选 $C$ 的哪几行（传感器）| $\min\vert S\vert$ |
| **q1（本项目）** | 固定 $C$，选 $\mathcal L=[L_0;R]$ | $\min q=\dim\operatorname{row}\mathcal L$ |

两者**接近但不同**。所以不能直接引用；但它给了：

1. **一个可复制的归约模板**（set cover → 图 → 功能可观测性）；
2. **一个关键连接点**：Fernando 的 $q_0=\sum_j\eta_j$ 是**功能可观测性指标之和**——
   而 Dey 等人的 NP-hardness 正是关于**可观测性指数**的。

$$\boxed{\ \text{若能让每个"集合/gadget"贡献 }\eta_j=1\text{，则 }q_0=\text{覆盖数}\ \Longrightarrow\ \text{q1 = 真}\ }$$

---

## 3. 归约的可行骨架（下一步要做的）

**目标**：把 set cover 实例（基集 $[r]$、子集 $S_1..S_p$）编成 MIN-ROWS 实例，使

$$q_{\min}=1+\text{minimum cover size}.$$

**Zhang–Fernando–Darouach 的构造**（可直接借）：

- 状态 $x_1..x_r$（功能态）、$x_{r+1}..x_{r+p}$（集合节点）；
- 自环 + 边 $(x_j,x_{r+i})$ 当 $j\in S_i$；
- 功能集 $F=\mathrm{col}(e_1..e_r)$；
- **每个状态都配一个专用传感器**（dedicated sensor），只需决定用哪些。

他们证明：$x_i$（$i\le r$）被选中的传感器"输出可达" $\iff$ 覆盖。

**我们要换的是**：把"选传感器"换成"选 $\mathcal L$ 的行"，目标从 $|S|$ 换成 $q$。

**关键待验证**：在这个图上，$q_{\min}$ 是否等于 $1+$ 覆盖数？

- 若 $\eta_j$（每个功能态的功能可观测性指标）恰为 1，则 $q_0=$ 功能态个数 $=r$——
  与覆盖数无关，**这条不直接成立**；
- 需要让 $\eta_j$ 依赖"哪个集合被选中"——即把指标编码进图的结构。

$$\text{这是目前唯一值得投入的具体构造问题。}$$

---

## 4. 另一个已确认的硬度（可能更好用）

Dey 等人：**「最少传感器使结构可观测指数 $\le k$」NP-complete**。

若能把"结构可观测指数 $\le k$"在 MIN-ROWS 里写成"$q\le k$"，则归约完成。
注意 Fernando 的 $q_0=\sum\eta_j$ 本身就是**指标之和**——形态非常接近。

---

## 5. 诚实的状态

- 相邻问题（传感器选择）**已证 NP-hard**（2021/2025，两个独立来源）；
- 本问题（最小阶）**仍无文献结果**；
- 但从"指标之和"到"覆盖数"的桥还没有搭起来。

**这是 q1 = 真 目前唯一的、有文献支撑的进攻路线。**
