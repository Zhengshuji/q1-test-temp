# Lean 4 备份（P 的递归定理）

> **2026-11-01 起的目录约定**：
> - `tools/lean/MyProof/` —— **共享/工具类** Lean（`Prelude` 公共引理、早期定理）；
> - `proof/<claim>/lean/MyProof/` —— **按命题归档**的 Lean（一命题一目录，见 `proof/5b_upper_bound/` 的样例）。
>   已迁：`quotient_equivalence`（H.1）、`d0_boundary`（H.3）；其余陆续迁。
> `check_lean.sh` 把**两处**都收进 WSL 工程再编译；WSL 的 `~/WorkSpace/lean4/MyProof` 才是真 lake 工程，
> Windows 侧是留档 + git。

## 环境

| 项 | 值 |
|---|---|
| 位置（WSL）| `/home/zsj/WorkSpace/lean4/MyProof` |
| 工具链 | `leanprover/lean4:v4.35.0` + Mathlib（预构建，约 7.1 GB olean）|
| 单文件编译 | `cd ~/WorkSpace/lean4/MyProof && export PATH="$HOME/.elan/bin:$PATH" && lake env lean MyProof/PRecursion.lean` |
| 模块构建 | `lake build MyProof.PRecursion` |

本目录是 Windows 侧备份，与 WSL 工程 `MyProof/PRecursion.lean` **逐字节一致**（8271 字节）。
按项目纪律 #7：Lean 文件用 `write` 工具写。


## 常见坑（2026-11-01 记录）

| 症状 | 原因 | 修法 |
|---|---|---|
| `Module.End.exists_eigenvalue` 报 `Module.End ?m ?m` 类型不匹配 | 在**子类型**（如 `↥(U.dualAnnihilator)`）上用，实例路径（`Submodule.addCommMonoid` vs `AddCommGroup.toAddCommMonoid`）不同 | 写一个**泛型**辅助引理 `(B : V →ₗ[K] V)`（V 任意），在 `V := 子类型` 处实例化；并给 `(K := ...) (V := ...)` |
| `rw [← LinearMap.mem_ker]` 在 `φ ∈ ker f` 上失败 | 目标里 `ker` 带 coercion，重写模式不匹配 | 用 `LinearMap.mem_ker.mpr : f φ = 0 → φ ∈ ker f` 显式构造 |
| `Submodule.mem_dualAnnihilator.mpr` 报 unknown constant | 对带参数的定理不能直接点 `mpr` | 写成 `(Submodule.mem_dualAnnihilator φ).mpr ...` |
| `Submodule.finrank_lt_finrank_of_lt` 给出 `finrank ⊤` 而非 `finrank E` | 该引理的右端是 `⊤` | `simpa using ...` |
| `Submodule.mem_sup.mp` 解构后 `rw` 报 typeclass stuck（`Module ?m ?m`） | 环境里的 `⊔` 类型未定 | 先给命题写全类型（`show x ∈ (⊤ : Submodule K E)`），或把 `mem_sup` 用在已定型的三元组上 |
| `rw [← htop] at *` 把无关目标也改掉 | `at *` 过度 | 只对需要的假设 `rw [...] at hx` |
| 成员构造写成一长串 `|>` | 类型推断丢信息 | 拆成 `have` 逐条写 |

## 机器验证的内容（40 个文件，`check_lean.sh` 全部退出码 0）

> **共享引理**：[`Prelude.lean`](../../trash/lean_removed_2026-11-19/tools/lean/MyProof/Prelude.lean)——`finrank_inter_add_finrank_map_mkQ`、
> `finrank_map_add_finrank_inf_ker`、`finrank_pos_of_ne_bot`。其余文件 `import MyProof.Prelude`，
> 本地只留一行别名（证明只有一份）。`check_lean.sh` 先用 `lake build MyProof.Prelude` 生成 `.olean`。

> **陈述一致性**：每个声明的"对应命题 + 差异"登记在 [STATEMENT_MAP.md](STATEMENT_MAP.md)，
> 由 `python tools/hygiene/audit_lean_statements.py` 机械检查（73 个声明 / 54 条登记 / 0 问题）。
> **写 `[Lean]` 必须带这里的声明名**（CLAUDE §4 硬规则 6）。

