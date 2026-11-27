# Class I（$p=r=1$）的结构测绘：$\rho=q-1$、Type I 的二分、$q=2$ 的强制候选不可容许

## 目标

按专家 15 号评审的 Priority 2，开始"最小约束情形 $p=r=1$、$n$ 增长"的分析。
先做两件事：**查重**（项目以前是否做过）与**结构测绘**。

## 设想与理由

$p=r=1$ 时 $C=c^{\mathsf T}$、$L_0=\ell^{\mathsf T}$，$V=\ker[c;cA]$、$K=\ker[c;\ell]$ 都很大（$\dim=n-2$ 量级），
与 $n=6,p=r=2$ 的两个反例（$V\cap K=0$）**恰好相反**：这里 $V\cap K=\ker\{c,cA,\ell\}$ 有维数 $n-3$，
即**中间层是常态**。因此 B.17 的商铅笔判据是这个类里的正确工具。

## 查重（项目以前做过什么）

| 已有工作 | 内容 | 与本轮的关系 |
|---|---|---|
| **B.13f / attempts 66–67** | $\dim V=\dim K=1$ 的标量情形（唯一可能是 $n=3,p=r=1$）| 已证**退化**：$\det\equiv0$，判据只剩 $V\ne K$。⟹ $n=3$ 已做完 |
| **attempts/52** | $p=r=1$ 下编码规模 $N=\binom{1.5n-3}{n}$ 指数 | 编码规模，不是分类 |
| **attempts/76–79** | 分层、中间层、对照实验 | 用 $n=6,p=r=2$；未涉及 $p=r=1$ |
| 结论 | **$p=r=1$ 且 $n\ge4$ 的类此前没有系统分析** | 本轮开始 |

## 做法

1. 证明结构事实（$r_1=2$、$s_0\in\{2,3\}$、$s_0=3\iff\ell\notin\operatorname{span}\{c,cA\}$、维数公式）；
2. 核验降维公式 $\rho=q-1$（对 $\mathcal Z\subseteq V\cap K$ 的 $714$ 个样本）；
3. 检查 $q=2$ 时"唯一候选 $\mathcal Z=V\cap K$"的可容许性。

## 进展

**（1）结构事实（已证）**：设 $p=r=1$、$(c,A)$ 可观测。则
* $r_1=\operatorname{rank}[c;cA]=2$（若 $=1$ 则 $cA=\alpha c$，$(c,A)$ 不可观测，矛盾）；
* $\dim V=\dim K=n-2$、$\dim(V\cap K)=\dim\ker\{c,cA,\ell\}\ge n-3$；
* $s_0=\dim(\operatorname{row}[c;\ell]+W)\in\{2,3\}$，且 $s_0=3\iff\ell\notin\operatorname{span}\{c,cA\}$；
* 因 $r_1+r=3$：**若 $\ell\in\operatorname{span}\{c,cA\}$ 则 $s_0=2<3$，该实例任何阶都无 Type I**
  （B.11c 的直接推论）；若 $\ell\notin\operatorname{span}\{c,cA\}$，Type I 可能发生。

**（2）降维公式（已核验 714/714）**：若 $\mathcal Z\subseteq V\cap K$（当 $d=n-1-q\le\dim(V\cap K)$，即 $q\ge2$ 时可行），
则 $S=V\cap\mathcal Z=\mathcal Z$，故
$$\rho:=\dim(V/S)=\dim V-d=(n-2)-(n-1-q)=q-1,$$
商铅笔 $\overline N_{\mathcal Z}$ 的尺寸为 $(n-d)\times\rho=(q+1)\times(q-1)$——**形状只由 $q$ 决定**。$q=2$ 时是 $3\times1$（单列）。

**（3）$q=2$ 的情形（负结果）**：此时 $d=n-1-2=n-3=\dim(V\cap K)$，故 $\mathcal Z=V\cap K$ 是 $V\cap K$ 里唯一的
$(n-3)$ 维子空间。在 77 个可构造的实例上，它**全部不可容许**（$(5a)$ 不成立）。
⟹ $q=2$ 阶的候选必须**不**含于 $V\cap K$（即 $s<d$），不能用"最大交集"候选。

## 最终结论

1. **查重结果**：$p=r=1$ 只在 $n=3$（退化）与编码规模两处做过；$n\ge4$ 的类**此前未分析** ✓；
2. **结构测绘完成**：$r_1=2$、$s_0$ 的二分、维数公式、以及**降维公式 $\rho=q-1$**（714/714）；
3. 这把 $p=r=1$ 的分类问题压成"**每阶一个 $(q+1)\times(q-1)$ 的小铅笔**"，但 $q=2$ 的"最大交集候选"不可容许，
   说明还要在 $s<d$ 的层里找；
4. 下一步：对 $q=q_0$ 与 $q=q_0+1$ 写清小铅笔的显式形式（$3\times1$、$4\times2$），并求"是否存在 $\mathcal Z$ 使其单射"。

## 放弃原因

不适用（测绘完成；分类待续）。

## 残留价值

* **降维公式 $\rho=q-1$**：把 $n$ 增长的问题压成 $q$ 决定的固定形状；
* $p=r=1$ 的 Type I 二分（$\ell\notin\operatorname{span}\{c,cA\}$ 才可能有 Type I）；
* 查重记录（本次没重复已有工作）。

## 相关文件

- `docs/02` B.17（商铅笔）、B.11c（Type I 判据）、B.13f（$n=3$ 退化）
- 专家答复：`workspace/for_expert/archive/15_stratification-answer.md` §2.6（Class I）
