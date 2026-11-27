# feasibility_geometry · 现状

> 上级：[q1_false](../STATUS.md)。**当前活跃**（2026-11-27 起）：attempts 204 个文件（编号至 661）；早期 001–098 为历史。

- 增广族参数化、$\Omega$-抽样、闭包与 $q_0$ 扫描、$Z$-生成。
- 已撤回：闭包不是精确最小维数；$q_{\min}\in\{\mathrm{cl},\mathrm{cl}+1\}$ 被反例推翻。
- 保留：参数化与抽样脚本，作为压缩链/子空间语言的前身。
- [548](attempts/548_projective_feasibility.md)：从 q1_true 转来——射影化可行集的结构判定
  （固定 $\operatorname{rank}R=r$，问可行性是否可由秩与谱条件多项式判定）。下一步：$q=3,k=2,m=1$ 的秩层枚举。
- [549](attempts/549_min_rank_layer_example.md)：最小秩层例子（$q=3,k=2,n=4$，$L_0=[e_1;e_2]$）——
  $(5a)$ 自动成立、$(5b)\iff r_3\ne0$，可行集是锥减超平面；Lean 核验 `no_common_root`。
- [550](attempts/550_m2_degenerate.md)：$m=2$ 同族数据下 $\gcd\equiv1$，可行集是全空间（退化）；
  需要换 $L_0/A$ 构造非退化例子再判断结构定理。
- [551](attempts/551_enumeration_always_infeasible.md)：$n=4,k=2,m=1$、$L_0=[e_1;e_2]$ 的 25 组枚举——
  gcd 恒非常数（只依赖 $A$ 的列）⇒ 该族恒不可行。小 $k$ 族多为退化。下一步 $k=3$。
- [552](attempts/552_n5k3_always_infeasible.md)：$n=5,k=3,m=1$、$L_0=I_3$ 的 64 组枚举——
  gcd 恒为 3 次且不依赖 $r$ ⇒ 恒不可行。下一步 $m=2$ 或 $L_0$ 秩亏。
- [553](attempts/553_rank_defect_counting.md)：满秩 $H_0$ 的一般障碍——固定行 pencil 的根需要自由行补偿；
  一般 $m\ge k$ 才可能，解释 551/552（$m=1$）恒不可行。下一步 $k=2,m=2$。
- [554](attempts/554_feasibility_independent_of_R.md)：$k=2,m=2$ 的 25 组枚举——6 组全可行、19 组全不可行，
  **0 组随 $R$ 变化**；猜想：可行性只依赖数据（不依赖自由行选择）。下一步 $k=3,m=2$ 检验。
- [555](attempts/555_generic_gcd_criterion.md)：gcd 次数上半连续 ⇒ 一般点取最小值；
  判定 $\exists R[(5a)\wedge(5b)]\iff (5a)$ 的簇不在 gcd 跳变簇里。修正 554 的“可行性不依赖 R”。
- [556](attempts/556_criterion_scope.md)：判据作用域澄清——555 是“固定数据、对 $R$ 取一般点”；
  530 是“无 $R$ 的数据判定器”。下一步：非平凡 $(5a)$ 实例上实现判定骨架。
- [557](attempts/557_nontrivial_infeasible_example.md)：非平凡 $(5a)$ 例子（$\ker H=\operatorname{span}\{e_3\}$）
  可行集为空（$\det P=\lambda(\lambda-1)^2r_3$，Lean 核验）；与 555 判据一致。
- [558](attempts/558_feasible_nontrivial_difficulty.md)：可行且 $(5a)$ 非平凡的难点——需 $\omega<q$ 且 $Z$ 在 $W$ 上无特征向量；
  下一步把 520 的构造参数化（第三行 $=rN$）。
- [559](attempts/559_param_gate_feasible.md)：**第一个可行且 $(5a)$ 非平凡的例子**——$w=0\wedge v\ne0\wedge u\ne v$；
  Lean 核验 `no_common_root`；与 555 判据一致。
- [560](attempts/560_param_family.md)：参数族 $H_A=\operatorname{diag}(a,b)$ 的完整可行条件——
  始终是“$w=0$ + 若干非零条件”；559 是 $a=1,b=2$ 的特例。559 的 $H_A$ 笔误已更正。
- [561](attempts/561_lean_param_family.md)：参数族核心矛盾的 **Lean 核验**（`no_common_root`，退出码 0）。
- [562](attempts/562_second_param_family.md)：第二参数族（$AN=I$）——可行 $\iff w=0\wedge a,b\ne1\wedge u,v\ne0$，
  与 560 同为“超平面 $w=0$ 上的开集”。一般结构（等式+开条件）为猜想。
- [563](attempts/563_lean_second_family.md)：第二参数族核心矛盾的 **Lean 核验**（`Q1Gadget563.no_common_root`，退出码 0）。
- [564](attempts/564_decomposition_families.md)：两族的完整分解——$(5a)=$ 全空间；跳变簇 = $\{w\ne0\}\cup$ 秩层上的超平面；
  可行集 = $\{w=0,au\ne v,v\ne0\}$（秩层上的开集）。下一步一般分解。
- [565](attempts/565_constructible_feasible_set.md)：一般结构——可行集是构造集（局部闭集之并），
  在 $\mathbb C$ 上可判定；复杂度未定。560/562/557 都是特例。
- [566](attempts/566_irreducible_branches_557.md)：557 的 $(5a)$ 分支分解——$\{r_3\ne0\}$（开）+ $\{r_1=r_3=0\}$（线性）；
  两分支都被跳变簇覆盖（可行集空）。分支可线性参数化，符合 ChatGPT 的判据。
- [567](attempts/567_nontrivial_branch_obstacle.md)：$H=[e_1;e_2;r]$ 下 $(5a)$ 非平凡（$r_3=0$）迫使第三列为零，
  于是 $\lambda=b$ 处 $(5b)$ 必失败；需换 $L_0$ 秩亏的形状。
- [568](attempts/568_q3k3m1_no_nontrivial_feasible.md)：$q=3,k=3,m=1$ 层——$(5a)$ 非平凡 ⇒ $(5b)$ 失败（两种 $H_0$ 秩都排除）。
  下一层：$q=4,k=3,m=2$。
- [569](attempts/569_q4k3m2_scan.md)：$q=4,k=3,m=2$ 随机扫描——224/300 可行，但 15 个非平凡核例子全部不可行；
  下一步从 530 出发加“落在 $\operatorname{row}H_0$ 内”的自由行做定向构造。
- [570](attempts/570_trivial_extension.md)：530 加 $r\in\ker N$ 得“非平凡且可行”的 q=4 实例，但为平凡扩张
  （额外行在 $H,H_A$ 中为零）；真正的问题是“有效自由行”（$rN\ne0$ 且不破坏 $(5b)$）。
- [571](attempts/571_only_duplicate_rows_feasible.md)：530 加自由行的 27 组枚举——仅 3 组可行，全部是重复行
  （$rN=(0,0,\pm1)$ 或 $0$）；猜想：可行自由行只能是已有行的重复（谱不可见）。
- [572](attempts/572_redundant_row_lemma_draft.md)：冗余行引理草稿——新行落在 $P_0(\lambda)$ 行空间 ⇒ 它是已有行组合；
  常数系数情形已证，$\lambda$-依赖系数未闭合。
