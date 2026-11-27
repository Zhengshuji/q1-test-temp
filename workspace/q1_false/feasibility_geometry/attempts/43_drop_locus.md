# 更正：`deg≥1` 不等于"所有 $\theta$ 都失败"——可行点恰在 gcd 的**掉落轨迹**上

## 目标

把"符号闭环"的 `INFEASIBLE` 判据做成**可靠**的；并解释它与网格结果的两次冲突。

## 设想与理由

一轮前把"图卡上 $\deg_\lambda\gcd\ge1$（一般 $\theta$）"直接当作"该图卡所有 $\theta$ 都失败"，据此输出 `INFEASIBLE`。
但 gcd 的 $\lambda$ 次数是 $\theta$ 的**半连续**函数：在特殊 $\theta$（gcd 的首项系数零点等）上它会**掉落**，
掉到 0 时 $(5b)$ **反而成立**。因此"一般位置失败"绝不能推出"处处失败"。

## 做法

1. 用 `symbolic_qmin.py` 在 6 个小图卡实例（参数 $\le2$）上同时跑符号判定与网格，统计冲突；
2. 修正 `decide_symbolic.decide`：**未逐个核验例外点前不输出 `INFEASIBLE`**，只报 `UNKNOWN` 并说明原因。

## 进展

修正前后对比（同一批 6 个实例）：

| 实例 | 修正前 | 修正后 | 网格 |
|---|---|---|---|
| $5/1/1$ seed 3000 | UNKNOWN | UNKNOWN | no(3) |
| $5/1/1$ seed 3002 | UNKNOWN | UNKNOWN | none(0) |
| $5/1/1$ seed 3006 | INFEASIBLE | **UNKNOWN** | no(39) |
| $5/1/2$ seed 3003 | **INFEASIBLE（错）** | **UNKNOWN** | **yes(7)** ← 冲突来源 |
| $5/1/2$ seed 3005 | **INFEASIBLE（错）** | **UNKNOWN** | **yes(2)** ← 冲突来源 |
| $6/1/2$ seed 3003 | INFEASIBLE | **UNKNOWN** | none(0) |

**结构发现**：这 6 个实例在 $q_0$ 阶、**每一个图卡**上都满足"一般 $\theta$ 下 $\deg\ge1$"——
即**一般位置全都失败**；而网格能在其中两例找到见证，说明那些见证点正是 gcd **掉落**到 0 的**例外 $\theta$**。

$$\boxed{\text{可行的 }\theta\ =\ \{\theta:\ \text{典型 } \gcd \text{ 在 } \theta \text{ 处掉到 } 0\}}$$

这解释了两件此前一直没解释的现象：
* $q_0$ 阶的可行集为什么是**薄集**（它是若干多项式的公共零点，而不是开集）；
* 为什么"抽样几乎必然失败、但确实存在见证"。

## 最终结论

1. **更正**：`deg≥1`（一般 $\theta$）**不能**推出"该图卡所有 $\theta$ 都失败"；`decide_symbolic` 已改为
   在未核验例外点时报 `UNKNOWN`，不再输出不可靠的 `INFEASIBLE`；
2. **结构发现**：在 $q_0$ 阶，一般 $\theta$ 全部失败，**可行点恰是 gcd 掉落轨迹上的例外 $\theta$**；
3. **C4 不受影响**：它的例外点（$\theta=5/4$、$4/5$）上 $\deg=1$（不是 0），即掉落轨迹**为空** ⟹
   整族不可行仍然成立（[attempts/41](41_symbolic_chart_gcd.md)）；
4. **下一步的确切目标**：算出"gcd 掉落"的多项式条件（gcd 各系数在 $\theta$ 上的公共零点，或子结式），
   把它并进判定——那才是 §8.1 真正的完整判据。

## 放弃原因

不适用（更正 + 发现完成）。**未做**：掉落轨迹的多项式刻画（子结式/系数组的公共零点），这是下一步。

## 残留价值

* 一个**可靠**的符号判定工具（不会再把"一般失败"当"处处失败"）；
* 一个**结构性解释**：$q_0$ 阶可行集的薄性来自"gcd 掉落轨迹"；
* 两次网格/符号冲突的原因（而非"谁的代码错了"）——这一次冲突是**语义**问题，不是实现 bug。

## 相关文件

- [tools/verification/decide_symbolic.py](../../../../tools/verification/decide_symbolic.py)（已修正）
- [tools/verification/symbolic_qmin.py](../../../../tools/verification/symbolic_qmin.py)
- [tools/verification/chart_gcd_analysis.py](../../../../tools/verification/chart_gcd_analysis.py)
- [workspace/q1_false/feasibility_geometry/attempts/41_symbolic_chart_gcd.md](41_symbolic_chart_gcd.md)（C4 的例外点已核验）
