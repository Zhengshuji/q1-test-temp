# Lean 4 功能观测器可行性证明链：六个形式化障碍的逐项解决方案

## 一、首先明确整体判断

这六个问题并不是六个彼此独立的数学困难。它们实际上分成三个层次：

1. **矩阵与线性映射之间的转换**：Item 1、Item 2。
2. **多项式与行列式的代数展开**：Item 3、Item 4。
3. **从谱条件到有限维 Gram 证书的形式化**：Item 5。

Item 6 则主要是 Mathlib API 的版本适配问题。

有一个很重要的发现：文档中对 Item 1 和 Item 2 的 Mathlib API 判断还可以进一步精确化。特别是，Mathlib 已经提供了矩阵秩等于列空间（或行空间）维数的定理，以及实矩阵乘以自身转置的秩保持定理。因此，这两个问题不需要重新证明全部线性代数基础。

本文采用以下标记区分结论的可靠程度：

- **已有 Mathlib 定理**：给出可以直接使用的定理名称。
- **可直接形式化的数学方案**：数学证明已经明确，Lean 工作主要是组织已有 API。
- **需要补充的形式化工作**：原文没有提供足够的定义，不能诚实地给出声称已经编译的完整证明。

需要说明的是，当前工作环境没有安装文档指定的 Lean 4.35.0 工具链，因此下面给出的代码片段不能冒称经过该版本的实际 `lake build`。我会将可以确定的 Mathlib 声明与尚需在固定环境核验的证明脚本明确区分，而不使用 `sorry` 冒充完成证明。

## 二、Item 1：矩阵秩恒等式（L1）

### 2.1 数学命题是正确的

原命题为：

```
variable {K : Type*} [Field K]
variable {m n p r : ℕ}

theorem rank_vstack_add_rank_mul
    (P : Matrix (Fin m) (Fin n) K)
    (M : Matrix (Fin p) (Fin n) K)
    (N : Matrix (Fin n) (Fin r) K)
    (hN : ∀ v : Fin n → K,
      P.mulVec v = 0 ↔ ∃ w, N.mulVec w = v)
    (hNr : ∀ w : Fin r → K,
      N.mulVec w = 0 → w = 0) :
    (Matrix.fromRows P M).rank =
      P.rank + (M * N).rank
```

这里的关键不是一般的矩阵乘法性质，而是一个标准的核空间分解。

令

\\[ V=K^n,\qquad U=K^m,\qquad W=K^p. \\]

定义线性映射

\\[ f:V\longrightarrow U,\quad f(v)=Pv, \\]\\[ g:V\longrightarrow W,\quad g(v)=Mv. \\]

那么：

\\[ \operatorname{rank} \begin{bmatrix}P\\\M\end{bmatrix} = \dim\operatorname{range}(f,g). \\]

考虑线性映射

\\[ \Phi:V\longrightarrow U\times W,\qquad \Phi(v)=(f(v),g(v)). \\]

根据线性映射的秩分解定理：

\\[ \boxed{ \dim\operatorname{range}\Phi = \dim\operatorname{range}f+ \dim g(\ker f). } \tag{1} \\]

这正是文档 Part II 中已有的：

```
theorem finrank_range_prod ...
```

它已经完成了最关键的抽象线性代数工作。

另一方面，假设 `hN` 和 `hNr` 成立。

`hN` 表示：

\\[ \operatorname{range}N=\ker P. \\]

`hNr` 表示：

\\[ \ker N=\\{0\\}. \\]

所以，限制映射

\\[ N:K^r\longrightarrow\ker P \\]

是线性同构。

因此：

\\[ g(\ker P) = \operatorname{range}(MN). \\]

由式 (1) 立即得到：

\\[ \begin{aligned} \operatorname{rank} \begin{bmatrix}P\\\M\end{bmatrix} &= \operatorname{rank}P+ \dim g(\ker P)\\\ &= \operatorname{rank}P+ \operatorname{rank}(MN). \end{aligned} \\]

这就证明了 L1。

### 2.2 真正应该使用的 Mathlib 桥梁

这里尤其需要纠正对 API 的搜索方向。

在指定版本的 Mathlib 中，相关定理的正式名称是：

```
Matrix.rank_eq_finrank_span_cols
Matrix.rank_eq_finrank_span_row
Matrix.rank_eq_finrank_range_toLin
```

而不是：

```
Matrix.rank_eq_finrank_col
Matrix.rank_eq_finrank_row
```

其中，\`Matrix.rank_eq_finrank_span_row\` 的形式为：

\\[ A.rank= \operatorname{finrank}\_K \left(\operatorname{span}\_K(\operatorname{range}(A.row))\right), \\]

而列空间版本对应：

\\[ A.rank= \operatorname{finrank}\_K \left(\operatorname{span}\_K(\operatorname{range}(A.col))\right). \\]

另一个重要事实是，\`Matrix.rank\` 本身就是通过 `mulVecLin.range` 的有限维维数定义的。Mathlib 文档给出了这一点，也给出了相应的 `rank_eq_finrank_range_toLin` 定理。

因此，不需要自行证明矩阵秩与线性映射值域维数之间的联系。

### 2.3 推荐的正式化顺序

不要直接在目标定理中展开矩阵的 `Fin` 索引。应当先建立一个一般的矩阵分块引理：

```
theorem rank_fromRows_eq_finrank_map
    (P : Matrix (Fin m) (Fin n) K)
    (M : Matrix (Fin p) (Fin n) K) :
    (P.fromRows M).rank =
      P.rank +
      Module.finrank K
        ↥(Submodule.map M.mulVecLin P.mulVecLin.ker) := by
  ...
