# $c=2$ 的好性：正确的块形式与两个分支（更正 144 的维度错误）

> 2026-11-08。上一版 144 把 $H$ 当成 $\omega\times k$，实际上 $H=L N_K$ 是 $q\times k=(\omega+1)\times(\omega+2)$。
> 本文件改正维度，写出**完整**的坏条件（不是单一特征向量判据），并指出 $c=1$ 与 $c=2$ 的差别。
> 状态：**M2（部分）**。

## 目标

判定 $c=2$、$q=\omega+1$ 时的**好性**（坏条件的反面）：对给定的 $(H,H_A)$，是否存在 $\lambda$ 使
$\operatorname{rank}(\lambda H-H_A)<\omega$。

## 设想与理由

$H=L N_K$ 是 $(\omega+1)\times k$、秩 $\omega$。用 $V=\ker H$（2 维）与 $\mathbb C^q$ 的
$\omega+1$ 分解把 $P$ 写成块矩阵；坏 = 行相关，得到一个 $(x,\alpha)$ 系统。

## 做法

## 正确的块形式

设 $q=\omega+1$、$k=\omega+2$（$c=2$），$H=L N_K\in\mathbb C^{q\times k}$，$\operatorname{rank}H=\omega$。
取基使
$$\mathbb C^k=V\oplus W_0,\qquad \dim V=2,\ \dim W_0=\omega;\qquad
\mathbb C^q=W_1\oplus W_2,\qquad \dim W_1=\omega,\ \dim W_2=1,$$
且
$$H=\begin{bmatrix}H_0&0\\0&0\end{bmatrix},\qquad H_0\in\mathrm{GL}_\omega,$$
（$H$ 的最后一行为 0，因为秩 $\omega<q$）。写
$$H_A=\begin{bmatrix}A_{11}&A_{12}\\B_1&B_2\end{bmatrix},\qquad
A_{11}\in\mathbb C^{\omega\times\omega},\ A_{12}\in\mathbb C^{\omega\times2},\ B_1\in\mathbb C^{1\times\omega},\ B_2\in\mathbb C^{1\times2}.$$
则
$$P(\lambda)=\lambda H-H_A=\begin{bmatrix}\lambda H_0-A_{11}&-A_{12}\\-B_1&-B_2\end{bmatrix}.$$

## 坏条件（完整）

$\operatorname{rank}P(\lambda)<\omega$ $\iff$ $P(\lambda)$ 的 $\omega+1$ 行线性相关
$\iff$ 存在 $0\ne(x,\alpha)\in\mathbb C^\omega\oplus\mathbb C$ 使
$$\boxed{x^{\mathsf T}(\lambda H_0-A_{11})=\alpha B_1,\qquad x^{\mathsf T}A_{12}=-\alpha B_2.}$$
（第一式是行向量方程：$x^{\mathsf T}(\lambda H_0-A_{11})-\alpha B_1=0$；第二式同理。）

### 分支 $\alpha=0$（齐次障碍）

$$x^{\mathsf T}A_{11}=\lambda x^{\mathsf T}H_0,\qquad x^{\mathsf T}A_{12}=0.$$
$H_0$ 可逆，令 $A=H_0^{-1}A_{11}$、$C=H_0^{-1}A_{12}$（左乘 $H_0^{-1}$ 不改变条件），得
$$\boxed{A^{\mathsf T}x=\lambda x,\qquad C^{\mathsf T}x=0.}$$
即 $x$ 是 $A^{\mathsf T}$ 的特征向量且落在 $\ker C^{\mathsf T}$ 中——这就是 121 的超平面判据在 $c=2$ 的类比
（$C^{\mathsf T}$ 是 $\omega\times2$，$\ker$ 维数 $\omega-2$）。

### 分支 $\alpha\ne0$（仿射障碍）

可令 $\alpha=1$（齐次），得
$$x^{\mathsf T}(\lambda H_0-A_{11})=B_1,\qquad x^{\mathsf T}A_{12}=-B_2.$$
这是关于 $(x,\lambda)$ 的**仿射特征值**条件；它**不是**单纯的“特征向量在子空间里”，
在 $c=2$ 可能出现（$c=1$ 时由提升约束排除，需单独核对）。

## 好性

好 $\iff$ 对每个 $\lambda$，上述 $(x,\alpha)$ 系统只有零解
$\iff$ 两个分支都空：
* $\alpha=0$：$\ker C^{\mathsf T}$ 不含 $A^{\mathsf T}$ 的特征向量；
* $\alpha\ne0$：仿射系统 $x^{\mathsf T}(\lambda H_0-A_{11})=B_1,\ x^{\mathsf T}A_{12}=-B_2$ 对每个 $\lambda$ 无解。

## 与 121（$c=1$）的关系

$c=1$ 时 $V$ 是线、$W_2$ 1 维、$A_{12}$ 是 $\omega\times1$、$B_2$ 是 $1\times1$。
121 的结论“坏 $\iff$ 特征向量落在 $\mathbb P(K_0)$ 的射影特征子空间”对应 $\alpha=0$ 分支；
$\alpha\ne0$ 分支在 $c=1$ 是否恒空，需要按 121 的提升约束核对（本文件未证）。
$c=2$ 时 $A_{12}$ 是 $\omega\times2$，$\alpha\ne0$ 分支不能忽略。