| 定理 | 内容 |
|---|---|
| `comapSubtypeEquiv` | 线性等价 `comap U.subtype M ≃ U ⊓ M` |
| `finrank_map_mkQ_add` | `dim (π U) + dim M = dim (U ⊔ M)` |
| `dim_lower_quotient` | **递归 $({\ge})$ 一半**：`T ≤ U`、`T ≤ M` ⟹ `dim T + dim (π U) ≤ dim U` |
| `bot_admissible` | `T = ⊥` 时 `U = ⊥` 可行（递归基）|
| `induced` | **level-1 映射良定义**：`Φ' = induced Φ M` |
| `admissible_image` | **可行性下降**：可行 `U` 的像在商实例中可行 |
| `exists_section` | 商的线性截面存在（`mkQ M ∘ s = id`）|
| `section_image` | 提升副本 `s '' U'` 满足 `π (s '' U') = U'` 且 `s '' U' ⊓ M = ⊥` |
| **`lift_admissible`**（`PRecursionLift.lean`）| **$({\le})$ 的构造步**：给定 $\sigma$，$U=T\sqcup(s+\sigma)''U'$ 可行且 $\dim U=\dim T+\dim U'$ |
| **`exists_lift_of_range_le`**（`PRecursionSigma.lean`）| **$\sigma$ 存在性的可复用核心**：若 $\operatorname{range}g\le\operatorname{range}\psi$，则 $g$ 沿 $\psi$ 提升为线性映射 |
| **`exists_mem_eq_mkQ_of_mem_sup`**（`PRecursionSigmaRange.lean`）| $w\in U'\sqcup C'$ ⟹ $w$ 与某个 $c\in C'$ 模 $U'$ 同余（区间包含的实质）|
| **`class_mem_range_of_mem_sup`**（同上）| 若 $\psi$ 的像覆盖 $C'$ 的类，则 $w$ 的类在 $\psi$ 的像里 |
| **`range_le_of_forall_mem_sup`**（同上）| **区间包含 $\operatorname{range}\varphi\le\operatorname{range}\psi$**（$\sigma$ 存在性缺的最后一步）|
| **`inducedQuotient`**（`PRecursionInduced.lean`）| **level-1 映射 $\Phi'$ 的良定义**：$\Phi M\le C'$ 时 $x\mapsto\Phi x$ 下降到 $Y/M\to Y/C'$ |
| **`inducedQuotient_mkQ`**（同上）| 定义性质：$\Phi'(x+M)=\Phi x+C'$ |
| **`inducedQuotient_map_T_le`**（同上）| 递归里的 $T'\subseteq C'$ 一步 |
| **`quad_det` / `quad_exists_ne_zero`**（`QuadraticMu2.lean`）| **定理 C.3 的二次式**：$\det[z,Dz]=a^2s+a(u-c)y-by^2$，且 $(a,b)\ne(0,0)$ 时该二次式**不恒为零**（专家构造的核心）|
| **`smul_sub_mul_transpose` / `det_smul_sub_mul_transpose` / `det_smul_sub_mul_transpose_eq_zero`**（`Theorem12.lean`）| **定理 12 的因式分解**：$\det(\lambda\bullet U-U T^{\mathsf T})=\det U\cdot\det(\lambda I-T^{\mathsf T})$，以及 $\det U=0$ 时恒零 |
| **`perturb` / `perturb_eq_of_mem_ker` / `perturb_eigen_of_mem_ker` / `exists_eigenvector_forall_s` / `perturb2_eigen_of_mem_ker`**（`Perturbation.lean`）| **秩一/秩二扰动在 $\ker\varphi$ 上不动** —— $(3,1)$ 层 $\mu=1$（定理 5）与 $\mu=2$（引理 6）判据的核心引理 |
| **`Pval` / `Pval_spec` / `Pval_min` / `Pval_le`**（`PVal.lean`）| **$\mathcal P$ 的形式化定义（$\mathrm{Nat.find}$）与接口**：可达性、下界、任意可行解的上界 |
| **`step_le`**（`PRecursionStep.lean`）| **一步递归的 $({\le})$ 半（无 $\sigma$）**：level-1 可行 ⟹ 存在 level-0 可行 $U$，$T\le U$，$\dim U=\dim T+\dim U'$ |
| **`exists_sigma`**（`PRecursionLin.lean`）| **$\sigma$ 存在性（线性版，完整）**：level-1 可行 $\Rightarrow$ $\exists$ **线性** $\sigma:U'\to M$ 使 $\pi(\Phi(su+\sigma u))\in U'$ |
| **`exists_correction_pointwise`**（`PRecursionSigmaPoint.lean`）| **$\sigma$ 的逐点校正**：level-1 可行性 $\pi(\Phi(su))\in U'+C'$ + $C'\subseteq\pi\Phi(M)$ ⟹ $\exists m\in M:\ \pi(\Phi(su))-\pi(\Phi m)\in U'$（线性化未做）|
| **`qe_colspace` / `qe_finrank` / `qe_well_defined`**（`QuotientEquivalence.lean`）| **Theorem Q 的代数核心**（2026-11-01）：$(TV+Z)/S=TV/S+Z/S$；$\dim(TV+Z)=\dim S+\dim((TV+Z)/S)$；$T(S)\le Z$ ⟹ 商铅笔良定义 |
| **`rank_barrier`**（`RankBarrier.lean`）| **秩屏障的内核**：$\dim(VM+J)\le j+\dim\pi_J(\operatorname{range}M)$（`finrank` 形式）|
| **`d0_rank_nullity` / `d0_rank_iff`**（`D0Boundary.lean`）| **$d=0$ 边界的内核**：$\dim T(V)+\dim(V\cap\ker T)=\dim V$，且 $\dim T(V)=\dim V\iff V\cap\ker T=\bot$ |
| **`alpha_colspace` / `alpha_rank_dual` / `alpha_row_mul` / `alpha_five_a`**（`AlphaBridge.lean`）| **α 桥**：$[T\mid Z]$ 的列空间 $=\operatorname{range}T\sqcup Z$；行秩 = 列秩；$A^{\mathsf T}\ell=\ell\circ A$；$(5a)$ 的秩形式 |
| **`alpha_matrix_rank_row` / `alpha_matrix_rank_col`**（同上）| **真矩阵接上**：$\operatorname{rank}A=\dim(\text{行空间})=\dim(\text{列空间})$ |
| **`rho_zero_iff` / `five_a_of_le` / `five_b_auto`**（`Rho0Layer.lean`）| **B.3（$\rho=0$ 层）**：$\pi_J V=\bot\iff V\le J$；$V\le J$ 时 $(5a)\iff AV\le J$；$(5b)$ 自动 |
| **`exists_root_quadratic` / `exists_ne_zero_quadraticMap_eq_zero` / `K2_isotropic`**（`Isotropy.lean`）| **K.2 的内核**：代数闭域上 $\ge2$ 元二次型有非零零点（含一元二次式必有根）|
| **`finrank_sup_eq_add_quotient` / `pencil_rank_eq` / `pencil_rank_forall`**（`PencilEquivalence.lean`）| **B.1（商铅笔）**：$\dim(W\sqcup J)=\dim J+\dim\pi_J(W)$；逐 $\lambda$ 与 $\forall\lambda$ 的等价 |
| **`exists_eigenvector` / `finrank_lt_of_eigenvector_mod` / `c_pos_of_five_b`**（`Eigen.lean`）| **γ 桥 + A.2**：代数闭域上端同态有特征向量；$(\lambda I-A)v\in J$ ⟹ $(5b)$ 严格失败；**A.2 本身**（$c\ge1$）|
| **`a3_rows` / `a3_epsilon` / `a3_rho` / `a3_lower_bound`**（`A3Bound.lean`）| **A.3 的维数部分**：$q\ge r$、$q\ge r+\varepsilon$、$c\ge1\Rightarrow q\ge\rho+1$ |
| **`aClosure` / `c1_of_closure_top` / `c1_finrank`**（`C1Closure.lean`）| **C.1**：$A$-不变闭包 $=\top$ ⟹ $V=\top$（唯一可行解是全空间，$q_{\min}=n$）|


