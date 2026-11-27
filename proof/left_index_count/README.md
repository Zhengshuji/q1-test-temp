# left_index_count —— 零左最小指标计数 + $(5b)$ 的必要条件 $h<q+r_1$（B.9）

> **对应 docs 条目**：B.6（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

## 陈述

设 $\mathcal L$ 行满秩、含 $L_0\ne0$，$Q_{\mathcal L}(\lambda)=[\lambda\mathcal L-\mathcal LA;CA;C]$，
$h$ 为其正规秩、$r_1=\operatorname{rank}[C;CA]$、$s=\operatorname{rank}\mathcal L$。则

1. $Q_{\mathcal L}$ 有 **$2p-r_1$ 个零左最小指标**，非零左指标个数为 $q+r_1-h$；
2. 因此 $(5b)\ \Longrightarrow\ h<q+r_1$（等价：$h\ge q+r_1\Rightarrow(5b)$ 必失败）。

## 状态

**[已证-纸面]**（[theorem.md](theorem.md)，用 B.6+B.8）$+$ **[精确验证 698/698]**（[verify.py](verify.py)：56 个闭包 + 各阶链式抽样）。

在 56 个功能可观测实例上，闭包处 $(5b)$ 失败的 **16 个全部**满足 $h\ge q+r_1$——
B.9 解释了样本里**所有**失败。

## 文件

| 文件 | 内容 |
|---|---|
| [theorem.md](theorem.md) | 引理 1（常值左零向量维数 $2p-r_1$）、引理 2（零指标计数）、推论 B.9 及证明 |
| [verify.py](verify.py) | 56 个铅笔上核验三条计数等式 + B.9（**验证不是证明**）|

## 复现

```bash
python proof/left_index_count/verify.py
```

## 加强：$q+r_1-s\le h<q+r_1$，且 $d_{\rm fin}\le s-(q+r_1-h)$

非零左指标每个 $\ge1$，故 $\sum\varepsilon\ge q+r_1-h$；而 $(5b)$ 要求 $\sum\varepsilon=s$，于是
$$q+r_1-s\ \le\ h\ <\ q+r_1\qquad(\text{左边是新的，右边是 B.9}),$$
并由此得**有限初等因子总次数的上界**
$$d_{\rm fin}=s-\sum\varepsilon\ \le\ s-(q+r_1-h).$$
（本轮复现的公开例子 $\mathcal L_5$：$q=5,h=8,s=5,r_1=4$ ⟹ 区间 $4\le8<9$ ✓，$d_{\rm fin}=0\le4$ ✓。
本文件的 [verify.py](verify.py) 在 **698 个** $(5a)$-可行铅笔上断言这两条（0 反例），
[proof/fernando_2gap](../fernando_2gap/verify.py) 在公开例子上也断言。）

## 注：逆命题不成立

"$h<q+r_1$ 充分"是**错的**：912 个 $(5a)$-可行铅笔中 415 个满足 $h<q+r_1$ 但 $(5b)$ 失败
（非零左指标存在但 $\sum\varepsilon<s$）。见 [C2](../refuted/C2_h_lt_q_r1_not_sufficient.md)。
B.9 只是**必要**条件。

## 意义

* **一个廉价的必要条件**：只算 $q,r_1,h$ 三个整数即可排除一大类；
* 它把"闭包处 $(5b)$ 何时成立"这个问题缩到 $h<q+r_1$ 的情形；
* 与 `h_bound` 的互补障碍（充分失败、只在 $q=n-r_1$）互补：B.9 在**所有阶**上给出下界。

## 相关

- [proof/kron_null_module](../kron_null_module/README.md)（B.6）
- [proof/t4b_infinite_divisors](../t4b_infinite_divisors/README.md)（B.7）
- [proof/toeplitz_criterion](../toeplitz_criterion/README.md)（判 $(5b)$ 的 Toeplitz 判据）
- [proof/h_bound](../h_bound/README.md)（互补障碍）
