# multiplication_gate · 现状

> 上级：[q1_true](../STATUS.md)。attempts：本目录 `attempts/`（180 个文件，编号至 628）。

- 已有 sound 组件：非零门（296）、输入非零门（303）、直和合取（297）、提升判据（288）。
- **缺乘法门**：复制整行会强制 $y_1=1$；单坐标复制无机制。
- 最近判断（391–392）：钉住 ⟹ 线性；不钉住 ⟹ 逃逸；可行集是线性空间的 Zariski 开集。
- 下一步：copy/format gadget $(0,y,z)\to(0,1,z)$ 的精确目标，或不可能性引理。

## 2026-11-27：组合接口
- [506](attempts/506_composition_R0_spurious.md)：303 B 的 $R=0$ 伪解写成引理（任意 $x,y,z$ 都满足 $(5a)(5b)$）；
  组合 soundness 需要：强制门自由行非零，并让该非零条件与门的变量共享同一 $R$ 条目/同一 $AN$ 列。
- 下一步：构造全局 $A$，让同一自由行同时充当 296 的 $f$ 与 303 B 的 $\beta$。
- [507](attempts/507_R0_means_zeroing.md)：$R=0$ 的精确含义是“门变量可被置零”，缺 equality/constant gadget；
  固定行 $q=r_0$ 时 $(5a)$ 化为 $l_1AN\parallel l_1N$（可含二次项）。$k=2$ 小枚举 0 命中，下一步 $k=3$。
- [508](attempts/508_fixed_row_linear_term_barrier.md)：$k=2$ 固定行的“一次项障碍”——
  $\det[l_1AN;l_1N]$ 要产生一次项 $z$ 需除法，故 $c(z-xy)$ 不可能；507b 的 0 命中得到解释。
- [509](attempts/509_fixed_row_invariance.md)：固定行 $q=r_0$ 的精确刻画——$(5a)\iff$ 压缩行空间在 $A$ 下不变；
  $H_0$ rank 1 不提供新东西（与 508 同）；rank 2 时次数可达 3，$z-xy$ 原则上可出现。下一步 $k=3,r_0=2$ 小枚举。
- [510](attempts/510_fixed_row_scaling_barrier.md)：$k=3,r_0=2$ 的缩放障碍——单个 $3\times3$ 子式不能等于 $c(z-xy)$
  （叉积常数分量与 $v$ 含 $x$ 因子不可兼得）；下一步搜“联合条件”的公共零集。
- [511](attempts/511_input_controlled_gate.md)：**第一个输入控制的 $(5a)$ 乘法门**（$q=r_0=2,k=3$，无自由行）：
  $L_0=[[z,x,0],[1,0,1]]$、$A=[[1,0,0],[1-y,0,1],[0,-1,1+y]]$ 给出 $(5a)\iff z=xy$（精确）。
  但 $(5b)$ 全门失败：三个子式共享 $q=\lambda^2-\lambda(y+1)+1$（ChatGPT 更正）。下一步打破 gcd。
- [512](attempts/512_row3_cannot_break_gcd.md)：改 $A$ 第三行**不能**打破 gcd——只要 $l_2=(1,0,1)$、$D_2=z-xy$，
  三个子式仍共享 $Q=\lambda^2-\lambda(y+\alpha)+1$（$\alpha$ 任意）。必须改 $l_2$ 或 $l_1$。
- [513](attempts/513_l1_locks_l2.md)：$l_1=(z,x,0)$ 时 $D_1$ 的门上条件强制 $l_2\parallel(1,0,1)$——512 的 gcd 不可避免。
- [514](attempts/514_l1_zx1_locked.md)：ChatGPT 建议的 $l_1=(z,x,1)$ 仍被锁死（$b=0,c=a,q=0,p=r$），
  且 $D_2=a^2x$ 失去 $z$ 项，不可能等于 $c_0(z-xy)$。下一步换 $l_1$ 的形状（$z$ 放第三位等）。
- [515](attempts/515_l1_shapes_symbolic.md)：五种 $l_1$ 形状的符号消元——四种与常数 $l_2$ 不相容，
  $(z,0,x)$ 的两族分别退化或带 $x$ 项，均不可用。
- ChatGPT 建议下一步：允许 $l_2$ 含一次项（9 参数），固定 $r_1,r_2$；判据仍是 $D_1|_{z=xy}\equiv0$ 有非退化解且 $D_2$ 不被迫为零。
- [516](attempts/516_l2_linear_no_gate.md)：$l_2$ 取 9 参数一次式仍无门——非退化形状的 $D_2$ 含 $x^2,xz,x$ 等
  杂项，无法等于 $c_0(z-xy)$；另两形状 $D_2=0$。下一步改 $r_1,r_2$。
