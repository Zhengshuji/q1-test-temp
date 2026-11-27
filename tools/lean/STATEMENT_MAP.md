# Lean 声明 ↔ 命题 对照表（statement map）



> **为什么有这个文件**：`[Lean]` 只说明"某个 Lean 定理被机器检查通过"，**不说明它和论文里那句话是同一句话**。
>
> **目的（2026-11-07 用户修订）**：本表给出**证明框架**——以命题为节点、以"支撑关系"为边的一张有向图。
> 它**只关注命题之间的联系，不关注具体证明**；一条命题只需要**出处**：
> * 引用参考文献（作者/年份/arXiv 编号），或
> * 链接到本项目**已证明的命题**（`docs/` 或 `proof/` 的链接皆可，也可只写编号如 `B.9(a)`）。
>
> **每一项的写法**：`- \`声明名\` —— <一句话>。**出处**：…`；`**意义**` 选填（该声明在框架中的作用）。
> 历史上的 `**对应**` / `**差异**` 格式保留有效，但**不再强制**："差异"曾是方向发散时用来区分各命题的，
> 现按用户指示取消。
>
> **闸门**：`tools/hygiene/audit_lean_statements.py` 检查三件事——每个声明都登记、每条登记的声明真实存在、
> 每条都带**出处**。工具/辅助声明可按 [`EXEMPT_AUXILIARY.md`](EXEMPT_AUXILIARY.md) 做文件级豁免；
> 豁免文件里的**命题级**声明仍须点名并登记。

---



## 0. 共同约定（很重要）



论文用**矩阵/秩**语言（$\operatorname{rank}[L;CA;C]$、$\det$），Lean 用**子空间/维数**语言

（`Submodule`、`Module.finrank`、`Submodule.map`、`Submodule.mkQ`）。两者之间的翻译：



| 论文 | Lean |

|---|---|

| $\operatorname{row}\mathcal L$ | 子空间 $V\le E$（**作为参数给入**，不由矩阵构造）|

| $\operatorname{row}[L;CA;C]$ | $V\sqcup J$ |

| 秩 | `Module.finrank K ↥·` |

| $(\lambda I-A)\mathcal V$ | `Submodule.map (lam • 1 - A) V` |

| $\pi_J$ | `Submodule.mkQ J` |

| $S=Z\cap V$ | 假设 `S ≤ Z`、`S ≤ V`（**交的等式本身不作为假设**，见各条"差异"）|



> 因此："论文里的 $\operatorname{rank}[\cdots]$"在 Lean 里必须**先**换成 $V$、$J$ 两个子空间；

> 这个替换是**定义性**的（行空间 = 行向量张成的子空间），但没有在 Lean 里作为定理出现——

> 它是本项目所有 Lean 结果的**共同前提**。若以后要把矩阵真的接进来，需要补一条

> "矩阵的行空间 = 相应子空间"的桥。



---



## 1. `tools/lean/MyProof/`（`check_lean.sh` 的 19 个文件）



### Prelude.lean —— 共享维数引理（2026-11-01 起唯一一份证明）



- `finrank_inter_add_finrank_map_mkQ` — $\dim(T\sqcap B)+\dim(T/B)=\dim T$。**对应**：A.1 的全部内容；也是 A.3/F.1/H.1 等所有维数记账的基础。**差异**：无。

- `finrank_map_add_finrank_inf_ker` — $\dim(TV)+\dim(V\cap\ker T)=\dim V$（限制的秩-零化度）。**对应**：H.3（$d=0$）与 A.2 证明里的一步。**差异**：无。

- `finrank_pos_of_ne_bot` — 子模 $\ne\bot$ ⟹ 维数 $>0$。**对应**：维数工具（"非平凡 ⇒ 至少 1 维"）。**差异**：无。



### ProjW.lean —— 工具：$E=W\oplus J$ 的投影与压缩



> 源文件归档在 [proof/xw_decomposition/lean/MyProof/ProjW.lean](../../trash/lean_removed_2026-11-19/proof/xw_decomposition/lean/MyProof/ProjW.lean)。



- `projW` / `projJ` — 沿 $J$ / 沿 $W$ 的投影。**对应**：B.2/B.5 的 $\pi_W$。**差异**：无。

- `projW_add_projJ` — $x=\pi_Wx+\pi_Jx$。**对应**：分块分解。**差异**：无。

- `dualAnnihilator_apply_eq_projW` — $\psi\in J^{\perp}\Rightarrow\psi x=\psi(\pi_Wx)$。**对应**：**B.5 的"$\psi$ 只看 $W$"**。**差异**：无。

- `compression` — $T_W=\pi_W\circ A|_W$。**对应**：B.2/B.5 里的压缩。**差异**：无。

- `compression_sub_mem` — $Aw-T_Ww\in J$。**对应**：分块的误差项落在 $J$。**差异**：无。

- `dualAnnihilator_compression` — $\psi\in J^{\perp}\Rightarrow\psi(Aw)=\psi(T_Ww)$。**对应**：**B.2/B.5 的桥梁**。**差异**：无。

- `projW_of_mem_W` — $x\in W\Rightarrow\pi_Wx=x$。**对应**：投影在 $W$ 上不动。**差异**：无。

- `projW_of_mem_J` — $x\in J\Rightarrow\pi_Wx=0$。**对应**：投影在 $J$ 上为零（B.5 里 $\psi(j_0)=0$ 的代数版）。**差异**：无。



### DimArithmetic.lean —— H.2（维数算术）



> 源文件归档在 [proof/h2_dim_arithmetic/lean/MyProof/DimArithmetic.lean](../../trash/lean_removed_2026-11-19/proof/h2_dim_arithmetic/lean/MyProof/DimArithmetic.lean)。



- `no_truncation` — $\mathbb N$ 上 $(w-q-s)+(v-s)+2s=w-q+v$（$s+q\le w$、$s\le v$）。**对应**：H.2 的 $\mathbb N$ 读法前提。**差异**：无。

- `r_add_t` — $r+t=w-q+v-2s$。**对应**：H.2 第 1 式。**差异**：用 $\mathbb Z$ 陈述（无截断）；$\mathbb N$ 版本由 `no_truncation` 支撑。

- `square_iff` — $(r+t=w_m)\iff q=t$。**对应**：H.2 第 2 式（**方阵条件**）。**差异**：同 $\mathbb Z$ 写法。

- `m_iff_h` — $q=t$ 下 $m=r+t\iff h=w$。**对应**：H.2 第 3 式。**差异**：同 $\mathbb Z$ 写法；$q=t$ 作为假设。





### KronCoeff.lean —— B.6（$(5a)$ ⟹ 右最小指标全为 $0$）的**归纳核心**



> 源文件 [tools/lean/MyProof/KronCoeff.lean](../../trash/lean_removed_2026-11-19/tools/lean/MyProof/KronCoeff.lean)；纸面证明见 [proof/kron_null_module/theorem.md](../../proof/kron_null_module/theorem.md)（docs/02 B.6）。



- `RowContains` — $(5a)$ 的函数形式 `∀ v, L v = 0 → C v = 0 → CA v = 0 → LA v = 0`。**对应**：B.6 的假设 $(5a)$（行包含）。**差异**：从秩形式推出该核条件的翻译（$LA=XL+Y_1CA+Y_2C$）在纸面完成。

- `kron_coeff_chain_strong` — 系数方程 $Lv_k=LAv_{k+1}$、$Lv_d=0$、$Cv_k=CAv_k=0$ ⟹ 每个 $Lv_k=0$ 且 $LAv_k=0$（倒向归纳）。**对应**：B.6 证明的归纳核心。**差异**：不含多项式←→系数序列的翻译。

- `kron_coeff_chain` — 同上，取 $LAv_k=0$ 那一半。**对应**：B.6 的结论（系数全在 $\ker LA$）。**差异**：同上是归纳核心，不含 Kronecker 语言。

- `kron_coeff_const` — $d=0$ 特例：$Lw=Cw=CAw=0$ ⟹ $LAw=0$。**对应**：B.6 的 $\lambda^0$ 项。**差异**：无（单步）。

- `kron_coeff_mem_N` — 每一项属于 $N=\ker L\sqcap\ker LA\sqcap\ker C\sqcap\ker CA$。**对应**：B.6 的"系数全在常值零空间"。**差异**：不含"右零模由常值向量生成 ⟹ 右最小指标为 0"的 Kronecker 步骤。



**整体差异**：本文件把 B.6 的**归纳核心**机器化；多项式翻译与 Kronecker 结论在纸面。

故 B.6 的标注为 **[已证-纸面] + [Lean 内核] + [精确验证 150/150]**。



### KronFactor.lean —— B.7 与 descriptor 约化的**线性代数内核**



> 源文件 [tools/lean/MyProof/KronFactor.lean](../../trash/lean_removed_2026-11-19/tools/lean/MyProof/KronFactor.lean)；纸面证明见

> [proof/t4b_infinite_divisors/theorem.md](../../proof/t4b_infinite_divisors/theorem.md) 与

> [proof/descriptor_reduction/theorem.md](../../proof/descriptor_reduction/theorem.md)。



- `kron_block_factor` — $LA=XL+Y_1CA+Y_2C$ ⟹ $\lambda L-LA=(\lambda I-X)L-Y_1CA-Y_2C$。**对应**：B.7 第 1 步（$Q_L=P(\lambda)H$ 的第一块）。**差异**：不组装完整的三块矩阵等式（另两块是 $CA$、$C$，恒等），也不含 Smith 形部分。

- `descriptor_ker` — $\ker J=\ker H$ ⟹ $\ker(J\circ D)=\ker(H\circ D)$（线性映射形式）。**对应**：descriptor 约化引理中"$R(\lambda)y=0\iff Q'(\lambda)^{\mathsf T}y=0$"这一步（取 $D=D(\lambda)^{\mathsf T}$）。**差异**：矩阵实例化（$J$ 与 $H^{\mathsf T}$ 的左乘）未显式写出；$D$ 依赖 $\lambda$ 的版本未形式化。



**整体差异**：B.7 的局部 Smith 形/行列式因子 $\mu$-赋值仍未 Lean 化；故 docs/02 B.7 的标注是

**[已证-纸面] + [Lean 内核] + [精确验证 151/151]**。



### D1Core.lean —— D.1（$P$ 下界）的证明核心



> 源文件归档在 [proof/p_is_polynomial/lean/MyProof/D1Core.lean](../../trash/lean_removed_2026-11-19/proof/p_is_polynomial/lean/MyProof/D1Core.lean)。



- `d1_core` — $S\le W$、$AW\le W\sqcup B$ ⟹ $AS\sqcup(S\sqcup B)\le W\sqcup(S\sqcup B)$。**对应**：D.1 证明的包含关系。**差异**：无。

- `d1_dim` — 其维数版本。**对应**：$\dim\frac{AS+S+B}{S+B}\le\dim\frac{W+S+B}{S+B}$。**差异**：$P$ 的 $\min$ 定义未接（见 [archive/workspace_notes/questions_for_expert_2026-11-01.md](../../archive/workspace_notes/questions_for_expert_2026-11-01.md) §4）。

- `d1_lower_bound` — $\dim S+\dim(AS\sqcup S\sqcup B)\le\dim W+\dim(S\sqcup B)$（即 $\dim W\ge\dim S+\dim\frac{AS+S+B}{S+B}$）。**对应**：**D.1 的逐 $W$ 下界**（对每个可行 $W$ 成立）。**差异**：$P$（对可行 $W$ 取 $\min$）的包装未做——需非空性与 $\mathbb N$ 下确界的接口（见专家清单 §4）。

