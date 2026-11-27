# 342 专家 97 号审计：两条承重结论被限定到"满行空间"；定理包与下一步

> 送审件 [97](../../../for_expert/archive/97_hyperplane_audit_request.md)（已归档），
> 答复 [97-reply](../../../for_expert/archive/97_hyperplane_audit_request-reply.md)。
> 这是一次**审计**：他逐条核了 11 个证明。结论：**多数成立，但两条承重的要加假设**，
> 且 Claim 1 的分量分解**没证成**。

## 目标

1. 记录 11 条断言的逐条裁决。
2. 落实四处更正（Claim 1、4、5、6 的假设）。
3. 记录他给的**修订定理包**（A/B/C/D）与下一步。

## 设想与理由

97 号是**审计**而不是建议：我把 11 条断言连同证明递过去，请他逐条判"成立 / 有缺口 / 需额外假设"。
最好的预期是"都成立"，最坏的预期是"承重的那条错了"。实际结果是中间：**多数成立，两条要加假设，一条（Claim 1）没证成**。

## 做法

逐条读裁决、把每条映射到它影响的卷宗，按"哪条承重"决定改哪些文件：
Claim 1（分量）→ 324；Claim 4/5（商铅笔/秩界）→ 328/329；Claim 6（$p=1$ 定理）→ 338；
Claim 7/8（零频）→ 337（补 $v\notin AK_0$ 情形）；Claim 9（反例）→ 336（升为 Prop D）。

## 进展

- 四处更正已写进源卷宗（324 降级、328/329 加前提、338 改陈述、337 补情形）；
- 修订定理包（A/B/C/D）与"特征纤维的两级判据"已记录；
- STATUS / ROADMAP / ATTEMPTS 已同步；97 号问答成对归档。

## 裁决总表

| # | 断言 | 97 号裁决 |
|---|---|---|
| 1 | 分量 $Z=Z^\circ\cup\bigcup F_\lambda$、$\le1+\delta$ | **计数成立、分解未证**：纤维维数比较**不**证明 $F_\lambda\not\subseteq\overline{Z^\circ}$（极限可与底点同时变化） |
| 2 | 坏集闭（射影 + 紧合） | **正确**（$Y$ 开也对；闭性是相对于 $Y$） |
| 3 | generic-gcd 判据 | **正确**（复几何意义），但要加有理点的限定 |
| 4 | 商铅笔 | **只在满行空间下成立**；$\operatorname{rank}(QN)=k-1$ 来自 $V=U^\perp$，**不**来自 $V\subseteq U^\perp$ |
| 5 | 秩界 $n-2-p$ | 对**辅助铅笔** $Q(\lambda I-A)N$ 正确；对观测器铅笔需 $V=U^\perp$ |
| 6 | $p=1$ ⟹ 非特征恒坏 | **只在 $p=1,q=n-2,r_0=0$ 成立**（此时 $V=U^\perp$ 被迫）；任意 $q$ 未证 |
| 7 | $\lambda=0$ 障碍 | **正确**（恒等式逐项核过，无需额外假设） |
| 8 | 推论 $\dim(AK_0)\ge k$ | **正确**；$v\notin AK_0$ 时正确的必要条件回到恒等式本身（$\dim(AK_0)\ge\omega$ 只必要不充分） |
| 9 | 反例（纤维充分性假） | **成立**，建议升为命题 |
| 10 | 移动根 / 固定根 $-2$ | **证据**；正确对象是函数域上的 generic gcd，固定根检查不是判据 |
| 11 | 富余档可以好 | **未证**：无约束高铅笔的 codimension 论证是标准的，但**结构族是否落在坏铅笔簇内**没证；缺的是"非包含" |

## 四处更正的落实

1. **Claim 1（[324](../../c_stratification/attempts/324_hyperplane_component_theorem.md)）**：把"$Z=Z^\circ\cup\bigcup F_\lambda$ 是分量分解"降级为
   **"计数 $\le1+\delta$ 成立；分解的不可比性未证"**。要补的是：把行空间入射簇与其 Grassmann 层写出来，
   证明极限行空间构成**可容许特征纤维的真闭子集**（Plücker 坐标/incidence 条件），且该族是向量丛（常秩论证）。
2. **Claim 4/5（[328](328_quotient_pencil_theorem.md)、[329](../../c_stratification/attempts/329_forced_relations_quotient_pencil.md)）**：
   把 $V=U^\perp$（等价 $q=n-2$）写成**显式假设**；秩界只对辅助铅笔成立。
3. **Claim 6（[338](../../c_stratification/attempts/338_dimension_map_p1.md)）**：定理改为
   > $p=1$、$q=n-2$、$r_0=0$ 时，超平面层的每个可容许**非特征**点都违反 $(5b)$。
   并注明 $k=1$ 的退化情形（$\omega=0$，论证空转）。
4. **[337](../../c_stratification/attempts/337_lambda0_obstruction.md)**：$\lambda=0$ 命题**无需改**（正确）；把"$v\notin AK_0$ 时的正确条件"
   补上：$\dim(AK_0)-\dim(AK_0\cap V^\perp)=\omega$，$\dim(AK_0)\ge\omega$ 只必要不充分。

