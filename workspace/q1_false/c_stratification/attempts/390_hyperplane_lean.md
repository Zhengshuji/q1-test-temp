# 390 Lean：超平面层论文的方向定理与预设行引理（已形式化）

## 目标

把论文里**可以形式化的部分**做完：Theorem 3（方向定理）与 Lemma 4（预设行），
并入 WSL 的 `~/WorkSpace/lean4/Q1Paper`（论文 artifact 库的工作源），并把镜像同步到 GitHub 仓库
`q1-functional-observer`。

## 设想与理由

论文里只有两条结果是**纯内积空间线性代数**，不涉及矩阵、维数或坐标：

1. **方向定理**：层内两个泛函 $u\mapsto\langle u,v\rangle$、$u\mapsto\langle u,Av\rangle$ 成比例
   $\iff$ 压缩把 $v$ 送到 $v$ 的倍数。证明只用"$Av=w+z$、$w\in K$、$z\in K^\perp$、$K\cap K^\perp=0$"。
2. **引理 4**：预设行消去 $v$ 与 $Av$ $\Longrightarrow$ $V_0\subseteq\operatorname{span}\{v,Av\}^\perp$
   （自动、且对方向一致）；以及 $V_0\cap(K_0\cap U_v^\perp)=V_0\cap K_0$（$\delta$ 与方向无关）。

其余结果（相对 Graßmann 丛参数化、满秩首项系数引理、图卡覆盖、位复杂度）都需要
相对丛/多项式次数/位模型，Mathlib 没有对应对象或代价过高，**明确不形式化**。

## 做法

新建两个模块（`namespace Q1Paper`，与姊妹稿模块同风格）：

- `Q1Paper/HyperplaneDirection.lean`
   - `innerLeft (v) : E →ₗ[ℝ] ℝ`：$u\mapsto\langle u,v\rangle$；
   - `compression_eq_of_proportional`：$Av=w+z$、$w\in K$、$z\in K^\perp$、泛函成比例 $\Rightarrow$ $w=\mu v$；
   - `proportional_of_compression`：反向；
   - `direction_iff`：两者等价（论文 Theorem 3）。
- `Q1Paper/HyperplanePrescribed.lean`
   - `le_orthogonal_span_pair`：行消去 $v,Av$ $\Rightarrow$ $V_0\le\operatorname{span}\{v,Av\}^\perp$（用 `span_induction`）；
   - `inf_inf_orthogonal_eq`：$V_0\le U^\perp$ $\Rightarrow$ $V_0\sqcap(K\sqcap U^\perp)=V_0\sqcap K$（论文 Lemma 4 的 $\delta$ 无关性）。

然后：把两模块加进 `Q1Paper.lean` 聚合文件与 `Q1Paper/Audit.lean` 的 `#print axioms` 列表，
跑 `bash scripts/check.sh`（`lake build` + 审计），最后把四个文件逐字节同步到 artifact 仓库。

## 进展

- `lake build Q1Paper` + `lake env lean Q1Paper/Audit.lean`：**exit=0**；
- 五条新声明的公理输出都只有 `propext`、`Classical.choice`、`Quot.sound`；
- artifact 仓库（`q1-functional-observer`）已提交 `111ec65`：两个模块 + 聚合/审计文件 + 论文 tex/pdf，
  `README` 证据表与 `paper/LEAN_MAP.md` 的 F 节已登记；
- 与 WSL 源逐字节一致（哈希核对 4 个文件）。

踩到的坑（都记下来避免重犯）：
1. `⟪x, y⟫` 记号未开 scope ⟹ "expected token"；改用 `inner ℝ x y` 即可；
2. `LinearMap.ker (innerSL ℝ v)` 在 `Submodule.map K.subtype` 上下文里类型不匹配（`.map` 要子模的**定义域**是 K）；
3. `Submodule.span_induction` 的 `p` 是**依赖**类型 `(x) → x ∈ span → Prop`，参数顺序是 mem/zero/add/smul 之后才是成员证明；
4. PowerShell 的 `Set-Content -Encoding utf8` 可能带 BOM ⟹ Lean 报 `expected token`；`.lean` 一律用 `write` 工具写再 `cp`。

## 最终结论

论文中"可以 Lean 的"三部分**已形式化并接入审计**：Theorem 3（方向定理）、Lemma 4（预设行）、
Lemma 2 的数值部分（$\dim D_v=k-1$）。其余部分**明确不形式化**（已在 LEAN_MAP 的 F 节写明）。
artifact 仓库现在覆盖三篇 paper 的 Lean + 证据表。

### 补充：第三个模块 `HyperplaneFibre.lean`（Lemma 2 的数值部分）

- `mem_orthogonal_span_pair_iff`：$w\perp\operatorname{span}\{v,Av\}\iff \langle w,v\rangle=\langle w,Av\rangle=0$；
- `Dv_eq_ker`：比例性下 $D_v=K\sqcap\operatorname{span}\{v,Av\}^\perp$ 就是 $\langle\cdot,v\rangle|_K$ 的核；
- `finrank_Dv`：**$\operatorname{finrank}D_v+1=\operatorname{finrank}K$**（即 $k-1$），
  用 `Module.Dual.finrank_ker_add_one_of_ne_zero` 加 `Submodule.equivMapOfInjective` 的维数换算。

又踩到两个坑（已记）：
5. `finrank ℝ (K ⊓ Uᗮ)` 会被解析成**类型层的 min**，必须写 `finrank ℝ ↥(K ⊓ Uᗮ)`；
6. `open Module` 是必须的（`finrank` 的记法在 `Module` 命名空间下）；
7. PowerShell 的 `Set-Content`/`-replace` 处理含 Unicode 的 `.lean` 会毁文件——一律用 `edit`/`write`。

## 放弃原因

- ~~Lemma 2 的数值部分（$\dim D_v=k-1$）~~：**已完成**（`HyperplaneFibre.lean`，见上）。
- 满秩首项系数引理、图卡覆盖、位复杂度：需要相对丛/多项式次数/位模型，Mathlib 无对应对象。

## 残留价值

- **5 条 `[Lean]` 声明**（已登记 STATEMENT_MAP），论文 Theorem 3 与 Lemma 4 有了机器检查；
- 两个模块可直接被后续工作复用（`innerLeft` 就是把 $v$ 变成泛函的构造）；
- 记录了四个具体的 Lean/Mathlib 坑。

## 相关文件

- WSL：`~/WorkSpace/lean4/Q1Paper/Q1Paper/HyperplaneDirection.lean`、`HyperplanePrescribed.lean`
- artifact 仓库：`q1-functional-observer`（`Q1Paper/`、`paper/hyperplane_layer.tex`、`paper/LEAN_MAP.md`）
- 论文：[paper/hyperplane/hyperplane_layer.tex](../../../../archive/paper_drafts/paper_III_workspace_2026-11/hyperplane/hyperplane_layer.tex)
- 登记：[tools/lean/STATEMENT_MAP.md](../../../../tools/lean/STATEMENT_MAP.md)
