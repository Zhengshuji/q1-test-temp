# 398 层程序的统一形式（$\exists\Theta$ 的一个具体化）与"一次判定"的障碍

> 承接 397（层号不单调 ⟹ 不能截断层号）。本文件把 $c=1,2$ 的结构写成**统一的**存在公式，
> 把它与文献的 $\exists\Theta$ 对齐，并说明为什么"不再逐层枚举"的一次性判定在图表路线下做不到。

## 目标

1. 给出**统一**的可行性刻画（对所有 $c$），即 $\exists\Theta$ 的具体化；
2. 分析"一次判定整个不变子空间族"的复杂度障碍。

## 设想与理由

$c=1$ 的（论文）与 $c=2$ 的（393–394）结构完全平行：

| | $c=1$ | $c=2$ |
|---|---|---|
| 方向 | 不变**直线**（$M$-特征向量） | 不变 **2-平面** |
| 底 | 有限个 $\mathbb P(E_\mu)$ | $\mathcal I_2(M)$ 的分量（点 / $\Gr(2,E_\lambda)$ / $\mathbb P\times\mathbb P$）|
| $K$-split 的 $V$ | $D^{\perp_K}$（$t=0$ 时） | $D^{\perp_K}\oplus W$，$W\subseteq T_D$ |
| 纤维 | $\Gr(t-w_0,\ \rho-r-t)$ 的 $c=1$ 版 | $\Gr(t-w_0,\ T_D/W_0)$ |

所以对一般 $c$ 应当有同一个形状。写成定理：

## 做法：统一形式

**定理 1（统一刻画，$K$-split 版）.** 设 $\dim V=q$、$c=k-\rho$。则 $K$-split 的 $c$-层可行
$\iff$ 存在

$$D\in\mathcal I_c(M):=\{D\in\Gr(c,K):\ M(D)\subseteq D\},\qquad
W\subseteq T_D:=K^\perp\cap(A_{21}D)^\perp,\quad \dim W=t,$$

使

$$\text{(i)}\ W_0\subseteq W,\qquad
\text{(ii)}\ \rank\bigl(\lambda H-H_A\bigr)=\omega\ \ \forall\lambda\in\mathbb C,$$

其中 $V=D^{\perp_K}\oplus W$、$H=V^{\mathsf T}N$、$H_A=V^{\mathsf T}AN$、$\omega=\rho$。

*证明.* 393 命题 2 的 $c=2$ 论证逐字推广：$V\cap K=D^{\perp_K}$（由 $K$-split 与 $V\subseteq U_D^\perp$）；
$V\subseteq U_D^\perp\iff W\subseteq T_D$；预设行给 (i)；(5b) 给 (ii)。$\square$

**这是 $\exists\Theta$ 的具体化**：$\Theta=(\text{底图卡坐标},\ \text{纤维图卡坐标})$，
量词结构是
$$\exists c\ \exists D\ \exists W\ \forall\lambda\ \bigl[\text{rank}(\lambda H-H_A)=\omega\bigr],$$
与文献的"$\exists$ 图卡 $\times$ 半代数"完全同型。

**推论 2（可判定性）.** 每一层（固定 $c$）是**可判定**的：$\mathcal I_c(M)$ 有有限个分量
（由 $M$ 的 Jordan 型决定）、每分量上按 $r(D)=\rank(A_{21}|_D)$ 分层、每层的相对丛有限个仿射图卡，
每张卡上一次函数域 gcd 检验（满秩引理保证"正次数 ⟹ 整卡坏"）。故对固定 $c$ 与固定图卡数，
判定是有限的精确计算。

## 进展：为什么"一次判定"在图表路线下做不到

**一次判定**要求把 $\exists c\ \exists D\ \exists W$ 一次性处理，而不是逐层逐分量。

**(a) 枚举本身是多项式的。** $c\le k$ 共 $O(n)$ 个；$\mathcal I_c(M)$ 的分量由 $M$ 的 Jordan 型给出，
可多项式枚举（每个块内 $\Gr(c,K_\lambda)$、块间的 $\prod\mathbb P$、链段的选择）；每分量的图卡数也有限。

