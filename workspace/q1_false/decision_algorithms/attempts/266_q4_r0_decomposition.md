# $q=4,r_0=2$ 的压缩分解：$(5a)$ = 固定行条件 + $RE\\in\\operatorname{row}H$

> 2026-11-09。为路线 A（固定行编码 ARM(3)）做代数准备。
> 把 $AN$ 分解为 $NM+E$（$N$ 的左逆 $N^+$，$E=(I-NN^+)AN$），则
> $$H=\\begin{bmatrix}H_0\\\\Y\\end{bmatrix},\\qquad
> H_A=\\begin{bmatrix}H_{A,0}\\\\YM+RE\\end{bmatrix},\\qquad Y=RN.$$
> 于是
> $$(5a)\\iff H_{A,0}\\in\\operatorname{row}H\\ \\text{且}\\ RE\\in\\operatorname{row}H.$$
> 状态：**M2（纸面）**。

## 目标

把 $q=4,r_0=2$ 的 $(5a)$ 分解成固定行/自由行两部分，判断能否编码 ARM 的仿射约束。

## 设想与理由

$H_0=L_0N$、$H_{A,0}=L_0AN$ 固定；$Y=RN$ 自由。
自由行的 $H_A$ 是 $YM+RE$：$YM\\in\\operatorname{row}Y\\subseteq\\operatorname{row}H$ 自动成立，
所以自由行只剩 $RE\\in\\operatorname{row}H$。

## 做法

### 1. 分解

取 $N^+$ 使 $N^+N=I_k$，令
$$M=N^+AN,\\qquad E=(I-NN^+)AN.$$
则 $AN=NM+E$、$N^+E=0$。对 $R$：
$$RN=Y,\\qquad RAN=YM+RE.$$
$(5a)\\iff\\operatorname{row}(H_A)\\subseteq\\operatorname{row}H$，即
$$H_{A,0}\\in\\operatorname{row}H,\\qquad YM+RE\\in\\operatorname{row}H.$$
而 $YM\\in\\operatorname{row}Y\\subseteq\\operatorname{row}H$，故
$$\\boxed{(5a)\\iff H_{A,0}\\in\\operatorname{row}H\\ \\text{且}\\ RE\\in\\operatorname{row}H.}$$

### 2. $E$ 的作用

- **$E=0$**（即 $A(K_0)\subseteq K_0$）：$RAN=YM\in\operatorname{row}Y$，
  自由行条件自动成立；$(5a)$ 只剩固定行 $H_{A,0}\in\operatorname{row}H$。
- **$E\ne0$**：$RE\in\operatorname{row}H$ 是**真正**的条件。
  注意 $R\mapsto(RN,RE)$ 不是满射到所有 $(Y,Z)$：它的像是一个线性子空间，
  所以 $Z=RE$ 不能独立于 $Y$ 选取；“吸收”不是自动的。
  编码窗口正是利用这个约束：设计 $E$，使 $RE\in\operatorname{row}H$ 等价于想要的方程。

### 3. 对 ARM 的含义

若要让 $(5a)$ 约束 $Y$（从而 $H$），必须让 $[N,E]$ 不满行秩；
此时 $R$ 的自由度被 $E$ 的秩限制，$(5a)$ 变成 $Y$ 上的方程。
ARM 的仿射约束能否这样编码，取决于 $E$ 的结构（由 $A$ 设计）。

## 进展

* $(5a)$ 的固定行/自由行分解；
* “$E$ 补足 $N$ ⇒ 吸收”的机制；
* 编码窗口：$[N,E]$ 不满行秩。

## 最终结论

* $q=4,r_0=2$ 的 $(5a)$ 可以写成“固定行包含 + $RE\\in\\operatorname{row}H$”；
* 自由行条件是 $RE\in\operatorname{row}H$；$E=0$ 时自动，$E\ne0$ 时是真条件；
* 路线 A 的关键是**设计 $E$**（即设计 $A$ 在 $K_0$ 外的分量），使这个条件编码目标方程。

## 放弃原因

* 未构造退化 $E$ 的具体编码；
* 未接 $(5b)$；
* 未处理 $r_0>2$。

## 残留价值

* 一个清晰的分解；
* 解释为什么“自由行吸收”反复出现；
* 明确路线 A 的设计条件。

## 相关文件

* [attempts/257](../../../q1_true/multiplication_gate/attempts/257_offset_absorption.md)
* [attempts/251](../../../q1_true/multiplication_gate/attempts/251_coupled_plane_obstruction.md)
* [路线 A 说明](../../../q1_true/arm_reduction/attempts/254_arm3_embedding.md)

## 状态

* 分解：**[M2 纸面]**。
* 退化 $E$ 构造：**[未做]**。
