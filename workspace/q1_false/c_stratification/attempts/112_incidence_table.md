# 总 incidence 分层表（专家 52 号 §7 的目标计算）

> 2026-11-08。对 $k=3,\omega=2,q=3$ 的五个实例（$d=1$ 三个、$d=2$ 两个）按
> **精确 admissibility** $e+\dim X_S-\dim(E\cap X_S)=\omega$（专家 52 号的 (4.2)）列表：
> 每层的 $(\operatorname{rank}Q,\operatorname{rank}[P;Q],\dim X_S,t)$、是否可容许、纤维好坏、以及好点的
> full-row-rank lift。工具：`tools/verification/incidence_table.py`。**验证不是证明。**
> **注意**：本表是逐实例精确数据；其“秩层 = 不可约分量”的一般解释已在
> [attempts/115](115_k3_component_decomposition.md) 撤回（专家 53 号反例）。

## 目标

1. 用 (4.2) 而不是 "$X_S\not\subseteq E$" 判 admissibility；
2. 列出每层的维数、兼容秩、好坏、lift；
3. 看 $d=1$ 与 $d=2$ 的分层差异，验证专家命题的预测。

## 设想与理由

* 专家 52 号：正确的 admissibility 是 $e+\dim X_S-\dim(E\cap X_S)=\omega$，再加 $E+F_0\subseteq S$、$m\ge\omega-e$。
* 在 $e=0$ 的本组实例里，(4.2) 退化为 $\dim X_S=2$，正好排除 $\dim X_S=1$ 的层。
* $d=1$ 的例外层 $(\operatorname{rank}Q=0)$ 应有好点并能 lift；开层 $(\operatorname{rank}Q=1)$ 应全坏；
  $d=2,U_0=0$ 的所有可容许层应全坏（专家命题）。

## 做法

* 对每个实例，枚举射影底 $\mathbb P((E+F_0)^\perp)$ 上的 $\sigma$（小整数网格）；
* 算 $B=\ker\sigma$、$P=B^\top Z_1$、$Q=B^\top Z_2$、$\operatorname{rank}Q$、$\operatorname{rank}[P;Q]$、
  $\dim X_S=\omega-(\operatorname{rank}[P;Q]-\operatorname{rank}Q)$、$t=\dim(E\cap X_S)$；
* 检查 $e+\dim X_S-t=\omega$ 与 $m\ge\omega-e$；
* 对可容许层，取 $[P;Q]$ 的左零空间采样兼容对，算 $H,H_A$、$\ker H\subseteq\ker H_A$、gcd；
* 对好点回代 $R$（$R N_K=H[1:]$、$RAN_K=H_A[1:]$），检查 $\operatorname{rank}L=3$。

## 进展

表（每行一个 rank 层；$n$ = 枚举到的 $\sigma$ 数；lift = 好点中能回代出满行秩 $R$ 的个数）：

| 实例 | $d$ | $e$ | $(\operatorname{rank}Q,\operatorname{rank}[P;Q],\dim X_S,t)$ | 可容许 | $n$ | 好/坏 | lift |
|---|---|---|---|---|---|---|---|
| 179/589/794 | 1 | 0 | $(0,0,2,0)$ | ✓ | 1 | **1/0** | **1** |
| 179/589/794 | 1 | 0 | $(1,1,2,0)$ | ✓ | 3 | 0/3 | 0 |
| 138 | 2 | 0 | $(1,1,2,0)$ | ✓ | 2 | 0/2 | 0 |
| 138 | 2 | 0 | $(1,2,1,0)$ | ✗ | 2 | — | — |
| 261 | 2 | 0 | $(1,1,2,0)$ | ✓ | 1 | 0/1 | 0 |
| 261 | 2 | 0 | $(1,2,1,0)$ | ✗ | 3 | — | — |
| 261 | 2 | 0 | $(2,2,2,0)$ | ✓ | 9 | 0/9 | 0 |

观察：

1. **$d=1$**：两层。例外层 $(\operatorname{rank}Q=0)$ 有好点且能 lift 成满行秩 $R$；开层
   $(\operatorname{rank}Q=1)$ 全坏（与 104 的符号 gcd $\lambda t$ 一致）。
2. **$d=2$**：所有可容许层全坏；$\dim X_S=1$ 的层被 (4.2) 正确排除（$e+\dim X_S-t=1\ne2$）。
   这与专家命题（$k=3,\omega=2,q=3,d=2,U_0=0$ 全坏）一致。
3. (4.2) 与旧的 "$X_S\not\subseteq E$" 在本组 $e=0$ 实例上给出相同结论（因为 $e=0$ 时两者都等价于
   $\dim X_S=2$）；但一般 $e$ 时只有 (4.2) 正确。

## 最终结论

* 专家 §7 要求的表已给出：每层的维数、兼容秩、admissibility、好坏、lift。
* $d=1$ 的例外层是**唯一**有好点且能 lift 的层；$d=1$ 开层与 $d=2$ 可容许层全坏。
* (4.2) 的精确形式在本组实例上与被排除的 $\dim X_S=1$ 层一致。
* 这仍不是不可约分量分解：层是按秩数据分的，$\sigma$ 只枚举了小网格。

## 放弃原因

* 没有做**不可约分量**分解（专家要的是 per irreducible component；这里 per rank stratum）。
* $\sigma$ 只枚举了小整数网格；纤维只采样，gcd 只在 $d=1$ 开层有符号证书（$\lambda t$）。
* 没有对一般 $k$ 验证分量数/次数是否受控（专家 §7 的关键问题）。

## 残留价值

* 一张可复现的分层表，直接对应专家 §7 的八项输出中的前七项（缺 per-component 分解）。
* 证实 (4.2) 排除 $\dim X_S=1$ 层；证实 $d=1$ 例外层可 lift。
* 给修正的投影定理提供了 $k=3$ 的基线数据。

## 相关文件

* [tools/verification/incidence_table.py](../../../../tools/verification/incidence_table.py)
* [attempts/104](104_p2_constrained_locus.md)（$d=1$ 单例与符号 gcd）
* [attempts/107](107_projective_constrained_theorem_v2.md) / [108](108_layer_constancy.md)（分层与 (4.2)）
* [attempts/110](110_d2_all_bad_example.md)（$d=2$ 全坏命题）
* [attempts/111](111_qmin_check_and_d2_scan.md)（$q_{\min}$ 与 $q=2$ 判据）

## 状态

* 分层表：**[精确验证 5 实例]**（小网格 + 采样纤维）。
* (4.2)：**[已证-纸面]**（专家 52 号；本表核对）。
* 未做：不可约分量分解（一般断言已在 115 撤回）、一般 $k$、实点。