```

这里数学上的意义是：

\\[ \operatorname{rank} \begin{bmatrix}P\\\M\end{bmatrix} = \operatorname{rank}P+ \dim M(\ker P). \tag{2} \\]

然后独立证明：

```
theorem finrank_map_mulVecLin_eq_rank_mul_of_basisKer
    (P : Matrix (Fin m) (Fin n) K)
    (M : Matrix (Fin p) (Fin n) K)
    (N : Matrix (Fin n) (Fin r) K)
    (hN : ∀ v, P.mulVec v = 0 ↔ ∃ w, N.mulVec w = v)
    (hNr : ∀ w, N.mulVec w = 0 → w = 0) :
    Module.finrank K
      ↥(Submodule.map M.mulVecLin P.mulVecLin.ker)
      = (M * N).rank := by
  ...
```

这一步只需处理下面三个关系：

\\[ \operatorname{range}N=\ker P, \\]\\[ (MN)v=M(Nv), \\]

以及 \\(N\\) 的单射性。

上述分解可以避免在最终定理中重复处理核空间、行空间以及矩阵秩。

**建议：将式 (2) 作为正式化的核心引理。** 这样不仅完成 L1，也能为后面 L2 的矩阵压缩提供统一工具。

### 2.4 关于具体 Lean 证明的注意事项

文档中原来的 `Matrix.fromRows P M` 对应的行索引不是 `Fin (m+p)`，而是：

```
Fin m ⊕ Fin p
```

这是一个非常容易忽略的类型问题。

Mathlib 提供：

```
Matrix.fromRows_mulVec
```

其数学内容是：

\\[ (P.fromRows\ M).mulVec(v) = \operatorname{Sum.elim}(Pv)(Mv). \\]

因此，矩阵对应的线性映射与两个映射的乘积（`LinearMap.prod`）之间，要通过

\\[ (Fin\\,m\oplus Fin\\,p\to K) \cong (Fin\\,m\to K)\times(Fin\\,p\to K) \\]

这一线性等价来连接。

这个等价最好单独定义并证明一次，而不是在每一个矩阵秩定理里重新处理。

**Item 1 的结论：** 数学上已经完全解决。真正需要补充的是矩阵到乘积线性映射的接口，以及基矩阵 \\(N\\) 对核空间的线性等价接口。\`Matrix.rank_eq_finrank_span_row\` 和 `Matrix.rank_eq_finrank_range_toLin` 是正确的秩桥梁。

---

## 三、Item 2：Gram 矩阵秩一致性条件（L4）

这个问题有一个比文档所列路线更直接的 Mathlib 入口。

### 3.1 首先纠正文档中的一个维数错误

文档写道：

\\[ \ker(MM^{\mathsf T})=\ker M. \\]

这一般不是一个有意义的等式，因为两个核空间的定义域不同：

\\[ M:\mathbb R^n\to\mathbb R^m, \\]

而：

\\[ MM^{\mathsf T}:\mathbb R^m\to\mathbb R^m. \\]

正确的等式是：

\\[ \boxed{ \ker(MM^{\mathsf T})=\ker(M^{\mathsf T}). } \tag{3} \\]

而且这正是证明 Gram 矩阵秩性质所需要的结果。

### 3.2 Mathlib 已经提供直接需要的秩定理

在指定版本的 Mathlib 中，已经存在：

```
Matrix.rank_self_mul_transpose
```

其形式为：

```
theorem Matrix.rank_self_mul_transpose
    (A : Matrix m n R) :
    (A * A.transpose).rank = A.rank
```

它要求实数所满足的线性序与严格有序环条件，以及相应的有限索引实例。

因此，对于文档中的矩阵 \\(M\\)，不需要重新证明：

\\[ \boxed{ \operatorname{rank}(MM^{\mathsf T}) = \operatorname{rank}M. } \\]

直接使用：

```
by
  exact Matrix.rank_self_mul_transpose M
```

这是本次六个问题中最明确的 API 级解决方案之一。

Mathlib 的矩阵秩文档还提供了对应的核空间定理：

```
Matrix.ker_mulVecLin_transpose_mul_self
```

要注意，该核空间定理的矩阵乘积方向是 \\(M^{\mathsf T}M\\)，而不是 \\(MM^{\mathsf T}\\)。两者不能混用。

### 3.3 原命题为什么成立

目标：

\\[ (\exists b,\ Mb=c) \iff \operatorname{rank}(MM^{\mathsf T}) = \operatorname{rank}(MM^{\mathsf T}+cc^{\mathsf T}). \tag{4} \\]

令：

\\[ G=MM^{\mathsf T}. \\]

首先：

\\[ \operatorname{range}G=\operatorname{range}M. \tag{5} \\]

这一结果在实数域上可由对称半正定性得到。事实上，\\(G\\) 与 \\(M^{\mathsf T}\\) 具有相同的核空间，结合正交补的线性代数关系即可得到相同的值域。

接下来考虑：

\\[ G+cc^{\mathsf T}. \\]

对任意 \\(x\in\mathbb R^m\\)，有：

\\[ \begin{aligned} x^{\mathsf T}(G+cc^{\mathsf T})x &=x^{\mathsf T}MM^{\mathsf T}x+ x^{\mathsf T}cc^{\mathsf T}x\\\ &=\\|M^{\mathsf T}x\\|^2+(c^{\mathsf T}x)^2. \end{aligned} \\]

两个平方项均非负。因此：

\\[ \ker(G+cc^{\mathsf T}) = \\{x\in\ker M^{\mathsf T}:c^{\mathsf T}x=0\\}. \\]

所以：

\\[ \operatorname{rank}(G+cc^{\mathsf T}) = \operatorname{rank}G \\]

当且仅当：

\\[ c^{\mathsf T}x=0 \qquad\forall x\in\ker M^{\mathsf T}. \\]

再利用有限维实内积空间中的基本关系：

\\[ (\ker M^{\mathsf T})^\perp = \operatorname{range}M, \\]

得到：

\\[ \operatorname{rank}(G+cc^{\mathsf T}) = \operatorname{rank}G \iff c\in\operatorname{range}M. \\]

而：

\\[ c\in\operatorname{range}M \iff \exists b,\ Mb=c. \\]

从而得到 L4。

### 3.4 一个更容易形式化的完整路线：增广矩阵

实际上，我更推荐用增广矩阵证明整个 L4，而不是直接证明两个 Gram 矩阵的值域相等。

定义：

\\[ D=\begin{bmatrix}M&c\end{bmatrix}. \\]

其维数为 \\(m\times(n+1)\\)。

于是：

\\[ DD^{\mathsf T}=MM^{\mathsf T}+cc^{\mathsf T}. \\]

根据 Mathlib 已有的 `Matrix.rank_self_mul_transpose`：

\\[ \operatorname{rank}(DD^{\mathsf T}) = \operatorname{rank}D. \\]

所以原命题等价于：

\\[ \exists b,\ Mb=c \iff \operatorname{rank}M=\operatorname{rank}D. \tag{6} \\]

而式 (6) 就是最基本的增广矩阵秩判据。

用列空间表达：

\\[ \operatorname{range}M = \operatorname{span}\\{\operatorname{col}\_1(M),\ldots, \operatorname{col}\_n(M)\\}. \\]

增广后：

\\[ \operatorname{range}D = \operatorname{range}M+\operatorname{span}\\{c\\}. \\]

因此：

\\[ \begin{aligned} \operatorname{rank}M=\operatorname{rank}D &\iff \operatorname{range}M=\operatorname{range}D\\\ &\iff c\in\operatorname{range}M\\\ &\iff \exists b,\ Mb=c. \end{aligned} \\]

这里最后一个从维数相等转为子空间相等的步骤，可以使用：

```
Submodule.eq_of_le_of_finrank_eq
```

即：两个有限维子空间中，一个包含于另一个且维数相等，则二者相等。

**Lean 中建议使用的辅助定义：**

```
def colMatrix (c : Fin m → ℝ) :
    Matrix (Fin m) (Fin 1) ℝ :=
  Matrix.vecMulVec c (fun _ : Fin 1 => 1)

