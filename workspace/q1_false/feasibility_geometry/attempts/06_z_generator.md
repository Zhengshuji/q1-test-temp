# Z-参数化：生成**任意阶**（含最小阶 $q_0$）的可行增广

## 目标

闭包路线（`omega_construct`）只能给"$\ge$ 闭包维数"的候选，**无法**在最小阶 $q_0$ 上生成候选；
而"$q_{\min}$ 是否等于 $q_0$"恰恰只看那一阶。本路线改用文献的几何参数化。

## 设想与理由

$$\mathcal Z=\ker\begin{pmatrix}C\\ \mathcal L\end{pmatrix}\subseteq\ker[C;L_0],\qquad \dim\mathcal Z=n-p-q .$$

反向：给定 $\mathcal Z$（$n\times d$，$d=n-p-q$，$\operatorname{im}\mathcal Z\subseteq\ker[C;L_0]$），
$[C;\mathcal L]$ 的行空间就是 $\mathcal Z^{\perp}$（维数 $p+q$，含 $\operatorname{row}C$）。
再按**本项目的要求**（$\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$）取
$\mathcal L=$ $L_0$ 的基 $+$ 从 $\mathcal Z^{\perp}$ 补足到 $q$ 行。

于是在 $\operatorname{Gr}(d,\,n-p-r)$ 中抽样即可得到**任意阶**的候选——包括 $q=q_0$。

## 做法

[tools/verification/z_generator.py](../../../../tools/verification/z_generator.py)：
`ker_cols`、`L_from_Z`、`sample_L_at_order`。

**单元测试**：取论文的 order-5 增广 $\mathcal L_5$，算 $\mathcal Z=\ker[C;\mathcal L_5]$（$d=1$），
再反构 $\mathcal L'$：$(5a)$ 成立、$(5b)$ 成立、$\varepsilon=[5]$ ✓（与 $\mathcal L_5$ 一致）。

## 进展

公开两阶差例子（$n=8,p=2,r=2,q_0=3$），每阶抽 40 个候选（每点最多 6 次尝试）：

| $q$ | 代数可行样本 | 其中 $(5b)$ 成立 |
|---|---|---|
| 3 | **0**（240 次尝试）| 0 |
| 4 | 40 | **0** |
| 5 | 40 | **40** |
| 6 | 1 | 1 |

## 最终结论

* $q=4$：**40 个独立的、代数可行的候选全部谱不可行**——比之前"20 个"更强，与论文"order 4 infeasible"一致；
* $q=5$：40/40 可行；$q=6$：可行（上端点）✓；
* $q=3$：240 次随机尝试没有一次满足 $(5a)$——说明 $(A)$ 在 $q_0$ 处是**薄集**
  （论文说每个图卡的 $(A)$ 族是"一参数"的，在 3 维图卡参数里是余维 2）。
  ⟹ 要判定 $q_0$ 阶必须**代数地**解 $(A)$，不能靠抽样。这正是专家 §7.5 的"混合方法"建议。

## 放弃原因

不适用（工具可用）。**未做**：$q=3$ 的完整 Grassmann 图卡分析（$\mathrm{Gr}(3,4)$ 的 4 个图卡，
每图卡把 $(A)$ 解成一参数族）——这需要符号消元/结式，本环境无 CAS。

## 残留价值

* 一个**任意阶**的候选生成器（闭包路线做不到最小阶）；
* 对公开例子的更强验证（$q=4$：40/40 失败）；
* 一个明确的量化结论：**(A) 在 $q_0$ 处是薄集**（0/240），这解释了为什么"抽样 + 过滤"永远判不了 $q_0$。

## 相关文件

- [tools/verification/z_generator.py](../../../../tools/verification/z_generator.py)
- [proof/fernando_2gap/](../../../../proof/fernando_2gap/README.md)
- [workspace/q1_false/feasibility_geometry/attempts/05_expert_followups.md](05_expert_followups.md)
