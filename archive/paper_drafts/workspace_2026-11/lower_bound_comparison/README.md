# 两条阶下界的对照（新框架 vs 旧框架）

> 目的：把论文新增的谱条件下界与 `proof/lower_bound/` 里旧框架的下界对齐，判断谁强、能否合并。

## 1. 两条界

**旧框架**（[`proof/lower_bound/theorem.md`](../../proof/lower_bound/theorem.md)，A.1–A.3）：

$$q_{\min}\ \ge\ \max\bigl(r+\varepsilon,\ \rho_{ci}+\max(c_0,1)\bigr),$$

其中 $\mathcal J=\operatorname{row}[C;CA]$、$j=\dim\mathcal J$、$\mathcal V=\operatorname{row}\mathcal L$、
$\rho=\dim\pi(\mathcal V)$、$c=\dim(\mathcal V\cap\mathcal J)$、$c_0=\dim(\operatorname{row}L_0\cap\mathcal J)$、
$\varepsilon=1-[\text{$L_0$ 本身是解}]$。

**新框架**（论文 `prop:lowerbound`）：

$$q_{\min}\ \ge\ r_0+\max\bigl(0,\ \operatorname{rank}[U_0;V_0]-s_0+1\bigr),
\qquad U_0=L_0N,\ V_0=L_0AN,\ s_0=\dim W_0 .$$

## 2. 找到的桥：$\rho=\omega$

商空间 $\mathbb R^n/\mathcal J$ 与 $K_0=\ker[C;CA]$ 同构，同构由 $u\mapsto uN$ 给出。于是

$$\rho=\dim\{uN:\ u\in\operatorname{row}\mathcal L\}=\dim\pi_1(W)=\omega .$$

**即旧框架的 $\rho$ 恰好是本文的 $\omega$。** 两个框架不是各说各话：$\rho$ 与 $\omega$ 是同一个量。

据此旧的下界可重写为 $q\ge\omega+\max(c_0,1)$，其中
$c_0=r_0-\operatorname{rank}U_0$（因为 $c_0=\dim\{u\in\operatorname{row}L_0:uN=0\}$）。

而新的下界来自 $\omega+1\le\dim W=s_0+t$，即 $q\ge r_0+\omega-s_0+1$；再用
$\omega\ge\operatorname{rank}[U_0;V_0]$ 换成可计算的形式。

## 3. 谁更强

在**同一 $\omega$** 下比较：

- 旧：$q\ge\omega+\max(c_0,1)$，$c_0=r_0-\operatorname{rank}U_0$；
- 新：$q\ge r_0+\omega-s_0+1$。

因 $s_0\le r_0$（$\operatorname{rank}(L_0M)\le\operatorname{rank}L_0$），新界比"$\omega+1$"多出
$r_0-s_0\ge0$，即**固定行 $L_0$ 在压缩意义下的冗余行数**。两者一般**互不包含**
（旧界用 $c_0$，新界用 $\operatorname{rank}[U_0;V_0]-s_0$），实践中取大者。

## 4. 在附录 B 的实例上

| 量 | 值 |
|---|---|
| $j=\dim\mathcal J$ | $4$ |
| $c_0=\dim(\operatorname{row}L_0\cap\mathcal J)$ | $0$ |
| 对已知解 $L$：$c=\dim(\operatorname{row}L\cap\mathcal J)$ | $1$ |
| $\rho=q-c$ | $3$ |
| 旧界（该解处）$\rho+\max(c_0,1)$ | $\mathbf 4$ |
| $\operatorname{rank}[U_0;V_0]$，$s_0$ | $3$，$2$ |
| 新界 $r_0+\max(0,3-2+1)$ | $\mathbf 4$ |
| 实际 $q_{\min}$ | $\mathbf 4$ |

**两条界在该实例上给出同一个值 4，且都取到等号。** 由于两条界是在不同框架下独立导出的，
这构成一次**互相验证**：新命题没有把旧结论改坏，旧结论也没有排除新命题。

## 5. 结论

1. **紧性**：新界在附录 B 的实例上取等号（$4=4$），可以如实写"attained on this instance"；
   但不声称一般紧（论文已按此措辞，见 `rem:lbtight`）。
2. **合并**：两条界互不包含，正确用法是取大者；论文只陈述本框架内的那条（旧的那条记号不同、
   且未在论文中出现），**不做合并公式**——合并会引入两套记号，收益仅是常数项。
3. **可做但未做**：若能证明 $c_0$ 与 $\operatorname{rank}[U_0;V_0]-s_0$ 的某种次序关系，
   可得到一条统一界；目前没有证据支持这种次序，故不做。

## 6. 脚本

[`tools/verification/c329_bounds_comparison.py`](../../tools/verification/c329_bounds_comparison.py)
—— 上表的全部数值，精确有理算术。
