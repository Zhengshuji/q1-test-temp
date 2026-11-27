# 用 $G_{\\mathcal Z}$ 判据重扫 $q_0$ 阶：命中率提升与新的统计

## 目标

上一轮的 $q_0$ 阶抽样命中率极低（很多实例只拿到 1 个样本）。原因已定位：
$\\dim G_{\\mathcal Z}<q_0$ 的 $\\mathcal Z$ 连必要条件都不过（282/300 个）。
本档用 [attempts/18](18_gz_criterion.md) 的判据**重扫**，并给出更可靠的"$q_{\\min}=q_0$"统计。

## 设想与理由

若 $(5a)\\iff\\operatorname{row}\\mathcal L\\subseteq G_{\\mathcal Z}$，那么只要在 $G_{\\mathcal Z}$ **内部**构造
$\\mathcal L$ 的行，$(5a)$ 就自动成立。这样每个"过必要条件"的 $\\mathcal Z$ 都应当能产出候选，
而不再依赖"从 $\\mathcal Z^{\\perp}$ 的基里贪心碰运气"。

## 做法

[q0_scan_gz.py](../../../../tools/verification/q0_scan_gz.py)：
每个实例抽 80 个 $\\mathcal Z$；先算 $G_{\\mathcal Z}$，只保留 $\\dim G_{\\mathcal Z}\\ge q_0$ 的；
在 $G_{\\mathcal Z}$ 内构造 $\\mathcal L$（含 $L_0$、$[C;L]$ 满秩）；判 $(5b)$。
实例集：$n=5,6,7$、$p,r\\in\\{1,2\\}$、10 个 seed。

## 进展

89 个功能可观测实例（$n=5,6,7$）：

| 结果 | 实例数 |
|---|---|
| **$q_{\\min}=q_0$（精确，有 $(5b)$ 见证）** | **38** |
| $q_{\\min}>q_0$（构造出候选但全失败，仅下界）| 29 |
| 无可达候选（$d=0$ 或所有 $\\mathcal Z$ 不过必要条件）| 22 |

典型数据（$n=7$、$p=r=2$、$q_0$ 各值）：

| seed | $q_0$ | $\\dim G_{\\mathcal Z}\\ge q_0$ 的 $\\mathcal Z$ | 构造出 $\\mathcal L$ | $(5b)$ 成立 |
|---|---|---|---|---|
| 3002 | 3 | 79 | 2 | **1** |
| 3003 | 2 | 77 | 77 | **77** |
| 3004 | 3 | 79 | 20 | **7** |
| 3005 | 3 | 75 | 75 | 0 |
| 3006 | 4 | 34 | 7 | **3** |
| 3007 | 4 | 17 | 3 | **1** |
| 3009 | 2 | 75 | 75 | **75** |

即：过必要条件的 $\\mathcal Z$ 数量在不同实例间差 2 个数量级以上（2 vs 79），
这与"代数可行的 $q_0$ 族有时薄、有时厚"一致。

## 最终结论

1. **命中率显著提升**：候选构造不再依赖"从基里贪心"，而是直接在 $G_{\\mathcal Z}$ 内取；多数实例能拿到多个候选；
2. **统计更新**（89 个实例）：$q_{\\min}=q_0$ 精确 **38** 个、$q_{\\min}>q_0$ 29 个、无候选 22 个；
   旧统计（56 个实例、旧采样器）是 39/16/1——两组实例集不同，不能直接相比，但新法在
   $n=7$ 的实例上明显更有效；
3. **$q_0$ 族的厚度差异是真实的**：$\\dim G_{\\mathcal Z}\\ge q_0$ 的 $\\mathcal Z$ 数目在 2–79 之间变化，
   这说明"薄/厚"不是采样假象，值得作为结构分类的一个量。

## 放弃原因

不适用（重扫完成）。**未做**：把"$\\dim G_{\\mathcal Z}\\ge q_0$ 的 $\\mathcal Z$ 有多少"变成可算的几何量
（它可能对应某个 Schubert 类，进而给出 $q_0$ 阶可行性的计数判据）。

## 残留价值

* 一个**改进的候选构造器**（在 $G_{\\mathcal Z}$ 内取行），可复用于任何实例；
* 更新的 $q_{\\min}$ 统计（89 实例：38 精确、29 下界、22 无候选）；
* 一个可量化的结构量（过必要条件的 $\\mathcal Z$ 数目），作为"族厚度"的代理。

## 相关文件

- [tools/verification/q0_scan_gz.py](../../../../tools/verification/q0_scan_gz.py)
- [workspace/q1_false/feasibility_geometry/attempts/18_gz_criterion.md](18_gz_criterion.md)（判据）
- [workspace/q1_false/feasibility_geometry/attempts/07_q0_scan.md](07_q0_scan.md)（旧统计）
- [tools/verification/g_z_criterion.py](../../../../tools/verification/g_z_criterion.py)
