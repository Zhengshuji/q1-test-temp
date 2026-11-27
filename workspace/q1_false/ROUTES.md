> **历史版本**（2026-11-26 结构重整前的 README），保留原来的路线一览与链接。
> 现行入口见同目录 [README.md](README.md)；本文件只作路线索引的历史记录。

# 方向 q1_false：证 $q_{\min}$ 多项式可算

> **现状：算术侧已成功（$P\in\mathbf P$），$(5b)$ 侧仍开放。**

## 路线一览

| # | 路线 | 文件 | 状态 |
|---|---|---|---|
| 1 | $q_{\min}=\dim V+1$ | [attempts/01_dimV_plus_1.md](../../archive/attempts_2026-10/q1_false/01_dimV_plus_1.md) | **推翻**（$n{=}5$ 反例）|
| 2 | 层公式（$q(\rho)$ 表）| [attempts/02_layer_formula.md](../../archive/attempts_2026-10/q1_false/02_layer_formula.md) | 部分有效 |
| 3 | 中间层 | [attempts/03_middle_layer.md](../../archive/attempts_2026-10/q1_false/03_middle_layer.md) | 有证书，不可放大 |
| 4 | $\rho_{ci}$ 闭式 | [attempts/04_rho_ci.md](../../archive/attempts_2026-10/q1_false/04_rho_ci.md) | **推翻** |
| 5 | 贪心闭包 | [attempts/05_greedy_closure.md](../../archive/attempts_2026-10/q1_false/05_greedy_closure.md) | **死** |
| 6 | 两值假设 | [attempts/06_two_values.md](../../archive/attempts_2026-10/q1_false/06_two_values.md) | **推翻** |
| 7 | $\rho=d_0{+}1$ 二次型判据 | [attempts/07_quadratic_criterion.md](../../archive/attempts_2026-10/q1_false/07_quadratic_criterion.md) | **有效**（46/47）|
| 8 | 层紧性引理 | [attempts/00_the_lemma.md](../../archive/attempts_2026-10/q1_false/00_the_lemma.md) | 部分有效 |
| 9 | $P$ 定理（算术侧）| [../proof/p_is_polynomial/](../../proof/p_is_polynomial/README.md) | **成功** |

## 结论（诚实）

$$q_{\min}=\min\{(\rho+c):(\rho,c)\ \text{可达}\}$$

- $\rho$ 侧 = $P$，**已多项式**（$O(n^4)$）；
- $(5b)$ 侧的可达集**没有**闭式：四个候选全被推翻（[../proof/refuted/](../../proof/refuted/README.md)）。

所以本方向剩下的唯一任务是 [docs/05](../../docs/05_open_questions.md) Q1：层判定的复杂度。

## tests/

`tests/` 保留该方向的可复现脚本，按主题分组（`rho1/ rho2_middle/ sigma/ zform/ scans/ verify/`）。