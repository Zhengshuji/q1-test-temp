# 论文写作检索表（PAPER_MAP）

> 用途：写/改论文时，按这张表查"这句话的证明在哪、能不能复用、引哪篇、有没有机器检查"。
> 只列**已存在的东西**；不存在的一律标 ❌，不要凭印象写。
> 唯一事实来源：`paper/current/others/q1_parametric_algorithms.tex`（论文）+ `workspace/q1_subspace/PROOF_fpt_ell.md`（完整纸面证明）。

---

## 0. 三份主文档的关系

| 文档 | 作用 | 状态 |
|---|---|---|
| `paper/current/others/q1_parametric_algorithms.tex` | 论文（IEEEtran，13 页） | 已编译 0/0/0；**尚未并入本轮 FPT$(\ell)$ 的结论** |
| `workspace/q1_subspace/PROOF_fpt_ell.md` | 完整纸面证明（引理 1–10） | 已闭合到"FIND 算术 FPT"，位复杂度待补 |
| `workspace/q1_subspace/AUDIT_fpt_k.md` | 审计过程（$k$ 版），含专家修正 | 历史记录，结论已被 PROOF 取代 |

---

## 1. 定理 / 引理 → 证明、Lean、实验、文献

| 命题 | 纸面证明 | Lean（`tools/lean/MyProof/`） | 精确实验 | 可引文献 |
|---|---|---|---|---|
| 压缩恒等式 $\operatorname{rank}[J;Q]=\operatorname{rank}J+\operatorname{rank}(QN)$ | PROOF §1 引理 1 | `Q1Compression.finrank_range_prod`（抽象）、`Q1RowSpace`（矩阵版桥） | c319 | 论文 §V |
| 条件只依赖 $W$：$\pi_2\subseteq\pi_1$、$\dim\pi_\lambda=\dim\pi_1$ | PROOF §1 引理 2（含复数化） | `Q1Pencil`（铅笔接口）、`Q1RowSpace.rank_fromRows_eq_rank_iff` | c320 | 论文 §V |
| 沙包 / 可实现性 | PROOF §1 引理 3 | `Q1Subspace.rowSpan_fromRows_left`、`mem_rowSpan_iff_exists_vecMul` | c320 往返 36/36 | — |
| 结构界 $\omega+1\le\dim W\le2\omega$ | PROOF §2 引理 4 | ❌（上界缺乘积维数引理；下界需特征值） | c320 | 专家 89/92 确认 |
| 单调 / 饱和 | PROOF §3 引理 5 | ❌ | c320 单调检查 | — |
| $q_{\min}=r_0+t_{\min}$，$t_{\min}\le2\ell$ | PROOF §3 引理 6 | ❌ | c322 压缩 36/36 | — |
| 换坐标到 $S$（$\ell$ 维） | PROOF §4 引理 7（措辞已按专家更正） | ❌ | c321 | — |
| 编码：$\sigma_\omega>0$、$\sigma_{\omega+1}=0$、$B^{\mathsf T}Bx=\mathbf e_1$ | PROOF §5 | ❌ | c316、c317 | 论文 §V–VI |
| $B$ 的尺寸 $\omega\binom{\nu}{\omega}\binom{\ell}{\omega}\times2\omega$ | PROOF §5 | ❌ | — | 专家 90 §4.4 |
| 分支剪枝 $1\le\omega\le\ell$、$\omega\le\nu\le2\omega$ | PROOF §5 | ❌ | c324 边界 | 专家 90/92 |
| 系数位高 $\tau_{\rm cert}\le\operatorname{poly}(\mathcal L)$ | PROOF §5.2 引理 8 | ❌ | ❌ 未数值核对 | — |
| 预处理代价 | PROOF §5.3 引理 10 | ❌ | — | — |
| Renegar 判定界 | PROOF §6 | ❌ | — | `foundations/Renegar_1992_JSC_PartII.pdf` |
| OPT 二分 | PROOF §7 | ❌ | c322 | — |
| 见证表示位长 | PROOF §8 引理 9 | ❌ | — | BPR 2006 **Thm 13.11**（§13.1） |
| 从一元表示恢复 $R$ | PROOF §8 | ❌ | — | 专家 92 §11 |
| FIND 位复杂度 | **❌ 未证** | — | — | 需要"位模型的采样点定理"，文献未找到 |

