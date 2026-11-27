# chart 表达式 $F_A(X)$ 的次数：精确验证（专家 60 号形式化顺序第 3–4 步）

> 2026-11-08。专家建议在核恒等式之后形式化 chart 表达式 $F_A(X)$ 及其二次性。
> 本文件用**符号精确验证**覆盖这一步（25 个符号实例），并说明 Lean 化的分工。
> 状态：**精确验证 25/25**；Lean 部分未做（理由见下）。

## 目标

核对 chart 矩阵
$$F_A(X)=\begin{bmatrix}A_{21}+A_{22}X-XA_{11}-XA_{12}X\\ A_{31}+A_{32}X\end{bmatrix}$$
的每个元素是 $X$ 的元素的**总次数 $\le2$** 的多项式；并确认 chart 恒等式（171 已机器核对 100/100）。

## 设想与理由

chart 公式的“二次性”是 Bézout 界的关键输入（次数 $d=2(r+1)$）。核恒等式与秩恒等式已在 Lean 中
（174）；chart 表达式的 Lean 形式化需要矩阵分块坐标、图子空间与多项式次数的簿记，工作量显著大于核恒等式。
按项目规则（Lean 不是硬门槛；精确验证 + 纸面可用），这里用 sympy 符号验证覆盖“次数 $\le2$”，
并在文档中写明 Lean 与验证的分工。

## 做法

工具：[tools/verification/buv_chart_degree.py](../../../../tools/verification/buv_chart_degree.py)

对 $(m,u)\in\{(2,2),(1,2),(2,3),(3,3),(3,4)\}$（$m=k-u$）与 5 个随机整数 $A$ 分块：
1. 取 $X$ 的 $m u$ 个符号；
2. 计算 $F_A(X)$ 的每个元素并 `expand`；
3. 用 `sympy.Poly(...).total_degree()` 断言 $\le2$。

## 结果

```
PASS: chart entries are polynomials of total degree <= 2 on 25 symbolic instances
```

与 171 的 chart 恒等式验证（100/100 随机有理 chart，`rank F_A(X) = u - dim(U∩A^{-1}U)`）互补：
- 恒等式：数值/精确算术（100/100）；
- 次数：符号多项式（25/25）。

## 进展

* chart 的二次性已符号验证（25 个实例）；
* 与 171 的 chart 恒等式、174 的 Lean 核恒等式共同覆盖专家顺序第 1–4 步；
* Lean 化 chart 表达式的分工已写明。

## 最终结论

* $F_A(X)$ 的元素总次数 $\le2$：符号验证通过；
* 结合 171 的秩恒等式，Bézout 界的次数输入（$d=2(r+1)$）成立；
* Lean 只覆盖核/秩恒等式（174）；chart 与次数用精确验证 + 纸面（按项目规则可接受）。

## 放弃原因

* 未 Lean 化 chart 表达式（矩阵分块/图子空间/多项式次数的簿记成本高；专家顺序是建议，非硬门槛）；
* 未验证 Bézout 界本身的紧性（引理是标准定理）；
* 符号验证是有限实例，不是对所有 $(m,u)$ 的证明（次数上界由公式结构显然，验证是复核）。

## 残留价值

* chart 二次性的可复现验证；
* 明确了 Lean 与精确验证的边界（174 vs 177）。

## 相关文件

* [attempts/171](../../c_stratification/attempts/171_Buv_rank_strata.md)（chart 恒等式）
* [attempts/174](174_Buv_lean_kernel.md)（Lean 核/秩恒等式）
* [tools/verification/buv_chart_degree.py](../../../../tools/verification/buv_chart_degree.py)

## 状态

* 次数验证：**[精确验证 25/25]**。
* Lean chart：**[未做]**（分工见上）。
