# 型控制猜想（专家 55 §6 / §9 Step 5）

> 2026-11-08。把 133 的“型控制定理”按专家 55 号降级为**猜想**，并写清它成立需要什么。
> 状态：**[猜想]**（不是定理；$N(c)$ 界与 $k$-无关性均未证）。

## 目标

精确陈述型控制猜想，并列出把它变成定理所需的四件事。

## 设想与理由

* 133 的 $N(c)\le\sum_\tau N(t(\tau))$ 不成立：纤维是开 Grassmannian 不自动给总分量；
  $X_\tau$ 不自动是低层同一问题；$k$-无关性被 Kronecker 数据（维数/块重数）破坏。
* 正确的问题（专家 55 §9 Step 5）：
  > 固定 $c$，$(\iota,A_0)$ 的子空间 incidence 簇能否分成**受控个数**的不可约局部闭层，
  > 每层纤维是开 Grassmannian？
* 这是“结构”问题，不是“数值不变量”问题；Kronecker 型是环境 pair 的规范形，不自动控制子空间簇。

## 做法

### 猜想

> **型控制猜想**：固定 $c\ge1$。存在有限个局部闭层
> $$\mathcal E_c=\bigsqcup_{\alpha\in A}\mathcal E_\alpha,$$
> 使得：
> 1. 每个 $\mathcal E_\alpha$ 在 Kronecker 型 of $(\iota|_W,A|_W)$ 与环境嵌入数据（$W\subseteq D\subseteq K_0$、
>    $A_0$ 在 $K_0$ 上的延拓）上常值；
> 2. 每个 $\mathcal E_\alpha$ 到其“$W$-底”的投影的纤维是开 Grassmannian
>    $\operatorname{Gr}(c-\dim(W+A(W)),K_0/(W+A(W)))$ 的开子集；
> 3. $\mathcal E_\alpha$ 的不可约分量数由一个只依赖 $c$ 与 Kronecker 数据（含维数/重数）的函数控制。

### 变成定理所需的四件事（专家 55 §6.1）

1. **底层有限分层**：把可能的 $W$（按 Kronecker 型/环境数据）分成有限个局部闭层；
2. **纤维的代数性**：每层上 $W\mapsto \mathcal F_W$ 是代数的（开 Grassmannian 丛）；
3. **总空间分量行为**：每层总空间到基的投影的像/分量对应（需要投影的纤维维数常值或可算）；
4. **底层分量界**：底层（quiver Grassmannian/incidence）的不可约分量数有界。

### $k$-无关性的限定

* $A|_{K_0}$ 不是自同态，Jordan 型无定义；
* 即使换成 Kronecker 型 of $(\iota,A_0)$，其数据含 $\dim D$、$\dim K_0$、块重数，**可能随 $k$ 增长**；
* 故不能声称“分量数只依赖 $c$”；只能说“由 $c$ 与 Kronecker 数据控制”，而 Kronecker 数据本身随输入规模变化。

### 与 $q1$ 的关系

* 若猜想成立且分层/纤维可算，则固定 $c$ 的判定可归约为有限个开 Grassmannian 上的 generic gcd；
* 这仍**不**给多项式算法（分层数与 Kronecker 数据可能大），也**不**排除 hardness；
* 专家 55 §8：固定 $c$ 多项式算法“plausible but not proved”；暂不做 hardness 归约。

## 进展

* 猜想已精确陈述（三层条件 + $k$-限定）。
* 变为定理所需的四件事已列出。
* 明确不再声称 $N(c)$ 的统一界或 $k$-无关性。

## 最终结论

* 型控制是**猜想**，不是定理；它给的是结构目标，不是分量数公式。
* 正确的语言是 Kronecker 表示 + quiver Grassmannian incidence；正确的纤维是开 Grassmannian。
* 下一步（专家 55 §9）：先把 $c=2/c=3$ 用精确条件重写（136/137 已做），再形式化 Kronecker 表示（138），
  最后才尝试猜想的证明。

## 放弃原因

* 没有证明四件事中的任何一件（只给了框架）。
* 没有给出分层/分量数的显式界。
* 实点、复杂度未做。

## 残留价值

* 一个精确、可检验的猜想，替代 133 的“定理”。
* 明确了要证的四个具体命题，便于后续逐条攻。
* 与专家 55 的结论完全对齐。

## 相关文件

* [attempts/133](../../c_stratification/attempts/133_type_control_theorem.md)（旧“定理”；本文件降级）
* [attempts/134](../../c_stratification/attempts/134_55_corrections_exact_fibre.md)（55 裁决）
* [attempts/135](../../c_stratification/attempts/135_exact_fibre_theorem.md)（精确纤维）
* [attempts/138](138_kronecker_representation.md)（Kronecker 表述）

## 状态

* 猜想：**[猜想]**（未证）。
* 四件必需命题：**[未做]**。
* 与 $q1$：结构性归约，不改变复杂度结论。
