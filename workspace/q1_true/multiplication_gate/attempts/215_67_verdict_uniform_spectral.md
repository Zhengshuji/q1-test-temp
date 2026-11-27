# 专家 67 号裁决落实：一致谱条件 = 过滤链 + 单位子式；剩余障碍是实现

> 2026-11-09。专家 67 号给出“一致矩形铅笔”机制：$H(X)$ 固定像 $W$、$H_A(X)=D(X)H(X)$、
> $D(X)|_W$ 一致无特征向量。本文件把该机制收紧为一条**单位子式引理**（比 Bezout 证书更简单），
> 并记录实现层的剩余障碍。状态：**M2（纸面）+ 精确验证（$\omega=2,3$）**。

## 目标

落实 67 号：给出 uniform 谱条件的可证明形式，明确剩余的可实现性问题。

## 设想与理由

专家机制：$P_X(\lambda)=(\lambda I-D(X))H(X)$，$\operatorname{im}H=W$ 固定，故
$$\operatorname{rank}P_X(\lambda)=\operatorname{rank}\big((\lambda I-D(X))|_W\big).$$
只要 $D(X)|_W$ 无特征向量，秩恒为 $\omega$。
过滤链条件：
$$D(X)w_j=w_{j+1}+\sum_{i\le j}a_{ij}(X)w_i\ (j<\omega-1),\qquad
D(X)w_{\omega-1}=g+\sum_{i\le\omega-1}a_{i,\omega-1}(X)w_i.$$

## 做法

### 1. 单位子式引理

在基 $w_0,\dots,w_{\omega-1},g$ 下，$(\lambda I-D)|_W$ 的列是
$$(\lambda I-D)w_j=\lambda w_j-Dw_j.$$
取行 $(w_1,w_2,\dots,w_{\omega-1},g)$、列 $(w_0,\dots,w_{\omega-1})$ 的子矩阵。
由过滤条件，第 $j$ 列在 $w_{j+1}$ 处系数为 $-1$，在 $w_1,\dots,w_j$ 处为 $0$，
在 $w_{j+2},\dots,g$ 处也为 $0$（$j<\omega-1$）；最后一列在 $g$ 处为 $-1$。
所以该子矩阵是**上三角**，对角全为 $-1$，行列式
$$\boxed{\det=(-1)^\omega\ne0.}$$
因此 $\operatorname{rank}((\lambda I-D)|_W)=\omega$ 对**所有** $\lambda\in\mathbb C$ 和**所有**参数 $X$ 成立。
这是比“两个子式差常数/Bezout 恒等式”更直接的一致证书；数值系数 $a_{ij}(X)$ 完全任意。

### 2. 图卡构造

取 $K_0=U\oplus Z$、$V(X)=\operatorname{graph}(X)$，
$$H(X)=\begin{bmatrix}I_U&-X\end{bmatrix},$$
则 $\ker H(X)=V(X)$、$\operatorname{im}H(X)=U=W$ 固定、$\operatorname{rank}H=\dim U=\omega$。
令 $q=\omega+1$，$D(X)$ 如上的过滤链（$a_{ij}(X)$ 可含算术变量），
$$H_A(X)=D(X)H(X),$$
则 $(5a)$ 自动、$(5b)$ 由单位子式引理自动。$q=\omega+1$ 是该机制下的**尖锐**值（$q>\omega$ 必要，$q=\omega+1$ 充分）。

### 3. 精确验证（$\omega=2,3$）

sympy 计算 $(\lambda I-D)|_W$ 的子式：
- $\omega=2$：行 $(w_1,g)$、列 $(w_0,w_1)$ 的子式 $=1$；
- $\omega=3$：行 $(w_1,w_2,g)$、列 $(w_0,w_1,w_2)$ 的子式 $=-1$。
与 $(-1)^\omega$ 一致；系数全符号化，故对所有参数成立。

### 4. 剩余障碍：实现层

$H(X),H_A(X)$ 不能任意给定：每行对 $(h_i,h_{A,i})$ 必须属于
$$\Psi:(\mathbb C^n)^*/\operatorname{row}C\to K_0^*\oplus K_0^*,\quad \bar g\mapsto(gN,gAN)$$
的像。当 $Av\in K_0$ 时必须满足兼容关系
$$h_A(v)=h(Av).$$
所以：
- 抽象铅笔层：**已解决**（单位子式）；
- 实现层：**未解决**（需设计固定的 $A,C,L_0$ 使图卡 $H(X)$ 与 $D(X)H(X)$ 的行对都在 $\operatorname{im}\Psi$ 中）；
- 算术表达：**未解决**（$z=xy$ 的单门 gadget）。

## 进展

* 一致谱条件收紧为单位子式引理（对所有参数、所有 $\lambda$）；
* 图卡 $H(X)=[I\ -X]$ 的固定像/核性质；
* $q=\omega+1$ 尖锐性；
* 实现层的兼容关系明确。

## 最终结论

* **uniform 谱条件不再是障碍**：过滤链 + 单位子式给出统一证书；
* 真正的剩余障碍是**实现**（行对属于 $\operatorname{im}\Psi$）与**算术表达**（$z=xy$）；
* 下一步按专家顺序：先做单门实现，再证 soundness/completeness，最后扩展电路。

## 放弃原因

* 未构造出满足 $\operatorname{im}\Psi$ 的图卡实现；
* 未编码 $z=xy$；
* 未 Lean 化单位子式引理（矩阵三角行列式）。

## 残留价值

* 一条统一、可复用的谱证书；
* 把硬度路线明确分解为 graph/leakage/lift 三层；
* 单位子式可作为未来 Lean 的目标。

## 相关文件

* [attempts/214](214_66_verdict_template_valid.md)（6 维模板）
* [attempts/213](213_65_verdict_implementation.md)（$q>\omega$、$\Delta$）
* [for_expert/archive/67...](../../../for_expert/archive/67_uniformity_question-answer.md)
* [attempts/201](201_pair_lift_theorem.md)（pair map）

## 状态

* 单位子式引理：**[已证-纸面 + 精确验证 ω=2,3，M2]**。
* 实现/算术 gadget：**[未做]**。
