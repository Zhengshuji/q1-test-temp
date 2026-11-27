> **2026-11-10 更新**：本文件是历史工作清单/路线记录；当前状态与下一步见 [STATUS.md](../../../STATUS.md)，项目脉络见 [HISTORY.md](../../../HISTORY.md)，当前送审件见 [83](../../../workspace/for_expert/archive/83_project_consolidation_q1_roadmap.md)。

# 09 · 工作清单（做过什么 / 别再重复）

> 目的：一眼看清**哪些已经做过**（成功或失败），避免重复劳动。
> 每条给：结论一句话 + 状态 + 文件指针。细节不在本文。
> 来源：`ATTEMPTS.md`（总表）、`proof/`、`workspace/*/attempts/`、`archive/attempts_2026-10/`、`archive/attack_A2V0/`。
> **更新规则**：新增一条工作 → 在对应小节加一行；状态只写 成功 / 推翻 / 死 / 受阻 / 未完 / 记录。

---

## A. 已定的技术结果（可引用，勿重做）

| # | 结论 | 状态 | 位置 |
|---|---|---|---|
| A1 | $(5b)\iff d_{\rm fin}=0\iff\sum_j\varepsilon_j=\operatorname{rank}\mathcal L$ | 成功 | `02_theorems_proven.md` B.6–B.8 |
| A2 | Toeplitz 判据 $\nu_s=(s+1)m-s$；序列由二阶差分恢复 | 成功（66/66）| `proof/toeplitz_criterion` |
| A3 | 谱障碍定域：只需查 $\operatorname{spec}\Lambda$；坏 $\lambda$ 可复 | 成功（3/3）| `proof/eigenvalue_confinement` |
| A4 | 零指标计数 B.9：零左指标 $=2p-r_1$、非零 $=q+r_1-h$；$(5b)\Rightarrow h<q+r_1$ | 成功（698/698）| `proof/left_index_count` |
| A5 | $h=\dim(\mathcal Z^\perp+W)=s_0+\dim\pi(V')$ | 成功（495/495）| `proof/h_formula` |
| A6 | **（2026-11-04 改为无条件式）** $h=s_0+q-\dim(R\cap S)$，故 $h\le s_0+q-r$；$s_0<r_1+r$ 时**无** Type I | 成功（B.11c）| `docs/02` B.11c；`08_results` §3 |
| A7 | $h=n\Rightarrow(5a)$ 自动 | 成功（117/117）| 同上 |
| A8 | C4 整族不可行（比例性 + $\mathbb P^1\to\mathbb P^1$ 满射）| 成功 | `proof/refuted/C4_type3_counterexample.md` |
| A9 | 遮蔽充分条件 $\dim\overline{\Phi}\ge q-r$；$n=6$ 上 $\dim Y=1=q-r$ | 成功 | 同上 + `workspace/augmentation_family/attempts/30,32,33` |
| A10 | 七条一致性检查模块（秩/维数/$CZ=LZ=0$/$(5a)$ 等价/目标秩=法秩/gcd=Toeplitz/域）| 成功 | `tools/verification/consistency_checks.py` |
| A11 | 编码规模：$O(n^3)$ 变量、$O(n^3)$ 方程、次数 $\le n$ ⟹ 多项式规模归约到 ETR | 成功 | `proof/dec_q_existsR/bitsize.md` |
| A12 | 商等价定理 + $d=0$ 边界（铅笔秩 $=r+t$；方阵 $\iff q=t$）| 成功 | `proof/quotient_equivalence` |
| A13 | $P\in\mathbf P$（算术侧 $O(n^4)$）| 成功 | `proof/p_is_polynomial` |
| A14 | $r=2$ 双向量问题：$m\le4$ 或 $\ell$ 大时恒有；$m\ge5,\ell\le3$ 有算法 | 成功（部分域）| `proof/bivector_r2` |
| A15 | Lean 内核：`kron_block_factor`、`descriptor_ker` 等 | 成功（52/52、146 声明）| `tools/lean/` |

## B. 已推翻的猜想 / 公式（勿再提出）

| # | 陈述 | 反例 | 位置 |
|---|---|---|---|
| B1 | $q_{\min}=\dim V+1$ | $n=5$ | `proof/refuted` R1 |
| B2 | $q_{\min}=\max(r,\rho^*+1)$ 及加 $\varepsilon$ 的变体 | $S=\mathcal J$ 时 $q_{\min}=n$ | R3 |
| B3 | 四闭式 $F_3=\max(r+\varepsilon,\rho^*+\max(c_0,1))$ | $n=4$ | R4 |
| B4 | 两值假设 $\rho^*\in\{\rho_0,\dim V\}$ | 中间层 | `attempts_2026-10/q1_false/06_two_values.md` |
| B5 | $\rho_{ci}$ 闭式 / "最小 ci 唯一" | $\mathbb Q$ 反例 | 同上 `04_rho_ci.md` |
| B6 | 贪心闭包 = 最小 | 20/24 | 同上 `05_greedy_closure.md` |
| B7 | 闭包 $+1$（$q_{\min}=\mathrm{cl}+1$）| 公开例子 4 vs 3 | `proof/refuted/C1_closure_plus_one.md` |
| B8 | "$h<q_0+r_1$ 充分"（猜想 T）| C4 反例 | `proof/refuted/C4_...` |
| B9 | $(T)$：坐标解不劣于非坐标解 | $n=6$ | `attempts_2026-10/q1_true/01_matroid_tap.md` |
| B10 | 可控性刻画 $(5b)\iff(S_\tau,\beta\vert_H)$ 可控 | 输入算子恒零 | `proof/controllability_equivalence` |
| B11 | 专家建议的 $\operatorname{rank}\mathcal L\le q+2p-h$ | $n=6$、$\varepsilon=[5,1]$ | `STATUS`（R21）|
| B12 | "$(5a)$ 只依赖 $\mathcal Z$"——**最终结论是它成立**（$\operatorname{rank}\varphi=0$）；中途两次更正 | — | `attempts/17,18,21` |

## C. 已死的路线（勿在没有新想法时重走）

### C.1 硬度（证 $q1$ 真）

| # | 路线 | 死因 | 位置 |
|---|---|---|---|
| C1-1 | 拟阵 / TAP | $(T)$ 有 $n=6$ 反例；圈空间不可实现 | `attempts_2026-10/q1_true/01_matroid_tap.md` |
| C1-2 | 图 / 超图归约（CYCLIC-COVER）| 坐标层是**松弛**，硬度不传递 | 同上 `05_graph_reduction.md` |
| C1-3 | min-rank / 覆盖 / 反馈设计（20 条）| 全落 Lovitz 公开问题；$C=I$ 时结构被抹平；$(5b)$ 是开条件 | 同上 `02_minrank_cover.md` |
| C1-4 | Z 形式（最大化子空间维数）| (8c) 缺项、被实例打停 | 同上 `03_z_formulation.md` |
| C1-5 | 谱切割 / 块结构 | $\mathbb F_3$ 上是域伪影 | 同上 `04_speccut.md` |
| C1-6 | 混合情形（代数⊗谱）| 无可用组合对象 | 同上 `06_mixed_case.md` |
| C1-7 | 线性截面秩一（Lovitz）| 受阻：公开问题 | 同上 `07_linear_section.md` |
| C1-8 | 层判定 NP/$\exists\mathbb R$-难的具体归约 | 四卡点（型层非乘积、闭集命中、正维族、$\mathbb F_p$ 不可提升）| `workspace/q1_true/attempts/10_hardness_attempt.md` |
| C1-9 | 静态输出反馈（Löfberg Betweenness）传递 | 提出未做 | `workspace/q1_true/attempts/08_sof_betweenness.md` |
| C1-10 | 坐标行限制当归约靶子 | **逻辑错误**：收紧解集不传递困难性 | `workspace/q1_false/feasibility_geometry/attempts/37_coordinate_rows.md`（已更正）|

### C.2 多项式算法（证 $q1$ 假）

| # | 路线 | 状态 | 位置 |
|---|---|---|---|
| C2-1 | 层公式 + 紧性 | 部分有效（70 对中 69 紧）| `attempts_2026-10/q1_false/02_layer_formula.md` |
| C2-2 | 二次型判据 $\rho=d_0+1$ | 有效 46/47 | 同上 `07_quadratic_criterion.md` |
| C2-3 | 中间层 / 层紧性引理 | 部分有效 | 同上 `03_middle_layer.md`、`00_the_lemma.md` |
| C2-4 | 地板 $\rho_{ci}$ vs 真实 $\rho^*$ | 地板不紧 | 同上 `08_floor_gap.md` |
| C2-5 | S1 区（$c\ge\rho-1$）| 维数路线已死 | `workspace/q1_false/STRATEGY`、`proof/rho1_layer/theorem.md` §21–25 |
| C2-6 | $\tau$ 量词消除 | 完成（判据层面）| 同上 §17–19、§27 |

### C.3 其它（$(5a)$ / Kronecker / 描述系统）

| # | 路线 | 状态 | 位置 |
|---|---|---|---|
| C3-1 | 五分支（A-1…A-5、B-1…B-5、D、E-1）| 完成/部分，详见总表 | `ATTEMPTS.md` 顶部 |
| C3-2 | Smith 形 / 行列式因子判据 | 成功（84+86 例 0 不一致）| `tools/verification/poly_smith.py` |
| C3-3 | 适配基（$q=t$ 方阵）| 完成 | `attempts_2026-10` 支4 |
| C3-4 | 截断对象 $D(K_S)$ vs $K_S$ | 仅 $q\ne t$ 域 | 支5 |
| C3-5 | 描述系统右指标 = $Q_L$ 左指标 | 成功 | `proof/descriptor_reduction` |
| C3-6 | 无穷初等因子全 1 次（B.7）| 成功（151/151）| `proof/t4b_infinite_divisors` |

## D. 本会话（2026-11-03）新增的工作

| # | 工作 | 结论 | 位置 |
|---|---|---|---|
| D1 | 阶差分布（结构化实例）| 13/6/1（0/1/2 阶差）| `attempts/12,13` |
| D2 | 自有阶差 2 实例 | 两阶均 Type I（B.9）| `attempts/13` |
| D3 | $q_0+1$ 禁闭的大样本 | 1999/1999 全 $h=8$ | `attempts/14` |
| D4 | 公开例子两阶都是 Type I + 显式 $L$ | 成功（已证）| `attempts/22`、`proof/fernando_2gap/fernando_type.py` |
| D5 | 失败类型由整数决定 | 成功（495/495）| `attempts/23` |
| D6 | 谱区统计：一般实例无 Type III | 1501/1501 | `attempts/24`（含更正）|
| D7 | C4 整族不可行（含比例性）| 成功 | `attempts/26,34` |
| D8 | Type III 只在边界 $r_1=p+r$ | 4/4（小样本）| `attempts/28` |
| D9 | "无解实例"异常 | **撤回**（专家给出 $q=3$ 解）| `attempts/29` |
| D10 | 遮蔽判据的修正与适用范围 | 成功（部分）| `attempts/30,32,33` |
| D11 | 逐阶穷举判定（阶区间 $[q_0,n_0-p]$）| 成功（工具）| `attempts/31`、`tools/verification/qmin_exact.py` |
| D12 | 零空间铅笔判据的实现与三路交叉 | 成功（6/6）| `attempts/34` |
| D13 | 七条一致性检查 | 成功 | `attempts/35` |
| D14 | $r=1$ 的 $\exists\mathbb R$ 表述 + 非仿射实验 | 成功（否定捷径）| `attempts/36` |
| D15 | 坐标行限制的结构数据 | 成功（但非归约靶子）| `attempts/37`（已更正）|
| D16 | 对外简报 01–06（06 为合并版）| 已提交/待回复 | `workspace/for_expert/` |
| D17 | 短 note 草稿骨架 | 草稿（已归档） | `archive/paper_drafts/workspace_2026-11/paper_draft/00_note_draft.md` |
| D18 | 带证书的逐阶判定 + 谱域参数 + 七条检查接线 | 成功 | `attempts/38`、`tools/verification/decide_with_certificate.py` |
| D37 | 阶差的算术判据（$\dim(\operatorname{row}L_0\cap W)\le p$，18/18 无假阳性）| 完成（73/74）| `attempts/57`、`tools/verification/gap_arithmetic.py` |
| D36 | 见证优先扫描：89 实例 48 s，74 个上界 + 阶差$\leftrightarrow r$ 规律 | 完成（上界）| `attempts/56`、`tools/verification/witness_scan.py` |
| D35 | $q_{\min}$ 证书化扫描（有阶差，但单例达 945 s）| 部分（性能受限）| `attempts/55`、`tools/verification/qminsweep.py` |
| D34 | $\theta$ 上行列式消元（C4 第四证；26 实例 24 个证书化）| 完成（可用）| `attempts/54`、`tools/verification/joint_theta.py` |
| D83 | B.35：两阶段流程（可靠、省 44%）+ $\Delta$ 剖面 | 完成（实验）| `docs/02` B.35、`attempts/98`、`tools/verification/{two_stage,kr_ranks}.py` |
| D82 | B.34：最窄中间层 $r_1=p+2$ 的统计 | 完成（统计）| `docs/02` B.34、`attempts/97`、`tools/verification/narrow_intermediate.py` |
| D81 | B.31 可行性必要条件 + 中间层可行证书 | 完成 | `docs/02` B.31、`attempts/96`、`proof/delta1_feasible/` |
| D80 | B.30：$\delta$ 三分（中间层可行）+ $(2,2)$ 阶差 0/1 | 完成（含观察）| `docs/02` B.30、`attempts/95`、`tools/verification/{delta_scan_22,qmin_22}.py` |
| D79 | B.29：$p=1$、任意 $r$ 的 $q_{\min}=n-1$ | 完成 | `docs/02` B.29、`attempts/94`、`tools/verification/p1_general_r.py` |
| D78 | **Class I 的 $q_{\min}=n-1$ 定理**（B.26+B.27）| 完成 | `docs/02` B.26/B.27、`attempts/93`、`tools/verification/{b26_class_I_only_Z,b27_check}.py` |
| D77 | Workstream A：B.25 矩形铅笔判据 + WorkA.lean 秩公式 | 完成 | `docs/02` B.25、`attempts/92`、`tools/lean/MyProof/WorkA.lean` |
| D76 | B.23 + B.24：谱侧统一因子化与显式判据（Class I $d\ge2$ 的形态）| 部分完成 | `docs/02` B.23/B.24、`attempts/91`、`tools/verification/{b23_factorization_rank,class_I_low_orders}.py` |
| D75 | B.22 等号障碍（专家证明）+ B.8b/B.19/B.11d 修正 + `B22.lean` | 完成 | `docs/02` B.22、`attempts/90`、`tools/lean/MyProof/B22.lean` |
| D74 | B.19 顶层与等号互斥（已证）+ 等号情形三次扫描 | 部分完成 | `docs/02` B.19、`attempts/89`、`tools/verification/equality_{case,search}.py`、`top_stratum2.py` |
| D73 | 专家审稿修订：B.8a/B.8b 拆分、等号未证、标签制、公理审计 | 完成 | `docs/02`、`attempts/88`、`tools/verification/equality_case.py`、`tools/lean/MyProof/AxiomAudit.lean` |
| D72 | `Logic.lean`：B.11d/B.18e 的逻辑骨架（exit=0）| 完成 | `tools/lean/MyProof/Logic.lean`、`attempts/87` |
| D71 | `Dims.lean`：B.11c/B.18c 的记账内核（exit=0）| 完成 | `tools/lean/MyProof/Dims.lean`、`attempts/87` |
| D70 | 三条核心判据的 Lean 内核（`Criterion.lean`）| 完成 | `tools/lean/MyProof/Criterion.lean`、`attempts/87` |
| D69 | B.18e 第 3 条已证 + Lean 内核（PsiImage.lean）| 完成 | `docs/02` B.18e、`attempts/86`、`tools/lean/MyProof/PsiImage.lean` |
| D68 | B.18e 拆三条：两条已证（$z\in V$ 不可容许、$z_2\ne0$ 自动可容许）| 完成（部分）| `docs/02` B.18e、`attempts/85` |
| D67 | Class I 的 $d=1$ 分类（猜想 B.18e，0/44 证据）| 完成（猜想）| `docs/02` B.18e、`attempts/84`、`tools/verification/class_I_d1.py` |
| D66 | 撤回 im ψ=ker c（专家反例）+ B.18d 循环坐标刻画 | 完成 | `proof/refuted/psi_image_ker_c.md`、`docs/02` B.18d、`tools/verification/psi_image_canonical.py` |
| D65 | B.18c：$d=1$ 判据 = 像包含；精确成员判据（229/229）；$d=1$ 无可行（240 样本）| 完成 | `docs/02` B.18c、`attempts/83`、`tools/verification/membership_test.py` |
| D64 | Class I：终阶必然可行（B.18b，589/589）+ $q_{\min}=n-1$（扫描）| 完成 | `docs/02` B.18b、`attempts/82`、`tools/verification/class_I_scan.py` |
| D63 | Class I（$p=r=1$）结构测绘 + 降维 $\rho=q-1$ | 完成（测绘）| `docs/02` B.18、`attempts/81` |
| D62 | B.17 永久核 + 商铅笔判据（1513/1513）+ 六点符号验证文档 | 完成 | `docs/02` B.17、`attempts/80`、`tools/verification/quotient_pencil.py` |
| D61 | J5 对照实验：结构化 vs 随机 $V,K$ 的失败率 67% vs 25% | 完成 | `attempts/79`、`tools/verification/avoid_control.py` |
| D60 | "中间层永不失败"猜想被否决（$s$ 只约束 $\dim U$）| 完成（否定）| `attempts/78`、`tools/verification/middle_counterexample.py` |
| D59 | 中间层：$A(V\cap\mathcal Z)\subseteq\mathcal Z$ + 显式反例 | 完成 | `docs/02` B.16b、`attempts/77` |
| D58 | 分层判据 B.16（按 $\operatorname{rank}(J_{\mathcal Z}\|_V)$ 分三层）| 完成（第一步）| `docs/02` B.16、`attempts/76`、`tools/verification/stratum_criterion.py` |
| D57 | 专家评审落实：B.13c 基础定理 + 覆盖完备性 + 术语映射 | 完成 | `attempts/75`、`docs/02` B.13c/B.14、`docs/06` |
| D56 | Q3 定型：AVOID = 带约束的 regular subpencil | 完成（定型）| `attempts/74`、`literature/SEARCH_LOG.md` |
| D55 | Lemma A/B 的 Lean 内核（`LemmaA.lean`/`LemmaB.lean`）| 完成（L3 内核）| `tools/lean/MyProof/LemmaA.lean`、`LemmaB.lean`、`attempts/73` |
| D54 | Lemma A：同型副本直和的阶差可加（B.15，阶差无界）| 完成（命题）| `docs/02` B.15、`attempts/72` |
| D53 | 两副本直和：阶差可加（证据）| 完成 | `attempts/71`、`tools/verification/two_copy_gap.py` |
| D52 | 落实 13 号答复：两处收紧 + B.14 可解类 (T*) | 完成 | `docs/02` B.14、`attempts/70`、`tools/verification/t_star_coverage.py` |
| D51 | 构件 3：底座上不可行 ⟸ 一组二次方程（充分不必要）| 完成 | `attempts/69`、`tools/verification/base_quadrics.py` |
| D50 | gadget 底座约束 $V\cap K=0\iff2p+r\ge n$；最小非退化是 $n=6,p=r=2$ | 完成 | `docs/02` B.13e、`attempts/68` |
| D49 | 标量情形退化：B.13f 判据恒成立，gadget 需 $\dim\ge2$ | 完成（否定）| `attempts/67`、`tools/verification/gadget_degree.py` |
| D48 | 标量 gadget 构件：不可行 $\iff$ 一个二次方程（B.13f）| 完成（构件 1/2）| `docs/02` B.13f、`attempts/66`、`tools/verification/scalar_gadget.py` |
| D47 | 单-$\lambda$ 覆盖证书（B.13e）| 完成 | `docs/02` B.13e、`attempts/65` |
| D46 | gadget 探针：整族不可行是薄集；ε=0 不蕴含之 | 完成 | `attempts/64`、`tools/verification/gadget_probe.py` |
| D45 | 第二个整族 Type III（阶差 2）+ 跌落 locus 为空 | 完成（已证）| `proof/type3_second_example/`、`attempts/63`、`tools/verification/drop_locus_new_instance.py` |
| D44 | $\varepsilon=0$ 三情形刻画 + 结构化搜索（未找到第二例）| 完成 | `docs/02` B.13d、`attempts/62`、`tools/verification/epsilon_zero_characterization.py` |
| D43 | II.4 审计 + B.13c（精确刻画）+ G.2 规模记账 | 完成 | `docs/02` B.13c、G.2；`attempts/61`；`tools/verification/encoding_size_accounting.py`、`drop_certificate.py` |
| D42 | 专家第十一轮答复的七项更正（G.2 递推、B.13 降级、B.11d、文献新颖性）| 完成 | `docs/02` G.2/B.11d/B.12、`literature/notes/OBSERVABILITY_REDUCTION_VS_LITERATURE.md` |
| D41 | B.13 incidence variety 维数 + 覆盖判据；更正 "Type III 只在 $r_1=p+r$" | 完成（含更正）| `docs/02` B.13、`docs/08` §4.11 |
| D40 | G.2 紧凑可观性编码（$s$ 分层 + 零化子 + 观测性左逆）| 完成（2 见证 × 16 约束）| `docs/02` G.2、`tools/verification/compact_obs_encoding.py` |
| D39 | 核验可观性归约（B.12）：固定候选谱检验 = q 维可观性秩计算 | 完成（44/44）| `docs/02` B.12、`tools/verification/observability_test.py` |
| D38 | 隐式路线：结构化编码多项式规模（G.1 早已如此）；指数只属非结构化变体 | 完成（含更正）| `attempts/58`、`proof/dec_q_existsR`、`tools/verification/compact_encoding_check.py` |
| D33 | 专家第三封的四条更正 + 行动清单 | 完成（更正）| `attempts/53` |
| D32 | B：编码规模指数增长 | 完成（测量）| `attempts/52`、`tools/verification/scale_measure2.py` |
| D31 | A 收尾：工具覆盖表（可用/部分/不可用）| 完成（收尾）| `attempts/51` |
| D30 | `decide_full`：分层+(*) 完整判定（未打通，工程缺陷）| 失败（记录）| `attempts/50`、`tools/verification/decide_full.py` |
| D29 | 秩分层实现（单参数图卡的可行方向）| 完成（单参数）| `attempts/49`、`tools/verification/rank_stratified.py` |
| D28 | 快速充分判据的边界：秩跌落是真正瓶颈 | 完成（诊断）| `attempts/48`、`tools/verification/fast_feasible.py` |
| D27 | $X$ vs $X_{\rm sp}$：两类实例（"薄"不普遍）| 完成（结构 + 更正）| `attempts/47`、`tools/verification/x_vs_xsp.py` |
| D26 | P1 回归：$(*)$ 判据实测（仅不可行方向可用）| 完成（回归）| `attempts/46`、`tools/verification/regress_bezout.py` |
| D25 | Bézout 秩等式判据（专家 $(*)$，C4 第三证）| 完成（有适用条件）| `attempts/45`、`tools/verification/bezout_rank_test.py` |
| D24 | 掉落轨迹的实现与边界（候选集不完备）| 部分（默认 UNKNOWN）| `attempts/44`、`tools/verification/drop_locus.py` |
| D23 | 更正：`deg≥1` ≠ 处处失败；可行点在 gcd 掉落轨迹 | 完成（更正 + 结构发现）| `attempts/43` |
| D22 | 符号闭环逐阶判定（见证/gcd 证书）| 完成（参数 ≤3）| `attempts/42`、`tools/verification/decide_symbolic.py` |
| D21 | 逐图卡符号 gcd 分析（§8.1 谱层）| 完成（不依赖网格；C4 的第二种证明）| `attempts/41`、`tools/verification/chart_gcd_analysis.py` |
| D20 | sympy 精确消元（§8.1）| 完成（工具 + 首个空集证书）| `attempts/40`、`tools/verification/exact_elimination.py` |
| D19 | 消元器（Buchberger）+ 单参数完整判定 | 部分（Buchberger 规模不可行；单参数方法**4/4 与网格一致**；曾误报的"退化 bug"是我新代码的转置错）| `attempts/39`、`tools/verification/{elimination,complete_small}.py` |

## E. 检验基础设施（勿重复造）

| 工具 | 用途 |
|---|---|
| `tools/verification/toeplitz_criterion.py` | $(5b)$ 的 Toeplitz 判据 |
| `tools/verification/spectral_gcd.py` | 极大子式 gcd（精确多项式）|
| `tools/verification/verify_Q1_nullspace.py` | 零空间铅笔判据（含精确 gcd 版）|
| `tools/verification/consistency_checks.py` | 七条一致性检查（**新增脚本必须调用**）|
| `tools/verification/qmin_exact.py` | 逐阶穷举判定（图卡 + 整数先筛）|
| `tools/verification/regression_Lstar.py` | 专家给的 $q=3$ 见证的回归测试 |
| `tools/verification/dim_Y.py` | 坏点像闭包维数 |
| `tools/verification/z_generator.py` / `omega_construct.py` | $Z$-参数化候选生成 |
| `tools/hygiene/claim_index.py` | 命题检索（`--grep`）|

## F. 结论：不要重复的事

1. 不要再用**抽样**判"不存在"（薄集；已两次踩）；
2. 不要用**有限个 $\lambda$** 代替 $\forall\lambda$（必须 gcd/恒等式）；
3. 不要把**坐标层**（解集收紧）当硬度来源（不传递）；
4. 不要重提 B 组任何被推翻的公式；
5. 不要重走 C1-1…C1-7（除非有新想法）；
6. 不要重新实现 E 组工具；
7. 引用 $(5a)$ 的结论前先看 `08_results.md` §3/§5 的"不作声称"；
8. **"网格 0 命中"不等于无解**：无解必须带证书（整数/遮蔽/单点），否则只能标 `UNKNOWN`
   （见 `tools/verification/decide_with_certificate.py`；专家 §8.1 两次强调）。
