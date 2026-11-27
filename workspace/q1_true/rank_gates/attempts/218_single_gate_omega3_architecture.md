# 单门实现（三）：$\omega=3$、$q=4$ 的架构与实现方程

> 2026-11-09。217 的 $q\ge\omega+2$ 只对 $\omega=2$ 成立；$\omega\ge3$ 时 $q=\omega+1$ 有至少两行变量，
> 交空间可以固定 2 维。本文件给出 $\omega=3,q=4,k=5,c=2$ 的候选架构与实现方程。状态：**进行中（M2）**。

## 目标

构造单门的候选数据：固定 $A,C,L_0$，$H$ 的行含固定首行与变量行，
$R(X)=\operatorname{row}H$ 含固定 2 维子空间、第三方向随 $X$ 变，核 $\ker H$ 为图卡。

## 设想与理由

$\omega=3$：行空间 3 维，含固定 2 维 $S=\operatorname{span}\{h_0,h_{A,0}\}$，第三方向变量。
这样 $h_{A,0}\in S$ 不与 $h_0$ 平行，避免 217 的掉秩；核 = $R(X)^\perp$ 随第三方向变。

## 做法

### 1. 数据

$n=7$、$p=1$、$C=e_7^*$；$A$ 取移位链
$$e_1\mapsto e_6,\quad e_2\mapsto e_1,\quad e_3\mapsto e_2,\quad e_4\mapsto e_3,\quad e_5\mapsto e_4,\quad e_6\mapsto e_7.$$
则 $CA=e_6^*$、$K_0=\ker[e_7;e_6]=\operatorname{span}\{e_1,\dots,e_5\}$、$k=5$、$A(K_0)\not\subseteq K_0$（$e_1\mapsto e_6$）。
对 $h\in K_0^*$：
$$h_A=s\,e_1^*+h(e_1)e_2^*+h(e_2)e_3^*+h(e_3)e_4^*+h(e_4)e_5^*,$$
其中 $s$ 是提升在 $e_6$ 上的自由分量。

### 2. 行与行空间

取 $h_0=e_1^*$（$L_0=e_1$），$h_{A,0}=e_2^*$（取 $s=0$）。
取变量方向 $v(X)\in\operatorname{span}\{e_3,e_4,e_5\}$，行
$$r_1=e_2^*+a\,v,\qquad r_2=v,\qquad r_3=h_0+r_1,$$
$q=4$、$\operatorname{rank}H=3$、$R(X)=\operatorname{span}\{e_1^*,e_2^*,v\}$、核 $=R(X)^\perp$ 维 2。

### 3. 实现方程

$H_A=D H$ 要求每行 $h_{A,i}\in R(X)$：
- $h_{A,0}=e_2^*\in R$ ✓；
- $h_A(r_1)=h_A(e_2)+a h_A(v)=e_1^*+a h_A(v)$（对 $h=r_1$，$h(e_1)=0$）$\in R$；
- $h_A(r_2)=h_A(v)\in R$；
- $h_A(r_3)=h_{A,0}+h_A(r_1)\in R$。

所以核心方程是
$$\boxed{h_A(v)\in R(X)=\operatorname{span}\{e_1^*,e_2^*,v\},\qquad
e_1^*+a h_A(v)\in R(X).}$$
它们把 $v$ 的系数与 $a$（以及 $s$）耦合起来；这正是算术关系可以进入的地方。

### 4. 下一步

1. 解 $h_A(v)\in\operatorname{span}\{e_1,e_2,v\}$：写 $v=(0,0,\alpha,\beta,\gamma)$，
   $h_A(v)=s e_1+\alpha e_4+\beta e_5$（$h_A(e_3)=e_2$? 需按 $v$ 的坐标重算）；
2. 令 $h_A(v)=\mu e_1+\nu e_2+\rho v$，得到 $\alpha,\beta,\gamma$ 的方程；
3. 选一个方程形如 $z-xy=0$，并验证 soundness/completeness。


### 5. 移位 $A$ 的失败与修正

取 $v=\alpha e_3+\beta e_4+\gamma e_5$。由 $A$ 的移位，
$$h_A(v)=s e_1+\alpha e_4+\beta e_5.$$
$h_A(v)\in R=\operatorname{span}\{e_1,e_2,\alpha e_3+\beta e_4+\gamma e_5\}$ 迫使
$$\rho\alpha=0,\quad \rho\beta=\alpha,\quad \rho\gamma=\beta.$$
若 $\alpha\ne0$ 则 $\rho=0$，进而 $\alpha=\beta=0$，$v=\gamma e_5$（核固定）；
若 $\alpha=0,\beta\ne0$ 则 $\rho=0$，$\beta=0$（矛盾）。
所以**移位 $A$ 下 $h_A(v)\in R$ 强迫 $v$ 落在固定方向**，变量核不可能。

**修正方向**：$A$ 必须在变量的 2 维商空间上保持一个非平凡线性映射（而不是把变量方向移进固定方向），
使 $h_A(v)$ 是 $v$ 与固定向量的组合，从而 $R$ 可以随 $v$ 变。下一步：取 $A$ 在 $\operatorname{span}\{e_4,e_5\}$
上为 $2\times2$ 矩阵，泄漏放在另一方向。

## 进展

* 修正 217 的适用范围（$\omega=2$）；
* 给出 $\omega=3,q=4,k=5$ 的候选数据；
* 写出实现方程 $h_A(v)\in\operatorname{span}\{e_1,e_2,v\}$。

## 最终结论

* $\omega=3$ 的架构避开了 217 的掉秩；
* 单门实现归结为两条线性包含方程；
* 尚未解出 $v(X)$ 或编码 $z=xy$。

## 放弃原因

* 未解出具体 $v(X)$；
* 未验证 $D$ 的过滤/无特征向量；
* 未证 soundness/completeness。

## 残留价值

* $\omega=3$ 的可行架构；
* 明确的实现方程；
* 为下一轮符号求解提供靶子。

## 相关文件

* [attempts/217](../../multiplication_gate/attempts/217_single_gate_q_lower_bound.md)（$\omega=2$ 下界）
* [attempts/216](../../multiplication_gate/attempts/216_single_gate_normal_form.md)（正规形）
* [attempts/215](../../multiplication_gate/attempts/215_67_verdict_uniform_spectral.md)（uniform 谱）

## 状态

* 架构：**[M2]**。
* 单门解：**[未做]**。
