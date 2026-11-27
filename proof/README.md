# proof/ — 命题卷宗与支撑材料

> **分工契约（2026-11-06）**
> * `docs/` 对**整个项目**（尤其 $q1$）负责：陈述、结论、论文级整理，是"note/论文"的载体。
> * `proof/` 对 docs 里的**具体命题/引理**负责：每个条目一个**卷宗** `proof/<条目>/README.md`，
>   统一管理 **纸面证明 + Lean 验证 + 精确/数值验证 + 状态与历史**，便于逐条检验。
>
> 卷宗必备小节：`## 命题`、`## 纸面证明`、`## Lean`、`## 精确验证`、`## 状态与历史`、
> 以及 `> **对应 docs**：…` 一行。`tools/hygiene/audit_proof_map.py` 会检查这些小节，
> 并把"尚无卷宗"的条目列为待办（基线见 `tools/hygiene/proof_dossier_baseline.txt`）。
>
> **完成度**（验收规则 2026-11-07）：**30/30 完成**——数学上均达 M3（专家复核 / 可信来源）；
> 其中 **22 条有 Lean 覆盖**（8 条字面 + 14 条内核），**8 条为可接受纸面**
> （B.4、B.8、B.10、B.13、B.14、B.24、B.37，以及 D.1 的递归等式——其 Lean 内核
> `exists_sigma`/`lift_admissible` 已登记且"无差异"）。
> 详见 [UNFINISHED.md](UNFINISHED.md)（当前：未完成 0 条）。

> 除卷宗外，`proof/` 还保留**支撑目录**（工具、历史归档、实例复现、`refuted/` 反例库），
> 由对应卷宗链接。

## 条目索引（与 docs/02 的 30 条主条目对齐）

| docs 主条目 | 卷宗 | 支撑目录 |
|---|---|---|
| A.1 · 维数分解与下界 | [A.1/](A.1/README.md) | [lower_bound/](lower_bound/README.md)、[base_family/](base_family/README.md) |
| B.1 · 商铅笔等价 | [B.1/](B.1/README.md) | [pencil_equivalence/](pencil_equivalence/README.md) |
| B.2 · 顶层可观测与 PBH | [B.2/](B.2/README.md) | [top_layer_observability/](top_layer_observability/README.md)、[xw_decomposition/](xw_decomposition/README.md)、[cyclic_vector_criterion/](cyclic_vector_criterion/README.md)、[controllability_equivalence/](controllability_equivalence/README.md) |
| B.3 · $\rho=0$ 层 | [B.3/](B.3/README.md) | [rho0_layer/](rho0_layer/README.md) |
| B.4 · $V=\mathbb C^n$ 的判据 | [B.4/](B.4/README.md) | [b4_full_space/](b4_full_space/README.md) |
| B.6 · 右最小指标与无穷初等因子 | [B.6/](B.6/README.md) | [kron_null_module/](kron_null_module/README.md)、[t4b_infinite_divisors/](t4b_infinite_divisors/README.md)、[descriptor_reduction/](descriptor_reduction/README.md)、[left_index_count/](left_index_count/README.md)、[toeplitz_criterion/](toeplitz_criterion/README.md) |
| B.8 · 铅笔的 Smith/Kronecker 结构 | [B.8/](B.8/README.md) | [5a_archive/](5a_archive/README.md)、[5b_upper_bound/](5b_upper_bound/README.md) |
| B.9 · 边界与等号结构 | [B.9/](B.9/README.md) | [h_formula/](h_formula/README.md)、[h_bound/](h_bound/README.md)、[l0_reduction/](l0_reduction/README.md)、[fernando_2gap/](fernando_2gap/README.md) |
| B.10 · 谱障碍的定域 | [B.10/](B.10/README.md) | — |
| B.11 · Type I/II 的几何形式 | [B.11/](B.11/README.md) | — |
| B.12 · 谱条件的可观性归约 | [B.12/](B.12/README.md) | — |
| B.13 · 计数判据族 | [B.13/](B.13/README.md) | [spectral_locus/](spectral_locus/README.md)、[eigenvalue_confinement/](eigenvalue_confinement/README.md)、[incidence_strata/](incidence_strata/README.md)、[global_incidence/](global_incidence/README.md)、[observability_chain/](observability_chain/README.md)、[PCC/](PCC/README.md)、[type3_second_example/](type3_second_example/README.md) |
| B.14 · 投影铅笔满列秩类 | [B.14/](B.14/README.md) | — |
| B.15 · 避免性引理 | [B.15/](B.15/README.md) | — |
| B.16 · 分层判据 | [B.16/](B.16/README.md) | — |
| B.17 · 永久核与商铅笔 | [B.17/](B.17/README.md) | — |
| B.18 · $p=r=1$ 的结构 | [B.18/](B.18/README.md) | — |
| B.21 · 右零空间与指标 | [B.21/](B.21/README.md) | — |
| B.22 · 等号障碍（独立引理） | [B.22/](B.22/README.md) | — |
| B.23 · 统一分块因子化 | [B.23/](B.23/README.md) | — |
| B.24 · 内蕴形式 $\Phi$ | [B.24/](B.24/README.md) | — |
| B.25 · 矩形铅笔与 gcd 判据 | [B.25/](B.25/README.md) | — |
| B.28 · 子空间归约与分层参数 | [B.28/](B.28/README.md) | — |
| B.31 · 可行性的必要条件（独立引理） | [B.31/](B.31/README.md) | [delta1_feasible/](delta1_feasible/README.md) |
| B.32 · 终端唯一区 | [B.32/](B.32/README.md) |
| B.37 · 谱可行性的统一刻画 | [B.37/](B.37/README.md) | B.17、B.24、B.8、B.1（见 `proof/B.35/README.md` 的支撑目录一节）| — |
| C.1 · 特殊族的精确值 | [C.1/](C.1/README.md) | [s_j_family/](s_j_family/README.md)、[layer_31_theorems/](layer_31_theorems/README.md)、[layer_program/](layer_program/README.md)、[rho1_layer/](rho1_layer/README.md) |
| D.1 · $P$ 的多项式可解性 | [D.1/](D.1/README.md) | [p_is_polynomial/](p_is_polynomial/README.md) |
| F.1 · 秩屏障 | [F.1/](F.1/README.md) | [rank_barrier/](rank_barrier/README.md) |
| G.1 · 复杂度上界与编码 | [G.1/](G.1/README.md) | [dec_q_existsR/](dec_q_existsR/README.md) |
| H.1 · 商等价、方阵条件与 $d=0$ 边界 | [H.1/](H.1/README.md) | [quotient_equivalence/](quotient_equivalence/README.md)、[h2_dim_arithmetic/](h2_dim_arithmetic/README.md)、[d0_boundary/](d0_boundary/README.md) |
| K.1 · 双向量可分解性 | [K.1/](K.1/README.md) | [bivector_r2/](bivector_r2/README.md) |

> 注：旧 B.16（分层判据）与旧 B.17（永久核）在 `docs/02` 中并入主条目 **B.17 · 统一商铅笔定理**
> （见 `docs/02` §0.1 别名表）；两份卷宗目录名保留，正文引用旧编号仍合法。

## 反例库

| 目录 | 内容 |
|---|---|
| [refuted/](refuted/README.md) | 被推翻的命题与反例证书（不属任何主条目）|
