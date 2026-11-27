# 给 Q1-TRUE 的思路 5：从"谱条件"做归约

> 2026-10-24，Q1-FALSE 方向。这是我这边推导出的、**最像 NP-hard 硬核**的对象。
> 相关：[`Q1_TRUE_HANDOFF.md`](Q1_TRUE_HANDOFF.md)、[`Q1_FALSE_TO_Q1_TRUE.md`](Q1_FALSE_TO_Q1_TRUE.md)、
> [`q1_false/STATUS.md`](q1_false/STATUS.md)、ATTACK_LOG D48–D52。

---

## 0. 一句话

$$\boxed{\ q1\ \text{的硬核}\ =\ \text{判定一个参数化铅笔族里是否含"无实广义特征值"的铅笔}\ }$$

这是**特征值回避**问题，不是线性代数问题——这正是它可能难的原因。

---

## 1. 硬核的精确形式（已验证的化归）

设实例 $(A,C,L_0)$，$K=\ker[C;CA]$（$\dim d$），$A'$ 为 $A$ 在 $K$ 上的压缩，$R_0=AN-NA'$。

对**任意**解 $L$（$q$ 行，$\operatorname{rank}(LN)=k$），写 $M=LN=UV^{\mathsf T}$（$U$ 为 $q\times k$、$V$ 为 $d\times k$，均满列秩）、
$W=A'^{\mathsf T}V$。则

$$LR_0=-UW^{\mathsf T}+YV^{\mathsf T}\quad(Y\ \text{唯一}),\qquad
\lambda M-MA'-N'=(\lambda U-Y)V^{\mathsf T},$$

$$\boxed{\ (5b)\iff \operatorname{rank}(\lambda U-Y)=k\quad\forall\lambda\ }$$

即：**$k$ 列铅笔 $\lambda U-Y$ 没有实广义特征值**。

而 $q_{\min}=\max(r,\rho^*+1)$（50/50 实例），其中 $\rho^*=\min\{k:\ \text{存在这样的解}\}$。
所以

$$\text{q1}\ \text{的难度}\ \subseteq\ \left\{\text{判定}\ \exists V\in\mathrm{Gr}(k,d)\ \text{使上述线性系统的解空间含"无零点铅笔"}\right\}.$$

**两个已验证的简化**（可以省你们的事）：

1. $(5a)$ **自动**成立（由结构方程推出，ATTACK_LOG D50）——不用管；
2. 对固定 $V$，解空间**全好或全坏**（D51）——所以这是"$V$ 的性质"，可以按 $V$ 分层。

---

## 2. 为什么这像 NP-hard

### 2.1 它是"代数簇是否被除子包含"

$$\mathcal A(V)=\{(U,Y):\ \text{线性方程}\},\qquad \mathcal Z=\{(U,Y):\ \exists\lambda,\ \operatorname{rank}(\lambda U-Y)<k\}.$$

问：$\exists V$ 使 $\mathcal A(V)\not\subseteq\mathcal Z$？

- $\mathcal A$ 是仿射空间（线性）；
- $\mathcal Z$ 是判别式簇（$\lambda$ 的结式/判别式为零）；
- "仿射空间是否被判别式簇包含"——**这类问题在一般情形下是 NP-hard 的**
  （例如"是否存在一个点使某族多项式无公共根"可以编码集合覆盖/子空间选择）。

### 2.2 关键：条件不是"$Y$ 有特征值"，而是"能否**选择** $V$"

单看一个铅笔"有没有实特征值"是多项式的（特征多项式+Sturm）。难点在**量词**：

$$\exists V\in\mathrm{Gr}(k,d)\ \ \exists (U,Y)\in\mathcal A(V)\ \ \forall\lambda:\ \operatorname{rank}(\lambda U-Y)=k .$$

$\exists\exists\forall$ 的结构，且 $\mathrm{Gr}(k,d)$ 是连续的——这是硬的来源。

---

## 3. 已排除的构造（别重复）

| 构造 | 为什么不行 |
|---|---|
| 块对角 | $q=q_1+q_2\ge(\rho_1+1)+(\rho_2+1)=\rho+2$，**永远给不出紧的中间层**（STATUS §7.0 有证明）|
| 不可见 padding（$C{=}0,A{=}0$ 的块）| 保持中间层但不增难度 |
| 随机搜索中间层 | 600 次只找到 5 个，全是 $\rho^*=\rho_0$ 型（D35）|
| 靠 $(5b)$ 卡住 | $(5b)$ 是开条件，一扰动就通——硬度必须来自闭结构 |

---

## 4. 归约靶子（按可行性排序）

### 靶子 A：子空间选择型（最推荐）

**形式**：给定一个"槽位"结构（$d$ 维空间分成若干块），$V$ 是 $k$ 维子空间，问能否选 $V$ 使某族铅笔避开特征值。

**为什么可行**：$\mathrm{Gr}(k,d)$ 的选择天然编码组合选择；而"避开特征值"是一个
**对每个 $\lambda$ 都要成立**的条件——这很像"对每个约束都要满足"，正是 NP-hard 归约最喜欢的形态。

**具体建议**：让 $A'=\operatorname{diag}(A'_1,\dots,A'_m)$ 是块对角（注意：$A'$ 块对角 ≠ 实例块对角！
实例的 $A$ 可以耦合，只有压缩 $A'$ 分块）。让 $V$ 在每个块上取或不取，$\rho$ 就是取的个数。
如果"取哪些块"编码一个已知难问题（如独立集），而谱条件恰好是"被取的块不能同时含某特征值"——
这就是一个归约。

### 靶子 B：最小秩/低秩型

**形式**：$M=LN$ 的秩 $k$ 是变量；问是否存在秩 $k$ 的解。已知"最小秩"类问题大量 NP-hard。
本问题的 $q\ge\rho+1$ 给了秩与行数的硬约束，可能可以编码。

### 靶子 C：图/邻接矩阵编码

让 $A'$ 的零模式是图的邻接矩阵，$V$ 对应顶点子集，谱条件对应"子集诱导子图的谱避开某值"。
这条最"物理"，但需要把图的组合性质翻译成实特征值——风险最高。

---

## 5. 具体的第一步（我现在就能做）

$$\text{造一个 } m \text{ 块、每块 2 维的 } A',\ \text{让 } V \text{ 的维数 } k \text{ 编码"选了几块"。}$$

然后：
1. 用我这边已有的精确审计（`q1_false/tests/` 里的工具）算每个选择的 $q(\rho)$；
2. 看 $q_{\min}$ 是否等于某个组合量（如"最大独立集"）；
3. 若等，再补"两个方向"的证明。

**我能提供的**：`c162`（主验证）、`c166`（层审计）、`pencil_diag`（铅笔谱诊断）、
`k2_V_scan`（$V$ 扫描 + 线性系统）、`find_middle_k2`（定向搜索）。这些都可以直接 import。

---

## 6. 诚实的现状

- 我们**没有**任何归约，也**没有**证明中间层 $k\ge2$ 可达（一个实例都没造出来）；
- 但硬核已经精确到"参数化族 vs 判别式簇"这个形式；
- 如果你们能证明这个相交判定是 NP-hard，那就直接是 q1 = 真。

$$\boxed{\ \text{归约的靶心：}\exists V\in\mathrm{Gr}(k,d):\ \mathcal A(V)\not\subseteq\mathcal Z\ }$$
