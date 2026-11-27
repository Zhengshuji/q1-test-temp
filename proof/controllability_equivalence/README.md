# 命题：$(5b)\iff$ 可控性（Q5）

> **对应 docs 条目**：B.2（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

$$\text{问题：}(5b)\iff(S_\tau,\beta|_{\mathcal H})\ \text{可控}\ ?$$

## 状态（2026-10-27）

| 情形 | 结论 |
|---|---|
| $B\subseteq\mathcal U$ | **已证**（[theorem.md](theorem.md) 推论 3.2）|
| 一般情形 | **⚠️ 提法本身有缺陷**（§8）：$\beta(\mathcal H)\subseteq B$ 恒成立，故"输入"恒为零，"可控"退化 |
| 数值 | 旧的 16276/16276 与 c191 的 63/65 都指向同一结论：**"可控"是错的提法** |

## 文件

| 文件 | 内容 |
|---|---|
| [theorem.md](theorem.md) | 行空间刻画（引理 2.1）、命题 3.1、推论 3.2（$B\subseteq\mathcal U$ 时的等价）、§4 精确缺口、§6 下一步 |

## 一句话

$(5b)$ 是"行的张成维数 $=\rho$"；PBH 只能控制**模 $B$** 的部分。当 $B\subseteq\mathcal U$ 时两者重合（已证）；
否则差一个"$R_\lambda\cap B$ 的维数"——这就是 Q5 真正的缺口，也是下一步实验的靶子。