---

## 2. 参考文献 → 实际用在哪（不要多引）

| 文献 | 文件 | 用在哪一句 | 注意 |
|---|---|---|---|
| Basu–Pollack–Roy 2006 | `pdf/foundations/Basu_Pollack_Roy_2006_ARAG.pdf` | §13.1 **Thm 13.11**：样本点的次数 $O(d)^k$、系数位高 $\tau d^{O(k)}$、点数 $s^{O(k)}d^{O(k)}$、算术代价 | **第二版**：Ch.11 CAD、**Ch.13 Existential Theory**、Ch.14 QE、Ch.15 Roadmaps。专家 92 曾误记为 Ch.15，已核实 |
| Renegar 1992 Part II | `pdf/foundations/Renegar_1992_JSC_PartII.pdf` | 判定界 $B(\log B)(\log\log B)(sD)^{O(N)}$ | 这是**位**复杂度定理 |
| Renegar 1992 Part III | `pdf/foundations/Renegar_1992_JSC_PartIII.pdf` | 备用（QE 路线，本论文未用） | — |
| Fernando 2026a | `papers_2026/2609.33615.pdf` | 最小阶与前 $q_0$ 的刻画 | 论文 §I 已引 |
| Fernando 2026b | `papers_2026/2609.37992.pdf` | 逐阶刻画 + **Grassmann 图算法**（Algorithm 1）+ gcd 谱检验 | 参数化对比：每图 $d(m_L-d)=(n-p-q)(q-r)$ 个参数，随 $n$ 增长 |
| Darouach–Fernando 2025 | （notes 有） | 统一代数框架 | — |
| Zhang–Fernando–Darouach 2025 | `papers_2026/2307.08923.pdf` | 传感器选择 NP-hard；版式参照 | — |
| Löfberg 2026 | `pdf/complexity/Lofberg_2026_SOF_stabilization_NP_hard.pdf` | SOF NP-hard | — |
| Liu 2026 | `papers_2026/2610.00390.pdf` | SOF $\exists\mathbb R$-complete + 有效增益维数 FPT | 邻近方向 |
| Barkai–Shames 2026 | `papers_2026/2609.38728.pdf` | SOF NP-hard | — |
| Majumdar 2026 | `papers_2026/2602.14037.pdf` | 仿射秩最小化 $\exists\mathbb R$ | — |
| Berthomieu–Gillot–Safey El Din 2026 | `pdf/complexity/Berthomieu_2026_sample_points.pdf` | 单不等式的样本点位复杂度 | **单不等式 + 概率算法**，不能套到我们的多多项式公式 |

---

## 3. 可复用的技术模块（写论文时直接搬）

1. **压缩三元组**：$N$、$M=[N\ AN]$、$W=\operatorname{row}(LM)$，条件变成 $\pi_2(W)\subseteq\pi_1(W)$ 与 $\dim\pi_\lambda(W)$ 恒定（PROOF §1）。
2. **结构界**：$\omega+1\le\dim W\le2\omega$，把 $t$ 的搜索压到 $2\omega-s_0$（PROOF §2）。
3. **$\ell$ 归约**：$W\subseteq S\times S$、$S=\operatorname{row}(AN)$，于是所有计数用 $\ell$ 而非 $k$（PROOF §4）。
4. **商空间图参数化**：$Z(Y)=[E_0;\,[I_t\mid Y]E_Q]$，自动含 $W_0$（PROOF §5.1）。
5. **Cauchy–Binet 压缩**：$B^{\mathsf T}B$ 由列子集 $\binom{\ell}{\omega}$ 求和得到，列数恒为 $2\omega$（PROOF §5）。
6. **Bézout 度界**：$\deg g<\omega$ 的恒等式 $\iff$ 无极小公根（PROOF §8 与论文 Lemma 4/5）。
7. **二分求最小阶**：单调 + $t_{\min}\le2\ell$（PROOF §7）。

---

## 4. 精确实验清单（`tools/verification/`）

