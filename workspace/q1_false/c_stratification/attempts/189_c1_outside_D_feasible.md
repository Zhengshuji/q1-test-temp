# $c=1$、$W_L\not\subseteq D$：可容许条件真空，可行性化为铅笔条件

> 2026-11-08。188 证明 $Av\notin K_0$ 时每个 $h\in\operatorname{Ann}(v)$ 都有可容许提升。
> 本文件把它推到底：此时 $c=1$ 层的可容许条件对 $H$ 的行**没有任何限制**，
> 可行性只剩秩与铅笔条件。铅笔好性在自由参数上是开条件，但**可能结构恒坏**
> （例如顶部行全在同一特征值处消失），所以只能得到“一般可行，除非铅笔恒坏”。
> 状态：**M2（纸面）**。

## 目标

给出 $c=1$、$W_L\not\subseteq D$ 时的可行性结论：可容许条件真空，铅笔好性开稠密。

## 设想与理由

188 的构造：对任意 $h$，用 $g_0$ 把提升调成 $l\cdot Av=0$。因此：
- 每个 $h\in\operatorname{Ann}(v)$ 都可作为 $H$ 的一行（配上某个可容许提升）；
- 于是 $\operatorname{rank}H=\omega$ 只受“底部行要张满 $\operatorname{Ann}(V)/\operatorname{row}(H_0)$”的约束；
- 铅笔条件 $\operatorname{rank}(\lambda H-H_A)=\omega\ \forall\lambda$ 是子式 gcd 常数，是**开条件**（在 $H$ 的行与提升的自由参数上）。

## 做法

固定 $V=L=\mathbb Cv\subseteq W_L$，$Av\notin K_0$。

1. **可容许行**：由 188，$\{h\in\operatorname{Ann}(v)\}$ 中每个 $h$ 都有可容许提升。故 $H$ 的行可在
   $\operatorname{Ann}(v)$ 中任意选（只要秩条件）。
2. **秩条件**：$\operatorname{rank}H=\omega$。因 $\operatorname{Ann}(v)$ 是 $\omega$ 维、顶行 $H_0$ 秩 $\rho_0$，
   只需底部行在 $\operatorname{Ann}(v)/\operatorname{row}(H_0)$ 中的投影秩 $\omega-\rho_0$；这是开条件。
3. **铅笔条件**：$P(\lambda)=\lambda H-H_A$ 的 $\omega$ 阶子式 gcd 常数。在 $H$ 的行与提升的自由参数上，
   坏 locus 是“存在公共根”，是**真闭子集**（除非结构上恒坏）；故补集非空开。
4. **结论**：步骤 2、3 都是开条件；若交非空，则存在可容许的 $(H,H_A)$，
   再经提升层得 $L$。但**铅笔可能结构恒坏**：例如顶部行都在同一特征值 $\lambda_0$ 处消失时，
   $\lambda_0$ 处秩由底部行决定，可能恒 $<\omega$。所以只能得到“一般可行，除非铅笔恒坏”。

**反例（合成，更清楚）**：取 $L_0=[e_4;e_5;e_6]$、$Ae_3=e_1$（$v=e_3$，$Av\notin K_0$）。
可容许要求 $h\in\operatorname{Ann}(e_3)$，即 $l_3=0$（$h=lN$ 的 $e_3$ 系数为 $l_3$），且 $l_1=0$（$l\cdot Av=0$）。
在 $\lambda=1$ 处顶部行全消失（$Ae_4=e_4$、$Ae_5=2e_5$、$Ae_6=3e_6$ 时 $e_4$ 行消失，$e_5,e_6$ 行只剩 $e_5,e_6$ 方向），
底部值 $(I-A)l$ 在 $K_0$ 上只剩 $-l_5e_5-2l_6e_6$（$l_3=0$、$e_4$ 方向也消失），
所以 $P(1)$ 的秩 $\le2<3$，**恒坏**。这说明“可容许真空”不等于“可行”。

## 与 182 的对照

| 情形 | 可容许条件 | 结论 |
|---|---|---|
| $W_L\subseteq D$（$Av\in K_0$）| 强制 $h\cdot w=0$（超平面）| **不可行**（182/183）|
| $W_L\not\subseteq D$（$Av\notin K_0$）| 真空（188）| **一般可行**（本文件）|

所以 $c=1$ 层的二分法：$W_L\subseteq D$ 是唯一的结构性障碍；否则一般可行。

## 进展

* $c=1$ 层的二分法完成（$W_L\subseteq D$ 不可行；否则一般可行）；
* 182 的“不可行”与 188 的“真空”互补；
* 给出了 $W_L\not\subseteq D$ 时构造 $L$ 的路线（开条件 + 提升层）。

## 最终结论

* $c=1$、$W_L\not\subseteq D$：可容许条件真空，秩与铅笔条件开稠密，**一般可行**；
* 特殊实例可能铅笔恒坏，需具体检查；
* $W_L\subseteq D$ 是 $c=1$ 层唯一的系统性不可行机制。

## 放弃原因

* 未给出“铅笔恒坏”的显式判据；
* 未构造 $W_L\not\subseteq D$ 的具体实例做数值验证（$c=1$ 需要 $r\ge2$，构造较繁）；
* 未 Lean 化。

## 残留价值

* $c=1$ 层的完整图景；
* 为固定 $c$ 的算法提供“$W_L$ 检查 + 开条件搜索”的模板。

## 相关文件

* [attempts/182](182_c1_infeasibility_lemma.md)（$W_L\subseteq D$ 不可行）
* [attempts/188](188_c1_outside_D.md)（真空构造）
* [attempts/186](186_61_verdict_implementation.md)（专家 61 号的推广建议）

## 状态

* 二分法：**[已证-纸面，M2]**。
* 铅笔恒坏的判据 / 具体实例：**[未做]**。
