# Class I 的 $d=1$：两半已证，第三半是猜想

## 目标

推进 B.18e（$d=1$ 整族不可行）。本轮把它拆成三条，证了前两条。

## 设想与理由

$d=1$ 时 $\mathcal Z=\langle z\rangle$。谱条件只依赖 $z$（B.18c/B.18d）；可容许性依赖 $\mathcal L$。于是分情况：

* $z\in V$：$\mathcal Z\subseteq V$ ⟹ $S=\mathcal Z$ ⟹ B.16b 的 $(5a)\Rightarrow A(S)\subseteq\mathcal Z$ 迫使 $Az\in\langle z\rangle$ ⟹ $z$ 是 $A$ 在 $\ker c$ 里的特征向量 ⟹ 与可观测矛盾 ⟹ **不可容许**；
* $z\notin V$（标准坐标下 $z_2\ne0$）：$\operatorname{rank}[C;\mathcal L]=n-1$ ⟹ $\operatorname{rank}[\mathcal L;CA;C]\in\{n-1,n\}$；
  若 $=n-1$，则 $cA\in\operatorname{row}[C;\mathcal L]$，于是 $cAz=0$；但伴矩阵坐标下 $cAz=(Az)_1=z_2\ne0$，矛盾。
  ⟹ $\operatorname{rank}[\mathcal L;CA;C]=n$ ⟹ $(5a)$ **自动成立**。

## 做法

1. 把上述两条写成证明（B.18e 第 1、2 条）；
2. 用伴矩阵实例（$n=5,6,7$）核验分情况的行为（$z\in V$ vs $z_2\ne0$）。

## 进展

**已证**：

| 情形 | 结论 |
|---|---|
| $z\in V$ | **不存在**可容许的 $\mathcal L$ 使 $\ker[C;\mathcal L]=\langle z\rangle$ |
| $z_2\ne0$ | 可容许性**自动成立** |

**证据（数值，$n=5,6,7$）**：

| 类别 | 样本 | 可容许 |
|---|---|---|
| $z\in V$ | 77 | **0** ✓（与第 1 条一致）|
| $z_2\ne0$ | 821 | **821** ✓（与第 2 条一致）|

**剩下的猜想（第 3 条）**：$z_2\ne0\Rightarrow z\in\operatorname{im}\psi$（$821/821$ 支持）。
若成立，则由三条合并得 $d=1$ 整族不可行，进而（配合 B.18b）$q_{\min}=n-1$。

## 最终结论

1. **B.18e 的两半已证**（$z\in V$ 不可容许；$z_2\ne0$ 自动可容许），且与数值完全吻合；
2. 整个 $d=1$ 分类**只剩一条猜想**：$z_2\ne0\Rightarrow z\in\operatorname{im}\psi$；
3. 这条猜想的形状很好：它是关于 B.18d 中多项式 $P_z$ 的纯代数陈述（"$P_z$ 不是非零常数"），
   与 $(5a)$ 无关了——即困难已完全转移到**像的刻画**上。

## 放弃原因

不适用（三条中两条已证）。

## 残留价值

* 两条**短证明**（特征向量排除、$cA\in\operatorname{row}[C;\mathcal L]$ 的矛盾）；
* 把 $d=1$ 的全部剩余困难**隔离**成一个关于 $P_z$ 的陈述；
* 分情况计数（$0/77$ 与 $821/821$）作为两条证明的独立校验。

## 相关文件

- `docs/02` B.18b/c/d/e、B.16b
- `tools/verification/class_I_d1.py`
- `attempts/84_class_I_d1.md`
