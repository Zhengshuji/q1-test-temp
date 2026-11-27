# 655 约束 Grassmann 表述与条件化充分性

> 2026-11-27。按 ChatGPT 的建议，把 653 的第三条（$UZ'\subseteq U+S$）写成 Grassmann 约束，
> 并明确下一步的“条件化充分性引理”。
> 状态：**[已证-纸面]**（等价性）+ **[开放]**（条件化充分性）。

## 约束 Grassmann 集

$T=T_\infty$、$d=k-\dim T$、$U_0=\operatorname{row}(H_0)$。
$$\mathcal G=\left\{U\in\operatorname{Gr}(d,k):\ U_0\subseteq U\subseteq T^\perp,\ UZ'\subseteq U+S\right\}.$$

## 秩条件写法

设 $B$ 为 $U$ 的行基（$d\times k$），$B_S$ 为 $S$ 的行基。则
$$UZ'\subseteq U+S\iff
\operatorname{rank}\begin{bmatrix}B\\ BZ'\\ B_S\end{bmatrix}
=\operatorname{rank}\begin{bmatrix}B\\ B_S\end{bmatrix}.$$
（左边是 $\dim(U+UZ'+S)$，右边是 $\dim(U+S)$；相等 ⇔ $UZ'\subseteq U+S$。）

## 必要条件汇总

1. $H_0|_{T}=0$（⇔ $U_0\subseteq T^\perp$）；
2. $\operatorname{rank}H_0\le d$（⇔ $\dim U_0\le d$）；
3. $\mathcal G\ne\varnothing$（即存在满足 $UZ'\subseteq U+S$ 的 $U$）。

## 条件化充分性（猜想）

> 对每个 $U\in\mathcal G$，存在 $H$（行空间 $U$、含 $H_0$）与 $Z$，使
> $$ZH-HZ'\in\operatorname{Mat}_{q\times k}(S),\qquad
> \operatorname{im}H\cap\ker(Z-\lambda I)=0\ \forall\lambda .$$

若成立，则 q1 判定从“搜索 $R$”化为“判定 $\mathcal G\ne\varnothing$ + 构造 $Z$”。

## 检验

- **638**：$T=\operatorname{span}\{e_3\}$、$d=2$、$U=\operatorname{span}\{e_1,e_2\}$、$S=\operatorname{span}\{e_2\}$。
  $UZ'=\operatorname{span}\{e_1\}\subseteq U$ ✓，$\mathcal G$ 非空；
- **631**：$T=0$、$d=k$、$U=S$ 空缺？$U_0=0$；任意 $U$ 满足 $UZ'\subseteq U+S$ 需要选取，构造已知可行；
- **648/650/654**：$T=\mathbb C^3$、$d=0$ ⇒ $U=0$；若 $U_0\ne0$ 则 $\mathcal G=\varnothing$ ⇒ 不可行 ✓。

## 意义

- $\mathcal G$ 的约束是线性代数/行列式的（Schubert + 一个秩等式），可计算；
- 若条件化充分性成立，q1 的可行性判定可转为“$\mathcal G$ 非空且 $Z$ 可选”——比原始搜索结构化。

## 下一步

1. 证明或反驳条件化充分性（先在小 $k,q$ 上实验）；
2. 若成立，写出 $\mathcal G$ 非空性的多项式判定；
3. 与 ChatGPT 核对秩条件的写法（它提醒“秩不等式不保证包含”）。

## 状态

- $\mathcal G$ 与秩条件：**[已证-纸面]**；
- 条件化充分性：**[M2 猜想]**。