def augment (M : Matrix (Fin m) (Fin n) ℝ)
    (c : Fin m → ℝ) :
    Matrix (Fin m) (Fin n ⊕ Fin 1) ℝ :=
  M.fromCols (colMatrix c)
```

接下来分成三个引理：

```
lemma augment_gram (M : Matrix (Fin m) (Fin n) ℝ)
    (c : Fin m → ℝ) :
    augment M c * (augment M c)ᵀ =
      M * Mᵀ + Matrix.vecMulVec c c := by
  ...
```

```
lemma rank_augment_iff (M : Matrix (Fin m) (Fin n) ℝ)
    (c : Fin m → ℝ) :
    (augment M c).rank = M.rank
      ↔ c ∈ LinearMap.range M.mulVecLin := by
  ...
```

```
theorem exists_mulVec_eq_iff_rank_gram
    (M : Matrix (Fin m) (Fin n) ℝ)
    (c : Fin m → ℝ) :
    (∃ b, M.mulVec b = c) ↔
      (M * Mᵀ).rank =
        (M * Mᵀ + Matrix.vecMulVec c c).rank := by
  ...
```

第三个引理的证明只需要：

1. `exists_solution_iff_mem_range`；
2. `augment_gram`；
3. `Matrix.rank_self_mul_transpose`；
4. `rank_augment_iff`。

其中，第 2 个引理通过 `Matrix.rank_eq_finrank_span_cols`、\`Matrix.range_mulVecLin\` 和 `Submodule.eq_of_le_of_finrank_eq` 建立。

这里的 `augment_gram` 可以通过 `Matrix.fromCols_mul_fromRows` 展开矩阵乘法，避免手动处理整个双重求和。\`Matrix.fromCols_mul_fromRows\` 正是此处适合使用的分块矩阵恒等式。

(推荐方案) Item 2 不需要重新发展 Gram 矩阵的正定性理论。增广矩阵路线更加直接，并且把 L4 化成一个一般的列空间命题。

---

## 四、Item 3：矩形矩阵的 Cauchy–Binet 公式

这个问题确实不同于前两个问题：这里缺少的不只是一个 API 桥梁，而是一个非平凡的行列式组合恒等式。

不过，已经有一个值得直接采用的外部 Lean 形式化成果。

### 4.1 已经存在的形式化成果

2026 年 9 月 24 日，Prove2Me 收录了一个已证明的 Cauchy–Binet 定理：

```
ClassicalGaps.cauchy_binet_det
```

作者是 Rizwan G Mir，所使用的环境为 Lean 4.30.0 和 Mathlib commit `c5ea003`。

其基本形式是：

```
theorem ClassicalGaps.cauchy_binet_det
    {m n : ℕ}
    (hmn : m ≤ n)
    (A : Matrix (Fin m) (Fin n) ℝ)
    (B : Matrix (Fin n) (Fin m) ℝ) :
    (A * B).det =
      ∑ S ∈ (Finset.univ : Finset (Fin n)).powersetCard m,
        if hS : S.card = m then
          (A.submatrix id
            (fun i : Fin m =>
              (S.orderIsoOfFin hS i : Fin n))).det *
          (B.submatrix
            (fun i : Fin m =>
              (S.orderIsoOfFin hS i : Fin n)) id).det
        else 0
