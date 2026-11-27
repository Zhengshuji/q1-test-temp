# 超平面层论文（草稿工作区）

> 目标：把本会话已完成的结果写成一篇独立论文。架构与写作规格见专家 106 号的裁决
> （[attempts/388](../augmentation_family/attempts/388_expert106_structure.md)）：
> **结构在前**；四条贡献；**三条主张必须分清**；闭性与满秩引理统一；实点稠密性明写。

## 节与状态

| 节 | 文件 | 行数 | 状态 |
|---|---|---|---|
| 1 引言 | [sec1_intro.md](sec1_intro.md) | ~50 | 初稿 |
| 2 预备与压缩表述 | [sec2_prelim.md](sec2_prelim.md) | ~60 | 初稿 |
| 3 几何与参数化 | [sec3_geometry.md](sec3_geometry.md) | 301 | 初稿（子 agent） |
| 4 精确代数判定 | [sec4_decision.md](sec4_decision.md) | 262 | 初稿（子 agent） |
| 5 固定 $p$ 位复杂度 | [sec5_complexity.md](sec5_complexity.md) | 225 | 初稿（子 agent） |
| 6 重复特征值反例 | [sec6_counterexample.md](sec6_counterexample.md) | 303 | 初稿（子 agent，已与 c357 逐项核对） |
| 7 与既有压缩表述的关系 | [sec7_relation.md](sec7_relation.md) | ~45 | 初稿 |
| 附录 A 完整数据与证书 | [appA_data.md](appA_data.md) | ~90 | 初稿 |
| 附录 B 高度与算术界 | [appB_heights.md](appB_heights.md) | 218 | 初稿（子 agent） |
| 附录 C 子结式估计 | [appC_subresultant.md](appC_subresultant.md) | 164 | 初稿（子 agent，含手算例） |

**合订本**：[draft_all.md](draft_all.md)（**1720 行**，按 1→7→附录 A→B→C 顺序拼接；`$$` 配平 298 个）。

## 装配记录

- 交叉引用已改：第 5 节原先引用的"第 3 节的引理 A / 定理 1′"改为实际的**引理 3.6 / 定理 3.15**。
- 底域统一为 $\mathbb R$（第 1、2 节原写 $\mathbb C$，已改）；$\lambda$ 仍取 $\mathbb C$。
- 记号冲突已注明：本文的 $\rho=\operatorname{rank}[C;CA]$ 与"层号"不是同一个量（第 2.1 节已注明）。
- **(S2) 的地位**：$\dim(V\cap K_0)=k-1$ 不是由 $c=1$ 与 $(5a)$ 推出的定理，而是层号定义的直接展开（$\omega:=\operatorname{rank}H=\dim(V\cap K_0)$）；第 3 节按此写法，正文须保持一致。

## 统一约定

- 记号以第 2 节为准：$K_0,k,\rho,N,H,H_A,\omega,c$、$M,A_{21},E_\mu,E_\mu^0,U_v,D_v,\mathcal Q_v,V_0,\delta,s,r(v)$。
- 层的条件是 $(5a')/(5b')$；谱条件用引理 2.1（公根）。
- 三条主张（第 1.5 节）：整层精确判定 / 几何单谱多项式 / 反例只否定某约化。
- 每条结果标注状态：**已证**（本文）／**引用**（既有工作）／**精确计算**。
- 不写日期、不写仓库路径、语气中立。

## 标题（暂定）

> Functional-Observer Feasibility in the Hyperplane Layer: Structural Parameterization, Exact Decision, and Fixed-Parameter Complexity

## 组装顺序

1. 四节草稿齐 → 统一记号与编号（定理/引理/命题按出现顺序重编）；
2. 写附录 A/B；3. 交叉引用检查；4. 与 `docs/02` 的既有命题对账，避免重复声称。