- `Feasible` — 可行子空间：$S\le W$ 且 $AW\le W\sqcup B$。**对应**：D.2 里 $\mathcal P$ 的约束集。**差异**：无。

- `P` — $P(A,B,S)=\min\{\dim W:\text{可行}\}$（$\mathbb N$ 下确界；空集取 0）。**对应**：$P(A,B,S)$。**差异**：空集情形需假设非空（见 `d1_P_lower_bound`）。

- `d1_P_lower_bound` — **D.1 的陈述**：可行集非空时 $\dim S+\dim(AS\sqcup S\sqcup B)\le P+\dim(S\sqcup B)$。**对应**：$P\ge\dim S+\dim\frac{AS+S+B}{S+B}$。**差异**：无（"可行集非空"是必要的建模条件，空集时 $P=0$）。



### PBH.lean —— B.2 的核心（PBH：可观测 ⟺ 无 ker D 里的特征向量）



> 源文件归档在 [proof/top_layer_observability/lean/MyProof/PBH.lean](../../trash/lean_removed_2026-11-19/proof/top_layer_observability/lean/MyProof/PBH.lean)。



- `Observable` — $(D,T)$ 可观测：$\bigcap_n\ker(DT^n)=0$。**对应**：B.2 里的"$(D_W,T_W)$ 可观测"。**差异**：无。

- `pbh_exists_eigenvector` — 代数闭域上端同态有特征向量（自包含复制）。**对应**：PBH 证明的引擎。**差异**：无。

- `pbh_iff` — 可观测 $\iff$ 不存在 $\ker D$ 里的特征向量。**对应**：**B.2 的第三步（PBH）**。**差异**：**弱于整条 B.2**——$Q_{\mathcal V}(\lambda)=\begin{pmatrix}-D_W^{\mathsf T}\\ \lambda I_d-T_W\end{pmatrix}$ 的分块形式（需 $X\oplus W$ 分解）未形式化。



- `pencil_pointwise`（**B2Block.lean**）— $\pi_W((\lambda I-A)x)=\lambda\pi_Wx-\pi_W(Ax)$。**对应**：铅笔的逐点线性性。**差异**：无。

- `block_on_J`（同文件）— $h\in\mathcal J$ 时 $\pi_W((\lambda I-A)h)=-\pi_W(Ah)$。**对应**：引理 1.1 的 **$-D_W^{\mathsf T}$ 块**。**差异**：坐标无关写法（无矩阵）。

- `block_on_W`（同文件）— $w\in W$ 时 $\pi_W((\lambda I-A)w)=\lambda w-\pi_W(Aw)$。**对应**：引理 1.1 的 **$\lambda I_d-T_W$ 块**。**差异**：同上。

- `block_on_W_compression`（同文件）— 同上去掉 $\pi_W(Aw)$ 写成 $T_Ww$。**对应**：引理 1.1 的 $W$-块（$T_W$ 形式）。**差异**：同上。



### CyclicVector.lean —— B.5（循环向量判据）



> 源文件归档在 [proof/cyclic_vector_criterion/lean/MyProof/CyclicVector.lean](../../trash/lean_removed_2026-11-19/proof/cyclic_vector_criterion/lean/MyProof/CyclicVector.lean)。



- `cyclicSpan` — 循环子空间 $\operatorname{span}\{T^kv\}$。**对应**：B.5 的 $\operatorname{span}\{v_W,v_WT_W,\dots\}$。**差异**：无。

- `mem_cyclicSpan_self` / `map_cyclicSpan_le` — $v$ 属于它；它 $T$-不变。**对应**：循环子空间的两个基本性质。**差异**：无。

- `isCyclic_iff` — $v$ 循环 $\iff$ 不存在含 $v$ 的真 $T$-不变子空间。**对应**：B.5 证明里的**事实 1**。**差异**：无。

- `ker_invariant_of_left_eigen` — $\psi\circ T=\lambda\psi$ ⟹ $\ker\psi$ 是 $T$-不变的。**对应**：**事实 2** 的前半。**差异**：无。

- `ker_ne_top_of_left_eigen` — $\psi\ne0$ ⟹ $\ker\psi\ne\top$。**对应**：**事实 2** 的真性一半。**差异**：无。

- `not_cyclic_of_left_eigen` — 存在这样的 $\psi$ 且 $\psi v=0$ ⟹ $v$ 不循环。**对应**：B.5 的 **"$(5b)$ 失败 ⟹ $v_W$ 不循环"** 方向。**差异**：无（单条内成立）。

- `exists_left_eigen_of_not_cyclic` — $v$ 不循环 ⟹ 存在 $\psi\ne0$、$\psi v=0$、$\psi\circ T=\lambda\psi$。**对应**：**反之方向**（把 $T^{\mathsf T}$ 限制到 $U^{\perp}$ 取特征向量）。**差异**：无（需 $[IsAlgClosed K]$）。

- `cyclic_iff_no_left_eigen` — $v$ 循环 $\iff$ 不存在以 $v$ 为根的非零左特征向量。**对应**：B.5 证明的**双向核心**。**差异**：**弱于整条 B.5**——"$(5b)\iff$ 左特征向量存在"的结构步骤（$\psi\in\mathcal J^{\perp}$、$\psi(j_0)=0$、$\psi|_W$ 左特征）仍纸面。

- `cyclic_exists_eigenvector` — 代数闭域上端同态有特征向量（自包含复制，同 `Eigen.exists_eigenvector`）。**对应**：上两条的引擎。**差异**：无。

- `exists_functional_of_rank_drop`（**CyclicStructural.lean**）— $(5b)$ 秩降 ⟹ 存在 $0\ne\psi\in J^{\perp}$ 使 $\psi(\lambda\ell-\ell A)=0$ 对一切 $\ell\in V$。**对应**：B.5 的"$(5b)$ 失败 ⟹ 见证泛函"。**差异**：无。

- `b5_structural`（同文件）— 该 $\psi$ ⟹ $\pi_W(j_0A)$ 不循环（$T_W$ 的）。**对应**：B.5 的结构步骤（$\psi(v_W)=0$、$\psi|_W$ 左特征）。**差异**：无（桥梁来自 `ProjW`）。

- `b5_five_b_fails_imp_not_cyclic`（同文件）— **合并**：$(5b)$ 秩降 ⟹ $v_W$ 不循环。**对应**：**B.5 的一个方向**（$(5b)$ 失败 $\Rightarrow$ 不循环；等价于"循环 $\Rightarrow(5b)$ 成立"）。**差异**：反向见 `b5_converse`；"循环"写成 `cyclicSpan = ⊤`（秩形式由 $\alpha$ 桥翻译）。

- `b5_converse`（同文件）— **反向**：$v_W$ 不循环 ⟹ 存在 $\lambda$ 使 $(5b)$ 秩降。**对应**：B.5 的另一方向（构造 $\tilde\psi=\psi\circ\pi_W$，再证 $MV+J\ne V+J$）。**差异**：需 $V=W\sqcup\operatorname{span}\{j_0\}$ 与 $(5a)$ 作假设；"循环"写成 `cyclicSpan = ⊤`。



### B4FullSpace.lean —— 独立辅助引理：对偶形式的零化子恒等式（**不作为 B.4 的覆盖**）



> 源文件归档在 [proof/b4_full_space/lean/MyProof/B4FullSpace.lean](../../trash/lean_removed_2026-11-19/proof/b4_full_space/lean/MyProof/B4FullSpace.lean)。



- `b4_finrank_iff` — $\dim(ME+J)=n\iff\ker M^{\mathsf T}\cap J^{\perp}=0$。**对应**：B.4 的第二、三步（对偶化 + 算 $^{\perp}$）。**差异**：无。

- `b4_iff_no_eigenvector` — 同上 $\iff$ 不存在 $0\ne\varphi\in J^{\perp}$ 使 $M^{\mathsf T}\varphi=0$。**对应**：**B.4 的陈述**（"$A^{\mathsf T}$ 在 $K$ 里无特征向量"，写成 $\varphi\circ(\lambda I-A)=0$）。**差异**：未把"特征向量"这一说法本身形式化；$A^{\mathsf T}\varphi=\lambda\varphi$ 与 $\varphi\circ(\lambda I-A)=0$ 是同一对象（`dualMap_apply` 为 `rfl`）。



### C1Closure.lean —— C.1（闭包族，唯一可行解是全空间）



- `aClosure` — $A$-不变闭包：所有"含 $J$ 且 $A$-不变"的子空间的交。**对应**：C.1 里的 $\langle\mathcal J\rangle_A$。**差异**：用"交"定义，不用迭代/极限（数学上等价）。

- `le_aClosure` — $J\le$ 闭包。**对应**：C.1 的定义性质。**差异**：无。

- `aClosure_le` — 闭包 $\le$ 任何含 $J$ 的 $A$-不变子空间。**对应**：C.1 的"最小性"。**差异**：无。

- `c1_of_closure_top` — $J\le V$、$AV\le V\sqcup J$、闭包 $=\top$ ⟹ $V=\top$。**对应**：**C.1 的陈述**（唯一可行解是 $\mathbb C^n$）。**差异**：无（$J\le V$ 由 $\operatorname{row}(L_0)=J$ 与 $L_0\subseteq\mathcal L$ 给出，作为假设）。

- `c1_finrank` — 同上，结论写成 $\dim V=\dim E$。**对应**：C.1 的 $q_{\min}=n$。**差异**：无。



### A3Bound.lean —— A.3（下界，维数部分）



- `a3_finrank_inter_add` — $\dim(T\sqcap B)+\dim(T/B)=\dim T$（自包含复制）。**对应**：维数工具。**差异**：无。

- `a3_rows` — $V_0\le V\Rightarrow\dim V_0\le\dim V$。**对应**：A.3 的 $q\ge r$。**差异**：无。

- `a3_epsilon` — $V_0\le V$、$V_0\ne V$ ⟹ $\dim V_0+1\le\dim V$。**对应**：A.3 的 $q\ge r+\varepsilon$（$q=r$ 时行空间相同）。**差异**：把"$L_0$ 非解"换成空间严格包含 $V_0\ne V$（纸面里由它推出）。

- `a3_rho` — $V\cap J\ne\bot$ ⟹ $\dim\pi_J(V)+1\le\dim V$。**对应**：A.3 的 $q\ge\rho+1$（$q=\rho+c$ 且 $c\ge1$）。**差异**：$c\ge1$ 作为**假设**（由 `Eigen.c_pos_of_five_b` 从 $(5b)$ 得到）；本文件不重复那个构造。

- `a3_lower_bound` — `a3_rows ∧ a3_rho` 的合取。**对应**：A.3 的维数部分。**差异**：不含 $\max(c_0,1)$ 里的 $c_0$（需要 $S$ 的 $A$-侧最小维数，属 A.4/$P$ 的语言）。



### Eigen.lean —— γ 桥（特征值/特征向量，支撑 A.2）



- `eig_finrank_inter_add` — $\dim(T\sqcap B)+\dim(T/B)=\dim T$（自包含复制）。**对应**：维数工具。**差异**：无。

- `eig_rank_nullity` — $\dim(TV)+\dim(V\cap\ker T)=\dim V$（自包含复制）。**对应**：A.2 证明里的秩-零化度。**差异**：无。

- `finrank_pos_of_ne_bot` — 子模块 $\ne\bot$ ⟹ 维数 $>0$。**对应**：维数工具。**差异**：无。

- `exists_eigenvector` — 代数闭域上端同态有特征向量。**对应**：A.2 证明的"代数闭域上有特征向量"一步（也服务 B.2/B.4）。**差异**：无（依赖 Mathlib 的 `Module.End.exists_eigenvalue`）。

