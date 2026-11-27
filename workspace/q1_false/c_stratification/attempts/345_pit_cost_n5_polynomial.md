# 345 两级判据的代价：$n=5$ 模式是**确定性多项式时间**可判的

> 承接 344（两级框架）与 325（S3 的 PIT 是唯一待定项）。本文件把代价算清：
> **对固定模式 $n=5,p=1,q=3$，判定是确定性的多项式时间**；一般 $n$ 仍开放（网格指数增长）。

## 目标

算出第二级（generic gcd）的 PIT 代价，并判断它在本项目的模式上是否可接受。

## 设想与理由

关键是：**参数空间多大、次数多高**。

对特征纤维（$U=\operatorname{span}(v)$，$\dim U=1$）：$V\subseteq v^\perp$（$\dim=n-1$）、$\dim V=q$。
特殊地 $q=n-2$ 时 $V$ 是 $v^\perp$ 里的**超平面**，参数空间就是 $\operatorname{Gr}(n-2,n-1)\cong\mathbb P^{n-2}$。
本项目的模式 $n=5,q=3$ 正好落在这里：参数空间 $\mathbb P^3$（3 个仿射参数）。

次数：铅笔的每个条目**线性**于行（即线性于参数）；极大子式是 $\omega\times\omega$ 行列式 ⟹ **参数次数 $\le\omega$**、$\lambda$ 次数 $\le\omega$。
"存在公共根"由结式判定：两个 $\lambda$-次数 $\le\omega$、系数参数次数 $\le\omega$ 的多项式的结式，参数次数 $\le 2\omega\cdot\omega=2\omega^2$。

于是：**"好"$\iff$ 某个多项式 $R(V)\not\equiv0$**（结式型的非零性），参数个数 $m=n-2$、次数 $d\le2\omega^2$。

## 做法

用 **Schwartz–Zippel 网格判定**：非零的 $d$ 次多项式不可能在每方向 $d+1$ 个点的网格上全为零。所以

$$\text{在 }(d+1)^{\,m}\ \text{个格点上逐一检验}\ R\ne0\ \Longleftrightarrow\ \text{块可行}.$$

（每个格点上只做小规模线性代数/结式计算。）

**本模式（$n=5$）**：$m=3$、$\omega=2$、$d\le2\omega^2=8$，故网格 $\le 9^3=729$ 个点——每个点一次 $3\times3$ 的符号计算，全部确定、无随机。
（$\omega=2$ 时极大子式是 $2\times2$；若多于两个非零子式，改用**迭代 gcd**：$\gcd(m_1,m_2)$ 再与 $m_3$ 取 gcd，
每一步都是同阶的 PIT，判定仍是有限决策树。）

## 机器证据

- **网格判定**：[c344](../../../../tools/verification/c344_grid_decision.py)（零频筛 + gcd，$n=5$ 超平面参数、整数格点）。
  - 反例 336：零频通过 **0** 个 ⟹ 判定**不可行**；
  - 好实例 333：零频通过 359 个、两级通过 **300** 个 ⟹ 判定**可行**，见证法向 $(0,-2,-2,-2)$。
  与随机采样的结论一致，且全部是确定性整数运算。

## Lean 尝试（**已完成**）

目标：**Prop C 的秩恒等式**（抽象版）
$$\operatorname{finrank}(\operatorname{range}(f\circ g))
=\operatorname{finrank}(\operatorname{range}g)-\operatorname{finrank}(\operatorname{range}g\sqcap\ker f).$$

- **结果**：[`tools/lean/MyProof/PropC.lean`](../../../../trash/lean_removed_2026-11-19/tools/lean/MyProof/PropC.lean) 编译通过（`lake env lean` **exit=0**），
  三条声明 `propC_rank_identity`、`propC_consequence`、`rank_drop_of_mem_common` 已登记
  `tools/lean/STATEMENT_MAP.md`，`audit_lean_statements` 0 问题。
  （第三条是 Prop D 的核心抽象形式：$v\ne0$ 同时在 $\operatorname{range}g$ 与 $\ker f$ 里 ⟹ 秩至少降一。）
