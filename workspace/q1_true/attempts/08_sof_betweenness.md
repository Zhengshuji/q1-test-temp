# 路线 9：从静态输出反馈的 NP-hardness 传递（Löfberg 2026）

## 目标

用 Löfberg (2026) 的 Betweenness 归约技巧，证明 $(k,1)$ 层的判定（或整个 $q_{\min}$）是 NP-hard。

## 设想与理由

Löfberg, *Static output-feedback stabilization is NP-hard*（arXiv:2609.16886, 2026-09）证明了：

$$\textbf{SOF1}(A,B,C):\ \exists K\in\mathbb R^{1\times n}:\ A+BKC\ \text{是 Hurwitz}\qquad\text{是 NP-hard}$$

（$B$ 单列、$D=6(m+n)$；归约自 **Betweenness**。技巧：一个"通用三次源多项式"的 **Routh 行列式**强制符号条件；
再用**频率分离**把所有源条件聚合成一个**对增益仿射**的多项式，最后实现为 $A+BKC$ 的特征多项式——因为 $B$ 单列时
$\det(sI-A-BKC)=\det(sI-A)-w^{\mathsf T}\mathrm{adj}(sI-A)B$ 对 $w=C^{\mathsf T}K^{\mathsf T}$ **仿射**。）

推论 3.3（by-product）：**"仿射参数化的有理多项式族是否含 Hurwitz 成员"** 是 NP-hard。

**与本项目的形状对应**：

| | 他们的 | 我们的（$(k,1)$ 层）|
|---|---|---|
| 未知量 | $K$（仿射进入）| $\tau$（仿射进入）|
| 条件 | 多项式族有 **Hurwitz 成员**（根在半平面）| 多项式族**无公根**（$\gcd=1$）|
| 逻辑形状 | $\exists$ 参数使某根条件成立 | $\exists\tau$ 使某根条件成立 |
| 条件类型 | 半代数**开**条件 | 半代数**开**条件（$m{=}2$ 时 $\operatorname{Res}\ne0$，即 $>0$ 或 $<0$）|

也就是说：**两个问题都是"∃ 参数使一个根条件成立"，且都是开条件**。所以他们的归约技术（Betweenness + 符号 + Routh + 频率分离 + anchor 逃逸机制）**原则上可迁移**。

## 做法（计划）

1. 把 $(k,1)$ 层的"无公根"条件改写成**符号条件**：$m{=}2$ 时 $\operatorname{Res}(p_1,p_2)\ne0$；$m\ge3$ 时需先把全组归约到一个 resultant 组合（或直接用 §17 的 Bézout 子式 $\Delta\ne0$）；
2. 造 Betweenness gadget，使"不满足 Betweenness"时**所有** $\tau$ 都让族有公根（即 $\mathrm{Bad}=\mathcal A$）——这正是 Löfberg 的 anchor/escape 机制做的事；
3. 检查自由度是否足够：他们的 $K$ 是 $n$ 个实变量（$1\times n$），我们的 $\tau$ 是 $kj$ 个实变量，且受 $(5a)$ 的仿射约束——**需要确认约束不破坏 gadget**。

## 进展

- 已读论文摘要、主定理、结论（§1、§7）与 Corollary 3.3；
- **未开始**造 gadget。

## 最终结论

**提出，未做**。若成功，$(k,1)$ 层 NP-hard ⟹ $q_{\min}$ NP-hard ⟹ **$q1$ = 真**。

## 放弃原因

不适用（未放弃）。

## 残留价值

- 论文本身是本项目**最重要的复杂度参照**：它证明"数值型控制问题也可以 NP-hard"，直接**否定了**本项目早先的启发式
  "NP-hard 只出现在结构型（0/1）问题里"；
- 它给出了一套可迁移的归约模板（Betweenness + 三次源 + Routh + 频率分离 + anchor）。

## 相关文件

- 论文全文：`literature/pdf/complexity/Lofberg_2026_SOF_stabilization_NP_hard.pdf`（文本抽取：`workspace/static_of.txt`）
- [../../proof/rho1_layer/theorem.md](../../../proof/rho1_layer/theorem.md)（§17–§20 的 Bézout / 子式判据）
- [../../q1_false/mainline_logic.md](../../q1_false/mainline_logic.md)