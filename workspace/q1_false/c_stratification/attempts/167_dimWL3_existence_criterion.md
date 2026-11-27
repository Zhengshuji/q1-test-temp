# $\dim W_L=c+1$ 的存在性判据：$\lambda_0$ 处的秩条件

> 2026-11-08。回答“$\dim W_L=3$ 的实例有没有理论支撑”：有。$r=1,k=4,c=2,q=3$ 时，
> $\dim W_L=3$ 等价于 $L_0N$ 是特征向量；可行性化为 $\lambda_0$ 处两个底部铅笔值的独立性，
> 后者是一个显式的秩条件。状态：**M2（纸面）**。

## 目标

给出 $r=1$、$k=4$、$c=2$、$q=3$、$\dim W_L=3$ 时 $q=3$ 可行的**必要/充分条件**，
从而把构造实例变成解线性方程，而不是试错。

## 设想与理由

$\dim W_L=k-\operatorname{rank}[L_0N;L_0AN]$。$\dim W_L=3$ $\iff$ 顶部块秩 1
$\iff$ $L_0AN=\lambda_0L_0N$（$L_0N\ne0$），即 $L_0N$ 是 $A$ 在 $K_0^*$ 上的特征向量（特征值 $\lambda_0$）。

在 $\lambda_0$ 处 $P(\lambda)$ 的顶部行 $(\lambda_0-\lambda_0)L_0N=0$ 消失。要保持
$\operatorname{rank}P(\lambda_0)=2=\omega$，需要两个底部行的铅笔值独立：
$$v_i=\lambda_0 h_i-H_{A,i}=l_i(\lambda_0I-A)N,\qquad i=1,2.$$

## 做法

### 参数化

$V\in\operatorname{Gr}(2,W_L)$；$\operatorname{Ann}(V)=\langle h_0,u_1\rangle$，$h_0=L_0N$。底部行
$h_i=a_ih_0+b_iu_1$；提升 $l_i=a_ip_0+b_ip_1+g_i$（$g_i\in\operatorname{row}[C;CA]$）。则
$$v_i=a_iP_0+b_iP_1+\Gamma_i,$$
其中
$$P_0=p_0(\lambda_0I-A)N=0,\qquad P_1=p_1(\lambda_0I-A)N=\lambda_0u_1-p_1AN,$$
$$\Gamma_i=g_i(\lambda_0I-A)N=-g_iAN\in W_\Gamma:=\operatorname{im}\Gamma,\qquad \Gamma(g)=gAN.$$
（$p_0$ 是 $h_0$ 的**特征向量**提升，故 $P_0=0$；$P_1$ 依赖 $u_1$ 的特解提升，但模 $W_\Gamma$ 良定义。）

于是
$$v_i=b_iP_1+w_i,\qquad w_i\in W_\Gamma.$$

### 判据

$\operatorname{rank}P(\lambda_0)=2$ $\iff$ $v_1,v_2$ 线性独立。

* **必要条件**：$\dim(W_\Gamma+\langle P_1\rangle)\ge2$。特别地 $W_\Gamma\ne0$ 且 $P_1\notin W_\Gamma$；
  若 $W_\Gamma=0$，则 $v_i=b_iP_1$ 全平行，$\lambda_0$ 处秩 $\le1$，**不可行**。
* **充分条件**：$W_\Gamma\ne0$ 且 $P_1\notin W_\Gamma$。取 $b_1=1,w_1=0$、$b_2=0,w_2\ne0$，
  则 $v_1=P_1$、$v_2=w_2$ 独立（$H$ 仍秩 2，因为 $h_1=h_0+u_1$ 与 $h_0$ 独立）。

**其它 $\lambda$**：$P(\lambda)$ 在 $\lambda\ne\lambda_0$ 处的秩由 $3\times k$ 铅笔的 $2\times2$ 子式 gcd 判定；
在 $W_\Gamma$ 的自由参数上，避开有限个坏 $\lambda$ 是开条件（有限并的补），故一般可满足。

### 构造配方

1. 选 $A,C,L_0$ 使 $L_0N$ 是特征向量（$\lambda_0$）、$\operatorname{rank}[C;CA]>\operatorname{rank}C$（$d_C\ge1$）、$CA^2N\ne0$（$W_\Gamma\ne0$）；
2. 选 $V\in\operatorname{Gr}(2,W_L)$ 与 $u_1$，检查 $P_1\notin W_\Gamma$；
3. 取 $b_1=1,w_1=0$、$b_2=0,w_2\ne0$，构造 $H,H_A$；
4. 在剩余自由参数上检验 $(5b)$（gcd），得到 $L$。

## 进展

* 得到 $\dim W_L=c+1$ 时的显式秩判据（$\lambda_0$ 处 $v_1,v_2$ 独立）；
* 必要条件 $W_\Gamma\ne0$、$d_C\ge1$；充分条件 $P_1\notin W_\Gamma$；
* 这把“构造 $\dim W_L=3$ 实例”变成解线性方程，而不是随机试。

## 最终结论

* $\dim W_L=3$ 的存在性有明确的理论判据：$d_C\ge1$、$W_\Gamma\ne0$、$\lambda_0$ 处 $P_1\notin W_\Gamma$；
* 若这些成立，构造是线性的；若不成立，该参数下不可行；
* 这回答了“有没有理论支撑”：有，而且是可判定的秩条件。

## 放弃原因

* 未实际构造出一个满足 $P_1\notin W_\Gamma$ 的 $(A,C,L_0)$（下一步）；
* 未处理 $q>3$ 或 $r>1$；
* 未证明 $P_1\notin W_\Gamma$ 在一般 $(A,C,L_0)$ 下可达（只给了条件）。

## 残留价值

* 把 $\dim W_L>c$ 的构造从“试错”变成“判据 + 线性方程”；
* 与 165/166 的 $b$-判据互补：那里是 $b$ 被强制 0，这里是 $\lambda_0$ 处需要 $W_\Gamma$ 提供独立方向。

## 相关文件

* [attempts/165](165_c2_forced_plane_criterion.md)（forced 情形）
* [attempts/166](../../decision_algorithms/attempts/166_c2_general_algorithm.md)（一般算法）
* [attempts/152](152_lift_completion_fixed_l0.md)（$\Gamma$、$d_C$）

## 状态

* 判据：**[已证-纸面，M2]**。
* 实例构造：**[已完成，见 168]**（$n=6$ 见证，七条检查通过）。