- `finrank_lt_of_eigenvector_mod` — $V\cap J=0$、$AV\le V+J$、$0\ne v\in V$、$(\lambda I-A)v\in J$ ⟹ $(5b)$ 在 $\lambda$ 处**严格失败**。**对应**：**A.2 的数学内核**（两种情形：核非平凡 / 像与 $J$ 交非平凡，各掉 1 维）。**差异**：无（作为内核独立成条）。

- `c_pos_of_five_b` — $V\ne0$、$V\cap J=\bot$、$AV\le V\sqcup J$，且 $(5b)$ 对所有 $\lambda$ 成立 ⟹ `False`。**对应**：**A.2 的陈述**（$c\ge1$ 那半；$c\ge c_0$ 是 $S\subseteq V$ 的定义性事实）。**差异**：无（诱导端同态 $\varphi=e^{-1}\circ(\pi\circ A|_V)$ 已在本条内构造）。



### PencilEquivalence.lean —— B.1（商铅笔等价）



- `pe_finrank_inter_add` — $\dim(T\sqcap B)+\dim(T/B)=\dim T$（自包含复制）。**对应**：维数工具。**差异**：无。

- `finrank_sup_eq_add_quotient` — $\dim(W\sqcup J)=\dim J+\dim\pi_J(W)$。**对应**：B.1 的**全部内容**（把"堆叠矩阵的秩"与"商铅笔的秩"用同一个 $J$ 拆开）。**差异**：无。

- `pencil_rank_eq` — 逐 $\lambda$：$\dim(W_\lambda\sqcup J)=\dim(V\sqcup J)\iff\dim\pi(W_\lambda)=\dim\pi(V)$。**对应**：**B.1 的逐 $\lambda$ 版本**（$(5b)$ $\iff$ $\operatorname{rank}Q_{\mathcal V}(\lambda)=\rho$）。**差异**：$\operatorname{rank}$ 用 $\dim$ 行空间写（依据 `AlphaBridge.alpha_matrix_rank_row`）。

- `pencil_rank_forall` — 上面的 $\forall\lambda$ 版本。**对应**：**B.1 的原句**（"$\forall\lambda$"）。**差异**：同上。



### Isotropy.lean —— K.2（代数闭域上的各向同性）



- `exists_root_quadratic` — $a\ne0$ 时 $\exists t,\ at^2+bt+c=0$（代数闭域）。**对应**：K.2 证明里"二次式必有根"那一步。**差异**：无（需 $2\ne0$，$\mathbb C$ 满足）。

- `exists_ne_zero_quadraticMap_eq_zero` — $\dim V\ge2$ 的二次型有非零零点。**对应**：**K.2 的数学内核**（"$q|_K$ 各向同性"）。**差异**：**弱于整条 K.2**——没有把"Klein 二次型 $=0\iff$ 双向量可分解"形式化（需要 $\Lambda^2$ 与 Plücker 建模）。

- `K2_isotropic` — 限制到 $\ge2$ 维子空间仍有非零零点。**对应**：K.2 的"$K\subseteq\Lambda^2\mathbb C^4$、$\dim K\ge2$ ⟹ 存在 $0\ne p\in K$ 可分解"的**各向同性一半**。**差异**：同上（可分解性的刻画未形式化）。



### Rho0Layer.lean —— B.3（$\rho=0$ 层）



- `rho_zero_iff` — $\pi_J(V)=\bot\iff V\le J$。**对应**：B.3 的"$\rho=0\iff\mathcal V\subseteq\mathcal J$"。**差异**：无（$\rho$ 写成 $\dim\pi_J(V)$）。

- `five_a_of_le` — $V\le J$ 时，$(5a)\iff AV\le J$。**对应**：B.3 的"$(5a)\iff S\subseteq J$ 且 $SA\subseteq J$"（$V\le J$ 时 $S=V$，$S\subseteq J$ 自动）。**差异**：把 $S=V\cap J$ 显式化为 $V$；这是 $V\le J$ 的直接推论。

- `five_b_auto` — $V\le J$ 且 $AV\le J$ ⟹ 每个 $\lambda$ 有 $\dim((\lambda I-A)V+J)=\dim J$。**对应**：B.3 的"$(5b)$ 自动"。**差异**：无（"自动"的准确条件是 $(5a)$，即 $AV\le J$，这里作为假设写清）。



### AlphaBridge.lean —— α 桥（矩阵/秩语言 ↔ 子空间/维数语言）



- `alpha_colspace` — $[T\mid Z]$ 的列空间 $=\operatorname{range}T\sqcup Z$。**对应**：论文里 $\operatorname{rank}[L;CA;C]$ 的**列**空间读法（也是商铅笔第一步）。**差异**：只做列；行版本靠 `alpha_rank_dual` 转过去。

- `alpha_rank_dual` — $\dim\operatorname{range}M^{\mathsf T}=\dim\operatorname{range}M$。**对应**：α 桥的**核心**（行秩 = 列秩），使"堆叠矩阵的秩"可以等价地读成"行空间维数"。**差异**：无（直接是 Mathlib 的 `LinearMap.finrank_range_dualMap_eq_finrank_range`）。

- `alpha_row_mul` — $A^{\mathsf T}\ell=\ell\circ A$。**对应**：行向量乘 $A$ 的定义（$LA$ 的行 = $L$ 的行复合 $A$）。**差异**：无。

- `alpha_five_a` — $\dim(AV{+}V{+}J)=\dim(V{+}J)\iff AV\le V{+}J$。**对应**：$(5a)$ 的秩形式。**差异**：与 `RankBarrier.five_a_iff` **同陈述**（自包含复制，因为逐文件编译无 `.olean`）。

- `alpha_matrix_rank_row` — 真正矩阵的 $\operatorname{rank}A=\dim(\text{行空间})$。**对应**：论文 $\operatorname{rank}[\cdots]$ 的**行空间**读法（Mathlib 的 `Matrix.rank_eq_finrank_span_row`）。**差异**：无。

- `alpha_matrix_rank_col` — $\operatorname{rank}A=\dim(\text{列空间})$（转置的行空间）。**对应**：论文 $\operatorname{rank}[\cdots]$ 的**列空间**读法。**差异**：无。



### A3sem.lean —— 支撑 A.1（$q=\rho+c$）与 D.2 的维数记账



- `finrank_inter_add_finrank_map_mkQ` — $\dim(T\sqcap B)+\dim(T/B)=\dim T$。**对应**：A.1 的全部内容（正合列 $0\to V\cap J\to V\to\pi V\to0$）。**差异**：无。

- `finrank_map_mkQ` — $\dim(T/B)=\dim T-\dim(T\sqcap B)$。**对应**：A.1 的推论形式。**差异**：无。

- `finrank_TS_and_phi` — $k=\dim T_S$、$\ell=\dim\phi(S)$ 的统一公式。**对应**：A3 语义层（TASKS 的 $k,\ell$ 定义）。**差异**：无。

- `inf_sup_of_le` — 模律 $(P\sqcup S)\sqcap G=(P\sqcap G)\sqcup S$（$S\le G$）。**对应**：D.2 的格论步骤。**差异**：无。

- `dim_TS_inter_BS_add` — $\dim(T_S\cap B_S)+\dim\phi(S)=\dim T_S$（加性形式）。**对应**：TASKS 的语义恒等式。**差异**：右边的 $\phi(S)$ 用商-商表示，未与 $(A(S)+G)/G$ 显式等同（那步是纸面）。

- `dim_TS_inter_BS_sub` — 同一恒等式的减法形式。**对应**：同上。**差异**：同上。

- `finrank_quotQuot` — $\dim((M/S)/(G/S))=\dim(M/G)$。**对应**：D.2/语义恒等式的桥梁。**差异**：无。

- `finrank_map_mkQ_add` — $\dim(A(S)+G)-\dim G=\ell$。**对应**：A3 的 $\ell$ 语义形式（D-5）。**差异**：无。



### QuotientEquivalence.lean —— H.1（商等价）



> 源文件已归档到 [proof/quotient_equivalence/lean/MyProof/QuotientEquivalence.lean](../../trash/lean_removed_2026-11-19/proof/quotient_equivalence/lean/MyProof/QuotientEquivalence.lean)。



- `qe_finrank_inter_add` — 同 A3sem 的第一条（自包含复制）。**对应**：A.1/H.1 的公共维数工具。**差异**：无。

- `qe_colspace` — $(TV+Z)/S=TV/S+Z/S$。**对应**：H.1 证明的第 2 步。**差异**：无。

- `qe_finrank` — $\dim(TV+Z)=\dim S+\dim((TV+Z)/S)$（$S\le Z$）。**对应**：H.1 证明的第 4 步（$h_\Theta=s+r+t$）。**差异**：只要 $S\le Z$，不要求 $S=V\cap Z$。

- `qe_well_defined` — $T(S)\le Z$ ⟹ 换代表元只把 $T(v)$ 改动一个 $Z$ 的元素。**对应**：H.1 的 $(A)$ 假设那一步。**差异**：无。

- `qe_full` — $\dim(TV+Z)=\dim(V+Z)\iff\dim((TV+Z)/S)=\dim((V+Z)/S)$。**对应**：**H.1 的陈述本身**（两边都用 dim 写）。**差异**：把"$r+t$"写成 $\dim((V+Z)/S)$；二者的相等（$=r+t$）是纸面的维数记账。



### RankBarrier.lean —— F.1（秩屏障）



- `rb_finrank_inter_add` — 同 A3sem（自包含复制）。**对应**：维数工具。**差异**：无。

- `rank_barrier` — $\dim(VM+J)\le j+\dim\pi_J(\operatorname{range}M)$。**对应**：F.1 证明的**线性代数内核**。**差异**：**弱于 F.1**——没有 $(5b)$ 假设、没有 $\rho$。

- `five_a_iff` — $\dim(AV+V+J)=\dim(V+J)\iff AV\le V+J$。**对应**：$(5a)$ 的子空间形式（$\operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C]$）。**差异**：无（矩阵→子空间的翻译见 §0）。

- `rank_barrier_full` — $(5b)$ 成立（$\dim(VM+J)=\dim(V+J)$）⟹ $\rho\le\dim\pi_J(\operatorname{range}M)$。**对应**：**F.1 的陈述本身**。**差异**：$r(\lambda)$ 写成 $\dim\pi_J(\operatorname{range}M)$，未与"$\operatorname{rank}[\lambda I-A;C;CA]-j$"显式等同（纸面一步）。



### D0Boundary.lean —— H.3（$d=0$ 边界）



> 源文件已归档到 [proof/d0_boundary/lean/MyProof/D0Boundary.lean](../../trash/lean_removed_2026-11-19/proof/d0_boundary/lean/MyProof/D0Boundary.lean)。



- `d0_rank_nullity` — $\dim T(V)+\dim(V\cap\ker T)=\dim V$。**对应**：H.3 证明的秩-零化度。**差异**：无。

- `d0_rank_iff` — $\dim T(V)=\dim V\iff V\cap\ker T=\bot$。**对应**：H.3 的"$(S)\iff V\cap\ker(\lambda I-A)=0$"**逐 λ**。**差异**：无。

- `d0_forall` — 对**所有** $\lambda$ 的上式。**对应**：H.3 的 $\forall\lambda$ 版本。**差异**：未把"$\forall\lambda$ 无特征向量"这一说法形式化（那是 $\lambda$ 的定义层，属纸面）。



### 其余 MyProof 文件（支撑性/见证）



- `ker_caz_eq`（CoreLemma.lean）— $\ker(CAZ)=Z\cap\ker[C;CA]$。**对应**：dec_q_existsR 引理 1 的 $\ker$ 部分（G.1 的编码）。**差异**：无（该引理的另一半"左逆 ⟹ 单射"在 ExistsRLemmas）。

