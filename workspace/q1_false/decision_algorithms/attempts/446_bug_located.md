# 446 bug 定位：`c385` 的 $(E)$ 实现错；构造性判定与 $(E)$ 一致；444 的判据得到支持

> 承接 445（内部矛盾）。本轮用**构造性判定**（取 $\mathcal T_W$ 的基当自由行）对照，
> 结论：**构造性判定与 $(E)$ 完全一致**（6/6，连 $\gcd$ 都相同），错的是一处实现。

## 目标

定位 445 指出的矛盾。

## 设想与理由

445 的论证：$(E)\wedge m\ge\dim\mathcal T_W\Longrightarrow(F)$，且若 $m=\dim\mathcal T_W$、
取 $\mathcal T_W$ 的基当自由行，则**铅笔的秩恒等于 $\dim E_\lambda(\mathcal T_W)$** ⟹
$(E)\iff(F)$（在 $m=\dim\mathcal T_W$ 时）✓。所以两者应当**完全一致**。

## 做法

对随机实例（$n=5$、$p=1$、$k=3$、$\omega=2$，相容 $W$ 由固定对的核给出），同时算：
- $(E)$：$M(\lambda)=(\lambda x_j-y_j)$ 的 $\omega$-子式 $\gcd$ 是否为常数；
- $(F)$：**取 $\mathcal T_W$ 的基当自由行**（$m=D$）构造铅笔，同法算 $\gcd$。

## 进展（结果，6/6 一致）

| trial | $\dim\mathcal T_W$ | $(E)$ 的 $\gcd$ | 构造性 $(F)$ 的 $\gcd$ | 一致？ |
|---|---|---|---|---|
| 0 | 3 | $(61\lambda^2+49\lambda-42)/61$ | **完全相同** | ✓ |
| 1 | 3 | $(75\lambda^2-56\lambda-221)/75$ | **完全相同** | ✓ |
| 2 | 3 | $(7\lambda^2+\lambda+5)/7$ | **完全相同** | ✓ |
| 3 | 3 | $\lambda(7\lambda-27)/7$ | **完全相同** | ✓ |
| 4 | 3 | $(13\lambda^2-20\lambda-58)/13$ | **完全相同** | ✓ |
| 5 | 3 | $\lambda^2-11\lambda+32$ | **完全相同** | ✓ |

**6/6 完全一致**，且 $m=D$ 时**逐字相同** ✓。

## 结论（bug 在哪）

`c385`（441 的依据）把"$\pi_1(\mathcal T_W)=\pi_2(\mathcal T_W)=W$"当成了 $(E)$——
那只是 $(E)$ 的**弱化**（它不检查子式的互素性）⟹ 于是它报出"$(E)$ 真、$(F)$ 假"的 20 个"反例" ✗。

**真实状态**：

1. $m\ge\dim\mathcal T_W$ 时 $(E)\iff(F)$ ✓（构造性验证 6/6）；
2. 实测里 $(E)$ 假（$\gcd$ 非常数）恰好都在 $\dim\mathcal T_W=3<2\omega=4$ ⟹ 与 444 的判据**一致** ✓；
3. 441 的"$(E)\not\Rightarrow(F)$"与 442 的"灰色带非空"**都是 bug 的产物**，撤回。

## 最终结论

1. **bug 定位**：`c385` 的 $(E)$ 用错了（用了投影条件的秩，而不是子式互素）；
2. **有效结论**：$m\ge\dim\mathcal T_W$ 时 $(E)\iff(F)$；且 444 的判据（$\mathcal T_W=W\oplus W$，即 $\dim=2\omega$）在**全部观测**上成立（6/6 + 10/10）；
3. 于是**层判据回到 444**，且它现在有：必要（437）、构造充分（441）、以及"$m$ 足够时等价"（本轮）三层支撑。

## 放弃原因

- 没有重跑 441/443 的全部实例（只跑了 6 个新实例）；
- 444 的判据仍**未证明**（缺"$\dim<2\omega$ ⟹ $(E)$ 失败"的一般证明）；
- 固定行补一位的边界仍未处理。

## 残留价值

- **一次干净的 bug 定位**（错误类型：用弱化条件代替真条件）；
- 恢复了"$(E)$ 与 $(F)$ 在行数足够时等价"这条主结论；
- 444 的判据从"数据支持"升级为"数据 + 等价性"支持。

## 下一步

1. 修 `c385`（用子式互素算 $(E)$），重跑 441/443 的实例，确认判据；
2. 证 444 的未证方向（"$\dim<2\omega$ ⟹ $(E)$ 失败"）。

## 相关文件

- [445](445_internal_conflict.md)（内部矛盾）
- [444](../../c_stratification/attempts/444_threshold_criterion.md)（判据）
- [441](../../c_stratification/attempts/441_projection_not_sufficient.md)、[442](../../c_stratification/attempts/442_three_conditions.md)、[443](../../c_stratification/attempts/443_gray_band_has_feasible.md)（受 bug 影响）
- [437](../../c_stratification/attempts/437_eval_map_criterion.md)（$(E)$）

## 状态

- bug：**[已定位]**（`c385` 的 $(E)$ 实现）。
- $(E)\iff(F)$（$m\ge\dim\mathcal T_W$）：**[已证-纸面]** + **[精确验证 6/6]**。
- 444 的判据：**[未证，数据一致]**。
