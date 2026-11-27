# 遮蔽判据的适用范围：$z(x)\in K$ 的相容性条件

## 目标

落实专家 2026-11-03 §4.2 的判据（$h=n$ 且 $\\dim\\overline{\\Phi(\\mathbb P(V))}\\ge q-r$ ⟹ 该阶无解），
并确定它在什么实例上**可用**。

## 设想与理由

判据的坏点映射是
$$\\Phi:\\ x\\in V=\\ker[C;CA]\\ \\longmapsto\\ \\operatorname{span}z(x),\\qquad
z(x)=(\\lambda(x)I-A)x,\\quad \\lambda(x)=\\frac{L_0Ax}{L_0x}.$$
要让它有定义并且坏点落在 $K=\\ker[C;L_0]$ 里，必须同时满足
$$Cz(x)=0\\ \\text{（自动，因 }C x=CAx=0\\text{）},\\qquad L_0z(x)=0\\iff \\lambda(x)\\,L_0x=L_0Ax .$$
当 $r=1$ 时 $\\lambda(x)$ 就是标量 $L_0Ax/L_0x$，自动成立。
当 $r\\ge2$ 时这是一个**2 个方程、1 个未知数**的组，通常不相容——
只有当 $L_0$ 的所有行在 $V$ 上共享同一个"广义 Rayleigh 商"时才可能。

## 做法

[dim_Y.py](../../../../tools/verification/dim_Y.py)：在 $V$ 的参数空间上用**精确有理插值**算
$x\\mapsto z(x)$ 的 Jacobian 秩（投影维数 $=\\operatorname{rank}-1$）；
先检查 $z(x)\\in K$（$Cz=0$ 且 $L_0z=0$），不相容则明确报告"不可用"。

## 进展

| 实例 | $r$ | $z(x)\\in K$ | $\\dim Y$ | $q-r$ | 判据是否预测无解 | 实际 |
|---|---|---|---|---|---|---|
| C4 反例（$q=3$）| 2 | **是** | **1** | 1 | 是（$1\\ge1$）| 无解 ✓ |
| 公开例子（$q=4$）| 2 | 否 | — | 2 | 不可用 | （整数障碍已排除该阶）|
| 公开例子（$q=5$）| 2 | 否 | — | 3 | 不可用 | 可行 |
| 异常实例（$q=3$）| 2 | $V\\subseteq\\ker L_0$ ⟹ 不定义 | — | 1 | 不可用 | 可行 ✓ |

即：

1. **C4 是判据适用的实例**：$\\dim Y=1\\ge q-r=1$，正确预测整族无解（与其独立证明一致）；
2. **公开例子不可用**：$L_0$ 的两行在 $V$ 上不共享同一个 $\\lambda$，$z(x)\\notin K$；
3. **异常实例不可用**：$V\\subseteq\\ker L_0$，坏点映射处处不定义——这本身就解释了它为何**不**被遮蔽。

## 最终结论

1. 专家的判据（$h=n$ 且 $\\dim Y\\ge q-r$）**在 C4 上验证有效**（$\\dim Y=1$、$q-r=1$）；
2. 但它的**适用性**不是自动的：需要 $z(x)\\in K$ 的相容性条件
   $$\\forall x\\in V:\\quad (L_{0,1}Ax)(L_{0,2}x)=(L_{0,2}Ax)(L_{0,1}x)\\ \\text{（一般 }r\\ge2\\text{ 时取所有行对）};$$
3. 三个基准实例恰好覆盖三种情形：适用且预测成功（C4）、适用性失败（公开例子）、映射不定义（异常实例）；
4. 因此"遮蔽判据"目前是一个**部分**判据：$r=1$ 时普遍可用，$r\\ge2$ 时需要上述相容性；
   对一般 $r\\ge2$ 的版本仍是开放问题（需要把 $\\ker\\mathcal L$ 而非 $K$ 作为目标空间）。

## 放弃原因

不适用（适用范围界定完成）。**未做**：一般 $r\\ge2$ 下的遮蔽判据（目标应改为 $\\ker\\mathcal L\\supseteq Z$）。

## 残留价值

* 判据在 C4 上的**定量验证**（$\\dim Y=1$、$q-r=1$）；
* 明确的**适用条件**（$z\\in K$ 的相容性），避免在不适用的实例上误用；
* 三个基准实例覆盖三种情形，可作为后续实现的回归用例。

## 相关文件

- [tools/verification/dim_Y.py](../../../../tools/verification/dim_Y.py)
- [workspace/q1_false/feasibility_geometry/attempts/30_occlusion_corrected.md](30_occlusion_corrected.md)
- [workspace/q1_false/feasibility_geometry/attempts/26_c4_proof.md](26_c4_proof.md)
- [workspace/for_expert/05_integer_obstruction_occlusion_anomaly-answer.md](../../../for_expert/archive/05_integer_obstruction_occlusion_anomaly-answer.md)（§4）