- `injective_of_left_inverse`（ExistsRLemmas.lean）— 左逆 ⟹ 单射。**对应**：G.1 引理 2 的一半。**差异**：不含量词消去/次数界。

- `finrank_range_eq_of_left_inverse`（ExistsRLemmas.lean）— 左逆 ⟹ $\operatorname{rank}P=\dim V$。**对应**：G.1 引理 2 的秩部分。**差异**：同上。

- `mapQ_not_injective`（A2.lean）— 若 $v\notin S$ 而 $Tv\in Z$，则 $S$ 上的商映射复合后不单射。**对应**：A2 命题 1（核障碍）的代数核心。**差异**：是命题的一步（不是"$\ker C\ne0$ ⟹ 不单射"的整句）。

- `polyOf_of_vanishing`（A2prop3.lean）— 非零次系数全为零 ⟹ 多项式退化为常数项。**对应**：A2 命题 3 的构造步。**差异**：是命题的一步。

- `polyOf_natDegree_pos`（A2prop3.lean）— 存在非零的 $\lambda^j$（$j\ge1$）系数 ⟹ 次数 $\ge1$。**对应**：A2 命题 3 的"非恒零 ⟹ 有根"那一半。**差异**：是命题的一步。

- `exists_eval_eq_zero`（A2root.lean）— $\mathbb C$ 上次数 $\ge1$ 的多项式有根。**对应**：A2 的代数核心。**差异**：无。

- `finrank_le_of_le`（A3.lean）— 子空间包含的维数单调性。**对应**：A3 的 $k\le r$ 剪枝。**差异**：无。

- `finrank_map_le_finrank`（A3.lean）— 像的维数 $\le$ 原像。**对应**：同上。**差异**：无。

- `range_mkQ_comp` / `ker_mkQ_comp` / `finrank_comap_subtype` / `finrank_inter_add_finrank_map_mkQ`（A3id.lean）— 商映射的像/核与 comap 的维数恒等式。**对应**：A3 的语义层工具。**差异**：无。

- `g4_real_zero` / `g4_complex_nonzero_witness` / `g4_counterexample`（G4.lean）— $\mathbb R$ 上无解但 $\mathbb C$ 上有解的显式例。**对应**：A2 §21 的 G4 反例（实/复差别）。**差异**：单实例见证。

- `range_coprod_eq`（QuotientPencil.lean）— $\operatorname{range}[T\mid Z]=\operatorname{range}T\sqcup Z$（列拼接的列空间 = 两个列空间之和）。**对应**：商铅笔恒等式第一步，也是"堆叠矩阵的列空间 = 子空间之和"这条**桥**的列版本。**差异**：只做列，不做行。

- `R17_A_witness` / `R17_Z_rank` / `R17_det_witness`（R17A.lean）— R17 见证的 $(A)$ 与秩。**对应**：支1 的 R17 见证。**差异**：单实例见证，不是定理。

- `cert_t2` / `cert_t1`（R17Cert.lean）— R17 的左逆证书（两个 $t$ 值）。**对应**：G.1 的实例验证。**差异**：单实例。

- `theoremC_endomorphism`（TheoremC.lean）— 代数闭域上每个自同态有特征值（$\exists\lambda$ 使 $\lambda I-B$ 不单射）。**对应**：Theorem C 的核心。**差异**：不含 Theorem C 的几何表述。

- `theoremD_dim_lt` / `theoremD_dim_eq`（TheoremD.lean）— 维数障碍两分支。**对应**：Theorem D（$q>t$）。**差异**：无。

- `theoremE`（TheoremE.lean）— $\operatorname{range}A$ 与 $\operatorname{range}\iota$ 不交、$A$ 单射 ⟹ $\forall\lambda$，$\lambda\iota-A$ 单射。**对应**：Theorem E。**差异**：这已是 Theorem E 的完整代数陈述。



---



## 2. `tools/lean/`（P 递归与 $(3,1)$ 层，`check_lean.sh` 第 2 组）



### PRecursion.lean —— D.2 的 $(\ge)$ 半



- `finrank_map_mkQ_add` — 同 A3sem 的 $\ell$ 公式（此文件内的独立副本）。**对应**：D.2 的维数工具。**差异**：无。

- `dim_lower_quotient` — $T\le U$、$T\le M$ ⟹ $\dim T+\dim\pi U\le\dim U$。**对应**：D.2 的 $(\ge)$ 半。**差异**：无。

- `bot_admissible` — 递归基。**对应**：D.2 的基例。**差异**：无。

- `admissible_image` — 可行性下降。**对应**：D.2 的 $(\ge)$ 方向。**差异**：无。

- `exists_section` — 商的线性截面。**对应**：D.2 的 $(\le)$ 构造。**差异**：无。

- `section_image` — 提升副本的维数/交。**对应**：D.2 的 $(\le)$ 构造。**差异**：无。



### PRecursionLift / Sigma / SigmaRange / SigmaPoint / Step / Lin / Induced



- `lift_admissible`（PRecursionLift.lean）— 构造步。**对应**：D.2 的 $(\le)$。**差异**：无。

- `exists_lift_of_range_le`（PRecursionSigma.lean）— $\sigma$ 存在性的通用核心。**对应**：D.2 的 $\sigma$ 存在性（区间包含形式）。**差异**：**弱于**D.2——未解包 level-1 可行性得到那个区间包含。

- `exists_mem_eq_mkQ_of_mem_sup` / `class_mem_range_of_mem_sup` / `range_le_of_forall_mem_sup`（PRecursionSigmaRange.lean）— 区间包含的实质。**对应**：$\sigma$ 存在性的最后一步。**差异**：无。

- `exists_correction_pointwise`（PRecursionSigmaPoint.lean）— $\sigma$ 的逐点校正。**对应**：$\sigma$ 存在性（逐点版）。**差异**：**弱于**线性版（线性化未做）。

- `step_le`（PRecursionStep.lean）— 一步递归的 $(\le)$ 半（无 $\sigma$）。**对应**：D.2 的 $(\le)$。**差异**：无 $\sigma$ 的自由度。

- `exists_sigma`（PRecursionLin.lean）— $\sigma$ 存在性（线性版，完整）。**对应**：D.2 的 $(\le)$ 的最后缺口。**差异**：无。

- `inducedQuotient_mkQ` / `inducedQuotient_map_T_le`（PRecursionInduced.lean）— level-1 映射良定义。**对应**：D.2 的 $\Phi'$。**差异**：无。



### PVal.lean —— $P$ 的形式化



- `Pval_exists` / `Pval_spec` / `Pval_min` / `Pval_le` — $P$ 的定义（`Nat.find`）与接口。**对应**：E.1 的 $P$（最小维数）。**差异**：**只在"可行集非空"的前提下**（`Nat.find` 的语义），空集情形是纸面。



### Perturbation.lean —— $(3,1)$ 层 C.2/C.3 的 Lean 支撑



- `perturb_eq_of_mem_ker` / `perturb_eigen_of_mem_ker` / `exists_eigenvector_forall_s` / `perturb2_eigen_of_mem_ker` — 秩一/秩二扰动在 $\ker\varphi$ 上不动。**对应**：C.2（$\mu=1$）与 C.3（$\mu=2$）的核心引理。**差异**：**只是引理**；判据本身（$T$ 有没有落在某子空间里的特征向量）仍是纸面。



### QuadraticMu2.lean —— C.3 的二次式



- `quad_det` — $\det[z,Dz]=a^2s+a(u-c)y-by^2$。**对应**：C.3 的显式二次式。**差异**：无。

- `quad_exists_ne_zero` — 该二次式不恒为零。**对应**：C.3 的"非恒零"一步。**差异**：无。



### Theorem12.lean —— C.4 的因式分解



- `smul_sub_mul_transpose` / `det_smul_sub_mul_transpose` / `det_smul_sub_mul_transpose_eq_zero` — $\det(\lambda\bullet U-UT^{\mathsf T})=\det U\cdot\det(\lambda I-T^{\mathsf T})$。**对应**：定理 12（$\mu=0$ 通道恒不可行）的因式分解。**差异**：定理 12 的其余步骤纸面。



---



## 3. 使用规则（写进 CLAUDE 之前先按这个执行）



1. 文档里写 `[Lean]` 时，**必须**同时给出本表里的声明名（不许只写文件名）；

2. 若某个命题只有"内核"被 Lean（本表"差异"列不写"无"），文档里**不得**把它写成 `[Lean]` 全称，

   只能写 `[Lean 内核]` 并注明差异；

3. 新增 Lean 声明 → 必须在本表加一行，否则 `audit_lean_statements.py` 报错。



### TypeII.lean —— B.9b（Type II 是空类）



- `typeII_rank_mono` —— `dim J ≤ dim (V ⊔ J)`（`J ≤ V ⊔ J` + `finrank` 单调）。**对应**：B.9b 的来源 1（$h\ge r_1$，行堆叠）。**差异**：无。

- `typeII_count` —— `r₁ ≤ h ⟹ q + r₁ - h ≤ q`（ℕ 截断减法，`omega`）。**对应**：B.9b 的计数核心。**差异**：无。

- `typeII_vacuous` —— `s = q ⟹ r₁ ≤ h ⟹ ¬(s < q + r₁ - h)`。**对应**：B.9b 的结论（Type II 永不发生）。**差异**：`h ≥ r₁` 与 `s = q` 作为假设给入（由上一行与行满秩提供）。

- `typeII_vacuous_geometric` —— `dim V + dim J - dim (V ⊔ J) ≤ dim V`。**对应**：B.9b 的维数版本。**差异**：同上。



### TypeIGeom.lean —— B.11b（Type I 的几何形式）



- `mkQ_map_inf_eq` —— `π((C ⊔ R) ⊓ W) = πR ⊓ πW`（`π = mkQ C`）。**对应**：B.11b 的核心引理。**差异**：不需要 `C ≤ W`（该假设只在读取维数时用）。

- `typeI_dim` —— `C ≤ W ⟹ dim ((C ⊔ R) ⊓ W) = dim C + dim (πR ⊓ πW)`。**对应**：B.11b 的维数形式。**差异**：无。

- `typeI_geometric` —— `C ≤ W ⟹ C ⊓ R = ⊥ ⟹ dim ((C ⊔ R) ⊔ W) + dim (πR ⊓ πW) = dim R + dim W`。**对应**：B.11b 的主形式（Type I ⟺ πR ⊓ πW = 0）。**差异**：写成等式而非"⟺"；"⟺"由等式直接读出。

- `B11_dim` —— `C ≤ W ⟹ C ⊓ R = ⊥ ⟹ dim ((C ⊔ R) ⊔ W) + (dim ((C ⊔ R) ⊓ W) - dim C) = dim R + dim W`。**对应**：B.11（$h=\dim(\mathcal Z^\perp+W)$ 与 $h=q+r_1-\delta$，$\delta\ge0$）。**差异**：$\delta$ 写成 `dim ((C⊔R)⊓W) - dim C`，非负性由 `C ≤ (C⊔R) ⊓ W` 保证。



### RowSpace.lean —— (α) 桥：矩阵行空间 ↔ 子空间语言



- `rowSpace` —— `Matrix.span_row` 在 Mathlib 里没有名字，本文件定义为 `Submodule.span K (Set.range A.row)`。**对应**：$\operatorname{row}M$ 的 Lean 实现。**差异**：无（纯定义）。

- `rank_eq_finrank_rowSpace` —— `A.rank = finrank (rowSpace A)`。**对应**：论文里"$\operatorname{rank}$"与"行空间维数"的翻译。**差异**：无（直接调用 `Matrix.rank_eq_finrank_span_row`）。

