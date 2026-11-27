# 574 冗余行定理：非退化情形下的完整证明与退化情形说明

> 2026-11-27。按 ChatGPT 的 (a)，把 572 的草稿推广，并明确假设。
> 状态：**[已证-纸面]**（非退化情形）+ **[精确点]**（退化情形由 573 支持）。

## 定理（非退化情形）

设 $H_0$ 行满秩（$h_1,\dots,h_{r_0}$ 线性无关）、$H_{A,0}$ 行满秩（$a_1,\dots,a_{r_0}$ 线性无关）。
若存在 $r$ 使
$$\lambda\,rN-rAN\in\operatorname{row}P_0(\lambda)\qquad\forall\lambda,$$
则 $rN\in\operatorname{row}H_0$ 且 $rAN\in\operatorname{row}H_{A,0}$。

**证明.** 设 $\lambda rN-rAN=\sum_i c_i(\lambda)(\lambda h_i-a_i)$，$c_i\in\mathbb C(\lambda)$。

1. **$\lambda\to\infty$**：两边除以 $\lambda$，得 $rN=\sum_i c_i(\lambda)h_i+O(1/\lambda)$。
   若某个 $c_i$ 在 $\infty$ 有极点，右边次数 $>0$ 或与 $h_i$ 的线性相关性冲突；由 $h_i$ 线性无关，
   $c_i$ 在 $\infty$ 正则，取极限得 $rN=\sum_i c_i(\infty)h_i\in\operatorname{row}H_0$。
2. **$\lambda=0$**：同理，$-rAN=\sum_i c_i(0)(-a_i)$；由 $a_i$ 线性无关，$c_i$ 在 $0$ 正则，
   得 $rAN=\sum_i c_i(0)a_i\in\operatorname{row}H_{A,0}$。$\square$

## 退化情形（$H_0$ 或 $H_{A,0}$ 行相关）

- 530 的门上 $H_0$ 秩 2（$h_1=xh_2$）、$H_{A,0}$ 秩 2（$a_3=0$），正是退化情形；
- 此时首项比较可能出现 $h_i$ 的线性相关抵消，结论需要更细的分析；
- 573 的 243 组枚举显示可行行全部冗余（$rN=(0,0,\pm1)$、$rAN\in\operatorname{span}\{a_1,a_2\}$），
  与“退化情形也冗余”一致，但**尚未证明**。

## 对 530 的意义

- 非退化假设不成立，所以不能直接把定理套到 530；
- 但 573 的精确点支持退化情形同样冗余；下一步是对 530 的 $h_1=xh_2$、$a_3=0$ 做局部展开证明。

## 状态

- 非退化定理：**[已证-纸面]**；
- 530 的退化情形：**[精确点]**（27/243 全冗余），未证。
