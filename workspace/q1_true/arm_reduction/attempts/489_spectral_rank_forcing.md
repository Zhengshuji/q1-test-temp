# 489 谱条件能提供什么秩信息？——只剩“谱秩强制 gadget”一个靶子

> 2026-11-27。PLAN 的 A 项：给“把秩约束编码进 $(5b)$ 谱条件”一次专门尝试（硬时限：只找机制）。
> **结论：没有找到机制。** 但把剩余可能压缩成一个精确的靶子：
> **谱秩强制 gadget**（rank $X\ge4$ ⇒ $Z$ 有特征向量）。状态：**[M2 分析]**，无构造。

## 目标

查清 $(5b)$ 在“秩”上到底能提供什么信息，判断它能否给出任何载体的秩上界（特别是 $\le3$）。

## 设想与理由

$(5b)$ 是“对所有 $\lambda$ 满秩”，看起来像“没有特征值”，也许能转化成某种秩条件。
若能把“rank 大”与“出现特征向量”挂钩，就能用 $(5b)$ 的失败来强制秩上界。

## 做法

### 1. $(5b)$ 的精确形式

$H=LN$、$H_A=LAN$、$\omega=\operatorname{rank}H$。$(5b)$ 即
$$\operatorname{rank}(\lambda H-H_A)=\omega\quad\forall\lambda.$$
因 $\ker H\subseteq\ker(\lambda H-H_A)$，秩相等 $\iff$
$$\ker(\lambda H-H_A)=\ker H\quad\forall\lambda.$$
等价地：**若 $Hx\ne0$，则 $H_Ax\ne\lambda Hx$**。令 $Z:W=\operatorname{im}H\to\mathbb C^q$，$Z(Hx)=H_Ax$，
则
$$(5b)\iff Z\ \text{在}\ W\ \text{上没有特征向量（没有不变直线）}.$$

### 2. 它不给秩上界

- $\omega=\operatorname{rank}H$、$\dim W=\omega+t$ 都不被 $(5b)$ 上界：$t$ 可增大（直和），
  且 $L=I_n$ 给出 $\omega=n$ 的可行实例（488）；
- $(5b)$ 约束的是 $Z$ 的**谱**（无不变直线），不是任何自然载体的秩；
- 所以“$\operatorname{rank}\le3$”不能从 $(5b)$ 直接读出。

### 3. 唯一可能的转化：谱秩强制

要让 $(5b)$ 强制秩上界，需要一个 gadget $G$，把载体 $X$ 变成 $Z$，使
$$\operatorname{rank}X\ge4\ \Longrightarrow\ Z\ \text{有特征向量}\quad(\text{即 }(5b)\text{ 失败}),$$
$$\operatorname{rank}X\le3\ \Longrightarrow\ (5b)\ \text{成立}.$$
这就是**谱秩强制 gadget**。它是 ARM 路线剩下的唯一靶子。

### 4. 为什么它难（启发性 no-go）

- 对一般的 $Z$（$\dim W\ge2$），“无特征向量”是开稠密条件；要让 rank 大**必然**产生特征向量，
  $Z$ 必须被 $X$ 强制成非一般形式（如 companion 型）；
- 但观测器侧 $Z$ 由 $L$ 决定（$Z(Hx)=LAx$），$L$ 同时决定 $H$；$Z$ 对 $L$ 是**分式线性**的，
  不是可以自由设计的矩阵；
- 已有的 sound gadget 只有“非零/输入非零”（296、303），它们编码的是**开条件**，不是秩。

**没有构造，也没有不可能定理**；这里只把靶子写清楚，供后续判断是否值得再投入。

## 进展

1. 把 $(5b)$ 精确化为“$Z$ 在 $W$ 上无特征向量”；
2. 说明它不提供任何秩上界（含 $L=I_n$ 反例）；
3. 把剩余可能压缩成“谱秩强制 gadget”，并给出三条它难的启发式理由。

## 最终结论

- **没有找到**把秩约束编码进 $(5b)$ 的机制；
- ARM 路线剩下的唯一靶子是“谱秩强制 gadget”；在它被构造或被证明不可能之前，
  ARM 作为**活跃路线**应当关闭（保留 390/488/489 的 no-go 与靶子记录）。

## 放弃原因

- 硬时限内只做了机制分析，没有构造；
- 分式线性耦合与“无特征向量是开条件”两点使构造前景不明；
- 没有把“谱秩强制不可能”写成定理（只给了启发式）。

## 残留价值

- $(5b)\iff$“$Z$ 无特征向量”的干净表述（可直接引用）；
- 精确靶子：谱秩强制 gadget；
- 与 488 一起，ARM 的自然接口全部有死因。

## 相关文件

- [PLAN](../PLAN.md)、[390](390_arm_translation_analysis.md)、[488](488_arm_interface_rowcount_nogo.md)
- [296](../../multiplication_gate/attempts/296_nonzero_gadget_observer.md)、[303](../../../q1_false/decision_algorithms/attempts/303_79_verdict_lifts.md)

## 状态

- $(5b)\iff$ 无特征向量：**[已证-纸面]**（线性代数）；
- 谱秩强制 gadget：**[未构造]**；
- 不可能性：**[未证]**。