- [518](attempts/518_omega_q_obstruction.md)：$q=r_0=2$ 的乘积门**整体不可行**——门上 $\omega=q=2$ 时
  $P=(\lambda I-Z)H_0$ 必有特征值；511–517 的失败都是这个障碍。$(5a)\iff z=xy$ 可由 $E\ne0$ 真实落地（$n=5$）。
- 下一步：$q\ge3$、$\omega<q$ 的固定行门，或回自由行 gadget（296 的 $\omega=1<q=2$）。
- [519](attempts/519_q3_omega2_compressed_gate.md)：$q=3,\omega=2$ 的**压缩门存在**——
  $H_0=[[z,x,0],[y,1,0],[0,0,1]]$（$\det=z-xy$），$H_{A,0}$ 取 $h_2,h_3$ 的组合；
  $(5a)$ 恒成立、门上 $\gcd=1$、$z\ne xy$ 时 $\omega=3$ 由 518 障碍失败 ⇒ 可行 $\iff z=xy$。
  落地受 $n=5$ 的 $E$ 秩 1 限制；下一步在 4 参数 $A_{00}$ 族里让 $(5b)$ 成立。
- [520](attempts/520_sound_multiplication_gadget.md)：**（单向）sound 乘法 gadget**——$n=5,q=3$，$(5a)$ 恒成立、
  $(5b)$ 门上 $\iff x\ne-1/2$，故可行 $\Rightarrow z=xy$。
- [526](attempts/526_lean_correction.md)：**Lean 核验 + 修正**——`det_D1/det_D2/M2_sub/common_root` 编译通过；
  $\operatorname{Res}(M_1,M_2)=64(2x+1)^2$，坏超平面 $x=-1/2$ 上完备性失败（反例 $(-1/2,2,-1)$）。
  归约须避开坏超平面；在找到之前 520/521/522 只标“单向 sound”。
- [521](attempts/521_block_composition.md)：块对角组合 sound——整体可行 $\iff$ 两条乘法都成立；
  变量共享（同一符号出现在多个块）不破坏证明，wiring/equality 自动。下一步：串成算术电路。
- [522](attempts/522_chain_and_scope.md)：链式检查器成立（$x_2:=z_1$）；但 520/521 是**实例检查器**，
  不是变量编码器——q1 的唯一量词是 $\exists L$，而 520 的 $q=r_0$ 没有自由行。归约需要未知量进入 $R$。
- [523](attempts/523_naive_injection_fails.md)：naive 变量注入（$rN=(x,y,z)$）不破坏 $(5a)$，但让 $\ker H=0$、
  门消失；$(5b)$ 要么恒失败、要么循环。下一步：混合行 / 核依赖 $R$ / 非零锚。
- [524](attempts/524_unknown_encoding_constraints.md)：**结构约束**——$(5a)$ 对 $R$ 线性，二次关系只能来自 $(5b)$ 的 gcd；
  最小 setup：$n=3,k=2,q=3$（两固定行 + 一自由行）。下一步在该族做符号搜索。
- [525](attempts/525_n3k2_too_permissive.md)：$n=3,k=2,q=3$ 族太宽松——486 个 $(5a)$ 点中 438 个可行，没有门；
  下一步扩到 $k=3$、$q=4$。
- [528](attempts/528_no_bad_set_gadget.md)：**无坏集的压缩 gadget**——$H_{A,0}=[-2h_2-2h_3;-2h_3;0]$，
  门上三子式 gcd=1 对所有 $x,y$（$d_{23}=\lambda^2$、$d_{12}(0)=4$）。压缩层可行 $\iff z=xy$。
  $p=1$ 落地不可能（秩 1 的 $E$）；下一步 $p=2$。
- [530](attempts/530_p2_realization.md)：**无坏集 sound gadget 落地**（$p=2$、$n=7$、$q=3$）——
  可行 $\iff z=xy$ 对所有 $x,y,z$（含 $x=-1/2$）。原始矩阵 5 点核验；Lean 核验 gcd 核心（529）。
  下一步：块对角组合（521）+ 变量共享。
- [531](attempts/531_block_530.md)：两个 530 gadget 的块对角合取（$p=4,q=6$）——可行 $\iff$ 两条乘法都成立；
  $x=-1/2$ 仍可行（无坏集继承）。Lean 核验 530 实际常系数版（`no_common_root` 等 5 条）。
- [532](attempts/532_chain_square.md)：链式（$z_2=z_1y_2$）与平方（$z_1=x_1^2$）电路成立——
  可行 $\iff$ 电路约束成立；$x=-1/2$ 仍可行。剩余缺口：未知量在 $R$（522）。
