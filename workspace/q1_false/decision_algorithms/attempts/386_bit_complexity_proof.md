# 386 位复杂度：固定 $p$、几何单谱时的多项式时间（七步路线的落实）

> 承接 384/385（105 号给了七步路线；$L_0$ 秩与满秩引理已解决）。
> 本文件把那七步写成可引用的引理与一条定理。

## 目标

给出 $\mathrm{DEC}_{c=1}$ 在固定 $p$、几何单谱下的**位复杂度**证明。

## 设想与理由

105 号的路线是：**所有中间量的高度都是 $\mathrm{poly}(n,\tau)$**，唯一的大因子是图卡变量数
$d\le p^2$（固定 $p$ 时为常数）。于是总代价 $\mathrm{poly}(n,\tau)$。

记输入的最大比特长为 $\tau$。

## 做法：六个引理 + 一条定理

### 引理 1（压缩高度）

> $K_0$ 的基 $N$ 与压缩 $M=(N^{\mathsf T}N)^{-1}N^{\mathsf T}AN$ 可在 $\mathrm{poly}(n,\tau)$ 位时间内算出，
> 且两者元素的比特长都是 $\mathrm{poly}(n,\tau)$。

*证明.* 把 $[C;CA]$ 清分母；对增广矩阵 $[A\mid I]$ 作**无分数**（Bareiss）消元得 $\ker$ 基，
再把基列清分母、取本原整数向量。子式的比特长由 **Hadamard 界**控制：$k\times k$ 子式
$\le(k^{1/2}2^\tau)^k$，故 $\log\le\frac{k}{2}\log k+k\tau$。$N^{\mathsf T}N$ 与 $N^{\mathsf T}AN$ 同样有界；
$M$ 是 $(N^{\mathsf T}N)^{-1}$ 乘上去，用伴随矩阵/无分数消元，其元素比特长仍 $\mathrm{poly}$。$\square$

### 引理 2（特征多项式高度）

> $\chi_M(t)=\det(tI-M)$ 清分母取本原部分后，系数比特长为 $\mathrm{poly}(n,\tau)$，且可在 $\mathrm{poly}$ 位时间内算出。

*证明.* 每个系数是主子式的和；由引理 1 与 Hadamard 界，主子式比特长 $\mathrm{poly}$。$\square$

### 引理 3（根高度与次数）

> $\chi_M$ 的任一复根 $\mu$ 满足 $[\mathbb Q(\mu):\mathbb Q]\le k\le n$ 且 $h(\mu)\le\mathrm{poly}(n,\tau)$；
> 其实嵌入可用精确实根隔离在 $\mathrm{poly}$ 位时间内求出。

*证明.* 次数 $\le\deg\chi_M\le k$；Cauchy 界 $|\mu|\le1+\max_i|a_i/a_k|$ 与引理 2 给 $h(\mu)=\mathrm{poly}$；
实根隔离的位复杂度是标准的（多项式）。$\square$

### 引理 4（特征向量与商丛基的高度）

> 在几何单谱假设下，$E_\mu$ 可由一个本原向量 $a$ 张成；其坐标（在 $K=\mathbb Q(\mu)$ 上）的比特长为 $\mathrm{poly}(n,\tau)$。
> 由 $a$ 出发的 $E_\mu^0$、$D_v$、$U_v^\perp$、$\mathcal Q_v/\overline V_{0,v}$ 的基同样如此。

*证明.* $a$ 是 $(M-\mu I)$ 的核，由 Cramer 法则/无分数消元给出，坐标是子式之比 ⟹ 比特长 $\mathrm{poly}$。
其余空间由核、像、和、商得到，维数 $\le n$，同理。**注意**：这些基必须在**同一个** $K$ 上算，不能退回 $\mathbb Q$。$\square$

### 引理 5（图卡规模）

> 图卡参数个数 $d_{\mathrm{chart}}=(s-\delta)(r(v)-s)\le p^2$；每个子式在 $X$ 与 $\lambda$ 上的次数都 $\le\omega\le n$；
> 子式个数为 $\binom{q}{\omega}\binom{k}{\omega}=k\binom{q}{s}=n^{O(p)}$；图卡数为 $\binom{r-\delta}{s-\delta}=O(1)^p$。

