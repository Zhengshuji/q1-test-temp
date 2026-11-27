# 顶层（$\rho=d$）的可观测判据：完整证明

> 对应 [docs/02](../../docs/02_theorems_proven.md) 的 B.2。本文是**展开版**。
> 数值复核：[tools/certificates/c191_pbh.py](../../tools/certificates/c191_pbh.py)（铅笔 65/65、可观测 65/65；"可控"只有 63/65 ⟹ 旧措辞是错的）。

## 0. 设定

沿用 [docs/01](../../docs/01_notation.md)：$\mathcal J=\operatorname{row}[C;CA]$、$j=\dim\mathcal J$、$d=n-j$、$\pi:\mathbb C^n\twoheadrightarrow X:=\mathbb C^n/\mathcal J$。

设解 $\mathcal L$（$q$ 行、行满秩）满足 $(5a)$ 且 **$\rho:=\dim\pi(\mathcal V)=d$**（"顶层"，$q=c+d$）。记
$$H=\mathcal V\cap\mathcal J\ (\dim c),\qquad \mathcal V=H\oplus W\ (\dim W=d,\ W\cap\mathcal J=0).$$
（这样的 $W$ 存在：$\pi|_{\mathcal V}$ 的核是 $H$，取象的任一截面即可。）

固定 $W$ 的一组基 $w_1,\dots,w_d$ 与 $H$ 的一组基 $h_1,\dots,h_c$。定义

$$T_W:=\pi_W A|_W:W\to W,\qquad D_W:=\big[\pi_W(h_1A)\ \cdots\ \pi_W(h_cA)\big]\in\mathbb C^{d\times c},$$

其中 $\pi_W:\mathbb C^n\to W$ 是沿 $\mathcal J$ 的投影（因 $\mathbb C^n=W\oplus\mathcal J$ 而良定义）。

> **记号约定**：本文用**行向量**约定（与项目其余部分一致）：$\mathcal L$ 是 $q\times n$，$\pi(\mathcal L)$ 是 $q\times d$。

## 1. 铅笔恒等式

**引理 1.1** 在 $\mathcal V=H\oplus W$ 的基 $h_1,\dots,h_c,w_1,\dots,w_d$ 下，
$$Q_{\mathcal V}(\lambda)\;=\;\lambda\,\pi(\mathcal L)-\pi(\mathcal LA)\;=\;\begin{pmatrix}-D_W^{\mathsf T}\\ \lambda I_d-T_W\end{pmatrix}\in\mathbb C^{(c+d)\times d}.$$

*证明*：$\pi$ 在 $\mathcal J$ 上为零，而 $H\subseteq\mathcal J$，故 $\pi(h_i)=0$；且 $\pi|_{W}:W\to X$ 是同构，取 $W$ 的基使其对应 $X$ 的标准基，则 $\pi(w_j)=e_j$。

于是
- 前 $c$ 行（$h_i$ 对应的行）：$\lambda\pi(h_i)-\pi(h_iA)=-\pi(h_iA)=-\big(\pi_W(h_iA)\big)^{\mathsf T}$，正是 $-D_W^{\mathsf T}$ 的第 $i$ 行；
- 后 $d$ 行（$w_j$ 对应的行）：$\lambda e_j-\pi(w_jA)=\lambda e_j-\big(\pi_W(w_jA)\big)^{\mathsf T}$，即 $\lambda I_d-T_W$ 的第 $j$ 行。$\square$

## 2. 主定理

**定理 2.1** 若 $\rho=d$，则
$$(5b)\iff \operatorname{rank}Q_{\mathcal V}(\lambda)=d\ \ \forall\lambda\in\mathbb C\iff (D_W^{\mathsf T},T_W)\ \text{可观测},$$
即可观测性判据
$$\operatorname{rank}\begin{pmatrix}D_W^{\mathsf T}\\ D_W^{\mathsf T}T_W\\ \vdots\\ D_W^{\mathsf T}T_W^{d-1}\end{pmatrix}=d .$$

