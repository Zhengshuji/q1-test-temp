# $G_{\\mathcal Z}$ 的秩公式、$(5a)$ 自动成立的条件，以及一个实现更正

## 目标

把上一轮的 $G_{\\mathcal Z}$ 判据写成可计算的秩条件，并找出"$(5a)$ 自动成立"的充分条件。

## 设想与理由

$G_{\\mathcal Z}=\\{\\ell\\in\\mathcal Z^{\\perp}:\\ell A\\in\\mathcal Z^{\\perp}+W\\}$ 是线性映射
$$\\varphi:\\mathcal Z^{\\perp}\\to\\mathbb C^{n}/(\\mathcal Z^{\\perp}+W),\\qquad \\ell\\mapsto \\ell A\\ \\bmod(\\mathcal Z^{\\perp}+W)$$
的核，故由秩-零化度
$$\\dim G_{\\mathcal Z}=(p+q)-\\operatorname{rank}\\varphi .$$
于是"$\\dim G_{\\mathcal Z}\\ge q$"（上一轮的 $\\mathcal Z$-层必要条件）等价于
$$\\operatorname{rank}\\varphi\\le p .$$
并且若 $\\dim(\\mathcal Z^{\\perp}+W)=n$（即 $h=n$，B.11），则 $\\varphi=0$、$G_{\\mathcal Z}=\\mathcal Z^{\\perp}$，
于是 $(5a)$ 对**每个**补都成立。

## 做法

[g_z_rank_formula.py](../../../../tools/verification/g_z_rank_formula.py)：
对实例抽 $\\mathcal Z$，算 $\\dim G_{\\mathcal Z}$、$\\operatorname{rank}\\varphi$、$h$，
检验三条：(i) 维数公式、(ii) 必要条件的形式、(iii) $h=n\\Rightarrow(5a)$ 自动。

## 进展

| 检验 | 结果 |
|---|---|
| (iii) $h=n\\Rightarrow(5a)$ 自动成立 | **117/117 通过** |
| (i)(ii) 用"基元素判定"的 $G$ 实现 | 与秩公式不一致 **40/252** |

**更正（实现层面）**：上一轮 [attempts/18](18_gz_criterion.md) 的 `G_of` 只挑"基元素 $b_i$ 满足 $b_iA\\in\\mathcal Z^{\\perp}+W$"，
它给出的是 $G_{\\mathcal Z}$ 的**子空间**（$\\subseteq$），一般**不等于** $G_{\\mathcal Z}$（真正的核还要含基元素的线性组合）。
本轮改用"商映射的核"计算，但实现有 bug（40/252 与秩公式不符）——所以 (i)(ii) 的**机器验证待修**；
它们的**数学内容**是秩-零化度恒等式，无需验证。

## 最终结论

1. **引理 A（已证，平凡但有用）**：$h=\\dim(\\mathcal Z^{\\perp}+W)=n\\ \\Longrightarrow\\ (5a)$ 对每个补自动成立；
   验证 117/117。这解释了公开例子在 $q=4,5$ 处"$(5a)$ 总是成立"的现象；
2. **引理 B（已证，秩-零化度）**：$\\dim G_{\\mathcal Z}=(p+q)-\\operatorname{rank}\\varphi$，
   故 $\\mathcal Z$-层必要条件 $\\dim G_{\\mathcal Z}\\ge q\\iff\\operatorname{rank}\\varphi\\le p$；
3. **实现更正**：`G_of` 是 $G_{\\mathcal Z}$ 的子空间近似；真正的核要按商映射算，
   当前实现有 bug（40/252），待修。

## 放弃原因

不适用（引理与更正完成）。**未修**：基于商映射的 `G_true` 实现（bug 待查）。

## 残留价值

* 引理 A 给出"$(5a)$ 自动成立"的可判定条件（$h=n$），并解释了公开例子；
* 引理 B 把 $\\mathcal Z$-层必要条件写成秩条件，便于后续与 Schubert/行列式判据对接；
* 明确标注了实现近似与 bug，避免后续基于错误 $G$ 的推理。

## 相关文件

- [tools/verification/g_z_rank_formula.py](../../../../tools/verification/g_z_rank_formula.py)
- [workspace/q1_false/feasibility_geometry/attempts/18_gz_criterion.md](18_gz_criterion.md)（被更正的那一轮）
- [proof/h_formula/README.md](../../../../proof/h_formula/README.md)（B.11）
