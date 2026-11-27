# feasibility_geometry —— 可行性几何（算法侧，历史）

> 状态：**历史**。上级：[q1_false](../README.md)。

对应本目录 `attempts/001–098` 那一段：增广族参数化、$\Omega$-抽样、闭包与 $q_0$ 扫描、
$Z$-生成、$q_{\min}$ 的早期统计。

## 已撤回 / 已修正

- 闭包不是精确最小维数；$q_{\min}\in\{\mathrm{cl},\mathrm{cl}+1\}$ 被反例推翻（间隔可达 2）；
- “$q_0$ 阶可行集总是薄”不成立；薄性只在部分分支出现。

## 保留价值

- 增广族的参数化与抽样脚本（`tools/verification/p1_family.py`、`z_generator.py`）；
- 这些是后来压缩链/子空间语言的前身，读历史时用。
