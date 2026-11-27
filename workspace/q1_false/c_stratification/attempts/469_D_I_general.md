# 469 一般 $D_I(X)$ 与同构定理：秩跳变就是 $\det D_I$ 的零点

> 承接 468（采纳专家框架）。本轮写出**一般的 $D_I(X)$**，证明同构，并在最小模型上验证。

## 目标

1. 写出从 $\mathcal S$、$U$、图空间约束出发的 $D_I(X)$；
2. 证明 $\mathcal T_{W_X}/(\mathcal S\cap(U\oplus U))\cong\ker D_I(X)$；
3. 在最小模型上核对，并指出秩跳变 = $\det D_I$ 的零点。

## 做法

从 $\mathcal S$、$U$ 与图空间约束出发写出 $C(X)$ 与 $D_I(X)=C(X)B_0$；用商映射 $\bar\pi$ 把"是否落在 $W_X\oplus W_X$"化成线性方程，再由正合列读出维数公式；最后在最小模型上核对。

## 进展

## 设想与理由

记号：$V=\mathbb Q^{1\times k}$、$U\subseteq V$（$\dim=d$）、$\bar V=V/U$、$b=k-d$、$a=\omega-d$；
$\bar\pi:V\to\bar V$ 为商映射，$\bar{\mathcal S}=(\bar\pi\oplus\bar\pi)(\mathcal S)$。

取 $\bar V$ 的有理基，把每个元素写成 $(\bar x^{(I)},\bar x^{(J)})$（pivot/补集坐标）。
图空间约束 $W_X/U=\operatorname{row}[I_a\ X]$ 等价于
$$\bar x^{(J)}=X\,\bar x^{(I)}\quad\Longleftrightarrow\quad[-X\ \ I_{b-a}]\begin{pmatrix}\bar x^{(I)}\\\bar x^{(J)}\end{pmatrix}=0 .$$
两个分量各一份，故

$$C(X)=\begin{pmatrix}-X&I_{b-a}&0&0\\0&0&-X&I_{b-a}\end{pmatrix},\qquad
D_I(X)=C(X)\,B_0,$$
其中 $B_0$ 是 $\bar{\mathcal S}$ 的一组有理基（按两个分量排成列）。

## 定理（同构与维数）

> 存在正合列
> $$0\longrightarrow \mathcal S\cap(U\oplus U)\longrightarrow \mathcal T_{W_X}\longrightarrow\ker D_I(X)\longrightarrow 0,$$
> 因此
> $$\dim\mathcal T_{W_X}=\dim\ker D_I(X)+\dim\bigl(\mathcal S\cap(U\oplus U)\bigr).$$

*理由.* 由构造，$\ker D_I(X)$ 恰是"商后满足图空间约束的可用对"；核正是"两个分量都落在 $U$ 里的可用对"
（它们在商里为零，但在 $W_X\supseteq U$ 里仍合法）✓。

**推论**：$\mathcal T_{W_X}$ 的维数跳变由 $\operatorname{rank}D_I(X)$ 控制；
而 $\operatorname{rank}D_I(X)$ 的跳变由它的极大子式的零点给出——
**秩分层就是 $\{\text{极大子式}=0\}$ 定义的局部闭层** ✓，与 468 的三层区分一致。

## 验证（最小模型 $k=2,\omega=1,U=0$）

$d=0$、$b=2$、$a=1$，卡 1 上 $X\in\mathbb A^1$，$B_0$ 取 $A$ 的图的两条基（$(e_1,Ae_1)$、$(e_2,Ae_2)$）：

$$D_I(X)=\begin{pmatrix}-X&1\\-X&2\end{pmatrix},\qquad \det D_I(X)=-X .$$

| $X$ | $\operatorname{rank}D_I$ | $\dim\ker D_I$ | $\mathcal T_{W_X}$ | 判定 |
|---|---|---|---|---|
| $0$ | 1 | **1** | 1 维 | **可行** ✓ |
| $1$ | 2 | **0** | $\{0\}$ | 不可行 |
| $2$ | 2 | **0** | $\{0\}$ | 不可行 |

**与 468 的手算完全一致** ✓；且**秩跳变恰在 $\det D_I=-X$ 的零点** ✓。

## 最终结论

1. **一般的 $D_I(X)$ 已写出**，同构定理已给出（含固定核部分 $\mathcal S\cap(U\oplus U)$）；
2. **秩跳变 = $\det D_I$ 的零点**，于是"特殊秩层"是**显式可写**的局部闭层 ✓；
3. 最小模型上验证一致（$\det D_I=-X$；$X=0$ 可行、$X\ne0$ 不可行）✓；
4. 于是 468 的三层区分有了**显式代数表达**：泛型层 = $\{\det D_I\ne0\}$（开），特殊层 = $\{\det D_I=0\}$（闭）。

## 放弃原因

- 没有证明同构在 $U\ne0$ 时"固定部分"确实就是 $\mathcal S\cap(U\oplus U)$（只给了理由，未逐式核）；
- 没有写出 (R)(E) 在 $\ker D_I(X)$ 上的**显式**形式（含固定部分的贡献）；
- 没有做特殊层的实可行性（A2）。

## 残留价值

- **显式的 $D_I(X)$ 与同构定理**——专家要求的第一步完成；
- **秩跳变 = 极大子式零点**这一表述，使分层成为可计算的代数对象；
- 最小模型上的完整核对（与手算一致）。

## 下一步

1. 写出 (R)(E) 在 $\ker D_I(X)$ 上的显式形式（含 $\mathcal S\cap(U\oplus U)$ 与 $V_0$ 的贡献）；
2. 对特殊层（$\det D_I=0$）做 A2 的实可行性；
3. 估端到端复杂度。

## 相关文件

- [468](../../decision_algorithms/attempts/468_three_levels_and_minimal_example.md)（三层区分与最小模型）
- [467](467_two_more_retractions.md)（撤回）
- [452](452_E_simplified.md)（(R)(E)）

## 状态

- $D_I(X)$ 与同构：**[已证-纸面，待逐式核 $U\ne0$ 情形]**。
- 最小模型验证：**[精确验证]**。
- (R)(E) 在 $\ker D_I$ 上的显式形式：**[未写]**。
- A2 实可行性：**[未做]**。
