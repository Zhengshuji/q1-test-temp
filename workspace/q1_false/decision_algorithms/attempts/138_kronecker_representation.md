# Kronecker 表示与 incidence 表述（专家 55 §3 / §7 / §9 Step 4）

> 2026-11-08。按专家 55 号：把 $c$ 维子空间问题写成 Kronecker 表示
> $(\iota,A_0):D\rightrightarrows K_0$（$D=K_0\cap A^{-1}K_0$）的子表示/incidence 问题，
> 而不是 $A|_W$ 的 Jordan 型。状态：**M2（纸面；表述与引理）**。

## 目标

1. 定义环境 pair $(\iota,A_0)$ 与受限 pair $(\iota|_W,A|_W)$；
2. 把精确纤维条件写成子表示 + 极大性条件；
3. 说明 Kronecker 型与 quiver Grassmannian 的分工与边界。

## 设想与理由

* $W\subseteq D$ 是必要的（$A(W)\subseteq K_0$）；$D$ 是**所有**候选 $W$ 的 ambient space。
* pair $(\iota,A_0)$ 的 pencil $\lambda\iota-A_0$ 是 Kronecker quiver（两条平行箭头 $D\to K_0$）的表示。
* $\iota$ 单射 ⇒ 满列法秩 ⇒ 无右最小指标块；奇异结构在左侧 + 有限/无限初等因子。
* 受限 pair $(\iota|_W,A|_W):W\rightrightarrows W+A(W)$ 的 Kronecker 型在 $A(W)\not\subseteq W$ 时仍有定义
  （这是替换 Jordan 型的关键）。

## 做法

### 1. 环境 pair

$$D=K_0\cap A^{-1}K_0,\qquad \iota:D\hookrightarrow K_0,\qquad A_0=A|_D:D\to K_0.$$
pencil
$$P(\lambda)=\lambda\iota-A_0.$$
$\iota$ 单射 ⇒ $P(\lambda)$ 对一般 $\lambda$ 满列秩 ⇒ 无右最小指标块。Kronecker 标准形记录：
有限初等因子、无限初等因子、左最小指标（Berger–Trunk–Winkler 2016；Berger–Trenn 2012；
Gantmacher Vol II Ch XII）。

### 2. 受限 pair

对 $W\subseteq D$：
$$\iota|_W:W\to W+A(W),\qquad A|_W:W\to W+A(W),$$
pencil $\lambda\iota|_W-A|_W$。这是 $W\rightrightarrows W+A(W)$ 的 Kronecker 表示；其 Kronecker 型
在 $A(W)\not\subseteq W$ 时仍有定义（Jordan 型则无定义）。

### 3. 子表示与极大性

$(W,U)$ 是 $(\iota,A_0)$ 的**子表示**，若
$$W\subseteq D,\quad U\subseteq K_0,\quad \iota(W)\subseteq U,\quad A_0(W)\subseteq U.$$
**极大性条件**：
$$U=W+A(W).$$
精确纤维条件（135）：
$$V\supseteq U,\quad \dim V=c,\quad \operatorname{rank}(V\to K_0/V)=c-\dim W,$$
等价于 $V\cap A^{-1}V=W$。

**incidence 簇**：
$$\mathcal E_c=\{(W,U,V):\ (W,U)\ \text{子表示},\ U=W+A(W),\ V\supseteq U,\ \dim V=c,\ 
\operatorname{rank}(V\to K_0/V)=c-\dim W\}.$$
它到 $\mathcal D_s$ 有自然投影 $(W,U,V)\mapsto V$；$W=V\cap A^{-1}V$ 由 $V$ 唯一决定，故此投影是
**双有理/单射在像上**（在 $V$ 的 $W$ 唯一的层上）。这是把“分量分解”转成“子表示 Grassmannian”的桥。

### 4. Quiver Grassmannian 与边界

固定维数 $t,u$，子表示 $(W,U)$ 的集合是 quiver Grassmannian（Caldero–Reineke 2008 的框架；
Kronecker quiver 是标准对象）。极大性 $U=W+A(W)$ 是额外的秩条件（像的维数固定）。

**边界（专家 55 §3.4）**：Kronecker 型分类**环境 pair**，不自动分类 quiver Grassmannian 的
分量；子空间 incidence 的几何可以仍然复杂。所以 138 给的是“正确的语言”，不是“分量已分类”。

## 进展

* 环境 pair、受限 pair、子表示、极大性、incidence 簇都已写出。
* 精确纤维条件与子表示条件接上了：$V\supseteq W+A(W)$ + 极大秩。
* 明确了 Kronecker 型的作用（分类环境 pair）与边界（不分类子空间簇）。

## 最终结论

* 正确的对象是 $(\iota,A_0):D\rightrightarrows K_0$ 的子表示 + 极大性 + 精确纤维条件。
* 受限 Kronecker 型替代 Jordan 型，在非不变情形也有定义。
* quiver Grassmannian 是子空间簇的正确语言；Kronecker 型是环境 pair 的规范形。
* 这是专家 55 §9 Step 4 的落实。

## 放弃原因

* 未证明 incidence 簇的分量/不可约性。
* 未把 Kronecker 型与环境数据精确到“控制分量”的定理（这是 139 的猜想内容）。
* 未处理实点。

## 残留价值

* 一个正确的、可继续的表示论框架。
* 把 135/136/137 的精确条件统一成“子表示 + 极大性 + 极大秩”。
* 为论文的“General Grassmannian formulation”一节提供内容。

## 相关文件

* [attempts/135](../../c_stratification/attempts/135_exact_fibre_theorem.md)（精确纤维）
* [attempts/136](../../c_stratification/attempts/136_c2_rewrite.md)（$c=2$）
* [attempts/137](../../c_stratification/attempts/137_c3_repair.md)（$c=3$）
* [attempts/139](139_type_control_conjecture.md)（型控制猜想）

## 状态

* 表述/引理：**[已证-纸面，M2]**。
* 分量/不可约性：**[开放]**。
