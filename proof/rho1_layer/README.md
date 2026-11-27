# 命题：$\rho=d_0{+}1$ 层的二次型判据

> **对应 docs 条目**：C.1（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

## 陈述

在 $\rho=d_0{+}1$ 层（$d_0=\dim U_0=r-c_0$），记 $b=\beta(h)$（$h\in\mathcal J$ 的像），$\tau$ 遍历一个由 $S$ 的约束给出的**仿射空间**。则

$$(5b)\ \text{在该层可满足}\ \Longleftarrow\ \det\,[\,b;\ S_\tau b\,]\ \not\equiv\ 0\ \text{在 }\tau\text{-仿射空间上}.$$

即：把 $\tau$ 当变量，行列式是**一次函数**（不是二次型——早先的说法已更正）；"在仿射空间上是否恒零"是**线性代数**问题，可多项式判定。

## 状态

| 项 | 值 |
|---|---|
| 验证 | [精确验证 46/47]（$\mathbb F_5$、$n{=}5$，穷举全部 $\rho=2$ 子空间）|
| 误报 | **0**（判据说"可行"时确实可行；唯一漏报 1 例）|
| 等级 | **[精确验证 46/47]**；旧的"经可控性"路线**已否决**（Q5，见 [../controllability_equivalence/](../controllability_equivalence/theorem.md) §8）|

## 为什么重要

这是目前**唯一**能对"中间层"做多项式判定的工具。若能把 $\rho=d_0{+}2,\dots$ 层也化成同样形状（"某多项式在仿射空间上非恒零"），则层判定多项式 ⟹ $q1=$ 假。

## 相关

- 复现：`tools/layer_search/c192_reduced_search.py`（穷举对照）、`archive/attempts_2026-10/q1_false/07_quadratic_criterion.md`
- 上下文：[docs/04](../../docs/04_structure.md) §4.3

## 关于 verify.py

本 claim **没有**独立的 `verify.py`：判据的复核依赖 `tools/layer_search/c192_reduced_search.py`
（穷举全部 $\rho=2$ 子空间做真值）与 `c194_layer2.py`（$\rho=2$ 层的定量实验）。
若要把 46/47 的判定固化成一个自包含脚本，需要把 $\tau$-仿射空间上的二次型判据重写一遍——**待做**。

## 已补：完整陈述与（条件性）证明

见 [theorem.md](theorem.md)：

- 引理 2.1（$2\times2$ Krylov 判据）、引理 2.2（$\tau$ 的一次性）、引理 3.1（可容许集仿射）均为 [已证]；
- 定理 4.1 **已撤回**：它依赖的 Q5 已被否决（输入算子恒为零）；
- $(k,1)$ 的推广是同一模板（$k\times k$ Krylov 行列式，仍是一次函数）。

## 最新状态（2026-10-27 晚）

| 部分 | 等级 |
|---|---|
| 引理 9.2（每个 $2\times2$ 子式对 $\lambda$ 与 $\tau$ 的次数都 $\le2$；含 $H$ 行的子式对 $\tau$ 线性）| [已证] |
| 推论 9.3（参数 $2j$ 个、每个子式系数 $O(j^2)$）| [已证] |
| 引理 9.5（"存在公共根"的 $\tau$ 集是**闭集**）| [已证] |
| 推论 9.6（该层判定 = $\mathcal A\not\subseteq\pi_\tau(\mathfrak B)$，**可判定**）| [已证] |
| 充分判据（$\operatorname{Res}(p_{12},p_{13})\ne0$，$O(j^3)$）| [已证]，对应 46/47 的"0 误报" |
| 消去 $\lambda$ 得到 $\pi_\tau(\mathfrak B)$ 的显式方程、并判定包含关系 | **未做**（§9.6）|

> 一句话：**次数界已被证明（多项式规模），闭集性已被证明（判定可行），剩下的是"在仿射集上判定包含"这一步的实际算法。**

## 定理 9.10（2026-10-27 晚，$w\ne0$）

$$(5b)\ \text{失败在}\ \tau\iff\exists\lambda:\ \lambda u_i-r_i(\tau)\in\langle w\rangle\ (i=1,2)$$

这组方程对 $(\lambda,\tau)$ **联合仿射**，故坏集 $\mathrm{Bad}$ 是 $\tau$-空间的**仿射子空间**（投影保持仿射）。
于是：固定 $(\mathcal U,\mathcal H)$ 时，可行性 $=\mathcal A\not\subseteq\mathrm{Bad}$，是 $O((2j+d)^3)$ 的**线性代数**。

