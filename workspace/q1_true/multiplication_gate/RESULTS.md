# multiplication_gate · 成果

| 成果 | 等级 | 位置 |
|---|---|---|
| 非零门：$(5b)\iff f\ne0$，完整观测器、逐行可提升 | M2 + 精确验证 | `attempts/296_nonzero_gadget_observer.md` |
| 输入非零门：$(5a)\wedge(5b)\iff x\ne0$ | M3 + 精确验证 | `attempts/303_expert_lifts.md` |
| 非零门直和（合取） | M2 + 精确验证 | `attempts/297_direct_sum_gadgets.md` |
| 混合块：$(5a)$ 强制 $z=xy$，但用见证变量 | M2 + 精确验证 | `attempts/299_mixed_gate.md` |
| 提升判据 $(H_i,H_{A,i})\in\operatorname{row}[N\ AN]$ | M2 | `attempts/288_lift_rank_bound.md` |

**没有**：sound 的乘法门，因此没有归约。
| **（单向）sound 乘法 gadget**：$q=3,n=5$，$(5a)$ 恒成立、$(5b)$ 门上 $\iff x\ne-1/2$，故可行 $\Rightarrow z=xy$；坏超平面 $x=-1/2$（526 修正） | **[已证-纸面]** + **[Lean]** + **[精确验证]** | `attempts/520_sound_multiplication_gadget.md`、`526_lean_correction.md` |
| 块对角组合：两个 520 gadget 的合取 sound；变量共享不破坏 | **[已证-纸面]** + **[精确验证]** | `attempts/521_block_composition.md` |
| **无坏集 sound 乘法 gadget（p=2 落地）**：$n=7,q=3$，可行 $\iff z=xy$（含 $x=-1/2$）；Lean 核验 gcd 核心 | **[已证-纸面]** + **[Lean]** + **[精确验证]** | `attempts/530_p2_realization.md` |
| 两个 530 gadget 的块对角合取：sound 且无坏集继承（$p=4,q=6$） | **[已证-纸面]** + **[Lean]** + **[精确验证]** | `attempts/531_block_530.md` |
| 链式/平方电路：530 块对角 + 共享变量，可行 $\iff$ 电路约束成立（含 $x=-1/2$） | **[已证-纸面]** + **[精确验证]** | `attempts/532_chain_square.md` |