```

该结果正是 Cauchy–Binet 公式在有限索引矩阵上的形式，且使用了 `Finset.orderIsoOfFin` 对选出的子集重新编号。

资料同时明确指出，这个定理尚未进入 Mathlib 主库。

可参考：

Prove2Me：The Cauchy–Binet formula。

### 4.2 如何把它转换为文档需要的矩形子矩阵版本

文档要求更一般的形式：

\\[ A\in K^{m\times n},\qquad B\in K^{n\times p}. \\]

选取：

\\[ I\subseteq\\{1,\ldots,m\\},\qquad J\subseteq\\{1,\ldots,p\\}, \\]

且：

\\[ |I|=|J|=t. \\]

需要证明：

\\[ \boxed{ \det((AB)\_{I,J}) = \sum\_{\substack{S\subseteq\\{1,\ldots,n\\}\\\\|S|=t}} \det(A\_{I,S})\det(B\_{S,J}). } \tag{7} \\]

这里可以完全规避直接处理两个任意 Finset 的困难。

先使用两个嵌入：

\\[ e_I:\operatorname{Fin}(t)\hookrightarrow\operatorname{Fin}(m), \\]\\[ e_J:\operatorname{Fin}(t)\hookrightarrow\operatorname{Fin}(p). \\]

定义：

\\[ A'=A.submatrix\ e_I\ id, \\]\\[ B'=B.submatrix\ id\ e_J. \\]

显然：

\\[ A'\in K^{t\times n},\qquad B'\in K^{n\times t}. \\]

直接按矩阵乘法定义逐项计算，可以得到：

\\[ (A'B')=(AB).submatrix\ e_I\ e_J. \\]

于是：

\\[ \det((AB)\_{I,J})=\det(A'B'). \\]

现在直接对 \\(A'\\) 和 \\(B'\\) 使用已有的方阵 Cauchy–Binet 定理。

这样便得到式 (7)。

### 4.3 为什么原文中的 Finset 表达式需要修改

原文件中的：

```
(A * B).submatrix (↑) (↑) I J
```

不是一个完整的 Lean 矩阵表达式。

`Matrix.submatrix` 需要的是索引函数：

```
Matrix.submatrix A f g
```

而不是直接传入两个 Finset。

建议把定理改为：

```
theorem cauchy_binet_rectangular
    {m n p t : ℕ}
    (A : Matrix (Fin m) (Fin n) R)
    (B : Matrix (Fin n) (Fin p) R)
    (I : Fin t ↪ Fin m)
    (J : Fin t ↪ Fin p) :
    ...
```

在求和项中，使用：

```
S.orderIsoOfFin hS
```

把中间索引集转换为 `Fin t`。

这种表达有三个好处：

- 不必额外定义任意 Finset 的排序函数。
- 两侧的行列指标类型自动都是 `Fin t`。
- 可以直接调用方阵版本的 Cauchy–Binet。

### 4.4 如何迁移到 Lean 4.35.0

推荐分成两步：

**第一步：移植方阵版本。**

先把：

```
ClassicalGaps.cauchy_binet_det
```

移植到：

```
leanprover/lean4:v4.35.0
Mathlib v4.35.0
```

不要同时扩大定理的泛化范围。

先保证方阵版本通过：

```
#check ClassicalGaps.cauchy_binet_det
```

并且实际执行完整的 `lake build`。

**第二步：建立矩形子矩阵版本。**

只需要证明：

```
(A.submatrix I id) * (B.submatrix id J)
    =
(A * B).submatrix I J
```

然后调用前面的方阵版本。

值得强调：这个外部成果的环境是 Lean 4.30.0，不能直接宣称它已经在 Lean 4.35.0 编译通过。它是一个可信的移植起点，而不是指定工具链下已经验证的依赖。

### 4.5 对功能观测器项目的具体应用

对于：

\\[ Q(\lambda)=\lambda X-G, \\]

设 \\(Q\\) 为 \\(q\times\omega\\) 矩阵。

那么：

\\[ Q(\lambda)^{\mathsf T}Q(\lambda) \\]

是 \\(\omega\times\omega\\) 矩阵。

Cauchy–Binet 给出：

\\[ \boxed{ \det(Q(\lambda)^{\mathsf T}Q(\lambda)) = \sum\_{\substack{I\subseteq\\{1,\ldots,q\\}\\\\|I|=\omega}} \det(Q_I(\lambda))^2. } \tag{8} \\]

对于复数情形，应使用共轭转置，并将平方改为模平方：

\\[ \det(Q(\lambda)^\*Q(\lambda)) = \sum\_{|I|=\omega} |\det Q_I(\lambda)|^2. \\]

这正是文档 Proposition 7 中需要的核心正定性来源。

因此，**Item 3 不需要直接证明所有任意矩形矩阵版本才能推进论文**。先实现式 (8) 所需要的方阵 Cauchy–Binet 特例，可能更经济。

---

## 五、Item 4：多项式矩阵乘法的系数提取

这是六个问题中最适合先完成的一个。

### 5.1 问题的本质

给定：

\\[ A\in K[\lambda]^{\omega\times n}, \\]\\[ B\in K[\lambda]^{n\times p}. \\]

需要证明：

\\[ \boxed{ (AB)\_{ij}.\operatorname{coeff}(k) = \sum\_{a=1}^{n} \sum\_{(u,v)\in\operatorname{antidiagonal}(k)} A\_{ia}.\operatorname{coeff}(u) B\_{aj}.\operatorname{coeff}(v). } \\]

实际上只需要两条性质：

第一，系数算子对有限和保持加法：

\\[ \operatorname{coeff}\_k\left(\sum_i f_i\right) = \sum_i\operatorname{coeff}\_k(f_i). \tag{9} \\]

第二，多项式乘积的系数公式：

\\[ \operatorname{coeff}\_k(fg) = \sum\_{u+v=k}f_u g_v. \tag{10} \\]

问题出在：这里需要使用的是针对 Finset 求和的版本，而不是文档中尝试使用的 `Polynomial.coeff_sum`。

### 5.2 建议增加一个局部辅助引理

直接通过 Finset 归纳证明式 (9)。

```
private theorem coeff_sum_finset
    {R α : Type*} [Semiring R]
    (s : Finset α)
    (f : α → Polynomial R)
    (k : ℕ) :
    (∑ a ∈ s, f a).coeff k =
      ∑ a ∈ s, (f a).coeff k := by
  classical
  induction s using Finset.induction_on with
  | empty =>
      simp
  | @insert a s ha ih =>
      simp [ha, ih]
