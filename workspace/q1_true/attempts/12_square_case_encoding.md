# 方阵情形（$q=t$）的硬度编码：系数映射的表达力

> 方向：$q1$ = 真（$\exists\mathbb R$-hard / NP-hard）。专家 2026-11-02 §5 认为这是**最有希望的落点**。

## 目标

在方阵情形 $q=t$，$(5b)$ 等价于

$$D_U(\lambda):=\det\bigl[U\mid P(\lambda)\bigr]\ \text{的**所有正次数系数为零、常数项非零**}$$

（专家 §5 的措辞；不能写成"非首项"）。目标：把某个已知 hard 问题（或其算术核）编码进这些系数，
并证明双向等价。

## 设想与理由

- Liu（arXiv:2610.00390）§4.1 已经把方程残差 $\ell_j^2-h_j$ 编进**系数**
  （用 $2\times2$ 块 $\det\begin{pmatrix}s^q+a&b\\-1&s^q-a\end{pmatrix}=s^{2q}+b-a^2$）；
- 我们的方阵条件恰好也是**系数级**条件（"正次数系数为零 + 常数项非零"），形状与 Liu 的构造一致；
- 若系数映射 $\Theta\mapsto(a_0,\dots,a_m)$ 足够表达，则可以把 ETR 的算术核编进来。

## 做法

1. **符号验证"次数上界"**：$D_U$ 对 $U$ 的每一列多重线性（行列式性质），
   故每个 $\lambda$-系数对 $U$ 的条目总次数 $\le r$（$r=\dim U$）。
2. 用 4×4 例子精确展开验证（脚本 `tools/verification/square_gadget_degree.py`）。
3. 由此得到可编码方程次数 $\le r$ 的**设计约束**。

## 进展

**已做**（符号计算，精确有理数）：取 $M(\lambda)=[g_1\mid g_2\mid c_3-\lambda e_3\mid c_4-\lambda e_4]$，
$g_1,g_2$ 为符号列，展开 $\det M(\lambda)$：

| 系数 | 总次数 | 对每个 $g$ 变量 | 单项数 |
|---|---|---|---|
| $a_0$ | 2 | 1 | 12 |
| $a_1$ | 2 | 1 | 10 |
| $a_2$ | 2 | 1 | 2 |

即每个变量次数 $\le1$、总次数 $\le r=2$ ✓。

**推论（设计层面）**：可编进系数的方程**次数 $\le r$**；编码 $z=xy$（次数 2）**需要 $r\ge2$**；
编码次数 $d$ 的算术需要 $r\ge d$。

**未做**：见下"残留价值"里的四项未解决点。

## 最终结论

待定（当前只得到一条**必要条件** $r\ge d$，不是充分条件）。

## 放弃原因

（暂不适用）

## 残留价值

即使编码失败，本文件留下四个必须回答的问题（也是"结构性障碍"的证明起点）：

1. **簿记未核对**：$r$（$U$ 的列数）与 docs/02 §H.1/H.2 里 $[U\mid P(\lambda)]$ 的 $w_m\times(r+t)$ 中的
   $r$ 是否同一个量——我没有逐条核对；
2. **可实现性未验证**：$M(\lambda)=[g_1\mid g_2\mid\ldots]$ 是否来自真实的观测器铅笔（$U$ 的列要落在
   $W/S$ 里、$P(\lambda)$ 要由 $A$ 导出）；
3. **实/复语义**：不能悄悄把实变量换成复变量（专家警告）；
4. `$r\ge d$ 只是必要条件`。

## 相关文件

- 专家复核记录：[archive/expert_correspondence/expert_review_2026-11-02/README.md](../../../archive/expert_correspondence/expert_review_2026-11-02/README.md)（§3、§5）
- 文献笔记：[literature/notes/LIU_2026_SOF_EXISTS_R.md](../../../literature/notes/LIU_2026_SOF_EXISTS_R.md)、
  [LOFBERG_2026_SOF_NP_HARD.md](../../../literature/notes/LOFBERG_2026_SOF_NP_HARD.md)
- 脚本：[tools/verification/square_gadget_degree.py](../../../tools/verification/square_gadget_degree.py)
- 上层：[docs/05](../../../docs/05_open_questions.md) Q1
