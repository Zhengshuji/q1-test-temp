# 阶差的全景：三个算例、两种机制

## 目标

把目前所有"阶差 $\ge1$"的算例放在一张表里，标注每个低阶的失败机制（Type I 整数 / Type III 谱），
为"何时 $q_{\min}>q_0$"这个问题划出边界。

## 设想与理由

前面分别得到：公开例子（阶差 2，两个低阶都是 Type I）、`diag-distinct-n7`（阶差 2，Type I）、
C4 反例实例（$q_0$ 阶 Type III）。本节把 C4 实例**往上扫**，补齐它的阶差，并统一记录。

## 做法

1. C4 实例（$n=6$、Jordan 块 $A$、$p=r=2$、$q_0=3$、$r_1=4$、$\\dim K=2$）：
   * $q=3$：$Z$-参数化 200 次抽样；
   * $q=4$：$d=0$，改为**直接构造补**（$\\operatorname{row}L_0$ + 2 个使 $[C;L]$ 满秩的行），400 次；
2. 用 `type3_structured.fast_dfin` 记 $h$、$d_{\\rm fin}$，并统计 $(5a)$ 与 $(5b)$。

## 进展

**C4 实例**：

| 阶 $q$ | 代数可行 | $(5b)$ 成立 | $h$ | $q+r_1$ | 机制 |
|---|---|---|---|---|---|
| 3 | 194 | **0** | $6=n$ | 7 | **Type III**（$\\delta=1$）|
| 4 | 400 | **400** | $6$ | 8 | 可行 |

⟹ C4 实例的 **$q_{\\min}=4$（阶差 1）**，且 $q_0$ 阶的失败是**谱障碍**（Type III）。

**三个算例的对照**：

| 算例 | $n,p,r$ | $q_0$ | $q_{\\min}$ | 阶差 | 低阶失败机制 |
|---|---|---|---|---|---|
| Fernando 2026 §VII | $8,2,2$ | 3 | 5 | **2** | Type I（$h=q+r_1$，由 $q+r_1=n$ 强制）|
| `diag-distinct-n7` | $7,2,1$ | 2 | 4 | **2** | Type I（$h\\ge q+r_1$）|
| C4 实例 | $6,2,2$ | 3 | 4 | **1** | Type III（$h<q+r_1$ 但 $d_{\\rm fin}>0$）|

## 最终结论

1. 阶差 1 与阶差 2 都出现，且都有 Type I 与 Type III 两种机制（Type III 见 C4 实例，阶差 1；
   文献与 `diag-distinct` 的阶差 2 是 Type I）；
2. 因此"阶差大小"与"失败机制"是**两个独立维度**：
   * 机制：由 $h$ 与 $q+r_1$ 的关系（B.9/B.11）分成 Type I / III；
   * 大小：由"第一个让 $h<q+r_1$（且谱可行）的阶"决定；
3. 目前**没有**"阶差大小"的判据；只有两个结构性的必要条件（B.9 与 B.11 的 $\\delta\\ge1$）。

## 放弃原因

不适用（数据与对照完成）。**未做**：$q>n-r_1$ 区间内"谱障碍何时消失"的判据——需要
$\\Lambda$ 的谱与 $\\operatorname{im}H$ 的关系（B.10 只给出"障碍必在 $\\operatorname{spec}\\Lambda$ 上"）。

## 残留价值

* 一张三算例对照表，把"阶差"与"机制"分开；
* C4 实例的完整阶差（$q_{\\min}=4$），补上了"Type III 也能只差 1 阶"的实例；
* 明确了下一步的理论缺口：$q>n-r_1$ 区间内的谱障碍判据。

## 相关文件

- [proof/refuted/C4_type3_counterexample.md](../../../../proof/refuted/C4_type3_counterexample.md)
- [proof/h_formula/README.md](../../../../proof/h_formula/README.md)（B.11）
- [proof/fernando_2gap/README.md](../../../../proof/fernando_2gap/README.md)
- [workspace/q1_false/feasibility_geometry/attempts/13_gap2_case.md](13_gap2_case.md)
