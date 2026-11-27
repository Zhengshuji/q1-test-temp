> **更正（2026-11-08）**：本文件把 $H$ 当成 $\omega\times k$，实际是 $(\omega+1)\times k$；且只给了 $\alpha=0$ 分支。
> 正确的块形式、完整坏条件（含 $\alpha\ne0$ 仿射分支）见 [145](145_c2_good_locus_corrected.md)。
> 本文件的特征向量判据**对 $t=2$（$V$ 不变）是正确的**：此时 $P$ 在 $V$ 上为零，降为 $q\times\omega$ 块；
> 对 $t<2$ 才需要 145 的完整 $(x,\alpha)$ 系统。

# $c=2$ 的好性 locus：块约化与 $\ker B^{\mathsf T}$ 判据（部分）

> 2026-11-08。143 只给了**可容许**层的参数化；$q=\omega+1$ 可行还要**好性**。
> 本文件把好性化为一个显式的块判据，并给出 $c=2$ 的计算路线。
> 状态：**M2（部分）**；$(2a)$ 的非空性待算。

## 目标

设 $k=\omega+2$（$c=2$）、$H=L N_K$（$\omega\times k$，秩 $\omega$）、$H_A=L A N_K$、
$P(\lambda)=\lambda H-H_A$。对给定的 $V=\ker H\in\operatorname{Gr}(2,K_0)$（及提升 $L$），判定
$$\operatorname{rank}P(\lambda)<\omega\ \text{对某个}\ \lambda\in\mathbb C$$
是否成立（“坏”）；好 = 对所有 $\lambda$ 秩 $\omega$。

## 设想与理由

$H$ 行满秩，取右可逆 $S$ 使
$$HS=[I_\omega\mid 0].$$
记
$$H_A S=[A\mid B],\qquad A\in\mathbb C^{\omega\times\omega},\ B\in\mathbb C^{\omega\times2}.$$
则
$$P(\lambda)S=[\lambda I-A\mid -B].$$
$\operatorname{rank}[\lambda I-A\mid-B]<\omega$ $\iff$ 行线性相关
$\iff$ 存在 $0\ne x\in\mathbb C^\omega$（行向量）使
$$x^{\mathsf T}(\lambda I-A)=0,\qquad x^{\mathsf T}B=0,$$
即
$$\boxed{A^{\mathsf T}x=\lambda x,\qquad B^{\mathsf T}x=0.}$$
所以**坏** $\iff$ $\ker B^{\mathsf T}$（当 $\operatorname{rank}B=2$ 时维数 $\omega-2$）含有 $A^{\mathsf T}$ 的一个特征向量；
**好** $\iff$ $\ker B^{\mathsf T}$ 不含 $A^{\mathsf T}$ 的任何特征向量。

## 做法

1. 由 $V=\ker H$ 确定 $H$（差左 $\mathrm{GL}_\omega$）；由提升 $L$ 确定 $H_A$。
2. 取 $S$ 把 $H$ 化为 $[I\mid0]$，读出 $A,B$。
3. 好性判据：$\ker B^{\mathsf T}\cap\bigcup_\lambda E_\lambda(A^{\mathsf T})=\{0\}$，
   等价于对每个特征值 $\lambda$，$\ker B^{\mathsf T}\cap\ker(A^{\mathsf T}-\lambda I)=0$。
4. 对 $c=2$ 的各子型，把 $H,H_A$ 用 143 的参数（$V$ 与提升）写出，再判定上述交是否为零。

## 进展

* 块约化与好性判据已写出（**正确性**：$\operatorname{rank}PS=\operatorname{rank}P$，行相关即坏）。
* **提升依赖性**：$V=\ker H$ 只定 $H$ 到左 $\mathrm{GL}_\omega$；$H_A$ 随提升 $L$ 变。
  好性判据对左 $\mathrm{GL}_\omega$ 不变（$A\mapsto GAG^{-1}$、$B\mapsto GB$），但对提升敏感。
  因此 $(2a)$ 的可行性问题是：**在固定 $V$ 的提升族中，是否存在 $L$ 使 $\ker B^{\mathsf T}$ 不含 $A^{\mathsf T}$ 的特征向量**。
* $(2a)$ 的显式计算：$V=\ell_\lambda\oplus\ell_\mu$（$A$-不变）；提升 $L$ 的参数是仿射空间；
  $H_A$ 线性依赖于 $L$，故 $B^{\mathsf T}$ 与 $A^{\mathsf T}$ 线性依赖于提升参数；好性条件是一个
  “线性子空间不含特征向量”的开条件——可在提升参数空间上判定。

## 最终结论

* 好性 = $\ker B^{\mathsf T}$ 不含 $A^{\mathsf T}$ 的特征向量（显式块判据）。
* 对 $c=2$，可行性 = 在某层的参数空间上，存在提升使好性成立；$(2a)$ 化为提升仿射空间上的开条件。
* 这条路线与 143 的可容许参数化合并，就是完整的 $c=2$ 可行性判定。

## 放弃原因

* $(2a)$ 的提升参数化与“存在提升”的判定未完成（只给了判据与路线）。
* 未处理 $(2b)(2c)$ 与 $t=1$ 的提升依赖。

## 残留价值

* 把“好性”从抽象块判据化为 $\ker B^{\mathsf T}$ 与特征向量的交，可直接算法化。
* 指出提升依赖是 $c=2$ 可行性的核心难点（不是可容许层本身）。

## 相关文件

* [attempts/143](143_c2_rigorous_parameterization.md)（可容许层）
* [attempts/122](122_invariant_eigenspace_obstruction.md)（特征空间障碍）
* [lean/BlockIff](../../../../trash/lean_removed_2026-11-19/augmentation_lean/BlockIff.md)（块判据的 Lean 形式）
* [attempts/121](121_hyperplane_vector_bundle.md)（$c=1$ 的对照）

## 状态

* 块约化/好性判据：**[已证-纸面，M2]**。
* $(2a)$ 提升判定、其余子型：**[未做]**。
