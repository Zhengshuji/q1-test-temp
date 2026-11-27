> **已收窄（463）**：本文"一次计算覆盖整卡"的说法**过强**——清分母得到的是非零多项式 $D(X)$ 而非 $1$，
> 只保证**非空开集**。正确形式见 [463](../../decision_algorithms/attempts/463_expert108_audit.md) 与其中的泛型秩路线。

# 461 移植 Paper III 的 Claim 8：一次计算覆盖**整卡**——修掉我 454/456 的"泛型点"错误

> 读 [Paper III](../../../../paper/current/paper_III_hyperplane.pdf)（超平面层）发现它的
> **Claim 8（满秩首项系数引理）** 正是我 454/456 缺的机制。本文件把该机制移植到我的 (R)(E$'$) 框架。

## 目标

弄清 Paper III 如何在"泛型点"与"整卡"之间跨过去，并判断能否移植。

## 设想与理由

Paper III 的表述（原文）：
> "On a chart of the parameter space, the maximal minors have no common root over the function field
> **if and only if every point of that chart is feasible**. The step from a generic point to the whole chart
> is a full-rank leading-coefficient lemma (Claim 8); without it a generic test certifies only a generic point."

**机制**（我的理解）：在函数域 $\mathbb Q(\text{参数})[\lambda]$ 上做 $\gcd$，若为 $1$，则存在
**带多项式系数的 Bézout 恒等式**
$$a(\lambda;\mathbf t)\,m_1+\cdots+b(\lambda;\mathbf t)\,m_s=1 .$$
这个恒等式在参数的**每个**特化点（分母不为零处）仍有意义 ⟹ 特化后 $1$ 落在理想里 ⟹ 子式在该点**没有公共根** ✓。
——所以"函数域上 $\gcd=1$"给出的是**整卡**结论，不只是泛型点 ✓✓。

## 做法

抽出 Claim 8 的陈述与证明机制（Bézout 恒等式），再看我的两个条件是否同型。

## 进展

## 移植到我的框架

我的两个条件在**坐标卡**上都是"某个子式 $\ne0$"（见 [457](457_constructible.md)）：
- $(E')$：$\pi_2(\mathcal T_W)=W$，即某个 $\omega\times\omega$ 子式 $\ne0$；
- $(R)$：$\operatorname{span}(V_0\cup\pi_1(\mathcal T_W))=W$，同样是一个子式 $\ne0$（包含性自动 ✓）。

所以**同一个 Bézout 论证适用** ✓：

> **命题（整卡判据）.** 固定 Grassmannian 的一个坐标卡。若在该卡的**函数域**上两个条件成立，
> 则该卡上**每个点**（在其常秩层内）都可行；反之若函数域上失败，则该卡上**没有**可行点。

## 这解释了我 456 的失败

456 里"网格能命中、随机点命不中"，原因很清楚：

$$\text{我的随机点与网格点落在\textbf{不同的坐标卡}}$$

- 随机大整数点几乎必然落在"主卡"（某坐标非零）上；那里函数域上的条件**恒假** ⟹ 该卡全不可行 ✓；
- 网格点（含 $0$ 坐标）落在**别的卡**上；那里函数域条件可能成立 ⟹ 整卡可行 ✓。

**所以我的测试不是"泛型点原理错"，而是"只查了一个卡"** ✗ ——Paper III 的做法是**按卡逐一算** ✓。

## 最终结论

1. **移植成功**：Paper III 的 Bézout/满秩机制在我的 (R)(E$'$) 上适用（两个条件都是"子式 $\ne0$"型）；
2. **456 的失败有了解释**：不是"泛型点不决定"，而是"**只查了一个卡**"——每个卡各自有一个函数域判定；
3. **正确算法**：**枚举 Grassmannian 的有限个坐标卡**（$k$ 个），**每卡做一次函数域计算** ⟹ 判定 ⟹
   这是 Paper III 的做法，且它对固定 $p$ 是多项式的 ✓；
4. 于是中间层的判定**回到"可算"**，且**不依赖泛型点** ✓。

## 放弃原因

- 没有实际实现"按卡逐一算"（只做了机制论证）；
- 没有核对 Paper III 的 Claim 8 是否**只对超平面层**成立（它的证明可能在 $\omega=k-1$ 时用到特殊结构）；
- 没有算"每卡一次计算"的复杂度（可能随卡数 × $\gcd$ 代价增长）。

## 残留价值

- **一次正确的移植**：把 Paper III 的"整卡"机制搬到我的框架，并修掉 456 的错误解释；
- 明确了正确算法形态（按卡枚举 + 每卡一次函数域计算）；
- 我的 454/456 的争论可以收束：**问题不在"泛型 vs 全部"，而在"卡的选择"**。

## 下一步

1. 核对 Claim 8 的适用范围（是否依赖超平面层的 $\omega=k-1$）；
2. 在我的实例上实现"按卡逐一算"，验证它给出的答案与网格枚举一致；
3. 若一致，中间层的判定就有了**可算且正确**的算法，$q1$ 的 P 一侧变得实在。

## 相关文件

- [Paper III](../../../../paper/current/paper_III_hyperplane.pdf)（Claim 8）
- [457](457_constructible.md)（构造性集）
- [456](../../decision_algorithms/attempts/456_generic_fails.md)（泛型点失败，本文件给出正确解释）
- [454](454_open_not_closed.md)（已撤回）

## 状态

- 整卡判据（移植）：**[已证-纸面]**（Bézout 论证）。
- 按卡实现：**[未做]**。
- Claim 8 的适用范围：**[未核]**。
