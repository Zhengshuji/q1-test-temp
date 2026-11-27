# $B_{u,v}$ 秩层：不可约性反例、二次 chart 与一致分量界（专家 60 号）

> 2026-11-08。专家 60 号对“非不变部分归约到
> $B_{u,v}=\{U\in\operatorname{Gr}(u,K_0):\dim(U\cap A^{-1}U)=v\}$”给出决定性答复：
> $B_{u,v}$ **不总是不可约**（有最简单的反例），但它是一个**秩层**，有**二次多项式 chart 描述**
> 与**一致（粗糙）分量界**。本文件把该结果写全，并给出一般 $c$ 的界。状态：**M2（纸面）**。

## 目标

1. 证明 $B_{u,v}$ 不总不可约（反例）；
2. 给出 $B_{u,v}$ 作为丛映射秩层的描述与二次 chart 公式；
3. 由仿射 Bézout 给出分量上界 $b_{u,v}$；
4. 写出一般 $c$ 的分量界（不变部分 + 非不变部分）。

## 设想与理由

$B_{u,v}$ 是“$U\mapsto U\cap A^{-1}U$ 的秩层”。它不是单个确定性子簇，而是**射影丛的秩层**；
秩层一般不不可约（如 $A=\operatorname{diag}(0,1)$ 的 $B_{1,1}$ 是两个点）。但它有统一的坐标描述：
在每个标准仿射 chart 上，它是一个**二次多项式矩阵**的秩层，于是仿射 Bézout 给出一致上界。

## 做法

### 1. 丛映射描述

$K=K_0\subseteq\mathbb C^n=\mathcal X$，$G=\operatorname{Gr}(u,K)$，$\mathcal S$ 为 tautological 秩 $u$ 子丛：
$$\varphi:\mathcal S\longrightarrow(\mathcal X\otimes\mathcal O_G)/\mathcal S,\qquad \varphi_U(x)=Ax+U.$$
则
$$\ker\varphi_U=\{x\in U:Ax\in U\}=U\cap A^{-1}U,\qquad \operatorname{rank}\varphi_U=u-\dim(U\cap A^{-1}U)=u-v.$$
故
$$B_{u,v}=\{U\in G:\operatorname{rank}\varphi_U=u-v\}=D_{u-v}\setminus D_{u-v-1},\qquad D_r=\{U:\operatorname{rank}\varphi_U\le r\}.$$
$B_{u,v}$ 局部闭，是**秩层**（不是确定性子簇）。

### 2. 不总不可约：反例

$K=\mathcal X=\mathbb C^2$、$A=\operatorname{diag}(0,1)$、$u=1$、$v=1$：
$$B_{1,1}=\{U:\ AU\subseteq U\}=\{[e_1],[e_2]\}\subset\mathbb P^1,$$
两个点，**可约**。更一般地，$u=1,v=1$ 时 $B_{1,1}$ 是 $A$ 在 $K_0$ 中的各特征子空间的并，
不同特征值给不同分量。所以“所有 $B_{u,v}$ 不可约”是**假**的。

### 3. 二次 chart

取 $K=E\oplus F$（$\dim E=u$、$\dim F=k-u$），chart 上 $U=\operatorname{graph}X$，基
$$G(X)=\begin{bmatrix}I\\X\\0\end{bmatrix},\qquad X\in\mathbb C^{(k-u)\times u}.$$
把 $A$ 按 $\mathcal X=E\oplus F\oplus K'$ 分块。$\mathcal X/U$ 的坐标是 $(y_F-Xy_E,\ y_{K'})$。于是
$$\boxed{F_A(X)=\begin{bmatrix}A_{21}+A_{22}X-XA_{11}-XA_{12}X\\ A_{31}+A_{32}X\end{bmatrix}}$$
是 $(n-u)\times u$ 矩阵，元素是 $X$ 的**次数 $\le2$** 的多项式，且
$$\boxed{\operatorname{rank}F_A(X)=u-\dim(U\cap A^{-1}U)=u-v.}$$
所以 $B_{u,v}$ 在每个 chart 上是**二次矩阵的精确秩层**。

### 4. 一致分量界

令 $r=u-v$、$m=u(k-u)$。若 $0\le r<\min(u,n-u)$，则 $D_r$ 在每个 chart 上由 $(r+1)$ 阶子式
（次数 $\le d=2(r+1)$）定义；仿射 Bézout 给该 chart 上至多 $d^m$ 个不可约分量。共有
$\binom{k}{u}$ 个标准 chart，每个整体分量至少与一个 chart 相交，故
$$\boxed{b_{u,v}:=\#\operatorname{Irr}(B_{u,v})\le\binom{k}{u}\big(2(u-v+1)\big)^{u(k-u)}.}$$
若 $r=\min(u,n-u)$（满秩），$B_{u,v}$ 是开集，不可约或空；若 $r>\min(u,n-u)$，空。

### 5. 一般 $c$ 的界

不变部分（169，修正后）+ 非不变部分（专家给出的 incidence 论证）：
$$\boxed{N(c)\le\sum_{\lambda\vdash c}s^{b(\lambda)}
+\sum_{t=0}^{c-1}\sum_{u=t}^{\min(2t,c)}\sum_{v=t}^{u}b_{u,v}.}$$
代入 Bézout 界：
$$N(c)\le\sum_{\lambda\vdash c}s^{b(\lambda)}
+\sum_{t=0}^{c-1}\sum_{u=t}^{\min(2t,c)}\sum_{v=t}^{u}\binom{k}{u}\big(2(u-v+1)\big)^{u(k-u)}.$$

**注意**：这是**压缩几何层**的界；实际 $L$ 的提升还要另加（专家 60 号 §5 的提醒）。

## 精确验证（2026-11-08）

`python tools/verification/buv_chart_check.py` 在 5 组 $(n,k,u)$（共 100 个随机有理 chart）上核对
$$\operatorname{rank}F_A(X)=u-\dim(U\cap A^{-1}U):$$
```
PASS: rank F_A(X) = u - dim(U cap A^-1 U) on 100 random exact charts
```
（验证的是 chart 恒等式本身，不是 Bézout 界；Bézout 界仍为引用。）

## 进展

* $B_{u,v}$ 的不可约性被反例否定；
* 二次 chart 公式与 Bézout 分量界已写出；
* 一般 $c$ 的界有了明确形状（不变 + 非不变）。

## 最终结论

* $B_{u,v}$ 一般不不可约；但它是秩层，有统一的分量界
  $\binom{k}{u}(2(u-v+1))^{u(k-u)}$；
* 一般 $c$ 的界 = 不变部分 $\sum s^{b(\lambda)}$ + 非不变部分 $\sum b_{u,v}$；
* 这是**压缩层**的界，提升层另算。

## 放弃原因

* 未把 Bézout 界形式化（专家建议可引用标准定理）；
* 未把 incidence → $V$ 的纤维论证写全（专家 §5 的 relative Grassmannian 构造）；
* 未处理提升层。

## 残留价值

* 一般 $c$ 分量界的一个**可写进论文**的形状；
* 二次 chart 公式是可精确验证的（可写 `verify` 脚本）。

## 相关文件

* [attempts/161](161_general_c_invariant_and_rank_strata.md)（$B_{u,v}$ 归约）
* [attempts/169](169_invariant_strata_irreducibility.md)（不变部分，需修正）
* [attempts/164](164_59_verdict_implementation.md)（专家 59 号）

## 状态

* 反例/chart/界：**[已证-纸面，M2]**（Bézout 引用）。
* 提升层：**[未做]**。
