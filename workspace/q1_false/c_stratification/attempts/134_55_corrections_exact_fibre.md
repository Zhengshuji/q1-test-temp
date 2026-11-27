# 55 号裁决落地：精确纤维条件、Kronecker 型、$c=2/c=3$ 的精确条件

> 2026-11-08。专家 55 号答复的逐条落实。最重要的一条：
> **$133$ 的纤维条件 $A(V)\cap V=B$ 不充分**；正确的是 $V\cap A^{-1}V=W$，
> 等价于 $\operatorname{rank}(V\to K/V)=c-t$。另：$A|_W$ 不是自同态，**Jordan 型无定义**；
> 正确的型是 Kronecker 表示 $(\iota|_W,A|_W):W\rightrightarrows W+A(W)$，环境对象是
> $(\iota,A_0):D\rightrightarrows K_0$，$D=K_0\cap A^{-1}K_0$。
> 状态：**M2（按专家裁决重写；未证部分标猜想）**。

## 目标

1. 给出**精确纤维定理**（替代 133 的错误条件）；
2. 用 Kronecker 型替代 Jordan 型；
3. 修正 $c=2$ 与 $c=3$ 的精确条件（含 131 的假非空条件、132 的弱条件）；
4. 把 133 的“型控制定理”降级为**猜想**。

## 设想与理由

* $W=V\cap A^{-1}V=\ker(\overline A_V:V\to K/V)$。条件 $A(V)\cap V=B$ 只保证
  $\operatorname{im}(A|_V)\cap V=B$，**不**保证 $\ker\overline A_V=W$：若 $Av\in B=A(W)$，
  则 $A(v-w)=0$，只给 $v-w\in\ker A$，不能推出 $v=w$。
* 正确的条件是**极大秩开条件**：$\operatorname{rank}\overline A_V=c-t$。
* $A(W)\subseteq V$ 但不必 $\subseteq W$；$A|_W:W\to A(W)$ 不是自同态，Jordan 型不存在。
* 正确的对象：pair of maps $(\iota|_W,A|_W):W\rightrightarrows W+A(W)$，pencil
  $\lambda\iota|_W-A|_W$；环境 pair $(\iota,A_0):D\rightrightarrows K_0$，$A_0=A|_D$，
  pencil $\lambda\iota-A_0$。Kronecker 标准形（Berger–Trunk–Winkler 2016；Berger–Trenn 2012；
  Gantmacher Vol II Ch XII）。
* Kronecker 型分类**环境 pair**，不自动分类子空间簇；后者是 quiver Grassmannian
  （Caldero–Reineke 2008）的 incidence 问题。

## 做法

### 1. 精确纤维定理

设 $W\subseteq D=K_0\cap A^{-1}K_0$、$\dim W=t$、$U=W+A(W)$。则
$$\boxed{\mathcal F_W=\{V\in\operatorname{Gr}(c,K_0):\ U\subseteq V,\ 
\operatorname{rank}(V\to K/V)=c-t\}.}$$
这里 $V\to K/V$ 由 $A$ 诱导，$\ker=V\cap A^{-1}V$。故 $\mathcal F_W$ 是
$$\operatorname{Gr}(c-\dim U,\ K_0/U)$$
中的**开子集**（极大秩条件），非空即不可约。

*证明*：$\ker(\overline A_V)=V\cap A^{-1}V$；$W\subseteq\ker$，故 $\ker=W\iff$
$\operatorname{rank}=c-t$。$\square$

**注意**：这**不**自动给出“总层每底分量一个分量”；还需分析纤维的变化与投影像（专家 55 §1.3）。

### 2. 型：Kronecker 替代 Jordan

* **粗数值型**：$\tau_{\mathrm{num}}(W)=(t,\ r=\dim A(W),\ s_0=\dim(W\cap A(W)),\ \kappa=\dim(W\cap\ker A))$。
  它决定 $\dim U=t+r-s_0$、$\ker(A|_W)$、纤维 Grassmannian 的维数；**不**决定不可约分量。
* **细型**：$\tau(W)=(\text{Kronecker type of }(\iota|_W,A|_W),\ \text{ambient incidence data})$。
  第二项未精确化；不能声称它是有限数值不变量。
* **环境 pair**：$(\iota,A_0):D\rightrightarrows K_0$，$D=K_0\cap A^{-1}K_0$；
  $\iota$ 单射 ⇒ pencil $\lambda\iota-A_0$ 满列法秩 ⇒ **无右最小指标块**；奇异结构在左侧 +
  有限/无限初等因子。
