# 329 商铅笔的强制关系：$C$ 的行落在 $U^\perp$ 里，白送 $p$ 个零组合

> 承接 328（商铅笔定理）与 95 号 §6.1 的建议（采特殊点，而不是只随机采样）。
> 本文件给出一个**结构命题**，它解释了 E3 的"次数恒为 2"，并说明那**不是** H1b 的证据。

## 目标

解释：为什么在 $n=5,p=1,r_0=0,q=3$ 的族里，降维铅笔 $\widetilde M$ 的三个 $2$-子式总是
$[q,0,0]$（$q$ 为二次），以及这对层可行性意味着什么。

## 设想与理由

查 E3 的实例时发现：$\widetilde M$ 有**整行恒零**。追下去是 $C$ 的行造成的。

$\mathcal T$ 与 $K_0$ 都在 $C$ 的核里（$K_0=\ker[C;CA]$，故 $K_0\subseteq\ker C$），
而 $U=\operatorname{span}(v,Av)\subseteq K_0$。所以 $C$ 的每一行（作为 $\mathbb C^n$ 的向量）都落在 $U^\perp$。

## 做法

### 命题（强制关系）

> **命题.** 设 $U\subseteq K_0$，$Q$ 的**行空间**为 $U^\perp$，$\hat N$ 为 $K_0$ 的基去掉 $v$ 那一列。
> 则对 $C$ 的每一行 $c$，存在唯一 $y\in\mathbb C^{n-2}$ 使 $c=y^{\mathsf T}Q$，且
> $$y^{\mathsf T}\widetilde M(\lambda)\equiv0,\qquad \widetilde M=Q(\lambda I-A)\hat N .$$
> 因此
> $$\operatorname{rank}\widetilde M(\lambda)\le n-2-p\qquad\forall\lambda .$$

> **适用性（97 号审计）**：秩界是对**辅助铅笔** $Q(\lambda I-A)N$（即行空间取满 $U^\perp$）证的。
> 一般层点 $V\subsetneq U^\perp$ 时，$C$ 的行未必在 $V$ 里，$p$ 个零行就不出现，
> **秩界不能直接搬到观测器铅笔上**。可用的情形是 $q=n-2$（此时 $V=U^\perp$ 被迫）。

*证明.* $U\subseteq K_0\subseteq\ker C$ ⟹ $c\perp U$ ⟹ $c\in U^\perp=\operatorname{row}Q$ ✓。
又 $\hat N$ 的列属于 $K_0=\ker[C;CA]$，故 $c\hat N=0$ 且 $cA\hat N=0$。于是
$$y^{\mathsf T}\widetilde M=Q(\lambda I-A)\hat N\ \text{的对应组合}=c(\lambda I-A)\hat N=\lambda c\hat N-cA\hat N=0 .$$
$p$ 个这样的 $y$ 线性无关（因为 $c$ 的行满秩 $p$ 且 $Q$ 是基），故行空间的秩至少被削掉 $p$。$\square$

**直接推论**：若 $n-2-p<k-1$（等价于 $\operatorname{rank}[C;CA]=p$，即 $CA$ 的行已含于 $C$ 的行空间），
则 $\operatorname{rank}\widetilde M\le n-2-p<k-1$ 恒成立 ⟹ **每个层点都坏，层不可行**。

### E3 的族：$n=5,p=1,k=3$

此时 $n-2-p=2=k-1$，**恰好卡在边界**：不是自动坏，需要看剩下那个子式。$C=e_5^{\mathsf T}$ 时
$Q$ 里含 $e_5$，对应整行零；剩下是 $2\times2$ 的铅笔
$$\widetilde M_{\rm eff}(\lambda)=\lambda X_{\rm eff}-G_{\rm eff},$$
它的行列式是一个**二次式** $q(\lambda)$。而
$$\text{坏}\iff\exists\lambda:\operatorname{rank}\widetilde M(\lambda)<2\iff q(\lambda)=0 .$$
在 $\mathbb C$ 上，非常值二次式**必有根** ⟹ **该族非特征层的每个点都坏**。

