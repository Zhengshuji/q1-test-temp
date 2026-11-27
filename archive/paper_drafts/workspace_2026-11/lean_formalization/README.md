# Lean 形式化路线（按专家回复 87 号文档整理）

> 来源：`workspace/for_expert/archive/87_lean_coverage-reply.md`（专家对五个缺口的逐条评估）。
> 本文只记录**可执行的顺序与接口**，不重复论证。

## 结论摘要

专家的判断：现有四个抽象核是实质贡献，但主定理尚未 kernel-checked。推荐**不要**追求"全部形式化"，
而是把证明链上最容易藏错的三座代数桥先做掉，把编码规模与系数增长留在论文里做可审计的外部论证。

## 顺序（依赖驱动）

| 步 | 内容 | 依赖 | 状态 |
|---|---|---|---|
| 0 | **矩阵压缩恒等式 $(\ast)$**：`finrank (range (f.prod g)) = finrank (range f) + finrank (map g (ker f))` | 无 | ✅ **已完成**（`Q1Paper/RankIdentity.lean`，`finrank_range_prod`，公理仅 `propext/choice/Quot.sound`，`lake build` 9067 jobs 通过） |
| 1 | **G2**：$s$ 个多项式的有界次数 Bézout。**不要**对 gcd 归纳（次数会膨胀）；走"两个一般线性组合：$F=\sum a_if_i$ 取非零，$G=\sum b_if_i$ 避开 $F$ 的有限根集（有限个真超平面覆盖不了 $K^s$），再用两多项式 Bézout，$g_i=Ua_i+Vb_i$，$\deg g_i<\omega$" | 已形式化的 `bezout_of_gcd_eq_one` | ✅ **完成**：`Q1Paper/G2Assembly.lean` 的 `exists_bezout_family` 一步给出 Lemma 4 的结论（$\sum_i g_if_i=1$ 且 $\deg g_i<\omega$）。组件：① 超平面规避 `exists_forall_apply_ne_zero`（`HyperplaneAvoid.lean`）；② 非零组合与根集有限（`BezoutDeg.lean`）；③ 无公共根 ⟹ Bézout 关系 `isCoprime_of_no_common_root`（绕开 gcd 归一化）；④ 次数界 `exists_bezout_deg_lt`；⑤ 拼装（整数情形 $G=0$ 单独处理）。公理均仅三条 |
| 2 | **G3a**：矩形左逆。**不要**定义 `RectangularAdjugate`；令 $Q_I=E_IQ$、$S_I=\operatorname{adj}(Q_I)E_I$，用方阵 `Matrix.adjugate_mul` 推 $S_IQ=f_II_\omega$，再乘 Bézout 系数合并 | 第 1 步 | ✅ **完成**：`G3Adjugate.lean`（`rowSel_mul`、`adjRowInverse_mul`：$S_IQ=\det(Q_I)\cdot1$）+ `G3LeftInverse.lean`（`leftInverse_of_bezout`、`exists_leftInverse`：$S=\sum_e g_eS_e$，$SQ=1$）。**注意**：`exists_leftInverse` 把"子式次数 $\le\omega$"作为假设 `hdeg` 传入——这正是下一块要证的 |
| 2b | **G3b 次数估计**：$\deg\det\le\omega$ 与 $\deg\operatorname{adj}\le\omega-1$；合成后 $\deg S\le2\omega-2$ | G3a | ✅ **完成**：`DegreeBounds.lean` —— `natDegree_det_le_sum`（按行分次）、`natDegree_det_le`（一致界）、`sum_ite_eq_zero_one`、`natDegree_adjugate_le`（用 `adjugate_apply` + `updateRow_apply` 的逐点形式）。**收尾完成**：`natDegree_adjRowInverse_le`（单块元素次数 $\le\omega-1$）+ `exists_leftInverse_linear`（`S*Q=1` 且 `S` 的元素次数 $\le 2\omega-2$，不再需要 `hdeg` 假设） |
| 3 | **G3c**：多项式左逆与系数系统 (\$)。论文 Lemma 6 的证明链是 (1)⇔(2)⇔(3)⇒(4)⇒(5)⇒(1) | G3a/G3b | ✅ **已按用户决定收敛**：形式化了 **(5)⇒(4)**（\spoly_mul_pencil_eq_one\，一般 \$；\spoly_mul_pencil_zero\ 为 \$\omega=1\$ 特例）与编码/乘积展开。**(4)⇒(5) 不再要求**（用户 2026-11-11 明确：Lean 只覆盖论文证明所需的方向）。**注意**：论文 Lemma 6 的证明里确实含 (4)⇒(5) 一步，该步仍是纸面级，§IX 的覆盖声明不应把它算作 Lean |
| 4 | **G1**：矩形 Cauchy–Binet。先移植外部 Lean 4.30 成果 `ClassicalGaps.cauchy_binet_det`（据称未进 Mathlib），核对许可证与 Lean 4.35 兼容性；走 Leibniz 展开路线（4 个子引理：展开、非单射项相消、按像集分组、合并） | 独立 | 中 |
| 5 | **G5**：固定 $(\omega,J)$ 分支的正确性定理；再证整个公式多项式大小 | 第 4 步（Gram 引理） | 中高 |
| — | **G4**：**不形式化**。论文里做 Cramer/Hadamard 的显式审计（清分母、Hadamard 界、项数的对数） | — | 低 |

