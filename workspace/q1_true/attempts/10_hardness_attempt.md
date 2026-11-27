# 路线 11（c）：向"层判定 NP/∃ℝ-难"的一次具体尝试与失败分析

> 2026-10-30。按专家优先级 4（最后做归约）。本文记录：归约必须达到什么、我试了什么、卡在哪。
> **没有**得到任何 hardness 结论 ✗。

## 目标

把某个已知难问题 $H$ 多项式时间归约到"层不可行"判定：

$$x\in H\ \Longleftrightarrow\ \text{实例 }\varphi(x)\text{ 的第 }(\rho,c)\text{ 层不可行}\quad(\text{即型层被 }\mathrm{Bad}\text{ 完全覆盖}).$$

## 设想与理由

**想法**：让型层恰好只有**两个**成员 $\mathcal V_0,\mathcal V_1$，其中
- $\mathcal V_0$ 可行（$(5b)$ 成立）；
- $\mathcal V_1$ 不可行（有公共根）；
并让"$\mathcal V_1$ 存在"取决于一个布尔条件 ✓ —— 则"层可行 ⟺ 该布尔为假" ✓。

## 做法

**构造尝试**：
1. 取 $n$ 小、$C$ 使 $\mathcal J$ 一维、$\rho=2$、$c=1$；
2. 让 $\mathcal U$ 的选择只有两个（例如 $\mathcal U$ 必须包含 $\beta(h)$ 且 $T$-不变，而 $T$ 只有两个 2 维不变子空间）；
3. 每个成员的 $\tau$ 只允许 1 个点（让 $\mathcal A$ 退化成一个点 ✓）。

## 进展

按上面的三步在 $n\le6$ 上试了 3 组 $(\alpha,\beta)$ 参数；**四步都卡住**（逐条见下节），
**没有**得到任何 hardness 结论 ✗。

## 卡在哪里（四点，逐条对应算式）

### 卡点 1：型层**不是**乘积集，无法独立设定"两个成员"

型层由 $(5a)$ 耦合 ✗：$\pi(\mathcal VA)\subseteq\pi(\mathcal V)$ 依赖 $\mathcal V$ 的**提升** ✓，
所以"$\mathcal V_0$ 与 $\mathcal V_1$ 同时满足 $(5a)$"不是一个可以分别安排的条件 ✗ ——
它们共享 $A$ 的作用 ✓，改一个往往破坏另一个 ✗。

### 卡点 2：$(5b)$ 是**开**条件，要"让它失败"必须精确打到闭集上

$(5b)$ 在型层上**泛型成立** ✓（实测：$\mathbb Q$ 上约 96% 的 $(\mathcal U,\mathcal H)$ 可行 ✓）。
所以"编码不可满足 = 让 $(5b)$ 失败"要求把参数**精确**推到 $\gcd$ 非常数的闭集上 ✗ ——
这类"精确命中"的构造对整数实例极不稳健 ✗（与 Löfberg 的 gadget 不同：那边用 Routh 行列式的**符号**，是开条件 ✓）。

### 卡点 3：要覆盖**整个型层**，不能只覆盖一个成员

层不可行 $\iff$ **每个** $(\mathcal U,\mathcal H)$ 都被覆盖 ✗。
而型层在 $\mathbb C$ 上是**正维数**的 ✓，覆盖要求 $A$ 与 $C$ 的结构使**所有**提升都失败 ✗ ——
这需要"全局"论证 ✗，而不是逐点安排 ✗。

### 卡点 4：底域问题

$\mathbb F_p$ 上可以做"精确覆盖"✓（见 [RCP §12](../../../proof/layer_program/RESTRICTED_COMPLETION_MODEL.md)：18 个候选全部不可行 ✓），
但**提升到 $\mathbb Q/\mathbb C$ 不成立** ✗（$\mathbb F_p$ 无解不推出 $\mathbb Q$ 无解 ✓，反方向才成立 ✓）。
所以 $\mathbb F_p$ 的构造**不能**直接用作归约 ✗。

## 放弃原因

本次具体构造失败：卡点 1（型层由 $(5a)$ 耦合、不是乘积集）与卡点 3（要求覆盖**正维数**的整个型层）
是结构性的，不是这次参数没选好 ✗。要继续这条线，必须先有"型层被完全覆盖"的判据（CQ），而它本身开放 ✗。

## 最终结论

$$\\boxed{\\ \\text{这次归约尝试失败；四个卡点里，卡点 1（型层非乘积）与卡点 3（正维数覆盖）是结构性的}\\ }$$

## 残留价值

1. 明确了"**为什么**这里的 hardness 比静态输出反馈难"：那边要一个开条件（符号），这边要一个**闭集命中 + 全局覆盖** ✗；
2. 明确了 $\mathbb F_p$ 构造**不能**提升 ✗ —— 这条限制了"先在有限域上设计 gadget"的做法 ✗；
3. 给出一个可检验的**必要条件**：任何 hardness 归约必须使"型层在 $\mathbb C$ 上被完全覆盖"✓，
   而这一点目前**没有任何已知判据** ✗（即专家 Q1 的 CQ ✗）—— 所以归约必须**顺带**解决 CQ ✗。

## 相关文件

- [09_hardness_blueprint.md](09_hardness_blueprint.md)（更早的蓝图）
- [../../proof/layer_program/RESTRICTED_COMPLETION_MODEL.md](../../../proof/layer_program/RESTRICTED_COMPLETION_MODEL.md)（RCP、CQ、$\mathbb F_p$ 数据）
- [../../proof/layer_program/STRATEGY_methods.md](../../../proof/layer_program/STRATEGY_methods.md)（方法清单）
- [../../archive/expert_correspondence/QA2_2026-10-30.md](../../../archive/expert_correspondence/QA2_2026-10-30.md)（专家意见）