- `rowSpace_fromRows` —— $\operatorname{row}[A;B]=\operatorname{row}A\sqcup\operatorname{row}B$。**对应**：行堆叠的行空间并（(α) 桥的核心）。**差异**：无。

- `rank_le_rank_fromRows` —— $\operatorname{rank}B\le\operatorname{rank}[A;B]$。**对应**：B.9 的矩阵级前提 $r_1\le h$。**差异**：只给不等式（这正是 B.9 用到的方向），不给等式。

- `rank_le_rank_fromRows₂` —— $\operatorname{rank}[A;B;C]\ge\operatorname{rank}C$（三重）。**对应**：$[\mathcal L;CA;C]$ 的用法。**差异**：同上。



### A0Row.lean —— A.0 的行空间形式（用 (α) 桥）



- `five_a_row_iff` —— `rank [LA;L;CA;C] = rank [L;CA;C] ↔ row(LA) ≤ row[L;CA;C]`。**对应**：A.0 的第一步（$(5a)\iff\operatorname{row}(\mathcal LA)\subseteq\operatorname{row}\mathcal L+\mathcal J$）。**差异**：不含再往后的商形式 $\pi(\mathcal VA)\subseteq\pi(\mathcal V)$。

- `rank_eq_of_rowSpace_le` —— 行空间包含 $\Rightarrow$ 秩等式。**对应**：$(5a)$ 检查时常用的方向。**差异**：无（`five_a_row_iff` 的 `.mpr`）。



### LemmaA.lean —— B.15 的关键一步（避免性引理）



- `exists_witness_not_mem` —— 若 $V\cap K'=0$、$Z\le K'$ 非零、$\varphi:V\to K'$ 满射，则 $\exists x\in V$ 使 $\varphi x\in Z$ 且 $x\notin Z$。**对应**：B.15 的核心机制（单-$\lambda$ 证书 ⟹ 每个 $\mathcal Z\subseteq K$ 都有见证）。**差异**：只证抽象线性代数核；不含 $\varphi=(\lambda_0I-A)|_V$ 的实例化与分块直和的秩记账（后者仍是纸面 L1）。

- `exists_witness_not_mem'` —— 同上，另加 $x\ne0$。**对应**：B.13e/B.15 中"见证可取非零"的用法。**差异**：同 `exists_witness_not_mem`。



### LemmaB.lean —— B.15 的另一半（直和下秩可加）



- `finrank_range_prodMap` —— 对 $f:E_1\to F_1$、$g:E_2\to F_2$，有 $\dim\operatorname{range}(f\oplus g)=\dim\operatorname{range}f+\dim\operatorname{range}g$。**对应**：B.15 第 3 步"块对角增广的 $(5a)/(5b)$ 按块相加"的抽象核。**差异**：线性映射层面的直和，不含矩阵 `fromBlocks` 的桥（Mathlib 无 `Matrix.rank_fromBlocks`），也不含"$Q_{\mathcal L}$ 块对角"的矩阵实例化。

- `finrank_range_prodMap_le` —— 上述等式的 $\le$ 形式。**对应**：只需不等式的场合（如 $h$ 的上界）。**差异**：由等式直接得到。



### PsiImage.lean —— B.18e 第 3 条的内核（$P_w$ 的次数与根）



- `recX_natDegree_and_ne` —— 对 $c\ne0$，递归 $x_3=-c$、$x_{k+1}=X\,x_k-w_k$ 给出的多项式序列非零且次数恰为 $k$。**对应**：B.18d/B.18e 中"$x_k$ 的次数为 $k-3$、首项系数为 $-w_2\ne0$"这一步（故 $\deg P_w=n-2$）。**差异**：证明的是多项式次数记账；$P_w$ 的显式组装（把 $\sum a_{k-1}x_k$ 与 $-w_n$ 并进去）由纸面 + 精确验证 412/412 覆盖。

- `natDegree_X_mul_add_of_lt` —— 若 $\deg r<\deg(Xq)$ 且 $q\ne0$，则 $\deg(Xq+r)=\deg(Xq)$。**对应**：$P_w=\lambda x_n+(\text{低次项})$ 的次数等于 $n-2$。**差异**：只做加法的次数论证，不含 $\mathbb C$ 上的根存在。

- `exists_root_of_natDegree_eq_two` —— $\mathbb C$ 上次数为 $n-2$（$n\ge3$）的多项式必有根（`IsRoot`）。**对应**：B.18e 第 3 条的收尾"正次数 $\Rightarrow$ 有根（代数闭）"。**差异**：用 Mathlib 的 `Complex.exists_root`（代数基本定理），不涉及 $A$、$c$、$\ell$ 的具体数据。



### Criterion.lean —— B.16b / B.17 / B.13c 的内核



- `b16b_mapsTo` —— 设 $(5a)$ 取行空间形式（存在线性 `T` 使 `L ∘ A = T ∘ stack`，`stack x = (Lx, (CAx, Cx))`），则 `A(V ∩ 𝒵) ⊆ 𝒵`，其中 $V=\ker C\cap\ker(CA)$、$\mathcal Z=\ker C\cap\ker L$。**对应**：B.16b 的结论。**差异**：抽象线性映射层面；$A,C,\mathcal L$ 的矩阵实例化与"行堆叠的秩 ↔ 行空间包含"由 `RowSpace.lean` 另行提供。

- `permanent_kernel` —— $S\subseteq\ker J$、$S\subseteq\ker T$ ⟹ $S\subseteq\ker(T-cJ)$ 对一切 $c$。**对应**：B.17 第 1 条（永久核）。**差异**：只做 $T-cJ$ 这一形状，不含 $J,T$ 来自 $\mathcal L,A,\mathcal Z$ 的实例化。

- `ker_eq_iff` —— 若 $S\subseteq\ker N$，则 $\ker N=S\iff$ 每个核向量都落在 $S$ 里。**对应**：B.17 第 2 条的核形式。**差异**：**未**形式化"诱导映射 $W/S\to W$ 单射"这一商空间表述（等价，但需 Mathlib 商空间 API 的记账）。

- `b13c_factor` —— 若 $F\circ A=\Lambda\circ F$ 则 $F\circ(cI-A)=(cI-\Lambda)\circ F$。**对应**：B.13c 证明中的因子化一步。**差异**：只这一恒等式；"失败 $\iff\exists x\in V\setminus\mathcal Z,\lambda:(\lambda I-A)x\in\mathcal Z$"的组装未形式化。



### Dims.lean —— B.11c 与 B.18c 的记账内核



- `b11c_modular` —— $C_0\le S\Rightarrow C_0\sqcup(R\sqcap S)=(C_0\sqcup R)\sqcap S$（模格恒等式）。**对应**：B.11c 证明中"$\mathcal Z^\perp\cap S=C\oplus(R\cap S)$"这一步。**差异**：抽象子空间层面；$\mathcal Z^\perp=\operatorname{row}C\sqcup R$ 等实例化是纸面。

- `b11c_add` —— 若 $C_0\sqcap(R\sqcap S)=\bot$ 则 $\dim(C_0\sqcup(R\sqcap S))=\dim C_0+\dim(R\sqcap S)$。**对应**：B.11c 的维数相加（$h=s_0+q-\dim(R\cap S)$ 的最后一步）。**差异**：只做这一加法定理，不含 $h,s_0,q$ 的具体记号。

- `b18c_annihilate` —— $Cx=0$、$C(Ax)=0$ ⟹ $C((cI-A)x)=0$。**对应**：B.18c 第 1 条（坏像落在 $\ker C$ 内）。**差异**：只这一恒等式；"$\operatorname{im}\psi\subseteq\ker c$"的集合表述与后续 $d=1$ 判据仍是纸面 + 精确验证。



### Logic.lean —— B.11d 与 B.18e 的逻辑骨架



- `typeI_kills` —— 若 $R(s)\le c$ 对一切 $s$ 且 $c<h$，则"$R(s)=h$ 对一切 $s$"不成立。**对应**：Type I（$h>q+r_1$）杀掉 $(5b)$ 的算术内核（$c=q+r_1$）。**差异**：只做算术；"$\operatorname{rank}[\lambda\mathcal L-\mathcal LA;CA;C]\le q+r_1$"这个矩阵秩不等式是纸面。

- `b11d_css` —— 给定"Type I 杀掉 $(5b)$"与 CSS 两条前提，则 $\exists i,\ (5a)\wedge(5b)\iff\exists i,\ (5a)\wedge\text{计数侧}$。**对应**：B.11d。**差异**：纯逻辑骨架，两条前提作为假设；不含秩的具体计算。

- `b18e_family` —— 给定"$z\in V$ ⟹ 不可容许"与"$z\notin V$ ⟹ $z\in\operatorname{im}\psi$ ⟹ $\neg(5b)$"与"$z\notin V$ ⟹ $z\in\operatorname{im}\psi$"，则该阶不存在可容许且满足 $(5b)$ 的候选。**对应**：B.18e 的整族不可行结论。**差异**：纯逻辑骨架；三件数学内容（B.18b/B.18c/B.18d）作为假设。



### B22.lean —— B.22（等号障碍）的两块基石



- `det_blockIdentity` —— $\det\begin{pmatrix}A&-B\\0&1\end{pmatrix}=\det A$。**对应**：B.22 第 3 步块因子化中的方块 $P(\lambda)=\begin{bmatrix}\lambda I_q-K_1&-K_2\\0&I_{r_1}\end{bmatrix}$ 的行列式 $=\det(\lambda I_q-K_1)$。**差异**：只做那个方块的行列式；$H_0$ 满行秩 ⟹ 秩不变、$K$ 的存在性、以及"秩化成方块秩"三步是纸面 + 精确验证。

- `exists_root_of_pos_natDegree` —— $\mathbb C$ 上正次数多项式有根（`Complex.exists_root`）。**对应**：B.22 第 5 步"$q\ge1$ 时 $\det(\lambda I_q-K_1)$ 有根"。**差异**：不涉及 $K_1$ 的具体来源。

- `exists_root_of_monic` —— 首一正次数多项式有根。**对应**：同上，带首一性。**差异**：首一性未被使用（保留以便与论文表述对齐）。



### WorkA.lean —— B.23 的秩公式（专家 §5 形式化优先级第 1 项）



- `kerRestrictEquiv` —— 限制映射的核与交的线性同构：$\ker(P|_S)\simeq S\cap\ker P$。**对应**：B.23 秩公式证明中的对齐步骤。**差异**：抽象的线性映射层面。

- `finrank_range_comp` —— $\dim\operatorname{range}(P\circ H)+\dim(\ker P\sqcap\operatorname{range}H)=\dim\operatorname{range}H$，即 $\operatorname{rank}(PH)=\operatorname{rank}H-\dim(\ker P\cap\operatorname{im}H)$。**对应**：B.23 的核心秩公式。**差异**：不含 $Q_{\mathcal L},H_0,K_1,K_2$ 的矩阵实例化与 $\lambda$-依赖运算。



### B27.lean —— B.27 情形 B 的代数内核



- `krylov_le` —— 若 $c\in S$ 且 $S$ 对"右乘 $A$"封闭，则 $\operatorname{span}\{cA^k:k\ge0\}\le S$。**对应**：B.27 情形 B 的归纳步骤。**差异**：只做对偶侧的线性子空间记账；行空间 $\mathcal V=\operatorname{row}[\mathcal L;c]$ 的实例化与"$(5a)\Rightarrow$ 右乘 $A$ 封闭"（B.26 第 3 条）是纸面 + 精确验证。

- `eq_top_of_krylov` —— 若 Krylov 张成 $=\top$（可观测性），则 $S=\top$。**对应**：B.27 情形 B 得出 $\mathcal V=\top$ 的那一步。**差异**：同上。