## 接口约定（专家给的具体建议）

- 矩阵级与抽象级**成对**给出：`rank_stack_eq_rank_add_rank_restriction`（子空间版）与
  `rank_vstack_eq_rank_add_rank_mul_kernelBasis`（矩阵版）。
- "存在系数避开有限个真超平面"抽象成**线性代数引理**（无限域上有限个非零线性泛函不能覆盖全空间），
  不要写成多项式专用。
- 次数约束用 `natDegree`（零多项式的次数约定要单独处理）；$\omega=0$ 的常数情形单独成引理。
- 代数闭域上做互素/Bézout，实系数结果由"复解取实部"回到 $\mathbb R$，不要混为一谈。
- $(\ast)$ 的优先级高于 G1：它是把现有抽象 Lean 结果与论文矩阵表述连起来的必要一环。

## 与论文的接口

论文 §IX 的证据表当前写 `Lean core`；完成第 0–3 步后可升级为
"Lemma 1（矩阵形式）、Lemma 4、Lemma 5、Proposition 1 的 Lean"，但**不要**写成主定理已 kernel-checked。

## G3c 最后一步的 Lean 陈述（下一轮直接抄）

`lean
theorem spoly_mul_pencil_eq_one {d : ℕ} (S : Fin (d + 1) → Matrix (Fin ω) (Fin q) K)
    (Xm Gm : Matrix (Fin q) (Fin ω) K)
    (h0 : S 0 * Gm = -1)
    (hj : ∀ j : Fin d, S (Fin.castSucc j) * Xm - S (Fin.succ j) * Gm = 0)
    (hd : S (Fin.last d) * Xm = 0) :
    spoly S * pencil Xm Gm = 1
`

走法：
w [spoly_mul_pencil] → Matrix.ext i j → Polynomial.ext k →
对每个 $ 用 Polynomial.coeff_sum、coeff_smul、coeff_C_mul、coeff_X_pow 化简，
得到 $[\lambda^k] = S_{k-1}X - S_kG$（=0$ 用 h0，\le k\le d$ 用 hj，=d+1$ 用 hd，其余为 0）。

## 已核实的 Mathlib API（G2 用）

| 需要的东西 | 现状 |
|---|---|
| 非零多项式根集有限 | ✅ `Polynomial.finite_setOfPred_isRoot (hp : p ≠ 0) : Set.Finite {x | IsRoot p x}`（`Algebra/Polynomial/Roots.lean:138`） |
| 两多项式 Bézout（无次数界） | ✅ 已有 `Q1Paper.bezout_of_gcd_eq_one` |
| 两多项式 Bézout 的**次数界**（`deg u < deg g` 等） | ❓ Mathlib 未确认；`grep gcd_eq_one_iff` 在 `Algebra/Polynomial/` 下无命中，需要自己写 |
| 超平面规避 | ✅ `Q1Paper.exists_forall_apply_ne_zero` |
| 代数闭域上"非寻常多项式有根" | ❓ 未确认名字（`IsAlgClosed.exists_root` 一类），搜索时注意别在项目根跑 `grep -r`（一次跑错把整个仓库扫了一遍） |

**踩坑记录**：`linarith` 只在**有序**环上可用；一般域 `K` 上必须用 `field_simp` / `eq_neg_iff_add_eq_zero` / `ring` 一类等式重写。`linear_combination` 在当前 import 集合下不可用。

## 88 号回复的补充（体裁与形式化覆盖）

- **体裁定案**：parameterized algorithms / complexity 论文，控制论只作动机；形式化优先级**不因体裁改变**，
  但论文呈现方式要改：算法定理按"算法描述 / 正确性 / 运行时间 / 参数依赖"四段写。
- **新增第 4 个优先项**：**Gram 矩阵的核心像空间与秩性质**（`im(ZᵀZ) = im(Zᵀ)`，由 `ker(ZᵀZ)=ker Z` +
  正交补得出），这是证书的线性代数基础，可在固定分支形式化里直接复用。
- **论文措辞**：只能说"若干关键抽象代数组件已用 Lean 4 + Mathlib 形式化、无额外公理"，
  并明确"矩阵级归约、次数界、系数位长与编码仍在论文中证明，尚未进入形式化"。
- **bit-size 与 QE**：都不形式化；但论文必须自己把 bit-size 链条写完整（专家列了 8 项）。

## 相关文件

- 提问（体裁与证明粒度）：`workspace/for_expert/archive/88_genre_and_proof_detail.md`
- 回复：`workspace/for_expert/archive/88_genre_and_proof_detail-reply.md`
- 提问（Lean 覆盖）：`workspace/for_expert/archive/87_lean_coverage.md`
- 回复：`workspace/for_expert/archive/87_lean_coverage-reply.md`
- Lean 源码：`paper/lean/Q1Paper/`（镜像）、WSL `~/WorkSpace/lean4/Q1Paper`
