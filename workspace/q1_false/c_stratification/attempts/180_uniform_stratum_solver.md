# 统一层求解器：一个工具覆盖任意 $(q,\omega,c)$ 的参数化流程

> 2026-11-08。把 165/166 的逐层脚本合并成一个统一工具
> [tools/verification/stratum_solver.py](../../../../tools/verification/stratum_solver.py)：
> 给定 $(A,C,L_0,q,\omega)$，自动算 $c=k-\omega$、$W_L$、在 $\operatorname{Gr}(c,W_L)$ 中枚举 $V$、
> 解可容许方程、检验铅笔秩、构造 $L$ 并跑七条检查。状态：**工具 + 精确验证**。

## 目标

用**一个**入口实现“统一方法”，避免每个 $(q,\omega,c)$ 写一个脚本；同时明确它是**搜索**而非完备判定。

## 设想与理由

方法本身与 $(q,\omega,c)$ 无关：
1. $c=k-\omega$，$W_L=\ker[L_0N;L_0AN]$，$V\in\operatorname{Gr}(c,W_L)$；
2. $\operatorname{Ann}(V)=\langle h_0,u_1,\dots,u_{\omega-1}\rangle$，$h_0=L_0N$；
3. 底部行 $h_i=a_ih_0+\sum_j b_{ij}u_j$，可容许 $H_A|_V=0$ 对 $(a,b,g)$ 线性；
4. $\operatorname{rank}H=\omega$ 等价于 $(b_{ij})$ 的 $(q-1)\times(\omega-1)$ 矩阵秩 $\omega-1$；
5. 铅笔 $\lambda H-H_A$ 的 $\omega$ 阶子式 gcd 为常数；
6. 构造 $L$、验证 $\operatorname{rank}[C;L]=\operatorname{rank}C+q$ 与七条检查。

逐层只是把上面的矩阵写出来；工具用同一段代码处理任意 $(q,\omega)$。

## 做法

工具：[tools/verification/stratum_solver.py](../../../../tools/verification/stratum_solver.py)

接口：
```python
solve(A, C, L0, q, omega=None, seed=0)
# omega 缺省 q-1；返回 (L 或 None, info)
```
步骤对应上面的 1–6；$V$ 的枚举是 $\operatorname{Gr}(c,W_L)$ 的**有限有理采样**（$d=\dim W_L=c$ 时唯一；
$d>c$ 时随机系数 + RREF 去重）；自由参数（可容许解空间）也是有限随机采样。

## 测试结果（精确有理算术）

| 实例 | $(q,\omega)$ | 结果 |
|---|---|---|
| seed 10 | $(3,2)$ | **FOUND**（$\dim W_L=2$，forced）|
| seed 16 | $(3,2)$ | none（forced，$b$ 全强制；165/172 已证不可行）|
| seed 21 | $(3,2)$ | 同上 |
| seed 16 | $(4,3)$ | none（$c=1$，$L\in\mathbb P(W_L)$ 采样）|
| seed 21 | $(4,3)$ | 同上 |
| 168 实例 | $(3,2)$ | **FOUND**（$\dim W_L=3$，非 forced）|

seed10 与 168 的 FOUND 都通过 `check_candidate` 的七条检查；16/21 的 none 与 165/172 的不可行证书一致。

## 确定性模式与状态字段（2026-11-08 补）

`solve(..., mode='random'|'grid')`：
* `random`（默认）：随机 $V$ 枚举 + 随机自由参数；
* `grid`：确定性网格——$V$ 的系数矩阵取 $\{-1,0,1\}^{d\times c}$（上限 200），自由参数取“零 + 单坐标 $\pm1$ + 双坐标 $\pm1$”组合。

返回值 `info['status']` 三态：
* `feasible`：找到见证（$L$ 通过七条检查）；
* `none in search` + `infeasible: True`（$\dim W_L=c$）：行空间证书；
* `none in search`（其余）：搜索失败，不是证明。

测试（两种模式）：
| 实例 | random | grid |
|---|---|---|
| seed 10 | FOUND | FOUND |
| seed 16/21 | none + infeasible 证书 | none + infeasible 证书 |
| 168（$\dim W_L=3$）| FOUND | FOUND |

## 不可行证书（2026-11-08 补）

工具现在对每个 $V$、每个底部行先做行空间判据：
$$e_b\in\operatorname{rowspace}(\mathrm{Des}_i)\iff b_i\ \text{被强制为 }0.$$
若所有底部行都被强制，则 $V$ 不可能给出 $\operatorname{rank}H=\omega$；记录 $\alpha_i$ 证书。
当 $\dim W_L=c$（$V$ 唯一）且所有行被强制时，返回 `infeasible: True` 与证书。

seeds 16/21（$q=3,\omega=2$）现在输出：
```
16 none {'infeasible': True, 'certificate': {'alphas': [(-1,0),(-1,0)]}}
21 none {'infeasible': True, 'certificate': {'alphas': [(-1,0),(-1,0)]}}
```
与 165/172 的证书一致。

## 进展

* 一个统一入口覆盖任意 $(q,\omega,c)$（不再逐层写脚本）；
* 在 5 个已知实例上复现了逐层脚本的结论；
* “none”明确标为搜索失败，不是不可行证明。

## 最终结论

* 统一方法可以工具化，且已在已知实例上验证；
* 工具的完备性仍受限于 $V$ 与自由参数的有限采样；
* 要得到“不可行”的证明，仍需 165 的行空间证书或符号消元。

## 放弃原因

* 未做 $\operatorname{Gr}(c,W_L)$ 的穷尽枚举（有理参数化 + 消元）；
* 不可行证书已加（$\dim W_L=c$ 时）；$\dim W_L>c$ 仍只是搜索；
* 未做性能优化（当前 $q\le4$、$k\le4$ 够用）。

## 残留价值

* 一个可复用的统一工具，替代逐层脚本；
* 为后续 $q=4$、$c=1$ 的符号消元提供代码骨架。

## 相关文件

* [attempts/165](165_c2_forced_plane_criterion.md)（forced-plane 判据）
* [attempts/166](../../decision_algorithms/attempts/166_c2_general_algorithm.md)（$c=2$ 算法）
* [attempts/168](168_dimWL3_witness.md)（$\dim W_L=3$ 实例）
* [attempts/179](../../decision_algorithms/attempts/179_c2_scope.md)（适用范围）
* [tools/verification/stratum_solver.py](../../../../tools/verification/stratum_solver.py)

## 状态

* 工具与测试：**[精确验证 5/5 实例]**。
* 完备枚举/不可行证书：**[未做]**。