```

这个引理的优势是：

- 不涉及特殊的 Polynomial API。
- 不需要处理 `Polynomial.sum`。
- 不需要手动调整类型类实例。
- 归纳过程中只使用系数的加法性质。

### 5.3 原命题的推荐证明

保持原定理的结构：

```
theorem coeff_mul_apply
    {n p : ℕ}
    (A : Matrix (Fin ω) (Fin n) K[X])
    (B : Matrix (Fin n) (Fin p) K[X])
    (i : Fin ω) (j : Fin p) (k : ℕ) :
    ((A * B) i j).coeff k =
      ∑ a : Fin n,
        ∑ x ∈ Finset.antidiagonal k,
          (A i a).coeff x.1 *
          (B a j).coeff x.2 := by
  classical
  rw [Matrix.mul_apply]
  rw [coeff_sum_finset]
  simp_rw [Polynomial.coeff_mul]
```

这里最后一步使用：

```
Polynomial.coeff_mul
```

而不是：

```
Polynomial.coeff_sum
```

`Polynomial.coeff_mul` 正是把多项式乘积系数展开到 `Finset.antidiagonal` 上的 Mathlib 定理。

需要注意：如果 `rw [coeff_sum_finset]` 因为求和记号的展开方式而不能直接匹配，可以显式将求和范围写成：

```
(Finset.univ : Finset (Fin n))
```

再进行重写。

### 5.4 为什么此前的四种证明策略会失败

四种失败实际上反映了不同的类型问题。

**第一次：**

```
rw [Matrix.mul_apply, Polynomial.coeff_sum]
```

失败的原因是 `Polynomial.coeff_sum` 不是针对一般 `Finset.sum` 的求和系数展开定理。

**第二次：**

遇到：

```
typeclass instance problem is stuck: AddCommMonoid ?m
```

原因是 `Polynomial.coeff_sum` 试图解释 Polynomial 内部特有的求和，而不是当前矩阵乘法产生的普通有限和。

**第三次：**

使用度数估计替代系数展开，会引入不必要的多项式归纳与类型类推断，因此容易造成 heartbeat 超时。

**第四次：**

直接应用 `Polynomial.coeff_mul`，确实已经正确处理了每一个多项式乘积，但外层的矩阵求和还没有被系数算子移进去。

因此，最合理的证明顺序就是：

\\[ \boxed{ \text{矩阵乘法展开} \longrightarrow \text{系数算子穿过有限和} \longrightarrow \text{多项式乘积系数展开}. } \\]

### 5.5 Item 4 的后续作用

有了这个引理，L6 的：

\\[ (iv)\Rightarrow(v) \\]

就不再是数学层面上的缺口。

具体地，将：

\\[ S(\lambda)=\sum\_{j=0}^{2\omega-2}S_j\lambda^j \\]

代入：

\\[ S(\lambda)(\lambda X-G)=I\_\omega. \\]

逐项取系数。

常数项：

\\[ -S_0G=I\_\omega. \\]

中间项：

\\[ S\_{j-1}X-S_jG=0. \\]

最高次项：

\\[ S\_{2\omega-2}X=0. \\]

这样就得到文档中的 (R0)。

因此，Item 4 解决后，L6 的两个方向便都具有 Lean 形式化基础：

\\[ (iv)\Rightarrow(v),\qquad (v)\Rightarrow(iv). \\]

其中第二个方向的 `spoly_mul_pencil_eq_one` 已经完成。

---

## 六、Item 5：Proposition 7 的窗口 Gram 证书

这是六个项目中最值得先确定数学表述的问题。

文档自己也指出，目前并没有一个确定的 Lean 定理陈述。这不是一个简单的 tactic 问题，而是需要先确定证书矩阵 \\(Z\\) 的定义。

我建议从 Bézout 定理出发，重新整理它的有限维线性代数含义。

### 6.1 从无公共复根出发

设：

\\[ f_1,\ldots,f_s\in\mathbb R[\lambda], \\]

并且：

\\[ \deg f_i\leq\omega,\qquad \omega\geq1. \\]

无公共复根的条件是：

\\[ \boxed{ \forall z\in\mathbb C,\quad \exists i,\quad f_i(z)\neq0. } \tag{11} \\]

这里把实系数多项式自然地看成复系数多项式。

由 Bézout 定理，可以得到：

\\[ \exists g_1,\ldots,g_s\in\mathbb R[\lambda], \\]

满足：

\\[ \sum\_{i=1}^{s}g_i(\lambda)f_i(\lambda)=1. \tag{12} \\]

而且：

\\[ \deg g_i<\omega. \\]

这正是文档 Part II 已经完成的 Bézout 有界次数结论在实系数、无公共复根情形下的应用。

这里有一个需要正式化的细节：文档现有 `exists_bezout_family` 是基于代数闭域上的无公共根条件。若直接用于复域，需要把复系数 Bézout 关系转化为实系数关系；对于实系数 \\(f_i\\)，可以通过实系数最大公因子或对复系数 Bézout 关系取实部来处理。不能直接把“无公共复根”替换为“无公共实根”。

### 6.2 将 Bézout 关系转换为有限维线性方程

因为：

\\[ \deg g_i<\omega, \\]

可以写成：

\\[ g_i(\lambda) = \sum\_{j=0}^{\omega-1}y\_{ij}\lambda^j. \\]

将它代入式 (12)：

\\[ \sum_i\sum\_{j=0}^{\omega-1} y\_{ij}\lambda^j f_i(\lambda)=1. \tag{13} \\]

又因为：

\\[ \deg(\lambda^j f_i) \leq j+\omega \leq2\omega-1, \\]

所以式 (13) 的所有系数只需要考虑：

\\[ 0,1,\ldots,2\omega-1. \\]

因此，定义系数矩阵：

\\[ Z\in\mathbb R^{s\omega\times2\omega}, \\]

它的行指标为：

\\[ (i,j)\in\\{1,\ldots,s\\}\times\\{0,\ldots,\omega-1\\}, \\]

列指标为：

\\[ k\in\\{0,\ldots,2\omega-1\\}. \\]

具体定义：

\\[ \boxed{ Z\_{(i,j),k} = \operatorname{coeff}\_k(\lambda^j f_i). } \tag{14} \\]

再令：

\\[ y=(y\_{ij})\in\mathbb R^{s\omega}, \\]

以及：

\\[ e_0=(1,0,\ldots,0)^{\mathsf T} \in\mathbb R^{2\omega}. \\]

那么式 (13) 等价于：

\\[ \boxed{Z^{\mathsf T}y=e_0.} \tag{15} \\]

这一步非常关键。

原来的多项式恒等式已经转化成一个有限维线性方程组。

### 6.3 为什么可以进一步写成 Gram 方程

利用实数域上的 Gram 矩阵性质：

\\[ \boxed{ \operatorname{range}(Z^{\mathsf T}Z) = \operatorname{range}(Z^{\mathsf T}). } \tag{16} \\]

这是一个通用的实矩阵结论，不依赖于 \\(Z\\) 是如何构造的。

因此：

\\[ \begin{aligned} \exists y,\quad Z^{\mathsf T}y=e_0 &\iff e_0\in\operatorname{range}(Z^{\mathsf T})\\\ &\iff e_0\in\operatorname{range}(Z^{\mathsf T}Z)\\\ &\iff \exists x,\quad Z^{\mathsf T}Zx=e_0. \end{aligned} \\]

于是：

\\[ \boxed{ \text{无公共复根} \iff \exists x\in\mathbb R^{2\omega}, \quad Z^{\mathsf T}Zx=e_0. } \tag{17} \\]

这里已经把 Proposition 7 的核心证书转换成了一个标准的矩阵方程。

需要特别注意：式 (17) 使用的是式 (14) 所定义的系数矩阵。如果论文中实际使用的 \\(Z\\) 不是这个矩阵，那么必须先证明两者之间的对应关系，不能直接把它们当作同一个对象。

### 6.4 建议采用的 Lean 定义

可以在 `Q1Paper` 中定义：

```
def bezoutWindow
    {ι : Type*}
    [Fintype ι]
    (f : ι → ℝ[X])
    (ω : ℕ) :
    Matrix (ι × Fin ω) (Fin (2 * ω)) ℝ :=
  fun ij k =>
    (Polynomial.X ^ (ij.2 : ℕ) * f ij.1).coeff k
