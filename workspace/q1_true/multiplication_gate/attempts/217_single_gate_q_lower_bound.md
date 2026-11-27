> **已撤回（专家 68/69 答复，见 [228](228_68_69_verdict.md) 与 [R22](../../../../proof/refuted/README.md)）**：
> $\omega=2,q=3$、固定 $L_0$ 的变量核**不是**不可能的；专家给出 $n=10$ 的显式族，
> 对所有 $t$ 可行（证书 [c228_omega2_family.py](../../../../tools/verification/c228_omega2_family.py)）。
> 本文件的“$q\ge\omega+2$”下界**不成立**；零行不使 $3\times k$ 秩 2 铅笔掉秩。

> **范围更正（218）**：本文件的结论只对 $\omega=2$、$q=3$（只有**一行**变量）成立。
> $\omega\ge3$、$q=\omega+1$ 时有 $\omega-1\ge2$ 行变量，交空间可以是 2 维，217 的论证不适用；
> 因此“$q\ge\omega+2$”不是一般下界，只是 $\omega=2$ 的下界。

# 单门实现（二）：$q=\omega+1$ 不足——固定 $L_0$ 的变量图卡需要 $q\ge\omega+2$

> 2026-11-09。在 216 的正规形上继续：$q=3$、$\omega=2$ 时，固定首行 $h_0$ 与变量行 $g(X)$
> 迫使 $h_{A,0}\in\operatorname{span}\{h_0\}$，从而 $P(\lambda_0)$ 掉秩。
> 所以单门实现至少需要 $q\ge\omega+2$。状态：**M2（结构性否定）**。

## 目标

判定 $q=\omega+1$（专家抽象机制中的尖锐值）能否承载固定 $L_0$ 的变量图卡。

## 设想与理由

216 的正规形：$H=C_0[h_0;g(X)]$，取 $q=3$、$\omega=2$，
$$C_0=\begin{bmatrix}1&0\\0&1\\1&1\end{bmatrix},\qquad
H\text{ 的行}=h_0,\ g(X),\ h_0+g(X).$$
$H_A=D H$ 迫使每一行 $h_{A,i}$ 都是 $H$ 的行的线性组合。

## 做法

### 1. 首行的约束

$h_{A,0}=L_0AN$ 是**固定**的（$L_0,A$ 固定）。由 $H_A=DH$，
$$h_{A,0}\in\operatorname{span}\{h_0,\ g(X),\ h_0+g(X)\}=\operatorname{span}\{h_0,g(X)\}$$
对**所有** $X$ 成立。

### 2. 变量图卡要求 $g(X)$ 离开 $\operatorname{span}h_0$

若 $\ker H=\ker h_0\cap\ker g(X)$ 要随 $X$ 变（图卡），$g(X)$ 必须在 $\operatorname{span}h_0$ 之外取值
（否则核固定）。于是
$$\bigcap_X\operatorname{span}\{h_0,g(X)\}=\operatorname{span}\{h_0\},$$
故 $h_{A,0}=\lambda_0 h_0$。

### 3. 掉秩

$h_{A,0}=\lambda_0 h_0$ 意味着 $H_A$ 的首行 $=\lambda_0 H$ 的首行，于是
$$P(\lambda_0)=\lambda_0 H-H_A$$
的首行为 $0$，$\operatorname{rank}P(\lambda_0)<\omega$，与 $(5b)$ 矛盾。

### 4. 结论

$$q=\omega+1,\ \text{固定 }L_0,\ \text{变量图卡}\ \Longrightarrow\ \text{不可行}.$$
即：专家的“$q=\omega+1$ 尖锐”只对**抽象谱机制**（首行可随 $X$ 变）成立；
固定 $L_0$ 的观测器实现需要至少**两行变量**，使 $h_{A,0}$ 落在固定交空间里而不与 $h_0$ 平行。

## 进展

* 证明了 $q=\omega+1$ 在固定 $L_0$ 下不能承载变量图卡；
* 明确了需要 $q\ge\omega+2$（至少两行变量，交空间维数 ≥2）；
* 修正了专家 $H=[I\ -X]$ 的 ansatz 与尖锐性结论的适用范围。

## 最终结论

* 单门实现的最小 $q$ 是 $\omega+2=4$（$c=2$）；
* 下一构造：$q=4$、$\omega=2$，两行变量 $g_1,g_2$，固定首行 $h_0$，
  要求 $h_{A,0}\in\operatorname{span}\{h_0,g_1,g_2\}$ 对所有 $X$ 且不与 $h_0$ 平行（交空间固定 2 维）。

## 放弃原因

* 未构造 $q=4$ 的实例；
* 未编码 $z=xy$；
* 未处理 $A(K_0)\cap K_0$ 的兼容关系。

## 残留价值

* 一个明确的下界 $q\ge\omega+2$；
* 修正了尖锐性结论的适用范围；
* 为 $q=4$ 构造指明“交空间固定 2 维”的条件。

## 相关文件

* [attempts/216](216_single_gate_normal_form.md)（正规形）
* [attempts/215](215_67_verdict_uniform_spectral.md)（$q=\omega+1$ 抽象机制）
* [attempts/201](201_pair_lift_theorem.md)（行对实现）

## 状态

* 否定：**[M2 纸面]**。
* $q=4$ 构造：**[未做]**。
