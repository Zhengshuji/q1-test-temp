> **295 降级**：依赖 282/284/292；q=5 只是搜索边界，不是关闭定理。

# $q=5$ rank 门的收束：三种情形都没有构造；建议转 $(5b)$ 谱门

> 2026-11-09。把 282–292 的 $q=5$ rank 门结果汇总：
> 三种可能的 $H_0$ 秩/吸收组合都没有给出可行构造。
> 这不是不可能性定理，但 rank 门的搜索空间已经基本穷尽；
> 建议按专家 77 号的优先级，转 $(5b)$ 的谱门（非零/开条件）。
> 状态：**M2（汇总）+ 路线建议**。

## 目标

汇总 $q=5$ rank 门的三种情形，判断是否继续。

## 设想与理由

$q=5,r_0=2,r=3$，$\omega=2$（284 的最小窗口）。$H_0$ 的秩只能 1 或 2。

## 做法：三种情形

### 1. $H_0$ 秩 2，且被 $Y$ 吸收

$H_0\subseteq\operatorname{row}Y$ 且 $\operatorname{rank}H_0=2=\omega$，
则 $\operatorname{row}Y=\operatorname{row}H_0$ 是**固定**二维平面。
$Y$ 的三行都线性地落在该平面内，条件是线性的，没有 $z=xy$ 型二次门。

### 2. $H_0$ 秩 2，且与 $Y$ 独立

282 的独立情形：$M$ 的特征值处固定块掉秩，自由块秩 $\le\operatorname{rank}Y$，
$$\operatorname{rank}P\le(\operatorname{rank}H_0-1)+\operatorname{rank}Y=\omega-1<2,$$
$(5b)$ 失败。

### 3. $H_0$ 秩 1

- $Y_1\ne e_1$：$\operatorname{row}Y=\operatorname{span}(e_1,Y_1)$ 固定，无二次门（292）；
- $Y_1=e_1$：$H_{A,1}=e_1+o_1$，$\lambda=1$ 掉秩，除非 $o_1$ 带 $e_3,e_4$ 分量；
  2000 个随机样本没有找到（291/292）。

## 进展

* 三种情形全部收束；
* $q=5$ rank 门没有可行构造；
* 明确下一步应转谱门。

## 最终结论

* $q=5$ 的 rank-one 门在三种自然结构下都被堵住；
* $q\ge6$ 的 rank 门仍开放，但同样的“吸收 vs 独立”二分可能继续限制；
* 按专家 77 号，Route B 的 $(5b)$ 谱门是更值得投入的方向：
  $(5a)$ 给等式，$(5b)$ 给非零/开条件（269 的极性）。

## 放弃原因

* 未证 $q=5$ rank 门不可能；
* 未穷举 $q\ge6$；
* 未构造谱门。

## 残留价值

* 一个清晰的收束表；
* 避免在 $q=5$ rank 门上重复搜索；
* 转向谱门的理由。

## 相关文件

* [attempts/284](../../../q1_false/decision_algorithms/attempts/284_rank_window.md)
* [attempts/292](../../../q1_false/decision_algorithms/attempts/292_y1_dichotomy.md)
* [attempts/269](../../../q1_false/decision_algorithms/attempts/269_spectral_polarity.md)

## 状态

* 汇总：**[M2 纸面]**。
* 谱门：**[未开始]**。
