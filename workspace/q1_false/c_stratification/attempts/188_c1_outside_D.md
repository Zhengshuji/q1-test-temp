# $c=1$ 引理在 $W_L\not\subseteq D$ 时的边界：机制失效

> 2026-11-08。专家 61 号建议把 $c=1$ 超平面引理推广到 $W_L\not\subseteq D$（$Av\notin K_0$）。
> 本文件证明：**推广不成立**——当 $Av\notin K_0$ 时，可容许条件不再强制秩降；
> 必须改用铅笔/提升条件。状态：**M2（纸面）**。

## 目标

判断 $c=1$ 的超平面机制在 $W_L\not\subseteq D$ 时是否仍然给出不可行性。

## 设想与理由

182 的关键步骤是 $l_i(Av)=h_i\cdot w$，它要求 $Av=Nw\in K_0$。若 $Av\notin K_0$，
$l_i(Av)$ 不由 $h_i=l_iN$ 决定；但可容许条件仍是 $l_i\cdot Av=0$。利用 $g\in\operatorname{row}[C;CA]$
的自由度（$gN=0$），可以调整 $l_i\cdot Av$。

## 做法

设 $v\in W_L$、$Av\notin K_0$。因为 $K_0=\operatorname{row}[C;CA]^\perp$，存在
$g_0\in\operatorname{row}[C;CA]$ 使 $g_0\cdot Av\ne0$（否则 $Av$ 与 $\operatorname{row}[C;CA]$ 正交，即 $Av\in K_0$，矛盾）。

固定任意 $h\in\operatorname{Ann}(v)$，取一个提升 $l_0$（$l_0N=h$）。令
$$l=l_0-\frac{l_0\cdot Av}{g_0\cdot Av}\,g_0.$$
则
$$lN=l_0N-\frac{l_0\cdot Av}{g_0\cdot Av}\,g_0N=h-0=h,\qquad
l\cdot Av=l_0\cdot Av-\frac{l_0\cdot Av}{g_0\cdot Av}\,(g_0\cdot Av)=0.$$
所以**每个** $h\in\operatorname{Ann}(v)$ 都有满足可容许条件的提升。于是：
- 可容许条件对 $h$ 的秩**没有**任何限制；$\operatorname{rank}H=\omega$ 可能；
- 182 的“所有行落在 $(\omega-1)$ 维超平面”结论**失效**。

**结论**：$W_L\subseteq D$ 是 182 的本质假设；$Av\notin K_0$ 时不能靠可容许条件推出不可行，
必须检查铅笔 $\operatorname{rank}(\lambda H-H_A)=\omega$ 与提升条件。

## 对一般 $c$ 的启示

同样的计算对任意 $\omega$ 成立：若 $Av\notin K_0$，则每个 $h\in\operatorname{Ann}(v)$ 都可提升为可容许行，
超平面机制消失。所以：
- **$W_L\subseteq D$** 的 $c=1$ 层：182/183 的不可行性成立；
- **$W_L\not\subseteq D$**：需要新的机制（铅笔、提升、$B_{u,v}$ 秩层），不能沿用超平面论证。

## 进展

* 证明了 $W_L\subseteq D$ 是 182 的本质条件；
* 给出了“每个 $h$ 都可容许提升”的显式构造；
* 明确了 $W_L\not\subseteq D$ 时下一步应查铅笔/提升，而不是继续找超平面。

## 最终结论

* $c=1$ 超平面引理**不能**推广到 $W_L\not\subseteq D$；
* 这不是证明“可行”，只是证明该机制失效；
* $W_L\not\subseteq D$ 的 $c=1$ 层仍是开放的计算/证明问题。

## 放弃原因

* 未给出 $W_L\not\subseteq D$ 时的替代判据（铅笔/提升的具体秩条件）；
* 未构造 $W_L\not\subseteq D$ 的实例做数值检验；
* 未 Lean 化。

## 残留价值

* 明确了 182 的适用边界；
* 一个可复用的“用 $g_0$ 调 $l\cdot Av$”技巧；
* 为 $W_L\not\subseteq D$ 的后续工作指明方向。

## 相关文件

* [attempts/182](182_c1_infeasibility_lemma.md)（$W_L\subseteq D$ 的引理）
* [attempts/183](183_c1_eigenlines.md)（特征线）
* [attempts/186](186_61_verdict_implementation.md)（专家 61 号的推广建议）

## 状态

* 边界结果：**[已证-纸面，M2]**。
* $W_L\not\subseteq D$ 的替代判据：**[未做]**。