**边界**：$w=0$（$hA\in\mathcal J$）时第三行消失，方程对 $(\lambda,\tau)$ 变成**二次**，定理不成立——§9.6 的双线性障碍只在此时残留。

**剩余**：层判定还要对 $(\mathcal U,\mathcal H)$ 量词（Grassmannian）；$\tau$ 这一维已被解决。

## 本层完整状态（2026-10-27 晚）

| 情形 | 结论 | 等级 | 数值 |
|---|---|---|---|
| $w\ne0$ | 坏集是**仿射子空间** ⟹ 可行性 $=\mathcal A\not\subseteq\mathrm{Bad}$，线性代数 $O((2j+d)^3)$ | [已证] 定理 9.10 | `verify.py` 1605/1605 |
| $w=0$ | 该 $(\mathcal U,\mathcal H)$ **恒不可行**（首一二次方程必有根）| [已证] 定理 9.12 | 625/625 |
| 层 | 剩 Grassmannian 量词：$\exists(\mathcal U,\mathcal H)$ 满足 $(5a)$、$w\ne0$、$\mathcal A\not\subseteq\mathrm{Bad}$ | 开放 | — |

$$\boxed{\ \text{固定 }(\mathcal U,\mathcal H)\text{ 时 }(2,1)\text{ 层已完全可判}\ }$$

## 复核脚本状态

| 脚本 | 内容 | 结果 |
|---|---|---|
| `verify.py` | 定理 9.10 的**逐点**判据（$(5b)$ 失败 $\iff\exists\lambda$ 使 $\lambda u_i-r_i\in\langle w\rangle$）| **1605/1605**（1590 可行 / 15 不可行，0 失配）|
| `verify_dim.py` | 定理 10.1 的**维数版**（$\exists\tau\in\mathcal A\setminus\mathrm{Bad}\iff\dim\mathrm{Bad}<\dim\mathcal A$）| 维数计算可跑（40 例全部 $\dim\mathrm{Bad}<\dim\mathcal A$）；但**采样部分还没对上**——生成器给出的 $\mathcal U$ 大多不满足 $(5a)$（`solve_tau` 返回 None），所以没有可比较的 $\tau$。**待修**：先用 $(5a)$-闭包构造 $\mathcal U$，再采样 $\tau$。|

## 定理 11.1′：$(2,1)$ 层稀有的真正原因

$\beta(h)\in B$ 恒成立，故 $\beta(h)$ 在 $X/B$ 里为零——"闭包 $\le2$"是空话（**已自我更正**）。
真正起作用的必要性是：$\mathcal U=\langle w,v\rangle$、$v\notin B$，而 $(5a)\iff T(v)\in\langle v\rangle+B$，即

$$\boxed{\ \text{需要一个}\ \textbf{模 }B\ \text{的特征方向}\ v\ }$$

这是行列式条件（余维 $\ge1$），一般 $A$ 不成立 ⟹ 该层空。**数值**：随机 216 个实例里 0 个找到这样的 $v$。

找 $v$ 是**广义特征值问题**（$Tv-\lambda v\in B$），属钳笔 Kronecker 理论（`literature/` 里 Verdier 2012）。

~~猜想 11.4~~：**已被证伪**（[theorem.md](theorem.md) §12）：5 个构造实例里 $\dim\mathrm{Bad}=\dim\mathcal A$ 且 $(5b)$ 失败。模 $B$ 特征方向是**必要但不充分**。

## 一般 $(k,1)$（theorem.md §14，纯证明）

| 结论 | 等级 |
|---|---|
| $(5b)$ 失败 $\iff\exists\lambda,\ \exists W_0$（$\dim W_0\le k-1$、$w\in W_0$）使所有行落在 $W_0$ 里 | [已证] 引理 14.1 |
| 每个 $W_0$ 给 $(\tau,\lambda)$ 空间的**仿射**子空间 | [已证] 引理 14.2 |
| 坏集 = Grassmannian 上一族仿射集的并 | [已证] 定理 14.3 |
| **$k=2$ 时 $W_0=\langle w\rangle$ 唯一** ⟹ 坏集仿射（定理 9.10 的结构性原因）| [已证] 推论 14.4 |
| $k=3$ 时 $W_0=\langle w,x\rangle$，多一个射影参数 $[x]$ ⟹ 多一层量词 | [已证] 推论 14.5 |
| $(3,1)$ 层可行性的复杂度 | **开放**（缺：$\exists[x]$ 上一族二次条件的可判性）|

$$\boxed{\ (2,1)\ \text{的线性代数不是普遍现象，而是 }k=2\text{ 的巧合}\ }$$
