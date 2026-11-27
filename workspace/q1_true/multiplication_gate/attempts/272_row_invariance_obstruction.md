# 行变换不变性：非零 gadget 不能依赖“某两行共享一个标量”

> 2026-11-09。路线 B 的落地障碍有一个更根本的原因：
> 观测器条件对 $L$ 的**可逆行变换**不变。
> 因此任何要求“两个自由行的某个 entry 相等”的 gadget 都不是良定义的；
> gadget 只能依赖 $L$ 的**行空间不变量**（子式/Plücker 坐标）。
> 状态：**M2（结构定理）**。

## 目标

解释为什么“共享 $f$”不能由 $L$ 的结构强制，并给出一般限制。

## 设想与理由

观测器条件是行空间条件：
$$(5a)\ \operatorname{row}(LA)\subseteq\operatorname{row}[L;CA;C],\qquad
(5b)\ \operatorname{rank}(\lambda L-LA)=\operatorname{rank}L\ \forall\lambda.$$
注意 $L=[L_0;R]$ 的第一块 $L_0$ 固定，所以不能取任意 $G\in GL_q$。
取保持 $L_0$ 的子群
$$G=\begin{bmatrix}I_{r_0}&0\\ H&G_{22}\end{bmatrix},\qquad G_{22}\in GL_r,\ H\ \text{任意}.$$
令 $L'=GL=[L_0;\,H L_0+G_{22}R]$。则 $L'A=G(LA)$，且 $(5a)(5b)$ 对 $L$ 与 $L'$ 同时成立或失败。
自由块可以任意混合（$G_{22}$），也可以加上固定行（$H L_0$）。

## 做法：不变性

### 1. 引理

$$L\ \text{可行}\iff GL\ \text{可行}\qquad(\forall G=\begin{bmatrix}I&0\\ H&G_{22}\end{bmatrix},\ G_{22}\in GL_r).$$

*证明*：$L'A=GLA$、$L'=GL$，所以
$$[L'A;L';CA;C]=\operatorname{diag}(G,G,I,I)\,[LA;L;CA;C],$$
行空间的秩不变；$(5a)$ 成立性不变。$(5b)$ 同理：
$$\lambda L'-L'A=G(\lambda L-LA),$$
秩不变。$\\square$

### 2. 推论

任何 gadget 若依赖“$L$ 的某两行满足 $R_1\\cdot v=R_2\\cdot v$”这类**逐行 entry 条件**，
则不是 $GL_q$-不变的：取 $G$ 打乱/混合两行，条件失效但可行性不变。
所以这样的 gadget **不可能**由 $(5a)(5b)$ 强制。

### 3. 对路线 B 的影响

270 的 gadget 需要 $H$ 的两个自由行都是同一个 $f$ 倍向量；
这等价于对 $L$ 的逐行条件，按引理不可能 sound。
要使非零 gadget 可行，$f$ 必须是 $L$ 的**行空间不变量**，例如：
- $L$ 的某个子式/Plücker 坐标；
- $H$ 或 $H_A$ 的行空间不变量；
- 由 $C,CA$ 固定的线性泛函（但那就不是 witness）。

### 4. 可能的替代

- 用 $f=\\det$ 的某个子式（行空间不变量）做非零 gadget；
- 但 $f$ 作为子式时，$H$ 的行缩放会改变 $f$ 的次数，需重新设计 gcd；
- 这仍是未解决的问题。

## 进展

* 证明 $GL_q$ 不变性；
* 排除“逐行共享标量”的 gadget；
* 明确非零 gadget 必须用行空间不变量。

## 最终结论

* 路线 B 的当前形式（共享 $f$）**不可能 sound**；
* 需要重新设计一个 $GL_q$-不变的非零 gadget；
* 这是比 271 更强的障碍。

## 放弃原因

* 未构造行空间不变量版本；
* 未接等式 gadget。

## 残留价值

* 一个基本的对称性约束（对所有 gadget 都适用）；
* 解释了 271 的失败；
* 为后续 gadget 设计设定必要条件。

## 相关文件

* [attempts/271](../../../q1_false/decision_algorithms/attempts/271_shared_f_obstruction.md)
* [attempts/270](../../../q1_false/decision_algorithms/attempts/270_nonzero_gadget.md)

## 状态

* 路线 B：**[遇到基本对称性障碍]**。
* 行空间不变量 gadget：**[未做]**。