- `no_caseB` —— $d=q+1$、$d=n$、$q+2\le n$ 矛盾。**对应**：B.27 情形 B 的维数矛盾。**差异**：纯算术。



### B313233.lean —— B.31/B.32/B.33 的内核



- `logic` / `necessary`（命名空间 `B31`） —— 若 $\delta\le\rho$ 且两个极端层（$\delta=\rho$、$\delta=0$）都不可行，则可行时 $1\le\delta<\rho$。**对应**：B.31 的逻辑骨架。**差异**：$\delta\le\rho$ 与两层的不可行性作为假设；行空间/零化子层面的推导是纸面。

- `no_intermediate`（命名空间 `B32`） —— $\rho\le1$ 时不存在整数 $\delta$ 满足 $1\le\delta<\rho$。**对应**：B.32 的"无中间层"。**差异**：纯算术。

- `terminal_only`（命名空间 `B32`） —— 若所有次终端阶都不可行且终阶可行，则最小可行阶 $=Q$（`IsLeast`）。**对应**：B.32 的"终端唯一"。**差异**：把"次终端不可行"作为假设；B.31 ⟹ 该假设的那一步是纸面。

- `dim_quotient`（命名空间 `B33`） —— $\dim(V/S)=\dim V-\dim S$（用 `Submodule.finrank_quotient_add_finrank`）。**对应**：B.33 的维数内核。**差异**：只做商维数公式。

- `dim_arith`（命名空间 `B33`） —— 由 $\dim V=n-r_1$、$\dim S=n-h$、$h=q+p+\delta$、$r_1=p+\rho$ 得 $\dim V-\dim S=q+\delta-\rho$。**对应**：B.33 的算术。**差异**：纯算术。

### B21_B13f.lean —— B.21（$s=n-h$）的维数内核

- `dim_inf_ker`（命名空间 `B21`）—— 对 $f:X\to Y$、$g:X\to Z$：$\dim(\ker f\cap\ker g)=\dim X-\dim\operatorname{range}(f\times g)$。**对应**：B.21 的 $s=n-h$。**差异**：见下条。
  **对应**：B.21 的 $s=n-h$（取 $f=[C;CA]$、$g=\mathcal L$、$h=\operatorname{rank}(f\times g)$）。
  **差异**：矩阵/行空间层面（$h=\operatorname{rank}[\mathcal L;CA;C]$、$S=V\cap\mathcal Z$）的翻译是纸面。
- B.13f 的代数步（$\mathbb C$ 上首项非零二次多项式必有根）**未单独立内核**：它是 $\mathbb C$ 代数闭性的直接实例
  （`Complex.exists_root` / `IsAlgClosed`），无须另证。

### RowSpaceLayer.lean —— B.9(a)/B.20/B.18(a)/B.28(a) 的子空间内核

- `finrank_sup_lt_of_inf_ne_bot` —— $V\cap W\ne\bot\Rightarrow\dim(V\sqcup W)<\dim V+\dim W$。**对应**：B.9（a）（"$h<q+r_1$"）。**差异**：矩阵/行空间翻译是纸面（由 `rank_eq_finrank_rowSpace` + `rowSpace_fromRows` 完成）。
- `inf_bot_of_finrank_sup_eq` —— 等号 $\Rightarrow V\cap W=\bot$（上条的逆否）。**对应**：B.9（d）（原 B.20）。**差异**：同上。
- `finrank_range_prod_le` —— $[C;CA]$ 的秩 $\le 2p$。**对应**：B.18（a）里的 $r_1\le2p$。**差异**：只证维数上界，不涉及具体矩阵。
- `map_sup_le_iff` —— $V=U\sqcup R$、$\operatorname{row}(AR)\subseteq W$ 时，$U\cdot A\subseteq V+W\iff V\cdot A\subseteq V+W$。**对应**：B.28（a）的分裂等价（亦即 B.26(3) 的核心）。**差异**：行空间 ↔ 子空间的翻译是纸面。


### MatrixBridge.lean —— 矩阵乘法与行空间的桥（B.9/B.20 的字面矩阵版）

- `rowMulLin` —— $x\mapsto x\cdot B$ 的线性映射。**对应**：B.1/B.9 等把 $[\lambda L-LA;CA;C]$ 的行空间写成映射像时用。**差异**：工具定义。
- `rowMulLin_apply` —— 定义展开。**对应**：工具。**差异**：无。
- `rowMulLin_sub` / `rowMulLin_add` —— 与矩阵加减相容。**对应**：工具（拼铅笔用）。**差异**：无。
- `rowSpace_mul` —— $\operatorname{rowSpace}(L\cdot M)=(x\mapsto x\cdot M)(\operatorname{rowSpace}L)$。**对应**：B.1/B.9 的矩阵—子空间桥的核心。**差异**：无（这是恒等式本身）。
- `rank_fromRows_lt_of_inf_ne_bot` —— $\operatorname{rowSpace}L\cap\operatorname{rowSpace}[CA;C]\ne\bot\Rightarrow\operatorname{rank}[L;CA;C]<\operatorname{rank}L+\operatorname{rank}[CA;C]$。**对应**：B.9（a）的**字面矩阵**版。**差异**：陈述里出现的是 `rank`/`fromRows`，与论文写法一致；无剩余差异。
- `inf_bot_of_rank_fromRows_eq` —— 等号 $\Rightarrow$ 行空间交为零。**对应**：B.9（d）的字面矩阵版。**差异**：无。
- `rowMulLin_smul` / `rowMulLin_one` —— $x\mapsto x\cdot(cB)=c(x\cdot B)$、$x\mapsto x\cdot 1=x$。**对应**：把 $\operatorname{rowMulLin}(\lambda\cdot1-A)$ 化成 $\lambda\cdot1-\operatorname{rowMulLin}A$ 的前置。**差异**：无。


### F1_Matrix.lean —— F.1 矩阵形式的前置

- `mul_pencil` —— $L(\lambda\cdot1-A)=\lambda L-LA$。**对应**：F.1 矩阵版的前置。**差异**：无。
- `rowSpace_one` —— $\operatorname{rowSpace}1=\top$。**对应**：$\operatorname{rowSpace}M=\operatorname{range}(x\mapsto xM)$ 的前置。**差异**：无。
- `rowSpace_eq_range` —— $\operatorname{rowSpace}M=\operatorname{range}(x\mapsto xM)$。**对应**：F.1 矩阵版。**差异**：无。
- `finrank_sup_eq_add_quotient` —— $\dim(W\sqcup J)=\dim J+\dim\pi_J(W)$。**对应**：F.1/B.1 的维数换算。**差异**：无。（F.1 主体的秩不等式尚未拼装，见该文件 TODO。）


### B12_Observability.lean —— B.12 的判据（Cayley–Hamilton）

- `krylovMap` / `krylovMap_apply` —— 观测矩阵的算子形式 $x\mapsto(i\mapsto D(T^ix))_{i<\dim}$。**对应**：B.12 的"观测矩阵"对象。**差异**：工具定义 + 展开。
- `pow_finrank_eq_neg_sum` —— $T^q=-\sum_{i<q}c_iT^i$（特征多项式展开）。**对应**：B.12 的关键一步。**差异**：无。
- `observable_iff_krylov` —— 可观测 $\iff$ 前 $q$ 步 Krylov 核为零。**对应**：B.12 的第二、三段等价。**差异**：与 $\ker[C;CA]$ 的归约（把 $\mathcal L$ 的铅笔翻成 $(E,\Lambda)$）是纸面。
- `observable_iff_rank_krylov` —— 可观测 $\iff$ 观测矩阵满秩。**对应**：B.12 的秩形式。**差异**：同上。


### B25_Family.lean —— B.25 的二元判据（gcd 与公共根）

- `gcd_eval_eq_zero_of_common_root` —— 公共根 $\Rightarrow\gcd$ 在该点为零。**对应**：B.25 的一支。**差异**：无。
- `no_common_root_of_gcd_ne_zero` —— 上条的逆否。**对应**：B.25。**差异**：无。
- `gcd_is_const_of_no_common_root` —— 无公共根 $\Rightarrow\deg\gcd=0$。**对应**：B.25 的另一支。**差异**：无。
- `no_common_root_iff_gcd_const` —— 无公共根 $\iff\gcd$ 是非零常数。**对应**：B.25 的二元完整判据。**差异**：推广到"极大子式的 gcd"（多子式）与矩阵秩的翻译仍是纸面。

### B13Fiber.lean —— B.13a 纤维二分的线性代数内核（辅助引理，F1）

- `scalar_unique_of_ne_zero` —— $w\ne0$ 且 $w=c\,z=d\,z$ 则 $c=d$。**对应**：B.13a 引理 2（$\mathcal B$ 之外纤维至多一点）。**差异**：只给比例唯一性；"纤维确实存在"还需 $Mx\in K$ 的条件。
- `zero_vec_proportional` —— $0=0\cdot z$。**对应**：B.13a 引理 3（$\mathcal B$ 之上纤维是整个 $\mathbb P(K)$）。**差异**：仅代数内核；射影化是纸面。
- `proportional_set_subsingleton` —— $\{c: w=c\,z\}$ 在 $w\ne0$ 时是 subsingleton。**对应**：同上（纤维唯一性）。**差异**：无。

### B24Phi.lean —— B.24 偏算子 $\Phi$ 的良定义（商泛性质，F2）

- `b24_factor` —— $\ker\pi\le\ker\sigma$ ⟹ $\sigma$ 沿 $\pi$ 在商上因子化：存在线性 $\Phi:E/\ker\pi\to F'$ 使 $\Phi([x])=\sigma x$。**对应**：B.24 的"$\Phi(xL)=x\Lambda$ 良定义"。**差异**：把具体 $\pi=(\cdot)L$、$\sigma=(\cdot)\Lambda$ 的实例化留给纸面。
- `b24_factor_unique` —— 该 $\Phi$ 唯一。**对应**：B.24 良定义性的唯一性部分。**差异**：无。
- `b24_no_full_row_rank` —— 因子化**不要求** $\pi$ 满射（即不要求 $L$ 行满秩）。**对应**：B.24 与旧版的关键差别（旧版要求满行秩）。**差异**：无。

### B37Domain.lean —— 专家第五轮里程碑 L2/L3/L6（域 $W_K$ 的代数内核）

- `l2_factor` —— $\ker(L|_{K})\le\ker(T|_{K})$ ⟹ $T|_K$ 沿 $L|_K$ 因子化：存在 $\Phi:K/\ker(L|_K)\to F$ 使 $\Phi([v])=Tv$。**对应**：L2（$\Phi_K$ 良定义，商形式）。**差异**：与 $\operatorname{range}(L|_K)=W_K$ 的同一化仍用纸面（商 vs 像）。
- `l3_unique` —— 该 $\Phi$ 唯一。**对应**：L3（与 $\Lambda$ 选法无关）。**差异**：无。
- `l6_finrank` —— $\dim(LK)=\dim K-\dim\ker(L|_K)$。**对应**：L6（维数公式）。**差异**：无。

### Theorems/Factor.lean —— $(5a)$ 的因子化（L1；命题级）

- `decomp_iff_ker` —— $(\exists\Lambda,G_0,G_1:\ LA=\Lambda L+G_0C+G_1CA)\iff\ker(L,C,CA)\subseteq\ker(LA)$。**对应**：$(5a)$ 的 $\Lambda$-分解形式（B.17 的 $(\ast)$）与专家第五轮里程碑 **L1**。**差异**：无（矩阵实例化由 `alpha_matrix_rank_row` 等在纸面完成）。
- `ker_tuple_le_of_decomp` / `decomp_of_ker_tuple_le` —— 两个方向（后者用 `exists_comp_eq_of_ker_le`，即专家建议的 factor-and-extend 引理）。**对应**：同上，拆分版。**差异**：无。

