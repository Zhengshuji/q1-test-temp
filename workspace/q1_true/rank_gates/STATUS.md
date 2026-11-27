# rank_gates · 现状

> 上级：[q1_true](../STATUS.md)。**q=5 结构化秩门已冻结**（2026-11-27，505）；attempts 39 个文件（218–505）；规划 [PLAN.md](PLAN.md)。

## 已知

- $q=2$：完整 no-go（非平凡门与 $(5b)$ 不可兼得，M2 纸面）；
- $q=4$：压缩门存在、不可逐行提升（M2 + 精确验证）；
- $q=5$：三情形被堵，仅搜索边界；
- “$\omega\le r$”：已撤回。

## 当前里程碑

按 ChatGPT 评估：**先统一参数化 + 完整符号消元**，不直接做 $q\ge6$ 分类。

1. 写 $q=4,5$ 的 $B$、$H_0$、$H_{A,0}$ 显式坐标（用 281/285 校准）；
2. 对 $R$ 的辅助行做符号消元（保留 $(5a)$ 的 $R$ 项）；
3. 有非平凡门 → 做提升与 $(5b)$ 守卫；无解 → 提炼 $q\ge4$ 障碍。

## 失败判据

- 第 2 步：得到非平凡门（成功），或消元给不出双向等价判据（失败）；
- 第 3 步：出现 $q\ge6$ 的符号可行实例，或障碍依赖特殊参数（失败）。

## 进展（2026-11-27）

- 统一参数化已写（PLAN §1）；
- [490](attempts/490_q4_family_probe.md)：在 $q=4$ 可提升族里，$\det H=0$ **不是门**——14 个 $(5a)$ 点中 12 个
  同时满足 $(5b)$。门必须来自**参数相关的公根**（谱条件），不是秩退化。
- 490b：$(5a)$ 子簇上失败点只占 9/36（多为 $s_1=0$ 或 $s_2=0$），失败集是真子集 ⟹ 该族**没有强制门**。
- 491：$k=5$ 随机 400 点只有 3 个 $\operatorname{rank}H=3$、0 个满足 $(5a)$ ⟹ 采样无效，必须联合参数化。
- ChatGPT（第二次）：先扩 $k=5,6$ 不扩 $q$；判据 $D|_S\equiv0$；有 $D\ne0$ 反例即否定该族；全类型反例则改 $H_0,H_{A,0}$ 结构。
- 下一步：$k=5$ 的联合参数化已写进 PLAN（10 变量 + 5 个秩方程 + ker 包含；先做结构化子族），待符号消元。
- [492](attempts/492_k5_span_subfamily.md)：子族 $r_2\in\operatorname{span}(e_1,e_2,r_1)$ **恒不可行**
  （$(5a)$ 迫使 $r_{1,4}=r_{1,5}=0$，$H_A$ 秩 $\le2$，$\lambda=0$ 掉秩）⟹ 该类型 no-go；$L_0=[e_1;e_3]$ 同样。
  ChatGPT 复核：无代数漏洞，但只对该子族成立。
- [493](attempts/493_q4_k5_family_infeasible.md)：**整族 no-go**——$q=4,k=5,L_0=[e_1;e_2]$、$A$ 移位时，
  $\operatorname{rank}H=4$ 不可行（$H_A=ZH$，$P=(\lambda I-Z)H$ 有特征值），秩 3 的两种情形都被排除。
  ChatGPT 复核：闭合；不推广到其他 $k$/$A$/$H_0$。
- 下一步：换 $k$、$A$ 或 $H_{A,0}$ 的结构（或 $q=5$），不要在该族上继续。
- 493b：换成 $K_0$ 上的上移位 $J_5$ 后，同一子族 300 点中有 4 个可行——493 的 no-go 是下移位 $A$ 的偶然；
  但可行集仍是开集，也不是门。
- [494](attempts/494_q4_L0e1e3_infeasible.md)：$L_0=[e_1;e_3]$、$A=J_5$ 的**整族空集**：$(5a)$ 迫使 $\operatorname{rank}H=4$，
  而 $q=4$ 的 $\omega=4$ 不可行。ChatGPT 复核通过（限该族）。
