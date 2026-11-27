> **已撤回（478）**：本文的"两实秩条件"**不充分**——$(E)$ 必须是完整的**铅笔秩条件**
> $\dim\pi_\lambda(\mathcal T_{W_X})=\omega\ \forall\lambda$（要查 $\gcd$），
> 不能只写成 $\operatorname{rank}Z_2=a$ 与 $\operatorname{rank}[\bar V_0;Z_1]=a$。见 [478](../../decision_algorithms/attempts/478_E_lambda_coupled.md)。

# 470 (R)(E) 在 $\ker D_I(X)$ 上的显式形式：两个**秩条件**，都在同一个秩层上

> 承接 469（同构定理）。本轮把两个子空间等式翻译成 $\ker D_I(X)$ 的矩阵条件。

## 目标

写出 (R)(E) 的显式形式，使它们成为**同一秩层上的两个秩条件**（这正是 468 的 A1 所需形态）。

## 做法

用 469 的正合列把两个子空间等式"搬到商里"：取 $\ker D_I(X)$ 的一组基并分成两个分量块，把条件写成这两块的秩等于 $a$；再在最小模型上核对。

## 进展

（见下文"结果：分层与判据的结构"与"最小模型核对"。）

## 设想与理由

由 469 的正合列，把 $\Pi:\mathcal S\to\bar{\mathcal S}$ 记为商映射，$K_U=\mathcal S\cap(U\oplus U)=\ker\Pi$。
则
$$\mathcal T_{W_X}=\Pi^{-1}\bigl(\ker D_I(X)\bigr),\qquad
\pi_1(\mathcal T_{W_X})=\pi_1(K_U)+\pi_1(\text{$\ker D_I$ 的升}),$$
而 $\pi_j(K_U)\subseteq U\subseteq W_X$ ✓。所以两个条件**只在商里看**：记
$$Z(X)=\text{$\ker D_I(X)$ 的一组基},\qquad Z_1(X),\ Z_2(X)\ \text{为其两分量块（在 }\bar V\text{ 坐标里）},$$
$$\bar V_0:=\bar\pi(\pi_1(L_0\text{ 的对}))\quad(\text{固定行的第一分量在商里的像}).$$

> **命题（显式判据）.** 在 $D_I(X)$ 常秩的层上，
> $$\textbf{(R)}\iff\operatorname{rank}\begin{bmatrix}\bar V_0\\ Z_1(X)\end{bmatrix}=a,
> \qquad
> \textbf{(E)}\iff\operatorname{rank}Z_2(X)=a,$$
> 其中 $a=\dim(W_X/U)=\omega-d$，秩都在 $\bar V$（$=\bar\pi(V)$）里算。

*理由.* $(E)$：$\pi_2(\mathcal T_{W_X})=W_X$ ⟺ 其商等于 $W_X/U$ ⟺ $\bar\pi_2(\ker D_I)=W_X/U$ ⟺ $\operatorname{rank}Z_2=a$ ✓。
$(R)$：$\operatorname{span}(V_0\cup\pi_1(\mathcal T_{W_X}))=W_X$ ⟺ 其商张成 $W_X/U$ ⟺ $\operatorname{rank}[\bar V_0;Z_1]=a$ ✓。

## 结果：分层与判据的结构

1. **同层两个秩条件**：$Z_1,Z_2$ 来自**同一组** $\ker D_I(X)$ 的基 ⟹ 两个条件都在**同一不可约层**上 ⟹
   正是 468 的 A1 所要求的形式 ✓；
2. **泛型层**（$\operatorname{rank}D_I=r_{\max}$，即 $\det$-型条件非零）是**开**的 ⟹ 泛型秩判据适用 ✓；
3. **特殊层**（$\operatorname{rank}D_I<r_{\max}$）是**闭**的 ⟹ 需 A2（半代数可行性）✓；
4. $Z(X)$ 在常秩层上是 $X$ 的**有理函数**矩阵 ✓ ⟹ 两个秩条件是有理函数的秩条件 ⟹ 可行集是构造性集 ✓（与 457 一致）。

## 最小模型核对（$k=2,\omega=1,U=0$）

$d_0=\dim\bar{\mathcal S}=2$；卡 1 上 $D_I(X)=\begin{pmatrix}-X&1\\-X&2\end{pmatrix}$：

| 层 | $\operatorname{rank}D_I$ | $\dim\ker$ | $Z$ | (E) $\operatorname{rank}Z_2=a=1$? | 判定 |
|---|---|---|---|---|---|
| 泛型（$X\ne0$） | 2 | 0 | 无 | ✗（秩 0） | 不可行 ✓ |
| 特殊（$X=0$） | 1 | 1 | $\ker=\operatorname{span}\{(1,0)\}$ ⟹ 对 $=(1,0\mid1,0)$ | ✓ | **可行** ✓ |

与 468/469 的手算一致 ✓。

## 最终结论

1. **(R)(E) 已写成 $\ker D_I(X)$ 上的两个秩条件**（同一层、同一组基）✓；
2. 于是"泛型层用 A1、特殊层用 A2"的分工有了**显式载体**；
3. 最小模型核对一致 ✓。

## 放弃原因

- 没有把 $\bar V_0$（固定行在商里的像）的具体计算写出（最小模型 $L_0$ 为零，故未检验该项）；
- 没有写出 $Z(X)$ 的**显式有理参数化**（只用了"常秩层上有理"这一般事实）；
- 没有做特殊层的 A2。

## 残留价值

- **显式判据**：两个秩条件都在 $\ker D_I$ 的基上，形态与 468 的 A1 完全匹配；
- 把 469 的同构定理变成**可操作的判定形式**；
- 最小模型的一致核对。

## 下一步

1. 写出 $Z(X)$ 的显式有理参数化（对 $\operatorname{rank}D_I=r$ 的层，选一个 $r$-子式做局部坐标）；
2. 对特殊层做 A2（实可行性）；
3. 若非零 $\bar V_0$，补上该项。

## 相关文件

- [469](469_D_I_general.md)（同构定理）
- [468](../../decision_algorithms/attempts/468_three_levels_and_minimal_example.md)（A1/A2 与最小模型）
- [452](452_E_simplified.md)（(R)(E) 原始形式）

## 状态

- 显式判据：**[已证-纸面]** + **[精确验证]**（最小模型）。
- $Z(X)$ 的显式参数化：**[未写]**。
- A2：**[未做]**。
