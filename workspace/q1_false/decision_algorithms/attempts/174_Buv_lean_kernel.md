# $B_{u,v}$ 秩恒等式的 Lean 内核（专家 60 号形式化顺序第 1–2 步）

> 2026-11-08。把专家 60 号 §4.1 的
> $$\ker\varphi_U=U\cap A^{-1}U,\qquad \operatorname{rank}\varphi_U=u-\dim(U\cap A^{-1}U)$$
> 写成 Lean 内核并编译通过。状态：**Lean（内核）+ 专家确认**。

## 目标

形式化 $B_{u,v}$ 的核恒等式与秩恒等式（有限维线性代数），作为 chart/Bézout 界的起点。

## 设想与理由

专家 60 号建议的形式化顺序：先证 $\ker\varphi_U=U\cap A^{-1}U$、$\operatorname{rank}\varphi_U=u-\dim$，
再证 chart 表达式 $F_A(X)$ 与其次数。前两步是纯线性代数，适合 Lean。

## 做法

文件：[tools/lean/MyProof/BuvKernel.lean](../../../../trash/lean_removed_2026-11-19/tools/lean/MyProof/BuvKernel.lean)（WSL 树同名文件已编译）。

两条声明：
```lean
theorem ker_mkQ_comp_domRestrict (A : E →ₗ[K] E) (U : Submodule K E) :
    LinearMap.ker (U.mkQ.comp (A.domRestrict U)) =
      Submodule.comap U.subtype (U ⊓ Submodule.comap A U)

theorem finrank_range_mkQ_comp_domRestrict [FiniteDimensional K E]
    (A : E →ₗ[K] E) (U : Submodule K E) :
    Module.finrank K (LinearMap.range (U.mkQ.comp (A.domRestrict U))) =
      Module.finrank K U - Module.finrank K ↥(U ⊓ Submodule.comap A U)
```

证明：
1. 核恒等式：`ext x; simp` 后用 `Submodule.mem_comap`/`mem_inf` 拆开；
2. 秩恒等式：秩-零化度 `LinearMap.finrank_range_add_finrank_ker`，
   `Submodule.comapSubtypeEquivOfLe` 把 $\operatorname{comap}$ 的维数换成 $U\cap A^{-1}U$ 的维数，`omega` 收尾。

## 验证

WSL：
```
lake env lean MyProof/BuvKernel.lean
EXIT:0
'ker_mkQ_comp_domRestrict' depends on axioms: [propext, Classical.choice, Quot.sound]
'finrank_range_mkQ_comp_domRestrict' depends on axioms: [propext, Classical.choice, Quot.sound]
```
无 `sorryAx`；`audit_lean_statements` 0 问题（两条已登记 STATEMENT_MAP §B.26）。

## 进展

* 两条秩恒等式已 Lean 化；
* 声明已登记（出处：171 + 专家 60 号 §4.1）；
* 这是专家形式化顺序的第 1–2 步。

## 最终结论

* $\ker\varphi_U=U\cap A^{-1}U$ 与 $\dim\operatorname{range}\varphi=u-\dim(U\cap A^{-1}U)$ 机器检查通过；
* 下一步是 chart 表达式 $F_A(X)$ 与二次性（专家顺序第 3–4 步）。

## 放弃原因

* 未进入聚合 `MyProof.lean` 的 import 图（单文件编译；整图编译需另加聚合）；
* chart 表达式/次数未形式化；
* Bézout 界未形式化（专家建议引用）。

## 残留价值

* $B_{u,v}$ 理论的第一块 Lean 内核；
* 可复用的 quotient/comap 维数技巧。

## 相关文件

* [attempts/171](../../c_stratification/attempts/171_Buv_rank_strata.md)（$B_{u,v}$ 理论）
* [tools/lean/MyProof/BuvKernel.lean](../../../../trash/lean_removed_2026-11-19/tools/lean/MyProof/BuvKernel.lean)
* [tools/lean/STATEMENT_MAP.md](../../../../tools/lean/STATEMENT_MAP.md) §B.26

## 状态

* 数学 M：M3（专家 60 号确认的恒等式）。
* 形式 F：F3（字面陈述形式化）。
* 导出 L：**L4**。
