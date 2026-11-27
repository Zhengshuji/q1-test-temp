# 01 · 记号

| 记号 | 含义 |
|---|---|
| $A,C,L_0$ | 系统矩阵、输出矩阵、固定行块（$r$ 行） |
| $\mathcal L=\binom{L_0}{R}$ | 待求的行堆叠，$q$ 行 |
| $\mathcal V=\operatorname{row}\mathcal L$ | 行空间，$\dim\mathcal V=q$（要求行满秩） |
| $S=\operatorname{row}L_0$ | 固定部分，$\dim S=r$ |
| $\mathcal J=\operatorname{row}[C;CA]$ | 观测空间，$j=\dim\mathcal J$ |
| $K=\ker[C;CA]$ | 不可观测/不可检测 kernel，$d=n-j$ |
| $\pi:\mathbb C^n\twoheadrightarrow\mathbb C^n/\mathcal J$ | 商映射 |
| $\rho=\dim\pi(\mathcal V)$ | $\mathcal V$ 在商里的维数 |
| $c=\dim(\mathcal V\cap\mathcal J)$ | $\mathcal V$ 落在 $\mathcal J$ 里的维数；$q=\rho+c$ |
| $c_0=\dim(S\cap\mathcal J)$ | 固定部分的 $\mathcal J$-部分 |
| $U_0=\pi(S)$ | 固定部分的商像，$\dim U_0=r-c_0$ |
| $d_0=r-c_0$ | $=\dim U_0$（$P$ 的下界层） |
| $\varepsilon\in\{0,1\}$ | $L_0$ 本身是否已是解（$\varepsilon=0$ 表示是） |
| $\rho^*$ | 可行解中 $\rho$ 的最小值（$=\rho_{ci}$ 当 $(5a)$ 层最小可行时） |
| $U=\pi(\mathcal V)$ | 约化坐标里的子空间（$\subseteq\mathbb C^n/\mathcal J$，$\dim=d$） |
| $H=\mathcal V\cap\mathcal J$ | 约化坐标里的"$\mathcal J$ 部分" |
| $T$ | $A$ 在商 $X/B$ 上的作用。$(5a)\iff\pi(\mathcal VA)\subseteq U$，且**只**有 $(5a)\Rightarrow T(U)\subseteq U+B$（反向不成立 ✗，见 docs/02 A.0）|
| $B$ | $=\pi(\mathcal J A)$，商里的"控制方向" |
| $M=T+C$（或 $M=U_0+B$） | $P$ 的递归里的"已占空间" |
| $P(A,B,S)$ | $\min\{\dim W:\ W\supseteq S,\ AW\subseteq W+B\}$ |
| $\rho_{ci}$ | $=P(T,B,U_0)$，即"只满足 $(5a)$ 的最小 $\rho$" |
| $q_{\min}$ | MIN-ROWS 的最优值 |
| $q(\rho)$ | 固定 $\rho$ 层的最优 $q$；$q_{\min}=\min_\rho q(\rho)$ |
| 层 | 固定 $\rho$（或固定 $(\rho,c)$）的解族 |
| 可达集 | $\{(\rho,c):\ \exists$ 满足 $(5a)\wedge(5b)$ 的解$\}$ |
| 算术侧 | $\rho_{ci}=P(T,B,U_0)$（只由秩数据决定，不涉 $(5b)$） |
| ci | conditioned invariant：$AW\subseteq W+B$ 的子空间（亦称 $(A,B)$-不变） |
| 见证 / witness | 一个显式可行的 $W$（或 $\mathcal L$），用于核验数值 |
| 证书 / certificate | 带矩阵数字的 JSON，可由脚本精确复核 |
| 可信基线 | `tools/verification/c164_trusted_baseline.py`（$(5a)/(5b)$ 的有理数精确判据） |

---

## 术语表（原 06_glossary，2026-11-09 合并）

