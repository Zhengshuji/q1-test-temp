# 403 $c=2$ 的 Lean 核验：$K$-split 纤维的三条引理；以及一轮过程自查

> 承接 393–402。用户要求：能 Lean 的验证一下、查过程有无问题、无问题则送专家审。

## 目标

1. 把 $c=2$ 里**可形式化**的部分做成 Lean（构建 + 公理审计）；
2. 对 391–402 这条链做一轮自查，列出发现的问题与更正；
3. 汇总送审。

## 设想与理由

$c=2$ 的结果按可形式化程度分三类：

| 结果 | 可形式化性 |
|---|---|
| 纤维的**集合/维数**断言（393 命题 2 的 (i) 与维数部分） | **可**：纯线性代数（子空间交、正交补、维数加性） |
| $V\subseteq(D+AD)^\perp\iff W\subseteq T_D$（命题 2 的 (ii)） | 可，但要用 $A_{21}=\pi_{K^\perp}A|_K$ 的定义与 $M(D)\subseteq D$；未做 |
| 底几何 $\mathcal I_2(M)$ 的三情形、推论 4（单谱有限） | 需实 Jordan 型/特征向量理论；未做 |
| 图卡定理（394）、统一形式（398）、层不单调（397） | 不可（构造性/计算性论证） |

## 做法

新模块 `Q1Paper/HyperplaneC2.lean`（`namespace Q1Paper`），三条引理：

1. `sup_inf_eq_left_of_le_orthogonal`：$D\le K$、$W\le K^\perp$ ⟹
   $((K\sqcap D^\perp)\sqcup W)\sqcap K=K\sqcap D^\perp$；
2. `disjoint_of_le_orthogonal`：$W\le K^\perp$ ⟹ $W$ 与 $K\sqcap D^\perp$ 不交；
3. `finrank_sup_of_disjoint_of_le_orthogonal`：$\dim V=\dim(K\sqcap D^\perp)+\dim W$（即 $q=(k-c)+t$）。

接入：`Q1Paper.lean` 加 import；`Q1Paper/Audit.lean` 加 import 与三条 `#print axioms`。

## 进展

- **位置更正（用户指示）**：这三条**不进 Q1Paper**（论文树）——内容尚未固定。
  已移到 **`~/WorkSpace/lean4/MyProof/MyProof/HyperplaneC2.lean`**，`namespace Q1PaperC2`，
  用 `lake build MyProof.HyperplaneC2` 与 `lake env lean MyProof/HyperplaneC2.lean` 两种方式各编译一次（**都是 exit=0**）；未接入 MyProof 的聚合图
  （`MyProof.lean` 由脚本生成，未固定前不入图）。
- Q1Paper 侧已回退：删 `Q1Paper/HyperplaneC2.lean`、还原 `Q1Paper.lean` 与 `Audit.lean`；
  `lake build Q1Paper` 重新为 **exit=0（9090 jobs）**；artifact 仓库用 `git revert` 撤掉
  （推送 `e52add1..ac7b139`），`git diff e7ad550` 为空。
- 三条声明的 `#print axioms` 只含 `propext`、`Classical.choice`、`Quot.sound`（在 MyProof 侧逐条打印）；
- `tools/lean/STATEMENT_MAP.md` 已改登记为 MyProof 位置与命名空间。

### 一处需要记的坑

`ᗮ` 记号只在其 import 链里可见：单引 `Mathlib.Analysis.InnerProductSpace.Basic` 会报
"expected token"（解析不了 `Kᗮ`）；引 `Q1Paper.HyperplaneFibre` 或直接 `import Mathlib` 才行。
MyProof 侧用的是 `import Mathlib` + `import MyProof.Prelude`，可用。

### 过程自查（发现的问题）

| # | 问题 | 处理 |
|---|---|---|
| 1 | **$\rho$ 重载**：393/394 的 $\dim T_D=\rho-r$ 把 $n-k$ 与 $\rank H$ 混了 | 已引入 $\rho_{\rm amb}=n-k$，改两处公式，并用 $n=8,k=4$ 的两个实例核对（3 与 2）→ [400](../../decision_algorithms/attempts/400_rho_overload_fix.md) |
| 2 | **$c=2$ 纤维公式写反**（$D\subseteq V$ 与 $D\perp V$ 矛盾） | 专家 107 号指出；已改成 full 与 $K$-split 两个正确公式 → [392](392_expert107_audit.md) |
| 3 | **共轭对贡献孤立 2-平面**只在复特征空间一维时成立 | 已在 393 加前提与"重数 $>1$ 时是正维族"的说明 |
| 4 | **gcd 次数不是层内不变量**（1 与 2 都出现） | 已记为方法论要点：图卡判定只需**正性** → [402](../../decision_algorithms/attempts/402_two_strata_decide.md) |
| 5 | 397 的 $c=1$ 侧：4 个 3 阶子式里只有 2 个非零 ⟹ 铅笔秩在整族上 $<3$，不可行更强 | 结论不变（不可行），已在该卷宗写明用的是 gcd |
| 6 | 400/401 的采样只覆盖部分层（$r=2$ 或 $r=0,1$ 各一层） | 已明确标注"只覆盖哪层"，未宣称整层结论 |

**未发现的问题**（本轮没能在自查中推翻的）：393 命题 2 的 (i) 与维数部分（已 Lean 化）、
394 的图卡构造、397 的两侧反例数据、398 的统一形式、399 的字典（三例核对）。

## 最终结论

1. $c=2$ 的纤维核心（$V\cap K=D^{\perp_K}$ 与 $\dim V=(k-c)+t$）**已 Lean 化并通过公理审计**；
2. 自查发现 6 个问题，其中 1–4 已修，5–6 是已标注的范围限制；
3. 命题 2 的 (ii)、底几何、推论 4 仍**只有纸面**（明确标注）。

## 放弃原因

- 没有形式化 (ii)（需要 $A_{21}$ 的块分解；`Strata.lean` 已有 `compressionPart`/`normalComp`，
  下一轮可以接上）；
- 没有形式化底几何（需要实 Jordan 型或特征向量分解的一般理论）。

## 残留价值

- **三条已审计的 Lean 声明**，覆盖 $c=2$ 纤维的两个关键断言；
- 一张**过程自查表**（6 条），其中"$\rho$ 重载"与"纤维写反"是两个真实错误；
- 明确了下一步可形式化的对象：命题 2 的 (ii)（用 `Strata.lean` 的块分解）。

## 相关文件

- Lean：`Q1Paper/HyperplaneC2.lean`（WSL `~/WorkSpace/lean4/Q1Paper`，artifact 仓库镜像）
- 登记：[tools/lean/STATEMENT_MAP.md](../../../../tools/lean/STATEMENT_MAP.md)
- 卷宗：[392](392_expert107_audit.md)、[393](393_c2_fibre_and_base.md)、[397](397_layer_nomonotone.md)、[400](../../decision_algorithms/attempts/400_rho_overload_fix.md)
