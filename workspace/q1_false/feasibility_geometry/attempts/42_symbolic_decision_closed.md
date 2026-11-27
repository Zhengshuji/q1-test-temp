# 符号闭环：逐阶判定"可行给见证、不可行给 gcd 证书"

## 目标

把 §8.1 的两半（$(5a)$ 层的消元、谱层的符号 gcd）合成一个**可下结论**的逐阶判定入口，
彻底摆脱网格。

## 设想与理由

专家 §8.1 的要求是"在图卡上解约束并证明代数集被完全描述"。有了 sympy：

* **谱层**：$P_{\mathcal Z}(\lambda)$ 的极大子式在 $\mathbb Q(\theta)[\lambda]$ 中的 gcd，
  其次数 $\deg_\lambda$ 决定该图卡"一般 $\theta$"下 $(5b)$ 成立（$\deg=0$）或失败（$\deg\ge1$）；
* **可行方向**：$\deg=0$ 时挑有理 $\theta$，构造 $\mathcal L$，跑七条一致性检查 ⟹ 见证；
* **不可行方向**：所有图卡 $\deg\ge1$ ⟹ gcd 证书（例外 $\theta$ 取 gcd 表示式的分母零点，需逐个核验）。

## 做法

[decide_symbolic.py](../../../../tools/verification/decide_symbolic.py)：
逐图卡 `analyse_chart` → 按 $\deg$ 分支 → 见上。输出三种结论：`FEASIBLE`（带见证）、`INFEASIBLE`（gcd 证书）、`UNKNOWN`（说明缺哪一步）。

## 进展

**C4 反例（$q_0=3$）**：两图卡 $\deg=2$、例外点（$5/4$、$4/5$）上 $\deg=1$（见 [attempts/41](41_symbolic_chart_gcd.md)）
$$\Longrightarrow\ \texttt{INFEASIBLE}\quad\text{（gcd 证书；无网格）}$$

**公开例子（$q=5$）**：四图卡全 $\deg=0$ ⟹ 取 $\theta=0$，得**显式 5 行见证**并通过七条一致性检查：

$$\mathcal L=\begin{pmatrix}
-2&-1&-2&-3&-1&3&2&0\\
1&-1&-2&1&0&2&0&1\\
11/36&1&0&0&0&0&0&0\\
-1/6&0&1&0&0&0&0&0\\
35/36&0&0&1&0&0&0&0
\end{pmatrix}\qquad\Longrightarrow\ \texttt{FEASIBLE}$$

耗时：C4（2 图卡）+ 公开例子（4 图卡 × 56 子式）共约 **265 s**。

## 最终结论

1. **逐阶判定已闭环**（对参数 $\le3$ 的图卡）：可行 ⟹ 见证（含七条检查）；不可行 ⟹ gcd 证书；
2. **不再依赖网格**：C4 与公开例子 $q=5$ 都得到确定结论；
3. 两个长期悬着的问题现在各有确定答案：
   * C4 的 $q_0$ 阶不可行（**两套独立证明**：射影满射 + 符号 gcd）；
   * 公开例子 $q_{\min}=5$（$q=5$ 有显式见证，$q\le4$ 由整数障碍与 gcd 证书排除）。

## 放弃原因

不适用（闭环完成）。**未做**：
* 例外 $\theta$ 的**自动**核验（目前 C4 已手工核完；工具只报告分母零点）；
* 参数 $\ge4$ 的图卡（子式数与 gcd 成本上升，未测）；
* $(5a)$ 层的符号消元与谱层**合并**成单一判定（目前 $(5a)$ 由见证侧用 `condA` 核验）。

## 残留价值

* 一个**可下结论**的逐阶判定入口（三种结论 + 说明）；
* 公开例子 $q=5$ 的**新见证**（5 行，$\theta=0$，通过七条检查）；
* 明确的剩余工作（例外点自动化、参数 $\ge4$、与 $(5a)$ 层合并）。

## 相关文件

- [tools/verification/decide_symbolic.py](../../../../tools/verification/decide_symbolic.py)
- [tools/verification/chart_gcd_analysis.py](../../../../tools/verification/chart_gcd_analysis.py)
- [tools/verification/consistency_checks.py](../../../../tools/verification/consistency_checks.py)
- [workspace/q1_false/feasibility_geometry/attempts/41_symbolic_chart_gcd.md](41_symbolic_chart_gcd.md)
