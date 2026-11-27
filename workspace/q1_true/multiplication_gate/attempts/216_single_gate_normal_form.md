# 单门实现（一）：固定 $L_0$ 下的正确正规形 $H=C_0[h_0;g(X)]$

> 2026-11-09。按专家 67 号优先级 2，开始单门实现。第一个发现：专家的图卡 $H(X)=[I\ -X]$
> 与**固定** $L_0$ 冲突（$H$ 的第一行是 $L_0N$，不能随 $X$ 变）。正确正规形是
> $H(X)=C_0\begin{bmatrix}h_0\\g(X)\end{bmatrix}$：固定 $C_0$、固定首行 $h_0$、变量在 $g(X)$。
> 状态：**M2（结构分析）**，尚无 gadget。

## 目标

把“图卡 + 固定像 + 固定谱”落到固定 $L_0$ 的观测器数据上，找出可实现的正规形。

## 设想与理由

专家的 uniform 机制要求 $\operatorname{im}H(X)=W$ 固定、$H_A(X)=D(X)H(X)$。
但 $H=LN$ 的第一行是 $H_0=L_0N$，由输入固定，**不能**是 $[I\ -X]$ 的变量首行。
所以变量只能进入其余行；同时像 $W$ 要固定。

## 做法

### 1. 正规形

取固定单射 $C_0:\mathbb C^\omega\to\mathbb C^q$，固定首行 $h_0=L_0N\in K_0^*$，变量 $g(X)\in K_0^*$：
$$H(X)=C_0\begin{bmatrix}h_0\\g(X)\end{bmatrix}.$$
则：
- $\operatorname{im}H(X)=\operatorname{im}C_0=W$ **固定**；
- $\operatorname{rank}H=\omega$ 当 $g(X)\notin\operatorname{span}h_0$；
- $\ker H(X)=\ker h_0\cap\ker g(X)$，随 $g(X)$ 变；
- 首行 $H_0$ 固定 ✓。

这正是“固定像 + 变量核 + 固定首行”的正确分解；$H=[I\ -X]$ 是 $L_0$ 不固定时的特例。

### 2. 谱层

取基 $w_0,\dots,w_{\omega-1}$ 张成 $W$，过滤链
$$D(X)w_j=w_{j+1}+\sum_{i\le j}a_{ij}(X)w_i,\qquad
D(X)w_{\omega-1}=g_{\rm out}+\sum_i a_{i,\omega-1}(X)w_i.$$
由 215 的单位子式，$\operatorname{rank}((\lambda I-D)|_W)=\omega$ 对所有 $X,\lambda$。
令 $H_A(X)=D(X)H(X)$。

### 3. 实现层

需要逐行 $l_i(X)$：
$$l_i(X)N=H_i(X),\qquad l_i(X)AN=H_{A,i}(X).$$
第一行 $l_1=L_0$ 固定；其余行由 $g(X)$ 与 $D(X)$ 决定。
兼容关系：若 $Av\in K_0$，则 $h_{A,i}(v)=h_i(Av)$。若 $A(K_0)\cap K_0=0$，则无兼容约束，
但 $A(K_0)$ 的维数/像会限制 $h_A$ 的形状（见 216 的下一步实验）。

### 4. 与 $H=[I\ -X]$ 的差别

专家图卡要求首行随 $X$ 变（$[1,0,-X_{11},-X_{12}]$），与固定 $L_0$ 矛盾。
正规形把变量放到 **$g(X)$ 一行**，图卡核变成 $\ker h_0\cap\ker g(X)$：
- 若 $h_0$ 选得好（如 $h_0=e_1^*$），$\ker h_0$ 是固定的 $(k-1)$ 维空间；
- $g(X)$ 在该空间上再切出 $c$ 维核，$X$ 可以编码算术关系。

## 进展

* 找到了固定 $L_0$ 下的正确正规形；
* 明确了变量只能进入 $g(X)$，像固定由 $C_0$ 保证；
* 实现层与谱层分离。

## 最终结论

* 单门实现的第一步：把专家图卡改写为 $H=C_0[h_0;g(X)]$；
* 下一步：选最小的 $\omega=2,c=2$，令 $g(X)$ 的核图卡编码 $z=xy$，并解 $L$ 的行对实现；
* 这一步尚未完成。

## 放弃原因

* 未选出具体的 $A,C,L_0,g(X)$；
* 未解 $l_iAN=D H_i$ 的兼容方程；
* 未编码 $z=xy$。

## 残留价值

* 固定 $L_0$ 的正规形；
* 澄清了专家图卡与输入约定的冲突；
* 为单门实现给出正确的参数化。

## 相关文件

* [attempts/215](215_67_verdict_uniform_spectral.md)（uniform 机制）
* [attempts/214](214_66_verdict_template_valid.md)（6 维模板）
* [attempts/201](201_pair_lift_theorem.md)（行对实现）

## 状态

* 正规形：**[M2]**。
* 单门 gadget：**[未做]**。