## 对 144 的更正

* 原 144 把 $H$ 当成 $\omega\times k$ 并令 $HS=[I\mid0]$：**维度错误**；$H$ 是 $q\times k$，正确形式如上。
* 原 144 的“坏 $\iff A^{\mathsf T}x=\lambda x,\ B^{\mathsf T}x=0$”只对应 $\alpha=0$ 分支；
  **漏了 $\alpha\ne0$ 的仿射分支**。

## 重要澄清：$t=2$ 时 $P$ 在 $V$ 上为零

若 $V$ 不变（$t=2$，即 $A(V)\subseteq V$），则对 $v\in V$：
$$Hv=0,\qquad H_A v=L A N_K v=L(A v)=0,$$
因为 $A v\in V$ 而 $L N_K V=H V=0$。故 $P(\lambda)v=0$，$P$ **降到一个 $q\times\omega$ 块**：
取 $\mathbb C^k=V\oplus W_0$，$P$ 由其在 $W_0$ 上的限制给出
$$\begin{bmatrix}\lambda I-A\\ B\end{bmatrix}:W_0\to W_0\oplus W',\qquad y\mapsto((\lambda I-A)y,\ By),$$
其中 $W'=\mathbb C^{q-\omega}$（$q=\omega+1$ 时 1 维）。于是 BlockIff 判据适用：
$$\text{坏}\iff\exists\,0\ne y\in W_0:\ Ay=\lambda y,\ By=0.$$
**这正是 144 的判据在 $t=2$ 的正确性**；144 的问题只在把它误用于 $t<2$。

对 $t<2$（$V$ 不不变，$A(V)\not\subseteq V$），$Pv=-H_A v\ne0$，$P$ 不能降为 $q\times\omega$；
必须用本文件上面的完整 $(x,\alpha)$ 系统。

## 固定 $A$ 时的“好提升存在性”引理

设 $A$ 固定（不随提升变），提升族给出的 $B$ 是仿射族
$$B(t)=B_0+\sum_i t_iB_i,\qquad t\in\mathbb C^N.$$
坏集是
$$\bigcup_{y\ \text{特征向量}}\{t:\ B(t)y=0\},$$
每个 $\{t:B(t)y=0\}$ 是仿射超平面。$\mathbb C^N$ 不能写成有限个**真**仿射子空间之并
（无限域；仿射空间不可约），故：

> **引理**：好提升存在 $\iff$ 不存在 $A$ 的特征向量 $y$ 使 $B(t)y=0$ 对所有 $t$ 成立
> $\iff$ 公共核 $\bigcap_t\ker B(t)=\bigcap_i\ker B_i\cap\ker B_0$ 不含 $A$ 的特征向量。

证明：若存在这样的 $y$，则所有 $t$ 都坏；若不存在，则每个超平面 $\{B(t)y=0\}$ 都是真的，
有限并不能覆盖整个仿射空间，故存在好 $t$。$\square$

**适用条件**：$A$ 不随提升变。若提升同时改变 $A$，需把 $A$ 也参数化；此时坏集是
“$B(t)$ 的公共核含 $A(t)$ 的特征向量”，不再是有限个固定超平面，引理不直接适用。
$A$ 不变的充分情形包括 $A(K)\subseteq K$ 且提升只改 $W'$-分量；这一情形下引理可直接用。

## 进展





* 正确的块形式与完整坏条件已写出；两个分支分离。
* $\alpha=0$ 分支化为“$\ker C^{\mathsf T}$ 不含 $A^{\mathsf T}$ 特征向量”——可算法化。
* $\alpha\ne0$ 分支化为仿射特征值系统；其非空性待判。

## 最终结论

* $c=2$ 的好性 = 两个分支都空；不是单一特征向量判据。
* 下一步：对 $(2a)$ 的 $V=\ell_\lambda\oplus\ell_\mu$，把 $A_{11},A_{12},B_1,B_2$ 用提升参数写出，
  分别判定两个分支。

## 放弃原因

* 两个分支在 $(2a)$ 的提升参数化未完成；
* $c=1$ 的 $\alpha\ne0$ 分支是否恒空未证。

## 残留价值

* 修正了 144 的维度错误与不完整判据；给出可继续计算的正确形式。

## 相关文件

* [attempts/143](143_c2_rigorous_parameterization.md)（可容许层）
* [attempts/144](144_c2_good_locus.md)（上一版，含维度错误，本文件更正）
* [attempts/121](121_hyperplane_vector_bundle.md)（$c=1$）
* [lean/BlockIff](../../../../trash/lean_removed_2026-11-19/augmentation_lean/BlockIff.md)（块判据的 Lean 形式，针对 $q\times\omega$ 的列堆叠）

## 状态

* 正确块形式/完整坏条件：**[已证-纸面，M2]**。
* 分支非空性/$(2a)$ 提升判定：**[未做]**。
