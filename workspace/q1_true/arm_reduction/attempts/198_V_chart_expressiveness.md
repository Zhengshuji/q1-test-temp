# $V$-chart 路线的分析：约束是二次/incidence 型，不是仿射型

> 2026-11-09。197 指出 $H$ 的约束是行空间型；本文件分析绕法 2（把变量放到 $V$ 的 chart 上），
> 结论：$V$ 的自然约束（$A(V)\subseteq V$ 等）在 chart 坐标中是**二次**的，
> 仍然不是 ARM 所需的仿射方程。状态：**M2（结构性分析）**。

## 目标

判断能否把 ARM 的变量与仿射约束编码到 $V\in\operatorname{Gr}(c,K_0)$ 的 chart 矩阵 $X$ 上。

## 设想与理由

取标准 chart：$K_0=E\oplus F$（$\dim E=c$），$V=\operatorname{graph}(X)$，$X:F\to E$（或 $E\to F$，按约定）。
则 $V$ 的 chart 坐标就是 $X$ 的元素。ARM 的未知矩阵 $X$ 自然对应这个 chart 矩阵。

需要检查：观测器的条件在 $X$ 上是什么形状？

## 做法

### 1. 不变性条件

$A(V)\subseteq V$ 在 chart 中写成
$$A_{21}+A_{22}X=X(A_{11}+A_{12}X),$$
这是 $X$ 的**二次**矩阵方程（$XA_{12}X$ 项）。不是仿射。

### 2. 可容许性

固定 $V$，$H$ 的行在 $\operatorname{Ann}(V)$（$\omega$ 维）中；顶行固定。$H_A|_V=0$ 是对提升 $l_i$ 的线性条件。
- 若 $V$ 不变（$A(V)\subseteq V$），则对任意 $h\in\operatorname{Ann}(V)$ 与任意提升 $l$，$l\cdot Av=0$（因 $Av\in V$），
  可容许性**自动**；
- 若 $V$ 非不变，$l\cdot Av=0$ 给提升的线性条件，可能可解也可能不可解（188 的 $g_0$ 构造）。

### 3. 铅笔条件

在可容许的 $(H,H_A)$ 上，$\operatorname{rank}(\lambda H-H_A)=\omega$ 是开条件（191 的特征空间单射）。
对不变 $V$，$H$ 的行在 $\operatorname{Ann}(V)$ 中自由，一般可取到 $B_*\ne0$ 且特征空间单射 ⇒ 好；
若结构强制 $B_*=0$，则坏。

### 4. 结论

- 对**不变** $V$：可行性 ≈ “$A(V)\subseteq V$”（二次）+ 铅笔（一般好）；这是**二次**条件；
- 对**非不变** $V$：可容许性是提升的线性条件，但 $V$ 本身的约束仍是 $A(V)\not\subseteq V$ 的开条件 + 铅笔；
- 无论哪种，$X$ 上的自然条件都是**二次/开**型，**不是** ARM 的仿射方程 $\langle A_i,X\rangle=b_i$。

## 与 ARM 的差距

ARM 的约束是 $X$ 的**线性**方程；观测器的自然约束是：
- 行空间型（197，对 $H$）；
- 二次型（$A(V)\subseteq V$，对 $V$ 的 chart）；
- 开型（秩、铅笔）。

**没有**直接的“$X$ 的线性方程”来源。所以绕法 2 也不能直接编码 ARM 的仿射约束。

## 可能的下一步

1. **用固定数据实现线性泛函**：$L_0$ 的行与 $A$ 的乘积 $L_0A^k$ 可以在 $H$ 上取线性泛函；
   但这些泛函作用在 $H$ 上，而 $H$ 与 $V$ 的关系是核关系，不是线性坐标。
2. **用 incidence 的线性化**：把 $\langle A_i,X\rangle=b_i$ 写成“某个子空间包含某向量”的 incidence；
   这类条件在 Grassmannian 上通常是线性的（Plücker），可能可用。
3. **换源问题**：ETR 算术电路（二次）比 ARM（仿射）更接近观测器的二次结构。

## 进展

* $V$-chart 的约束形状分析完成：二次/开型，不是仿射；
* 绕法 2 不能直接编码 ARM；
* 指出 incidence 线性化与 ETR 两个可能方向。

## 最终结论

* 观测器的自然约束是行空间型（$H$）、二次型（$V$ 的 chart）、开型（秩/铅笔）；
* ARM 的仿射约束没有直接来源；
* 硬度归约更可能需要 incidence 线性化或换用二次型的源问题（ETR）。

## 放弃原因

* 未构造任何具体 incidence gadget；
* 未证明“不能编码 ARM”的不可行性；
* 未尝试 ETR 源。

## 残留价值

* 对 hardness 表达力的清晰限制；
* 指明 incidence 线性化 / ETR 两个方向。

## 相关文件

* [attempts/196](196_ARM3_reduction_plan.md)（计划）
* [attempts/197](197_ARM3_expressiveness_limit.md)（$H$ 的行空间限制）
* [attempts/171](../../../q1_false/c_stratification/attempts/171_Buv_rank_strata.md)（chart 二次项）

## 状态

* 分析：**[M2]**。
* incidence gadget / ETR：**[未做]**。