**(b) 每张图卡的变量数是 $O(cn+p^2)$，不是 $O(c^2)$。** 图卡维数
$$d_{\rm chart}=\underbrace{c(d_\lambda-c)}_{\text{底}}+\underbrace{(t-w_0)((n-k)-r-t)}_{\text{纤维}}.$$
纤维项受 $n-k\le2p$ 控制，是 $O(p^2)$；但**底项 $c(d_\lambda-c)$ 可以是 $O(cn)$**
（$c=2$ 而重根特征空间维数 $\Theta(n)$ 时就是 $\Theta(n)$）。函数域 gcd 的代价随变量数指数增长，
所以图表路线给的是

$$n^{O(cn+p^2)}\ \text{（**不是** } n^{O(c^2)}\text{）},$$

而且"$m$ 个变量的图卡"本身**不**直接给出任何复杂度界——先要有对变量数的显式算法。

**(b′) 枚举本身也不是一致多项式的。** $\mathcal I_c(M)$ 的分量数可以指数：$M$ 为 $k$ 个互异实特征值时
$|\mathcal I_c(M)|=\binom{k}{c}$，当 $c$ 是输入的一部分时取 $c=\lfloor k/2\rfloor$ 就是 $\Theta(2^k/\sqrt k)$。
所以"枚举是多项式的"只在**固定 $c$** 的意义下成立。

（这两条是专家 108 号 §13 的更正，原文的 $n^{O(c^2)}$ 结论**撤回**。）

**(c) 所以 $q1$ 的缺口正是"能否去掉图表"。** 需要一个**线性代数/结构**判据：
把"(ii) 对所有 $\lambda$ 满秩"换成对 $(D,W)$ 的有限个**多项式条件**，且这些条件能在
$\Gr(c,K)$ 上一次性处理（例如用不变量理论把 $\exists W$ 消掉）。

**(d) 与已有 FPT 的关系。** Paper I 已有"固定 $\ell=\rank(AN)$ 的 FPT"；本程序的指数参数是 $c$。
两者是**不同的参数**（$\ell$ 与 $c$ 互不决定），所以层程序既不蕴含也不被蕴含于 Paper I 的 FPT。
$q1$ 的困难区正是 $c$ 与 $\ell$ 同时增长。

## 最终结论

1. **统一刻画（定理 1）**成立：$K$-split 的 $c$-层可行 $\iff\exists D\in\mathcal I_c(M),\ \exists W\subseteq T_D$
   满足预设行与铅笔条件——这就是 $\exists\Theta$ 的具体化；
2. **每层可判**（推论 2）：有限分量 × 有限图卡 × 函数域 gcd；
3. **一次判定做不到**：图表变量数 $O(cn+p^2)$（且 $\mathcal I_c(M)$ 的分量可指数）⟹ 图表路线只是"固定 $c$ 可判"；$q1$ 的真正缺口是"去掉图表的线性代数判据"；
4. 与 Paper I 的 FPT（参数 $\ell$）互补：困难区是 $c$ 与 $\ell$ 同时增长。

## 放弃原因

- 没有构造"去掉图表"的判据（例如用不变量理论把 $\exists W$ 消成 $(D)$ 的条件）；
- 没有分析 $\mathcal I_c(M)$ 的分量数在 $c$ 上的增长（可能与 Jordan 型有关，需单独算）；
- 没有把定理 1 与 Paper II 的 $W$-表述对齐（Paper II 用的是压缩行对空间，不是 $K$-split 的 $D,W$）。

## 残留价值

- **统一的层刻画（定理 1）**与"每层可判"（推论 2），把 $c=1,2$ 的结果写成同一形状；
- **$q1$ 缺口的准确定位**：需要"一次处理 $\Gr(c,K)$ 上整个不变子空间族"的判据，图表路线给不出；
- 与 Paper I 的 FPT 的参数对照（$\ell$ vs $c$）。

## 相关文件

- [attempts/397](../../c_stratification/attempts/397_layer_nomonotone.md)（层不单调，故不能截断）
- [attempts/395](../../c_stratification/attempts/395_c2_to_q1.md)（到 $q1$ 的路线）
- [attempts/394](394_c2_total_charts.md)（$c=2$ 的图卡）
- [attempts/386](386_bit_complexity_proof.md)（$c=1$ 的 $n^{O(p^2)}$ 记账，同型）
- [docs/04_structure.md](../../../../docs/04_structure.md)（$q=\rho+c$ 与 $\rho$ 侧的多项式算法）