- [533](attempts/533_unknown_interface_objection.md)：未知量接口——ChatGPT 的“线性参数化”方案与结构反驳
  （$L_0$ 固定，$R$ 只能进自由行；523 已证 naive 注入使门消失）。下一步：混合行 $h_3=h_{3,0}+rN$。
- [534](attempts/534_degree_count_free_rows.md)：**次数计数**——$(5b)$ 子式关于 $R$ 的次数 $\le$ 含 $R$ 的行数；
  一个自由行只能编码线性条件，$z=xy$ 需要 $m\ge2$（$q\ge r_0+2$）。下一步 $q=5,m=2$。
- [535](attempts/535_q5_redundant_rows.md)：$q=5$ 冗余自由行 ansatz 压缩层成立（gcd=1、门外 $\lambda=0$ 掉秩），
  但门仍在固定数据上；且 $H_{A,0}=0$ 与 $r_iN=r_iAN$ 不能同时落地。
- [536](attempts/536_free_row_gate_obstruction.md)：自由行门的结构障碍——$(5b)$ 在 $\lambda=0$ 要求 $\operatorname{rank}H_A=\omega$；
  $H_0=\operatorname{diag}(1,1,0)$ 迫使 $u_3=v_3=0$。要编码 $u_3=u_1u_2$ 须 $H_0$ 秩 1、$\omega=2$。
- [537](attempts/537_homogeneity_obstruction.md)：**齐次性障碍**——$H_{A,0}=0$ 时所有子式关于 $R$ 齐次，
  编码不了非齐次的 $z-xy$；须 $H_{A,0}\ne0$ 提供常数项（混合结构）。
- [538](attempts/538_graded_minors.md)：精化——$P$ 的条目都齐次，子式按“涉及的自由行数”分次；
  单个子式不能等于 $u_3-u_1u_2$，混合次数只能来自跨子式的 gcd 条件。
- [539](attempts/539_diagonal_ansatz_no_gate.md)：对角 ansatz（$H_0=I_3$、$A_0=\operatorname{diag}(1,0,0)$、$B$ 对角）
  的 3×3 子式 gcd 恒为 1 ⇒ 无门；对角结构只能给线性条件。下一步非对角 $B$。
- [540](attempts/540_nondiag_B_no_factor.md)：非对角 $B$（循环置换）的 10 个子式两两 resultant 均不被
  $u_3-u_1u_2$ 整除；下一步稀疏 $B$ 族搜索。
- [541](attempts/541_freeze_linear_interface.md)：$B_1\ne B_2$ 的最后实验 0 命中；**冻结线性行变换接口**，
  下一阶段转“非线性提升接口”（$R$ 条目进高维辅助子空间）。530/531/532 的结果保留。
- [542](attempts/542_nonlinear_lifting_kernel.md)：**非线性提升接口**——$\operatorname{rank}H=2$ 时核向量是自由行的叉积（二次），
  $(5a)$ 给出三次方程，可绕开“子式齐次”的限制。下一步：$h_1=e_1$ 的最小三次方程组。
- [543](attempts/543_cross_kernel_lean.md)：叉积核向量的 **Lean 核验**（`dot_u_cross`、`dot_v_cross`、`e1_dot_cross`，退出码 0）。
  下一步：$h_1=e_1$ 的三次方程组搜索。
- [544](attempts/544_stage_summary.md)：**阶段总结**——sound gadget（520/528/530）、合取/电路（521/531/532）、
  未知量编码的三重障碍（522/533、534、537/538）、线性接口冻结（539–541）、三次接口进行中（542/543）。
- [546](attempts/546_projective_reduction.md)：**射影化归约**——可行集是锥，只能编码齐次关系；
  目标改为 $zw-xy=0$（$w\ne0$ 时等价于 $z=xy$）。下一步：共享变量匹配（$v=Mu$）。
- [547](attempts/547_shared_variables_not_forced.md)：$v=Mu$（546 方式 1）不能由实例强制——
  $u=r_1N,v=r_2N$ 由求解者选择；要强制就循环。剩：双线性配对/锚点归一化/改量词结构。
- [595](attempts/595_block_conjunction_circuits.md)：**块对角合取 + 算术电路编码**——594 的乘积门可块对角组合，
  同法得线性门（$\ell=0$）；链 $z_2=z_1r_3$ 的精确验证通过；q1_true 路线重新打开（归约未完成）。
