# 落实专家 2026-11-04 的评审：他独立导出同一基础定理 + 四条可执行建议

## 目标

专家对（较早一版）报告给了长篇评审。其中有四条对我们**当前**工作直接可用：

1. 他**独立导出**了 $(5a)\Rightarrow\bigl[(5b)\text{ 失败}\iff\exists x\in V,\lambda:\ x\notin\mathcal Z,\ (\lambda I-A)x\in\mathcal Z\bigr]$，
   并建议把它作为谱侧论证的**基础定理**；
2. 他提醒：**不能**把"压缩满列秩"的**否定**当成失败（还需 $P_{\mathcal Z}B_Vu\ne0$）；
3. 他给出**术语建议**（dimension obstruction / spectral obstruction / uniform dimension criterion /
   projective occlusion criterion）；
4. 他把"Grassmannian 参数化不完整"列为**最高风险**（Risk 1），要求任何枚举报告说明图卡是否覆盖。

## 设想与理由

* 第 1 条：我们的 **B.13c** 就是这条定理（早已证明）。⟹ 记录"专家独立导出"作为交叉确认。
* 第 2 条：我们的 **B.14**（(T*) 可解类）只用了充分性，正好符合他的提醒；但文档里应把"否定不蕴含失败"写明。
* 第 3 条：把中英术语对齐写进术语表，便于后续沟通。
* 第 4 条：我们用的正是 $\binom{k}{d}$ 个**标准坐标图卡**，它们**覆盖整个** $\operatorname{Gr}(d,K)$，
  且符号计算在 $\mathbb Q(\theta)[\lambda]$ 上（**不采样**）⟹ 两个整族反例的证明是**完备**的（不是网格搜索）。
  这条必须写进证明文档，否则读者会以为是采样。

## 做法

1. `docs/02` B.13c 增"注 (0)"：专家独立导出 + 他的原话 + 指向 B.14 的提醒；
2. `docs/02` B.14 增注："(T*) 只用于充分性；其否定不蕴含失败（$u$ 可能落在 $\ker(P_{\mathcal Z}B_V)$ 里）"；
3. 两个反例的证明文档（proof/type3_second_example/ 与 proof/refuted/C4_type3_counterexample.md）末尾加**覆盖完备性**段：
   $\binom{k}{d}$ 个标准图卡覆盖 $\operatorname{Gr}(d,K)$；符号计算不采样；再取 $(5a)$ 可容许子集；
4. `docs/06` 术语表加中英映射（Type I ↔ dimension obstruction 等）。

## 进展

四项全部落地（见上）。其中第 3 项实际上**加强**了两个反例的结论：此前文档只写"逐图卡符号 gcd"，
未说明图卡并覆盖全 Grassmannian；补上后，C4 与新实例的"整族"结论不再有"参数化不完整"的疑点。

## 最终结论

1. **B.13c = 专家建议的基础定理**，已证（L1）+ 6 个显式证书（L2）；他的独立导出是交叉确认；
2. **(T*) 的否命题不成立**这一点已在文档中显式化（B.14 注）；
3. **两个整族反例的证明现在是完备的**（图卡覆盖 + 符号计算），可直接回应 Risk 1；
4. 术语已对齐。

## 放弃原因

不适用。

## 残留价值

* 一条可引用的"基础定理"表述（B.13c）与专家背书；
* 覆盖完备性的标准论证段（可复用到任何"逐图卡"证明）；
* 中英术语映射，减少后续沟通成本。

## 相关文件

- `docs/02` B.13c、B.14
- `proof/type3_second_example/README.md`、`proof/refuted/C4_type3_counterexample.md`（覆盖完备性段）
- `docs/06_glossary.md`（术语映射）
- 专家答复：`workspace/for_expert/archive/14_proofs_and_direction-answer.md`
