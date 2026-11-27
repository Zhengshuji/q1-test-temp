# 自有阶差 2 实例的细查：**两阶都由 Type I（B.9）解释**

## 目标

[gap_scan.py](../../../../tools/verification/gap_scan.py) 在结构化实例族里发现一个**阶差 2** 的实例
（`diag-distinct-n7`、$n=7$、$p=2$、$r=1$、$q_0=2$）。本档细查：在 $q=2,3$ 上，失败是 Type I（零指标障碍）
还是 Type III（谱障碍）？

## 设想与理由

文献的两阶差例子（Fernando 2026 §VII）在 $q_0,q_0+1$ 的失败是**谱**障碍（Type III 方向）。
若我们的实例也是 Type III，则说明"阶差 2 可以由谱障碍产生"；若是 Type I，则说明**阶差 2 也能由整数障碍产生**，
两种机制都能给 2。

## 做法

[gap2_case.py](../../../../tools/verification/gap2_case.py)：重建实例（确定性种子），在 $q=2$（120 样本）、
$q=3$（**300 样本**）、$q=4$（60 样本）上抽样并分类。

## 进展

实例：

$$A=\operatorname{diag}(0,1,2,3,0,1,2),\quad
C=\begin{pmatrix}0&1&1&1&1&0&1\\1&0&1&1&0&1&0\end{pmatrix},\quad
L_0=\begin{pmatrix}0&0&32&243&0&1&0\end{pmatrix},$$

$n=7$、$p=2$、$r=1$、$q_0=2$、$r_1=4$、$n-p=5$。

| 阶 $q$ | 样本 | 分类 |
|---|---|---|
| 2 | 5 | **Type I 5** |
| 3 | 300 | **Type I 300** |
| 4 | 60 | 可行 **60/60** |

## 最终结论

1. 该实例的阶差 2 **完全由零指标障碍（B.9）解释**：$q=2$ 与 $q=3$ 的所有候选都有 $h\ge q+r_1$；
2. 因此**阶差 2 有两种不同机制**：
   * **Type I（整数）**：本文实例——只需 $h\ge q+r_1$；
   * **Type III（谱）**：文献例子（及 [C4](../../../../proof/refuted/C4_type3_counterexample.md) 的反例）；
3. 这与"$q_{\min}>q_0$ 由 $h$ 的取值刻画"的直觉部分吻合：**当 $h$ 在低阶被顶到 $q+r_1$ 时会出现阶差**，
   但它**不是**唯一机制（C4）。

## 放弃原因

不适用。**未做**：$q=3$ 的**证明**（不是抽不到，而是抽样不能证明）；需要图卡消元。

## 残留价值

* 一个**自有**的阶差 2 实例（不依赖文献），且机制清楚（Type I）；
* 说明"阶差 2"不是稀有现象：13/6/1 的分布里就有一个；
* 与文献例子（谱机制）形成对照，为"阶差的两种机制"提供了两个可复算的例子。

## 相关文件

- [tools/verification/gap2_case.py](../../../../tools/verification/gap2_case.py)
- [tools/verification/gap_scan.py](../../../../tools/verification/gap_scan.py)
- [workspace/q1_false/feasibility_geometry/attempts/12_structured_gap_table.md](12_structured_gap_table.md)
- [proof/refuted/C4_type3_counterexample.md](../../../../proof/refuted/C4_type3_counterexample.md)
