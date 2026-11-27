# 掉落轨迹：概念、实现骨架与可靠性边界（未完成，但有明确结论）

## 目标

把"gcd 在特殊 $\theta$ 上掉落到 0"这件事变成可判定的条件，从而补上 §8.1 的最后一块：
"该图卡存在可行 $\theta$" vs "该图卡处处失败"。

## 设想与理由

典型 gcd $g(\theta,\lambda)$ 的 $\lambda$ 次数在特殊 $\theta$ 处会掉落。**必要**条件是：
$g$ 的 $\lambda$ 首项系数 $\ell(\theta)$ 或 gcd 表示式的分母在 $\theta$ 处为零。所以候选集是有限的；
逐点精确核验即可。若候选集为空或全部候选点上 $\deg_\lambda\ge1$，则（在该候选集意义下）无掉落。

## 做法

[drop_locus.py](../../../../tools/verification/drop_locus.py)：

1. 逐图卡取 `chart_gcd_analysis` 的符号 gcd；取 $\mathrm{LC}_\lambda(g)$ 与分母，求**有理根**得候选 $\theta$；
2. 在每个候选点精确算全部极大子式并求 gcd：
   * $\deg=0$ ⟹ 该点 $(5b)$ 成立 ⟹ 若 $(5a)$ 也成立，构造见证并通过七条检查 ⟹ `FEASIBLE`；
   * $\deg\ge1$ ⟹ 该点仍失败。

## 进展

| 实例 | 图卡 | 典型 $\deg$ | 候选 $\theta$ | 候选点上的 $\deg$ |
|---|---|---|---|---|
| C4（$q_0=3$）| (0) | 2 | $5/4$ | **1** |
| C4 | (1) | 2 | $4/5$ | **1** |
| $5/1/2$ seed 3003 | (0) / (1) | 1 / 1 | $0$ / — | 空（该点图表退化）/ — |
| $5/1/2$ seed 3005 | (0) / (1) | 1 / 1 | — / $0$ | — / 空（退化）|

## 最终结论

1. **C4 的空轨迹结论得到（部分）机器复核**：两个例外点都 $\deg=1$，与
   [attempts/41](41_symbolic_chart_gcd.md) 的手工核验一致；
2. **但候选集不完备**：掉落还可能发生在**各子式自身**的 $\lambda$ 首项系数零点（不只是 gcd 的），
   而本实现只取了 gcd 的首项系数与分母。故工具**默认只报 `UNKNOWN`**，仅在
   [attempts/41](41_symbolic_chart_gcd.md) 那种逐点手工核验后才可声明"轨迹为空"；
3. 对 seed 3003/3005，候选点 $\theta=0$ 处图表退化（$\mathcal Z$ 不满秩），说明网格找到的见证在**别的** $\theta$ 上
   ——正是"掉落轨迹"上的点，只是不在当前候选集里。

## 放弃原因

**候选集完备性未解决**：严格的必要条件是"某个**子结式**退化"，需要子结式/多项式结式的系统计算
（sympy 有 `subresultants`，但把 $N$ 个子式的整族子结式组织成判定仍需要设计）。
当前实现只覆盖了"gcd 首项系数"这一必要条件的子集。

## 残留价值

* 把"掉落轨迹"讲清楚了：**可行点 = gcd 掉落到 0 的点**，并解释了薄性；
* 一个**不会误报**的工具骨架（默认 `UNKNOWN`），以及 C4 的逐点复核数据；
* 明确了下一步的理论任务：**用子结式刻画掉落轨迹**（而不是猜测候选集）。

## 相关文件

- [tools/verification/drop_locus.py](../../../../tools/verification/drop_locus.py)
- [tools/verification/chart_gcd_analysis.py](../../../../tools/verification/chart_gcd_analysis.py)
- [workspace/q1_false/feasibility_geometry/attempts/41_symbolic_chart_gcd.md](41_symbolic_chart_gcd.md)
- [workspace/q1_false/feasibility_geometry/attempts/43_drop_locus.md](43_drop_locus.md)（本路线的概念来源）