*证明*：
$(5b)\iff\operatorname{rank}Q_{\mathcal V}(\lambda)=d\ \forall\lambda$ 是引理 1.2（$\rho=d$）。

**($\Rightarrow$)** 若存在 $0\ne\xi\in\mathbb C^d$ 与 $\lambda$ 使 $D_W\xi=0$ 且 $T_W\xi=\lambda\xi$，则由引理 1.1
$$Q_{\mathcal V}(\lambda)\xi=\begin{pmatrix}-D_W^{\mathsf T}\xi\\ (\lambda I_d-T_W)\xi\end{pmatrix}=0,$$
故 $\operatorname{rank}Q_{\mathcal V}(\lambda)\le d-1$，与 $(5b)$ 矛盾。

**($\Leftarrow$)** 反之若 $\operatorname{rank}Q_{\mathcal V}(\lambda)\le d-1$ 对某个 $\lambda$ 成立，取 $0\ne\xi\in\ker Q_{\mathcal V}(\lambda)$；由引理 1.1 得 $D_W^{\mathsf T}\xi=0$ 与 $T_W\xi=\lambda\xi$。

于是：$(5b)$ $\iff$ 不存在"$\xi\ne0$ 是 $T_W$ 的特征向量且 $\xi\in\ker D_W^{\mathsf T}=\ker D_W$"。

**（PBH）** 对算子 $T_W$ 与观测矩阵 $D_W^{\mathsf T}$，"没有 $T_W$ 的特征向量落在 $\ker D_W^{\mathsf T}$ 里"等价于
$$\operatorname{rank}\Big[(D_W^{\mathsf T})^{\mathsf T}\ \big| \ (T_W^{\mathsf T})^0 (D_W^{\mathsf T})^{\mathsf T}\ \big|\cdots\Big]=d,$$
即 $\operatorname{rank}[D_W^{\mathsf T};D_W^{\mathsf T}T_W;\dots;D_W^{\mathsf T}T_W^{d-1}]=d$（标准 PBH / 可观测性秩判据，见 [docs/03](../../docs/03_theorems_cited.md)）。$\square$

**推论 2.2**（$c=1$ 的退化形式）当 $c=1$ 时 $D_W$ 是向量 $v_W=\pi_W(h_1A)$，判据退化为
$$\operatorname{rank}\big[v_W;\ v_WT_W;\ \dots;\ v_WT_W^{d-1}\big]=d,$$
即 "$v_W$ 是 $T_W$ 的循环向量"——这正是 [proof/cyclic_vector_criterion/](../cyclic_vector_criterion/README.md) 的判据（$c_0=1$、$r=1$ 时 $h_1=j_0$）。

**注 2.3**（与"可控"的区别）"$(T_W,D_W)$ 可控"是 $\operatorname{rank}[\lambda I-T_W\mid D_W]=d$，它是**对偶**条件；当 $T_W$ 非对称时与可观测性**不同**——c191 上实测 63/65，故旧交接文档里的"可控"表述是错的。

## 3. 用途

- 顶层判定变成**一个不含 $\lambda$ 的秩条件**：$\operatorname{rank}$ 一个 $(cd)\times d$ 有理矩阵，$O(d^3)$；
- 取代"子式 gcd"机制（后者仍适用于一般层，见 [proof/pencil_equivalence/](../pencil_equivalence/README.md)）；
- 与 [proof/rho0_layer/](../rho0_layer/README.md)（$\rho=0$ 层）、[proof/cyclic_vector_criterion/](../cyclic_vector_criterion/README.md)（$c_0=1$）共同覆盖三层。

## 4. 复核

| 项 | 脚本 | 结果 |
|---|---|---|
| 铅笔 vs $(5b)$ | `tools/certificates/c191_pbh.py` | 65/65 |
| 可观测 vs $(5b)$ | 同上 | 65/65 |
| 可控 vs $(5b)$ | 同上 | 63/65（**反例存在** ⟹ 旧表述被否）|

复核是验证（有限实例），不构成证明；证明在本文 §1–§2。
