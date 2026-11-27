> **282 更正**：$q=4,r_0=2,\omega=3$ 已被必要条件 $\omega\le r=q-r_0$ 排除（$r=2<3$）。
> 本文件的压缩门只能作为形式例子；Route A 需 $q\ge5$ 或 $r_0$ 更小。

> **77 号审计更正**：$\det\pi(Y)=0$ 只给 $\operatorname{rank}H\le3$；要 rank 恰好 3 需 $\pi(Y)\ne0$。
> chart $r_{11}=1$ 上非零自动；无限制等价应写 $\det=0$ 且 $\pi(Y)\ne0$。

# rank-one 截面的落地门：$(5b)$ 的 $\\operatorname{rank}H=3$ 给出 $2\\times2$ 行列式

> 2026-11-09。按 76 号建议研究 $\\mathcal V\\cap\\{\\operatorname{rank}\\le1\\}$。
> 在 $q=4$、$r_0=2$、$\\operatorname{rank}H_0=2$ 的 Case II 下，
> $$\\operatorname{rank}H=3\\iff \\operatorname{rank}\\pi(Y)=1,$$
> 其中 $\\pi:\\mathbb C^k\\to\\mathbb C^k/S_0$。取 $k=4$、$\\dim V=2$，$\\pi(Y)$ 是 $2\\times2$；
> 于是
> $$\\boxed{\\operatorname{rank}H=3\\iff \\det\\pi(Y)=0.}$$
> 若 $\\pi(Y)=\\begin{bmatrix}r_{11}&r_{12}\\\\r_{21}&r_{22}\\end{bmatrix}$，则
> $$\\det=0\\iff r_{11}r_{22}-r_{12}r_{21}=0,$$
> 在 chart $r_{11}=1$ 上就是 $r_{22}=r_{12}r_{21}$——**乘法门**。
> 状态：**M2（构造目标 + 精确等价）**。

## 目标

把 76 号的 rank-one 截面落成一个具体的 $2\\times2$ 行列式门。

## 设想与理由

$H=[H_0;Y]$，$H_0$ 秩 2、$S_0=\\operatorname{row}H_0$。
$\\operatorname{rank}H=3$ 当且仅当 $Y$ 在 $\\mathbb C^k/S_0$ 中的像是一维（一条线）。
$k=4$ 时 $\\dim V=2$，$\\pi(Y)$ 是 $2\\times2$，秩一 $\\iff\\det=0$。

## 做法

### 1. 压缩层构造

取 $H_0=\\begin{bmatrix}e_1\\\\e_2\\end{bmatrix}$（$S_0=\\operatorname{span}\\{e_1,e_2\\}$），
$V=\\operatorname{span}\\{e_3,e_4\\}$，$\\pi$ 取坐标 3、4。
令
$$Y=\\begin{bmatrix}
0&0&r_{11}&r_{12}\\\\
0&0&r_{21}&r_{22}
\\end{bmatrix},$$
则
$$\\pi(Y)=\\begin{bmatrix}r_{11}&r_{12}\\\\r_{21}&r_{22}\\end{bmatrix},\\qquad
\\operatorname{rank}H=3\\iff r_{11}r_{22}-r_{12}r_{21}=0.$$
chart $r_{11}=1$：$r_{22}=r_{12}r_{21}$，即 $z=xy$（$x=r_{12}$、$y=r_{21}$、$z=r_{22}$）。

### 2. $(5a)$ 的处理

若取 $E=0$（$A(K_0)\\subseteq K_0$），则自由行 $YM\\in\\operatorname{row}Y\\subseteq\\operatorname{row}H$ 自动；
固定行取 $H_{A,0}=0$（$L_0A\\in S$），则 $(5a)$ 自动成立。
但 $E=0$ 可能触发 205 的全局刚性（$(5a)$+$\\omega>0$ 不可行），所以还需检查 $(5b)$。

### 3. $(5b)$ 的 guard

$(5b)$ 要求 $\\operatorname{rank}P(\\lambda)=3$ 对所有 $\\lambda$，不只是 $\\operatorname{rank}H=3$。
$P=(\\lambda I-F)H$；需要 $\\operatorname{im}H$ 避开 $F$ 的特征空间。
这一步决定 chart $r_{11}\\ne0$ 与边界 $r_{11}=0$ 的分支选择。

## 进展

* rank-one 截面在 $k=4$ 时化为 $2\\times2$ 行列式；
* chart 下就是乘法；
* $(5a)$ 可通过 $E=0,H_{A,0}=0$ 自动满足（待 $E=0$ 的刚性检查）；
* 下一步是 $(5b)$ 的 guard 与 $A,C,L_0$ 的显式实现。

## 最终结论

* 76 号的 rank-one 截面确实能给出乘法门；
* 这是目前最具体的“非单行”门：乘法来自 $(5b)$ 的 $\\operatorname{rank}H=3$，不是 $(5a)$；
* 关键剩余：$E=0$ 的刚性、$(5b)$ 的谱 guard、边界 chart。

## 放弃原因

* 未构造 $A,C,L_0$ 的完整实例；
* 未验证 $(5b)$；
* 未处理 $r_{11}=0$ 边界。

## 残留价值

* 一个清晰的 $2\\times2$ 门目标；
* 把 $(5b)$ 的秩条件变成乘法；
* 与专家建议的 rank-one 截面对齐。

## 相关文件

* [attempts/272](../../../q1_true/rank_gates/attempts/272_76_verdict.md)
* [attempts/266](266_q4_r0_decomposition.md)
* [attempts/269](269_spectral_polarity.md)

## 状态

* 压缩层门：**[M2 纸面]**。
* 完整实例：**[未构造]**。
