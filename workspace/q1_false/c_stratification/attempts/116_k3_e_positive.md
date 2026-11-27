# $k=3$, $e>0$ 的首批数据：$d=1$ 仍混合，$d=2$ 的“全坏”被打破

> 2026-11-08。按专家 53 号的 Priority 1，做 $k=3$、$e=1$ 的实例：用修正后的
> $\widetilde E_S+X_S=\mathbb C^\omega$ 与 $\operatorname{rank}(\varphi_S|_{\widetilde E_S})$ 分层。
> 结论：$d=1$ 的混合现象**存活**；但 $d=2$ 的“全坏”**不再成立**（$U_0\ne0$ 时可以有好点 + lift）。
> 状态：**精确验证**（采样）；不是一般定理。

## 目标

1. 在 $k=3,q=3,\omega=2,r=1$、$e=1$（$U_0\ne0$）时，检验：
   * $d=1$ 的“开层全坏 + 例外点好”是否还在；
   * $d=2,U_0=0$ 的受限全坏定理是否在 $U_0\ne0$ 时失效。
2. 用修正后的坐标条件（$\widetilde E_S$）与 $\operatorname{rank}(\varphi_S|_{\widetilde E_S})$ 分层。

## 设想与理由

* 专家 53 号指出：受限 $d=2$ 全坏定理依赖 $U_0=0$（因为 $V_0Z_2=-U_0Z_1=0$）；$U_0\ne0$ 时 $V_0Z_2=0$
  未必成立，全坏论证可能失败。
* $d=1$ 的混合机制是“纤维维数跳变”，与 $E$ 的大小无关；预期它在 $e=1$ 时仍成立。
* 修正后的 admissibility：$E+F_0\subseteq S$、$\widetilde E_S+X_S=\mathbb C^\omega$、$m\ge\omega-e$；
  $\dim(\widetilde E_S\cap X_S)=e-\operatorname{rank}(\varphi_S|_{\widetilde E_S})$。

## 做法

* 用 `tools/verification/incidence_table.py`（已更新种子列表），对 $e=1$ 的实例枚举射影底
  $\mathbb P((E+F_0)^\perp)$ 上的 $\sigma$；
* 算 $\operatorname{rank}Q$、$\operatorname{rank}[P;Q]$、$\dim X_S$、$t=\dim(\widetilde E_S\cap X_S)$、
  $e+\dim X_S-t$、$m\ge\omega-e$；
* 对可容许层采样兼容对，算 gcd 与好坏；对好点回代 $R$ 并检查 $\operatorname{rank}L=3$。

## 进展

$e=1$ 的实例（$k=3,q=3,\omega=2$；$n=7,p=2,r=1$）：

| seed | $d$ | 层 $(r_Q,r_{PQ},\dim X_S,t)$ | $e+\dim X_S-t$ | 可容许 | 好/坏 | lift |
|---|---|---|---|---|---|---|
| 1163 | 1 | $(0,0,2,1)$ | $2$ | ✓ | **1/0** | **1** |
| 1163 | 1 | $(1,1,2,1)$ | $2$ | ✓ | 0/3 | 0 |
| 753 | 2 | $(1,1,2,1)$ | $2$ | ✓ | 0/4 | 0 |
| 1081 | 2 | $(1,1,2,1)$ | $2$ | ✓ | **1/0** | **1** |
| 1327 | 2 | $(1,1,2,1)$ | $2$ | ✓ | **1/0** | **1** |
| 1491 | 2 | $(1,1,2,1)$ | $2$ | ✓ | **1/0** | **1** |
| 302 | 2 | $(1,2,1,0)$ | $2$ | ✓ | 无纤维点 | — |

观察：

1. **$d=1,e=1$（1163）仍是混合的**：例外层 $(r_Q=0)$ 好且能 lift；开层 $(r_Q=1)$ 全坏。
   机制与 $e=0$ 相同（$t=1$ 只表示 $E\subseteq X_S$，不改变纤维维数跳变）。
2. **$d=2,e=1$ 不全坏**：1081/1327/1491 有好点 + lift；753 全坏。所以受限全坏定理的
   $U_0=0$ 假设**是必要的**——$U_0\ne0$ 时 $d=2$ 也可以好（$q=3,\omega=2$ 可行）。
3. seed 302 的层 $(1,2,1,0)$ 在 $\sigma$ 层面可容许（$e+\dim X_S-t=1+1-0=2$），但采样没找到
   满足 $\operatorname{rank}H=2$ 的兼容对；可能是纤维为空或采样漏，需要精确检查。
4. 所有 $e=1$ 可容许层都满足 $t=1$（因为 $\dim X_S=2$，$E$ 被包含）；$\widetilde E_S+X_S=\mathbb C^2$。

## 最终结论

* **$d=1$ 的混合现象对 $e>0$ 稳健**：1163 与 $e=0$ 的三例同型（例外层好 + lift、开层坏）。
* **$d=2$ 的全坏是 $U_0=0$ 的特权**：$U_0\ne0$ 时 1081/1327/1491 都有好点并能 lift。
  这与专家 53 号对受限定理假设的提醒一致。
* 因此“$d=2$ 全坏”不能作为一般现象；正确的边界是 $U_0=0$（或 $V_0Z_2=0$ 的更强条件）。
* 这仍只是 $q=3,\omega=2$ 的层；$q_{\min}$ 需逐 $\omega$ 层检查。

## 放弃原因

* 采样，不是证明；好点的结构性刻画（何时 $d=2,e=1$ 好）未给出。
* seed 302 的“无纤维点”未精确判定。
* 只做了 $r=1$（$e\le1$）；$r>1$ 的 $e>1$ 未做。

## 残留价值

* 第一批 $e>0$ 数据，直接检验了专家 53 号的 Priority 1。
* 给出了受限全坏定理的**边界**：$U_0=0$ 时全坏，$U_0\ne0$ 时可好。
* $d=1$ 混合的稳健性证据，支持把它作为结构性现象保留。

## 相关文件

* [tools/verification/incidence_table.py](../../../../tools/verification/incidence_table.py)
* [attempts/112](112_incidence_table.md)（$e=0$ 表）
* [attempts/113](../../decision_algorithms/attempts/113_projective_theorem_corrected.md)（$\widetilde E_S$ 与 lifted incidence）
* [attempts/110](110_d2_all_bad_example.md)（$U_0=0$ 受限全坏）
* [attempts/115](115_k3_component_decomposition.md)（$k=3$ 一般线性性撤回）

## 状态

* $e=1$ 表：**[精确验证 6 实例]**（采样）。
* 结论：$d=1$ 混合稳健；$d=2$ 全坏仅 $U_0=0$。
* 未做：$d=2,e>0$ 好点的结构刻画、$r>1$、实点。
