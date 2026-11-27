# $c=3$ 严格参数化：精确参数空间、互斥穷尽、非空条件

> 2026-11-08。把 137 的 $c=3$ 结构分解补成与 143 同标准的精确参数化：
> 每层的底空间、纤维、非空条件、互斥/穷尽。状态：**M2（纸面）**。
> 好性（可行性）与 143/145 一样是独立的一半，本文件只做可容许层。

## 目标

对 $c=3$、$V\in\operatorname{Gr}(3,K_0)$、$W=V\cap A^{-1}V$、$t=\dim W\in\{0,1,2,3\}$，给出：

1. 每层的**精确参数空间**（底 + 纤维）；
2. **互斥与穷尽**；
3. **可容许非空条件**。

## 设想与理由

* 135 的精确纤维：$\mathcal F_W=\{V\supseteq U:\operatorname{rank}\Phi_V=3-t\}$，$\Phi_V:V\to\mathcal X/V$；
* $t=3$：$V$ 是 $A$-不变 3-平面，按 $A|_V$ 的 Jordan 型分类；
* $t=2$：$\dim U\in\{2,3\}$；$\dim U=3$ 时 $V=U$，$\dim U=2$ 时 $A(W)\subseteq W$、$V=W+\langle x\rangle$；
* $t=1$：$AL\subseteq L$ 或不是；前者 $V=L+U'$（$U'$ 是 $K_0/L$ 中的 2-平面），后者 $V=U+\langle x\rangle$；
* $t=0$：开条件 $\operatorname{rank}\Phi_V=3$。

## 做法

### $t=3$：$A(V)\subseteq V$（六种 Jordan 型）

$A|_V$ 是 $V$ 上的自同态。按 Jordan 型（$\dim 3$）：

**(3a) 三个不同特征值** $\lambda,\mu,\nu$：
$$V=\ell_\lambda\oplus\ell_\mu\oplus\ell_\nu,\qquad \ell_\star\subseteq E_\star\cap K_0;$$
参数
$$\big(\mathbb P(E_\lambda\cap K_0)\times\mathbb P(E_\mu\cap K_0)\times\mathbb P(E_\nu\cap K_0)\big)/S_3;$$
非空 $\iff$ 三个交都非零。

**(3b) 单特征值、$1+1+1$**：$V\subseteq E_\lambda\cap K_0$；参数 $\operatorname{Gr}(3,E_\lambda\cap K_0)$；非空 $\iff\dim\ge3$。

**(3b′) $\lambda$ 的 $1+1$ 与 $\mu\ne\lambda$ 的 $1$**：
$$V=U_\lambda\oplus\ell_\mu,\quad U_\lambda\in\operatorname{Gr}(2,E_\lambda\cap K_0),\ \ell_\mu\subseteq E_\mu\cap K_0;$$
参数 $\operatorname{Gr}(2,E_\lambda\cap K_0)\times\mathbb P(E_\mu\cap K_0)$；非空 $\iff\dim(E_\lambda\cap K_0)\ge2$、$E_\mu\cap K_0\ne0$。

**(3c) 单特征值、$2+1$**：$V=\operatorname{span}\{u,T_\lambda u\}\oplus\ell_\lambda$，
$(A-\lambda I)u=T_\lambda u$、$(A-\lambda I)T_\lambda u=0$、$T_\lambda u\ne0$，且链线
$\ell=\mathbb C T_\lambda u\subseteq(A-\lambda I)(K_0)$（链提升）；纤维：仿射，$\dim=\dim(E_\lambda\cap K_0)-1$；
非空 $\iff$ 链可提升且 $\dim(E_\lambda\cap K_0)\ge1$。

**(3c′) $\lambda$ 的 $2$ 与 $\mu\ne\lambda$ 的 $1$**：链（2 维）$\oplus$ 特征线 $\ell_\mu$；
参数 = (3c) 的链参数 $\times$ $\mathbb P(E_\mu\cap K_0)$；非空 = 两者非空。

**(3d) 单特征值、$3$**：$V=\operatorname{span}\{u,T_\lambda u,T_\lambda^2u\}$，
$(A-\lambda I)u=T_\lambda u$、$(A-\lambda I)T_\lambda u=T_\lambda^2u$、$(A-\lambda I)T_\lambda^2u=0$，
$T_\lambda^2u\ne0$；链提升条件
$$\mathbb C T_\lambda^2u\subseteq(A-\lambda I)(K_0),\qquad \mathbb C T_\lambda u\subseteq(A-\lambda I)^2(K_0);$$
纤维：仿射（模 $E_\lambda\cap K_0$）；非空 $\iff$ 3-链可提升。

**互斥穷尽**：$\dim 3$ 的 Jordan 型只有上述（按“不同特征值个数 + 各特征值的分拆”），互斥；$t=3$ 即 $V$ 不变。

### $t=2$：$\dim W=2$

**(2a) $\dim U=3$**：$V=U=W+A(W)$；精确条件 $\operatorname{rank}\Phi_V=1$，
等价于 $Ab\notin V$（$b$ 为 $A(W)$ 模 $W$ 的生成元；结果与 $b$ 的选取无关，专家 56 号 §1.3）。
参数：$W$ 的 2-维型（同 $c=2$ 的 $t=2$ 三子型）$\times$ $\{b\}$（$b$ 为 $A(W)$ 模 $W$ 的生成元）；
非空 $\iff$ 存在 $W$ 使 $Ab\notin W+A(W)$（与 $b$ 的选取无关，因为换 $b\mapsto b+w$ 只改 $Ab$ 一个 $W$-分量）。

