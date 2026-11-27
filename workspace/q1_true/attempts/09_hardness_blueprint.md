# 路线 10：硬度归约的**精确目标**（blueprint）

> 2026-10-29。本文件不是证明，而是把"要证 $q1$ = 真"所需的归约写成可检验的目标。

## 目标

给出一个多项式时间归约，把某个已知难问题（$\exists\mathbb R$-完全 或 NP-完全）映射到某个层的判定上，
从而证明 $q1$ = 真。

## 设想与理由

$c=1$ 时（任意 $\rho\ge2$），**固定** $(\mathcal U,\mathcal H)$ 之后：

$$\text{可行}\iff \mathcal A\not\subseteq\mathrm{Bad},\qquad
\mathrm{Bad}=\{\tau\in\mathcal A:\ \exists\lambda:\ \operatorname{rank}R(\tau,\lambda)\le\rho-1\}$$

（$R(\tau,\lambda)$ 是 $(\rho+1)\times d$ 的铅笔行矩阵。）于是

$$\text{层判定}=\exists(\mathcal U,\mathcal H):\ \mathcal A_{(\mathcal U,\mathcal H)}\not\subseteq \pi_\tau\{\operatorname{rank}\le\rho-1\}$$

- $\rho=2$：容器唯一 ⟹ $\mathrm{Bad}$ 仿射 ⟹ 全程线性代数 ✓（定理 9.10/10.1）；
- $\rho\ge3$：$\mathrm{Bad}$ 是**投影**（$\forall\tau\exists\lambda$）⟹ 硬度可能的入口。

## 做法

两个可选形式：

- **形式 A（$\exists\mathbb R$-难）**：多项式时间映射 $\varphi:\{\exists\mathbb R\text{-完全问题}\}\to(A,C,L_0,\rho,c)$，
  使"可满足 $\iff$ 第 $(\rho,c)$ 层可行"；
- **形式 B（NP-难）**：同上，改用 Betweenness / 3-SAT 等；
- **形式 C（条件性）**：证明"若存在多项式时间的 $\mathrm{Bad}$-成员测试（一般 Grassmannian），则 $q1$ = 假"。

参考 [Löfberg 2026 的 gadget 清单](../../../literature/notes/LOFBERG_2026_GADGETS.md)：

| gadget | 我们的对应物 | 障碍 |
|---|---|---|
| G1 消去型源多项式（Routh 行列式化为 $Nuv-1$）| 我们的行由 $A$ 决定、不能自由设计 | **主要障碍** |
| G2 锚点（把参数关进盒子）| 可用 $L_0$ 与 $C$ 的部分结构 | 待设计 |
| G3 定量裕度 | 整数实例的常数间隔 | 待设计 |
| G4 频率分离（AND ⟹ 一个多项式）| 我们的 $\gcd$ 判据天然是 AND | **可对接** |
| G5 一阶截断（仿射）| 我们的 $\tau$ 本来就仿射 | **可对接** |
| G6 全局缺陷（不可满足 ⟹ 全参数被抓）| 需要"不可满足 ⟹ $\mathrm{Bad}=\mathcal A$" | **最难** |

## 进展

**未做**形式 A/B/C 中任何一个 ✗。已完成的相邻工作：

- $\tau$ 量词消除（T11）✓；
- 固定 $(\mathcal U,\mathcal H)$ 的 $O(n^3)$ 判定（定理 29.1）✓；
- 可判定性（§30）✓；
- 已排除的捷径：所有**秩型不变量**判据 ✗（[S1_dimension_route_dead](../../q1_false/S1_dimension_route_dead.md)）。

## 最终结论

**蓝图阶段，无结论**。

## 放弃原因

不适用（未放弃），但已知三大障碍：

1. **自由度不匹配**：Löfberg 的 $K$ 有 $n$ 个自由实数；我们的 $\tau$ 只有 $\rho j$ 个，且行被 $(5a)$ 绑住；
2. **$\mathrm{Bad}$ 不可设计**：它由 $A$ 与 $\mathcal V$ 决定，而 gadget 需要逐条构造多项式；
3. **第二层量词**：固定 $(\mathcal U,\mathcal H)$ 的 gadget 之外，还要它在 Grassmannian 上出现。

## 残留价值

- 把 "$q1$ = 真" 的**最低要求**写成形式 A/B/C，任何后续归约都可对照；
- 明确了"$\rho=2$ 不可能 hard"（容器唯一 ⟹ 线性代数）⟹ 硬度必须从 $\rho\ge3$ 或 $c\ge2$ 来；
- gadget 对照表直接指出哪两个 gadget 可对接、哪一个是主要障碍。

## 相关文件

- [proof/rho1_layer/theorem.md](../../../proof/rho1_layer/theorem.md) §28–§30
- [TECHNICAL_REPORT](../../../archive/paper_drafts/TECHNICAL_REPORT_2026-10-29.md)
- [LOFBERG_2026_GADGETS](../../../literature/notes/LOFBERG_2026_GADGETS.md)
- [S1_dimension_route_dead](../../q1_false/S1_dimension_route_dead.md)
