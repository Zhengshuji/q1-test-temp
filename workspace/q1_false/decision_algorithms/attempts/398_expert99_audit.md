# 360 专家 99 号审计：核心定理成立，四处更正；结论范围收窄

> 送审件 [99](../../../for_expert/archive/99_linear_decoding_exclusion.md)（已归档），
> 答复 [99-reply](../../../for_expert/archive/99_linear_decoding_exclusion-reply.md)。
> **总评（他的话）**："核心排除论证在修正 II.1 之后是可靠的"、"这是报告里最强的结果"、
> 但"II.1 的分解与若干宽泛结论需要更正"；最终应作为**对仿射线性算术 gadget 归约的重要负结果**保留，
> **不是**对观测器可行性 NP-难的普遍不可能定理。

## 目标

1. 记录审计的四处数学更正（含一处**我的错误**）。
2. 落实：358（分解 + 闭包论证 + 证书）、359（全局析取、非退化定义、范围收窄）。
3. 记录他给的三条出口排序与下一步建议。

## 设想与理由

审计型回复：只记明确裁决。这次他**指出我一处硬错误**（II.1 的分解等式），
并给了正确形式与证明；其余是范围与措辞的修正。

## 做法：逐条裁决

### 1. 硬错误：$\{\operatorname{rank}H=\omega\}=\bigcup_W M_W$ **是假的**

> 因为 $\operatorname{rank}H=\omega$ 只约束 $h_i$，**不约束 $g_i$**。
> 反例：$W_0=0$、$m=1$、$\omega=1$，取 $h\in W$、$g\notin W$——$\operatorname{rank}H=1$，但点不在任何 $M_W$ 里。

**正确形式（可行秩层的分解，需固定行协调）**：
$$\boxed{\mathcal F_\omega=\bigcup_{W\supseteq W_0}\Bigl[M_W\cap\{\operatorname{rank}H=\omega\}\cap\{(5b)\}\Bigr]}$$
他给了双向包含的证明。**开集性不受影响**：$M_W$ 上恒有 $\operatorname{rank}H\le\omega$，故
$\{\operatorname{rank}H=\omega\}$ 在 $M_W$ 里开——这正是证明的支点。

**落实**：358 与 359 都改成这个形式，并在 358 里保留反例说明原等式为什么错。

### 2. 闭包论证：精确秩层是**局部闭**，不是闭

我写的"$\overline{\mathcal F}\subseteq\{\operatorname{rank}H=\omega\}$ 因为该层闭"是错的。
正确：闭包含于**闭**行列式簇 $D_\omega=\{\operatorname{rank}H\le\omega\}$，而中点 $\notin D_\omega$。

**落实**：358 的证明按此改写。

### 3. 证书要补全

他只看到 $H_p,H_q$，看不到 $H_A$、$\mathcal T$、Bézout 证书。

**落实**：[c358](../../../../tools/verification/c358_nonlinear_stratum_witness.py) 现在打印
$H$、$H_A$、非零极大子式与 $\gcd$，并逐条断言；358 加了完整表格。

### 4. 强化：析取是**全局**的

$M_W$ 是**线性**空间、必含 $0$，故常数只能是 \(x(0)\)（或 \(y(0)\)）。于是
$$\boxed{\mathcal F\subseteq\{x=x(0)\}\cup\{y=y(0)\}}$$
即可行集在 $(x,y)$-平面上的投影落在一条竖线 $\cup$ 一条横线里。

### 5. "表达乘法"的定义要收紧

$\{(x,y,z):x=0,z=0\}$ 也满足 $z=xy$，但没编码任何乘法。他给的定义：

> **非退化乘法门**：(i) $z=xy$ 在每个可行点成立；(ii) 可行集到 $(x,y)$ 的投影在 $\mathbb A^2$ 中 **Zariski 稠密**。

> **推论（他写的）**：仿射线性解码下**不存在非退化乘法门**——由 (D) 立即得到。

**落实**：359 加了定义与推论 3。

### 6. $\bigcup_W M_W$ 不是 $\{\operatorname{rank}H\le\omega\}$

$M_W$ 同时约束 $h_i$ 与 $g_i$，其并是 $\operatorname{rank}\begin{bmatrix}H\\H_A\end{bmatrix}\le\omega$，
不是 $\operatorname{rank}H\le\omega$。**落实**：359 已改（并强调"只在可行集上两者才一致"）。

### 7. 结论范围收窄（重要）

我写"ARM 翻译被同一论证排除"**说过头了**。他的原话：

> 定理排除的是**一类**算术 gadget 归约——其中标量乘法由**非退化的、仿射线性解码的**乘法门表示。
> 它**不**排除直接编码秩条件的归约，或换一种源问题表示的归约。

**落实**：359 的最终结论已按此改写，并列出三条出口。

### 8. 三条出口（他给的排序）

1. **不用乘法门的归约**（他推荐优先）；
2. 放弃逐行同一性（换架构，但要确认仍对应原问题）；
3. 非线性解码（可行但难验证、难解释）。

### 9. Q5：Grassmannian 分解对算法暂时没用

他给的理由很实在：$W$ 本身在全族上量化——**特定的 $W$ 可能可行而一般的 $W$ 不行**，
所以"对 generic $W$ 做 generic-gcd 检验"不够。他给了六步算法框架，但指出第 6 步是主要困难。
有用的部分是**组织实验**：先采 $W$，再在 $M_W$ 里测"秩精确部分是否非空"与"该纤维是否谱可行"。

## 进展

- 四处更正全部落实（358、359、c358）；
- 结论范围按他的措辞收窄；
- 记录了下一步的两个方向。

## 最终结论

1. **核心定理站得住**：仿射线性解码下不存在**非退化**乘法门。这是可保留的负结果。
2. **我的两处过头话已撤回**：①"$\{\operatorname{rank}H=\omega\}=\bigcup_W M_W$"（数学错误）；
   ②"ARM 路线被排除"（只排除了用乘法门的 ARM 翻译）。
3. **下一步（他优先）**：**不用乘法门的归约**——直接编码秩条件，绕过 gadget 架构。

## 放弃原因

- 没有开始"不用乘法门的归约"（这是一个新方向，需要单独设计）；
- 没有验证他的六步算法框架的第 6 步（"$W$ 上的量化"）是否可做。

## 残留价值

- 一条**经过专家复核的定理**（仿射线性非退化乘法门不存在），含全局析取 (D)；
- 一处被专家抓出的数学错误及其正确形式（分解 (B)）；
- 一条明确的下一步：**不用乘法门的归约**。

## 相关文件

- [99](../../../for_expert/archive/99_linear_decoding_exclusion.md)、[99-reply](../../../for_expert/archive/99_linear_decoding_exclusion-reply.md)
- [358](../../../q1_true/multiplication_gate/attempts/396_clp_counterexample.md)（分解已改、闭包论证已改、证书已补）
- [359](../../../q1_true/multiplication_gate/attempts/397_no_go_all_strata.md)（全局析取、非退化定义、范围收窄）
- [c358](../../../../tools/verification/c358_nonlinear_stratum_witness.py)

## 状态

- 审计落实：**[完成]**。
- 定理：**[已证-纸面]** + 专家复核（他明确说 "This proof is correct"）。
- 下一步方向：**[未开始]**（不用乘法门的归约）。
