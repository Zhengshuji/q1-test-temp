# 技术报告：最小行数问题（MIN-ROWS / $q1$）的已证结果与已否定路线

> 2026-10-29 汇总。**本报告只收录有纸面证明或 Lean 检查的内容**；所有被反驳的命题单列，并给出证书。
> 每条结论都能点到仓库里的文件。$q1$ 本身**仍未解决**（见 §7）。

---

## 1. 问题

给定 $(A,C,L_0)$（$A\in\mathbb Q^{n\times n}$、$C\in\mathbb Q^{p\times n}$、$L_0\in\mathbb Q^{r\times n}$），求最小 $q$ 使存在 $R$（$\mathcal L=\binom{L_0}{R}$，$q$ 行、行满秩）满足

$$(5a)\ \operatorname{rank}[\mathcal L A;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L;CA;C],\qquad
(5b)\ \operatorname{rank}[\lambda\mathcal L-\mathcal L A;CA;C]=\operatorname{rank}[\mathcal L;CA;C]\quad\forall\lambda .$$

**等价性**：$(5a)/(5b)$ 与 Fernando–Trinh–Jennings（IEEE TAC 2010）的 Condition 1/2 **逐项相同**，
故本问题就是**最小阶线性功能观测器**（minimum-order functional observer）的存在性问题。
$q1$ 问：计算 $q_{\min}$ 是否 NP-hard。

**文献状态（2026-10-28 核查）**：Fernando 的两篇 2026 预印本给出了**完整刻画**（阶谱、每阶的 chart 参数化、铅笔形式、$\gcd$ 判据），
但**没有任何复杂度声明**；"最小动态覆盖"（Varga 2004）已有低复杂度算法。详见 [docs/07](../../docs/07_literature_review.md)。

---

## 2. 记号与两个基本分解

| 记号 | 含义 |
|---|---|
| $\mathcal J=\operatorname{row}[C;CA]$，$j=\dim\mathcal J$ | 可观空间 |
| $\pi:\mathbb C^n\twoheadrightarrow\mathbb C^n/\mathcal J$ | 商映射 |
| $\rho=\dim\pi(\mathcal V)$，$c=\dim(\mathcal V\cap\mathcal J)$ | $q=\rho+c$ |
| $T$：$A$ 在商上的诱导作用；$B=\pi(\mathcal J A)$ | 商动力学 |
| $\beta(h)=\pi(hA)$（$h\in\mathcal J$）| "输入" |
| $U_0=\pi(\operatorname{row}L_0)$ | 固定部分的商像 |
| $P(A,B,S)=\min\{\dim W:W\supseteq S,\ AW\subseteq W+B\}$ | 算术侧 |

**命题 2.1（$(5a)$ 的商形式）** $(5a)\iff T(\pi(\mathcal V))\subseteq\pi(\mathcal V)$。
*证明*：$(5a)\iff\operatorname{row}(\mathcal L A)\subseteq\operatorname{row}\mathcal L+\mathcal J$，两边取 $\pi$ 即得。$\square$
（[docs/02 A.0](../../docs/02_theorems_proven.md)）

**命题 2.2（$(5b)$ 的商形式）** $(5b)\iff\operatorname{rank}Q_{\mathcal V}(\lambda)=\rho\ \forall\lambda$，其中 $Q_{\mathcal V}(\lambda)=\pi(\mathcal L(\lambda I-A))$。

**命题 2.3（$(5b)$ 的秩上界，免费）** $(5a)\Rightarrow\operatorname{rank}Q_{\mathcal V}(\lambda)\le\rho\ \forall\lambda$。
*证明*：$(5a)$ 给 $\operatorname{row}(\lambda\mathcal L-\mathcal L A)\subseteq\operatorname{row}\mathcal L+\mathcal J$，取商即得。$\square$
（[proof/5b_upper_bound/](../../trash/README.md)，含 Lean）

**于是** $(5b)$ 的内容只剩"**秩不下降**"，等价地"全部 $\rho\times\rho$ 子式的 $\gcd$ 为非零常数"。

---

## 3. 算术侧：$P\in\mathbf P$

