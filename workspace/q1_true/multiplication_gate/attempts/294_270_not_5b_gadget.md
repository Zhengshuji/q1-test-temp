# 270 的非零 gadget 不是 $(5b)$ gadget：$H=fH_0$ 使 $\\operatorname{rank}H$ 随 $f$ 变化

> 2026-11-09。检查 270 的压缩 gadget 是否真的实现 $(5b)\\iff f\\ne0$。
> 结论：**不是**。270 取
> $$H=f\\begin{bmatrix}e_1\\\\e_2\\\\e_3\\end{bmatrix},$$
> 所以 $f=0$ 时 $H=0$、$\\operatorname{rank}H=0$，而 $(5b)$ 的前提是固定 $\\omega=\\operatorname{rank}H$。
> $f=0$ 处“$(5b)$ 失败”其实是因为 $H$ 掉秩（$(5a)$/秩层问题），不是谱条件失败。
> 状态：**撤回 270 的“非零 gadget”结论**。

## 目标

判断 270 的 $\\gcd=f$ 构造是否给出 $(5b)\\iff f\\ne0$。

## 设想与理由

$(5b)$ 的前提是 $\operatorname{rank}H=\omega$ 固定；先检查 270 的 $H$ 是否保持秩。

## 做法：检查 $H$ 的秩

270 的
$$H=\\begin{bmatrix}f e_1\\\\f e_2\\\\e_1+e_2\\end{bmatrix}.$$
- $f\\ne0$：$H$ 行空间含 $e_1,e_2$，秩为 3（$q=3,k=3$；或至少 2，取决于 $k$）；
- $f=0$：$H$ 只剩 $e_1+e_2$，秩 1。

$(5b)$ 的定义是
$$\\operatorname{rank}[\\lambda L-LA;CA;C]=\\operatorname{rank}[L;CA;C]\\quad\\forall\\lambda,$$
右边 $\\operatorname{rank}H=\\omega$ 是**固定**的。若 $f=0$ 时 $\\operatorname{rank}H$ 变了，问题已经不在同一个秩层，
不能把“$f=0$ 时 rank 降”当作 $(5b)$ 的失败。

## 正确的非零 gadget 要求

1. $H$ 的秩对 $f$ **恒定**（至少 $f\\ne0$ 与 $f=0$ 同秩）；
2. $P$ 的极大子式 gcd 为 $f$（作为 $\\lambda$ 的多项式，gcd 是常数 $f$）；
3. 在 $f=0$ 处，$\\operatorname{rank}P(\\lambda)<\\omega$ 对某个 $\\lambda$；
4. 在 $f\\ne0$ 处，$\\operatorname{rank}P(\\lambda)=\\omega$ 对所有 $\\lambda$。

270 只满足第 2 条（且 $H$ 的秩随 $f$ 变），不满足 1、3、4 的秩层稳定性。

## 进展

* 撤回 270 的“非零 gadget”结论；
* 明确正确 gadget 的四个条件；
* 指出 $H=fH_0$ 与固定 $\\omega$ 冲突。

## 最终结论

* 270 是“秩随参数变”的退化例子，不是 $(5b)$ 的非零 gadget；
* Route B 需要新的构造：$H$ 满秩且与 $f$ 无关，$P$ 的 gcd 才编码 $f$。

## 放弃原因

* 未构造正确的非零 gadget；
* 未验证四个条件。

## 残留价值

* 一个明确的反例检查；
* 正确 gadget 的四条标准；
* 避免把 270 当作已完成的 gadget。

## 相关文件

* [attempts/270](../../../q1_false/decision_algorithms/attempts/270_nonzero_gadget.md)
* [attempts/269](../../../q1_false/decision_algorithms/attempts/269_spectral_polarity.md)
* `tools/verification/c270_nonzero_gadget.py`

## 状态

* 270：**[撤回为“非 $(5b)$ gadget”]**。
* 正确 gadget：**[未构造]**。
