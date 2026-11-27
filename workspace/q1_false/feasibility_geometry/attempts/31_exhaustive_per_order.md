# 逐阶判定升级为穷举版：阶区间修正、图卡枚举、等价类先筛整数障碍

## 目标

按专家 2026-11-03 §5 的第一条建议，把逐阶判定改成**枚举完整**的版本，并把四件事分开：
(1) 可行 $\\mathcal Z$ 的参数空间；(2) $(5a)$；(3) 整数障碍 $h\\ge q+r_1$；(4) 谱条件。

## 设想与理由

专家指出两处必须改：

* **阶区间**是 $[q_0,\\ n_0-p]$（$n_0=\\operatorname{rank}\\mathcal O_C$），不是 $[q_0,n-p]$；
* 候选枚举必须**穷尽** $\\operatorname{Gr}(d,K)$；随机抽 $Z$ 会漏解（异常实例的 $q=3$ 就漏了）。

做法：对 $\\operatorname{Gr}(d,K)$（$k=\\dim K$）逐**图卡**枚举（$d\\times d$ 单位块 + 自由参数），
按 $d(k-d)$ 选自适应网格（$\\le3$ 用 12 点网格、$=4$ 用 3 点网格、更大则跳过并标注）；
每个 $\\mathcal Z$ 先判 $(5a)$，再算**便宜的** $h=\\operatorname{rank}[\\mathcal L;CA;C]$：
若 $h\\ge q+r_1$ 直接记"整数障碍"并跳过（省掉昂贵的 $(5b)$）；否则才做 $(5b)$。

## 做法

[qmin_exact.py](../../../../tools/verification/qmin_exact.py)（新增）：
`python tools/verification/qmin_exact.py n p r seed` 或 `... fernando`（公开例子）。
穷举版把 $h$ 的计算与 $(5b)$ 的判定分开，使得"整数障碍"的识别是 $O(n^3)$ 的。

## 进展

**异常实例**（$n=7,p=r=2$，seed 4004；区间 $[2,3]$）：

| 阶 | $d$ | $\\dim\\operatorname{Gr}$ | 扫描 | $(5a)$-可行 | 成功 | 整数障碍 | $h$ |
|---|---|---|---|---|---|---|---|
| 2 | 3 | 0 | 1 | 1 | 0 | 0 | 5 |
| 3 | 2 | 2 | 243 | **18** | **2** | 0 | 5–6 |

$q_{\\min}=3$ ✓，并找到**新的**见证 $\\mathcal L=[L_0;(0,0,0,1,0,1,0)]$（与专家的 $\\mathcal L_*$ 不同）。
这也确认：此前"只有 3 个候选"是采样不足，而非无解。

**公开例子**（$n=8,p=r=2$；区间 $[3,6]$）：

| 阶 | $d$ | $\\dim\\operatorname{Gr}$ | 扫描 | $(5a)$-可行 | 整数障碍 | $h$ | $q+r_1$ |
|---|---|---|---|---|---|---|---|
| 3 | 3 | 3 | 2916 | **0**（网格未命中薄集）| — | — | 7 |
| 4 | 2 | 4 | 486 | **486** | **486** | 8 | 8 |
| 5 | 1 | 3 | 2916 | **2916** | 0 | 8 | 9 |

即：$q=4$ 的整族是 Type I（486/486，与 B.11 的 $h=q+r_1$ 一致）；$q=5$ 全在谱区（$h=8<9$），可行已知。

## 最终结论

1. **逐阶算法已升级**：阶区间正确、枚举按图卡穷尽、整数障碍先筛（便宜）、$(5b)$ 只对剩下的候选算；
2. **异常实例确认 $q_{\\min}=3$**，并给出新见证（回归测试 [regression_Lstar.py](../../../../tools/verification/regression_Lstar.py) 独立核验专家的 $\\mathcal L_*$）；
3. **公开例子的 $q=4$ 级整族 Type I** 在穷举下成立（486/486）；
4. **限制（诚实）**：网格枚举**不证明空集**——$q=3$ 在 2916 点上 0 命中，只能说明薄，不能说明不存在
   （我们另有商空间论证给出 $q=3$ 的显式可行 $\\mathcal L$，见 [attempts/22](22_fernando_failure_type.md)）。

## 放弃原因

不适用（升级完成）。**未做**：以消元替代网格（真正的"完全判定"需要对每个图卡解多项式方程组）。

## 残留价值

* 一个按专家建议重写的逐阶判定入口（阶区间、图卡枚举、整数先筛）；
* 两个可复算的基准：异常实例（$q_{\\min}=3$，18 可行/2 成功）与公开例子（$q=4$ 整族 Type I，486/486）；
* 明确的诚实边界：网格 ≠ 证明空集。

## 相关文件

- [tools/verification/qmin_exact.py](../../../../tools/verification/qmin_exact.py)
- [tools/verification/regression_Lstar.py](../../../../tools/verification/regression_Lstar.py)
- [workspace/q1_false/feasibility_geometry/attempts/29_anomaly_no_observer.md](29_anomaly_no_observer.md)（已撤回）
- [workspace/q1_false/feasibility_geometry/attempts/30_occlusion_corrected.md](30_occlusion_corrected.md)
