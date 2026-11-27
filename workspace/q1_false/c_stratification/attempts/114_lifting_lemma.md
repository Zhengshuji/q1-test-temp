# 满行秩 lifting 引理

> 2026-11-08。补专家 52 号的 lifting 缺口：给定压缩层面的兼容对 $(H,H_A)$，何时存在
> $R$ 使 $L=[L_0;R]$ 满行秩？答案是**一条可判定的线性代数引理**（符号秩），不是新的几何。
> 状态：**M2（纸面）**；$k=3$ 例子的好点已回代验证。

## 目标

设 $N=N_K\in\mathbb C^{n\times k}$、$M=AN_K\in\mathbb C^{n\times k}$，$m=q-r$。给定
$H_b,H_{A,b}\in\mathbb C^{m\times k}$，令
$$\mathcal R=\{R\in\mathbb C^{m\times n}:\ RN=H_b,\ RM=H_{A,b}\}.$$
目标是判定 $\mathcal R$ 中是否存在 $R$ 使 $\operatorname{rank}[L_0;R]=q=r+m$。

## 设想与理由

* $\operatorname{rank}[L_0;R]=r+m$ $\iff$ $R$ 的 $m$ 行在商空间 $\mathbb C^n/\operatorname{row}L_0$ 中的像线性无关。
* $\mathcal R$ 是仿射空间；$\pi R$ 对 $R$ 是线性的，所以"一般 $R$ 的 $\pi R$ 秩"就是符号矩阵的秩。
* 于是 lifting 归结为：符号矩阵 $\pi R(t)$ 是否有 $m$ 阶子式不恒为零。

## 做法

设 $\pi:\mathbb C^n\to\mathbb C^n/\operatorname{row}L_0$ 是商映射，$R_0$ 是 $\mathcal R$ 的一个特解，
$R_1,\dots,R_s$ 是齐次空间 $\{R:RN=0,RM=0\}$ 的基。令
$$\pi R(t)=\pi R_0+\sum_{j=1}^s t_j\,\pi R_j .$$

**引理（lifting）**：先设 $\operatorname{rank}L_0=r$（否则没有 lift；这是初始不可行检查），并需 $m\le n-r$（$q\le n$）。
1. $\operatorname{rank}[L_0;R]=q\iff\operatorname{rank}(\pi R)=m$；
2. $\mathcal R$ 含满行秩 lift $\iff$ $\pi R(t)$ 在 $\mathbb C(t)$ 上秩为 $m$（等价地，某个 $m$ 阶子式不恒为零）；
3. 若 (2) 成立，则满行秩 lift 的集合在 $\mathcal R$ 中 Zariski 开稠密。

*证明*：
1. $[L_0;R]$ 的行空间维数 $=r+\operatorname{rank}(\pi R)$（把 $R$ 的行模 $\operatorname{row}L_0$ 约化）。
2. $\pi R(t)$ 的每个 $m$ 阶子式是 $t$ 的多项式；某个不恒为零 $\iff$ 存在 $t$ 使其非零 $\iff$
   $\exists R\in\mathcal R$ 使 $\pi R$ 满秩。$\mathbb C$ 无限，故"不恒为零"等价于"存在零点非零"。
3. 满秩 locus 是这些非零子式的补，故 Zariski 开稠密。$\square$

**推论（实用判据）**：只需解一次线性系统得 $R_0$ 与齐次基 $R_j$，再算一个符号矩阵的秩；
不需要几何分解，也不需要搜索 $R$。

**一般形式（专家 53 号）**：设 $\mathcal A=R_0+\mathcal V\subseteq\mathbb C^{m\times n}$ 是非空仿射子空间，
$\pi:\mathbb C^n\to\mathbb C^N$ 是固定线性映射。则
$$\mathcal A_{\rm full}=\{R\in\mathcal A:\operatorname{rank}(\pi R)=m\}$$
或为空，或是 $\mathcal A$ 的非空 Zariski 开稠密子集；非空 $\iff$ 一般 $\pi R(t)$ 在仿射参数域上秩为 $m$。
observer lifting 取 $\pi$ 为商 $\mathbb C^n\to\mathbb C^n/\operatorname{row}L_0$ 即可。

## 进展

* 引理已证（三行）。
* $k=3$ 的实例：112 的表对好点回代 $R_0$，$\operatorname{rank}[L_0;R_0]=3$，故 lift 存在；
  引理进一步说"存在 $\iff$ 符号秩 $=2$"，且存在时是开稠密的。
* 未做：把符号秩判据写成对一般 $k=3$ 实例的自动检查（工具已有雏形，未接符号秩）。

## 最终结论

* lifting 不再是一个几何缺口：它是**仿射空间上的符号秩判定**，可判定、可验证。
* 对 $k=3$ 的族定理：104 的例外点、112 表里的好点都已回代验证；开层/坏层不需要 lift。
* 这补上了专家 52 号对 $d=1$ 族定理的限定。

## 放弃原因

* 没有把符号秩判据接进 112 的工具（需要符号矩阵的秩；可以用 `sympy` 或精确插值）。
* 没有对一般 $k$ 给出"符号秩何时满"的组合判据（只给了可判定性）。

## 残留价值

* 一条干净、可判定的 lifting 引理，适用于任何 $k,q,r$。
* 把"满行秩"从几何问题降为线性代数符号秩，和 $q=2$ 判据、投影定理的 gcd 判定同一层次。
* 可直接写进论文的“lifting”一节。

## 相关文件

* [attempts/109](109_family_theorem_p1_mixed.md)（$d=1$ 族；lifting 限定）
* [attempts/112](112_incidence_table.md)（$k=3$ 的表；好点回代）
* [attempts/113](../../decision_algorithms/attempts/113_projective_theorem_corrected.md)（修正版投影定理的 (e) 条件）

## 状态

* 引理：**[已证-纸面，M2]**。
* 实例验证：**[精确验证]**（104/112 的好点 $R_0$ 满行秩）。
* **[Lean 内核-独立编译]**：`rank_prod_eq`（`workspace/augmentation_family/lean/LiftKernel.lean`）编译通过；
  `#print axioms` = `[propext, Classical.choice, Quot.sound]`。未加入 `lake build MyProof` 聚合图。
* 未做：符号秩自动判据、一般 $k$ 的组合判据。