```

常向量：

```
def e0 (ω : ℕ) : Fin (2 * ω) → ℝ :=
  fun k => if k.val = 0 then 1 else 0
```

这里的矩阵尺寸值得特别注意：

\\[ Z:\mathbb R^{s\omega\times2\omega}. \\]

因此：

\\[ Z^{\mathsf T}Z: \mathbb R^{2\omega\times2\omega}. \\]

这正好对应文档给出的：

\\[ x\in\mathbb R^{2\omega}. \\]

### 6.5 建议正式化的三个定理

我建议不要直接写一个巨大的 Proposition 7 定理，而是拆成三个定理。

**第一定理：系数矩阵与 Bézout 关系。**

```
theorem bezout_iff_window_linear
    (f : ι → ℝ[X])
    (ω : ℕ)
    (hω : 1 ≤ ω)
    (hdeg : ∀ i, (f i).natDegree ≤ ω) :
    ...
```

目标是：

\\[ \begin{aligned} &\exists g,\quad \sum_i g_i f_i=1,\quad \forall i,\deg g_i<\omega\\\ &\quad\iff\quad \exists y,\quad Z^{\mathsf T}y=e_0. \end{aligned} \\]

**第二定理：Gram 方程与普通线性方程等价。**

```
theorem gram_solvable_iff_transpose_solvable
    (Z : Matrix α (Fin (2 * ω)) ℝ) :
    (∃ x, (Zᵀ * Z).mulVec x = e0 ω) ↔
    (∃ y, Zᵀ.mulVec y = e0 ω) := by
  ...
```

其证明使用式 (16)。

实际上，式 (16) 可以先作为独立通用引理证明，然后这一个定理只需要使用已有的：

```
exists_solution_iff_mem_range
```

**第三定理：Proposition 7。**

把文档已有的无公共复根条件与有界 Bézout 定理连接起来：

```
theorem proposition7_window_certificate
    (f : ι → ℝ[X])
    (ω : ℕ)
    (hω : 1 ≤ ω)
    (hdeg : ∀ i, (f i).natDegree ≤ ω) :
    NoCommonComplexRoot f ↔
      ∃ x : Fin (2 * ω) → ℝ,
        (Zᵀ * Z).mulVec x = e0 ω := by
  ...
