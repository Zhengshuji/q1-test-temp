# $S=\mathcal J$ 闭包族：完整证明

> 对应 [docs/02](../../docs/02_theorems_proven.md) 的 C.1。本文是**展开版**。
> 数值复核：[tools/certificates/c190_invariant_family.py](../../tools/certificates/c190_invariant_family.py)（$8/8$ 实例 $q_{\min}=n$）。

## 1. 陈述

设 $\operatorname{row}(L_0)=\mathcal J$ 且 $\langle\mathcal J\rangle_A=\mathbb C^n$（$\mathcal J$ 的 $A$-闭包是整个空间）。则**任何**可行解都必须等于 $\mathbb C^n$。于是

$$\boxed{\ q_{\min}=\begin{cases} n, & \mathcal V=\mathbb C^n\ \text{可行},\\ \text{无解}\ (\text{不可行}), & \text{否则}.\end{cases}}$$

## 2. 证明

**引理 2.1** 若 $S=\operatorname{row}L_0=\mathcal J$，则任何可行解 $\mathcal V=\operatorname{row}\mathcal L$ 满足：$\mathcal V$ 是 $A$-不变的，且 $\mathcal V\supseteq\mathcal J$。

*证明*：$S\subseteq\mathcal V$ 给出 $\mathcal J\subseteq\mathcal V$。由 $(5a)$ 的行空间形式（[proof/lower_bound/theorem.md](../lower_bound/theorem.md) 引理 1.1）：$\mathcal V A\subseteq\mathcal V+\mathcal J$；而 $\mathcal J\subseteq\mathcal V$ 故 $\mathcal V+\mathcal J=\mathcal V$，于是 $\mathcal V A\subseteq\mathcal V$，即 $\mathcal V$ 是 $A$-不变的。$\square$

**推论 2.2** 若还有 $\langle\mathcal J\rangle_A=\mathbb C^n$，则 $\mathcal V\supseteq\langle\mathcal J\rangle_A=\mathbb C^n$，即 $\mathcal V=\mathbb C^n$。

*证明*：由引理 2.1，$\mathcal V$ 是 $A$-不变子空间且包含 $\mathcal J$；含 $\mathcal J$ 的 $A$-不变子空间必含 $\langle\mathcal J\rangle_A$（按定义，后者是含 $\mathcal J$ 的最小 $A$-不变子空间）。$\square$

**引理 2.3** $\mathcal V=\mathbb C^n$ 满足 $(5a)$；它满足 $(5b)$ $\iff$ $A^{\mathsf T}$ 没有落在 $K=\ker[C;CA]$ 里的特征向量。

*证明*：$\mathcal L$ 是 $n\times n$ 可逆矩阵（$\mathcal V=\mathbb C^n$、行满秩）。
$(5a)$：$\operatorname{rank}[\mathcal LA;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C]=n$，两端都是 $n$（都含 $n$ 个线性无关行）$\square$。

$(5b)$：由 $\mathcal L$ 可逆，$\operatorname{row}(\lambda\mathcal L-\mathcal LA)=\operatorname{row}(\mathcal L(\lambda I-A))=\operatorname{row}(\lambda I-A)$。故
$$(5b)\iff \operatorname{row}(\lambda I-A)+\mathcal J=\mathbb C^n\quad\forall\lambda\in\mathbb C .$$
对给定 $\lambda$，$\operatorname{row}(\lambda I-A)+\mathcal J\ne\mathbb C^n$ $\iff$ 存在 $0\ne\xi\in\mathbb C^n$ 使
$$\xi^{\mathsf T}(\lambda I-A)=0\ \text{且}\ \xi^{\mathsf T}\mathcal J=0,$$
即 $\xi$ 是 $A^{\mathsf T}$ 的特征向量且 $\xi\in\mathcal J^\perp=K$（$\mathcal J^\perp=\ker[C;CA]$）。$\square$

## 3. 结论（C.1）

由推论 2.2，唯一候选是 $\mathcal V=\mathbb C^n$；由引理 2.3，它的可行性有明确判据。故
$$q_{\min}=n\ \text{或}\ \text{无解},$$
且当引理 2.3 的条件满足时 $q_{\min}=n$。$\square$

## 4. 用途：为什么这个族能杀死闭式

在这个族里（$S=\mathcal J$、$\langle\mathcal J\rangle_A=\mathbb C^n$）：

| 量 | 值 |
|---|---|
| $r=\dim S$ | $j$ |
| $c_0=\dim(S\cap\mathcal J)$ | $j$ |
| $d=n-j$ | $n-j$ |
| $\dim V=\dim\langle S\rangle_{A'}$ | $n$ |
| $\rho^*=\dim\pi(\mathcal V)$ | $d=n-j$ |
| $q_{\min}$ | $n=j+d$ |

故：
- $\dim V+1=n+1>q_{\min}$ ⟹ **R1 死**；
- $\max(r,\rho^*+1)=\max(j,d+1)<n=j+d$（当 $j\ge1,d\ge1$）⟹ **R3 死**；
- 但 $\max(r+\varepsilon,\rho^*+\max(c_0,1))=\max(j+\varepsilon,\ d+j)=n$ ⟹ **R4（$F_3$）在这个族上不被推翻**，它需要另一族反例（[proof/refuted/](../refuted/README.md) R4）。

## 5. 复核

| 项 | 脚本 | 结果 |
|---|---|---|
| 该族 $q_{\min}=n$ | `python tools/certificates/c190_invariant_family.py` | $8/8$ |
| C.1 的可行性判据（引理 2.3） | `python proof/top_layer_observability/verify.py` | $12/12$（B.4 即本引理）|
