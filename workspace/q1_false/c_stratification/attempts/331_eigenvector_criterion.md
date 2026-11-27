# 331 这一族的 $c=1$ 层：判据就是"$K_0$ 里有没有特征向量"

> 承接 329（非特征层结构性全坏）、330（特征纤维生成好）。
> 补充实验：[c338](../../../../tools/verification/c338_bad_eigen_fibre_search.py)（10 个实例搜"全坏"特征纤维，未找到）。

## 目标

把 $n=5,p=1,r_0=0,q=3$ 这一族的 $c=1$ 层判定收敛成一个**可测的判据**，
并写清哪一半是定理、哪一半是证据。

> **范围更正（专家 96 号）**：这个判据**不是**普遍原则，而是**临界维度** $n-2-p=k-1$ 的推论。
> 普遍的表述是"可行性 $\iff$ 某个可容许层含有一个**约简铅笔可观测**的点"。
> 三个 regime：$n-2-p<k-1$（自动坏）、$=k-1$（方阵 ⟹ 必有根 ⟹ 全坏）、$>k-1$（可能好，特征向量**不再是**必要条件）。
> 详见 [335](335_expert96_verdict.md)。
>
> **反例（[336](336_fibre_sufficiency_counterexample.md)）**：本判据**不是充要**——存在实例
> $K_0$ 含特征向量、但整条特征纤维全坏（原因：$\dim(A K_0)=\omega$ 且 $v\in A K_0$ ⟹
> $\operatorname{rank}H_A\le\omega-1$ ⟹ $(5b)$ 在 $\lambda=0$ 处即失败）。
> 所以本文的判据应读作**必要条件**；缺失的条件是 $\lambda=0$ 的秩条件
> $\operatorname{rank}H_A=\omega$。

## 设想与理由

324 给出：$Z=Z^\circ\cup\bigcup_\lambda F_\lambda$。于是层可行 $\iff$ 某个分量可行。
两半的性质完全不同：

- **$Z^\circ$（非特征层）**：329 证明 $\operatorname{rank}\widetilde M\le n-2-p$；在本族 $n-2-p=2=k-1$，
  剩下的有效铅笔是 $2\times2$、行列式为非常值二次 ⟹ 必有复根 ⟹ **整支全坏**（证）。
- **$F_\lambda$（特征纤维）**：330 在一个实例上给出显式好点；c338 在 10 个不同 $A$ 上各取 12 组行，
  每个实例都出现好点（8–11 组）⟹ **生成好**（证据，未证一般情形）。

## 做法（判据）

$$
\text{层可行}\iff E:=\bigcup_\lambda\mathbb P\bigl(K_0\cap\ker(A-\lambda I)\bigr)\cap B\ne\varnothing .
$$

- $E=\varnothing$ ⟹ 只有 $Z^\circ$，而它全坏 ⟹ **不可行（已证）**。
- $E\ne\varnothing$ ⟹ 对应 $F_\lambda$ 非空；只需在其纤维里找到**一个**好点（$\operatorname{rank}H=k-1$、$(5a)$、$\gcd=1$）
  ⟹ 该分量可行 ⟹ **可行（证书式）**。

**$E$ 的计算是多项式的**：算 $A$ 的特征结构、与 $K_0$ 求交，取非空项。

## 进展

| 方向 | 状态 |
|---|---|
| $E=\varnothing\Rightarrow$ 不可行 | **[已证-纸面]**（329 + 324） |
| $E\ne\varnothing\Rightarrow$ 可行 | **有证书即可证**（330 的判据）；一般情形下"是否总有证书"= H4，**未证** |
| 反例搜索 | c338：10 个实例、每实例 12 组行，**未见全坏的特征纤维** |

**推论（条件性）**：若 H4 对本族成立，则本族的 $c=1$ 判定属于 **RP**（一侧错误：NO 精确、YES 带证书）。

## 最终结论

1. 本族的层判定被压成一句话：**$K_0$ 里有没有特征向量**（且落在 $B$ 里）。
2. 否的一侧是**定理**；是的一侧**只要给一个显式好点**就成立——所以实践上判定是多项式的（带证书）。
3. 尚未闭合的只有：**"$E\ne\varnothing$ 时纤维一定生成好"**（= H4 的本族版本）。c338 的 10 个实例全支持它，
   但仍需结构解释（95 号说 H4 需要这样一层）。

## 放弃原因

- H4 的本族版本未证（只有 10 个实例的证据）。
- 只处理 $r_0=0$；$r_0>0$ 时 $B$ 更小、$E$ 可能为空，判据要相应调整（未做）。
- 只在 $n=5,p=1,q=3,k=3$ 这一维度模式上成立；$n-2-p\ne k-1$ 时非特征层未必全坏（329 的机制不适用）。

## 残留价值

- 一个**可操作的判据**（$E\ne\varnothing$?）与它的两侧状态（定理 / 证书）；
- 把 H4 压缩成"本族特征纤维是否总生成好"，并给了 10 个实例的支持；
- 一个条件性算法结论（RP）。

## 相关文件

- [attempts/329](329_forced_relations_quotient_pencil.md)（非特征层全坏）
- [attempts/330](330_eigen_fibre_feasibility.md)（特征纤维生成好）
- [attempts/324](324_hyperplane_component_theorem.md)（$Z=Z^\circ\cup F_\lambda$）
- [c337](../../../../tools/verification/c337_eigen_fibre_check.py)、[c338](../../../../tools/verification/c338_bad_eigen_fibre_search.py)

## 状态

- "$E=\varnothing\Rightarrow$ 不可行"：**[已证-纸面]**。
- "$E\ne\varnothing\Rightarrow$ 可行"：**证书式可证**；一般性 = H4，**[未证]**。
- 判据本族内可用；其它维度模式**[未处理]**。