```

其中 `NoCommonComplexRoot` 应另行明确定义为：

\\[ \forall z\in\mathbb C,\quad \exists i,\quad \operatorname{eval}\_{z}(f_i)\neq0. \\]

这样，Proposition 7 就不再是一个模糊的矩阵证书，而是一个经过 Bézout 和线性代数逐层建立的等价定理。

### 6.6 Item 5 有一个重要的数学优势

上述证明不仅适用于最大子式。

实际上，它只使用了：

- 一族次数有界的实系数多项式；
- 无公共复根；
- 有界次数 Bézout 表示；
- 一个实数 Gram 矩阵。

因此，它可以成为一个一般性定理，供多个谱判据复用。

这比只针对功能观测器中特定矩阵的 Proposition 7 更有价值。

---

## 七、Item 6：Mathlib v4.35.0 的 API 缺口整理

这一部分不需要重新进行数学证明，主要是把已经确定的正确 API 固定下来。

我还专门核对了 Mathlib 的 `v4.35.0` 标签下的源文件，而不是只依赖当前 master 分支的文档。

相关源文件：

- Matrix.Rank.lean（v4.35.0）
- Matrix.ToLin.lean（v4.35.0）

值得特别保留以下 API：

| 目标                      | v4.35.0 中应使用的名称                           |
| ----------------------- | ----------------------------------------- |
| 矩阵秩与列空间                 | `Matrix.rank_eq_finrank_span_cols`        |
| 矩阵秩与行空间                 | `Matrix.rank_eq_finrank_span_row`         |
| 矩阵秩与线性映射值域              | `Matrix.rank_eq_finrank_range_toLin`      |
| \\(M^{\mathsf T}M\\) 的秩 | `Matrix.rank_transpose_mul_self`          |
| \\(MM^{\mathsf T}\\) 的秩 | `Matrix.rank_self_mul_transpose`          |
| 矩阵乘法对应线性映射复合            | `Matrix.mulVecLin_mul`                    |
| 矩阵行拼接与向量乘法              | `Matrix.fromRows_mulVec`                  |
| 矩阵乘向量的值域                | `Matrix.range_mulVecLin`                  |
| 从线性映射值域取维数              | `LinearMap.finrank_range_add_finrank_ker` |
| 子空间维数相等时的包含关系           | `Submodule.eq_of_le_of_finrank_eq`        |

其中有两个容易混淆的地方：

**第一，Gram 矩阵的方向。**

```
Matrix.rank_transpose_mul_self
```

处理：

\\[ M^{\mathsf T}M. \\]

```
Matrix.rank_self_mul_transpose
```

处理：

\\[ MM^{\mathsf T}. \\]

这两个定理在 v4.35.0 的源码中都确实存在。

**第二，矩阵乘法的线性映射对应。**

应优先使用：

```
Matrix.mulVecLin_mul
```

其具体形式：

```
@[simp]
theorem Matrix.mulVecLin_mul
    (M : Matrix l m R)
    (N : Matrix m n R) :
    Matrix.mulVecLin (M * N) =
      (Matrix.mulVecLin M).comp
        (Matrix.mulVecLin N)
```

这正好适用于 Item 1。

其他文档中记录的 API 处理方式可以保留。例如：

- `Matrix.sum_mul` 而不是普通的 `Finset.sum_mul`。
- `Matrix.mul_smul` 而不是 `mul_smul`。
- `Fin.sum_univ_one` 而不是 `Finset.sum_univ_one`。
- `Polynomial.coeff_mul` 与自定义 `coeff_sum_finset` 配合。
- 对任意域不要使用依赖有序环的 `linarith`。
- 行列式次数估计优先使用逐行 Laplace 展开，避免直接展开全部排列求和。

这些经验非常值得作为项目内的正式开发规范。

---

## 八、补充：Item 1 最接近完整 Lean 实现的核心适配代码

为了使 Item 1 的解决方案更容易落到现有工程，我把上面的数学方案进一步整理成 Lean 代码结构。

真正需要解决的关键是：

\\[ (\operatorname{Fin}m\oplus\operatorname{Fin}p\to K) \cong (\operatorname{Fin}m\to K)\times (\operatorname{Fin}p\to K). \\]

先定义通用的线性等价：

```
private def sumArrowEquivProd
    {K : Type*} [Semiring K]
    (α β : Type*) :
    ((α ⊕ β) → K) ≃ₗ[K]
      ((α → K) × (β → K)) where

  toFun v :=
    (fun a => v (Sum.inl a),
     fun b => v (Sum.inr b))

  invFun x :=
    Sum.elim x.1 x.2

  left_inv v := by
    funext i
    cases i <;> rfl

  right_inv x := by
    rcases x with ⟨u, v⟩
    rfl

  map_add' u v := by
    apply Prod.ext <;> funext i <;> rfl

  map_smul' c v := by
    apply Prod.ext <;> funext i <;> rfl
```

接下来，定义：

```
private theorem rank_fromRows_add_map
    (P : Matrix (Fin m) (Fin n) K)
    (M : Matrix (Fin p) (Fin n) K) :
    (P.fromRows M).rank =
      P.rank +
        Module.finrank K
          ↥(Submodule.map M.mulVecLin P.mulVecLin.ker) := by
  classical

  let e := sumArrowEquivProd (K := K) (Fin m) (Fin p)

  have hpair :
      e.toLinearMap.comp (P.fromRows M).mulVecLin =
        P.mulVecLin.prod M.mulVecLin := by
    ext v
    apply Prod.ext
    · funext i
      simp [e, Matrix.fromRows_mulVec]
    · funext i
      simp [e, Matrix.fromRows_mulVec]

  have hrange :
      (P.mulVecLin.prod M.mulVecLin).range =
        Submodule.map e.toLinearMap
          (P.fromRows M).mulVecLin.range := by
    rw [← hpair, LinearMap.range_comp]

  calc
    (P.fromRows M).rank =
        Module.finrank K
          ↥(P.fromRows M).mulVecLin.range := rfl

    _ = Module.finrank K
          ↥(P.mulVecLin.prod M.mulVecLin).range := by
      rw [hrange]
      exact (e.finrank_map_eq _).symm

    _ = P.rank +
          Module.finrank K
            ↥(Submodule.map M.mulVecLin P.mulVecLin.ker) := by
      simpa [Matrix.rank] using
        (finrank_range_prod P.mulVecLin M.mulVecLin)
```

这是 Item 1 的主要矩阵适配层。最后一行使用的是文档中已经证明的 `finrank_range_prod`。

然后只需把 \\(N\\) 的值域等于 \\(P\\) 的核空间这一事实传递给矩阵乘积：

```
private theorem mulVecLin_range_eq_ker
    (P : Matrix (Fin m) (Fin n) K)
    (N : Matrix (Fin n) (Fin r) K)
    (hN : ∀ v : Fin n → K,
      P.mulVec v = 0 ↔
        ∃ w, N.mulVec w = v) :
    N.mulVecLin.range = P.mulVecLin.ker := by
  ext v
  simp only [
    LinearMap.mem_range,
    LinearMap.mem_ker,
    Matrix.mulVecLin_apply
  ]
  exact (hN v).symm
