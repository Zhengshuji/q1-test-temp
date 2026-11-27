# 隐式多项式矩阵路线（专家 Q5 首选）：结构化编码是**多项式规模**的

> **2026-11-04 更正（重要）**：本文最初把"典型层占 $q_0$ 样本仅 7%"当作"结构化编码覆盖面有限、全阶 $\exists\mathbb R$ 未定"
> 的理由。**这是错的**：项目早有的 G.1 编码（`proof/dec_q_existsR`）正是**结构化**左逆
> $X(\lambda)P(\lambda)=I_t$（次数界用 Noferini–Van Dooren 的铅笔右逆判据），而**退化层由
> $O(n)$ 项"$s=\dim(Z\cap\mathcal V)$"析取 + 在商 $V/S$ 上做左逆**处理，根本不需要广义逆或 Smith 酉模的次数控制。
> 因此 **$\mathrm{DEC}(q)\in\exists\mathbb R$（多项式规模，每个固定 $q$）成立**；本文实测到的指数 $N$ 只属于
> **非结构化**变体 $\sum u_im_i=1$。下面的"最终结论"第 3–4 条按此更正理解，正文其余部分（规模核算、7% 统计、
> 未完成的自动核对）仍然有效。

## 目标

按专家 2026-11-04 §Q5 的第 1 优先级：**不展开极大子式**，把 $(5b)$ 写成**矩阵等式**，
看编码规模能否降到多项式。

## 设想与理由

朴素的 Bézout 写法 $\sum_i u_i m_i=1$（$m_i$ = $P_{\mathcal Z}(\lambda)$ 的极大子式）需要**显式**列出全部 $m_i$，
个数 $\binom{n}{\rho}\binom{\rho+d}{\rho}$ 随 $n$ 指数增长——这是我们此前"$\exists\mathbb R$ 路线作废"的依据。

但同一条件有**结构化**写法：在 $V\cap\mathcal Z=0$（即 $\operatorname{rank}[V|\mathcal Z]=\dim V+d=:\rho$，典型层）时
$$\operatorname{rank}P_{\mathcal Z}(\lambda)=\rho\ \ \forall\lambda
\iff \text{极大子式的 gcd 是常数}
\iff \exists X(\lambda)\in\mathbb C[\lambda]^{\rho\times n}\ (\deg X\le\rho-1):\ X(\lambda)P_{\mathcal Z}(\lambda)=I_\rho .$$
最后一条对 $X$ 的**系数线性**，未知数 $\rho\cdot n\cdot(\rho)=O(n^3)$；标准 Bézout 界给 $\deg X\le\rho\deg P-1=\rho-1$
（因 $\deg_\lambda P_{\mathcal Z}\le1$）。

**于是编码规模**（固定阶 $q$、典型层）：

| 项 | 规模 |
|---|---|
| 变量：$\mathcal Z$ 的参数 $W$（$k\times d$）与其左逆 $Y$（$d\times k$）| $O(n^2)$ |
| 变量：$(5a)$ 的辅助矩阵 $T$（$LA=T[\mathcal L;CA;C]$）| $O(n^3)$ |
| 变量：左逆 $X$ 的系数 | $\rho\cdot n\cdot\rho=O(n^3)$ |
| 方程：$YW=I_d$、$LA=T[\mathcal L;CA;C]$、$X P=I_\rho$ 的系数 | $O(n^3)$，次数 $\le2$ |

即：**结构化写法把编码从指数降到多项式**；而且**不需要枚举图卡**（用 $W$ 与 $YW=I_d$ 直接参数化 $\mathrm{Gr}(d,K)$）。

## 做法

* [compact_encoding_check.py](../../../../tools/verification/compact_encoding_check.py)：在给定 $\theta$ 上把
  $XP=I_\rho$ 写成对 $X$ 系数的线性系统，用精确秩判据（$\operatorname{rank}M=\operatorname{rank}[M|b]$）判可解；
  与"$P$ 的极大子式 gcd 次数为 0"对照。
