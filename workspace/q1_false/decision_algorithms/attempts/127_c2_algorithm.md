# $c=2$ 的判定算法：用 125/126 的分量表 + 每分量随机点

> 2026-11-08。把 125（分量分类）、126（非空条件）、123（每分量随机点 + gcd）拼成
> $c=k-\omega=2$ 的端到端一侧算法。状态：**M2（算法 + 概率界）**。

## 目标

给定 $(A,C,L_0)$、$q=\omega+2$、$k=\omega+2$（$c=2$），判定是否存在好的满行秩 $R$。

## 设想与理由

* 125：$\mathcal D_2$（点 / $\operatorname{Gr}(2,E_\lambda)$ / $J_\lambda$）、$\mathcal D_3$（每特征值一个投影丛）、
  $\mathcal D_4$（开）——分量数 $\le\binom{s}{2}+3s+1$，只依赖谱。
* 126：每个分量的非空条件都是线性代数的（$m_0$、$e_\lambda$、$T_\lambda$），可先筛掉空分量。
* 113：每分量上坏集闭；全坏则任何点坏，有好开集则随机点以概率 1 落进去。
* 所以：**每个非空分量取一个随机点 + gcd**，与 123 同型。

## 做法

**算法（固定 $q=\omega+2$、$k=\omega+2$）**：

1. 算 $K,N,K_0$、$m_0=\dim K_0$、$e_\lambda=\dim(E_\lambda\cap K_0)$、
   $T_\lambda=(A-\lambda I)|_{K_0}$。
2. 列出非空分量（126）：
   * $\mathcal D_2$ 点：$\lambda\ne\mu$、$e_\lambda,e_\mu\ge1$；
   * $\operatorname{Gr}(2,E_\lambda)$：$e_\lambda\ge2$；
   * $J_\lambda$：$e_\lambda\ge1$ 且 $\operatorname{im}T_\lambda\cap\ker T_\lambda\ne0$；
   * $\mathcal D_3$：$e_\lambda\ge1$ 且 $m_0\ge3$（$m_0=2$ 用特例）；
   * $\mathcal D_3$ (b) 幂零 2-步（131）：$D=K_0\cap A^{-1}K_0\ne0$ 且 $A|_D$ 非标量；
   * $\mathcal D_4$：维数充分条件（所有 $e_\lambda\le m_0-2$）或 $m_0=2$ 精确。
3. 对每个非空分量取随机点：
   * 点：$V$ 固定；
   * $\operatorname{Gr}(2,E_\lambda)$：$E_\lambda\cap K_0$ 中的随机 2-平面；
   * $J_\lambda$：随机特征线 $L\subset E_\lambda\cap K_0$，随机 $w\in K_0$ 解 $(A-\lambda I)w\in L\setminus\{0\}$；
   * $\mathcal D_3$：随机 $L$，随机 $w\in K_0\setminus L$ 且 $V/L$ 不是 $\bar A$ 的特征线；
   * $\mathcal D_3$ (b)：随机 $L\in\mathbb P(D)$ 非特征线，$V=L+AL$；
   * $\mathcal D_4$：随机 $V\in\operatorname{Gr}(2,K_0)$，检查 $\dim(V+AV)=4$（否则重取）。
4. 对每个 $V$：取 $m$ 行随机 $R$（每行在 $(V+AV)^\perp$ 里），检查
   $\operatorname{rank}H=\omega$、$\operatorname{rank}[L_0;R]=q$；算 $\lambda H-H_A$ 的 $\omega$-子式 gcd；
   gcd $=1$ 则**接受**。
5. 全部分量都不接受则**拒绝**。

**正确性**：同 123。每分量不可约；坏集闭；好分量随机点以概率 1 落好集；全坏分量永不接受。
故**无假阳性**，假阴性由 Schwartz–Zippel 控制（每分量 $\le D/N$，重复 $T$ 次）。

## 进展

* 算法框架完成；分量表 + 非空条件 + 随机点 + gcd 四块齐全。
* 复杂度：分量数 $\le\binom{s}{2}+3s+1$（谱的函数）；每片一次 gcd；总复杂度多项式。
* 候选实例：$n=8,p=2,r=1$、$k=4,\omega=2,q=3$ 的 seed 60/103/146/318 正好是 $c=2$；
  精确验证留作辅助（按项目规矩，实验不作证明）。

## 最终结论

* $c=2$ 有一个端到端一侧算法，与 $c=1$ 的 123 同型：
  **分量表（125）→ 非空筛选（126）→ 每分量随机点 + gcd**。
* 分量数只依赖谱，不是“任意 determinantal variety”；这是 $c=2$ 可算法化的原因。
* 完整 DEC(q) 仍要对 $\omega$ 取并；实点另算。

## 放弃原因

* 没有具体实例的精确验证；
* $\mathcal D_4$ 的精确覆盖判定（除 $m_0=2$）未给；采样可能漏掉非空性；
* 实点、确定性版本、$c\ge3$ 未做。

## 残留价值

* $c=2$ 的第一个端到端判定过程，直接复用 123 的模板。
* 把“分量分类 + 非空条件”接成算法；为 $c=3$ 的归纳提供模板。
* 论文“算法”一节的 $c=1/c=2$ 两小节。

## 相关文件

* [attempts/123](../../c_stratification/attempts/123_hyperplane_algorithm.md)（$c=1$ 算法模板）
* [attempts/125](../../c_stratification/attempts/125_c2_structure_complete.md)（$c=2$ 分类）
* [attempts/126](../../c_stratification/attempts/126_c2_k0_truncation.md)（非空条件）
* [attempts/113](113_projective_theorem_corrected.md)（genericity）

## 状态

* 算法：**[M2，纸面 + 概率界]**。
* 正确性：一侧；假阴性 $\le2^{-T}$。
* 未做：实例验证、$\mathcal D_4$ 精确覆盖、实点、$c\ge3$。
