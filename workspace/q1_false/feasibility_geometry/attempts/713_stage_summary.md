# 713 阶段总结：$T$-纤维、$\rho_d$ 障碍与预筛选链
> **更正（729）**：661 因 $T=0$ 对 $d>0$ 不可行，~~$\omega>s$ 重新开放~~；**733 已给出新的 $\omega>s$ 可行例**，631 需 $T=S$（727）。


> 2026-11-27。把 677–712 的 proved 结果与开放问题整理成一页，供后续（含 ChatGPT）对齐。
> 状态：**[整理]**。

## 已证（纸面）

| 条目 | 内容 |
|---|---|
| 677 | 引理 S：$\operatorname{rank}\Phi=2d-\deg\gcd$；故 $\operatorname{rank}H=d$ 时 $(5b)\iff\operatorname{rank}M=2d$ |
| 674 | $d=2$ 定理：$(5b)\iff\operatorname{rank}M=4$（674；或由 677） |
| 679 | $q=r_0$：可行 $\iff$ 固定铅笔 $\gcd=1$（多项式时间） |
| 687 | $Z$ 的自由部分（$\Delta H=0$）不改变铅笔 |
| 692/697 | $G=LW$ 的行空间是 $T=\{lW:lN=0\}\subseteq S$；相容性 $H_iZ'\in U+T$ |
| 690/695 | 可行 ⇒ $d'\le\dim(\operatorname{row}(H(\mu I-Z'))+T)$ |
| 704 | 可行 ⇒ $\operatorname{rank}H_A=d'$（$\lambda=0$） |
| 705 | 若全部 $d'$-子式成比例（$\rho_{d'}=1$），则 $\operatorname{rank}M\le d'<2d'$ ⇒ 不可行 |
| 707/708/709 | 638：$e_1\notin U$、$H_A=\Pi_U(HZ')$ 唯一、$P$ 的行在 $U$ 内 ⇒ $\rho_2=1$ ⇒ $d'=2$ 不可行 |
| 710 | 638：$d'=1$ 不可行（$v\in T$ 不相容；$v\notin T$ ⇒ $Zu=\mu u$ 掉秩） |
| 661 | 撤回：$T=0$（$N=I_2$）⇒ $G=0$、$P=H(\lambda I-Z')$ 在 $\sigma(Z')$ 处降秩 ⇒ $d>0$ 不可行 |
| 733 | **$\omega>s$ 恢复**：$d'=2>s=t=1$ 可行（显式 $L$、$\gcd=1$，子 agent 独立复算） |
| 734 | 定理 B：可行 ⇒ $d'\le\operatorname{rank}(H(\mu I-Z'))+\dim E_H$（$E_H=\operatorname{span}\bigcup_i(T\cap(U-H_iZ'))$）；标量 $Z'$ ⇒ $d'\le\dim(U\cap T)$；733 取等 |
| 732 | 猜想 $d'\le t$ 被 733 推翻 |
| 693/712 | $t<s$ 实例；$LW$ 变化空间恰为 $T$（实验 A） |

## 预筛选链（只依赖数据）

1. $\lambda=0$：$\operatorname{rank}H_A=d'$（704）；
2. 651：$H_0|_{T_\infty}=0$、$d'\le k-\dim T_\infty$；
3. 690/695：$\dim(\operatorname{row}(H(\mu I-Z'))+T)\ge d'$；
4. $m=1$（$q=k=d'$）⇒ 不可行；
5. $S=0$、$d'\ge1$ ⇒ 不可行（629）；
6. 通过后对具体 $H$ 算 $\gcd$（或 $\operatorname{rank}M=2d'$）。

## 开放问题

1. **$T$-纤维的一般理论**：$T\cap U$、$T/(T\cap U)$ 与特征空间的关系（ChatGPT 的最高优先级）；
2. **$\rho_d$ 退化分类**：$\rho_d=r$ 时 $\operatorname{rank}M\le r\cdot d$；$r=1$ 已用于 638，$r\ge2$ 的结构未明；
3. **多 $\mu$ 同时补偿**（696）：逐 $\mu$ 可达 ≠ 联合可行；
4. **$\exists H$ 的复杂度**：P vs NP-hard 仍开放；
5. **665/689 的 $T$-版本**：需要重新线性消元。

## 当前对 q1 的判断

- 结构理论（引理 S、$T$、$\rho_d$、预筛选）已相当完整；
- 但“$\exists H$ + 多项式时间判定”仍无实质突破；
- q1 ∈ P 与 NP-hard 都未被排除。

## 状态

- 整理：**[已完成]**；
- 下一步：实验 B（$T\cap U$ 的方向交互）与 C（$\rho_d$ vs Bézout）。