*证明.* $r(v)\le\rho\le2p$ 给 $d\le p^2/4$；次数由图卡行对 $X$ 线性、铅笔对 $\lambda$ 线性给出；
计数用 $q-\omega=s\le\rho+1\le2p+1$ 与 $\binom{k}{\omega}=k$。$\square$

### 引理 6（子结式 gcd）

> 在 $K(X)[\lambda]$ 上，全体子式的 gcd 可用**子结式 PRS**（无分数）在
> $$\mathrm{poly}\bigl(D,\;H\bigr),\qquad D=\omega\binom{d+\omega}{d}=n^{O(p^2)},\ H=\text{系数比特长}$$
> 内算出；答案的次数为正 $\iff$ 去掉内容后的 gcd 非常数。

*证明.* 子结式是 Sylvester 矩阵（$(2\omega)\times(2\omega)$）的行列式，元素是 $X$ 的多项式（次数 $\le\omega$、
系数在 $K$ 中、高度 $\mathrm{poly}$）；无分数计算避免分母爆炸。多多项式情形迭代取 gcd，
次数单调不增，故总代价 $\mathrm{poly}$。$\square$

### 定理（固定 $p$、几何单谱）

> 对固定的 $p$，在**几何单谱**（每个实特征值的特征空间一维）的输入上，超平面层的判定可在
> $$\mathrm{poly}(n,\tau)\quad(\text{具体 }n^{O(p^2)})$$
> 位时间内完成，用的都是精确算术。

*证明.* 依次执行：引理 1（压缩）、分解 $\chi_M$（LLL，poly）、隔离实根（引理 3）、
对每个实根取特征向量（引理 4）、构造图卡（引理 5）、算子结式 gcd（引理 6）。
每步是 $\mathrm{poly}$，且 \(\mathrm{rank}H\equiv\omega\) 保证"正次数 ⟹ 整图卡坏"（引理 8，385）。
块数 $\le k\cdot O(1)^p$，故总代价 $\mathrm{poly}(n,\tau)$。$\square$

## 进展

1. 七步全部落成可引用的引理，且都是**标准事实 + 本项目记号**的组合。
2. 唯一非平凡的是**引理 6**的"无分数"要求——朴素欧几里得会分母爆炸，必须用子结式。
3. 定理的指数是 $p^2$（来自图卡变量数），与 103 号 §8 的 $p^2$ 界一致。

## 最终结论

1. **固定 $p$、几何单谱 ⟹ 多项式位复杂度**（在本文件的形式下成立）。
2. 依赖的标准事实：整数多项式分解（LLL）、实根隔离、数域算术、子结式 PRS——都可以引用。
3. 若放开"几何单谱"，$d_{\mathrm{chart}}$ 上界不变但**底维**随 $n$ 增长 ⟹ 这条路线失效（384 已记）。

## 放弃原因

- 引理 6 只给了"$\mathrm{poly}(D,H)$"的形态，没有写出显式常数与位运算模型细节；
- 没有把无理特征值的实现补齐（定理允许，实现只到有理）；
- 没有处理"$\mathcal L$ 不要求行满秩"的变体。

## 残留价值

- **一条完整的、可写进论文的复杂度定理**（含六个引理）；
- 明确了唯一的技术要求（子结式而非朴素欧几里得）；
- 指数 $p^2$ 与既有文献的界一致。

## 相关文件

- [attempts/384](384_expert105_audit.md)（七步路线）
- [attempts/385](../../c_stratification/attempts/385_L0_rank_resolution.md)（前置检查 + 引理 8）
- [attempts/375](../../c_stratification/attempts/375_stage2_bit_complexity.md)（早期的记账版）
- [attempts/374](../../c_stratification/attempts/374_complete_parameterization.md)（参数化）

## 状态

- 定理（固定 $p$ + 几何单谱）：**[已证-纸面]**（依赖四条标准事实）。
- 无理特征值的实现：**[未做]**。
- 显式常数/位模型细节：**[未写]**。
