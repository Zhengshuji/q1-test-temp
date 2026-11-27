> **311 更正**：303C 的 sound 表述是 $\exists R\iff x\ne0$，不是“对所有 $R$，$(5b)\iff x\ne0$”。

# 80 号审计更正：303 的乘法门只是“实现”，不是 sound q1 gadget

> 2026-11-10。80 号指出一个关键区分：
> **full-observer realization**（给定压缩对被某个 $R$ 实现）不等于 **sound q1 gadget**
> （对**所有**可行 $R$，解码关系都成立）。
> 303 的乘法门属于前者，不是后者：取 $R=0$ 即可绕过 $z=xy$，而 $(5a)(5b)$ 仍成立。
> 状态：**M3 更正**；303 的“完整乘法门”降级为“实现 + 指定见证下精确”。

## 目标

按 80 号审计更正 303/297/299/300 的 soundness 结论。

## 设想与理由

80 号给出 $R=0$ 反例；先确认它推翻的是 soundness 而非 realization。

## 做法：反例与逐条更正

### 1. 303 乘法门的 soundness 反例

303 的固定行：
$$H_0=\begin{bmatrix}e\\e\end{bmatrix},\qquad
H_{A,0}=\begin{bmatrix}0\\e\end{bmatrix},\qquad e=(1,0,0).$$
取自由行
$$R=0.$$
则
$$H=\begin{bmatrix}e\\e\\0\\0\end{bmatrix},\qquad
H_A=\begin{bmatrix}0\\e\\0\\0\end{bmatrix},\qquad
P(\lambda)=\begin{bmatrix}\lambda e\\(\lambda-1)e\\0\\0\end{bmatrix}.$$
$(5a)$ 成立；$P$ 的前两行中 $\\lambda$ 与 $\\lambda-1$ 不同时为零，故 $\\operatorname{rank}P=1=\\operatorname{rank}H$ 对所有 $\\lambda$。
所以该实例可行，但对 $x,y,z$ **没有任何条件**。
故 303 的乘法门不是 sound q1 gadget；它只在“$H_3=v_x,H_4=0$”等指定自由行下给出 $z=xy$。

### 2. 296 仍是 sound 的

296：$q=2,k=1$，$H_0=1$，$H_{A,0}=0$，自由行 $R=(r_1,r_2,r_3)$：
$$H=\begin{bmatrix}1\\r_1\end{bmatrix},\qquad
H_A=\begin{bmatrix}0\\r_2\end{bmatrix}.$$
$\\operatorname{row}H=\\mathbb C^1$，$(5a)$ 对所有 $R$ 自动成立。
$$P(\lambda)=\begin{bmatrix}\lambda\\\\ \\lambda r_1-r_2\end{bmatrix};$$
$\\lambda\\ne0$ 时秩 1；$\\lambda=0$ 时秩 1 当且仅当 $r_2\\ne0$。所以
$$(5b)\\iff r_2\\ne0,$$
且对**所有** $R$ 成立。296 是 sound 的非零 gadget。

### 3. 303 C 输入非零门仍是 sound 的

$H=(1,u)$、$H_A=(0,xv)$，$R=(u,v,w)$ 任意：
$P(0)=(0,-xv)$，秩 1 当且仅当 $xv\\ne0$；$\\lambda\\ne0$ 时第一分量 $\\lambda$ 非零，秩自动 1。
所以
$$\\exists R:(5a)\\wedge(5b)\\iff x\\ne0,$$
不受 $R$ 的其它分量影响。这是 sound 的。

### 4. 297 直和 unsound

297 的 $H$ 有零自由行；无限制的 $R$ 可以把这些零行变成非零，扩大 $\\operatorname{row}H$，使两个块的铅笔同时自动满足。
80 号给出的 $J$ 型 offset 就是这种交叉项。故 297 的“直和 = 合取”只对显示的块对角压缩矩阵成立，**不是** q1 实例的合取。

