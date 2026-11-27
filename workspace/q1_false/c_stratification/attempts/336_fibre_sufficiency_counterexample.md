# 336 纤维充分性猜想的**反例**：$K_0$ 含特征向量，整条特征纤维仍然全坏

> 承接 96 号（他建议"先找反例，再谈证明"）与 331（本族判据 $E\ne\varnothing$）。
> 本文件给出反例，并把缺失的条件定位到 **$\lambda=0$ 的秩**。
> 证书：[c341](../../../../tools/verification/c341_fibre_sufficiency_counterexample.py)。

## 目标

判定 96 号的 **Conjecture（纤维充分性）** 是否成立：临界模式下，$K_0$ 含特征向量是否总能
在对应特征纤维里找到可行点？

## 设想与理由

96 号说：若猜想假，反例本身有价值——它会指出"除了 $K_0$ 含特征向量之外还需要什么"。

一条必须满足的**独立条件**：$(5b)$ 要求 $\operatorname{rank}(\lambda H-H_A)=\omega$ 对**每个** $\lambda$，
特别地 $\lambda=0$ 时
$$\operatorname{rank}H_A=\omega .$$
而 $\operatorname{rank}H_A=\operatorname{rank}(LAN)=\dim(A K_0)-\dim(A K_0\cap\ker L)
=\dim(A K_0)-\dim(A K_0\cap V^\perp)$。

## 进展

- 反例已构造并**验证**（c341）：20 个随机层点，好 0 / 坏 20，全部 $\operatorname{rank}H_A\le1$。
- 结构原因一行：$\dim(A K_0)=\omega$ 且 $v\in A K_0$ ⟹ $A K_0\cap V^\perp\ne0$ ⟹ $\operatorname{rank}H_A\le\omega-1$。
- 缺失条件定位到 $\lambda=0$ 的秩；判据从"充要"降为"必要"。

## 做法与结果

**实例**：$n=5$、$p=1$、$C=e_5^{\mathsf T}$、
$$A=\begin{pmatrix}2&2&-1&0&0\\0&-2&1&0&1\\0&1&-2&0&-1\\0&0&0&0&2\\0&-1&2&0&-1\end{pmatrix}.$$
此时 $v=e_1$：$Ae_1=2e_1$、$Ce_1=0$、$CAe_1=0$ ⟹ **$e_1$ 是 $K_0$ 中的特征向量** ✓。

**结构**：$K_0=\operatorname{span}\{e_1,(0,2,1,0,0),e_4\}$，
$$A K_0=\operatorname{span}\{Ae_1=(2,0,0,0,0),\ A(0,2,1,0,0)=(3,-3,0,0,0)\},\qquad \dim(A K_0)=2=\omega .$$
且 $e_1\in A K_0$。

**于是**：任何层点都有行空间 $V\subseteq e_1^\perp$（因为自由行满足 $rv=0$），故 $V^\perp\supseteq\operatorname{span}\{e_1\}$。
结合 $e_1\in A K_0$：
$$\dim(A K_0\cap V^\perp)\ge1\ \Longrightarrow\
\operatorname{rank}H_A\le\dim(A K_0)-1=1<\omega=2 .$$
**故 $(5b)$ 在 $\lambda=0$ 处已经失败——与 $R$ 的选取无关。**

**验证**（c341）：20 个随机层点（都满足 $\operatorname{rank}H=2$、$(5a)$），
**好 0 / 坏 20**，且**全部** $\operatorname{rank}H_A\le1$；每个 $\gcd$ 都被 $\lambda$ 整除。

## 最终结论

1. **纤维充分性猜想不成立**：例中 $K_0$ 含特征向量，但对应特征纤维**整条全坏**，
   该层的非特征层（由 96 号的统一定理）也全坏 ⟹ **这一层的答案是否**。
2. **缺失的条件被定位**：$\lambda=0$ 是 $\mathbb C$ 中的点，所以
   $$\operatorname{rank}H_A=\omega\quad\text{是必要条件},$$
   而 $\operatorname{rank}H_A=\dim(A K_0)-\dim(A K_0\cap V^\perp)$。例中 $\dim(A K_0)=\omega$ 且 $e_1\in A K_0$，
   交集被强制非零 ⟹ 必要条件不可满足。
3. **对判据的修正**：不能写"$E\ne\varnothing\iff$ 可行"。正确的必要条件是
   $$\dim(A K_0)-\dim(A K_0\cap V^\perp)=\omega\quad\text{对某个可容许 }V,$$
   再叠加谱条件。这也就是 96 号三 regime 里"约简铅笔**可观测**"那一层的具体化。

## 放弃原因

- 只给出一个反例；"哪些 $A$ 会落入这种 $\lambda=0$ 障碍"没有一般刻画
  （一个已知的必要条件：$\dim(A K_0)\ge\omega+1$ 当 $v\in A K_0$）。
- 没有给出修正后的**充要**判据。
- 修正判据的算法复杂度未分析。

## 残留价值

- **一个干净的反例**（结构原因一行：$e_1\in A K_0$、$\dim(A K_0)=\omega$），证书可复跑；
- 把缺失条件定位到 $\lambda=0$ 的秩——这是 96 号要的"除了特征向量还需要什么"的第一条；
- 说明 331 的判据只是**必要条件**的一支，不能当充要。

## 相关文件

- [attempts/335](335_expert96_verdict.md)（96 号裁决：Theorem 2 与 Conjecture）
- [attempts/331](331_eigenvector_criterion.md)（判据；本文件给出反例，判据须修正）
- [attempts/329](329_forced_relations_quotient_pencil.md)（非特征层；96 号的统一定理）
- [attempts/333](333_eigen_fibre_symbolic_certificate.md)（正面侧的符号证书）
- [c341](../../../../tools/verification/c341_fibre_sufficiency_counterexample.py)

## 状态

- 反例：**[已证-纸面]** + **[精确验证]**（c341：20/20 坏、$\operatorname{rank}H_A\le1$）。
- 修正后的充要判据：**[未做]**。