* 另测：在 $q_0$ 阶的样本里，$V\cap\mathcal Z=0$（典型层）出现的频率。

## 进展

**（1）典型层在 $q_0$ 阶很稀**：$n=5,6,7$、$p,r\in\{1,2\}$、4 个 seed、全部图卡、每图卡 6 个随机 $\theta$，
共 660 个样本中

| 类别 | 计数 |
|---|---|
| $V\cap\mathcal Z=0$（典型层，编码可用）| **48** |
| $V\cap\mathcal Z\ne0$（退化）| **612** |
| $(5a)$ 可行 | 128 |

即典型层约占 7%——**多数 $q_0$ 阶样本落在退化层**，所以"典型层编码"在这些实例上几乎无处施力。

**（2）等价性未能自动核对**：脚本在"典型层且 $(5a)$ 可行"的交集里没有取到样本（660 个样本中该交集为空），
且用作参照的 Toeplitz 判据在**无 $(5a)$** 的 $L$ 上会触发 B.8 的断言失败（B.8 的前提就是 $(5a)$）——
故本轮**没有**得到"紧凑可解 ⟺ gcd 次数 0"的实测证据。脚本保留，但**不可作为结论依据**。

**（3）一般秩情形（$V\cap\mathcal Z\ne0$）**：此时 $\operatorname{rank}P=\rho<m$（列数），左逆不存在，
需要"秩因子分解"式编码
$$\exists P_1(n\times\rho),P_2(\rho\times m),X,Y:\ P=P_1P_2,\ XP_1=I_\rho,\ P_2Y=I_\rho .$$
存在性来自 Smith 形 $P=USV$（常秩 $\rho$ ⟹ $S=\operatorname{diag}(c_1,\dots,c_\rho,0)$，$c_i$ 为非零常数），
但 $U,V$ 酉模可有无界次数 ⟹ **$P_1,P_2,X,Y$ 的次数界未解决**，故该编码的"多项式规模"**未证**。

## 最终结论

1. **结构化（矩阵等式）编码确实是多项式规模**（典型层）：变量与方程均 $O(n^3)$、次数 $\le2$、且不需要枚举图卡；
   这**推翻**了我们此前"编码规模指数 ⟹ $\exists\mathbb R$ 路线作废"的断言——那个指数只属于**非结构化**
   的 $\sum u_im_i$ 写法；
2. **但覆盖面有限**：$q_0$ 阶样本中典型层仅约 7%（48/660），一般秩情形需要秩因子分解编码，其**次数界未解决**；
3. **等价性未实测**（脚本在可用样本集为空 + 参照判据在无 $(5a)$ 时失效）；
4. 因此对复杂度只应说：**典型层上 $\mathrm{DEC}(q)$ 有显式的多项式规模 $\exists\mathbb R$ 编码**，
   全阶/全秩层的 $\exists\mathbb R$ 成员性**仍未定**。

## 放弃原因

不适用（设计与规模核算完成；自动化核对与一般秩的次数界是明确的未完成项）。

## 残留价值

* 一个**多项式规模**的编码（典型层），以及它与非结构化 Bézout 的规模对比（$O(n^3)$ vs 指数）；
* 一个新的定量事实：**$q_0$ 阶样本约有 93% 落在退化层** $V\cap\mathcal Z\ne0$——这本身就是对"为什么逐卡/分层麻烦"的解释；
* 明确的未完成项：一般秩的次数界（Smith 形酉模的次数控制）、紧凑编码与 gcd 判据的自动化对照。

## 相关文件

- [tools/verification/compact_encoding_check.py](../../../../tools/verification/compact_encoding_check.py)（WIP，不作结论依据）
- [docs/08_results.md](../../../../docs/08_results.md) §5（$\exists\mathbb R$ 的更正已按本条改写）
- [workspace/for_expert/09_paper_proofs_for_review.md](../../../for_expert/archive/09_paper_proofs_for_review.md)（专家 Q5）
