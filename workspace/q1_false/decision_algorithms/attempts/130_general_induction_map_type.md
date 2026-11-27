# 一般 $c$ 的归纳：线性映射型控制（并更正“不变子空间”说法）

> 2026-11-08。写一般 $c$ 的归纳前，先修正 125/128 的一个错误：
> “$\mathcal D_3$ = 含不变线 / $\mathcal D_4$ = 含不变 2-子空间”**不成立**。
> 正确的对象是 $W=V\cap A^{-1}V$ 与线性映射 $A|_V:V\to K$ 的**型**。
> 状态：**M2（纸面草稿）**；一般 $c$ 的型分类只给了框架。

## 目标

1. 给出反例，说明“不变线/不变子空间”不覆盖 $\mathcal D_s$；
2. 用 $W=V\cap A^{-1}V$ 与 $A|_V$ 的**线性映射型**重述分层；
3. 陈述一般 $c$ 的归纳：固定 $c$ 时分量由型控制，与 $k$ 无关。

## 设想与理由

* 125/128 的“不变子空间”只覆盖 $AW=W$ 的子型；$\mathcal D_s$ 的定义只用 $W=V\cap A^{-1}V$，
  $W$ 不必不变。
* 正确的归纳对象是 $(W,A|_V)$ 的**线性映射型**；固定 $c$ 时型是有限个整数元组。
* 每层应是 Grassmannian 上的线性条件纤维，故分量数只依赖 $c$ 与型。

## 做法

### 反例：$t=1$ 但无不变线

取 $K=K_0=\mathbb C^4$，$A=J_4(0)$（$Ae_1=0$、$Ae_2=e_1$、$Ae_3=e_2$、$Ae_4=e_3$），
$c=2$，$V=\langle e_2,e_3\rangle$。则
$$V\cap A^{-1}V=\langle e_3\rangle,\qquad t=1,$$
但 $V$ 中**没有**不变线：
* $Ae_2=e_1\notin V$，$Ae_3=e_2\in V$ 但 $e_2\notin\langle e_3\rangle$；
* 任意 $\alpha e_2+\beta e_3$ 的像 $\alpha e_1+\beta e_2$ 要落在自身张成的线里，只能 $\alpha=\beta=0$。

所以 $V\in\mathcal D_3$（$c=2$，$\rho=3$）但不含不变线。125 的“$\mathcal D_3$ = 含不变线”**只覆盖了
$A W=W$ 的子型**，漏掉了 $A W\ne W$ 的“幂零链”子型。

## 正确的分层：$W=V\cap A^{-1}V$ 与线性映射型

对 $V\in\operatorname{Gr}(c,K_0)$，令
$$W=V\cap A^{-1}V,\qquad t=\dim W,\qquad \rho(V)=2c-t.$$
则 $A(W)\subseteq V$，且 $W=\ker(V\to K/V)$。定义**型**
$$\tau(V)=\big(t,\ \dim A(W),\ \dim(A(W)\cap W),\ \operatorname{rank}(A|_W),\ 
\dim(V\cap\ker A),\ \dim(A(V)\cap V)\big).$$
（这些量都由 $V$ 与固定的 $A$ 决定；$\dim(A(V)\cap V)=t$。）

**分层**：$\mathcal D_s=\{V:\rho(V)\le s\}=\{V:t\ge2c-s\}$，再按 $\tau$ 细分。
* $t=c$：$AV\subseteq V$（不变 $c$-子空间）；
* $t<c$：$W$ 可能不变（$AW=W$）也可能不变（$AW\ne W$，甚至 $AW\cap W=0$）；
* 每一型都是 $V$ 与 $A$ 的**线性代数条件**（子空间包含/维数），故是局部闭层。

## 归纳的结构

固定 $c$ 与一个型 $\tau$。层内：
* $W$ 是 $t$ 维子空间，且 $A(W)\subseteq V$；
* $V$ 是 $W$ 的 $(c-t)$ 维扩张；
* 给定 $W$，$A|_W:W\to K$ 的像 $A(W)$ 是固定的（由 $W$ 决定），$V$ 必须包含 $A(W)$ 与 $W$，
  并在 $K/(W+A(W))$ 中选 $(c-t-\dim(A(W)/(A(W)\cap W)))$ 维。

