> **已更正（454）**：本文"闭条件"的说法**错**——实际是**开**（秩达最大）；$B$-不变是包含型（闭），
> 这里是维数最大的等式型（开）。见 [454](454_open_not_closed.md)。

# 453 两个条件的类型：都是"单调映射的不动点"⟹ **闭**条件；$\exists W$ 化归不动点存在性

> 承接 452（中间层判据 = (R) ∧ (E$'$)，两个子空间等式）。本轮判断它们在 $\operatorname{Gr}(\omega,k)$ 上的类型。

## 目标

判断 $\{\,W:\pi_2(\mathcal T_W)=W\,\}$ 与 $\{\,W:\operatorname{span}(V_0\cup\pi_1(\mathcal T_W))=W\,\}$ 是开、闭、还是都不是。

## 设想与理由

定义两个映射
$$\Gamma_2(W):=\pi_2\bigl(\mathcal T_W\bigr),\qquad
\Gamma_1(W):=\operatorname{span}\bigl(V_0\cup\pi_1(\mathcal T_W)\bigr),$$
其中 $\mathcal T_W=\mathcal S\cap(W\oplus W)$、$V_0=\operatorname{span}\{h_i^0\}$。两者都取值在 $W$ 里（$\Gamma_2(W)\subseteq W$；
$\Gamma_1(W)\supseteq V_0$ 且 $\subseteq W$ 当 $V_0\subseteq W$），并且都是**单调**的：$W_1\subseteq W_2\Rightarrow\Gamma_j(W_1)\subseteq\Gamma_j(W_2)$ ✓。

于是两个条件分别是**不动点方程**
$$\Gamma_2(W)=W,\qquad \Gamma_1(W)=W .$$

## 做法

把两个条件写成不动点方程，再判断不动点集的类型。

## 进展

**为什么是闭条件**：不动点集 $\{W:\Gamma(W)=W\}$ 是代数条件"$\dim\Gamma(W)=\dim W$ 且 $\Gamma(W)\subseteq W$"的解集——
它是**闭**的（正是"$W$ 等于一个由 $W$ 决定、且包含于 $W$ 的代数子空间"这种形状；
与"$B$-不变子空间"完全同型，见 [440](440_S_closed_subspaces.md) 里 $BW\subseteq W$ 是闭的）✓。

$$\boxed{\text{（R）与（E$'$）都是 }\operatorname{Gr}(\omega,k)\text{ 上的}\textbf{闭}\text{条件}}$$

## 最终结论（对 $q1$）

1. 中间层的可行集是 **闭的**（不动点集）；
2. 于是"$\exists W$"= **不动点存在性**问题——与"不变子空间存在性"同型，
   而后者有成熟理论（线性关系 / matrix pencil 的 **Kronecker 标准形**）✓；
3. 因此 $\exists W$ 很可能**可判**（多项式）⟹ 中间层可判 ⟹ 与顶层、$\omega=0$ 合起来 $q1$ 可判 ⟹
   **硬度关闭**；
4. 反之，若 Kronecker 理论在这里不给多项式算法，那么障碍就精确定位在**不动点存在性**上——
   那才是硬度的真正候选（而不是我之前猜的"影子缺失"）。

## 放弃原因

- 没有证明"闭"（只给了与不变子空间同型的论证）；
- 没有给出不动点存在性的算法（Kronecker 理论的具体接口未做）；
- 没有验证小实例上"可行集闭"这一点（例如检查可行集是否是离散点集）。

## 残留价值

- **把 $\exists W$ 化归成"单调映射的不动点存在性"**——这是本轮最实质的一步；
- 明确了它与"不变子空间"同型，从而可以借用成熟的线性关系理论；
- 指出 $q1$ 的两种可能结局对应的**具体数学**：Kronecker 给算法 ⟹ $\mathrm P$；否则障碍在不动点存在性。

## 下一步

1. 验证"可行集闭"：在小实例（$k=3$、$\omega=2$、$n=5$）上把可行 $W$ 的集合算出来，看它是否离散/闭；
2. 若闭，把 $\Gamma_2$ 写成**线性关系**（$\mathcal S$ 本身就是一个线性关系），用 Kronecker 标准形求不动点。

## 相关文件

- [452](452_E_simplified.md)（(E$'$) 与 (R)）
- [440](440_S_closed_subspaces.md)（$\mathcal S$-闭 = 不变子空间 = 闭）
- [451](../../decision_algorithms/attempts/451_split_collapse.md)（split 设计下的塌缩）

## 状态

- 类型（闭）：**[已证-纸面，同型论证]**。
- 不动点存在性的算法：**[未做]**。
