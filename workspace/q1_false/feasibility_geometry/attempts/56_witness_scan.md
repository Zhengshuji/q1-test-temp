# 见证优先的快速扫描：89 个实例 48 秒，74 个给出 $q_{\\min}$ 的**上界**（带证书）

## 目标

在不做（昂贵的）不可行性消元的前提下，快速、广覆盖地给 $q_{\\min}$ 上界，并看阶差的分布。

## 设想与理由

不可行方向要 Gröbner（单例可达 15 分钟，见 [attempts/55](55_qmin_sweep_slow.md)），
但**可行方向**只需构造 $\\mathcal L$ 并核 $(5a)$、$(5b)$、七条检查——纯有理算术，极快。
秩跌落点常是有理/简单点（[attempts/43](43_drop_locus.md)），所以取小分母有理 $\\theta$ 的候选集就能命中相当多实例。

## 做法

[witness_scan.py](../../../../tools/verification/witness_scan.py)：对每个实例、每阶、每图卡，
在 20 个候选 $\\theta$（$0,\\pm1,\\pm2,\\pm3,\\pm\\frac12,\\pm\\frac32,\\frac52,\\pm\\frac13,\\frac23,\\frac43,\\frac14,\\frac34,\\frac53,\\frac72$）上构造 $\\mathcal L$，
通过即 `FEASIBLE`；否则 `NO_WITNESS`（**不是**不可行证明）。结果写入 `data/qmin_upper.tsv`。

## 进展

**89 个实例（$n=5,6,7$；$p,r\\in\\{1,2\\}$；各 10 seeds），总耗时 48 秒**：

| 结果 | 数量 |
|---|---|
| 找到见证（$q_{\\min}\\le$ 该阶）| **74** |
| 无见证 | 15 |

**阶差分布（$q_{\\rm upper}-q_0$）**：

| 阶差 | 0 | 1 | 2 |
|---|---|---|---|
| 实例数 | **55** | 18 | 1 |

（平均 0.27。）

**按 $r$ 分组，阶差差异非常规律**：

| 组 | 平均阶差 |
|---|---|
| $r=1$（$p=1$）| 0.40 |
| $r=1$（$p=2$）| 0.43–0.50 |
| $r=2$（$p=1$）| 0.00 |
| $r=2$（$p=2$）| 0.00–0.12 |

即 **$r=2$ 的实例几乎总是 $q_{\\min}=q_0$**，$r=1$ 的实例常有 1（偶有 2）的阶差。
这是一个新的经验规律（此前只知道"$q_0$ 下界"与"某些实例有阶差"）。

**15 个无见证实例**分布较散（$p=r=1$ 6 个、$p=1,r=2$ 2 个、$p=2,r=1$ 4 个、$p=2,r=2$ 3 个），
多数 $q_0$ 已接近 $n_0-p$（如 $n=5,p=1,r=1$ seed 3009：$q_0=4$、$n_0=5$），可搜索的阶很少。

## 最终结论

1. **见证优先的扫描极快**（89 实例 48 s），且结论都带证书（见证 + 七条检查）；
2. **74/89 得到 $q_{\\min}$ 上界**；阶差以 0 为主（55），1 次之（18），2 仅 1 例；
3. **新经验规律**：阶差与 $r$ 强相关——$r=2$ 几乎没有阶差，$r=1$ 常有 1；
4. **边界**：`NO_WITNESS` 不是不可行证明；下界（$q<q_{\\min}$ 不可行）仍需 `joint_theta` 的 Gröbner，
   目前只有 4 个实例有完整两端证书（[attempts/55](55_qmin_sweep_slow.md)）。

## 放弃原因

不适用（阶段性完成）。**未做**：为 15 个无见证实例找见证（可能需更大候选集或代数点）；
以及把下界证书补到全部实例（代价问题）。

## 残留价值

* **89 实例的 $q_{\\min}$ 上界表**（`data/qmin_upper.tsv`），每条都有见证；
* **阶差 $\leftrightarrow$ $r$ 的经验规律**（值得向专家求证是否已知）；
* 明确的性能分工：可行方向廉价、不可行方向昂贵。

## 相关文件

- [tools/verification/witness_scan.py](../../../../tools/verification/witness_scan.py)
- `workspace/q1_false/feasibility_geometry/data/qmin_upper.tsv`（数据表，89 行）
- [workspace/q1_false/feasibility_geometry/attempts/55_qmin_sweep_slow.md](55_qmin_sweep_slow.md)
- [tools/verification/fast_rank.py](../../../../tools/verification/fast_rank.py)（典型层秩比较，诊断用）
