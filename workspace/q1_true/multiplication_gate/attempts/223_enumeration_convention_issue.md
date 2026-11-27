# 单门实现（八）：$\operatorname{Gr}(2,3)$ 枚举的约定问题与修正方案

> 2026-11-09。尝试在 168 实例上枚举 $W_L$ 里所有 2 维 $V$ 的好性（$\operatorname{Gr}(2,3)=\mathbb P^2$）。
> sympy 版本枚举 124 个平面得 0 个好点，**与已验证的 168 见证矛盾**；定位到两个方法问题。
> 状态：**方法记录（负结果）**，正确枚举待重做。

## 目标

在 168 实例上确定好 $V$ 的集合，检验“可行核离散”猜想。

## 设想与理由

$W_L=\operatorname{span}\{e_4,e_5,e_6\}$，$V$ 由法向量 $w=(a,b,c)$ 参数化；
对每个 $w$ 算 $\mathcal L_V$、$H,H_A$、铅笔子式 gcd。

## 做法与发现的问题

### 问题 1：只取两行子式，漏掉第三行

168 的 $q=3$：$H$ 是 $3\times4$，$\operatorname{rank}H=2$。
第三行（不可见方向）的 $P$ 行**不一定为零**（在我用的坐标/约定下 $H_{A,3}\ne H_{A,2}$），
所以只对两行取 $2\times2$ 子式会误判。
正确做法：对 $3\times4$ 的 $P$ 取**全部** $2\times2$ 子式，gcd 为常数才判好。

### 问题 2：sympy 与项目 `linalg_q` 的约定可能不同

168 见证在 `check_candidate` 下通过；但用 sympy 手算 $H_A=LAN$ 得到不同矩阵。
在排除笔误之前，以**项目工具**（`linalg_q.mul`、`check_candidate`）为准；
枚举脚本必须复用它，不能用 sympy 重写一遍矩阵乘法。

## 进展

* 定位了“0 个好点”的两个方法原因；
* 结论：该枚举结果**无效**，不能用来支持或反驳离散性；
* 给出正确的重做方案。

## 最终结论

* 222 的单族结论（$V_t$ 只有 $t=0$）仍以 `check_candidate` 的数值/符号一致性为准，但其“只有两行”的推导需用全子式复核；
* $\operatorname{Gr}(2,3)$ 的完整枚举必须用项目工具重做；
* 在重做之前，不对“离散性”下结论。

## 放弃原因

* 枚举脚本未使用项目约定；
* 未取全部子式；
* 时间用在了定位方法问题上。

## 残留价值

* 明确的 bug/约定清单；
* 下一步的正确实现路径；
* 避免把无效枚举当成反例或证据。

## 相关文件

* [attempts/168](../../../q1_false/c_stratification/attempts/168_dimWL3_witness.md)
* [attempts/221](221_variable_kernel_family_test.md)、[222](222_168_family_symbolic.md)
* [tools/verification/c2_dimWL3_witness.py](../../../../tools/verification/c2_dimWL3_witness.py)

## 状态

* 方法记录：**[已记录]**。
* 正确枚举：**[未做]**。