- [573](attempts/573_rank_exactness_check.md)：秩精确性复查——(5b) 需 rank P=ω 恰好，须补 $(\omega+1)$ 子式为零；
  重跑 530 枚举：27/243 可行、全冗余（支持 572）。569 的判据描述需补此检查（结论未变）。
- [574](attempts/574_redundant_row_theorem.md)：冗余行定理（非退化：$H_0,H_{A,0}$ 行满秩）已证；
  530 的退化情形（$h_1=xh_2$、$a_3=0$）由 573 的精确点支持但未证。
- [575](attempts/575_530_degenerate_complete.md)：530 退化情形的完整证明——扩展行必冗余
  （$rN=\beta h_2+\gamma h_3$、$rAN\in\operatorname{span}\{a_2\}$）。冗余行定理完整，530 不可扩展。
- [576](attempts/576_lean_coeff_compare.md)：575 系数比较的 **Lean 核验**（`coeff_compare`，退出码 0）；
  575 的 $p_1$ 表示式已更正。
- [577](attempts/577_new_start_eliminated.md)：ChatGPT 的新起点（$H_0=[e_1;e_2]$、$H_{A0}=[e_3;e_4]$、自由行 $r,s$）
  被 $(5a)$ 直接淘汰——$\ker H$ 总含 $(x_3,x_4)\ne0$，而 $H_{A0}$ 要求其为零。
- [578](attempts/578_alignment_condition.md)：对齐条件——$H_{A0}$ 每行的 $(x_3,x_4)$ 部分必须与 $r$ 平行，
  故 $(5a)$ 把自由行限制在超平面上（仍为锥，与 545 一致）。下一步具体例子的 $(5b)$。
- [579](attempts/579_alignment_example_fails.md)：对齐例子（$a=(0,0,1,0)$、$b=0$）在 $\lambda=0$ 掉秩失败；
  需 $H_{A0}$ 两行都非零独立、再加 $s$ 补到 3 维。
- [580](attempts/580_effective_free_row.md)：$k=4,q=3$ 的有效自由行例子——可行 $\iff r_3=r_4=0\wedge r_1(\alpha-1)\ne0\wedge r_2(\beta-2)\ne0$；
  Lean 核验 `no_common_root`。与 575 的“追加行”问题不同，这是从头设计的 gadget。
- [581](attempts/581_mixed_row_degree.md)：混合行的次数分析——2×2 子式的 λ 系数只能线性；
  二次项 $r_1r_2-z$ 只能出现在 3×3 子式的 $\lambda^2$ 系数里。下一步 3×3 构造。
- [582](attempts/582_3x3_construction_conflict.md)：3×3 构造中 $r_1r_2$ 与 $-z$ 两项的冲突分析；
  下一步用小范围 sympy 枚举找 $C_2=r_1r_2-z$ 的组合。
- [583](attempts/583_single_term_obstacle.md)：单项 $h_i$ 的因子障碍——$-z$ 项总带 $r_1$ 或 $r_2$ 因子，
  故 $C_2=r_1r_2-z$ 需要多项 $h_i$；下一步双项枚举。
- [584](attempts/584_det_route_linear_condition.md)：3×3 行列式路线——$\lambda^2$ 系数 $=-(r_1r_2-z)$，
  但 $\lambda$ 系数 $r_1+r_2$ 必须为零才能让 $\det P$ 无根；可行集只编码 $z=-r_1^2$，不是一般乘法。
- [585](attempts/585_homogeneous_det_obstacle.md)：$H_A=I$ 的 3×3 路线——$S_2$ 二次齐次、$\mathrm{tr}H$ 一次齐次，
  不可能同时正比于非齐次的 $r_1r_2-z$；需 $a_i$ 带常数或非方阵。
- [586](attempts/586_q3omega3_nogo.md)：$q=\omega=3$ 不可行（$\det H\ne0$ ⇒ $\det P$ 非常数 ⇒ 有根）；
  即 518 的特例。$q=3$ 的可行实例必须 $\omega\le2$。
- [587](attempts/587_584_criterion_error.md)：**584 判据错误**——$\omega=2$ 时 $\det P$ 必须恒为零，
  584 的构造需 $1=0$ ⇒ 恒不可行；584/585 的 det 分析只适用于 $\omega=3$（已被 586 排除）。
- [588](attempts/588_corrected_3x3_route.md)：修正后 3×3 路线的试算失败——实际 $\det P=-r_1\lambda(\lambda-1)\ne0$
  （手算漏交叉项，sympy 复核）；下一步用 sympy 搜索 $\det P\equiv0$ 的组合。
- [589](attempts/589_q3_classification.md)：$q=3$ 分类（**已被 590 推翻**）。
- [590](attempts/590_counterexample_q3omega2.md)：**反例**——$H=\operatorname{diag}(1,1,0)$、$H_A=ZH$（$Z$ 三阶循环置换），
  $\det P\equiv0$、$\gcd=1$、$\operatorname{rank}P=2$：$q=3,\omega=2$ **可行**；589 的分类被推翻。
- [591](attempts/591_product_inequality_gadget.md)：**乘积不等式 gadget**——$q=3,k=3$，$H=[[0,0,0],[r_1,1,0],[z,r_2,0]]$、
  $Z$ 幂零 Jordan、$H_A=ZH$；**可行 $\iff r_1r_2\ne z$**（第一个编码自由变量乘法的 gadget，形式为不等式）；
  Lean 核验 `det_P_zero`、`minor_zero`。
- [592](attempts/592_composition_closure.md)：$\ne$ 门的组合闭包——可表示“有限个二次型 $\ell_1\ell_2-\ell_3\ell_4\ne0$”的合取；
  仍是开集，不能表示等式；一般高次需中间变量（又回到等式门）。
- [593](attempts/593_product_equality_gadget.md)：**乘积等式 gadget**——$H=[[r_1,z,0],[1,r_2,0],[0,0,1]]$、$H_A=ZH$（$Z$ 循环），
  **可行 $\iff r_1r_2=z\wedge r_1^3\ne1$**；Lean `det_H`、sympy 三点验证。这是第一个等式乘法门。
- [594](attempts/594_product_equality_clean.md)：**干净的乘积等式 gadget**——593 的循环 $Z$ 换成幂零 Jordan，
  附加条件 $r_1^3\ne1$ 消失：**可行 $\iff r_1r_2=z$**；Lean `det_H`、`det_lambdaI_sub_Z`；sympy 三点验证。