**(2b) $\dim U=2$**：$A(W)\subseteq W$（$W$ 不变）；$V=W\oplus\langle x\rangle$，精确条件
$$Ax\notin W+\langle x\rangle.$$
参数：$W$ 的不变 2-维型 $\times$ $\{x\in K_0/W\}$；非空 $\iff$ 存在这样的 $x$。

### $t=1$：$W=L=\mathbb Cv$

**(1a) $AL\subseteq L$**：$U=L$；$V=L\oplus U'$，$U'$ 是 $K_0/L$ 中的 2-平面；精确条件
$$U'\cap\bar A^{-1}U'=0\quad\text{（在 }\mathcal X/L\text{ 中）},$$
即 $\operatorname{rank}\Phi_V=2$。参数：$A$-不变线 $L$ $\times$ $\operatorname{Gr}(2,K_0/L)$ 中的开子集；非空 $\iff$ 存在 $U'$。

**(1b) $AL\not\subseteq L$**：$U=L+AL$（2 维）；$V=U\oplus\langle x\rangle$；精确条件
$$\operatorname{rank}\Phi_V=2,\qquad \ker\Phi_V=L,$$
精确条件是
$$Ax+V,\quad A^2L+V\ \text{在}\ \mathcal X/V\ \text{中线性独立}$$
（$V/L$ 的基取 $\bar x,\overline{AL}$；$\Phi_V$ 在其上的像就是这两条）。等价地：
$Ax\notin V$、$A(AL)\notin V$，且两者模 $V$ 独立。
参数：$(L,x)$；非空 $\iff$ 存在这样的 $x$。

### $t=0$：$W=0$

$V\in\operatorname{Gr}(3,K_0)$ 满足 $\operatorname{rank}\Phi_V=3$（即 $V\cap A^{-1}V=0$），开子集；非空 $\iff$ 存在这样的 $V$。

## 互斥与穷尽（总）

* $t=\dim W\in\{0,1,2,3\}$，穷尽且互斥；
* $t=3$ 按 $A|_V$ 的 Jordan 型分 (3a)(3b)(3b′)(3c)(3c′)(3d)，穷尽且互斥；
* $t=2$ 按 $\dim U\in\{2,3\}$ 分 (2a)(2b)，穷尽且互斥；
* $t=1$ 按 $AL\subseteq L$ 与否分 (1a)(1b)，穷尽且互斥；
* $t=0$ 单层。
故 $c=3$ 的层构成 $\operatorname{Gr}(3,K_0)$ 的有限分层，每层是底空间上的（开）纤维丛。

## 可容许非空条件汇总

| $t$ | 子型 | 条件 |
|---|---|---|
| 3 | (3a) | 三个交非零 |
| 3 | (3b) | $\dim(E_\lambda\cap K_0)\ge3$ |
| 3 | (3b′) | $\dim(E_\lambda\cap K_0)\ge2$、$E_\mu\cap K_0\ne0$ |
| 3 | (3c)/(3c′) | 链可提升（$\ell\subseteq(A-\lambda I)(K_0)$）+ 其余因子非空 |
| 3 | (3d) | 3-链可提升 |
| 2 | (2a) | $\exists W$，$Ab\notin W+A(W)$ |
| 2 | (2b) | $\exists W$ 不变、$x$，$Ax\notin W+\langle x\rangle$ |
| 1 | (1a) | $\exists L$ 不变、$U'$，$U'\cap\bar A^{-1}U'=0$ |
| 1 | (1b) | $\exists L,x$，$Ax\notin U+\langle x\rangle$（且 $AL\not\subseteq L$）|
| 0 | 开 | $\exists V$，$V\cap A^{-1}V=0$ |

## 进展

* 十一个层的精确参数空间、互斥穷尽、可容许非空条件已写出。
* 与 137 的秩条件一致；新增 (3b′)(3c′) 的显式参数化与 (3d) 的双重链提升条件。
* **注意**：与 143 一样，这里只做**可容许层**；$q=\omega+3$ 的可行性还要好性（块判据）。

## 最终结论

* $c=3$ 的可容许层是 $\operatorname{Gr}(3,K_0)$ 的有限分层，每层参数空间精确；
* 非空性化为线性代数条件（特征空间、链提升、秩条件）；
* 这是与 143（$c=2$）同标准的 $c=3$ 严格参数化。

## 放弃原因

* 好性（可行性）未做；
* 各层不可约性/分量数未证；
* 实点未做；算法未实现。

## 残留价值

* 可直接用于 $c=3$ 的算法与分量研究；
* 补齐了专家 56 号所说“$c=3$ 仍是结构描述”的参数空间缺口。

## 相关文件

* [attempts/137](137_c3_repair.md)（$c=3$ 结构重写）
* [attempts/143](143_c2_rigorous_parameterization.md)（$c=2$ 严格参数化，模板）
* [attempts/145](145_c2_good_locus_corrected.md)（好性判据）

## 状态

* 参数化/互斥穷尽/可容许非空：**[已证-纸面，M2]**。
* 好性/不可约性/实点/算法：**[未做]**。