```

利用：

```
Matrix.mulVecLin_mul
```

得到：

\\[ \begin{aligned} \operatorname{range}((MN).mulVecLin) &=\operatorname{range} (M.mulVecLin\circ N.mulVecLin)\\\ &=M(\operatorname{range}N)\\\ &=M(\ker P). \end{aligned} \\]

对应的 Lean 核心重写为：

```
have hMNrange :
    (M * N).mulVecLin.range =
      Submodule.map M.mulVecLin P.mulVecLin.ker := by
  rw [Matrix.mulVecLin_mul,
      LinearMap.range_comp,
      mulVecLin_range_eq_ker P N hN]
```

最后把这个结果代入 `rank_fromRows_add_map` 即可。

这里还有一个值得注意的数学简化：

**`hNr` 对目标秩恒等式实际上是冗余的。**

原因是：

\\[ \operatorname{range}(MN) = M(\operatorname{range}N). \\]

只要 `hN` 保证 \\(\operatorname{range}N=\ker P\\)，就已经足够。并不需要再要求 \\(N\\) 单射。

如果希望保留原来的定理签名，可以继续保留 `hNr` 参数，只是在证明中不使用它。

以上代码展示的是完整的证明分解和关键适配项；由于本次无法实际启动指定 Lean 工具链，仍需将这一段放回 `Q1Paper` 工程执行编译，尤其核验局部的 `LinearEquiv.finrank_map_eq` 和 `LinearMap.range_comp` 的具体 elaboration。

---

## 九、六个问题最终解决状态

综合以上结果：

| 项目                  | 数学状态       | Lean 形式化状态            | 推荐处理                               |
| ------------------- | ---------- | --------------------- | ---------------------------------- |
| Item 1：矩阵秩恒等式       | 已证明        | 主要适配层已给出              | 使用 `finrank_range_prod`            |
| Item 2：Gram 秩一致性    | 已证明        | 核心秩引理已有 Mathlib 定理    | 使用 `rank_self_mul_transpose` 和增广矩阵 |
| Item 3：Cauchy–Binet | 已知经典定理     | 有 Lean 4.30 外部证明，尚需移植 | 先实现方阵版本                            |
| Item 4：系数提取         | 已证明        | 给出了辅助引理和直接证明结构        | 优先完成                               |
| Item 5：Gram 窗口证书    | 给出了严格的候选形式 | 需要与论文的实际 Z 定义核对       | 从 Bézout 有界次数出发                    |
| Item 6：API 缺口       | 已整理        | 可直接按 v4.35.0 API 使用   | 维护项目内部 API 规范                      |

这里要区分两种意义上的完成：

**数学上的完成**不等于**Lean 内核检查通过**。

特别是 Item 1、Item 2、Item 5，不能仅凭数学推导就声称原项目已经全部通过 `lake build`。

## 十、建议的后续工作顺序

我建议采用以下顺序，而不是按 Item 1 到 Item 6 简单顺序机械推进。

**第一阶段：完成最确定的基础定理**

1. **Item 4：系数提取**

   补上 `coeff_sum_finset`，完成 L6 的 (iv) ⇒ (v)。
2. **Item 1：矩阵秩恒等式**

   添加 `sumArrowEquivProd`，利用既有 `finrank_range_prod` 完成矩阵适配。
3. **Item 2：Gram 矩阵秩判据**

   使用 Mathlib 已有的 `Matrix.rank_self_mul_transpose`，补充增广矩阵引理。

---

**第二阶段：补齐行列式工具**

1. **Item 3：Cauchy–Binet**

   移植外部方阵版本，再推广到一般矩形子矩阵。
2. **Item 5：Proposition 7**

   固定 \\(Z\\) 的确切定义，完成有界 Bézout、系数矩阵及 Gram 方程之间的等价关系。

---

**第三阶段：整合论文主定理**

将 L1–L6、Proposition 7、Prop 1 和 Theorem 1–3 连接成完整证明链，并逐项执行 `#print axioms`。

### 十一、我认为最值得保留的三个新认识

第一，**Item 1 不应该被当作一个独立的矩阵行列式问题。**

它是 `finrank_range_prod` 的直接矩阵化。真正需要的是有限函数空间的线性等价，而不是重新证明秩恒等式。

第二，**Item 2 的 Gram 证书可以通过增广矩阵统一处理。**

尤其是：

\\[ \operatorname{rank}(MM^{\mathsf T}+cc^{\mathsf T}) = \operatorname{rank}[M\ c]. \\]

这个等式使 L4 直接归结为增广矩阵秩判据，而不需要另建一套正定矩阵理论。

第三，**Item 5 的证书本质上是有界 Bézout 恒等式的 Gram 化。**

其数学结构是：

\\[ \boxed{ \begin{gathered} \text{无公共复根}\\\ \Updownarrow\\\ \text{有界次数 Bézout 表示}\\\ \Updownarrow\\\ Z^{\mathsf T}y=e_0\text{ 可解}\\\ \Updownarrow\\\ Z^{\mathsf T}Zx=e_0\text{ 可解}. \end{gathered} } \\]

这条链值得作为论文中一个独立的通用形式化模块。

**最终判断：** 当前项目最重要的基础数学并没有被这六个障碍否定。Item 1、2、4 已经有明确的完成路径，其中 Item 2 还找到了指定版本 Mathlib 的直接定理；Item 3 有可以借鉴的外部 Lean 证明；Item 5 则需要以真实的证书矩阵定义为准，完成最后的数学对接。

真正的工作重点已经从寻找复杂数学定理，转移到了建立可靠的矩阵、线性映射、多项式和 Gram 证书之间的形式化接口。