# 16/21 对**所有** $q$ 不可行（项目约定下）

> 2026-11-08。把 165/172/182/183/184 的论证按 $c=k-\omega$ 统一，得到：
> seeds 16/21 在项目约定（$L=[L_0;R]$ 满行秩、$\operatorname{rank}[C;L]=p+q$）下**没有任何可行的 $q$**。
> 状态：**M2（纸面 + 精确计算）**；需注意与原始文献约定的差别。

## 目标

证明：对 seeds 16/21，任意 $q\ge1$ 都不可行。

## 设想与理由

$c=k-\omega$，$k=4$。按 $c$ 分四类：
- $c\ge3$：$V\subseteq W_L$，但 $\dim W_L=2$，不可能；
- $c=2$：$V=W_L$ 被迫，行空间判据给所有底部行 $b=0$；
- $c=1$：182 的超平面引理（非特征线）+ 183 的特征线检验；
- $c=0$：$\det P$ 非零多项式必有根。

## 做法

### $c\ge3$

$\dim V=c\ge3$，而 $V\subseteq W_L$、$\dim W_L=k-\operatorname{rank}[L_0N;L_0AN]=4-2=2$。矛盾。

### $c=2$（$\omega=2$）

$V=W_L$ 被迫（159/164）。$H$ 的每个底部行 $h_i=a_ih_0+b_iu_1$，可容许方程与 $q$ 无关；
两 seed 的行空间判据都给 $b_i$ 被强制为 0（165/172，$\alpha=(-1,0)$）。于是所有行 $\propto h_0$，
$\operatorname{rank}H=1<2=\omega$，矛盾。**对任意 $q$ 成立**（加行不改变每行的可容许方程）。

### $c=1$（$\omega=3$）

$V=L=\mathbb Cv\subseteq W_L$。两 seed 都有 $W_L\subseteq D=K_0\cap A^{-1}K_0$，故
$A_0\cdot v=L_0ANv=0$、$G_j\cdot v=RD_j\cdot(Av)=0$。可容许条件退化为
$$b\cdot\varphi(v)=0,\qquad \varphi_j(v)=u_j\cdot w,$$
其中 $w$ 是 $Av$ 的 $K_0$ 坐标，$u_j$ 是 $\operatorname{Ann}(L)/\langle h_0\rangle$ 的基。

- **非特征线**（$w\notin\operatorname{span}v$）：$\{h\in\operatorname{Ann}(L):h\cdot w=0\}$ 是 $\operatorname{Ann}(L)$ 的真超平面（$\omega-1=2$ 维）；
  $h_0$ 也在其中；$H$ 的所有行都落在这个 2 维空间里，$\operatorname{rank}H\le2<3$。
- **特征线**：183 在 21 的两条有理线、16 的两条复共轭线上算得 $\varphi\ne0$（秩 1），
  故 $b$ 落在复 1 维子空间，底部行加 $h_0$ 的秩 $\le2<3$。

所以 $c=1$ 对两 seed 不可行。**与 $q$ 无关**（论证只用 $V$ 与 $\operatorname{Ann}(L)$，不依赖行数）。

### $c=0$（$\omega=4=k$）

$H$ 满秩；$\det P(\lambda)$ 是次数 $k=4$ 的非零多项式，必有根，$(5b)$ 失败（184）。

## 结论

$$\boxed{\text{seeds 16/21 在项目约定下对任意 } q\ge1 \text{ 都不可行。}}$$

## 注意

* 项目约定含 $\operatorname{rank}[C;L]=p+q$（$C$ 与 $L$ 行独立）。原始文献的观测器问题可能**不要求**这一条；
  若去掉它，$c=2$ 的“$V=W_L$ 被迫”与行空间判据可能改变。
* **补充（186，专家 61 号后）**：本文件的不可行论证**只用压缩方程**（$V=W_L$ 由 $(5a)$ 与维数给出；
  $b$ 强制由 $H_A|_V=0$；$c=1$ 的超平面用 $l_i$ 的任意提升；$c=0$ 的行列式）——**都不依赖**
  $\operatorname{rank}[C;L]=p+q$。因此只要“不存在压缩对”，$\mathsf P_{\rm ind}$ 与 $\mathsf P_{\rm full}$
  （只要求 $L$ 满行秩）**都不可行**。依赖约定的是提升层，而无压缩对时提升层无关紧要。
  所以本结论很可能对两个问题都成立；最终措辞仍按专家要求分 $\mathsf P_{\rm ind}/\mathsf P_{\rm full}$。

## 进展

* 按 $c$ 四类的统一论证完成；
* 16/21 的 $q_{\min}$ 不存在（项目约定下）；
* 与 184 的 $q_{\min}\ge5$ 一致并加强。

## 最终结论

* 16/21 是项目约定下的**不可行实例**（任意 $q$）；
* 这解释了之前所有层搜索的 `none`；
* 需与专家确认原始约定是否含 $\operatorname{rank}[C;L]=p+q$。

## 放弃原因

* 未检查去掉 $\operatorname{rank}[C;L]=p+q$ 后的情形；
* 未把 $c=1$ 的 $\varphi\ne0$ 推广到一般 $\omega$（当前只 $\omega=3$，够用）；
* 未 Lean 化。

## 残留价值

* 两个实例的完整不可行性；
* 按 $c$ 分类的统一论证模板。

## 相关文件

* [attempts/165](165_c2_forced_plane_criterion.md)
* [attempts/182](182_c1_infeasibility_lemma.md)、[183](183_c1_eigenlines.md)
* [attempts/184](184_q4_excluded.md)

## 状态

* 不可行性：**[已证-纸面 + 精确计算，M2]**（项目约定）。
* 原始约定：**[待确认]**。
