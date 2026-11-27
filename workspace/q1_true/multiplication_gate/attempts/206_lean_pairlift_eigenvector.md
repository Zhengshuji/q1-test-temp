# Lean 内核：pair-lift 与不变子空间特征向量（201/205）

> 2026-11-09。把可 Lean 化的两步写成内核并编译通过：
> `pairLift_annihilator`（201 的核心）与 `invariant_subspace_has_eigenvector`（205 的关键一步）。
> 状态：**Lean（两条引理）；205 的整体秩论证仍为纸面**。

## 目标

按“能 Lean 的就 Lean，不能的纸面交专家”的原则，形式化 201/205 的线性代数内核。

## 设想与理由

- 201 的 $\mathcal L_V=(V+AV)^\perp$ 是子空间零化子的 sup 恒等式，Mathlib 有 `dualAnnihilator_sup_eq`；
- 205 的关键一步是“非零不变子空间含特征向量”，用 `Module.End.exists_eigenvalue` 在限制映射上取特征向量。

## 做法

文件：[tools/lean/MyProof/InvarianceKernel.lean](../../../../trash/lean_removed_2026-11-19/tools/lean/MyProof/InvarianceKernel.lean)

```lean
theorem pairLift_annihilator (A : V →ₗ[K] V) (V₀ : Submodule K V) :
    (V₀ ⊔ V₀.map A).dualAnnihilator =
      V₀.dualAnnihilator ⊓ (V₀.map A).dualAnnihilator

theorem invariant_subspace_has_eigenvector
    [IsAlgClosed K] [FiniteDimensional K V]
    (A : Module.End K V) (W : Submodule K V) (hW : W ≠ ⊥)
    (hA : ∀ x ∈ W, A x ∈ W) :
    ∃ μ : K, ∃ x : V, x ∈ W ∧ x ≠ 0 ∧ A x = μ • x
```

证明：
1. `pairLift_annihilator` 直接 `rw [Submodule.dualAnnihilator_sup_eq]`；
2. `invariant_subspace_has_eigenvector` 把 $A$ 限制为 $W$ 的自同态（`codRestrict`），
   用 `Module.End.exists_eigenvalue` 取 $\mu$，从非零特征空间取 $x$。

## 验证

```
EXIT:0
'pairLift_annihilator' depends on axioms: [propext, Classical.choice, Quot.sound]
'invariant_subspace_has_eigenvector' depends on axioms: [propext, Classical.choice, Quot.sound]
```
无 `sorryAx`；STATEMENT_MAP §B.27 已登记（300 声明/223 条目一致）。

## 未 Lean 化的部分（纸面，交专家）

- 205 的整体链：$\operatorname{row}H=V^\perp$、取 $y$ 使 $yH=l$、$yP(\lambda)=0$、$\operatorname{rank}P<\omega$。
  这些涉及行空间/秩/矩阵表示的显式翻译，工作量大；当前以纸面证明 + 专家审核。
- 203 的 $\omega\le k-\dim(V+AV)$ 维数论证（纸面）。

## 进展

* 两条 Lean 引理完成；
* 205 的关键代数步骤有机器检查；
* 整体定理仍纸面。

## 最终结论

* 201 的核心恒等式、205 的关键引理：**Lean（L4）**；
* 205 整体：**纸面（M2），请专家审核**。

## 放弃原因

* 未形式化行空间/秩的完整链；
* 未形式化 203 的维数论证。

## 残留价值

* 两个可复用的内核；
* 为专家审核提供机器检查的支撑。

## 相关文件

* [attempts/201](201_pair_lift_theorem.md)、[attempts/205](205_AinvK0_impossible.md)
* [tools/lean/MyProof/InvarianceKernel.lean](../../../../trash/lean_removed_2026-11-19/tools/lean/MyProof/InvarianceKernel.lean)
* [tools/lean/STATEMENT_MAP.md](../../../../tools/lean/STATEMENT_MAP.md) §B.27

## 状态

* 数学 M：M3（专家确认的线性代数事实）。
* 形式 F：F3（两条引理字面形式化）。
* 导出 L：**L4**（引理级）。
