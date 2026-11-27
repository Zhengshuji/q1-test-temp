# 502 门的正确逻辑：$\operatorname{rank}P\le\omega$，on-gate 必须 $\omega=2$

> 2026-11-27。501 之后重新梳理门的逻辑方向；ChatGPT 指出一个先决条件：
> 由 $(5a)$，$\operatorname{rank}(\lambda H-H_A)\le\operatorname{rank}H=\omega$ 恒成立，
> 所以 on-gate 的 rank-2 层必须满足 $\omega=2$ 且 pencil 在商空间上处处满秩；off-gate 的 rank-3 层必须失败。
> 状态：**[M2 分析]**。

## 事实

$(5a)$ 给 $\operatorname{row}H_A\subseteq\operatorname{row}H$，即 $H_A=ZH$。于是
$$P(\lambda)=(\lambda I-Z)H,\qquad \operatorname{rank}P(\lambda)\le\operatorname{rank}H=\omega .$$
$(5b)$ 要求等号对所有 $\lambda$ 成立；失败 $\iff$ 某个 $\lambda$ 处 $\operatorname{rank}P<\omega$
$\iff$ $Z$ 在 $W=\operatorname{im}H$ 上有特征向量。

## 门的逻辑

285 的门：on-gate（$z=xy$）$\operatorname{rank}H=2$；off-gate $\operatorname{rank}H=3$。

- **on-gate**：$\omega=2$，要求 $Z|_W$ 无特征向量（$2$ 维 $W$，$Z:W\to\mathbb C^5$，一般可以实现）；
- **off-gate**：$\omega=3$，要求 $(5b)$ 失败（$Z|_W$ 有特征向量），才能让“非门”不可行。

所以构造目标不是“让 rank 掉”，而是：

1. 找一个提升，使 on-gate 的 $Z|_W$（$2$ 维）无特征向量；
2. 同一提升下，off-gate 的 $Z|_W$（$3$ 维）必有特征向量（例如 $3\times3$ 压缩必有特征值）。

## 与 495–501 的关系

495/499/500/501 都在具体 $A$ 下检查 on-gate 的提升，全部失败（$(5a)$ 的列关系把门参数钉死或把 $H_A$ 压到低秩）。
502 说明：这些失败不等于门不可能，只是那些 $A$ 的 $Z|_W$ 在 $\omega=2$ 时仍有特征向量。

## 先决条件（ChatGPT）

> 先确认 on-gate 的 $\omega=2$ 层能否让 $(5b)$ 成立；这是整个构造能否成立的前提。
> 应把 $H,H_A$ 在商空间 $\mathbb C^4/\ker H$ 上诱导为 $2\times2$ 矩阵，检查 pencil 是否对每个复 $\lambda$ 满秩。

## 下一步

构造一个 $\omega=2$ 的提升：$W$ 二维，$Z:W\to\mathbb C^5$ 选成“$W$ 上的旋转型”（无特征向量），
再回推 $H_A=ZH$、$L$ 与 $A$；用精确算术验证 $(5a)$ 与 $(5b)$。

## 状态

- 逻辑与事实：**[M2 分析]**（$\operatorname{rank}P\le\omega$ 是线性代数事实）；
- $\omega=2$ 的具体构造：**[未做]**。