## 修订定理包（97 号）

- **Theorem A**：坏集闭 + 分量可行 $\iff$ generic gcd $=1$（复几何）。
- **Theorem B**：$p=1,q=n-2,r_0=0$ 时非特征点全部违反 $(5b)$（**对 $A$ 一致**）。
- **Proposition C**：$\operatorname{rank}H_A=\dim(AK_0)-\dim(AK_0\cap V^\perp)$；$v\in AK_0$ ⟹ $\le\dim(AK_0)-1$；
  $\lambda_0\ne0$ 的特征向量 ⟹ 需 $\dim(AK_0)\ge k$。
- **Proposition D**：Claim 9 的反例——$K_0$ 含特征向量、整条特征纤维不可行。

## 特征纤维的正确判据（97 号 §13）

两级：
1. **零频秩**：$\dim(AK_0)-\dim(AK_0\cap V^\perp)=k-1$（对 $V$ 的线性代数条件，可作**预处理**）；
2. **公共根**：在满足 1 的层上，$\gcd_I m_I=1$ 在 $\overline{\mathbb Q(Y)}[\lambda]$ 中。

于是"特征纤维问题"变成：**找出满足零频条件的行空间层 → 看哪一层的 generic gcd 为 1 → 有理点**。

## 下一步（97 号 §14，按其优先级）

1. **修 Claim 1**（分量分解）——要用它才能做逐分量判据；
2. **把 Theorem B 立起来**（干净、对 $A$ 一致）；
3. **把 Claim 9 升为命题**；
4. **把 Claim 7 当预处理**：每个特征纤维先算 $\dim(AK_0)-\dim(AK_0\cap V^\perp)$，不满足直接丢弃；
5. Claim 11 走"结构化系数映射"（$\Phi_v:U^\perp\to\mathbb Q^{1\times k}\times\mathbb Q^{1\times k}$，$r\mapsto(rN,rAN)$），
   要证的是**结构族不落在坏铅笔簇内**（不是"高铅笔生成好"那一半——那是标准的）；
6. 用 **generic gcd 证书**替代采样。

## 最终结论

1. 这条线的承重结论现在是：**Theorem A + Theorem B + Prop C + Prop D**——前两条成立有前提，
   后两条无条件成立。
2. **$c=1$ 的判据仍缺**，但形状明确了：两级（零频 + generic gcd），且第一级是线性代数、可作预处理。
3. 最有价值的一条（97 号自己说的）是 **Claim 9 的反例**：它把"$K_0$ 含特征向量就够"彻底否掉。

## 放弃原因

- 没有补 Claim 1 的不可比性证明；
- 没有做 Claim 11 的非包含论证；
- 没有把 Theorem B 的陈述写进正式卷宗（只在本文件记录）。

## 残留价值

- 一份**逐条裁决**（哪条成立、哪条要加假设、哪条没证）；
- 修订后的定理包与"两级判据"形状；
- 明确的下一步顺序（修 1、立 B、升 9、用 7 作预处理）。

## 相关文件

- 送审件：[97](../../../for_expert/archive/97_hyperplane_audit_request.md)
- 答复：[97-reply](../../../for_expert/archive/97_hyperplane_audit_request-reply.md)
- [324](../../c_stratification/attempts/324_hyperplane_component_theorem.md)（Claim 1，已降级）
- [328](328_quotient_pencil_theorem.md)、[329](../../c_stratification/attempts/329_forced_relations_quotient_pencil.md)（Claim 4/5，加 $q=n-2$）
- [338](../../c_stratification/attempts/338_dimension_map_p1.md)（Claim 6 → Theorem B）
- [337](../../c_stratification/attempts/337_lambda0_obstruction.md)（Prop C，正确）
- [336](../../c_stratification/attempts/336_fibre_sufficiency_counterexample.md)（Prop D，正确）

## 状态

- Theorem A：**已证**（97 号确认）。
- Theorem B：**已证**（限定 $p=1,q=n-2,r_0=0$）。
- Prop C/D：**已证**。
- Claim 1（分量分解）、Claim 11（富余档生成好）：**未证**。

## 专家复核意见（裁决）

| 断言 | 裁决 | 落实 |
|---|---|---|
| 1 分量 | 计数成立、分解未证 | 324 已降级 |
| 2 闭性 | 正确 | — |
| 3 判据 | 正确（复几何） | 加有理点限定 |
| 4/5 商铅笔/秩界 | 仅满行空间 | 328/329 加 $q=n-2$ |
| 6 $p=1$ 定理 | 仅在 $q=n-2$ | 338 改陈述 |
| 7/8 零频障碍 | 正确 | 337 补 $v\notin AK_0$ 情形 |
| 9 反例 | 成立 | 升为 Prop D |
| 10 固定/移动根 | 证据 | 用 generic gcd 证书 |
| 11 富余档 | 未证（缺非包含） | 记入下一步 |
