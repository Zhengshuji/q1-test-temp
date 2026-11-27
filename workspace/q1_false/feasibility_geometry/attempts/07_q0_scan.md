# 最小阶上的正确统计：$q_{\min}=q_0$（39/56 精确）

## 目标

回答"$q_{\min}=q_0$ 吗"，**在 $q_0$ 阶上**判定 $(5b)$。此前做不到：闭包会加多行
（公开例：$q_0=3$ 而闭包 $=4$），所以所有基于闭包的"$\mathrm{cl}$"统计都不可靠。

## 设想与理由

用 Z-参数化（[z_generator.py](../../../../tools/verification/z_generator.py)）：
$\mathcal Z=KW$，$W\in\operatorname{Gr}(d,\,n-p-r)$，$d=n-p-q_0$，再从 $\mathcal Z^\perp$ 反构
$\mathcal L$（保持 $\operatorname{row}L_0\subseteq\operatorname{row}\mathcal L$）。
这样**每个样本都在最小阶**，$(5a)$ 过滤后判 $(5b)$：

* 找到 $(5b)$ 见证 ⟹ $q_0\le q_{\min}\le q_0$ ⟹ **$q_{\min}=q_0$（精确）**；
* 没找到 ⟹ 只有下界 $q_{\min}\ge q_0+1$（抽样不能排除薄集）。

## 做法

[q0_scan.py](../../../../tools/verification/q0_scan.py)：56 个功能可观测实例（$n=5,6$、$p,r\in\{1,2\}$、
10 个 seed），每实例 60 个 $q_0$ 阶样本（每个最多 6 次尝试）。

## 进展

| 结果 | 实例数 |
|---|---|
| **$q_{\min}=q_0$（精确，有显式见证）** | **39** |
| $q_{\min}>q_0$（仅下界；$q_0$ 阶样本全部失败）| **16** |
| $q_0$ 阶找不到代数可行样本（$(A)$ 是薄集）| 1 |

~~其中 **3 个**实例的障碍是"纯几何的（Type III）"~~ —— **此说法已更正**：
它们其实是 **Type I**（$h=q+r_1$ 恰在边界），由 B.9 解释。
见 [attempts/08_failure_types.md](08_failure_types.md)：228 个 $q_0$ 阶样本里 **Type III 为 0**。

## 最终结论

1. **$q_{\min}=q_0$ 在 39/56 个实例上被精确确定**——这是本项目第一次在**最小阶**上做正确统计；
2. 16 个实例 $q_{\min}>q_0$；其中 3 个的失败是**几何型**（$(A)$ 满维、$(5b)$ 全失败），
   正是专家建议重点研究的第三类失败；
3. 之前的 $\mathrm{cl}$ 统计（C1/C3）建立在会加多行的闭包上，**不能**用来讨论 $q_0$ 处的问题——
   本条取代那些结论。

## 放弃原因

不适用。**未做**：那 16 个实例的 $q_{\min}$ 具体值（需要逐阶检验，且 $q_0+1$ 阶同样可能薄集）；
以及 3 个几何型失败的结构解释（需要不变子空间/谱分析）。

## 残留价值

* **39 个精确的 $q_{\min}=q_0$**（每个都带显式增广，可复算）；
* 一个明确的**靶集**：3 个"$(A)$ 满维但 $(5b)$ 全失败"的实例，适合做结构定理的第一步；
* 一个方法论结论：**判定 $q_0$ 阶必须用 Z-参数化**，闭包与随机 $L$ 都不行。

## 相关文件

- [tools/verification/q0_scan.py](../../../../tools/verification/q0_scan.py)
- [tools/verification/z_generator.py](../../../../tools/verification/z_generator.py)
- [workspace/q1_false/feasibility_geometry/attempts/06_z_generator.md](06_z_generator.md)
- [proof/fernando_2gap/](../../../../proof/fernando_2gap/README.md)
