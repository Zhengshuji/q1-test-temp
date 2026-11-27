# (5a) 门（三）：$(5a)$ 不能强制秩一，$(5b)$ 可以——通道更正

> 2026-11-09。229/230 的门都放在 $(5a)$，失败。本文件给出结构性原因：
> “无秩增”条件 $(5a)$ 对门块的秩是**单调**的，不能强制秩一（$z=xy$）；
> 正确的通道是 $(5b)$ 的**固定秩 $\omega$**：用 $\omega-1$ 个 guard 行 + 2 个门行，
> 使 $\operatorname{rank}P=(\omega-1)+\operatorname{rank}G$，于是秩 $\omega$ 当且仅当 $\operatorname{rank}G=1$。
> 状态：**M2（结构性论证）**。

## 目标

确定门应放在 $(5a)$ 还是 $(5b)$，并给出正确的块结构。

## 设想与理由

### 1. $(5a)$ 的单调性

$(5a)$ 等价于 $\operatorname{row}(LA)\subseteq\operatorname{row}[L;CA;C]$，即“加行不增秩”。
设门块 $G=\begin{bmatrix}1&x\\ y&z\end{bmatrix}$ 是 $[L;CA;C]$ 的子块，且 $LA$ 提供一行 $w$。
在门坐标中，$\operatorname{rank}[G;w]-\operatorname{rank}G$：
- 若 $G$ 满秩（$z\ne xy$），行空间是整个 $\mathbb C^2$，任何 $w$ 都依赖 ⇒ 差为 $0$；
- 若 $G$ 秩一（$z=xy$），$w$ 可能独立 ⇒ 差可为 $1$。

所以“差为 $0$”在满秩时**自动成立**；若在秩一时也成立，则无法用“差为 $0$”区分两者。
要让它只在秩一时成立，需要 $w$ 在秩一时依赖、在满秩时独立——但满秩的行空间包含秩一时的行空间极限，
不可能。故 $(5a)$（无秩增）**不能**把 $z=xy$ 作为充要条件。

### 2. $(5b)$ 的固定秩

$(5b)$ 是 $\operatorname{rank}P(\lambda)=\omega$（固定值），不是“无增”。
取 $q=\omega+1$ 行：
- $\omega-1$ 个 guard 行，在 $\lambda$ 上恒独立；
- 2 个门行，其模 guard 的像张成 2 维当且仅当 $\det G\ne0$，张成 1 维当且仅当 $\det G=0$。

则
$$\operatorname{rank}P(\lambda)=(\omega-1)+\operatorname{rank}_{\rm mod\ guard}(G).$$
于是
$$\operatorname{rank}P=\omega\iff \operatorname{rank}G=1\iff z=xy.$$
这正是需要的方向：满秩（$z\ne xy$）给 $\omega+1$，违反 $(5b)$；秩一给 $\omega$，通过。

## 做法：目标块结构

1. $q=\omega+1$，$P$ 分为 $(\omega-1)$ 个 guard 行 + 2 个门行；
2. guard 用固定移位链（215 的单位子式）保证 $\omega-1$ 行恒独立；
3. 门行的 $P$ 像在 guard 的商空间中恰为 $G=\begin{bmatrix}1&x\\ y&z\end{bmatrix}$（或其行变换）；
4. $(5b)$ 强制 $\det G=0$，即 $z=xy$；
5. 门行的 $h\ne0$ 以保证 $\operatorname{rank}H=\omega$（门行也参与 H 的秩）。

## 进展

* 证明 $(5a)$ 的“无秩增”不能强制秩一（单调性）；
* 给出 $(5b)$ 的正确块结构：$(\omega-1)$ guard + 2 gate，秩 $=(\omega-1)+\operatorname{rank}G$；
* 明确门应在 $(5b)$，与专家 68/69 的“$(5a)$ 门”建议不同。

## 最终结论

* 门通道应是 $(5b)$ 的固定秩，而不是 $(5a)$ 的无秩增；
* 下一步：把 $G$ 实现为两个门行在 guard 商空间中的像，并保证 $\operatorname{rank}H=\omega$；
* 这需要 $H_A=D H$ 的 $D$ 在门行上给出 $G$，而 guard 部分保持移位链。

## 放弃原因

* 未构造具体的 $A,C,L_0$ 实现 $G$；
* 未证 soundness；
* 未接 10 维谱守卫。

## 残留价值

* 通道更正（$(5a)\to(5b)$）；
* 一个清晰的块秩公式；
* 为下一轮构造提供精确目标。

## 相关文件

* [attempts/229](229_gate_seed.md)、[230](230_proportionality_gate.md)
* [attempts/215](215_67_verdict_uniform_spectral.md)（guard）
* [for_expert 68/69 answer](../../../for_expert/archive/68_69-answer.md)

## 状态

* 通道论证：**[M2]**。
* 具体实现：**[未做]**。