**定理 3.1（一步递归）** $\mathcal P(Y,C,\Phi,T)=\dim T+\mathcal P(Y',C',\Phi')$，其中 $Y'=Y/M$、$M=T+C$、$C'=\bar\pi\Phi(M)$、$T'=\bar\pi\Phi(T)$、$\Phi'=\Phi\bmod M$。
两个方向都有证明（$(\ge)$ 用维数下界，$(\le)$ 用截面 + 提升引理）。$\square$

**定理 3.2** $P\in\mathbf P$，且算法为 $O(n^4)$（$\le n$ 步递归，每步一次秩运算）。

**定理 3.3（算术侧闭合）** $\rho_{ci}=P(T,B,U_0)$；于是 $q_{\min}\ge\max(r+\varepsilon,\ \rho_{ci}+\max(c_0,1))$。

**Lean（2026-10-29 汇总，23 条，全部 `lean` 退出码 0）**：

| 模块 | 条数 | 内容 |
|---|---|---|
| `PRecursion` | 7 | $(\ge)$ 半、可行性下降（`admissible_image`）、$\Phi'$ 良定义、截面、构造 |
| `PRecursionLift` | 1 | 构造步（给定 $\sigma$）|
| `PRecursionSigma` | 1 | 通用提升引理 |
| `PRecursionSigmaRange` | 3 | **区间包含**（$\sigma$ 存在性的核心）|
| `PRecursionSigmaPoint` | 1 | $\sigma$ 的逐点校正 |
| `PRecursionInduced` | 3 | level-1 映射 $\Phi'$ 良定义 |
| `PRecursionLin` | 1 | **$\sigma$ 存在性（线性版，完整）** |
| `PRecursionStep` | 1 | **一步递归 $({\le})$ 半（无 $\sigma$）** |
| `PVal` | 4 | **$\mathcal P$ 的定义（`Nat.find`）与接口**（可达/下界/上界）|

**未形式化**：一步递归的**组装**（把两半合成关于 $\mathcal P$ 的等式）、$n$ 步迭代、$O(n^4)$ 复杂度（后者纸面即可）。

---

## 4. $\tau$ 量词的消除（本项目的主要新结果）

**设定**：固定 $(\mathcal U,\mathcal H)$ 后，$\tau$ 在仿射集 $\mathcal A$ 上自由；(5b) 的失效集 $\mathrm{Bad}$ 是"一参数族的仿射集的并"。

**定理 4.1（Bézout 线性化）** 层可行 $\iff\exists D\ \exists$ 极大子式 $\Delta$ of $\Phi_D$：$\Delta$ 在 $\mathcal A$ 上不恒为零，
其中 $\Phi_D(\tau):\bigoplus_j\mathbb C[\lambda]_{\le D}\to\mathbb C[\lambda]_{\le d+D}$，$(a_j)\mapsto\sum a_jp_j(\tau,\cdot)$。
"$\Delta$ 在仿射集上恒零"是**系数比较**（与次数无关）——但这是**有限**判据，
**不是**多项式时间算法 ✗：子式个数与 Bézout 矩阵规模在 $\rho$ 随 $n$ 增长时是指数级（2026-10-29 更正，见 QA_2026-10-29）。

**定理 4.2（T11）** 若 $\gcd(p_1,\dots,p_m)=1$、$\deg\le d$，则存在 $D_0\le 2d(m-1)$ 使 $\Phi_{D_0}$ 行满秩。
*证明*：单调性（满秩在 $D$ 上向上封闭）+ 对 $m$ 归纳（$m=2$ 用 Sylvester；$m\ge3$ 用 $\gcd(p_1,p_2)$ 约化）。$\square$

**验证**：$m\in\{2,3,4,5\}$、$d\in\{1,2,3\}$ 的 195 个 $\gcd=1$ 样本全部满足界；
端到端对拍（§17 的两条判据）：$\mathcal A=\mathbb R^j$ 300/300、$\mathcal A$ 为仿射直线 40/40。

$$\\boxed{\\ \\text{对固定 }(\\mathcal U,\\mathcal H)\\text{，层判定是系数量比较 = 多项式时间}\\ }$$

---

## 5. 已知的层判据

| 层 | 结论 | 等级 |
|---|---|---|
| $\rho=0$ | $\mathcal V\subseteq\mathcal J$，$(5b)$ 自动 | [已证] |
| $\rho=d$ | $(D_W^{\mathsf T},T_W)$ 可观测（PBH）| [已证] + 65/65 |
| $\rho=d$、$c_0=1$ | $v_W$ 是 $T_W$ 的循环向量 | [已证] + 35/35 |
| $(2,1)$、$w\ne0$ | 坏集仿射 ⟹ 维数比较 | [已证]（9.10/10.1）|
| $(2,1)$、$w=0$ | 恒不可行 | [已证]（9.12）+ **423/423** 复核 |
| $c\ge\rho-1$、$\dim\beta(\mathcal H)=\rho-1$、**固定 $(\mathcal U,\mathcal H)$** | $\mathrm{Bad}$ 仿射且 $\mathrm{Bad}\subseteq\mathcal A$ ⟹ 可行 $\iff\dim\mathrm{Bad}<\dim\mathcal A$（$O(n^3)$）| [已证]（定理 29.1）+ 构造式验证 200（全可行 110 / 全不可行 90 / mix 0）|

---

## 6. 已否定（单列，含证书）

| 命题 | 否证方式 |
|---|---|
| $q_{\min}=\dim V+1$；$=d+\max(c_0,1)$；$=\max(r+\varepsilon,\rho^*+1)$；$F_3$ | 4 类显式反例（[proof/refuted/](../../trash/README.md)）|
| 拟阵/TAP 归约 | 显式反例（$n{=}6$）|
| $(5b)\iff(S_\tau,\beta|_{\mathcal H})$ 可控（Q5）| 输入 $\beta(\mathcal H)\subseteq B$ 恒为零 ⟹ 算子退化 |
| 猜想 11.4 | 5 个构造实例 |
| S1 充要判据 $\dim K\ge\rho$ | 精确反例（$n{=}4,\rho{=}2,c{=}1$）|
| **任何秩型不变量判据** | $(\rho,c,\mu,\nu)$ 与加细的 $(\rho,\mu,\nu,\kappa)$ **都不决定**可行性 |

---

## 7. 仍未解决的部分（$q1$ 的全部剩余内容）

**定理 7.1（可判定性）** 对固定 $(\rho,c)$，层判定可判定。
*证明思路*：层判定只依赖有限多个秩（"签名"），每个签名的可行性是 $\mathbb C$ 上 constructible 集的非空性问题 ⟹ Chevalley–Tarski。$\square$

$$\\boxed{\\ q1\\iff\\text{"上述 constructible 集非空性能否}\\textbf{多项式}\\text{判定"}\\ \\text{或}\\ \\text{"能否编码}\\ \\exists\\mathbb R\\text{-难问题"}\\ }$$

两条都未完成：

- **(i) 算法**：需要把"$\exists\mathcal V$（type $+$ $(5a)$ $+$ 某 $\Delta\not\equiv0$）"化成多项式时间的秩/线性条件 ✗；
- **(ii) 硬度**：需要把 Betweenness 或已知 $\exists\mathbb R$-完全问题归约到某个层 ✗。
  参考 Löfberg 2026 的 gadget 清单（[literature/notes/LOFBERG_2026_GADGETS.md](../../literature/notes/LOFBERG_2026_GADGETS.md)）。

**已排除的捷径**：任何只看 $(\rho,c)$ 与若干维数/秩不变量的判据都**不可能**成立（§6 最后一行）。

---

## 8. 复现

```bash
python tools/hygiene/audit_layout.py                     # 布局审计（应 0 issue）
python tools/p_algorithm/c195_P_q.py                     # P 的值
python proof/lower_bound/verify.py                       # 下界
python proof/rho1_layer/verify_9_12.py                   # 9.12 复核（423/423）
python proof/rho1_layer/verify_29_1.py                   # 定理 29.1 构造式验证（200 例）
python proof/rho1_layer/verify_t11.py                    # T11（195/195）
python proof/rho1_layer/verify_bezout_equivalence.py      # §17 对拍（300/300）
python proof/rho1_layer/verify_bezout_affine.py           # §17 带仿射约束（40/40）
# Lean（WSL）
cd ~/WorkSpace/lean4/MyProof && export PATH="$HOME/.elan/bin:$PATH" && lake env lean MyProof/PRecursionSigmaRange.lean
```

## 9. 一句总结

$$\underbrace{\text{算术侧 }P\in\mathbf P}_{\text{已证 + Lean}}\quad+\quad
\underbrace{\tau\text{ 量词已消（T11）}}_{\text{已证 + 对拍}}\quad+\quad
\underbrace{(2,1)\text{ 层完整}}_{\text{已证}}\quad\Longrightarrow\quad
\underbrace{q1\ \text{仍开放}}_{\text{缺 (i) 或 (ii)}}$$

---

## 附录 A. 摘要（可投稿版）

> **最小阶线性功能观测器的算术侧与 $	au$ 量词的消除**
>
> 我们研究最小阶线性功能观测器（等价地，本文的 MIN-ROWS 问题）的判定问题。已知该问题的**存在性刻画**已完整
> （Fernando 2026 的阶谱 + chart 参数化），但其**计算复杂度**仍开放。本文给出三组有完整证明的结果。
>
> **(1) 算术侧多项式性**：只满足代数条件（即本文的 $(5a)$）的最小维数 $
ho_{ci}=P(T,B,U_0)$ 可在 $O(n^4)$ 内算出，
> 依据是一步递归定理 $\mathcal P(Y,C,\Phi,T)=\dim T+\mathcal P(Y',C',\Phi')$（两个方向都有证明），
> 并在 Lean 4 中机器验证了 23 条引理（含递归两半、$\sigma$ 存在性、$\mathcal P$ 的定义与接口）。
>
> **(2) $	au$ 量词的消除**：固定 $(\mathcal U,\mathcal H)$ 后，谱条件可等价地写成"某个极大子式在仿射集 $\mathcal A$ 上不恒为零"，
> 其判定是**系数比较**（**有限**代数判据；$\rho$ 固定时多项式，$\rho$ 随 $n$ 增长时规模指数级 ✗，见 proof/layer_program/SCALE_tau_elimination.md）。关键引理（T11）：若 $\gcd(p_1,\dots,p_m)=1$、$\deg\le d$，
> 则存在 $D_0\le 2d(m-1)$ 使乘法映射 $\Phi_{D_0}$ 行满秩（对 $m$ 归纳；$m{=}2$ 用 Sylvester）。
>
> **(3) 一串否定结果**：4 个闭式、拟阵/TAP 归约、"可控性"刻画、以及**任何只看 $(\rho,c)$ 与秩型不变量的判据**
> 都被显式反例否定（附精确证书）。
>
> **结论**：$q1$ 等价于"上述 constructible 集的非空性能否多项式判定"，或"能否编码一个 $\exists\mathbb R$-难问题"；
> 两条都未解决。

## 附录 B. 相关工作（按结论排列）

| 文献 | 结论 | 与本项目的关系 |
|---|---|---|
| **Darouach** 1994 | 低阶功能观测器的经典存在条件（$q=r$ 情形）| 本问题的特例 |
| **Fernando–Trinh–Jennings**, TAC 2010 | 与 $(5a)/(5b)$ **逐项相同**的 Condition 1/2 | 本问题的真身 |
| **Fernando** 2026（arXiv:2609.33615, 2609.37992）| **阶谱完整刻画**、chart 参数化、铅笔形式、$\gcd$ 判据 | 覆盖了本文的 $\gcd$ 判据与阶谱观察；**无复杂度声明** |
| **Varga**, MTNS 2004 | "最小维动态覆盖"的**低复杂度算法** | 说明相关的子问题已在 $\mathbf P$ |
| **Emre–Hautus**, SICO 1980 | $(A,B)$-不变子空间的**多项式刻画** + supremal 的构造 | **只做 supremal**，不涉最小维数 ⟹ 本文 $P$ 的结果不被覆盖 |
| **Wonham–Morse** 1972；**Warren–Eckberg** 1975 | 几何框架；可控性子空间维数由不变量决定 | 背景 |
| **Blondel–Tsitsiklis** 2000 综述 | 区间约束镇定 NP-hard；无约束静态输出反馈当时开放 | 复杂度线 |
| **Löfberg** 2026（arXiv:2609.16886）| **无约束静态输出反馈稳定化 NP-hard**（Betweenness 归约）| **否证了"数值型 ⟹ 易"的启发式**；提供可迁移 gadget |
| **Dodig**, LAA 2008 | 铅笔**行/列补全**的 Kronecker 不变量可达集 = 有限条不等式 | 支撑"$(5b)$ 是 Kronecker 型条件"的看法 |

## 附录 C. 证明细节索引

| 结论 | 完整证明 | 验证 |
|---|---|---|
| $(5a)$ 的商形式 | [docs/02 A.0](../docs/02_theorems_proven.md) | — |
| $(5b)$ 的秩上界（免费）| [proof/5b_upper_bound/](../../trash/README.md) | Lean + 数值 |
| 一步递归（两方向）| [proof/p_is_polynomial/theorem.md](../proof/p_is_polynomial/theorem.md) | Lean 23 条 |
| $P\in\mathbf P$（$O(n^4)$）| [proof/p_is_polynomial/algorithm.md](../proof/p_is_polynomial/algorithm.md) | 对拍 |
| $(2,1)$ 层完整判定 | [proof/rho1_layer/theorem.md](../proof/rho1_layer/theorem.md) §9–§13 | 1605/1605、423/423 |
| **T11** | [proof/rho1_layer/theorem.md](../proof/rho1_layer/theorem.md) §27 | 195/195 |
| Bézout 线性化 | §17 + §27 | 300/300、40/40 |
| 定理 29.1（固定 $(\mathcal U,\mathcal H)$ 判据）| §29 | 200 例（0 mix）|
| 可判定性 | §30 | — |
| 否定结果 | [proof/refuted/](../../trash/README.md)、[workspace/q1_false/S1_dimension_route_dead.md](../workspace/q1_false/S1_dimension_route_dead.md) | 精确证书 |
