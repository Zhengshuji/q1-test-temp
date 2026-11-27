# q1_true · 成果汇总（索引）

> 上级只给一句话 + 等级 + 位置；详细陈述与验证在对应 attempts/ 或 `proof/`。
> 等级按根 `CLAUDE.md` §4：`[已证]` / `[Lean]` / `[精确验证 n/N]` / `[数值]` / `[猜想]`。

## 可借用的组件（不是硬度定理）

| 成果 | 一句话 | 等级 | 位置 |
|---|---|---|---|
| 非零门 | 完整观测器，$(5b)\iff f\ne0$（逐行可提升） | M2 + 精确验证 | `workspace/q1_true/multiplication_gate/attempts/296_nonzero_gadget_observer.md` |
| 输入非零门 | $(5a)\wedge(5b)\iff x\ne0$ | M3 + 精确验证 | `augmentation_family/attempts/303_expert_lifts.md` |
| 非零门直和 | 块对角，$(5b)\iff f_1\ne0\wedge f_2\ne0$（合取） | M2 + 精确验证 | `workspace/q1_true/multiplication_gate/attempts/297_direct_sum_gadgets.md` |
| 混合块 | $(5a)$ 强制 $z=xy$，但变量是见证变量，不是输入 | M2 + 精确验证 | `workspace/q1_false/decision_algorithms/attempts/299_mixed_gate.md` |
| 提升判据 | $(H_i,H_{A,i})\in\operatorname{row}[N\ AN]$（硬门槛） | M2 | `workspace/q1_false/decision_algorithms/attempts/288_lift_rank_bound.md` |

## 负结果 / no-go

| 结果 | 一句话 | 位置 |
|---|---|---|
| 乘法门不 sound | 完整观测器 realization 下 $R=0$ 仍满足 $(5a)(5b)$ | `augmentation_family/attempts/306_...`（见 LESSONS） |
| wiring 障碍 | 复制整行强制 $y_1=1$；无单坐标复制机制 | `augmentation_family/attempts/305_...` |
| port rigidity | 固定局部子空间冻结 $W$，移动端口需 $E_2$ 依赖参数 | `augmentation_family/attempts/309/310` |

## 没有的东西

- **没有归约**，因此没有 NP-hard / $\exists\mathbb R$-hard 定理；
- 唯一完整的 sound 组件是“非零/输入非零”，它们只能表达**合取**，不能表达乘法。