> 2026-10-28：新增 `PRecursionSigmaRange.lean`（3 条）+ `PRecursionInduced.lean`（3 条，level-1 映射良定义）+ `PRecursionSigmaPoint.lean`（1 条，$\sigma$ 的逐点校正），均 `lake env lean` 退出码 0。
> 注意：这 3 条是**一般形式**；把它们实例化到具体递归数据（$\psi:m\mapsto\pi(\Phi m)$、$\varphi:u\mapsto\pi(\Phi(su))$）仍是纸面层面。

## 尚未机器验证

~~$\sigma$ 存在性里唯一剩下的一步：区间包含~~ —— **2026-10-28 已机器验证其一般形式**（`PRecursionSigmaRange.lean`）。
剩余：把一般形式实例化到具体递归数据（纸面 §3 已给出，Lean 未做）。
（另有：递归迭代本身与 $O(n^4)$ 算法的形式化。）

## 数值对拍（独立于 Lean）

* `tools/p_algorithm/c195_P_q.py`：$\mathbb Q$ 上的精确递推算法，与 $\mathbb F_p$ 穷举（$p=5,7,11$）比较 → 无一个 $P_{\mathbb F_p} > P_{\mathbb Q}$（理论要求的单向不等式全部成立）。
* 网格穷举（$\mathbb Q$ 上，$\{-1,0,1\}$ 整数向量张成）与算法值 $11/12$ 一致；唯一不一致的实例未在网格中找到 $P_{\text{alg}}$ 维的见证，原因是可行集在 $\mathbb P^3$ 中的代数集可能**没有 $\mathbb Q$-点**——算法只做秩运算，给出的是代数闭域（$\mathbb C$）上的值，这正是 $q1$ 需要的。
* 早期的 $\mathbb F_5$ 穷举对拍：$n=4,5,6$ 共 $29/29$。
