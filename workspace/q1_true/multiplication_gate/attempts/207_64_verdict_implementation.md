> **重要更正（2026-11-09，自查）**：本文件 §3 的“局部泄漏刚性”中，**“V 不变 ⇒ 铅笔秩降”这一步不成立**。
> 它需要全局 $A(K_0)\subseteq K_0$（才有 $H_A=HT$）；仅有 $A(V)\subseteq K_0$ 时，$lA$ 不是 $K_0$ 上的泛函。
> 反例：seed 10 的可行见证 $V=W_L$ 满足 $A(V)\subseteq K_0$（且 $A(V)\subseteq V$）、$\omega=2>0$，但 $(5a)(5b)$ 成立。
> 因此“可行正秩 ⇒ $A(V)\not\subseteq K_0$”是**假**的；专家的 §4/§5.1 结论需修正（见 [210](210_local_leakage_correction.md)）。
> 全局定理 $A(K_0)\subseteq K_0$、$0<\omega<k$ 仍成立。

# 专家 64 号裁决落实：刚性定理的边界更正与局部泄漏刚性

> 2026-11-09。专家确认 205 的证明在 $0<\omega<k$ 成立，但**更正**：$c>0$ 包含 $\omega=0$（$c=k$），
> 该边界可行（有反例）。并给出更强的**局部泄漏刚性**：只要 $A(V)\subseteq K_0$ 且 $\omega>0$，
> 可行 ⇒ $A(V)\subseteq V$，进而铅笔秩降。状态：**M2（记录 + 更正）**。

## 目标

落实 64 号的更正与强化，明确刚性定理的精确范围与硬度后果。

## 设想与理由

专家给出更干净的证明：$A(K_0)\subseteq K_0$ 时 $AN=NT$，故 $H_A=HT$，$P(\lambda)=H(\lambda I-T)$；
$V^\perp$ 是 $T^{\mathsf T}$-不变非零空间，含左特征向量 $l$；$yH=l$ ⇒ $yP=0$，秩降。
该论证需要 $\omega>0$（$V^\perp\ne0$）。

## 做法：更正与强化

### 1. 更正：定理范围是 $0<\omega<k$

$$\boxed{A(K_0)\subseteq K_0,\ 0<\omega<k\ \Longrightarrow\ \text{不可行}.}$$
等价地 $0<c<k$。$c=k$（$\omega=0$）必须单独处理。

**反例（专家给）**：$n=3$、$p=1$、$q=1$，
$$C=\begin{bmatrix}1&0&0\end{bmatrix},\quad
A=\begin{bmatrix}0&1&0\\1&0&0\\0&0&0\end{bmatrix},\quad
L=\begin{bmatrix}0&1&0\end{bmatrix}.$$
$K_0=\operatorname{span}\{e_3\}$、$A(K_0)=0\subseteq K_0$、$k=1$、$H=LN=0$、$\omega=0$、$c=1>0$；
$(5a)(5b)$ 都成立（$P=0$），且 $\operatorname{rank}[C;L]=2=p+q$，满足 $\mathsf P_{\rm ind}$。

### 2. $\omega=0$ 分支

$H=0$ ⇒ $L$ 的行在 $K_0^\perp=\operatorname{row}[C;CA]$ 中 ⇒ $L,LA\subseteq\operatorname{row}[C;CA]$，
$(5a)(5b)$ 自动成立；只需满足行独立约定与 $L_0$。$\mathsf P_{\rm ind}$ 下可用维数 $d_C$ 决定。

### 3. 局部泄漏刚性（更强）

**命题**：设 $V\subseteq K_0$、$\dim V=c$、$A(V)\subseteq K_0$、$\omega=k-c>0$。若观测器满足 $(5a)$，
则
$$A(V)\subseteq V.$$
*证明*：每行 $h_i=l_iN$ 零化 $V$ 且零化 $A(V)$（因 $Av\in K_0$ 且 $l_iAv=0$），故
$\operatorname{row}H\subseteq(V+AV)^\perp$，$\omega\le k-\dim(V+AV)$ ⇒ $\dim(V+AV)\le c$，而 $V\subseteq V+AV$，
故 $V+AV=V$。$\square$

再用 205 的铅笔论证：$V$ 不变、$\omega>0$ ⇒ $V^\perp$ 含左特征向量 ⇒ 秩降。所以
$$\boxed{\omega>0,\ (5a),(5b)\ \Longrightarrow\ A(V)\not\subseteq K_0.}$$
即：**可行的正秩观测器，其核 $V$ 必须真正“漏出” $K_0$**。

### 4. 泄漏的线性代数

写 $l=(h,g)\in K_0^*\oplus G^*$、$Av=A_Kv+A_Gv$（$A_Kv\in K_0$、$A_Gv\in G$）。则 $(5a)$ 为
$$h|_V=0,\qquad h(A_KV)+g(A_GV)=0.$$
令 $J_V:V\to G$、$J_V(v)=\pi_G(Av)$。对固定 $h$，可容许的 $g$ 需满足
$$g\circ J_V=-h\circ A_K|_V,$$
可解条件
$$h\circ A_K|_V\in\operatorname{im}J_V^*.$$
$J_V=0$ ⇔ $A(V)\subseteq K_0$（不可行，$\omega>0$）；$J_V\ne0$ 是可行的必要条件。

### 5. 对 gadget 的结论

- 63 号的乘法 gadget 用 $A_{31}+A_{32}X=0$（即 $A(V)\subseteq K_0$）⇒ 由局部刚性**不可行**；
- 加 $A_{31},A_{32}$ 但不能让 $A(V)\subseteq K_0$：必须 $J_V\ne0$；
- 专家建议：**放弃“不变子空间乘法 gadget”**，改做“泄漏 + 同时提升”的 gadget，初始目标 $c=2$（$c=1$ 的 $g$ 太自由，约束被吸收）；
- 第一个实验：$J_V\ne0$、至少两行独立、非平凡同时提升、铅笔好的显式证明。

## 进展

* 205 的范围更正（$\omega>0$；$\omega=0$ 反例）；
* 局部泄漏刚性（更强、更可用）；
* 泄漏的线性代数条件；
* gadget 路线的明确否定与替代方向。

## 最终结论

* 刚性定理：$A(K_0)\subseteq K_0$、$0<\omega<k$ ⇒ 不可行；$\omega=0$ 例外；
* 更强：可行正秩 ⇒ $A(V)\not\subseteq K_0$；
* 不变子空间 gadget 死；硬度需“泄漏 + 同时提升”，$c\ge2$。

## 放弃原因

* 未构造泄漏 gadget；
* 未把 $\omega=0$ 分支写进求解器/判定树（已记录，待实现）；
* 未 Lean 化 $H_A=HT$ 版本。

## 残留价值

* 精确的刚性定理与边界；
* 泄漏条件的显式公式；
* 明确的 gadget 方向。

## 相关文件

* [attempts/205](205_AinvK0_impossible.md)（被更正）
* [attempts/203](203_invariance_theorem.md)（局部版本更强）
* [attempts/200](200_multiplication_gadget.md)（gadget）
* [attempts/194](194_62_verdict_implementation.md)（上一轮裁决）

## 状态

* 更正/强化：**[完成，M2]**。
* 泄漏 gadget/$c=2$：**[未做]**。