- [596](../../q1_false/feasibility_geometry/attempts/596_realizability_correction.md)：**595 的 $H_A=ZH$ 不可实现**，
  门不成立；q1 对应右铅笔 $P=H(λI-Z')$，需重做。
- [602](attempts/602_mixed_conjunction_circuits.md)：**混合合取**（线性门 601 + 乘积门 598）——精确验证通过；
  算术电路（$+,\times$）可在 q1 中编码；归约骨架完成，{\min}$ 的下界未处理。
- [603](attempts/603_qmin_monotonicity.md)：**单调性**（570 的零行扩张）⇒ $q=Q$ 可行 $\iff q_{\min}\le Q$；归约剩下的关键是**可靠性**：任意 $H$ 满足 $(5b)$ 是否强制所有门成立（开放）。
  归约剩下的关键是**可靠性**：任意 $ 满足 $ 是否强制所有门成立（开放）。
- [605](attempts/605_reliability_counterexample_rank1.md)：**可靠性反例**——$H=uv^{\mathsf T}$（秩 1），
  只要 $v$ 不是 $Z'$ 的左特征向量，$(5b)$ 就成立、绕过所有门；电路编码**不健全**，需重设计。
- [606](attempts/606_min_rank_trivial_5a.md)：最小秩计算——$H_A=HZ'$（$AN=NZ'$）下 $\min\operatorname{rank}H=1$，
  $(5a)$ 自动、无下界作用；块对角框架先天不健全，需 $AN\ne NZ'$ 使 $(5a)$ 非平凡。
- [607](attempts/607_nontrivial_5a_rank1_blocked.md)：一般分解 $H_A=HZ'+G$（$G=LW$）；$W\ne0$ 时秩 1 逃逸
  只在 $v_1=0$ 且 $v$ 为 $Z'$ 左特征向量时存活——一般被阻断。下一步两块最小秩。
- [608](attempts/608_stage_summary_right_pencil.md)：**阶段总结**——有效（598/601/602/603/604/607）与已撤回（594/595、599/600、605/606）；
  缺口：可靠性（$W\ne0$ 能否排除低秩逃逸）、两块最小秩、归约。
- [609](attempts/609_rank1_classification.md)：秩 1 逃逸的完整分类——情形 B（$v$ 为 $Z'$ 的、第一坐标为 0 的左特征向量）
  仍存活；选 $Z'$ 使所有左特征向量第一坐标非零可消除它。
- [610](attempts/610_rank1_J_vs_two_blocks.md)：情形 A 的秩 1 必在 $\lambda=\mu$ 掉秩；单块 $J$ 阻断秩 1；
  两块 $Z'=\operatorname{diag}(J,J)$ 仍可经 $e_4$ 逃逸——需跨块混合的 $Z'$。
- [611](attempts/611_block_diagonal_obstruction.md)：**结构障碍**——块对角 $Z'$（$\ge2$ 块）必有第一坐标为 0 的左特征向量，
  秩 1 逃逸必然存在；要阻断需不可约 $Z'$，但这与块对角门不相容。
- [612](attempts/612_irreducible_Z_stopped.md)：不可约 $Z'$（循环移位）——秩 1 被阻断，但秩条件化为“核与零和超平面
  相交维数”，**未恢复乘积门**；按判据停止该路线。
- [613](attempts/613_irreducible_gate.md)：**不可约 $Z'$（循环）的乘积门**——$H=[[r_1,z,0],[1,r_2,0],[0,0,1]]$，
  可行 $\iff r_1r_2=z\wedge r_2\notin\{1,\omega,\omega^2\}$；秩 1 逃逸被阻断；sympy 四点验证。
- [614](attempts/614_irreducible_multi_gate_count.md)：不可约 $Z'$ 多门——$\lambda=1$ 处需“恰好一个核向量落在
  $\operatorname{im}M$”，给出 6 个“二选一”条件；具体等价性待算。
- [615](attempts/615_six_cycle_no_gate.md)：六阶循环 + 块对角 $H$——秩在所有 6 次单位根处恒等于 $\omega$，
  **无门**（精确验证）；不可约多门未成功。
- [616](attempts/616_coupled_H_no_gate.md)：跨块耦合的 $H$（加 $H_{0,4}=1$）仍无门（秩恒等于 $\omega$）；
  按判据**停止组合路线**，转向全局多项式约束归约。
- [617](../../q1_false/feasibility_geometry/attempts/617_evidence_polynomial.md)：结构证据汇总（M2）——多门组合路线停止；
  q1_true 仅剩“全局多项式编码”值得一试。
- [628](attempts/628_free_satisfiable_audit.md)：**M2 审计**——598/601/613 全是“自由可满足型”（自由行可取任意 $H$，
  门条件有解 ⇒ 求解者可满足），不能承载 hardness；q1_true 自由行 gadget 路线关闭；仅数据层（530）是数据分离型。
