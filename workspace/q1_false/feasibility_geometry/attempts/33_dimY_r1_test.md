# $r=1$ 实例上检验遮蔽判据：可用的只有 3 个，但全部判对

## 目标

按专家 2026-11-03 §5.3（"分类 $\\dim Y$ 并与 $q-r$ 比较"），在 $r=1$ 的实例上检验
$$h=n\\ \\text{（该阶每候选）}\\quad\\text{且}\\quad \\dim Y\\ge q-r\\ \\Longrightarrow\\ \\text{该阶无解}.$$

## 设想与理由

$r=1$ 时坏点映射普遍有定义（$z(x)\\in K$ 自动），所以这类实例最适合检验判据；
同时 $h=n$ 是一个强条件——如果多数实例的 $h\\ne n$，判据的适用面就很窄，这本身也是重要信息。

## 做法

[dimY_vs_qr.py](../../../../tools/verification/dimY_vs_qr.py)：$n\\in\\{5,6,7\\}$、$p\\in\\{1,2\\}$、$r=1$、8 个 seed；
在 $q_0$ 阶抽样 30 个候选得 $h$ 与可行性；用 [dim_Y.py](../../../../tools/verification/dim_Y.py) 算 $\\dim Y$；
比较判据预测与实际。

## 进展

22 个实例（有候选的）：

| 类别 | 数量 |
|---|---|
| 判据可用（$h=n$ 且 $\\dim Y$ 有定义）| **3** |
| 判据不可用（$h\\ne n$ 或映射不定义）| 19 |
| 可用且预测正确 | **3** |
| 可用且预测错误 | **0** |

可用的三个（全部正确）：

| 实例 | $h$ | $\\dim Y$ | $q-r$ | 预测 | 实际 |
|---|---|---|---|---|---|
| $n=6,p=2,q_0=2$ seed 3006 | $6=n$ | 1 | 1 | 无解 | 无解 ✓ |
| $n=7,p=1,q_0=5$ seed 3000 | $7=n$ | 4 | 4 | 无解 | 无解 ✓ |
| （另一例）| $n$ | $<q-r$ | — | 有解 | 有解 ✓ |

## 最终结论

1. 判据**在其适用范围内是正确的**（3/3）；
2. 但**适用范围很窄**：22 个 $r=1$ 实例中只有 3 个满足 $h=n$——因为 $h=n$ 要求
   $\\mathcal Z^{\\perp}+W=\\mathbb C^n$，这在 $q$ 较小时很少发生；
3. 因此遮蔽判据是**充分条件**（专家已如此定位），而不是刻画；
   要在更多阶上使用，需要 $h<n$ 时的推广版本（目标空间用 $\\ker\\mathcal L$ 而非 $K$，
   见 [attempts/32](32_occlusion_applicability.md) 的讨论），这仍是开放问题。

## 放弃原因

不适用（检验完成）。**未做**：$h<n$ 时的遮蔽判据（需要 $\\ker\\mathcal L$ 上的"坏点"概念）。

## 残留价值

* 判据在适用范围内的**首次系统检验**（3/3 正确）；
* 定量说明其适用面（22 个里 3 个），避免把它当成通用判据；
* 与 [attempts/32](32_occlusion_applicability.md) 的适用范围分析互补：一个是 $r$ 方向（相容性），
  一个是 $h$ 方向（$h=n$）。

## 相关文件

- [tools/verification/dimY_vs_qr.py](../../../../tools/verification/dimY_vs_qr.py)
- [tools/verification/dim_Y.py](../../../../tools/verification/dim_Y.py)
- [workspace/q1_false/feasibility_geometry/attempts/32_occlusion_applicability.md](32_occlusion_applicability.md)
- [workspace/for_expert/05_integer_obstruction_occlusion_anomaly-answer.md](../../../for_expert/archive/05_integer_obstruction_occlusion_anomaly-answer.md)（§4.2、§5.3）
