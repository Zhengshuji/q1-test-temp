# forced-plane 判据的 Lean 内核：行空间判据（专家 60 号 Priority 3）

> 2026-11-08。把 165/172 的
> $$e_b\in\operatorname{rowspace}(\mathrm{Des})\iff e_b(x)=0\ \ \forall x\in\ker\mathrm{Des}$$
> 写成 Lean 并编译通过。状态：**Lean + M3**。

## 目标

形式化 forced-plane 判据的线性代数根据（对偶零化子），使 165/172 的证书有机器检查的基础。

## 设想与理由

$\mathrm{Des}$ 是线性映射 $f:V\to W$；$e_b$ 是 $V$ 上的线性泛函（$V$ 的對偶）。行空间判据就是
$$(\ker f)^{\circ}=\operatorname{range}f^{\mathsf T},$$
即对偶零化子的基本定理。Mathlib 已有 `LinearMap.range_dualMap_eq_dualAnnihilator_ker`。

## 做法

文件：[tools/lean/MyProof/BuvKernel.lean](../../../../trash/lean_removed_2026-11-19/tools/lean/MyProof/BuvKernel.lean)

```lean
theorem mem_range_dualMap_iff {K V W : Type*} [Field K]
    [AddCommGroup V] [Module K V] [AddCommGroup W] [Module K W]
    (f : V →ₗ[K] W) (φ : Module.Dual K V) :
    φ ∈ LinearMap.range f.dualMap ↔ ∀ x : V, f x = 0 → φ x = 0 := by
  rw [LinearMap.range_dualMap_eq_dualAnnihilator_ker, Submodule.mem_dualAnnihilator]
  simp [LinearMap.mem_ker]
```

导入 `Mathlib.LinearAlgebra.Dual.Lemmas`（引理所在模块）。

## 验证

```
EXIT:0
'mem_range_dualMap_iff' depends on axioms: [propext, Classical.choice, Quot.sound]
```
无 `sorryAx`；已在 STATEMENT_MAP §B.26 登记（出处：165/172 + 专家 60 号 §1.1）。

## 进展

* 行空间判据 Lean 化；
* $B_{u,v}$ 的三个内核（核恒等式、秩恒等式、行空间判据）现都在 `BuvKernel.lean` 中；
* 165/172 的 forced 证书有了形式化根据。

## 最终结论

* $e_b\in\operatorname{rowspace}(\mathrm{Des})\iff e_b|_{\ker\mathrm{Des}}=0$ 机器检查通过；
* 结合 165 的“两行都强制 ⇒ $H$ 秩 1 ⇒ 不可行”，seeds 16/21 的结论有 Lean 支撑的判据。

## 放弃原因

* 未把具体的 $3\times4$ 矩阵 $\mathrm{Des}$ 与 $e_b$ 实例化进 Lean（当前是抽象判据）；
* 未 Lean 化 chart 表达式（177 用精确验证）。

## 残留价值

* forced-plane 判据的形式化根据；
* `BuvKernel.lean` 现在是三个内核（核、秩、行空间）的集合。

## 相关文件

* [attempts/165](../../c_stratification/attempts/165_c2_forced_plane_criterion.md)（判据）
* [attempts/172](172_forced_certificates.md)（证书）
* [tools/lean/MyProof/BuvKernel.lean](../../../../trash/lean_removed_2026-11-19/tools/lean/MyProof/BuvKernel.lean)

## 状态

* 数学 M：M3（专家 60 号 §1.1 确认）。
* 形式 F：F3。
* 导出 L：**L4**。