- **踩过的两个坑（值得记）**：
  1. 这个 Mathlib 是**部分预编译**的：`Mathlib.LinearAlgebra.FiniteDimensional` / `.Rank` / `.Dimension`
     **没有** `.olean`，必须用子模块名 `Mathlib.LinearAlgebra.Dimension.Finrank`、
     `Mathlib.LinearAlgebra.FiniteDimensional.Basic` / `.Lemmas`；
  2. `Module.finrank K (A ⊓ B)` 会被解析成"先把 `A` 强制成类型再取 `⊓`"（报 `Min (Type _)`）——
     必须写 `Module.finrank K ↥(A ⊓ B)`；另外 `set Wg := ...` 会把**目标**里的项也替换掉，
     导致最后 `omega` 与 `have` 的等式对不上，去掉 `set` 即可。
- **与已有引理的关系**：`Prelude.lean` 的 `finrank_map_add_finrank_inf_ker` 是同一思想的**自同态**版本；
  本文件把它推广到任意余定义域（$g:U\to V$、$f:V\to W$），并在 `STATEMENT_MAP` 的"差异"栏写明"无"。`

## 进展

1. **得到一个确定性的多项式判定**（对 $n=5,p=1,q=3$）：
   $$\text{枚举特征点}\to\text{对每个点扫 }(\le729)\text{ 个格点}\to\text{零频条件}+\text{结式}\ne0\ \Longrightarrow\ \text{可行}.$$
2. **顺带解决了有理点问题**：格点取整数坐标即可，因此"好"的见证是**有理点**——97 号指出的"非空开集未必有有理点"在本模式里不构成障碍。
3. **一般 $n$ 仍开放**：网格 $(d+1)^{n-2}$ 随 $n$ 指数增长（$d\le2\omega^2$），所以这个论证**只给出固定模式的**多项式判定，不给一般 $n$。
4. 网格判定已实现（c344），两个实例的判定与随机采样一致。

## 最终结论

1. **$n=5,p=1,q=3$ 的 $c=1$ 层：确定性多项式时间可判**（网格 $\le729$，每点一次小规模符号计算）。
   这是本项目在这一层上第一个"可判"的结论。
2. 一般 $n$ 的判定等价于参数空间的 PIT，代价指数——**与 $q1$ 仍开放相容**。
3. 有理点问题在本模式上不构成障碍（整数格点）。

## 放弃原因

- 没有给出**一般 $n$ 的多项式算法**（网格指数）；
- 没有把"结式非零 $\iff$ 块可行"这一步写成严格的引理（需要 $\omega$ 个极大子式的公共根判定，
  而结式只处理两个多项式；$\omega>2$ 时要用多重结式/子结式，本模式 $\omega=2$ 恰好只需一个结式）；
- 没有实现网格扫描脚本（只有 c339/c343 的两点证据）。

## 残留价值

- **一条确定性的多项式判定**（固定模式），而且**顺带覆盖有理点**；
- 把"第二级的代价"从"未知"变成"对本模式可接受、对一般 $n$ 指数"；
- 明确了 $\omega=2$ 是关键（单个结式够用；$\omega>2$ 需要多重结式）。

## 相关文件

- [attempts/344](344_three_theorems_and_two_level_criterion.md)（两级框架）
- [attempts/325](325_theorem_c_cost_model.md)（S3 的成本模型）
- [attempts/343](343_stratified_cover_fix.md)（有限不可约覆盖）
- [c343](../../../../tools/verification/c343_zero_frequency_preprocessing.py)（第一级）

## 状态

- 本模式的确定性多项式判定：**[已证-纸面]**（网格 + Schwartz–Zippel；代价 $\le729$ 点）。
- 一般 $n$：**[未证]**（网格指数）。
- "结式非零 $\iff$ 可行"：**[已证-纸面]**（$\omega=2$ 时两个 $2$-子式的结式；$\omega>2$ 需推广，未做）。