| 脚本 | 做什么 | 结论 |
|---|---|---|
| `c311_rank_consistency.py` | 秩一致性与约束检查 | 通过 |
| `c313_gram_indexing.py` | Gram 指标化简 | 通过 |
| `c316_gram_certificate_random.py` | Gram 证书随机实例 | 通过 |
| `c317_cauchy_binet_random.py` | Cauchy–Binet 恒等式随机核对 | 通过 |
| `c318_r0_linear_system.py` | $r=0$ 的线性系统 | 通过 |
| `c319_encoding_and_rowspace.py` | $\exists\mathbb R$ 编码与行空间 | 通过（40 族） |
| `c320_subspace_reduction.py` | 子空间归约：沙包/可实现性/结构界/往返/单调 | **0 failure**（12 实例，6 见证） |
| `c321_dimensional_test.py` | 可行性是否只由 $(k,d,s,r)$ 决定 | 未发现反例，但**弱证据**（采样） |
| `c322_opt_find.py` | OPT 压缩到自身 $t$ | **36/36 通过** |
| `c323_common_projection_core.py` | 迭代公共投影核 $S_*$ | $\dim S_*=\ell$（随机）；可行 $W$ 全在核内，**0 failure** |
| `c324_boundary_cases.py` | 边界：$k=0$、$m=0$、$W_0=0$、复公根铅笔 | **4/4 PASS** |

复用注意：`c320` 有 `feasible()` 与 `preimage()` 两个工具函数，后续脚本都 import 它。

---

## 5. Lean 模块（`tools/lean/MyProof/`，全图 9116 jobs，公理三条）

| 模块 | 内容 |
|---|---|
| `Q1Subspace.lean` | 行空间 = 行映射像、可实现性、沙包 |
| `Q1Compression.lean` | 压缩恒等式（抽象） |
| `Q1RankInclusion.lean` | 秩可加 $\iff$ 行包含 |
| `Q1RowSpace.lean` | $\operatorname{rank}=\dim\operatorname{row}$、$\operatorname{row}[A;B]=\operatorname{row}A\sqcup\operatorname{row}B$、第 2 条矩阵形式 |
| `Q1Pencil.lean` | 铅笔 $zH-H_A$（**两块独立**）、常秩两种写法等价、$z=0$ 处 $\operatorname{rank}H_A=\operatorname{rank}H$ |
| `Q1Projection.lean` | $\pi_1,\pi_2$、同维且包含 ⟹ 相等 |
| `Q1Step3.lean` | 第 3 条矩阵形式：$\operatorname{row}H_A=\operatorname{row}H$ |

**保真教训（写论文时别忘）**：$K_0=\ker[C;CA]$ **不一定** $A$-不变，所以 $H_A=LAN\ne HA$。铅笔必须写 $zH-H_A$，两块独立。

---

## 6. 不能写进论文的东西（缺口 / 未证）

| 项 | 状态 |
|---|---|
| FIND 的**位**复杂度 | ❌ 需要"位模型的采样点定理"，BPR 只给算术复杂度（其第 8 章明说位长估计不能由算术分析推出） |
| 结构界下界的 Lean | ❌ 需图 + 特征值 |
| $q_{\min}=r_0+t_{\min}$ 的 Lean | ❌ 纸面 3 行 |
| 引理 8 的逐项数值核对 | ❌ 未做（不影响阶） |
| 约化阶版本 | ❌ 未证（论文已声明只做行槽模型） |
| $S_*$ 作为主参数 | ❌ 只是结构性观察，不是算法改进（专家 90 §10.2 的 Claim A/B 区分） |

---

## 7. 写作顺序建议（按依赖）

1. §II 问题与记号（含**行槽模型**声明、输入输出模型）
2. §III 压缩（引理 1–3）
3. §IV 结构界（引理 4）
4. §V $\ell$ 归约与编码（引理 7、§5.1–5.2）
5. §VI 判定界（Renegar）
6. §VII 最小阶（引理 5–6 + 二分）
7. §VIII 构造（BPR Thm 13.11 + 恢复 $R$；**明确标注位复杂度待补**）
8. §IX 结论与限制（行槽模型、FIND 位复杂度）

论文目前 §II 还写着"对 OPT/FIND 不作声明"，与本轮结果不符，需要更新（本轮未改论文）。