实测（3 个随机 $A$）：非零子式恰 1 个、次数 2、**判别式非零**（两个不同根）；
把 $L$ 换成更小的行空间（2 行、仍 $\operatorname{rank}H=2$）时，gcd 仍是二次 ⟹ 也坏。
这与"更小的 $V$ 只会让 $P$ 更矮、更容易降秩"一致。

## 进展

1. **E3 的"次数恒为 2"有了解释**：不是 H1b 的普遍现象，而是"$C$ 白送 $p$ 个零组合、剩下的有效铅笔是 $2\times2$"这个**维度巧合**。
   95 号警告"不能只靠固定核方向推全分量度数恒定"——他是对的，而且这里的解释还要多一层（$C$ 的强制关系）。
2. **E3 那个族的层是不可行的**（非特征层全坏），且原因是结构的：非常值二次式必有根。
3. 一个新的、可判的充分条件：$\operatorname{rank}[C;CA]=p$ ⟹ 该层的非特征部分**自动不可行**。

## 最终结论

1. 商铅笔还要再削掉 $p$ 行：$\operatorname{rank}\widetilde M\le n-2-p$。这是 328 的定理应当补上的一条。
2. H1b 在 E3 上的"证据"作废——它与 H1b 无关，是维度巧合。
3. **下一步**（也是这个族的唯一悬念）：**特征纤维 $F_\lambda$ 是否可行**（H4）。若特征纤维也坏，则这个族的 $c=1$ 层整体不可行；
   若好，则要解释"为什么偏偏特征点好"——那才是真正的结构现象。

## 放弃原因

- 没有一般地处理 $\operatorname{rank}[C;CA]>p$ 的情形（此时 $n-2-p>k-1$，需要看有效铅笔的行列式是否为常数）；
- 没有判定 $F_\lambda$（下一步）；
- 没有证明"有效 $2\times2$ 的行列式非常值"对**所有** $v$ 成立（只测了 3 个实例的判别式非零）。

## 残留价值

- 一个能解释"$[q,0,0]$"的结构命题（含证明），以及"$\operatorname{rank}[C;CA]=p$ ⟹ 自动不可行"的可判充分条件；
- 撤回了 E3 对 H1b 的支持（避免把维度巧合当成普遍现象）；
- 把该族的悬念收窄到**特征纤维**。

## 相关文件

- [attempts/328](../../decision_algorithms/attempts/328_quotient_pencil_theorem.md)（商铅笔定理）
- [attempts/327](327_lambda_movement_experiment.md)（E3/E4）
- [attempts/326](../../decision_algorithms/attempts/326_eigenvector_form_of_badness.md)（谱形式）
- [attempts/324](324_hyperplane_component_theorem.md)（分量：$Z^\circ$ 与 $F_\lambda$）
- 专家 95 号答复：[archive/95-...-reply](../../../for_expert/archive/95_hyperplane_experiments_and_conjectures-reply.md)

## 状态

> **更新（专家 96 号，见 [335](335_expert96_verdict.md)）**：本文件里"有效 $2\times2$ 的行列式是否非常值"
> 这个待检项**已被统一证明**——把 $C$ 放进 $Q$ 的基，$\operatorname{rank}X=2$（$X$ 可逆），
> 故 $\det B(\lambda)=\lambda^2\det X+\cdots$ 次数恰为 2，必有复根；**判别式无关、重根也算根**。
> 于是"非特征层全坏"从"实例级"升为**定理**。

- 命题（强制关系）：**[已证-纸面]**；实例核对：**[精确验证 3 例]**。
- "$\operatorname{rank}[C;CA]=p$ ⟹ 自动不可行"：**[已证-纸面]**（推论）。
- 非特征层全坏（本模式）：**[已证-纸面]**（96 号）。
- 该族特征纤维：**[未定]**。
