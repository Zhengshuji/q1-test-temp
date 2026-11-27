# 单门实现（四）：$A(W)\subseteq S$ 架构与 $D$ 的零列障碍

> 2026-11-09。218 的移位 $A$ 失败后，试“变量方向经 $A$ 落入固定子空间 $S$”的架构。
> 结果：$h_A(v)\in S$ 使 $D$ 在变量方向上出现**零列**，$\lambda=0$ 掉秩；
> 若 $h_A(v)$ 含 $v$ 分量，又给出特征值。单门实现需要更长的变量链。状态：**M2（结构性障碍）**。

## 目标

构造 $A$ 使变量核变化、$h_A(v)$ 可控，同时 $D|_W$ 无特征向量。

## 设想与理由

取固定 $S=\operatorname{span}\{e_3,e_4\}$、变量 $W=\operatorname{span}\{e_1,e_2\}$，
$A(W)\subseteq S$、$A(S)\subseteq S$、泄漏 $e_6\mapsto e_5\mapsto e_7$。
则 $K_0=\operatorname{span}\{e_1,e_2,e_3,e_4,e_6\}$、$k=5$、$C=e_7$、$A(K_0)\not\subseteq K_0$（$e_6\mapsto e_5$）。
固定行 $h_0,h_1\in S^*$，变量 $v\in W^*$；$R=\operatorname{span}\{S^*,v\}$ 随 $v$ 变。

## 做法

### 1. $h_A(v)\in S^*$

$A v\in S$ ⇒ $h_A(v)=h(Av)\in S^*\subseteq R$ ✓。所以实现方程自动满足（对所有 $v$）。

### 2. $D$ 的零列

$H$ 的行含 $h_0,h_1,v,h_0+h_1$。$H_A$ 的行：
$h_A(h_0),h_A(h_1)\in S^*$，$h_A(v)\in S^*$，$h_A(h_0+h_1)\in S^*$。
所以 $H_A$ 的每一行都在 $S^*$ 中，**没有 $v$ 分量**。
在行坐标基 $(h_0,h_1,v,h_0+h_1)$ 下，$D$ 的“$v$ 列”为 $0$：
$$D\,w_v=0,\qquad w_v=(0,0,1,0)\in W.$$
于是 $\operatorname{rank}((0\cdot I-D)|_W)<\omega$，$\lambda=0$ 处掉秩。

### 3. 若 $h_A(v)$ 含 $v$ 分量

若 $h_A(v)=\lambda v+\text{(S)}$，则 $D$ 在 $v$ 方向上有对角元 $\lambda$，
$v$ 是特征向量 ⇒ 在 $\lambda$ 处掉秩。所以“$h_A(v)$ 落 $S$”与“$h_A(v)$ 含 $v$”都不行：
前者零列，后者特征值。

### 4. 需要的结构

要避免两者，变量方向必须形成**至少 2 步的链**：
$$v_1\mapsto v_2,\qquad v_2\mapsto g_{\rm out}+\cdots,$$
使 $D$ 在变量部分没有特征向量。但这需要 $W$ 中至少 2 个变量方向，
而固定行 $h_0,h_1$ 已占 2 维（$\omega=3$）。
若只留 1 个固定行，$h_{A,0}\in S$（1 维）⇒ 与 $h_0$ 平行 ⇒ 特征值。
所以 $\omega=3$ 的 $2+1$ 分解不够；需要 $\omega\ge4$（固定 2 维 + 变量链 2 维），或
固定部分不参与 $D$ 的不变结构（更复杂）。

## 进展

* 证明 $A(W)\subseteq S$ 架构下 $D$ 有零列，$\lambda=0$ 掉秩；
* 证明 $h_A(v)$ 含 $v$ 分量时出现特征值；
* 结论：变量部分需要至少 2 步链 ⇒ $\omega\ge4$（或非不变固定部分）。

## 最终结论

* 单门实现的最小 $\omega$ 可能是 4（$q\ge5$），而不是 3；
* 需要“固定 2 维 + 变量 2 步链”的 $W$ 分解；
* 这给出一个新的下界候选 $\omega\ge4$（待严格化）。

## 放弃原因

* 未构造 $\omega=4$ 的实例；
* 未证明 $\omega=3$ 完全不可能（只排除了两类 $h_A(v)$）；
* 未编码 $z=xy$。

## 残留价值

* 零列/特征值的两难；
* $\omega\ge4$ 的候选下界；
* 为下一轮 $\omega=4$ 架构指明“固定 2 + 变量 2 链”。

## 相关文件

* [attempts/218](../../rank_gates/attempts/218_single_gate_omega3_architecture.md)
* [attempts/217](217_single_gate_q_lower_bound.md)
* [attempts/215](215_67_verdict_uniform_spectral.md)

## 状态

* 障碍：**[M2]**。
* $\omega=4$ 构造：**[未做]**。