* **警告**：Kronecker 型不自动分类 quiver Grassmannian 的分量（专家 55 §3.4）。

**Jordan 型合法的两情形**：$t=c$（$W=V$，自同态）与 $A(W)=W$（可逆自同态）。其余情形无定义。

### 3. $c=2$ 的精确条件（修正 131）

**$t=2$（不变）**：$A(W)\subseteq W$（**不是** $A(W)=W$）。
* 两个不同特征值 $\lambda\ne\mu$：参数空间是
  $$\mathbb P(E_\lambda\cap K_0)\times\mathbb P(E_\mu\cap K_0),$$
  **不是点**（只有在两个交都是一维时才是点）。131 的“点”是错的。
* 标量型：$V\in\operatorname{Gr}(2,E_\lambda\cap K_0)$。
* 非平凡 Jordan 块：$V=\operatorname{span}\{u,T_\lambda u\}$，
  $T_\lambda u\ne0$、$T_\lambda^2u=0$、$u,T_\lambda u\in K_0$；固定特征线 $L$，
  仿射自由度是 $\dim(E_\lambda\cap K_0)-1$（模 $L$），**不是** $\dim E_\lambda$；
  且并非所有 $L$ 都有链向量。

**$t=1$**：$W=L=\mathbb Cv$。
* **A：$A(L)\subseteq L$**（包含 $Av=0$）。取 $V/L$ 的一条线；精确条件是
  $\overline A_V:V/L\to K_0/V$ 单射，等价于代表元 $x\in V\setminus L$ 满足
  $$Ax\notin V.$$
  这是 $K_0/L$ 的线空间中的开集。
* **B：$A(L)\not\subseteq L$**。$Av$ 与 $v$ 独立，$Av\in V$，故 $V=\operatorname{span}\{v,Av\}$；
  精确条件是
  $$\boxed{\operatorname{rank}[v,Av,A^2v]=3}$$
  （等价于 $A^2v\notin V$）。
  **131 的非空条件“$D\ne0$ 且 $A|_D$ 非标量”是假的**：取 $D$ 上的幂零 $J_2$
  （$Ae_1=0$、$Ae_2=e_1$），$A^2v=0$ 对所有 $v\in D$，没有线满足 (B)。
  正确的非空条件是
  $$\boxed{\exists v\in D=K_0\cap A^{-1}K_0:\ \operatorname{rank}[v,Av,A^2v]=3.}$$

**$t=0$**：$V\cap A^{-1}V=0$，即 $\operatorname{rank}\overline A_V=2$，开集。

### 4. $c=3$ 的精确条件（修正 132）

**$t=2$**：$U=W+A(W)$，$\dim U\in\{2,3\}$（纤维非空时）。
* $\dim U=3$：$V=U$ 被决定；**可容许还需** $\operatorname{rank}\overline A_V=1$，例如
  $B=\langle b\rangle$ 时 $Ab\notin V$。132 漏了这个条件。
* $\dim U=2$：$B\subseteq W$（即 $A(W)\subseteq W$）；在 $K_0/W$ 中取线，精确条件是
  $Aw\notin V$（开条件）。
* 正确的分界是 $A(W)\subseteq W$ vs $A(W)\not\subseteq W$，**不是** $A(W)=W$。

**$t=1$**：$W=L=\mathbb Cv$。
* **A：$A(L)\subseteq L$**。商平面 $U=V/L$ 必须满足
  $$\boxed{U\cap\bar A^{-1}U=0}$$
  （等价于 $\bar A_U:U\to(K_0/L)/U$ 秩 2）。132 的“不含 $\bar A$-不变线”**太弱**：
  可以有 $u\in U$、$\bar Au\in U$ 但 $u$ 不在不变线上——这会扩大 $W$，必须排除。
* **B：$A(L)\not\subseteq L$**。$U=L+A(L)$ 二维，加第三条线；精确条件是
  $$\boxed{A^2v+V,\ Aw+V\ \text{在 }K_0/V\text{ 中线性独立}}$$
  （等价于 $\overline A_V:V/L\to K_0/V$ 秩 2）。132 的“$A^2v\notin V$”只是必要，不充分。

