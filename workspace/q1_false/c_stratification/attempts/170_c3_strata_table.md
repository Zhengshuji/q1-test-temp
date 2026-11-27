# $c=3$ 的十一层精确清单（Deliverable 3）

> 2026-11-08。按专家 59 号要求的格式，把 146 的 $c=3$ 分层整理成一张表：
> 每层的定义条件、$(t,u)$、Jordan/结构数据、参数空间、非空条件、不可约性。
> 状态：**M2（纸面）**；可随下一封送审件提交。

## 目标

给出 $c=3$ 的**穷尽、互斥**的十一层清单，供专家审计 $c=3$ 的分量界（159）与参数化（146）。

## 记号

$K_0=\ker[C;CA]$，$\dim K_0=k\ge3$；$V\in\operatorname{Gr}(3,K_0)$，$W=V\cap A^{-1}V$，$t=\dim W$，
$U=W+A(W)$，$u=\dim U$；$D=K_0\cap A^{-1}K_0$；$E_\lambda=\ker(A-\lambda I)$；
$T_\lambda=A-\lambda I$。

## 设想与理由

专家 59 号要求“精确清单”才能审计 $c=3$：每层要有定义、$(t,u)$、Jordan 数据、参数空间、非空条件、互斥与穷尽。
146 已有这些内容但分散在文字里；本文件把它们压成一张表，并补上逐层的不可约性指针（169/158/160）。

## 做法：十一层

| # | 层 | $t$ | $u$ | 结构/Jordan 数据 | 参数空间 | 非空条件 | 不可约性 |
|---|---|---|---|---|---|---|---|
| 1 | (3a) | 3 | 3 | 三个不同特征值 $\lambda,\mu,\nu$：$V=\ell_\lambda\oplus\ell_\mu\oplus\ell_\nu$ | $\mathbb P(E_\lambda\cap K_0)\times\mathbb P(E_\mu\cap K_0)\times\mathbb P(E_\nu\cap K_0)/S_3$ | 三个交非零 | 不可约（积/有限群商）|
| 2 | (3b) | 3 | 3 | 单特征值，$1+1+1$：$V\subseteq E_\lambda\cap K_0$ | $\operatorname{Gr}(3,E_\lambda\cap K_0)$ | $\dim(E_\lambda\cap K_0)\ge3$ | 不可约（Grassmannian）|
| 3 | (3b′) | 3 | 3 | $\lambda$ 的 $1+1$ + $\mu\ne\lambda$ 的 $1$：$V=U_\lambda\oplus\ell_\mu$ | $\operatorname{Gr}(2,E_\lambda\cap K_0)\times\mathbb P(E_\mu\cap K_0)$ | $\dim(E_\lambda\cap K_0)\ge2$、$E_\mu\cap K_0\ne0$ | 不可约 |
| 4 | (3c) | 3 | 3 | 单特征值，$2+1$：$V=\langle u,T_\lambda u\rangle\oplus\ell_\lambda$，$T_\lambda^2u=0$、$T_\lambda u\ne0$，$\ell_\lambda$ 与链空间独立 | 底：$\{\ell\subseteq E_\lambda\cap K_0:\ell\subseteq T_\lambda(K_0)\}$（射影线性子空间）；纤维：仿射（模 $E_\lambda\cap K_0$）| 链可提升且 $\dim(E_\lambda\cap K_0)\ge1$ | 不可约或空（169）|
| 5 | (3c′) | 3 | 3 | $\lambda$ 的 $2$ + $\mu\ne\lambda$ 的 $1$ | (3c) 的参数 $\times\mathbb P(E_\mu\cap K_0)$ | 两者非空 | 不可约或空 |
| 6 | (3d) | 3 | 3 | 单特征值，$3$：$V=\langle u,T_\lambda u,T_\lambda^2u\rangle$，$T_\lambda^3u=0$、$T_\lambda^2u\ne0$ | 底：$\{\ell_2\subseteq E_\lambda\cap K_0:\ell_2\subseteq T_\lambda(K_0),\ \ell_1\subseteq T_\lambda^2(K_0)\}$；纤维：仿射（两步提升）| 3-链可提升 | 不可约或空（169）|
| 7 | (2a) | 2 | 3 | $U=W+A(W)$、$\dim U=3$、$\dim(U\cap A^{-1}U)=2$（等价 $\operatorname{rank}\varphi_U=1$）；$V=U$ | $W$ 的 2 维型 $\times\{b\}$（$b$ 为 $A(W)$ 模 $W$ 的生成元）| $\exists W$，$Ab\notin W+A(W)$（与 $b$ 选取无关）| 积空间的开子集，不可约（158 的开性）|
| 8 | (2b) | 2 | 2 | $A(W)\subseteq W$（$W$ 不变 2 维）；$V=W\oplus\langle x\rangle$ | $W$ 的不变 2 维型 $\times\{x\in K_0/W\}$ | $Ax\notin W+\langle x\rangle$ | 底不可约、$x$ 开，不可约 |
| 9 | (1a) | 1 | 1 | $AL\subseteq L$（$U=L$）；$V=L\oplus U'$，$U'$ 为 $K_0/L$ 的 2-平面 | 不变线 $L$（按 $\lambda$）$\times$ $\operatorname{Gr}(2,K_0/L)$ 的开子集 | $U'\cap\bar A^{-1}U'=0$ | 每 $\lambda$ 一块，不可约 |
| 10 | (1b) | 1 | 2 | $AL\not\subseteq L$（$U=L+AL$）；$V=U\oplus\langle x\rangle$ | $(L,x)$，$L$ 满足 $AL\not\subseteq L$ | $\operatorname{rank}\Phi_V=2$、$\ker\Phi_V=L$（$Ax,A^2L$ 模 $V$ 独立）| 开子集，不可约 |
| 11 | (0) | 0 | 0 | $V\cap A^{-1}V=0$ | $\operatorname{Gr}(3,K_0)$ | $\operatorname{rank}\Phi_V=3$（开）| 开子集，不可约 |

