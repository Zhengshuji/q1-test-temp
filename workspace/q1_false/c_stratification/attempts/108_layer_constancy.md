# 分层常值性：$\dim X_S$ 的秩公式

> 2026-11-08。补 attempts/107 的最实缺口：证明在常秩层上 $\dim X_S$（以及 $E+X_S$ 的维数）
> 确实常值。状态：**M2（纸面）**；证明是线性代数，不依赖未证猜想。

## 目标

在 $k=\omega+1$、$q=\omega+1$ 的设定下，设 $S=\ker\sigma$（$\dim S=\omega$），$B$ 为 $k\times\omega$ 的基，
$$P=B^\top Z_1,\qquad Q=B^\top Z_2\quad(\omega\times d),$$
$$X_S=\{a\in\mathbb C^\omega:\ aP\in\operatorname{row}(Q)\}.$$
证明：在 $\operatorname{rank}Q$ 与 $\operatorname{rank}[P;Q]$ 常值的层上，$\dim X_S$ 常值；
并说明 $E+X_S$ 的维数也可通过有限细分变成常值。

## 设想与理由

* $X_S$ 是"$a\mapsto aP$ 模 $\operatorname{row}Q$"的核；用秩-零化度，$\dim X_S$ 应等于
  $\omega-(\operatorname{rank}[P;Q]-\operatorname{rank}Q)$。
* 这样就不需要"$X_S$ 是核/像的复合、逐层检查"这种含糊论证；秩条件直接给出常值性。
* $E+X_S$ 的维数由 $\dim X_S$ 与 $X_S\subseteq E$ 与否决定；后者是闭条件，细分后常值。

## 做法

**引理 1（$\dim X_S$ 的秩公式）**：
$$\dim X_S=\omega-\big(\operatorname{rank}[P;Q]-\operatorname{rank}Q\big).$$

*证明*：考虑线性映射
$$\psi:\mathbb C^\omega\longrightarrow \mathbb C^d/\operatorname{row}(Q),\qquad a\longmapsto aP\bmod \operatorname{row}(Q).$$
$\ker\psi=X_S$。$\psi$ 的像 $=(\operatorname{row}P+\operatorname{row}Q)/\operatorname{row}Q$，其维数
$$=\dim(\operatorname{row}P+\operatorname{row}Q)-\dim\operatorname{row}Q
=\operatorname{rank}[P;Q]-\operatorname{rank}Q.$$
由秩-零化度，$\dim X_S=\omega-\operatorname{rank}\psi$。$\square$

**推论 1**：在 $\operatorname{rank}Q$ 与 $\operatorname{rank}[P;Q]$ 常值的层上，$\dim X_S$ 常值。
这两个秩都是 $\sigma$ 的确定性秩条件（$P,Q$ 的元素是 $\sigma$ 的多项式），故每层是局部闭的；
秩只取有限个值，故分层有限。

**引理 2（$E+X_S$ 的精确条件）**：在可容许层上 $E\subseteq S$，$X_S\subseteq S$。则
$$\dim(E+X_S)=e+\dim X_S-\dim(E\cap X_S),\qquad e=\dim E .$$
故
$$E+X_S=S\iff e+\dim X_S-\dim(E\cap X_S)=\omega .$$
注意“$X_S\not\subseteq E$”只说明 $E+X_S$ 严格大于 $E$，一般**不**等于 $S$
（例：$S=\mathbb C^3$、$E=\langle e_1\rangle$、$X_S=\langle e_2\rangle$）；它只在 $e=\omega-1$
（或 $\dim X_S=\omega$）时充分。正确做法是按 $t=\dim(E\cap X_S)$ 细分；$t$ 是秩条件（局部闭），
每片上 $e+\dim X_S-t$ 常值，再检查是否等于 $\omega$。另外需要 $m\ge\omega-e$
（$m=q-r$ 行底部行要张成 $S/E$）。

**定理（分层常值性）**：按
$$\big(\operatorname{rank}Q,\ \operatorname{rank}[P;Q],\ \dim(E\cap X_S)\big)$$
细分后，每片上 $\dim X_S$、$\dim(E+X_S)$ 常值；细分仍是有限个局部闭层。

## 进展

* 引理 1、推论 1、引理 2 已证（线性代数，无未证假设）。
* **专家 52 号更正**：原稿把 $E+X_S=S$ 当成 $X_S\not\subseteq E$ 的补；当 $e<\omega-1$ 时这是错的。
  已改为精确等式 $e+\dim X_S-\dim(E\cap X_S)=\omega$，并按 $t=\dim(E\cap X_S)$ 细分；另加 $m\ge\omega-e$。
* **应用（attempts/104）**：$p=0$、$Q=B^\top e_1$；开层 $q\ne0$ 时 $\operatorname{rank}Q=1$，
  $\operatorname{rank}[P;Q]=1$，故 $\dim X_S=2-(1-1)=2$；点 $q=0$ 时两个秩都是 $0$，故
  $\dim X_S=2-(0-0)=2$。$E=0$ 故 $E+X_S=S$。与 104 的显式计算一致。
* 未做：把这套细分写成程序对所有 $\sigma$ 枚举；一般 $k$ 的不可约分量仍未处理。

## 最终结论

* 107 的"分层常值性"缺口**已闭合**：$\dim X_S$ 有显式秩公式，$E+X_S$ 的维数经有限细分常值。
* 107 的定理现在只剩"不可约分量枚举 / 一般 $k$ / 实点"三个缺口；分层部分不再含糊。
* 这仍是结构定理，不是 $q1$ 的算法。

## 放弃原因

* 没有把细分写成程序；$k=3$ 的枚举验证留到下一轮。
* 一般 $k$ 的不可约分量枚举超出本轮；这里只证"分层存在且有限"。

## 残留价值

* 一条干净的秩公式 $\dim X_S=\omega-(\operatorname{rank}[P;Q]-\operatorname{rank}Q)$，
  可直接用于任何 $k=\omega+1$ 的例子。
* 把 107 的定理从"骨架"推进到"分层部分可检查"。
* 对 $E=0$、$r=1$ 的情形（104 的例子）给出完整常值性。

## 相关文件

* [attempts/107](107_projective_constrained_theorem_v2.md)（投影约束定理写实版；本文件补其常值性）
* [attempts/104](104_p2_constrained_locus.md)（$\mathbb P^1$ 例；本文件的实例）
* [proof/B.24/README.md](../../../../proof/B.24/README.md)（闭性、定理 A）
* [workspace/ROADMAP.md](../../../ROADMAP.md) §5

## 状态

* 引理 1/2：**[已证-纸面]**（秩-零化度 + 有限细分）。
* 107 的常值性缺口：**已闭合**。
* 剩余：分量枚举、一般 $k$、实点、程序验证。
