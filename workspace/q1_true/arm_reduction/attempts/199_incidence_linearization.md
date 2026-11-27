# incidence 线性化实验：$A_{12}=0$ 给 Sylvester 型线性条件，但不是任意仿射

> 2026-11-09。198 指出 $V$ 的 chart 约束一般是二次的。本文件试一个特例：取 $A_{12}=0$，
> 则不变性方程退化为 $X$ 的**线性** Sylvester 方程。结论：能得到结构化的线性条件，
> 但仍不是 ARM 的任意仿射方程 $\langle A_i,X\rangle=b_i$。状态：**M2（分析 + 小实验）**。

## 目标

检验“incidence 线性化”能否把一条仿射约束编码到 $V$ 的 chart 矩阵 $X$ 上。

## 设想与理由

$V=\operatorname{graph}(X)$，$A$ 按 $K_0=E\oplus F$ 分块。不变性 $A(V)\subseteq V$ 等价于
$$A_{21}+A_{22}X=X(A_{11}+A_{12}X).$$
若 $A_{12}=0$，则
$$\boxed{A_{21}+A_{22}X-XA_{11}=0}$$
是 $X$ 的**线性**方程（Sylvester 型）。这是 $V$ 上少见的线性条件来源。

## 做法

### 1. Sylvester 的逐元形式

取 $A_{11}=\operatorname{diag}(\lambda_1,\dots,\lambda_c)$、$A_{22}=\operatorname{diag}(\mu_1,\dots,\mu_{k-c})$，
则逐元
$$(\mu_j-\lambda_i)X_{ij}=-(A_{21})_{ij}.$$
所以：
- 若 $\mu_j\ne\lambda_i$，$X_{ij}$ 被**唯一确定**；
- 若 $\mu_j=\lambda_i$，$(A_{21})_{ij}=0$ 是相容条件，$X_{ij}$ 自由。

### 2. 能得到什么

- **固定某些 entry**：$X_{ij}=b$（通过选 $A_{21}$ 与特征值差）；
- **线性关系**：若多个块/多个方程叠加，得到 $\sum_k d^{(k)}_{ij}X_{ij}=b_{ij}$ 型（逐元系数和）；
- 但系数矩阵受“特征值差”的结构限制：$d_{ij}=\mu_j-\lambda_i$ 是**差矩阵**，不是任意矩阵。

### 3. 不能直接得到什么

ARM 的一条约束是 $\sum_{ij}(A_1)_{ij}X_{ij}=b_1$，系数 $(A_1)_{ij}$ **任意**。
Sylvester 给出的是逐元（或差结构）条件，不能实现任意系数组合。要多条任意仿射方程，
需要更多自由度，当前构造没有。

### 4. 结论

- incidence 线性化在 $A_{12}=0$ 时**部分成功**：能得到 Sylvester 型线性条件；
- 但不是任意仿射条件；ARM 的 $\langle A_i,X\rangle=b_i$ 仍不能直接编码；
- 若要任意系数，需要额外的 gadget（例如用多个块/辅助变量消去差结构）。

## 进展

* 找到了一个线性条件的来源（$A_{12}=0$ 的 Sylvester）；
* 分析了它的逐元形式与结构限制；
* 明确了与 ARM 任意仿射约束的差距。

## 最终结论

* 观测器能实现**结构化**线性条件（Sylvester/差矩阵），不是任意仿射；
* ARM 归约仍需更强的 gadget；
* 这是 197/198 之后对表达力的进一步细化。

## 放弃原因

* 未构造多块 gadget 来实现任意系数；
* 未证明“任意仿射不可实现”；
* 未做数值/符号实验。

## 残留价值

* Sylvester 线性化这一具体来源；
* 对“能实现什么形状的线性条件”的清晰描述。

## 相关文件

* [attempts/197](197_ARM3_expressiveness_limit.md)（$H$ 行空间限制）
* [attempts/198](198_V_chart_expressiveness.md)（二次型）
* [attempts/196](196_ARM3_reduction_plan.md)（计划）

## 状态

* 分析：**[M2]**。
* 多块 gadget / 不可行性：**[未做]**。
