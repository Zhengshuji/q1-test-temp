# $(5a)$ 的 $\\mathcal Z$-层判据：$\\operatorname{row}\\mathcal L\\subseteq G_{\\mathcal Z}$

## 目标

给出 $(5a)$ 在"固定 $\\mathcal Z$"下的**精确**判定，并纠正上一轮的过度概括。

## 设想与理由

上一轮（[attempts/17](17_z_determinacy.md)）在公开例子的 $q=4,5$ 上观察到"换补不改变判定"，
据此猜测 $(5a)$ 只依赖 $\\mathcal Z$。但本轮的推导指出：

$$(5a)\\iff \\operatorname{row}\\mathcal L\\subseteq G_{\\mathcal Z},\\qquad
G_{\\mathcal Z}:=\\bigl\\{\\ell\\in\\mathcal Z^{\\perp}:\\ \\ell A\\in\\mathcal Z^{\\perp}+W\\bigr\\}.$$

（$\\operatorname{row}\\mathcal L+W=\\mathcal Z^{\\perp}+W$，所以 $(5a)$ 就是"每一行 $\\ell$ 的 $\\ell A$ 落在 $\\mathcal Z^{\\perp}+W$ 里"。）

$G_{\\mathcal Z}$ 只依赖 $\\mathcal Z$，但"$\\operatorname{row}\\mathcal L\\subseteq G_{\\mathcal Z}$"**依赖补的选取**——
所以 $(5a)$ **不是** $\\mathcal Z$ 的函数。

## 做法

[g_z_criterion.py](../../../../tools/verification/g_z_criterion.py)：
对 `diag-distinct-n7`（$n=7,p=2,r=1,q_0=2$，$q_0+r_1=6<n$ ⟹ $(5a)$ 是真条件）抽 300 个 $\\mathcal Z$，
逐个算 $G_{\\mathcal Z}$、构造 $\\mathcal L$、比较"$(5a)$"与"$\\operatorname{row}\\mathcal L\\subseteq G_{\\mathcal Z}$"，
并统计 $(\\dim G_{\\mathcal Z}\\ge q_0,\\ (5a))$ 的联合分布。

## 进展

| 检验 | 结果 |
|---|---|
| $(5a)\\iff\\operatorname{row}\\mathcal L\\subseteq G_{\\mathcal Z}$ | **300/300 一致**（0 不一致）|
| $(\\dim G_{\\mathcal Z}<q_0,\\ (5a)$ 成立$)$ | **0** ⟹ $\\dim G_{\\mathcal Z}\\ge q$ 是必要条件 |
| $(\\dim G_{\\mathcal Z}\\ge q_0,\\ (5a)$ 成立$)$ | 6 |
| $(\\dim G_{\\mathcal Z}\\ge q_0,\\ (5a)$ 不成立$)$ | 12（补没落在 $G_{\\mathcal Z}$ 里）|

**改进的构造**（在 $G_{\\mathcal Z}$ 内部取 $\\mathcal L$ 的行）：对 $\\dim G_{\\mathcal Z}\\ge q_0$ 的 13 个 $\\mathcal Z$，
5 个成功构造出 $(5a)$-可行的 $\\mathcal L$（另 8 个因 $[C;L]$ 秩不足失败），这 5 个的 $(5b)$ 全部失败
（与该实例 $q_0$ 阶不可行一致）。

## 最终结论

1. **$(5a)$ 的精确形式**：$\\operatorname{row}\\mathcal L\\subseteq G_{\\mathcal Z}$——**可以**通过选补来满足或破坏；
2. **$\\mathcal Z$-层的必要条件**：$\\dim G_{\\mathcal Z}\\ge q$（否则任何补都不行）；
3. **更正**：上一轮"$(5a)$ 只依赖 $\\mathcal Z$"**是错的**；那时之所以看不出差别，
   是因为那些实例的 $G_{\\mathcal Z}$ 足够大（公开例子在 $q=4,5$ 处 $\\mathcal Z^{\\perp}+W=\\mathbb C^n$，
   $(5a)$ 对**任意** $\\mathcal L$ 都自动成立）；
4. 这也解释了此前"$q_0$ 阶只有 1 个样本"的现象：大多数 $\\mathcal Z$ 的 $\\dim G_{\\mathcal Z}<q$（282/300）。

## 放弃原因

不适用（判据与纠正完成）。**未做**：$G_{\\mathcal Z}$ 的几何（何时 $\\dim G_{\\mathcal Z}\\ge q$ 可满足）的系统刻画。

## 残留价值

* 一个**精确**的 $(5a)$ 判据（$\\mathcal Z$-层 + 补的约束），并把"薄性"定量为 $\\dim G_{\\mathcal Z}$ 的分布；
* 一个**改进的构造器**：在 $G_{\\mathcal Z}$ 内取行，比"从 $\\mathcal Z^{\\perp}$ 的基贪心"更容易命中；
* 明确纠正了上一轮的过度概括，避免后续基于错误结论的推理。

## 相关文件

- [tools/verification/g_z_criterion.py](../../../../tools/verification/g_z_criterion.py)
- [workspace/q1_false/feasibility_geometry/attempts/17_z_determinacy.md](17_z_determinacy.md)（被更正的那一轮）
- [proof/h_formula/README.md](../../../../proof/h_formula/README.md)（B.11）
