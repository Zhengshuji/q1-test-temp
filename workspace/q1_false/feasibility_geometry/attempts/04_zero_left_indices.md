# 闭包处 $(5b)$ 何时成立：零左指标计数给出必要条件 $h<q+r_1$

## 目标

$q=\mathrm{cl}$ 时 $(5a)$ 解**唯一**（闭包 $V_{\min}$），所以"闭包处 $(5b)$ 是否成立"是**结构问题**。
实测 56 个可观测实例：40 成立、16 失败。本轮要找出**能解释这 16 个失败**的可计算条件。

## 设想与理由

把每个实例闭包的全部不变量与 $(5b)$ 判定做交叉表（[closure_feasibility.py](../../../../tools/verification/closure_feasibility.py)）：

| 不变量 | 成立/不成立 |
|---|---|
| $\mathrm{cl}=s$ | $1{:}7/8$, $2{:}17/4$, $3{:}8/4$, $4{:}8/0$ |
| $h$ | $2{:}3/0$, $3{:}7/4$, $4{:}15/5$, $5{:}13/5$, $6{:}2/2$ |
| $m=q+2p-h$ | $0{:}0/13$, $1{:}23/3$, $2{:}17/0$ |
| $d_{\rm fin}$ | $0{:}40/0$, $1{:}0/8$, $2{:}0/4$, $3{:}0/4$ |
| 互补障碍 | False $40/12$, True $0/4$ |

$d_{\rm fin}$ 的分界是同义反复（$(5b)\iff d_{\rm fin}=0$）。真正有信息的是 $m$：**$m=0$ 的 13 个全部失败**。
往这个方向追，得到下面的引理。

## 做法

1. 证明：铅笔 $Q_{\mathcal L}$ 的**常值**左零向量恰是 $(C,CA)$ 行相关的那些——由 $\varphi_1\mathcal L=0$ 与
   $\mathcal L$ 行满秩得 $\varphi_1=0$，故常值左零向量空间维数 $=2p-r_1$（$r_1=\operatorname{rank}[C;CA]$）；
2. 这些恰是**零左指标**，故非零左指标个数 $=m-(2p-r_1)=q+r_1-h$；
3. 若 $h\ge q+r_1$，则无非零左指标 ⟹ $\sum\varepsilon=0$ ⟹ 由 B.8 得 $d_{\rm fin}=s>0$ ⟹ $(5b)$ 失败。

纸面证明：[proof/left_index_count/theorem.md](../../../../proof/left_index_count/theorem.md)；机器核验：
[verify.py](../../../../proof/left_index_count/verify.py)。

## 进展

* 56 个铅笔上三条计数等式（左指标个数 $=q+2p-h$、零指标 $=2p-r_1$、非零 $=q+r_1-h$）**全部通过**；
* B.9 触发 16 次，**全部** $d_{\rm fin}>0$（无反例）；
* 也就是说：**样本里 16 个失败全部由 B.9 解释**。

## 最终结论

$$\boxed{(5b)\ \Longrightarrow\ h<q+r_1}$$

这是一个**廉价**的必要条件（只算 $q,r_1,h$ 三个整数），且与 `h_bound` 的互补障碍互补：
后者是充分失败条件、只在 $q=n-r_1$ 触发；B.9 在**所有阶**上给必要条件。

**残余（已解决）：逆命题不成立**。在 912 个 $(5a)$-可行铅笔（不限于闭包）中，
满足 $h<q+r_1$ 但 $(5b)$ 失败的**有 415 个**——非零左指标存在，但 $\sum\varepsilon<s$。
例（$n=5,p=1,r=1$、$q=4$）：$h=5$、$r_1=2$、$\varepsilon=[3]$、$s=4$、$d_{\rm fin}=1$。
故 $h<q+r_1$ **只是必要条件**，见 [C2](../../../../proof/refuted/C2_h_lt_q_r1_not_sufficient.md)。

## 放弃原因

不适用。

## 残留价值

* **B.9**：$(5b)$ 的必要条件，已证 + 已验证；
* 交叉表方法（把闭包的不变量与判定做表）可复用到任何"单点判定"的问题；
* 一个明确的下一步问题：$h<q+r_1$ 是否充分？

## 相关文件

- [proof/left_index_count/](../../../../proof/left_index_count/README.md)（B.9 的证明与验证）
- [tools/verification/closure_feasibility.py](../../../../tools/verification/closure_feasibility.py)（交叉表）
- [tools/verification/omega_construct.py](../../../../tools/verification/omega_construct.py)（闭包）
- [proof/refuted/C1_closure_plus_one.md](../../../../proof/refuted/C1_closure_plus_one.md)（C1 推翻）

## 后续更正（专家答复后）

1. 本 attempt 用的"闭包"**不是精确最小维数**：公开例子 $q_0=3$ 而闭包 $=4$（[复现](../../../../proof/fernando_2gap/README.md)）。
   贪心加入 $xA$ 可能加多行（专家 §8.1）。权威量是 $q_0=\sum_j\eta_j$。
2. B.9 可加强为 $q+r_1-s\le h<q+r_1$，并给出 $d_{\rm fin}\le s-(q+r_1-h)$；
   这两条在公开例子上都验证通过。
3. B.9 本身不受影响（它对任意 $(5a)$ 增广成立，不依赖闭包）。
