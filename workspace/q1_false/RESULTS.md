# q1_false · 成果汇总（索引）

> 论文级结果只写 **Paper I / Paper II**（按根 `README.md` §1.5 的引用约定）；本地独立结果写等级与位置。
> 等级：`[已证]` / `[Lean]` / `[精确验证 n/N]` / `[数值]` / `[猜想]`。

## 论文（可靠基准）

| 成果 | 一句话 | 出处 |
|---|---|---|
| 固定 $q$ 的 XP | $\mathrm{DEC}(q)\in\mathrm P$，$\mathcal L^{O(q^2)}$ | **Paper I**, Theorem 1 |
| 固定 $\ell$ 的 FPT | $\exp(O(\ell^2\log(\ell+2)))\operatorname{poly}(\mathcal L)$，与 $r$ 无关；$r=0$ 多项式 | **Paper I**, Theorem 2 + Proposition 4 |
| $\exists\mathbb R$ 上界 | chart-free 编码，$O(n^3)$ 变量/方程 | **Paper I**, Theorem 5 |
| 最小阶 | $q_{\min}=r_0+t_{\min}$，$t_{\min}\le2\ell$ | **Paper II**, Proposition 1 |
| 谱下界 | $\operatorname{rank}[U_0;V_0]\le\omega\le s_0+t-1$ | **Paper II**, Proposition 2 |
| 单调/饱和 | $\mathrm{DEC}(q)\Rightarrow\mathrm{DEC}(q+1)$；饱和到 $\dim(T/W_0)$ | **Paper II**, Claim 5 |

## 本地独立结果

| 成果 | 一句话 | 等级 | 位置 |
|---|---|---|---|
| $P\in\mathrm P$ | 算术侧最小维数可多项式算（$P(A,B,S)$） | M3 | `proof/p_is_polynomial/` |
| $c=1$ 三定理 | 坏集闭 + 分量判据（A）；非特征层全坏（B）；Prop C/D | M3 纸面 | `c_stratification/attempts/344_...`、`proof/rho1_layer/` |
| $c=1$ 的 S3 缺口 | 移动根 = 唯一的 PIT，**未证**；故 $c=1\notin\mathrm P$ 尚不能声称 | — | `attempts/325`、`323` |
| $c=2$ 的像约化 | 行空间恒等式、可实现性两界、约化判据、单谱 poly | Paper IV 草稿 | `paper/current/paper_IV_c2.tex` |
| 层不单调 | $c=2$ 的反例（Paper IV 定理 16） | 已证-纸面 | `paper/current/paper_IV_c2.tex` |

## 没有的东西

- 一般 $q$（$q$ 随输入增长）的多项式算法；
- 一般 $k>\omega$ 的完整分量判据（只有 $c=1$ 的定理）；
- $c=1$ 的 PIT 闭合。