### 5. 299/300 只是压缩关系

299/300 的 $H,H_A$ 也含零行/自由行；同样需要 soundness 分析，不能直接称为 q1 门。

## 80 号对 305 的回答

- 列重合的逐行限制**不是**根本障碍：$(5a)$ 是全局行空间条件，允许跨行混合；
- 移位构造
  $$H=\begin{bmatrix}1&0\\0&1\\0&0\end{bmatrix},\quad
  H_A=\begin{bmatrix}0&0\\1&0\\0&1\end{bmatrix}$$
  满足 $(5a)(5b)$，且 $H_3=0$、$(H_A)_3=H_2$，是跨行转移；
- 但“可行”不等于“强制”：wiring gadget 必须让期望依赖在**每个**可行 $R$ 中出现。

### 更好的表示：射影线

80 号建议用射影线而不是标量复制：
$$(1,x,0),\ (0,1,y),\ (1,0,-z),$$
$$c\in\\operatorname{span}\\{a,b\\}\\iff z=xy.$$
固定坐标置换 $(u,v,w)\\mapsto(v,u,-w)$ 把输出 $(1,0,-z)$ 变成下一门的输入格式 $(0,1,z)$。
这是压缩层的几何原语；是否 sound 仍需证明。

### 双门串联的压缩构造（80 号）

在 $\\mathbb R^4$ 中
$$a_1=e_1+x_1e_2,\\ b_1=e_2+y_1e_3,\\ a_2=e_4+x_2e_1,\\ c_1=e_1-z_1e_3,\\ c_2=e_4+z_2e_3,$$
$$W=\\operatorname{span}\\{a_1,b_1,a_2\\}.$$
则
$$c_1\\in W\\iff z_1=x_1y_1,\\qquad
c_2\\in W\\iff z_2=x_2z_1.$$
用
$$H=[a_1;b_1;a_2;0;0;0],\\quad
H_A=[0;a_1;b_1;a_2;c_1;c_2]$$
可得 $\\operatorname{rank}H=3$、$\\operatorname{rank}P=3$ 对所有 $\\lambda$。
但零行自由时，$c_1,c_2$ 可被提升为 $H$ 的生成元，两个乘积自动成立；
80 号给出显式假赋值（$x_1=y_1=x_2=0,z_1=1,z_2=2$ 等）使实例可行。故这仍是**压缩构造**，不是 sound q1 串联。

## 更正后的结论

1. **sound q1 gate**：296（非零）、303 C（输入非零）；
2. **full realization but not sound**：303 B 乘法门、297 直和、299/300 压缩块；
3. **wiring 不是行复制问题**：射影线 + 全局行空间是更好的方向；
4. **真正缺失**：全局 incidence realization theorem——
   固定 $A,C,L_0$，使**每个**可行 $R$（包括额外非零行、跨块分量）都解码为源电路的解。

## 进展

* 一个关键的 soundness 反例；
* 296/303C 与 303B 的区分；
* 80 号的射影线/双门压缩构造；
* 明确下一目标是全局 incidence realization，而不是标量 copy。

## 最终结论

* “门库完整”应改为“有两个 sound 门 + 若干实现/压缩构造”；
* 乘法与 wiring 的 soundness 仍未解决；
* 不应声称 $\exists\mathbb R$-hardness。

## 放弃原因

* 未构造 sound 乘法门；
* 未证明全局 incidence realization；
* 未接归约。

## 残留价值

* 一个反例；
* 正确的 sound/realization 区分；
* 射影线的方向。

## 相关文件

* [80 答复](../../../for_expert/archive/80_wiring_copy_gadget-answer.md)
* [attempts/303](../../../q1_false/decision_algorithms/attempts/303_79_verdict_lifts.md)
* [attempts/296](296_nonzero_gadget_observer.md)

## 状态

* 更正：**[M3]**。
* sound 乘法门：**[未解决]**。
