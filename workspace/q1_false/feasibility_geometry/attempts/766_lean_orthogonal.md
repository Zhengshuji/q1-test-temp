# 766 Lean：$({\star})$ 的抽象子空间部分

> 2026-11-28。把 753 的 $({\star})$ 中“纯子空间/正交补”的部分形式化：正交补对并的恒等式与维数公式。
> 状态：**[Lean]**（抽象部分）；完整 $({\star})$ 仍缺“$\operatorname{row}A^{\perp}=\ker A$”的矩阵-伴随识别。

## 文件与声明

`MyProof/Q1OrthSpace.lean`（已入构建图）：

```lean
theorem q1_orthogonal_sup (U T : Submodule 𝕜 E) : (U ⊔ T)ᗮ = Uᗮ ⊓ Tᗮ

theorem q1_finrank_sup (U T : Submodule 𝕜 E) :
    finrank 𝕜 ↥(U ⊔ T) = finrank 𝕜 E - finrank 𝕜 ↥(Uᗮ ⊓ Tᗮ)
```

（$\Bbbk$ 为 $\mathbb R$ 或 $\mathbb C$，$E$ 有限维内积空间；$(-)ᗮ$ 为 `Submodule.orthogonal`。）

## 证明

- `q1_orthogonal_sup`：$x\perp(U+T)\iff x\perp U\land x\perp T$（用 `mem_sup` 分解 $y=u+t$ 与 `inner_add_left`）；
- `q1_finrank_sup`：由 `Submodule.finrank_add_finrank_orthogonal (U⊔T)` 与上式，`omega` 收尾。

## 验证

| 项 | 结果 |
|---|---|
| 注册（`in_build.txt`、`blocks.tsv`） | 完成 |
| `lake build MyProof` | **BUILD=0（9120 jobs）** |
| `lake build MyProof.Q1OrthSpace` | B=0 |
| `#print axioms` 两条 | `[propext, Classical.choice, Quot.sound]`，无 sorryAx |

## 覆盖范围与缺口

$({\star})$ 的完整陈述是
$$\dim(\operatorname{row}A+T)=k-\dim(\ker A\cap T^{\perp}),$$
还差一步：
$$(\operatorname{row}A)^{\perp}=\ker A .$$
这需要把 $\operatorname{row}A$ 识别为伴随映射的像（`Aᴴ` 的 range），再用“像的正交补 = 核”的标准结论。Mathlib 中对应的名称不是 `LinearMap.orthogonal_range_adjoint`（不存在），需要另行查找或构造；这一步**尚未 Lean 化**。

因此：
- **已 Lean**：$(U\sqcup T)^{\perp}=U^{\perp}\cap T^{\perp}$ 与维数公式（任意有限维内积空间）；
- **未 Lean**：$\operatorname{row}A^{\perp}=\ker A$ 与完整 $({\star})$。

## 与 762 的组合

762 已 Lean 化 $({\star\star})\ \operatorname{row}(HA)\subseteq\operatorname{row}A$；766 给出 $({\star})$ 的子空间部分。两者合起来覆盖了 753 维数论证的骨架，但“行空间 = 伴随像”的桥接仍是纸面。

## 下一步

1. 找到/构造 `range Aᴴ` 的正交补 = `ker A` 的 Lean 证明（矩阵伴随 API）；
2. 完成后把 753 的“749 ⇒ 695 失败”整条 Lean 化；
3. 再回到 B 的多项式 Bézout 形式化。

## 状态

- 766：**[Lean]**（抽象部分）；
- 完整 $({\star})$：**[待补桥接]**；
- 完整 753：**[已证-纸面]**。