**注**：(2a) 的 $u=3$ 在本分层中自动满足（$U\subseteq V$、$\dim V=3$，158 的维度引理），
所以 $S_{2,3}$ 是开子集。

## 互斥与穷尽

* $t=\dim W\in\{0,1,2,3\}$，穷尽且互斥；
* $t=3$：$V$ 不变，按 $A|_V$ 的 $3\times3$ Jordan 型分六种——(3a)(3b)(3b′)(3c)(3c′)(3d)，
  即按“不同特征值个数 + 各特征值的分拆”，穷尽且互斥；
* $t=2$：$W\subset V$ 2 维，$V=W+\langle x\rangle$；$U=W+A(W)$ 的维数只能是 2 或 3，
  分别给 (2b)(2a)，穷尽且互斥；
* $t=1$：$W=L$ 线，$AL\subseteq V$；按 $AL\subseteq L$ 与否分 (1a)(1b)，
  穷尽（$AL\not\subseteq L$ 时 $AL$ 与 $L$ 独立，$U=L+AL$）且互斥；
* $t=0$：单层。

**穷尽性证明**：任取 $V\in\operatorname{Gr}(3,K_0)$，令 $t=\dim(V\cap A^{-1}V)$；$t\in\{0,1,2,3\}$ 自动。
$t=3$ 即 $V\subseteq A^{-1}V$，即 $A(V)\subseteq V$，Jordan 型只有六种。
$t=2$：$W=V\cap A^{-1}V$ 2 维，取 $x\in V\setminus W$，则 $V=W+\langle x\rangle$；
$U=W+A(W)\subseteq V$ 且 $W\subseteq U$，故 $\dim U\in\{2,3\}$。
$t=1$：$W=L$ 线，$AL\subseteq V=V$ 的 3 维空间；若 $AL\subseteq L$ 为 (1a)，否则 $AL$ 与 $L$ 独立，
$U=L+AL$ 2 维，为 (1b)。
$t=0$：$V\cap A^{-1}V=0$，单层。$\square$

> **专家 60 号修正（2026-11-08）**：
> (3c)(3c′) 需补 $T_\lambda^2u=0$、$T_\lambda u\ne0$；(3d) 需补 $T_\lambda^3u=0$、$T_\lambda^2u\ne0$；
> (2a) 仅 $\dim U=3$ 不够，需 $\dim(U\cap A^{-1}U)=2$（等价 $\operatorname{rank}\varphi_U=1$），
> 它是 $B_{3,2}$ 的开子集，**不自动不可约**；(1b) 的底也是秩层，同样不自动不可约。
> 非不变层的分量数由 [171](171_Buv_rank_strata.md) 的 $b_{u,v}$ 界控制。

## 不可约性汇总

* (3a)(3b)(3b′)：(3a) 是射影空间积/有限群商，(3b)(3b′) 是 Grassmannian×射影空间积，均不可约；
* (3c)(3c′)(3d)：169 的循环向量参数化（单块/多块不变层），不可约或空；
* (2a)(2b)(1a)(1b)(0)：底空间不可约 + 纤维是开子集/仿射空间，不可约或空（158/160 的方法）。

## 进展

* 十一层的精确清单已按专家要求列成表（定义、$(t,u)$、Jordan 数据、参数空间、非空、不可约）；
* 互斥与穷尽给出证明；
* 不可约性逐层对应到 169/158/160。

## 最终结论

* $c=3$ 的十一层是 $\operatorname{Gr}(3,K_0)$ 的有限分层，穷尽、互斥；
* 不变层不可约或空（169，已按 60 号修正）；非不变层的底是秩层，**不自动不可约**，用 171 的 $b_{u,v}$ 界；
* 159 的界 $\binom{s}{3}+\binom{s}{2}+2s^2+4s+3$ 在基空间层面成立（提升纤维另计）。

## 放弃原因

* 未给每层的**精确非空判据**的算法实现；
* 未处理提升纤维的分量（专家提醒的三个空间不要混同）；
* 未 Lean 化。

## 残留价值

* 可直接提交给专家审计 $c=3$ 的清单；
* 作为一般 $c$ 分层表的模板。

## 相关文件

* [attempts/146](146_c3_rigorous_parameterization.md)（完整推导）
* [attempts/158](158_c3_s23_audit.md)（$S_{2,3}$ 开性）
* [attempts/159](159_c3_component_bound_corrected.md)（分量界）
* [attempts/169](169_invariant_strata_irreducibility.md)（不变层不可约性）

## 状态

* 清单/互斥穷尽：**[已证-纸面，M2]**。
* 精确非空判据/提升纤维/Lean：**[未做]**。