**$t=3$**：不变 3-子空间；按**初等因子**分类，不只按分拆 $3$：$1+1+1$、$2+1$、$3$，
但要允许不同特征值的组合 $1_\lambda+1_\mu+1_\nu$、$2_\lambda+1_\mu$、$1_\lambda+2_\lambda$ 等；
参数空间是 $\mathbb C[x]$-子模簇，不必是点或单一仿射丛。

**$t=0$**：$\operatorname{rank}\overline A_V=3$，开集。

### 5. 型控制：降级为猜想

133 的 $N(c)\le\sum_\tau N(t(\tau))$ **不成立**（专家 55 §6.1）：需要
底层的有限分层、纤维的代数性、总空间的分量行为、底分量数的界；$X_\tau$ 不自动是低层同一问题。
正确的陈述是**猜想**：

> **型控制猜想**：固定 $c$，$(W,V)$（$W=V\cap A^{-1}V$、$\dim V=c$）的 incidence 簇
> 有有限个局部闭层，其几何由受限 pair $(\iota|_W,A|_W)$ 的 Kronecker 型与环境嵌入数据控制。

不声称统一的 $N(c)$ 界。$k$-无关性也要修正：Kronecker 数据含维数/块重数，可能随 $k$ 增长。

### 6. 下一步（专家 55 §9）

1. 写并证明**精确纤维定理**（本文件 §1）；
2. 用精确纤维条件**重写 $c=2$**（含本文件 §3 的修正；循环向量条件）；
3. 修正 **$c=3$**（本文件 §4）；
4. 形式化 **Kronecker 表示** $(\iota,A_0)$ 与 quiver Grassmannian incidence；
5. 在底层理解后再证型控制（否则只是猜想）；
6. Lean 并行：核秩不等式（已做）→ lifting 秩公式 → 反例 → 块判据 → 双曲秩恒等式 → 多项式证书；
7. **论文现在就可以写**：精确约化 + 双曲定理 + lifting + generic determinant divisor 为核心；
   $c=2/c=3$ 作为低余维扩展；型控制标为猜想。

## 进展

* 精确纤维条件已写（§1）；Kronecker 替代 Jordan（§2）；
* $c=2$ 的三处错误（点参数化、链纤维维数、假非空条件）与 $c=3$ 的三处弱条件已修正；
* 133 已降级为猜想；$N(c)$ 与 $k$-无关性的问题已记录。

## 最终结论

* **精确纤维定理**（§1）是新的基础；它替代 133 的 $A(V)\cap V=B$。
* **型** = Kronecker 型 + 环境数据，不是 Jordan 型。
* $c=2$：$t=2$ 参数空间是 $\mathbb P\times\mathbb P$；$t=1$ 的 B 需要
  $\operatorname{rank}[v,Av,A^2v]=3$；旧的“$D\ne0$ 且 $A|_D$ 非标量”被 $J_2$ 反例推翻。
* $c=3$：$t=2$ 的 $V=U$ 需 $\operatorname{rank}\overline A_V=1$；$t=1$ 的 A 需
  $U\cap\bar A^{-1}U=0$、B 需秩 2 条件。
* 型控制：**猜想**，不是定理。

## 放弃原因

* 精确纤维定理的**总层分量行为**（投影像、底分层）未证；
* Kronecker 型与环境数据如何精确控制分量，未建立；
* $c=2/c=3$ 的重写只给了条件，未逐型列全表；
* 实点、复杂度未做。

## 残留价值

* 一个正确的、可继续的基础（精确纤维定理 + Kronecker 语言）。
* 明确纠正了 131/132/133 的错误与弱条件，避免继续在错误分类上建归纳。
* 与专家 55 的七问答复完全对齐：下一步顺序、Lean 顺序、论文结构。

## 相关文件

* [attempts/133](133_type_control_theorem.md)（降级为猜想）
* [attempts/131](131_c2_d3_nilpotent_subtype.md)（$c=2$；本文件修正其三处）
* [attempts/132](132_c3_d4_d5_subtypes.md)（$c=3$；本文件修正其三处）
* [attempts/122](122_invariant_eigenspace_obstruction.md)（Lean 内核）
* [docs/05 Q9](../../../../docs/05_open_questions.md)（Kronecker/quiver 的定位）

## 状态

* 精确纤维定理：**[已证-纸面，M2]**。
* Kronecker 型框架：**[草稿，M2]**。
* $c=2/c=3$ 精确条件：**[已证-纸面/条件，M2]**（表未列全）。
* 型控制：**[猜想]**。
