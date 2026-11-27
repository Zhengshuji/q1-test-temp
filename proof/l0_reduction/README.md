# 归约：$L_0$ 中落在 $\operatorname{row}C$ 的行可以去掉（每去一行，$q_{\min}$ 减 1）

> **对应 docs 条目**：B.9（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

> 2026-10-30。目的：对接 P2（arXiv:2609.37992）的假设 $\operatorname{rank}[C;L]=p+r$
> （即"$L$ 独立于 $C$"）。本项目的 $L_0$ 可能含 $\operatorname{row}C$ 的分量。

## 命题

设 $L_0=\binom{c}{L_1}$（$c$ 是一行）且 $c\in\operatorname{row}C$。则
$$q_{\min}(A,C,L_0)\;=\;q_{\min}(A,C,L_1)+1 .$$

*证明*：记 $\mathcal L=[L_0;R]$、$\mathcal L'=[L_1;R]$。两件事：
1. **$c$ 不改变两个秩**：$c\in\operatorname{row}C\subseteq\operatorname{row}[\mathcal L';CA;C]$，且 $cA\in\operatorname{row}(CA)\subseteq\operatorname{row}[\mathcal L';CA;C]$。
   因此
   $$\operatorname{rank}[\mathcal L A;\mathcal L;CA;C]=\operatorname{rank}[\mathcal L'A;\mathcal L';CA;C],\qquad
   \operatorname{rank}[\mathcal L;CA;C]=\operatorname{rank}[\mathcal L';CA;C],$$
   对 $\lambda\mathcal L-\mathcal LA$ 同理（$c$ 那一行是 $(\lambda c-cA)$，而 $c,cA$ 都在 $\operatorname{row}[CA;C]$ 里，$\lambda c$ 是 $c$ 的倍数、仍在同一行空间 ✓）。
2. 于是：$\mathcal L$ 满足 $(5a)(5b)\iff\mathcal L'$ 满足 $(5a)(5b)$。
   故可行解一一对应（行数差 1）⟹ $q_{\min}(L_0)=q_{\min}(L_1)+1$。$\square$

**推论**：把 $L_0$ 中所有落在 $\operatorname{row}C$ 的行去掉，得 $L_0^{\mathrm{mod}C}$，则
$$q_{\min}(A,C,L_0)=q_{\min}(A,C,L_0^{\mathrm{mod}C})+\#\{\text{去掉的行}\},$$
且 $\operatorname{rank}[C;L_0^{\mathrm{mod}C}]=p+\operatorname{rank}L_0^{\mathrm{mod}C}$ —— **P2 的假设成立** ✓。

**注意**：落在 $\operatorname{row}[C;CA]\setminus\operatorname{row}C$ 的行**不能**这样去掉（$cA\notin\operatorname{row}[CA;C]$ 的一般情形），
它们正是项目里 $c_0>0$ 的那部分；P2 的假设只要求"独立于 $C$"，所以它们被保留、由定理正常处理 ✓。

## 对假设核对表的更新

[../../literature/notes/P1P2_ASSUMPTIONS_CHECK.md](../../literature/notes/P1P2_ASSUMPTIONS_CHECK.md) 第 2 条由 ⚠️ 改为 ✓：
引用 P1/P2 时先做本归约（去掉 $\operatorname{row}C$ 的行、记下被去掉的行数），即可在"$L$ 独立于 $C$"的假设下使用其定理。

## 验证

- 本命题是纸面三行（上面的等式 1）。
- 机器复核 [verify.py](verify.py)：在 **100 个随机实例**上，把 $\operatorname{row}C$ 的一行加进 $\mathcal L$ 前后，
  `cond_5a_orig` 与 `cond_5b_orig` 完全一致 —— **100/100** ✓（验证的是秩等式，不是 $q_{\min}$ 本身）。