> 该文件其余 5 条声明为工具（`tuple`、`inj1/2/3`、`tuple_eq`），按 `tools/lean/EXEMPT_AUXILIARY.md` 文件级豁免，不逐条登记。

### B24L4.lean —— L4：(12) 的集合层（$\ker Q$ 与 $\ker P_K$ 的纤维关系）

- `l4_ker_fiber` —— $\ker(T-\lambda L)\cap K=K\cap L^{-1}(\ker(\Phi-\lambda\,\mathrm{id}))$，条件是 $\Phi(Lv)=Tv$（$v\in K$）。**出处**：B.24 的 (12)（[proof/B.24](../../proof/B.24/README.md)）与专家第六轮 §6.1。**意义**：把"$v$ 是 $Q_{\mathcal L}$ 在 $\lambda$ 处的核向量"精确化为"$Lv$ 是 $\Phi$ 的 $\lambda$-特征向量"，这是 Theorem A 判据的集合层内容。
- `l4_finrank` —— 两边的 $\dim$ 相等（随集合层）。**出处**：B.24 的 (12)（[proof/B.24](../../proof/B.24/README.md)）。**意义**：维数版的 (12) 的左半。

> 说明：**(12) 的"$\dim\ker Q=\dim D+\dim\ker P_K$"** 中"$+\dim D$"这一步由 $v\mapsto Lv$ 的秩-零化度给出，本模块只形式化了集合层；该加法仍在纸面（B.24 直接证明）。

### B36FiveA.lean —— 专家恒等式：$(5a)$ 的核形式

- `ker_inf_le_iff_restrict` —— $K\cap\ker L\le\ker T\iff\ker(L|_K)\le\ker(T|_K)$。**出处**：专家第九轮答复 §3 的恒等式 $(5a)\iff\ker H\subseteq\ker H_A$（[proof/B.24](../../proof/B.24/README.md)）。**意义**：把 $(5a)$ 化成"限制映射的核包含"，是 RAZE 归约里把 $(5a)$ 写成 $\ker H\subseteq\ker H_A$ 的依据。
- `ker_inf_le_of_injective` —— $L|_K$ 单射 ⟹ 中介条件自动成立（即 $H$ 满列秩 ⟹ $(5a)$ 自动）。**出处**：B.24 的 $(5a)$ 恒等式推论（专家第九轮 §3，[proof/B.24](../../proof/B.24/README.md)）。**意义**：说明满秩层上 $(5a)$ 免费。

### LayerAllBad.lean —— 约束层全坏（attempts/103）的秩内核

- `rank_le_one_of_rows_zero` —— 3×3 矩阵若每行前两个坐标为 0（即每行都是 $E_3$ 的倍数），则秩 $\le1$。**对应**：attempts/103 的定理——在 $\lambda_0=-1$（$S_1$）或 $+1$（$S_2$）处，$\lambda_0H-H_A$ 的三行全落进 $\operatorname{span}\{E_3\}$，故秩 $\le1<2$，整层全坏。**差异**：只做秩不等式；从相容方程与参数化到行形式的推导由纸面 + `tools/verification/constrained_all_bad_check.py` 覆盖。
- `rowForm_rank_le` —— 只有第三列可能非零的 3×3 行形式的秩 $\le1$。**对应**：同上，具体行形式（$\lambda_0$ 处的矩阵形状）。**差异**：同上；不涉及具体参数值。

## B.26 $B_{u,v}$ 秩恒等式（2026-11-08）

- `ker_mkQ_comp_domRestrict` —— 映射 $U\to E/U$、$x\mapsto Ax+U$ 的核等于 $U\cap A^{-1}U$（作为 $U$ 的子模）。**出处**：[attempts/171](../../workspace/q1_false/c_stratification/attempts/171_Buv_rank_strata.md) 与专家 60 号 §4.1（$\ker\varphi_U=U\cap A^{-1}U$）。**意义**：$B_{u,v}$ 秩层的核恒等式。
- `finrank_range_mkQ_comp_domRestrict` —— $\dim\operatorname{range}\varphi=\dim U-\dim(U\cap A^{-1}U)$（有限维）。**出处**：[attempts/171](../../workspace/q1_false/c_stratification/attempts/171_Buv_rank_strata.md) 与专家 60 号 §4.1（$\operatorname{rank}\varphi_U=u-\dim(U\cap A^{-1}U)$）。**意义**：$B_{u,v}=\{\operatorname{rank}\varphi=u-v\}$ 的维数形式。
- `mem_range_dualMap_iff` —— $\varphi\in\operatorname{range}f^{\mathsf T}\iff\varphi|_{\ker f}=0$（行空间判据）。**出处**：[attempts/165](../../workspace/q1_false/c_stratification/attempts/165_c2_forced_plane_criterion.md)、[attempts/172](../../workspace/q1_false/decision_algorithms/attempts/172_forced_certificates.md) 与专家 60 号 §1.1。**意义**：forced-plane 判据“$e_b\in\operatorname{rowspace}(\mathrm{Des})$”的 Lean 根据。

## B.27 pair-lift 与不变子空间（2026-11-09）

- `pairLift_annihilator` —— $(V+AV)^\perp=V^\perp\cap(AV)^\perp$（即 $\mathcal L_V=(V+AV)^\perp$）。**出处**：[attempts/201](../../workspace/q1_true/multiplication_gate/attempts/201_pair_lift_theorem.md)。**意义**：pair-lift 定理的 Lean 内核。
- `invariant_subspace_has_eigenvector` —— 代数闭域上有限维空间里，非零不变子空间含特征向量。**出处**：[attempts/205](../../workspace/q1_true/multiplication_gate/attempts/205_AinvK0_impossible.md)。**意义**：205 否定定理的关键一步。

## B.24 谱维数上界（2026-11-09）

- `pairMap` —— 配对映射 $x\mapsto(fx,gx)$。**出处**：[attempts/247](../../workspace/q1_true/multiplication_gate/attempts/247_fixed_qc_tractable.md) 与 74 号答复的 $\kappa_{\rm obs}$ 定义。**意义**：$\Delta R\mapsto(\Delta RN,\Delta RAN)$ 的抽象形式。
- `pairMap_apply` —— `pairMap f g x = (f x, g x)`（定义展开）。**出处**：[attempts/247](../../workspace/q1_true/multiplication_gate/attempts/247_fixed_qc_tractable.md)。
- `ker_pairMap` —— $\ker(\text{pairMap }f g)=\ker f\cap\ker g$。**出处**：[attempts/248](../../workspace/q1_true/multiplication_gate/attempts/248_kappa_not_enough.md)；[attempts/248](../../workspace/q1_true/multiplication_gate/attempts/248_kappa_not_enough.md)。**意义**：不可见子空间 $\ker N\cap\ker(AN)$。
- `finrank_ker_add_finrank_range` —— 秩-零化度加性形式。**出处**：标准线性代数；[attempts/247](../../workspace/q1_true/multiplication_gate/attempts/247_fixed_qc_tractable.md)。
- `finrank_ker_eq_finrank_sub_finrank_range` —— 秩-零化度减法形式。**出处**：[attempts/247](../../workspace/q1_true/multiplication_gate/attempts/247_fixed_qc_tractable.md)。
- `finrank_ker_pairMap` —— 配对映射的核维数 $=\dim E-\operatorname{rank}$。**出处**：[attempts/247](../../workspace/q1_true/multiplication_gate/attempts/247_fixed_qc_tractable.md)、[attempts/248](../../workspace/q1_true/multiplication_gate/attempts/248_kappa_not_enough.md)。**意义**：每行核维数 $n-\operatorname{rank}[N,AN]$ 的 Lean 内核。
- `finrank_ker_pairMap_add_finrank_range` —— 配对映射的加性秩-零化度。**出处**：[attempts/247](../../workspace/q1_true/multiplication_gate/attempts/247_fixed_qc_tractable.md)。
- `finrank_ker_inf_add_finrank_range_pairMap` —— $\dim(\ker f\cap\ker g)+\operatorname{rank}(\text{pairMap})= \dim E$。**出处**：[attempts/247](../../workspace/q1_true/multiplication_gate/attempts/247_fixed_qc_tractable.md)。
- `kappaObs` —— 定义 $\kappa_{\rm obs}=r\operatorname{rank}[N,AN]$。**出处**：[attempts/247](../../workspace/q1_true/multiplication_gate/attempts/247_fixed_qc_tractable.md)。
- `kappaObs_def` / `kappaObs_eq_row_count` —— 定义展开。**出处**：[attempts/247](../../workspace/q1_true/multiplication_gate/attempts/247_fixed_qc_tractable.md)。
- `range_eq_rowSpan` —— 行空间等于行映射 $u\mapsto uM$ 的像。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节（秩压缩恒等式与 Statements 1–4）；`Matrix.range_mulVecLin`（Mathlib）。
- `range_le_rowSpan` —— 行映射的像落在行空间内。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节（秩压缩恒等式与 Statements 1–4）；`Matrix.range_mulVecLin`（Mathlib）。
- `rowSpan_le_range` —— 行空间的每个向量都是某个 $u$ 的像。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节（秩压缩恒等式与 Statements 1–4）；可实现性那一步。
- `rowSpan_fromRows_left` —— **沙包**：$\operatorname{row}L_0\le\operatorname{row}[L_0;R]$。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节（秩压缩恒等式与 Statements 1–4），Statements 1–4 的第 1 条。
- `range_restrictToKer` —— $g$ 在 $\ker f$ 上的限制的像等于 $\ker f$ 在 $g$ 下的像。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节（秩压缩恒等式与 Statements 1–4），秩压缩恒等式证明的第一步。
- `finrank_range_prod` —— 压缩恒等式的抽象形式：$\dim\operatorname{range}(f\times g)=\dim\operatorname{range}f+\dim\operatorname{map}g(\ker f)$。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节（$\operatorname{rank}[J;M]=\operatorname{rank}J+\operatorname{rank}(MN_J)$）；论文 §V 的压缩步。**意义**：论文每个压缩步都经过它。
- `mem_rowSpan_iff_exists_vecMul` —— 可实现性：行空间里每个向量都是某个自由行的像。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节（Statements 1–4 的第 2 条）。
- `finrank_sup_eq_iff_le` —— $\dim(S\sqcup T)=\dim S\iff T\le S$。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节（$\operatorname{rank}[H_A;H]=\operatorname{rank}H\iff\operatorname{row}H_A\subseteq\operatorname{row}H$）；论文 Lemma 1。**意义**：把 (5a) 化成行包含。

- `finrank_sup_eq_iff_not_le` —— 上一条的否定形式。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节。

> 保真修正（2026-11-11）：`Q1Pencil` 与 `Q1Step3` 的铅笔改为 `z • H - H_A` 且 **H 与 H_A 相互独立**。原写法用 `z • H - H * A`，隐含 $K_0=\ker[C;CA]$ 在 $A$ 下不变；但 $Cx=CAx=0$ 推不出 $CA^2x=0$，故 $H_A=LAN$ 一般**不等于** $HA$。纸面证明从未使用该等式。
- `hasConstantRank_iff_rankIndependent` —— 铅笔秩恒定 $\exists r\forall z$ 与逐点相等 $\forall z\,w$ 等价。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节（谱条件的两种写法）。

- `spectralCondition_hasConstantRank` —— 论文条件 $\operatorname{rank}(zH-HA)=\operatorname{rank}H$ 是秩恒定的特例。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节。