- [495](attempts/495_q5_natural_lift_fails.md)：$q=5$ 的自然提升（$A00$ 移位、$E=e_4^*$）下 285 的门不可实现——
  $\ker H=\operatorname{span}(e_2)$，$H_Ae_2=H[:,3]\ne0$。下一步换 $A00/E$。
- [496](attempts/496_eigenvector_obstruction.md)：**特征向量障碍**——$K_0$ 内 $A$ 的特征向量若不在 $\ker H$，$(5b)$ 必失败；
  扫描（$e_3$ 固定）373/400 满足 $(5a)$ 但 0 可行。下一步试非半单 $A00$（单 Jordan 块）。
- [497](attempts/497_q5_fullshift_rank3_open.md)：完整移位 $A$：rank-4 排除；结构化 172 个 rank-3 点全部 $(5b)$ 失败，
  但 ChatGPT 判定 rank-3 分支**未解决**（需查 $\operatorname{im}H\cap E_\mu(Z)$）。
- [498](attempts/498_q5_rank3_excluded.md)：**rank-3 分支关闭**——$(5a)$ 迫使 $\operatorname{rank}H_A\le2$
  （所有 $rQ$ 落在同一 2 维子空间），$\lambda=0$ 掉秩。ChatGPT 复核通过。该族可行实例只能 $\omega\le2$；
  285 的门在 $z=xy$（$\omega=2$）的可行侧，下一步检验它。
\n- [499](attempts/499_q5_gate_kernel_conflict.md)：285 的门在完整移位族里不可提升——=xy$ 时 $\\ker H\\ni e_2$ 自由，而 =H[:,3]\\ne0$。\n- [500](attempts/500_q5_candidateA_forces_x_zero.md)：换 $（=0$）后 $ 给 =xLe_1$；=[e_1;e_1]$ 第 5 坐标为 0 ⇒ =0$，门退化。下一步 =[e_1;e_5]$。\n
- [499](attempts/499_q5_gate_kernel_conflict.md)：285 的门在完整移位族里不可提升——$z=xy$ 时 $\ker H\ni e_2$ 自由，而 $H_Ae_2=H[:,3]\ne0$。
- [500](attempts/500_q5_candidateA_forces_x_zero.md)：换 $A$（$Ae_2=0$）后 $(5a)$ 给 $Le_5=xLe_1$；$L_0=[e_1;e_1]$ 第 5 坐标为 0 ⇒ $x=0$，门退化。下一步 $L_0=[e_1;e_5]$。
- [501](attempts/501_q5_x_pinned_by_L0.md)：$L_0=[e_1;e_5]$ 也不行；$(5a)$ 把 285 门的 $x$ 钉成 $L_0$ 的列比，**$x$ 不是自由变量**。需重新设计门。
- [502](attempts/502_gate_logic_omega2.md)：门的逻辑——$(5a)$ 给 $\operatorname{rank}P\le\omega$；on-gate 需 $\omega=2$ 且 $Z|_W$ 无特征向量，off-gate 需 $\omega=3$ 且失败。下一步构造 $\omega=2$ 的提升。
- [503](attempts/503_standard_kernel_Ainvariance.md)：$e_j\in\ker H$ 且 $Ae_j\in K_0$ ⇒ $Ae_j\in\ker H$；完整移位下 $e_2\in\ker H$ 迫使第 2,3,4 列为零，与 285 门冲突。下一步：构造无标准核向量的门。
- [504](attempts/504_noncoordinate_kernel_fails.md)：非坐标核也失败——完整移位下 $(5a)$ 迫使 $x=1$（门退化）；候选 $A$ 下迫使 $Le_1=Le_5=0$（矛盾）。
- [505](attempts/505_q5_targeted_freeze.md)：非移位 $A$ 的定向实验 600 点 0 可行；**冻结 $q=5$ 结构化秩门**（一般 $q=5$ 未解决）。
