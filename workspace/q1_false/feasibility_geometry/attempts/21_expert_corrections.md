# 专家 2026-11-03 两条更正的核验与落实

## 目标

核验并落实专家对第四份简报的两条更正：

* **Correction A**：$q+r_1=n$ **不**推出 $h=n$（只能得 $\\delta\\ge0$）；$\\delta\\ge1$ 在 $q+r_1=n$ 时是
  Schubert **除子**（余维 1），不是空集。
* **Correction B**：$(5a)\\iff G_{\\mathcal Z}=\\mathcal Z^{\\perp}\\iff\\operatorname{rank}\\varphi=0$，
  **不是**"$\\operatorname{row}\\mathcal L\\subseteq G_{\\mathcal Z}$ 且 $\\operatorname{rank}\\varphi\\le p$"。

## 设想与理由

Correction B 的证明（专家给）：$\\operatorname{row}C\\subseteq G_{\\mathcal Z}$ 恒成立，且
$\\mathcal Z^{\\perp}=\\operatorname{row}C+\\operatorname{row}\\mathcal L$；若 $(5a)$ 成立则
$\\operatorname{row}\\mathcal L\\subseteq G_{\\mathcal Z}$，故 $\\mathcal Z^{\\perp}\\subseteq G_{\\mathcal Z}$，即相等。
反过来显然。于是 $(5a)$ **只依赖 $\\mathcal Z$**。

Correction A：由 $h=q+r_1-\\delta\\le n$，当 $q+r_1=n$ 时只能得 $\\delta\\ge0$；而 $\\delta\\ge1$ 是
Schubert 簇 $\\{T\\in\\operatorname{Gr}(q,N):T\\cap U\\ne0\\}$（余维 $n-q-r_1+1$），当 $q+r_1=n$ 时余维 1。

## 做法

[phi_rank_check.py](../../../../tools/verification/phi_rank_check.py)：
按定义计算 $\\varphi:\\mathcal Z^{\\perp}\\to\\mathbb C^n/(\\mathcal Z^{\\perp}+W)$ 的秩
（用 $\\mathcal Z^{\\perp}+W$ 的补空间取坐标），在 974 个 $(\\mathcal Z,\\mathcal L)$ 样本
（469 个 $(5a)$ 成立）上核验：

* $(5a)\\iff\\operatorname{rank}\\varphi=0$；
* $\\delta=q+r_1-h$ 与 $h=\\dim(\\mathcal Z^{\\perp}+W)$。

## 进展

| 检验 | 结果 |
|---|---|
| $(5a)\\iff\\operatorname{rank}\\varphi=0$ | **974/974**（469 个成立、0 不一致）|
| $\\delta=q+r_1-h$、$h=\\dim(\\mathcal Z^{\\perp}+W)$ | 0 失败 |

## 最终结论

1. **Correction B 成立**：$(5a)\\iff\\operatorname{rank}\\varphi=0\\iff G_{\\mathcal Z}=\\mathcal Z^{\\perp}$。
   这条**推翻了我上一轮（attempts/18）的"更正"**——$(5a)$ 其实**是** $\\mathcal Z$ 的函数
   （我此前的"$\\dim G_{\\mathcal Z}\\ge q$ 是必要条件、$(5a)$ 依赖补"是错的；
   那个弱条件只说明"能否放 $q$ 行"，不保证与 $C$ 一起张满 $\\mathcal Z^{\\perp}$）；
2. **Correction A 成立**：$q+r_1=n$ 时 $\\delta\\ge1$ 是 Schubert 除子（余维 1）；
   "公开例子 $q=4$ 处 $\\delta=0$"是**抽样证据**（1999/1999），**不是**维数必然；
   符号证明仍开放；
3. **89 实例统计不受影响**：那些统计用 `condA`（精确的 $(5a)$ 检验），不是用 $\\dim G_{\\mathcal Z}$ 近似的，
   所以数字本身有效；但"为何薄/厚"的解释要改用 $\\operatorname{rank}\\varphi=0$ 的语言；
4. Schubert 框架应当采纳：
   $$K=\\ker C,\\quad U=W/\\operatorname{row}C\\subset K^*\\ (\\dim a=r_1-p),\\quad
   T=\\mathcal Z^{\\perp}\\cap K^*\\ (\\dim q),$$
   $$\\delta=\\dim(U\\cap T),\\qquad \\delta\\ge1\\iff T\\cap U\\ne\\{0\\},$$
   当 $q+a\\le N=n-p$ 时 $\\delta\\ge1$ 的余维 $=N-q-a+1=n-q-r_1+1=d-a+1$。

## 放弃原因

不适用（核验与更正完成）。**未做**：公开例子 $q=4$ 处"全族 $\\delta=0$"的符号证明。

## 残留价值

* 两条更正都已在样本上核验，并被采纳；
* $(5a)$ 的**精确**形式（$\\operatorname{rank}\\varphi=0$）取代了上一轮的弱必要条件，
  这也让后续实验可以用"$\\operatorname{rank}\\varphi=0$"直接判定 $(5a)$（比 `condA` 更快）；
* Schubert 余维公式给出了"$\\delta\\ge1$ 何时薄"的定量语言。

## 相关文件

- [tools/verification/phi_rank_check.py](../../../../tools/verification/phi_rank_check.py)
- [proof/h_formula/README.md](../../../../proof/h_formula/README.md)（B.11，已补 Schubert 形式）
- [workspace/q1_false/feasibility_geometry/attempts/18_gz_criterion.md](18_gz_criterion.md)（被再更正的那一轮）
- [workspace/q1_false/feasibility_geometry/attempts/20_gz_rank_and_lemma.md](20_gz_rank_and_lemma.md)
- [archive/expert_correspondence/answer_2026-11-03_to_03.md](../../../../archive/expert_correspondence/answer_2026-11-03_to_03.md)（原文）
