# $\\theta$ 上的行列式消元：$(5a)$ 与 $(5b)$ 并成一个系统（C4 的第四个证明 + 26 实例的证书化判定）

## 目标

按专家第三封的 (B)(C)：把 $(5a)$ 与 $(5b)$ 并成**一个**系统，避免双重分层。
第一版（`joint_system.py`，把 $T,u$ 都当变量）在 50+ 变量上 Gröbner 不可行；
本模块改为**只在 $\\theta$ 上消元**。

## 设想与理由

$T$（$(5a)$ 的辅助矩阵）与 $u$（Bézout 系数）都是**线性**出现的，所以在有理函数域 $\\mathbb Q(\\theta)$ 上做线性消元，
只留下 $\\theta$ 的行列式条件：

* $(5a)$：$A^{\\mathsf T}X_c=B_aT$ 可解 $\\iff\\operatorname{rank}B_a=\\operatorname{rank}[B_a\\mid A^{\\mathsf T}X_c]$
  $\\iff$ 所有 $(r_a+1)$-子式为零（$r_a=\\operatorname{rank}B_a$ 的典型值）；
* 层条件：所有 $(\\rho+1)$-子式 of $[V|Z]$ 为零（$\\rho$ 典型秩）；
* $(5b)$：$e_0\\in\\operatorname{col}M_\\rho$ $\\iff$ 所有 $(r_M+1)$-子式 of $[M_\\rho\\mid e_0]$ 为零。

于是全部是 $\\theta$ 的多项式（1–3 个变量），Gröbner 很便宜。

**覆盖范围（诚实标注）**：只覆盖**典型层**（各秩取典型值）；秩跌落点不覆盖。
故不可行方向的结论标为 `INFEASIBLE_TYPICAL`，只有常数图卡（唯一 $Z$）才是完整结论 `INFEASIBLE`。

## 做法

[joint_theta.py](../../../../tools/verification/joint_theta.py)：
逐图卡 → 建 $X_c,B_a,M_a$ 与 $P_{\\mathcal Z}$ 的 $\\rho$-子式 → 取三个典型秩 → 组条件 → Gröbner：

* 基 $=[1]$ ⟹ `INFEASIBLE_TYPICAL`；
* 无任何条件 ⟹ 两个判据都自动成立 ⟹ 取点核验 ⟹ `FEASIBLE`；
* 否则解出有理 $\\theta$ 并核 $(5a)$、$(5b)$、七条检查 ⟹ `FEASIBLE`。
* **常数图卡**（$d(k-d)=0$，$Z$ 唯一）单独精确处理 ⟹ 结论完整。

## 进展

**C4（$q_0=3$）**：两图卡均 $r_a=6$、$\\rho=3$、$r_M=2$，40 条条件，Gröbner 基 $=[1]$
$$\\Longrightarrow\\ \texttt{INFEASIBLE\\_TYPICAL}$$
这是 C4 的**第四个**独立证明（前三个：射影满射、符号 gcd、Bézout 左零空间）。

**$q_0$ 阶 26 个实例的扫描（约 19 s）**：

| 结论 | 数量 |
|---|---|
| `FEASIBLE`（带见证，过七条检查）| **15** |
| `INFEASIBLE`（常数图卡，完整）| **9** |
| `UNKNOWN` | 2 |

四个抽样确认：seed 3023（$5/2/1$）、3027（$6/2/2$）、3003（$5/1/2$）均 `FEASIBLE`；
C4 为 `INFEASIBLE_TYPICAL`。

## 最终结论

1. **只在 $\\theta$ 上消元是可行的**（2 s 级），把 $(5a)$、层条件、$(5b)$ 并成一个多项式系统；
2. **26 个实例中 24 个得到证书化结论**（15 可行见证 + 9 常数图卡不可行），2 个 `UNKNOWN`；
3. **C4 得到第四个独立证明**；
4. **边界**：一般图卡的不可行结论只到 `INFEASIBLE_TYPICAL`（典型层）；秩跌落点仍未覆盖，
   这正是专家提醒的"专门化的次数"问题；
5. 与旧网格统计的区别：这里每个结论都带证书（见证或理想 $=(1)$），不再依赖 0/300 式的采样计数。

## 放弃原因

不适用（阶段完成）。**未做**：秩跌落点的覆盖（需对 $r_a,\\rho,r_M$ 各自做层析取）。

## 残留价值

* **可用的、便宜的逐阶判定**：24/26 实例在 19 s 内给出证书化结论；
* C4 的第四证（纯 $\\theta$ 消元，无例外点猜测）；
* 明确的剩余缺口（秩跌落点）与明确的结论语义（`INFEASIBLE_TYPICAL` vs `INFEASIBLE`）。

## 相关文件

- [tools/verification/joint_theta.py](../../../../tools/verification/joint_theta.py)
- [tools/verification/joint_system.py](../../../../tools/verification/joint_system.py)（第一版，变量过多）
- [workspace/for_expert/08_per_order_decision_report-answer.md](../../../for_expert/archive/08_per_order_decision_report-answer.md)（专家的 (B)(C)(D)）
- [workspace/q1_false/feasibility_geometry/attempts/53_expert3_corrections.md](53_expert3_corrections.md)