- [596](attempts/596_realizability_correction.md)：**重要更正**——$H_A=ZH$ 在 q1 中不可实现（$H_A=LAN$）；
  正确形式是右铅笔 $P=H(λI-Z')$，此时 $H$ 可逆 ⇒ $(5b)$ 自动成立，594 的门极性反转、不成立。
  594/595 已标注“不可实现于 q1”；右铅笔重做为下一步。
- [597](attempts/597_right_pencil_no_gate.md)：右铅笔重做（一）——零行 $H$ + 幂零 $Z'$，两侧 $(5b)$ 都自动成立，**无门**；
  需 $Z'$ 带非零特征值才能产生掉秩条件。
- [598](attempts/598_right_pencil_product_gate.md)：**右铅笔乘积等式门**——$H=[[r_1,z,0],[1,r_2,0],[0,0,0]]$、
  $Z'=\operatorname{diag}(0,1,0)$、$H_A=HZ'$，**可行 $\iff r_1r_2=z$**（q1 可实现：$n=5,C=e_5^T,A$ 在前 3 坐标取 $Z'$、$Ae_4=e_5$）；
  Lean `det2_P`、sympy 四点验证。
- [599](attempts/599_right_pencil_conjunction_linear_gate.md)：右铅笔合取（链验证通过）+ **线性门的两种尝试失败**；
  猜想：右铅笔下线性等式门不可能（$H$ 可逆 ⇒ $(5b)$ 自动）。
- [600](attempts/600_diagonal_linear_gate_impossible.md)：对角 $H$ 的线性门不可能（$H$ 可逆 ⇒ 自动；$Z'$ 特征向量与 $W$ 的关系与 $\ell$ 无关）；
  一般情形为猜想。
- [601](attempts/601_linear_gate_exists.md)：**线性门存在**（非对角）——=[[1,0,0],[0,0,r_1],[0,0,0]]$、'=J$，可行 $\iff r_1=0$；
  推翻 600 的一般猜想（对角情形仍不可能）。乘积门+线性门+合取 ⇒ $+,\times$ 可编码。
- [617](attempts/617_evidence_polynomial.md)：**结构性证据汇总**（M2 判断）——q1 更可能有多项式算法；
  多门组合路线停止，q1_true 仅剩“全局多项式编码”值得一试。
- [618](attempts/618_rank_stratum_algorithm.md)：q1_false 的**秩层算法骨架**（M2 计划）：一般点用符号秩+子式 gcd，
  退化层待定；下一步在小实例上实现第一步并与 549/557/598/613 对照。
- [619](attempts/619_stratum_check_598.md)：598 检验 618——一般层（$\omega=2$）不可行，可行点在 $\omega=1$ 退化层；
  只做第一层会误判，须逐层判定。
- [620](attempts/620_stratum_checker.md)：**秩层判定器**（脚本）——对 598/613 打印每层子式数与 gcd；
  $\omega=2$（598）/$\omega=3$（613）一般层不可行，可行层由子式恒零给出 $r_1r_2=z$。局限：未做层内特化。
- [621](attempts/621_stratum_specialization.md)：层内特化——598 门上判可行；613 的附加条件定位到 $r_2$ 的三次单位根特化；
  完整判定需**递归分层**。
- [623](attempts/623_chatgpt_assessment_p_route.md)：**ChatGPT 评估**（新对话）——现有迹象对 q1 ∈ P 有中等结构支持；
  最该做的是“多项式规模规范分层”（秩势函数 $Φ$、状态合并）；三步任务见文。
- [624](attempts/624_rank_potential.md)：秩势 $\Phi$——598/613 的参数族各只有 **3 个状态**；
  特化链严格下降；猜想：可达状态数多项式。下一步对 557/616 枚举并尝试证明状态界。
- [625](attempts/625_rank_potential_more.md)：$\Phi$ 枚举（续）——557 有 2 状态（全不可行）、616 有 3 状态（全可行）；
  四族状态数 2–3，远小于参数组数；强化猜想：状态数多项式。
- [626](attempts/626_state_count_refuted.md)：**状态数猜想被推翻**——两块 598 有 6 个状态（随块数指数增长）；
  但判定只需按 $\omega$（$\le\min(q,k)+1$ 种）检查“所有谱点秩=ω”，难点仍是层内存在性。
- [629](attempts/629_invariant_K0_trivial.md)：**定理**——$A K_0\subseteq K_0$ 时可行 $\iff L_0N=0$（$q_{\min}=r_0$）；
  右铅笔 gadget 的“门”全部不成立（557/598/601 精确验证）；q1_true 只剩 $W\ne0$ 情形。
- [630](attempts/630_W_nonzero_decomposition.md)：$W\ne0$ 的结构分解——$H=H_0+H_{\rm free}$、$G=G_0+G_{\rm free}$，
  自由行对 $H$ 与 $G$ 独立可控，但 $G$ 的行只在 $\operatorname{row}(W)$ 内；分情形可行性开放。
- [631](attempts/631_W_full_row_rank_feasible.md)：**定理**——$W$ 满行秩且有自由行（$q-1\le k$）时 q1 可行；
  证明用 $H$ 取 $q-1$ 秩、$Z$ 的特征向量避开 $\operatorname{im}H$、$G$ 由 $W$ 的右逆实现。
  与 629 合并：hardness 入口只剩 $\operatorname{row}(W)$ 真子空间。
- [632](attempts/632_rank_bound_by_W.md)：**猜想**——可行 $\Rightarrow\operatorname{rank}H\le\dim\operatorname{row}(W)$；
  左特征向量特例已证（$\lambda=\lambda_0$ 时 $P=-G$，秩 $\le s$）；一般情形待证。
- [633](attempts/633_response_to_chatgpt_omega0.md)：回应 ChatGPT——$\omega=0$ 的强结论被 631 推翻
  （$Z$ 是 $q\times q$，限制映射不是方阵特征值问题）；$\omega>s$ 的数值例子不可行，支持 $\omega\le s$。
- [634](attempts/634_exhaustive_omega_s.md)：穷举 $k=q=3$、$Z'$ 循环、$s=1$、$\omega=2$ 的 7536 个 $H$——
  **0 个可行**，支持 $\omega\le s$；早先 3 个“反例”因漏掉复特征根被 gcd 排除。
- [635](attempts/635_proof_attempt_omega_s.md)：$\omega\le s$ 的证明尝试——单式行列式论证不适用（限制映射非方阵）；
  真正的障碍是 $ZV\subseteq V+\operatorname{im}G$（$\dim\le\omega+s$）与特征向量存在性的连接，未闭合。
- [636](attempts/636_counterexample_failed.md)：反例尝试失败——$G=0$ 时回到 629（$\omega=0$），
  $\lambda=0$ 处掉秩；$(5b)$ 用的是 $Z'$（数据）不是自由 $Z$；$\omega\le s$ 猜想仍成立。
- [637](attempts/637_exhaustive_multi_Z.md)：三种 $Z'$（循环、$\operatorname{diag}(0,1,2)$、幂零 Jordan）穷举，
  $\omega=2>s=1$ 均 **0/7536** 可行；支持 $\omega\le s$。
- [638](attempts/638_counterexample_omega_gt_s.md)：**反例**——$\omega=2>s=1$ 的可行 q1 实例（=6$、=e_5^T+e_6^T$、 e_1=e_2,e_2=e_4,e_4=e_5,e_5=e_6$），
  推翻 632 的 $\omega\le s$ 猜想；634/637 的穷举覆盖不足（=e_1$、三种 '$）。
- [639](attempts/639_K_infinity_theorem.md)：**定理**——$\omega\le k-\dim K_\infty$（$K_\infty$ 为 $Z'$ 在 $S^\perp$ 内的最大不变子空间）；
  $H|_{K_\infty}=0$；统一 629（界 0）、631（界 k）、638（界 2 达到）与 634/637 穷举。充分性为猜想。
- [640](attempts/640_converse_false.md)：反向不成立（逐 $H$）——$S=\mathbb C^3$、$H=I$、$Z=\operatorname{diag}(1,2,3)$ 满足 $K_\infty$ 上界
  但 $(5b)$ 失败；$K_\infty$ 必要不充分，存在性判定仍开放。
- [641](attempts/641_two_extensions.md)：实验——同一 $K_\infty$、同一 $H_0$、同一 $G$ 的两个扩展：
  A 可行（gcd=1），B 不可行（gcd=$\lambda(\lambda-1)$）；$K_\infty$ 必要不充分（逐 $H$），实例层面 A 存在即可行。
- [642](attempts/642_bezout_system.md)：**Bézout 线性系统**——把 $(5b)$ 的 gcd=1 转成有限线性条件；
  A（可行）系统可解、B（不可行）不可解；固定 $H,Z$ 时是多项式大小线性判定，扩展存在性仍开放。
- [643](attempts/643_parametric_bezout.md)：参数化 Bézout 矩阵——$(5b)\iff\operatorname{rank}M(\theta)=\operatorname{rank}[M|b]$；
  给出有限行列式条件（A/B/638 验证）；复杂度开放。
- [644](attempts/644_reachability_conjecture.md)：猜想——可行 $\iff\operatorname{rank}H_0\le k-\dim K_\infty$；
  638 的典范 $H$（核 $=K_\infty$）验证上界可达；$\omega^*=1$ 的定向构造未完成。
- [645](attempts/645_Kinfinity_corrected.md)：更正 $K_\infty$ 计算（$S=e_1$、$Z'=C_3$ 时为 $\operatorname{span}\{e_2\}$，$\omega^*=2$）；
  秩 1 不可能（$G$ 行约束）；秩 2 穷举 0/7536 ⇒ 该实例很可能不可行，“$\operatorname{rank}H_0\le\omega^*$ ⇒ 可行”猜想受挑战。
- [646](attempts/646_random_search_e1.md)：随机搜索（$H\in\{-3..3\}$，301 个秩 2）——$S=e_1$、$Z'=C_3$ 仍 **0 可行**；
  支持该实例不可行（$H_0=0$），将反驳 $\operatorname{rank}H_0\le\omega^*$ 猜想；一般证明待做。
- [648](attempts/648_e1_instance_infeasible_proof.md)：**严格证明**——$S=e_1$、$Z'=C_3$ 时秩 1、秩 2 都不可能；但 $r_0=0$ 时 $L=0$ 给出 $\omega=0$ 可行，故实例**可行**（645/646 的“不可行”仅指秩 $\ge1$）；派生：$r_0=0$ 的实例恒可行，hardness 需 $r_0\ge1$。
- [649](attempts/649_necessary_conditions_H0.md)：**推论**——可行 $\Rightarrow H_0|_{K_\infty}=0$、$\operatorname{rank}H_0\le d=k-\dim K_\infty$；
  统一 629/557/598/601/638；充分性为 M2 猜想。
- [650](attempts/650_sufficiency_counterexample.md)：**反例**——648 数据上取 $H_0=e_1^{\mathsf T}$（满足 649 条件）但实例不可行；
  649 的充分性被推翻；机制：$G$ 在 $S^\perp$ 列上零化 + $Z'$ 循环作用逼 $He_2=He_1=0$。
- [651](attempts/651_Tinfinity_theorem.md)：**定理**——$T_\infty$（$K_\infty$ 沿 $S^\perp$ 内 $Z'$ 前向传播的闭包）满足 $H|_{T_\infty}=0$，
  $\omega\le k-\dim T_\infty$；统一 629/631/638/648/650；充分性为猜想。
- [652](attempts/652_lifting_lemma.md)：**提升引理**（已证）——$H_0|_T=0$、$\operatorname{rank}H_0\le d$、$q\ge d$
  ⇒ 存在含 $H_0$、秩 $d$、在 $T$ 上为零的扩展；充分性归约为“$Z$ 构造引理”（开放）。
- [653](attempts/653_Z_construction_reduced.md)：$Z$ 构造引理拆成两条——逐行可解性 $UZ'\subseteq U+S$（已证等价）、
  特征向量避让（开条件，开放）；猜想 $T_\infty$ 保证第一条自动。
- [654](attempts/654_Tinfinity_not_automatic.md)：另一个 $r_0=1$ 的不可行实例（幂零 $Z'$，$T_\infty=\mathbb C^3$，$d=0$）；
  $H_0=e_1^{\mathsf T}\ne0$ 与 $H=0$ 矛盾；与 650 一起说明可行性数据依赖。
- [655](attempts/655_grassmann_formulation.md)：**约束 Grassmann 集** $\mathcal G$（$U_0\subseteq U\subseteq T^\perp$、$UZ'\subseteq U+S$）
  与秩条件写法；条件化充分性为 M2 猜想；若成立 q1 判定化为 $\mathcal G\ne\varnothing$ + $Z$ 构造。
- [656](attempts/656_extremes_and_gap.md)：极端情形（$s=k$ 由 631、$s=0$ 由 629）成立；中间情形 $0<s<k$ 为缺口；
  $T_\infty=0$ 的维数观察；$k=2$ 小例子待验证。
- [657](attempts/657_middle_case_positive.md)：**中间情形的第一个正面例子**（$k=2$、$Z'=[[0,0],[1,0]]$、$S=e_1$、$T_\infty=\operatorname{span}\{e_2\}$、$d=1$）：
  $H=u e_1^{\mathsf T}$（$u=(1,0,1)$）、$Z=e_3e_1^{\mathsf T}$ 的秩1解，sympy 验证秩1 ∀λ。
- [658](attempts/658_rank1_template.md)：**秩一模板**——$H=uv^{\mathsf T}$，$v\in S\cap\ker(Z'^{\mathsf T})$，
  $HZ'=0$、$G=(Zu)v^{\mathsf T}$ 行在 $S$；避让 $\iff\lambda u-Zu\ne0\ \forall\lambda$；657 是特例。
- [659](attempts/659_chatgpt_rank_d_template.md)：ChatGPT 深入回答的整理——定理1（秩 $d$ 模板：$H=UV$、$VZ'=0$、
  $\operatorname{rank}[U\ B]=2d$ ⇒ 可行）、定理2（行约束充要条件）、定理3（$S\cap\ker Z'^T\subseteq T_\infty^\perp$）、
  反例4（$k=1,q=1$：651 条件不充分）、秩 $=q$ 障碍；开放：仿射铅笔问题。
- [660](attempts/660_affine_degenerate_example.md)：仿射铅笔的退化例子（$V=I$、$d=2$、$S=e_1$）——定理 2 把 $B$ 的第二列钉为零，
  $\gcd=\lambda$ 必败；说明 $\mathcal B\ne\varnothing$ 不等于可行；实例级判据仍开放。
- [661](attempts/661_corrected_counterexample5.md)：**修正 ChatGPT 反例5**——$H_0=e_1^{\mathsf T}$ 违反 651（$T_\infty=\operatorname{span}\{e_1\}$）；
  改用 $H_0=e_2^{\mathsf T}$ 得真正的实例级不可行（$k=q=2,r_0=1$，自由行 1）：秩1 逼 $Zu=0$、秩2 特征值障碍，
  满足 651 全部条件。
- [662](attempts/662_chatgpt_priority_assessment.md)：ChatGPT 评估——q1 倾向 P 但谨慎；优先级：
  (1) 仿射铅笔 $d=1,2$ 的 gcd 分类（以 661 为测试），(2) 实例级不可行证书，(3) 秩层算法化；
  并警告位复杂度（DEC 调用次数 ≠ 复杂度）。
- [663](attempts/663_d1_classification.md)：**仿射铅笔 $d=1$ 完整分类**——$v|_K\ne0$ 不可行（$Z$ 必以 $u$ 为特征向量）；
$v\in E=S\cap(Z'^{\mathsf T})^{-1}S$ 时可构造，$q\ge2$ 下秩一可行 $\iff E\ne0$；
  统一解释 629/631/638/657/661（661 = $E=0$ + 秩 $=q$ 障碍）。
- [664](attempts/664_d2_framework.md)：ChatGPT 的 $d=2$ 框架与 $\lambda\in\mathbb C$ 澄清——
  $d=2$ 的对象是二维行空间 $D\subseteq S\cap\ker Z'^{\mathsf T}$ + $U$ 仿射空间 + 复 gcd；
  五条引理 A–E 与优先级；下一步实验：$k=2,3,4$ 枚举 $D,U$ 算复 gcd，找必要条件全满足但无 gcd=1 的反例。
- [665](attempts/665_template_theorem.md)：**秩 $d$ 模板的完整判据**（$VZ'=0$）——可行 $\iff$ $\dim E\ge d$、
  $q\ge d+1$、固定行匹配；$q=d$ 由 $\det(\lambda U-B)$ 必根排除；638 说明模板不是必要条件。
- [666](attempts/666_uniform_rank_criterion.md)：**Theorem U（统一恒秩判据）**——$\operatorname{rank}P(\lambda)=d\ \forall\lambda$
  $\iff$ 所有 $(d+1)$ 子式恒零且 $d$ 子式 gcd=1 $\iff$ Bézout 证书 $\iff$ Smith 不变因子全为 1；
  665 由 Cauchy–Binet 推出（模板是特例），661 由 $\gcd=\det P$ 直接判不可行；战略：放弃逐 $d$ 分类，转统一判据 + 设计变量系统。
- [667](attempts/667_uniform_bezout_system.md)：Theorem U 的完整证明 + **统一 Bézout 系统**——
  $(5b)\iff\operatorname{rank}[M(H)\mid e_0]=\operatorname{rank}M(H)$；$M$ 为 $2d\times md$、条目次数 $\le d$；
  统一可行性 = 多项式方程（$(d+1)$-子式零）+ 行列式条件；638/641B/661 验证。
- [668](attempts/668_bezout_rank_check.md)：Bézout 秩判据的数值验证——638（可行）$\operatorname{rank}M=4=[M\mid e_0]$；
  641B（不可行）$2<3$，与 gcd 判据一致。
- [669](attempts/669_U_corollaries_d1_d2.md)：Theorem U 的直接推论——$d=1$ 的干净重推（$(5b)\iff u$ 非 $Z$ 特征向量）、
  $d=2$ 的 $M$ 显式 Sylvester 型结构（$4\times2m$，列成对移位）。
- [670](attempts/670_M_rank_stratification.md)：$M$ 的秩分层——$(5b)\iff\exists r\le2d$：$\operatorname{rank}M=r$ 且
  $\operatorname{rank}[M\mid e_0]=r$；层数 $\le2d+1$（与 $q,k$ 无关），每层是 $M$ 子式的构造集。
- [671](attempts/671_d1_M_reduction.md)：$d=1$ 的 $M$ 显式约化（$M$ 列为 $v_j[-z_i;u_i]$）——精确复现 663 的
  “$u$ 非 $Z$ 特征向量”判据；列出 $d=2$ 的 $r=0..4$ 秩层条件；657 数值核验 $\operatorname{rank}M=2$ 可解。
- [672](attempts/672_full_rank_sufficient.md)：满秩 $M$ 的充分条件——$\operatorname{rank}M=2d\Rightarrow$ 可行；
  $D_d(R)=\sum|2d\text{-子式}|^2\not\equiv0$ 是统一的符号判据；$D_d\equiv0$（如 $m=1$）落入退化层（661 即此）。
- [673](attempts/673_Dd_experiment.md)：$D_d$ 实验——638 满秩可解；300 组随机 $Z$、26 个随机秩 2 $H$
  均未出现“秩 $<4$ 且可解”；猜想（$d=2$、$m\ge2$）$e_0\in\operatorname{col}M\Rightarrow\operatorname{rank}M=4$（仅抽样）。
- [674](attempts/674_d2_theorem.md)：**$d=2$ 定理**——$\operatorname{rank}H=2$ 时 $(5b)\iff\operatorname{rank}M=4$；
  一般 $d$ 猜想：$(5b)\iff\operatorname{rank}M=2d$（$d=1,2$ 已证，$d=3$ 有抽样支持）。
- [675](attempts/675_sylvester_rank_lemma.md)：一般 $d$ 的 **Sylvester 秩引理（猜想）**——$\operatorname{rank}\Phi=2d-\deg\gcd$；
  若成立则 674 的猜想随 $\gcd=1$ 成立；证据：$d=2$ 证明、$d=3$ 铅笔样本、3000 组抽象三元组、5 组非平凡 gcd（秩 $=2d-\deg g$）。
- [676](attempts/676_chatgpt_lemmaS_assessment.md)：ChatGPT 评估引理 S——统一判据的核心；停止逐 $d$ 分类；实设计 Bezout 证书可取实系数；$\operatorname{rank}H<d$ 时须按实际最高次数设证书空间；统一判据不解决 $\exists U$ 与多项式时间。
- [677](attempts/677_lemmaS_proof.md)：**引理 S 的证明**——$U=I\cap\mathbb C[\lambda]_{<2d}$，故 $\operatorname{rank}\Phi=2d-\deg\gcd$；
  由此 **674 的一般 $d$ 猜想成立**：$\operatorname{rank}H=d$ 时 $(5b)\iff\operatorname{rank}M=2d\iff D_d\ne0$（开条件）。
- [678](attempts/678_existsH_criterion.md)：**$\exists H$ 判据**——$H_A=HZ'+G$、$G\in S^q$ 自由；可行 $\iff$
  $\exists H$（秩 $d'$、前 $r_0$ 行 $=H_0$）使 $D_{d'}(H,\cdot)$ 在 $S^q$ 上不恒为零；无自由行时退化为单点 $\operatorname{rank}M=2d'$。
- [679](attempts/679_q_eq_r0_poly.md)：**$q=r_0$ 时可行 $\iff$ 固定铅笔最大子式 $\gcd=1$（多项式时间）**；
  因此 q1 的困难只在“选择自由行”（$\exists R$），不在给定 $L$ 的判定。
- [680](attempts/680_free_row_random.md)：638 数据带自由行的随机搜索——找到可行点（秩 $M=4$），验证 678 判据；
  随机搜索可作可行性 Monte Carlo，但不是多项式判定。
- [681](attempts/681_chart_reduction.md)：**图表归约**——可行 $\iff$ 有限个图表上的 PIT（多项式非零）；
  开放：图表数 $\binom{k}{d'}$ 与去随机化；若“可行 ⇒ 存在 Zariski 开图表集”成立，则 q1 可行性 $\in$ RP。
- [682](attempts/682_fixed_d_RP.md)：**固定 $d'$ 的可行性 $\in$ RP**——可行 $\Rightarrow$ $\tilde D$ 的零点集真闭，
  参数空间中 $\{\tilde D\ne0\}$ 是 Zariski 开稠密；随机采样即得单边证书；复杂度关于 $d'$ 指数。
- [683](attempts/683_feasibility_sampler.md)：682 算法的实现与测试——638/657 找到证书（⇒ 可行），661 在 300 次内未找到
  （与不可行一致，但非证明）。
- [684](attempts/684_D_zero_sources.md)：**$D\equiv0$ 的两个结构性来源**——$m=1$（$q=k=d'$，518）与 $S=0,d'=k$（公共因子 $\det(\lambda I-Z')$，629）；
  猜想其余情形 $D\not\equiv0$（一般可行）；抽样：$S\ne0$ 98/108 满秩，$S=0$ 0/76。
- [685](attempts/685_correction_5a_G.md)：**更正**——$G\in S^q$ 不自由；$(5a)$ 要求 $H_iZ'+G_i\in\operatorname{row}(H)$（$G_i\in S\cap(U-H_iZ')$）。
  678 的判据须加此仿射约束；682 的 RP 降级为条件性；661 只是 $q=2$ 不可行（$q=3$ 可行，$q_{\min}=3$）；638/657 证书仍有效。
- [624](attempts/624_randomized_algorithms_direction.md)：**新研究方向存档**（未做）——q1 的随机算法：
  定位为“可行解空间的泛型结构 + 随机化判定”，三目标定理 A/B/C 与优先级见文；暂不推进。
- [686](attempts/686_Z_parametrization.md)：**修正判据（以 $Z$ 为变量）**——$(5a)$ 自动（$H_A=ZH$），$ZH-HZ'$ 行在 $S$ 为线性条件；
  显式检查 638/657/661（$q=2$ 不可行、$q=3$ 可行）；RP 改为条件性（需在 $\mathcal V$ 上有效采样）。
- [687](attempts/687_Z_free_part.md)：**$Z$ 的自由部分不改变铅笔**——固定 $H$ 时 $Z$ 的解只差左零空间，$ZH$ 唯一；
  可行性化为 $H$ 的条件（相容性 $H_iZ'\in U+S$ + gcd1），无 $Z$ 搜索；$d'=k$ 时相容性自动。
- [688](attempts/688_audit_650_654.md)：**复核 650/654**——结论仍成立；661 改为“$q=r_0+1$ 不可行”（$q_{\min}=3$）；
  给出修正后的证明版图与开放问题（$d'=k,q>k$、$d'<k$ 相容性、$\exists H$ 判定）。
- [689](attempts/689_dk_q_gt_k_construction.md)：**$d'=k,q>k$ 的构造**——$H=[I_k;0]$、$A=Z'+C$（$C$ 行在 $S$）、$B$ 行在 $S$；
  若 $A$ 简单谱且 $B$ 杀死特征向量则可行；数值 $k=3,q=4$ 验证；标量 $Z'$ 需 $k\le2s$。
- [690](attempts/690_eigenvalue_rank_necessary.md)：**特征值-秩必要条件**——可行 $\Rightarrow$ 对每个特征值 $\mu$，
  $\operatorname{rank}(\mu I-Z')\ge d'-s$；解释标量 $Z'$（$d'>s$）不可行；$S=\mathbb C^k$ 自动成立。
- [691](attempts/691_necessary_chain.md)：**必要条件合并**——$T_\infty$、690（特征值-秩）、$m=1$、$S=0$ 预筛选链；
  标量 $Z'$ 完整结论：可行 $\Rightarrow d'\le s$（$d'=k,s<k$ 不可行）。
- [692](attempts/692_correction_T_not_S.md)：**更正**——$G$ 的行空间是 $T=\{lW:lN=0\}\subseteq S$（$\dim T=t$），不是 $S$；
  678/682/690 的表述改为 $T$；测试数据 $t=s$，具体结论不变；638 在 $T$ 下仍可行（已验证）。
- [693](attempts/693_t_lt_s_example.md)：**$t<s$ 实例**——$n=4,k=2$，$S=\operatorname{span}\{e_1,e_2\}$、$T=\operatorname{span}\{e_1\}$、$Z'=0$；
  690 的 $t$-版本给 $d'\le1$；$H_0=e_2^{\mathsf T}$ 不可行（任何 $q$），$H_0=e_1^{\mathsf T}$ 可行。
- [694](attempts/694_chatgpt_direction_obstruction.md)：ChatGPT 对 $T$ 更正与方向型障碍的评估——四条命题、
  新版预筛选（$S,t$、651、690-$t$、$T\cap U$、gcd）；命题 2 待核，命题 3 已证（693 特例）。
- [695](attempts/695_proposition2_proof.md)：**命题 2（强化 690）的证明**——可行 ⇒ $d'\le\dim(\operatorname{row}(H(\mu I-Z'))+T)$；
  由行空间包含关系直接得到，是 690 的 $t$-版本的子空间强化。
- [696](attempts/696_equality_multimu.md)：695 的等号分析——单 $\mu$ 可达（$q\ge D$）；多 $\mu$ 同时是开放问题；
  693 是单特征值的紧例；核心转到 $\{G:\operatorname{rank}P(\mu)\ge d'\ \forall\mu\}$ 的交集。
- [697](attempts/697_correction_T_compatibility.md)：**再次更正**——$(5a)$ 相容性应为 $H_iZ'\in U+T$（$T\subseteq S$）；
  638 的旧证书失效（$HZ'$ 第 2 行 $\notin U+T$），小范围搜索仅 1 个相容 $H$ 且 $T\cap U=0$ ⇒ 638 可行性未定；657/661 复核仍有效。
- [698](attempts/698_638_recheck.md)：**撤回 638 的可行性**——按 $U+T$ 相容性，旧证书无效；已查的 $d'=2$ 类子式全为 $\lambda^2$ 倍数
  （$\operatorname{rank}M=2<4$），其它 $U$ 与相容性矛盾；489/634/637 的“$\omega>s$”结论待重查。
- [699](attempts/699_omega_gt_s_via_661.md)：**$\omega>s$ 仍成立**——661（$q=3$）$U=\mathbb C^2$ 相容性自动，$\operatorname{rank}M=4$，
  是有效例子；638 撤回不影响该结论；随机 35 个相容实例中未再找到 $\omega>s$（稀有）。
- [700](attempts/700_chatgpt_plan_and_stats.md)：ChatGPT 的下一轮计划（四类失败、引理 A/B/C、638 待定）与
  $k=3,q=3,t=1,d'=2$ 的统计：46 个相容实例中 $\operatorname{rank}M$ 分布 $\{2:45,\ 4:1\}$——$\omega>s$ 稀有但存在。
- [701](attempts/701_638_search_d2.md)：638 的 $d'=2$ 搜索——247 个相容 $H$ 中无一使 $\operatorname{rank}M=4$
  （很可能不可行，未证明）；$\omega>s$ 仍由 661 保证。
- [702](attempts/702_638_minors_proportional.md)：638 的 2-子式**全部成比例**（同一二次式的常数倍），故 $\operatorname{rank}M=2$；
  猜想这是 638 的结构性不可行机制（$\bigwedge^2P$ 秩 1），待证。
- [703](attempts/703_chatgpt_exterior_framework.md)：ChatGPT 的外幂/系数秩框架——$\rho_d$（子式系数张成维数）、$\beta_d$、
  结构性不可行判据（$\rho\le r<d$ 且 $\beta\le2r$）；690-T 与 695 一致；$T$ 的适用范围表；$H_0$ 预筛选 $\operatorname{rank}H_A=d'$。
- [704](attempts/704_lambda0_prefilter.md)：$\lambda=0$ 预筛选——可行 ⇒ $\operatorname{rank}H_A=d'$；
  693 的 $e_2$ 情形由 $H_A=0$ 直接排除；建议放在预筛选链最前。
- [705](attempts/705_proportional_minors_infeasible.md)：**比例子式型不可行**——若全部 $d$-子式是同一多项式的常数倍（$\rho_d=1$），
  则 $\operatorname{rank}M\le d<2d$ ⇒ 不可行；638 的 $d'=2$ 不可行归约到 $\rho_2=1$（待证）。
- [706](attempts/706_rho2_stats.md)：638 的 $\rho_2$ 统计——44 个相容实例**全部** $\rho_2=1$（且 $e_1\notin U$）；
  由 705 全部不可行；一般性证明待做。
- [707](attempts/707_638_e1_notin_U.md)：638 的结构引理——相容秩 2 的 $H$ 必有 $e_1\notin U$（否则 $U$ 为 $Z'$-不变 2 维子空间，
  但 $e_1$ 在三个特征向量上分量全非零）；故 $U+T=\mathbb C^3$，与 706 统计一致。
- [708](attempts/708_HA_unique.md)：$U\cap T=0$（$U+T=\mathbb C^3$）时 $H_A$ 与 $P$ 被 $H$ 唯一确定——
  $H_A=\Pi_U(HZ')$（沿 $T$ 投影）；638 的 $\rho_2$ 与 $Z$ 自由度无关。
- [709](attempts/709_638_infeasible_proof.md)：**638 的 $d'=2$ 不可行（完整证明）**——707（$e_1\notin U$）+ 708（$H_A=\Pi_U(HZ')$）
  ⇒ $P$ 的行都在 2 维 $U$ 内 ⇒ $\rho_2\le1$ ⇒ 705 给 $\operatorname{rank}M\le2<4$；638 彻底撤回为反例。
- [710](attempts/710_638_d1_infeasible.md)：**638 的 $d'=1$ 也不可行**——$v\in T$ 不相容；$v\notin T$ 时或 $u=0$ 或 $Zu=\mu u$ 掉秩；
  结合 709，638 正秩完全不可行；$q_{\min}=0$（$r_0=0$ 平凡解）。
- [711](attempts/711_T_fiber_framework.md)：ChatGPT 的 $T$-纤维框架（$\mathfrak I(H)=(d,t,\dim(T\cap U),\rho_d,\deg\gcd)$、三层障碍）
  与 693 的修正（$Z=-I$ 在 $\lambda=-1$ 降秩；改为 $Zu=e_2\notin\operatorname{span}u$，sympy 验证 $\operatorname{rank}M=2$）。
- [712](attempts/712_experiment_A_fiber.md)：实验 A（693 数据）——固定 $H$ 后 $LW$ 的变化空间恰为 $T=\operatorname{span}\{e_1\}$，
  严格小于 $S=\operatorname{span}\{e_1,e_2\}$；确认 692/697 的修正。
- [713](attempts/713_stage_summary.md)：**阶段总结**——677/674/679/687/692/697/690/695/704/705/707-710/661/693 的 proved 清单、
  预筛选链与开放问题（$T$-纤维、$\rho_d$ 分类、多 $\mu$、$\exists H$ 复杂度、665/689 的 $T$-版本）。
- [714](attempts/714_experiment_B_TcapU.md)：实验 B（$Z'=0$）——**$T\cap U=0$ ⇒ 不可行**（$G=0$、$P(0)=0$）；
  $T\cap U=U$ 时 $d'=1$ 可构造可行（$Zu=e_2$，$\operatorname{rank}M=2$）。
- [715](attempts/715_d1_U_in_T.md)：**$d'=1$：可行 ⇒ $U\subseteq T$**（$v\in T$）；$T\cap U=0$ ⇒ 不可行。
  推广了 710 的论证；$d'\ge2$ 的 $\dim(T\cap U)$ 作用仍开放。
- [716](attempts/716_lemmaE_proposal.md)：ChatGPT 的**引理 E**（$\operatorname{rank}(ZX-XA)\le a=\dim(U\cap T)$）与引理 F 提案；
  记录商空间诱导算子的陷阱（需 $(U\cap T)Z'\subseteq T$）；引理 E 的证明有两处待核（左零空间维数、商空间良定义）。
- [717](attempts/717_lemmaE_check.md)：引理 E 的小例检验（$\operatorname{rank}(ZX-XA)=0\le a=1$）与修正——
  可证弱界为 $\operatorname{rank}(ZX-XA)\le k-d+a$；$\le a$ 的强形式仍是 M2 提案。
- [718](attempts/718_lemmaE_search.md)：引理 E 的反例搜索——44 个相容实例中**无** $\operatorname{rank}(ZX-XA)>a$；
  强形式未被推翻（样本有限）。
- [719](attempts/719_k4_search_empty.md)：$k=4$ 的引理 E 搜索——200 组随机样本 0 相容；随机搜索在 $k\ge4$ 效率低，
  需改用构造族（$Z'=0$ 或 $U+T=\mathbb C^k$）。
- [720](attempts/720_lemmaE_Zp0.md)：**$Z'=0$ 时引理 E 成立**——$ZX=GV^+$、$\operatorname{rank}G\le a$、$ZX-XA=(I-XR)ZX$
  ⇒ $\operatorname{rank}(ZX-XA)\le a$；一般 $Z'$ 仍为 M2 提案。
- [721](attempts/721_lemmaE_reduction.md)：引理 E 的精确归约——$r=\operatorname{rank}((I-XR)GV^+)\le\operatorname{rank}G\le t$；
  $Z'=0$ 时 $G\in U\cap T$ 给 $r\le a$；一般 $Z'$ 的强界仍开放（$a=0$ 的 31 例中 $r=0$）。
- [722](attempts/722_strong_bound_d1.md)：一般 $Z'$ 的强界——$d=1$ 已证（$\Pi G=(\Pi Zu)v^{\mathsf T}$，$v\notin T\Rightarrow Zu=\mu u$）；
  $d=2,a=0$ 的 33 个实例 $\operatorname{rank}(\Pi G)=0$（猜想）；引理 F 仍条件性。
- [723](attempts/723_invariance_reformulation.md)：**等价改写**——$\Pi G=0\iff Z(\operatorname{im}H)\subseteq\operatorname{im}H$；
  猜想 $a=0\Rightarrow$ 不变性（$d=1$ 已证，39 例数值支持）；一般 $a$ 对应“缺陷 $\le a$”。
- [724](attempts/724_a0_invariance_obstacle.md)：$a=0$ 不变性的证明尝试——障碍是“行-列桥接”：
  $G$ 的行约束只给 $ZX\overline V$，不直接约束 $Z$ 在 $\operatorname{im}X$ 上的作用；需新引理。
- [725](attempts/725_lemmaE_proof.md)：**引理 E 的完整证明**——商空间桥接 $\operatorname{rank}\overline V=d-a$、$\Pi ZX\overline V=0$
  ⇒ $\operatorname{rank}(ZX-XA)\le a$；推论：$a=0\Rightarrow Z(\operatorname{im}H)\subseteq\operatorname{im}H$、引理 F（$g_\mu\le a$）。
- [726](attempts/726_a_ge_1.md)：**新必要条件**——可行（$d>0$）⇒ $a=\dim(U\cap T)\ge1$（由引理 F：$g_\mu\le a$ 且 $g_\mu\ge1$）。
- [727](attempts/727_631_correction.md)：**更正 631**——$W$ 满行秩不足以保证可行（需 $T=S$）；反例 $N=I,W=I$：$T=0$，$P=H(\lambda I-Z'-I)$ 必降秩。
- [728](attempts/728_audit_665_689.md)：**审计 665/689**——$G$ 的行必须在 $T$（非 $S$）：665 的 $E$ 应为 $T\cap\ker Z'^{\mathsf T}$，
  689 的 $C,B$ 行须在 $T$（$T=0$ 时退化）；预筛选链加入 $T=0$、$a=0$ 排除与 $g_\mu\le a$。
- [729](attempts/729_subagent_scan_cleanup.md)：**子 agent 扫描 + 主 agent 清理**——58 条 S/T/631/661 问题；697 曾为空文件（已重写）；
  **661 因 $T=0$ 对 $d>0$ 不可行 ⇒ $\omega>s$ 重新开放**（638/661 均失效）；631 加反例横幅；691 改 $d'\le t$。
- [730](attempts/730_cleanup_summary.md)：**清理汇总**——子 agent 复核通过（697 非空、5 横幅、0 空文件）；
  给 16 个文件加审计横幅、修 661 标题与 699 正文；ChatGPT 建议 $S/T$ 分层（不盲目替换），先清理再攻方向性预筛选。
- [731](attempts/731_next_priority.md)：清理收尾（678/682/683/686/688 正文 S→T）与 ChatGPT 的下一优先级——
  先攻方向性预筛选严格定理（从 $G_i\in T\cap(U-H_iZ')$ 出发），再推广 715，最后找 $\omega>s$。
- [732](attempts/732_conjecture_d_le_t.md)：**猜想 $d'\le t=\dim T$**——$Z'=0$ 已证（$H_A=G\in U\cap T$）；
  638（$t=1,d'=2$）与 661（$t=0$）均不可行，631 修正版（$t=k$）可行；一般情形待证。
- [733](attempts/733_counterexample_d_gt_t.md)：**反例**——$d'=\omega=2>t=s=1$ 可行（$Z'=\begin{bmatrix}1&2\\1&1\end{bmatrix}$、$H$ 与 $Z$ 显式），
  推翻 732 的 $d'\le t$ 猜想；$\omega>s$ 重新成立。
- [734](attempts/734_direction_rank_lemma.md)：**定理 B（方向性补偿秩）**——可行 ⇒ $d'\le\operatorname{rank}(H(\mu I-Z'))+\dim E_H$，
  $E_H=\operatorname{span}\bigcup_i(T\cap(U-H_iZ'))$；标量 $Z'$ 给 $d'\le\dim E_H\le\dim(U\cap T)$；733 取等。
- [735](attempts/735_665_T_version.md)：**665 的 $T$-版本**——模板需 $\operatorname{row}(V)\subseteq E_T=T\cap\ker(Z'^{\mathsf T})$（不是 $S$）；
  657（$E_T=1\ge d'$）通过，638（$E_T=0$）不可行，733 非模板。
- [736](attempts/736_quotient_direction_conjecture.md)：ChatGPT 的猜想 (D)——$\dim E_H\le\dim(U\cap T)+\operatorname{rank}(H(\mu I-Z'))$；
  若成立则 $d'\le\dim(U\cap T)+2\operatorname{rank}(HM)$；733 平凡成立，$t\ge2$ 待检验。
- [737](attempts/737_D_proof.md)：**猜想 D 的证明**——$F_i=t_i+(U\cap T)$、$t_i\equiv-H_iM\ (\mathrm{mod}\ U)$ ⇒
  $\dim E_H\le\dim(U\cap T)+\operatorname{cls}$（$\operatorname{cls}=\dim((\operatorname{row}HM+U)/U)$）；子 agent 342 例 0 反例、等式 342/342。
- [739](attempts/739_quotient_saturation.md)：**商空间饱和引理**——$\dim E_H=\dim(U\cap T)+\operatorname{cls}$（等式，已证）；
  故 $d'\le\operatorname{rank}(HM)+\dim(U\cap T)+\operatorname{cls}$；数值 342/342 与之一致。
- [740](attempts/740_lean_rank_core.md)：**Lean 内核**——`rank_sub_le`（734 的 $\operatorname{rank}(f-g)\le\operatorname{rank}f+\operatorname{rank}g$）与
  `dim_sup_add_dim_inf`（739 的维数恒等式）在 `ChkRank6.lean` 单文件编译 EXIT=0；未入聚合构建图，故只标内核。
- [741](attempts/741_lean_integration.md)：**Lean 集成**——`Q1RankCore.lean` 进入构建图，`lake build MyProof` BUILD=0（9116 jobs），
  `#print axioms` 仅 propext/Classical.choice/Quot.sound；`check_rules.sh` 仍有既有历史问题（与本文件无关）。
- [742](attempts/742_lean_sub_le_of_le.md)：**Lean 内核收尾**——`q1_rank_sub_le_of_le`（734 的最终形式）入构建图，
  `lake build MyProof` BUILD=0（9118 jobs），公理干净；完整 734/739 仍为纸面。
- [743](attempts/743_eq739_boundary.md)：**739 的边界**——子 agent 664 例（$k=5,6$，cls≥2）等式 664/664；
  空 $F_i$ 使等式失败但本身不可行 ⇒ **可行 ⇒ 等式**；候选 A 说明 $\operatorname{cls}<\operatorname{rank}(HM)$。
- [744](attempts/744_prefilter_theorem.md)：**统一预筛选定理**——704/726/725/690/695/734+739 七条必要条件（含 $d'\le\operatorname{rank}(HM)+\dim(U\cap T)+\operatorname{cls}$）。
- [745](attempts/745_equality_opposite_outcomes.md)：**取等但相反**——638 与 733 都满足 $d'=\operatorname{rank}(HM)+\dim(U\cap T)+\operatorname{cls}=2$，
  638 不可行（$\rho_2=1$）、733 可行（$\rho_2=3,\gcd=1$）；方向性取等不是判据。
- [746](attempts/746_prefilter_certificate.md)：**预筛选证书脚本**（`certificates/verify_prefilter_733_638.py`）精确复现：
  638 与 733 均取等 $R+\dim V+\operatorname{cls}=2$，但 638 $\rho_2=1,\gcd=\lambda(\lambda-1),\operatorname{rank}M=2$；733 $\rho_2=3,\gcd=1,\operatorname{rank}M=4$。
- [747](attempts/747_batch_733_family.md)：**625 例枚举**——733 族中 $B=Z'_{12}$ 是判别量：$B\ne0$ 可行（500），$B=0$ 不可行（125），
  其中 **120 个取等却不可行**；并澄清 687 的“$\gcd$ 与 $Z$ 无关”只在 $G$ 固定时成立。
- [748](attempts/748_factor_source.md)：**因子来源定理**（$d'=k$）——若 $Z'$ 有特征向量 $v\in T^\perp$，则 $P(\mu)v=0$ ⇒ 不可行；
  解释 747 的 $B=0$ 与 661；733 因 $v_1\ne0$ 不适用（可行）。
