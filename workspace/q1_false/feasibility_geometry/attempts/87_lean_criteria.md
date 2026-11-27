# 三条核心判据补 Lean：`Criterion.lean`（B.16b、B.17、B.13c 的内核）

## 目标

按用户要求把可 Lean 的核心判据补成 Lean。选中的三条（原因码 (α) 的桥 `RowSpace.lean` 已建好，
故它们只剩纯线性代数）：**B.16b**、**B.17**、**B.13c**。

## 设想与理由

三条的实质都是线性映射/子空间层面的**抽象**命题，不需要矩阵、多项式或代数几何：

* B.16b：$(5a)$ 的行空间形式（存在线性 `T` 使 `L ∘ A = T ∘ (L, CA, C)`）⟹ $A(V\cap\mathcal Z)\subseteq\mathcal Z$；
* B.17：$S\subseteq\ker J\cap\ker T$ ⟹ $S\subseteq\ker(T-cJ)$（永久核）；判据的核形式；
* B.13c：$F\circ A=\Lambda\circ F$ ⟹ $F\circ(cI-A)=(cI-\Lambda)\circ F$。

## 做法

新文件 `tools/lean/MyProof/Criterion.lean`，四条声明：
`b16b_mapsTo`、`permanent_kernel`、`ker_eq_iff`、`b13c_factor`。
迭代过程（记录）：`stack` 的定义要用显式 `toFun`（`LinearMap.prod` 的 `Function.prod` 形式无法直接 `rw`）；
`hxCA` 需先 `simp only [LinearMap.comp_apply]` 才能重写；`T (0,(0,0))` 要显式给 `h0 : ((0:Y₂),(0:Y₁),(0:Y₁)) = 0`（`rfl`）再 `map_zero`。

## 进展

| 项 | 结果 |
|---|---|
| `Criterion.lean` | **编译 exit=0，0 error 0 warning**（4 条声明）|
| `STATEMENT_MAP` | 已登记 4 条（含对应/差异），**170 声明 / 159 条目 / 0 问题** |
| `docs/02` | B.16b、B.17、B.13c 均已加 `[Lean 内核]` 并写明差异 |
| `lean_coverage` | B.16b/B.17/B.13c 三行改为 ✓ [Lean 内核]，**0 不一致** |

差异（写在每处）：抽象映射层面；矩阵实例化与"行堆叠秩 ↔ 行空间包含"由 `RowSpace` 提供；
B.17 的"诱导映射 $W/S\to W$ 单射"商空间表述未形式化（等价于已证的核形式）；
B.13c 只形式化了因子化恒等式，$x\notin\mathcal Z\iff\mathcal Lx\ne0$ 的组装仍是纸面。

## 最终结论

1. 三条判据现在都有 **Lean 内核**（`Criterion.lean`，exit=0）；
2. 覆盖率从 19/57 完整 + 8 部分 + 30 无 ⟹ **19 完整 + 11 部分 + 27 无**；
3. 仍然无 Lean 的主要是 (β)/(γ)/(δ) 类：B.8/B.9/B.10（多项式矩阵/Smith）、B.12（PBH）、
   B.13d（$\varepsilon=0$ 三情形）、B.16/B.18*（已部分 Lean 或纯记账）。

## 放弃原因

不适用。

## 残留价值

* 一个可复用的 `Criterion.lean`（后续"核 = S"、"永久核"类命题可直接引用）；
* 三条主判据的 Lean 内核 + 明确的差异说明；
* 迭代中记下的三个 Lean 技巧（显式 `toFun`、`comp_apply` 先展开、零元组用 `rfl` 桥）。

## 相关文件

- `tools/lean/MyProof/Criterion.lean`
- `tools/lean/STATEMENT_MAP.md`、`proof/lean_coverage.md`、`docs/02` B.16b/B.17/B.13c

## 续（同一轮）：`Dims.lean`——记账型三条

新增 `tools/lean/MyProof/Dims.lean`（**exit=0，0 error 0 warning**），三条声明：

| 声明 | 对应 |
|---|---|
| `b11c_modular` | B.11c 的模格恒等式 $C_0\le S\Rightarrow C_0\sqcup(R\sqcap S)=(C_0\sqcup R)\sqcap S$ |
| `b11c_add` | B.11c 的维数相加（$\dim(C_0\sqcup(R\sqcap S))=\dim C_0+\dim(R\sqcap S)$，当交为零）|
| `b18c_annihilate` | B.18c 第 1 条：$Cx=0,C(Ax)=0\Rightarrow C((cI-A)x)=0$ |

踩坑记录：`finrank Φ (p ⊔ q)` 会被当成"类型上的 `⊔`"（报 `Min (Type)`）——**必须写 `finrank Φ ↥(p ⊔ q)`**；
`c • LinearMap.id` 需标注 `(LinearMap.id : X →ₗ[Φ] X)`；`sup_inf_assoc_of_le` 给出的是反向等式，需 `.symm`；
`[FiniteDimensional]` 只放在 `b11c_add`（否则 `b11c_modular`/`b18c_annihilate` 报 unused variable 警告）。

覆盖率（三条新标的）：**25 完整 + 15 部分 + 17 无**（其中 B.11c、B.18c、B.18d 归入部分）。

## 续（同轮）：`Logic.lean`——两条归约型命题的逻辑骨架

新增 `tools/lean/MyProof/Logic.lean`（**exit=0，0 error 0 warning**），三条声明：

| 声明 | 对应 | 差异 |
|---|---|---|
| `typeI_kills` | Type I（$h>q+r_1$）杀掉 $(5b)$ 的算术内核 | 只做算术；秩不等式是纸面 |
| `b11d_css` | B.11d 的 CSS 归约 | 纯逻辑骨架，两条前提作为假设 |
| `b18e_family` | B.18e 的整族不可行结论 | 纯逻辑骨架；三件数学内容作为假设 |

踩坑：`Classical.arbitrary` 需要 `[Nonempty σ]`；未用的假设会触发 unused-variable 警告（已删 `hnotV`）。

覆盖率：**25 完整 + 16 部分 + 16 无**（B.11d 归入部分）。
