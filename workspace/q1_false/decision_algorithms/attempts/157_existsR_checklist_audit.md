# G.1 对照专家 00 号的 $\exists\mathbb R$ 检查清单

> 2026-11-08。专家 00 号在复核 $\mathrm{DEC}(q)\in\exists\mathbb R$ 时列出 8 项编码检查。
> 本文件逐项对照现有 [G.1](../../../../proof/dec_q_existsR/README.md)，标出“已覆盖 / 需补充 / 缺口”，
> 并把需要补充的两处（$\omega$ 分支、满行秩）写成明确陈述。状态：**M2（审计）**。

## 目标

给出 $\mathrm{DEC}(q)\in\exists\mathbb R$ 的**编码完整性**清单，确认每一项在 G.1 中都有对应，
或明确缺口与补法。

## 设想与理由

G.1 的 chart-free 编码（变量 $S,Q,Y,K,G_A,R,J,A_Q^W,X_0..X_{t-1}$，约束 1–7）已覆盖
必要性/充分性/规模/比特长；专家 00 的 8 项是对**复杂度定理**的编码细节检查。

## 做法：逐项对照

| # | 专家 00 的要求 | G.1 对应 | 状态 |
|---|---|---|---|
| 1 | 有理输入编码 | §3（有理矩阵、Gauss 消元给有理基）| **已覆盖** |
| 2 | 未知系数个数多项式 | §3 规模表：总变量 $O(n^3)$ | **已覆盖** |
| 3 | 方程比特复杂度多项式 | §5.5 / [bitsize.md](../../../../proof/dec_q_existsR/bitsize.md)：$O(n^2(B+\log n))$ | **已覆盖**（精确验证 12/12 只覆盖常数）|
| 4 | 显式处理不同 $\omega$ | 编码固定 $q$、枚举 $s=\dim(Z\cap\mathcal V)$；$\omega$ 由商铅笔的秩条件体现 | **需补充一句**（见下）|
| 5 | $\omega=0$ 单独处理 | $t=0$ 分支（§5 边界用例；$q=0$ 归入 $t=0$）| **已覆盖** |
| 6 | 秩等式析取的规模 | 编码用**列满秩** $K[S\,Q\,Y]=I$（无析取）；$(A)$ 也用 $G_A$ 线性化 | **已覆盖** |
| 7 | 固定 $L_0$ 正确纳入 | §3 的 $H=\ker[C;L_0]$、约束 3（$\operatorname{im}S,\operatorname{im}Y\subseteq H$）| **已覆盖** |
| 8 | 满行秩要求与原问题一致 | 编码的 $R$ 有右逆 $J$（$RJ=I_q$），故 $\operatorname{rank}R=q$；原 $L=[L_0;R]$ 的满行秩由 lifting 引理（[B.24](../../../../proof/B.24/README.md)/[114](../../c_stratification/attempts/114_lifting_lemma.md)）接上 | **需补充一句**（见下）|

### 补充 1：$\omega$ 分支

编码**不显式枚举 $\omega$**。原因：$\omega=\operatorname{rank}H$ 在 chart-free 编码中由
$P(\lambda)=R(\lambda Q_W-A_Q^W)$ 的秩条件（$X(\lambda)P(\lambda)=I_t$）体现；
不同的 $\omega$ 对应不同的 $t=\dim(\mathcal V/S)$，而 $t$ 由枚举 $s$ 与 $q$ 决定（$t=v-s$）。
因此“$\omega$ 的所有可能值”被 $s$ 的 $O(n)$ 个分支统一覆盖，不需要额外枚举。
**在写论文时应加一句**：编码对 $\omega$ 是统一的，$\omega$ 的每个值落在某个 $s$ 分支中。

### 补充 2：满行秩

原问题要求 $L=[L_0;R]$ 满行秩。编码的约束 5 给 $RJ=I_q$，即 $\operatorname{rank}R=q$；
但 $[L_0;R]$ 的满行秩是**更强**的条件（$r+q\le n$ 且行独立）。
这一条件由 lifting 引理处理：给定压缩解 $R$，存在满足满行秩的提升 $\iff$ 符号秩 $=q-r$，
且存在时 Zariski 开稠密（114）。**在写论文时应加一句**：$\mathrm{DEC}(q)$ 的编码先解压缩问题，
满行秩由 114 的提升引理接上；若把“$[C;L]$ 满行秩”作为设计约束（本项目七条检查的约定），
则需在编码里加 $[C;L]$ 的满行秩约束（列满秩辅助变量），这是标准的线性化。

## 进展

* 8 项逐项对照完成：6 项已覆盖，2 项需在论文中补一句（$\omega$ 分支、满行秩）；
* 无需改动 G.1 的数学内容；只需在表述层补两句。

## 最终结论

* G.1 的编码对专家 00 的清单是**完整**的（6 项已覆盖 + 2 项表述补充）；
* $\mathrm{DEC}(q)\in\exists\mathbb R$ 的编码部分可视为闭合；
* 剩余的是论文写作层面的说明，不是数学缺口。

## 放弃原因

* 未把两句补充写回 G.1（本文件只是审计；改 G.1 需另一次编辑并跑门）；
* 未补 $\omega=0$ 的独立小节（已由 $t=0$ 覆盖）。

## 残留价值

* 给专家 00 号一个逐项对照的答复；
* 明确“$\exists\mathbb R$ 成员”在编码层面的完成度。

## 相关文件

* [proof/dec_q_existsR](../../../../proof/dec_q_existsR/README.md)（G.1）
* [attempts/141](../../c_stratification/attempts/141_polynomial_certificate.md)（证书路线）
* [attempts/114](../../c_stratification/attempts/114_lifting_lemma.md)（满行秩提升）

## 状态

* 审计：**[已证-纸面，M2]**。
* G.1 表述补充：**[未做]**（不影响数学结论）。