所以每层是**以 $W$ 的 Grassmannian 为底、以线性条件切出的 Grassmannian 纤维**的丛；
分量数由 $c$ 与型 $\tau$ 的组合（有限）控制，与 $k$ 无关。

**归纳命题（草稿）**：

> 对固定 $c$，$\mathcal D_s$ 的每个分量都是“某个 $t\le c$ 的子空间 $W$ 的 Grassmannian 上的
> 线性条件纤维”的丛；型的组合数只依赖 $c$（有限），与 $k$ 无关。最低层 $t=c$ 是
> $A$-不变 $c$-子空间；其余层由 $W$ 与 $A(W)$ 的相对位置（$\dim(A(W)\cap W)$ 等）分类。

这比“不变子空间控制”弱，但仍然是**有限、$k$-无关**的；且它正确覆盖了反例。

## 修正 125/128

* 125 的 $\mathcal D_3$：应分成
  * $AW=W$（不变线，$A W=W$）；
  * $AW\ne W$（幂零链型；反例 $V=\langle e_2,e_3\rangle$）。
  两类的非空条件不同（后者要 $AW\subseteq V$ 但 $AW\nsubseteq W$）。
* 128 的 $\mathcal D_4$：“含不变 2-子空间”只覆盖 $AW=W$ 的子型；一般 $W=V\cap A^{-1}V$ 不必不变。
  正确的说法是“含 $W$ 且 $A(W)\subseteq V$”，$W$ 由 $V$ 决定。
* 这两处是**过度简化**，不是致命错误：不变子空间情形是其中一层；但一般归纳必须用型。

## 进展

* 反例已给出（$J_4(0)$、$V=\langle e_2,e_3\rangle$）。
* 正确的型 $\tau(V)$ 与分层框架已写；每层是 Grassmannian 上的线性条件纤维。
* 归纳命题已陈述（草稿）：固定 $c$ 时型有限、分量 $k$-无关。
* 未做：一般 $c$ 的型分类（哪些型非空、型之间的包含关系）；分量数的显式函数；具体验证。

## 最终结论

* “不变子空间控制”是**错的**；正确的是“**线性映射型控制**”：$W=V\cap A^{-1}V$ 与 $A|_V$ 的像/核维数。
* 固定 $c$ 时，型是有限个整数元组；每层是 Grassmannian 上的线性条件纤维；分量数只依赖 $c$ 与型，
  与 $k$ 无关。
* 这把 Q9 的分量问题归约成“$c$ 固定的有限型分类 + Grassmannian 上的线性代数”，比“任意 determinantal variety”可控。

## 放弃原因

* 一般 $c$ 的型分类只给了框架，没有逐型列出；
* 每层是否不可约、分量数是否真的只依赖型，未逐型证明；
* 没有实例验证。

## 残留价值

* 一个明确的反例，纠正了 125/128 的“不变子空间”过度简化。
* 正确的型 $\tau(V)$ 与分层框架，可作为一般归纳的起点。
* 说明“模型控制”应理解为“线性映射型控制”，不是“不变子空间控制”。

## 相关文件

* [attempts/125](../../c_stratification/attempts/125_c2_structure_complete.md)（$c=2$ 分类；本文件更正其 $\mathcal D_3$）
* [attempts/128](../../c_stratification/attempts/128_c3_structure.md)（$c=3$ 层；本文件更正其 $\mathcal D_4$）
* [attempts/129](../../c_stratification/attempts/129_c3_jordan_truncation.md)（$c=3$ Jordan/截断）
* [docs/05 Q9](../../../../docs/05_open_questions.md)（$\mathcal D_s$ 的定位）

## 状态

* 反例：**[已证-纸面]**。
* **反例 Lean 内核**：`counterexample_t1`、`counterexample_no_invariant_line`
  （`workspace/augmentation_family/lean/CounterKernel.lean`）编译通过，axioms 干净；
  用 $J_3(0)$、$V=\langle e_1,e_2\rangle$ 机器检查“$t=1$ 但无不变线”。
* 型框架：**[草稿，M2]**。
* 一般归纳命题：**[草稿，M2]**（未逐型证明）。
* 未做：型分类、分量数显式函数、实例验证。