| 术语 | 含义 | 出处 |
|---|---|---|
| **q1** | "计算 $q_{\min}$ 是否 NP-hard"这个复杂度问题 | [docs/00](00_problem.md) |
| **MIN-ROWS** | q1 的判定版本：$\exists\mathcal L$，$q\le k$，$(5a)\wedge(5b)$ | [docs/00](00_problem.md) §0.5 |
| **$(5a)$ / $(5b)$** | 两个秩条件（定义见 [docs/00](00_problem.md)） | — |
| **算术侧** | $\rho_{ci}=P(T,B,U_0)$：只由 $(5a)$ 决定的 $\rho$ 下界，只依赖秩数据 | [docs/04](04_structure.md) §4.2 |
| **层** | 固定 $\rho$（或 $(\rho,c)$）的解族 | [docs/04](04_structure.md) §4.3 |
| **可达集** | $\{(\rho,c):\exists\ \text{可行}\mathcal V\}$；$q_{\min}=\min(\rho+c)$ | [docs/04](04_structure.md) §4.1 |
| **$P(A,B,S)$** | $\min\{\dim W: W\supseteq S,\ AW\subseteq W+B\}$，$(A,B)$-不变版本的最小维数 | [proof/p_is_polynomial/](../proof/p_is_polynomial/README.md) |
| **ci / conditioned invariant** | $AW\subseteq W+B$ 的子空间（同 $(A,B)$-不变） | [docs/03](03_theorems_cited.md) 引用 7 |
| **c.s. / controllability subspace** | ci 的子类；Warren–Eckberg 的 open 是**这个**版本 | [docs/03](03_theorems_cited.md) 引用 3 |
| **见证 (witness)** | 一个显式可行的 $W$ 或 $\mathcal L$，用于核验数值 | [tools/p_algorithm/c197_P_witness.py](../tools/p_algorithm/c197_P_witness.py) |
| **证书 (certificate)** | 带矩阵数字的 JSON，脚本可精确复核 | [proof/refuted/certificates/](../proof/refuted/certificates/) |
| **可信基线** | $(5a)/(5b)$ 的有理数精确判据（`c164_trusted_baseline.py`） | [tools/verification/](../tools/verification/) |
| **薄集 (thin set)** | 解集是余维 > 0 的代数集；采样必错过 ⟹ 需"薄集搜索"或代数判定 | CLAUDE.md 纪律 3 |
| **$\mathbb F_p$ 伪影** | 小素数上"有解/无解"与 $\mathbb Q$ 不一致的现象（层数据、秩退化） | 见 [docs/04](04_structure.md) §4.4 的警告 |
| **$F_3$** | 曾被当作"最后幸存的闭式"$\max(r+\varepsilon,\rho^*+\max(c_0,1))$，已被 $n{=}4$ 反例推翻 | [proof/refuted/](../proof/refuted/README.md) |
| **$\sigma$** | $({\le})$ 证明里的修正映射 $\sigma:U'\to T\sqcup C$（纸面已证存在，Lean 部分） | [docs/05](05_open_questions.md) Q2 |

## 术语映射（专家 2026-11-04 §Q2/§Q5 的建议）

| 本文档用语 | 专家建议的英文名 | 条件 |
|---|---|---|
| Type I（计数障碍）| **dimension obstruction** | $h\ge q+r_1$ |
| Type III（谱障碍）| **spectral obstruction** | $h<q+r_1$ 且 $d_{\rm fin}>0$ |
| —— | uniform dimension criterion | 横截阶上 $s_0\ge r+r_1$ |
| 遮蔽/覆盖判据（条件性）| projective occlusion criterion | $\dim Y\ge q-r$ 且 $h=n$ |
| 谱可行 | spectral feasibility | $d_{\rm fin}=0$ |

说明：$\text{失败}=\text{dimension obstruction}\ \vee\ \text{spectral obstruction}$；
谱障碍是**通过维数检验之后**剩下的那一个（专家原话）。