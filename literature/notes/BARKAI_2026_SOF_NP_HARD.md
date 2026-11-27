# Barkai–Shames (2026), *On the NP-Hardness of Unconstrained Static Output Feedback Stabilization* — 阅读笔记

> arXiv:2609.38728v1（2026-09-30），15 页，eess.SY。
> 作者：Gal Barkai（Université de Lorraine, CNRS, CRAN）、Iman Shames（University of Melbourne）。
> 读取日期：2026-11-09。全文：`literature/papers/2609.38728.{pdf,txt}`。

---

## 1. 主要结果

- 从 **Subset Sum** 多项式归约到**无约束**静态输出反馈（SOF）稳定化 ⇒ **NP-hard**；
- 构造：一个输入、$N$ 个输出、$10N+3$ 个状态；
- 每个输出含一个带通（band-pass）标量原型，其稳定增益落在 1 和 2 附近的两个窄区间；
  另加一个共享求和块的加权副本，强制 $W=\\sum_i a_i k_i$ 落在窄区间；
- 用**频率分离**（带通变换）把 $N+1$ 个解耦回路的稳定性与耦合 plant 的稳定性联系起来；
- 用 Rouché 定理比较真实特征多项式与各块在右半平面不同区域的根数；
- 构造自然给出**每个稳定增益的界**与显式 modulus margin，plant 数据是多项式二进制编码。

## 2. 与 Liu/Ahmadi/Löfberg 的区别

| | Barkai–Shames | Liu | Ahmadi et al. | Löfberg |
|---|---|---|---|---|
| 结论 | **NP-hard** | **∃R-complete** | **NP-hard** | **NP-hard** |
| 归约源 | Subset Sum | ETR | 3SAT | Betweenness |
| 特点 | 频率分离、增益有界、modulus margin | 有效增益维数、残差进系数 | 连续+离散、无法写出控制器 | 单输入多输出、Routh 行列式 |

NP-hard 弱于 ∃R-complete；不能替代 Liu 作为“完全”来源，但技术上有用。

## 3. 对本项目的可用点

1. **增益/见证的界**：构造给出每个稳定增益的显式界与 modulus margin，
   这对“spurious witness（任意大增益）”是直接的技术参考；
2. **频率分离**：把解耦块的稳定性与耦合 plant 的稳定性严格连接，
   与观测器“铅笔在所有 λ 上满秩”有相似形状（都是全频条件）；
3. **近似离散选择**：两个标量块强制增益落在窄区间，可作为编码布尔/离散选择的模板；
4. **Rouché 根计数**：可能用于把“所有 λ 的秩条件”转化为有限区域上的根计数。

## 4. 与本项目的关系（限制）

- 目标条件是 **Hurwitz**（根在左半平面），不是“$\\lambda L-LA$ 的铅笔满秩”；
- 归约是 NP-hard，不是 ∃R-complete；对 $q1$ 只能作为**中间里程碑**或技术来源；
- 观测器的自由度是行空间 $L$（连续子空间），不是增益矩阵 $K$；编码方式不能直接搬。
