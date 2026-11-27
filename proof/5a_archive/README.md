# (5a) 归档：4 块形式、行包含、(A)、最小增广 $q_0$

> **对应 docs 条目**：B.8（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

> 归档日期：2026-10-21
> 状态：**结构/判定 ✅ 已证；$q_0$ 闭式 ✅（P1 Theorem 2，项目未独立证明）；候选族 q2 ✅；q3 端点 ✅**

## 一句话

$(5a)$ 是原命题的**代数侧**：

$$(5a)\ \operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C].$$

它有三个等价形式：

$$(5a)\iff \operatorname{row}(LA)\subseteq\operatorname{row}(L,CA,C)=:(A)
\iff \ker[L;CA;C]\subseteq\ker(LA)
\iff \exists\Lambda,G_0,G_1:\ LA=\Lambda L+G_0C+G_1CA.$$

只要求 $(A)$ 时的最小行数是

$$q_0=\sum_{j=1}^r\eta_j\qquad(\text{P1 Theorem 2}),$$

这是 $q_{\min}$ 的**下界基线**，也是 $(5b)$ 分析的入口（$F=\Lambda H$）。

**$(5a)$ 必要但多项式；$(5b)$ 必要且未证（谱条件）。硬度在 $(5b)$，但 $(5a)$ 的证明不可少。**

## 文件地图

| 文件 | 内容 |
|---|---|
| [`README.md`](README.md) | 本文件：结论、状态、入口 |
| [`01_描述与意义.md`](01_描述与意义.md) | $(5a)$ 是什么、三种等价形式、控制论意义、与 $(5b)$/q1 的关系 |
| [`02_证明.md`](02_证明.md) | T1、核条件、Lean 链（`ABridge`/`Factor`）、T3/T4、$q_0$、q2、q3 |
| [`03_验证.md`](03_验证.md) | 如何跑、测试结果、局限 |
| [`lean/ABridge.lean`](../../trash/lean_removed_2026-11-19/proof/5a_archive/lean/ABridge.lean) | Lean：$(A)$ 的秩形式 $\iff$ 分解 |
| [`lean/Factor.lean`](../../trash/lean_removed_2026-11-19/proof/5a_archive/lean/Factor.lean) | Lean：分解 $\iff$ 三重核条件；`tuple_apply` |
| [`lean/DimCount.lean`](../../trash/lean_removed_2026-11-19/proof/5a_archive/lean/DimCount.lean) | Lean：维数计数（阈值侧的辅助） |
| [`scripts/verify_5a.py`](scripts/verify_5a.py) | 独立检查：三种等价形式 + `p1` 的 $q_0$ |

> `lean/` 下是 `scripts/lean/` 的副本，便于归档查阅；编译以 `scripts/lean/` / WSL 工程
> `~/WorkSpace/lean4/MyProof` 为准。

## 核心结论

| 内容 | 状态 | 依据 |
|---|---|---|
| $(5a)\iff$ 4 块 $\iff\operatorname{row}(LA)\subseteq\operatorname{row}(L,CA,C)$ | ✅ 已证 | T1；[`ABridge`](../../trash/lean_removed_2026-11-19/proof/5a_archive/lean/ABridge.lean) |
| $(A)\iff$ 分解 $LA=\Lambda L+G_0C+G_1CA$ | ✅ 已证（Lean） | [`ABridge.decomp_iff_rank`](../../trash/lean_removed_2026-11-19/proof/5a_archive/lean/ABridge.lean) |
| 分解 $\iff$ 核条件 $\ker[L;CA;C]\subseteq\ker(LA)$ | ✅ 已证（Lean） | [`Factor.decomp_iff_ker`](../../trash/lean_removed_2026-11-19/proof/5a_archive/lean/Factor.lean) |
| $(A)$ 的精确阈值 $k+\dim(E+\operatorname{row}B_{A,T})\ge d_C$ | ✅ 已证 | T3/T4，[FINAL](../../archive/paper_drafts/FINAL.md#L146-L155) |
| 只要求 $(A)$ 的最小行数 $q_0=\sum\eta_j$ | ✅ 定理（P1 Thm 2） | 项目**未独立证明** ⚠️ |
| 候选行族约束不增加硬度（q2） | ✅ 已证 | [q2.md](../../archive/problem_statements/q2.md#L35-L52) |
| $\operatorname{rank}[C;CA]=n\Rightarrow$ $(5b)$ 自动成立，$\nu_{\min}=q_0$ | ✅ 已证 | [q3.md](../../archive/problem_statements/q3.md#L3) |

## 与 $(5b)$ / q1 的关系

1. **逻辑上**：q1 要求 $(5a)\wedge(5b)$；$(5a)$ 是不可缺少的合取项。
2. **技术上**：$(5a)\Longrightarrow F=\Lambda H$，这是 $(5b)$ 化成铅笔 $(\lambda I-\Lambda)H$ 的前提；没有它，上界 $\operatorname{rank}(\lambda H-F)\le\operatorname{rank}H$ 会失败，gcd 判据也不等价于 $(5b)$。
3. **下界**：$q_0$（$(5a)$ 单独的最小行数）给出 $q_{\min}\ge q_0$；没有它，连“至少需要多少行”都不确定。
4. **硬度**：$(5a)$ 单独是多项式的（$q_0$ 闭式、阈值多项式），所以 q1 的 NP-hard 难度（若存在）只能在 $(5b)$ 侧；但这不等于 $(5a)$ 可以跳过。

## 如何复现

```bash
# 1. 本归档的独立检查
python proof/5a_archive/scripts/verify_5a.py

# 2. 四条等价关系（E1/E4 就是 (5a) 的两种形式）
python scripts/core/verify_equivalences.py

# 3. 地基检查：原始 4 块 (5a) vs 三块约化
python scripts/core/reliable_S_test.py

# 4. 铅笔形式 (A) <=> q_i ∈ row P
python scripts/core/verify_pencil_v2.py

# 5. Lean
export PATH="$HOME/.elan/bin:$PATH"
cd ~/WorkSpace/lean4/MyProof && lake build
```

## 相关文档

- [FINAL T1/T3/T4](../../archive/paper_drafts/FINAL.md#L133-L155)
- [problems/q1.md](../../archive/problem_statements/q1.md#L80-L81)（“仅 (5a) 是多项式的”）
- [problems/q2.md](../../archive/problem_statements/q2.md)（候选族不提供硬度）
- [problems/q3.md](../../archive/problem_statements/q3.md)（$d_{CA}=0$ 端点）
- [docs/05](../../literature/notes/05_相关工作检索.md#L29-L35)（$q_0=\sum\eta_j$ 的文献状态）
- [(5b) 上界归档](../5b_upper_bound/README.md)（$(5a)$ 是它的前提）
