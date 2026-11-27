# P1：用 $(*)$ 判据做全回归（结果：只证了不可行方向，可行方向缺"按秩析取"）

## 目标

按专家 §7 的 P1：把 $(*)$ 判据接到所有已有例子上做回归，看它能否替代"典型 gcd + 猜例外点"。

## 设想与理由

$(*)$：$e_0\in\operatorname{col}M(\theta)$ ⟺ $(5b)$ 成立。本模块用"左零空间 $\Rightarrow C_j=y_j^{\mathsf T}e_0$"给证书：
$(C_j)=(1)$ ⟹ 无任何 $\theta$ 可行。可行方向则需解理想 $I=(C_j)$ 并取实点。

## 做法

[regress_bezout.py](../../../../tools/verification/regress_bezout.py)：对每个（实例，阶）逐图卡跑
`(5a)` 构造 → 极大子式 → $M(\theta)$ → 左零空间 → $C_j$ → Gröbner → 分支（可行取解、不可行给证书、否则 `unknown`）。
加了预算：子式数 $\times D>48$ 的图卡跳过（符号左零空间过慢）。

## 进展

| 实例（阶）| 结论 | 说明 |
|---|---|---|
| **C4 反例 $q_0=3$** | **INFEASIBLE** | 两图卡理想均 $=(1)$ ✓（第三个独立证书）|
| C4 $q_0+1=4$ | UNKNOWN | 图卡退化（$d=0$ 或常数）|
| 公开例子 $q=2$ | UNKNOWN | 图卡退化（常数子式）|
| rand $5/1/2$ seed 3003、3005（$q_0=3$）| UNKNOWN | $\operatorname{rank}[V|Z]$ **不恒定** ⟹ 需按秩析取 |
| rand $5/1/1$ seed 3000（$q_0=2$）| UNKNOWN | 图卡退化 |
| rand $5/1/1$ seed 3006（$q_0=3$）| UNKNOWN | 一图卡秩不恒定；另一图卡**理想非 $(1)$** 但解不出有理/实见证 |
| rand $6/1/2$ seed 3003（$q_0=4$）| UNKNOWN | 三图卡秩均不恒定 |

（公开例子 $q=4$ 与 $q=5$ 未跑：$q=4$ 已由**整数障碍** $h=q+r_1=8$ 排除，$q=5$ 已由显式见证排除；
其图卡的 $M$ 为 $8\times224$，当前符号左零空间超预算。）

## 最终结论

1. **不可行方向可用**：C4 得到第三个独立证书（且是专家推荐的形式）；
2. **可行方向尚缺两件**：
   * **按秩析取**：$\operatorname{rank}[V|Z]$ 会在特殊 $\theta$ 处掉落，此时极大子式的尺寸也随之变化，
     当前实现固定尺寸 ⟹ 只能报 `unknown`（这正是专家提醒的"有限析取"）；
   * **实点求解**：理想 $I\ne(1)$ 时需要在实/有理点上求解（sympy 的 `solve` 只覆盖简单情形），
     严格做法是实量词消去（CAD），代价高；
3. **预算**：子式数 $\times D$ 随 $n$ 增长很快（公开例子 $q=4$ 已到 $8\times224$），
   符号左零空间是当前瓶颈；
4. 因此 $(*)$ 判据目前是**不可行方向的证书工具**，还不是通用判定器。

## 放弃原因

不适用（阶段性完成）。**未做**：按秩析取、实点求解、以及大图卡的预算优化。

## 残留价值

* $(*)$ 判据的**回归数据**（哪些情形现在能判、哪些不能，原因是什么）；
* C4 的第三个独立证书（可靠性最强的一个，因为它只依赖多项式恒等式）；
* 明确的两个缺口（按秩析取、实点求解），可直接作为下一步的实现清单。

## 相关文件

- [tools/verification/regress_bezout.py](../../../../tools/verification/regress_bezout.py)
- [tools/verification/bezout_rank_test.py](../../../../tools/verification/bezout_rank_test.py)
- [workspace/q1_false/feasibility_geometry/attempts/45_bezout_rank.md](45_bezout_rank.md)
- [workspace/for_expert/07_programme_report_and_open_problems-answer.md](../../../for_expert/archive/07_programme_report_and_open_problems-answer.md)（§6、§7）