- `spectralCondition_zero` —— $z=0$ 处给出 $\operatorname{rank}(HA)=\operatorname{rank}H$；这是把 $\operatorname{row}H_A\subseteq\operatorname{row}H$ 升为等号的那一步。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节（结构界证明）。
- spectralCondition_zero_eq_zero —— =-H A$（定义的展开）。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节。
- `spectralCondition_zero_eq_zero` —— 定义展开：`(0 : K) • H - H * A = -H * A`。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节。
- `mem_pi1` —— $x\in\pi_1(W)\iff\exists y,(x,y)\in W$。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节。

- `mem_pi2` —— $y\in\pi_2(W)\iff\exists x,(x,y)\in W$。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节。

- `eq_of_le_of_finrank_eq` —— 同维且包含 ⟹ 相等。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节（结构界证明里 $\pi_1(W)=\pi_2(W)$ 那一步）。

- `pi1_eq_pi2_of_le_of_finrank_eq` —— **第 3 条**：$\pi_2(W)\le\pi_1(W)$ 且维数相等 ⟹ $\pi_1(W)=\pi_2(W)$。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节（用 $(5a)$ 与 $\lambda=0$ 的谱条件）。
- `rowSpace_eq_span_col_transpose` —— 行空间等于转置的列张成的空间。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节（矩阵-子空间翻译）。

- `rank_fromRows_eq_rank_iff` —— **第 2 条（矩阵形式）**：$\operatorname{rank}[A;B]=\operatorname{rank}B\iff\operatorname{row}A\le\operatorname{row}B$。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节。
- `mulVecLin_neg` —— $\operatorname{mulVecLin}(-M)=-\operatorname{mulVecLin}M$。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节。

- `matrixRank_neg` —— $\operatorname{rank}(-M)=\operatorname{rank}M$。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节。

- `rank_of_spectralCondition` —— 谱条件在 $z=0$ 给出 $\operatorname{rank}(HA)=\operatorname{rank}H$。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节（结构界证明）。

- `rowSpace_eq` —— **第 3 条（矩阵形式）**：$\operatorname{rank}[H_A;H]=\operatorname{rank}H$ 加谱条件 ⟹ $\operatorname{row}H_A=\operatorname{row}H$。**出处**：[89 号回复](../../workspace/for_expert/archive/89_subspace_reduction_and_fpt-reply.md) 第 1 节。

### PropC.lean —— Prop C：复合映射的秩恒等式（attempts/344）

- `propC_rank_identity` —— $\operatorname{finrank}(\operatorname{range}g)=\operatorname{finrank}(\operatorname{range}(f\circ g))+\operatorname{finrank}(\operatorname{range}g\sqcap\ker f)$。**出处**：[344 §Prop C](../../workspace/q1_false/c_stratification/attempts/344_three_theorems_and_two_level_criterion.md)。**意义**：把 `Prelude.lean` 的 `finrank_map_add_finrank_inf_ker`（自同态版本）推广到任意余定义域；取 $g=AN$、$f=L$ 即 $\operatorname{rank}(LAN)=\dim(AK_0)-\dim(AK_0\cap\ker L)$。**差异**：无。

- `propC_consequence` —— `range g ⊓ ker f ≠ ⊥` ⟹ $\operatorname{finrank}(\operatorname{range}(f\circ g))+1\le\operatorname{finrank}(\operatorname{range}g)$。**出处**：[344 §Prop C 推论](../../workspace/q1_false/c_stratification/attempts/344_three_theorems_and_two_level_criterion.md)。**意义**：零频障碍 $v\in AK_0$ ⟹ $\operatorname{rank}H_A\le\dim(AK_0)-1$ 的抽象核。**差异**：无。

- `rank_drop_of_mem_common` —— 若 `v ≠ 0` 同时落在 `range g` 与 `ker f`，则 $\operatorname{finrank}(\operatorname{range}(f\circ g))+1\le\operatorname{finrank}(\operatorname{range}g)$。**出处**：[344 §Prop D 的核心](../../workspace/q1_false/c_stratification/attempts/344_three_theorems_and_two_level_criterion.md)。**意义**：零频障碍的抽象形式（$g=AN$、$f=L$、$v\in AK_0\cap V^\perp$ ⟹ $\operatorname{rank}(LAN)\le\dim(AK_0)-1$）。**差异**：无。

### Quad.lean —— Theorem B 的取根一步（attempts/344）

- `exists_sq_eq_of_isAlgClosed` —— 代数闭域上每个元素是完全平方。**出处**：[344 §Theorem B](../../workspace/q1_false/c_stratification/attempts/344_three_theorems_and_two_level_criterion.md)。**意义**：判别式的平方根。**差异**：无。

- `quadratic_has_root` —— $a\ne0$ ⟹ $\exists x,\ a x^2+b x+c=0$（代数闭域上的非平凡二次必有根）。**出处**：[344 §Theorem B](../../workspace/q1_false/c_stratification/attempts/344_three_theorems_and_two_level_criterion.md)。**意义**：临界档 $\det(\lambda X'-G')$ 首项系数可逆 ⟹ 有复根 ⟹ 该处降秩。**差异**：矩阵层的"$\det(\lambda X-G)$ 是首项系数 $\det X\ne0$ 的二次多项式"（展开与次数记账）**未形式化**。

### HyperplaneDirection.lean —— 论文 Theorem 3（方向定理，Paper III）

- `compression_eq_of_proportional` —— 设 $Av=w+z$，$w\in K$、$z\in K^\perp$，且 $u\mapsto\langle u,Av\rangle$ 在 $K$ 上是 $u\mapsto\langle u,v\rangle$ 的 $\mu$ 倍；则 $w=\mu v$（压缩把 $v$ 送到 $v$ 的倍数）。**出处**：论文 Theorem 3，本仓库 [archive/paper_drafts/paper_III_workspace_2026-11/hyperplane/hyperplane_layer.tex](../../archive/paper_drafts/paper_III_workspace_2026-11/hyperplane/hyperplane_layer.tex)。**意义**：把"选行空间"化为"选特征向量 + 在方向上选子空间"的代数内核。

- `proportional_of_compression` —— 反向：$w=\mu v$ ⟹ 两泛函成比例。

- `direction_iff` —— 上述两条的等价形式：两泛函成比例 $\iff$ $w=\mu v$。**出处**：论文 Theorem 3。

### HyperplanePrescribed.lean —— 论文 Lemma 4（预设行，Paper III）

- `le_orthogonal_span_pair` —— 若 $V_0$ 的每行都消去 $v$ 与 $Av$，则 $V_0\le\operatorname{span}\{v,Av\}^\perp$。**出处**：论文 Lemma 4 的"自动正交性"。

- `inf_inf_orthogonal_eq` —— 若 $V_0\le U^\perp$，则 $V_0\sqcap(K\sqcap U^\perp)=V_0\sqcap K$。**出处**：论文 Lemma 4 的 $\delta=\dim V_0-\dim(V_0\cap K_0)$ 与方向无关。

- 说明：上述五条在 `-~/WorkSpace/lean4/Q1Paper` 构建并通过 `Audit.lean` 的 `#print axioms`（只有 `propext`、`Classical.choice`、`Quot.sound`）；镜像在 artifact 仓库 `q1-functional-observer` 的 `Q1Paper/`。

### HyperplaneFibre.lean —— 论文 Lemma 2 的数值部分（Paper III）

- `mem_orthogonal_span_pair_iff` —— $w\perp\operatorname{span}\{v,Av\}\iff\langle w,v\rangle=0\wedge\langle w,Av\rangle=0$。

- `Dv_eq_ker` —— 比例性下 $D_v=K\sqcap\operatorname{span}\{v,Av\}^\perp$ 等于 $u\mapsto\langle u,v\rangle$ 在 $K$ 上的核。

- `finrank_Dv` —— $\operatorname{finrank}D_v+1=\operatorname{finrank}K$（即命题里的 $k-1$）。**出处**：论文 Lemma 2。**意义**：纤维的公共核是 $K$ 的超平面；这条给后面"纤维 $=\operatorname{Gr}(s-\delta,\cdot)$ 的维数 $(s-\delta)(r-s)$"提供了 $k-1$ 这一步。

### SplitFibre.lean —— $c=2$ 的 $W$-消去核心（卷宗 406）**（在 MyProof，不在 Q1Paper）**

> **位置**：`~/WorkSpace/lean4/MyProof/MyProof/SplitFibre.lean`，`namespace Q1PaperC2`；同上，内容未固定。
> **构建**：`lake build MyProof.SplitFibre`（exit=0）；`#print axioms` 只含三条标准公理。

- `split_design_orthogonal_D` —— $D\le K$、$W\le K^\perp$ ⟹ $(K\sqcap D^\perp)\sqcup W\le D^\perp$。
- `orthogonal_split_iff` —— $A=M+N$、$M(D)\subseteq D$、$\operatorname{im}N\subseteq K^\perp$ ⟹
  $V\le(D+AD)^\perp\iff W\le(ND)^\perp$。**出处**：[attempts/406](../../workspace/q1_false/c_stratification/attempts/406_eliminate_W.md) 定理 2；
  **意义**：$K_0$-split 设计上 $(5a)\iff W\subseteq T_D$（这是纤维公式的根据）。
- `phi_kills_D` —— $w\le(ND)^\perp$、$d\in D$ ⟹ $\langle w,Nd\rangle=0$，即 $\Phi(W)\subseteq D^\circ$（$\dim\le c$）。

**未形式化**：行空间恒等式 $\operatorname{row}(\lambda H-H_A)=\operatorname{row}(\lambda H_K-(H_A)_K)+\Phi(W)$（矩阵层，需要显式块构造）。

### HyperplaneC2.lean —— $c=2$ 层的 $K$-split 纤维（卷宗 393 命题 2）**（在 MyProof，不在 Q1Paper）**

> **位置**：`~/WorkSpace/lean4/MyProof/MyProof/HyperplaneC2.lean`，`namespace Q1PaperC2`。
> **不放进 Q1Paper**（论文树）的原因：这些内容**尚未固定**（2026-11-21 用户指示）；等 $c=2$ 定稿再迁移。
> **构建方式**：`cd ~/WorkSpace/lean4/MyProof && lake env lean MyProof/HyperplaneC2.lean`（exit=0）；
> 未接入 MyProof 的聚合图（`MyProof.lean` 由脚本生成，未固定前不入图）。

- `sup_inf_eq_left_of_le_orthogonal` —— 设 $D\le K$、$W\le K^\perp$，则 $((K\sqcap D^\perp)\sqcup W)\sqcap K=K\sqcap D^\perp$。
  **出处**：[attempts/393](../../workspace/q1_false/c_stratification/attempts/393_c2_fibre_and_base.md) 命题 2(i)（$V\cap K=D^{\perp_K}$）。
  **意义**：$K$-split 设计 $V=D^{\perp_K}\oplus W$ 在 $K$ 内的部分只由方向 $D$ 决定，$W$ 不贡献——
  这是 $c=2$ 纤维从"底 + 纤维"分解的依据。

- `disjoint_of_le_orthogonal` —— $W\le K^\perp$ ⟹ $W$ 与 $K\sqcap D^\perp$ 不交（用 $\langle x,x\rangle=0\Rightarrow x=0$）。

- `finrank_sup_of_disjoint_of_le_orthogonal` —— $\dim V=\dim(K\sqcap D^\perp)+\dim W$，即层记帐 $q=(k-c)+t$。
  **出处**：卷宗 393 命题 2 的维数部分；**意义**：$c=\dim D$、$t=\dim W$ 与 $q$ 的关系式。

- 说明：三条的 `#print axioms` 只含 `propext`、`Classical.choice`、`Quot.sound`。
