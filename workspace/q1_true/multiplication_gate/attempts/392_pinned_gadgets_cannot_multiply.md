# 354 钉住不可能给乘法：可行集是线性空间的 Zariski 开集

> 承接 353（钉住引理与权衡）。本文件把"钉住救乘法"这条道**证死**，
> 并据此把 sound 乘法门的必要条件收窄成一句可检验的话。
> 这同时回答了 80 号 §5.2 建议（"force the intended rank stratum"）在乘法侧是否可行：**不可行**。

## 目标

证明：若实例是**钉住**的（$\dim(A K_0)=\operatorname{rank}H_0=\omega_0$），则它的可行集
**不能**表达任何非线性（例如乘法）关系——只能表达线性关系。

## 设想与理由

353 已经证明钉住后 $(5a)$ 退化为线性条件、可行集落在
$$\mathcal L:=\bigl(\mathcal T\cap(W_0\times W_0)\bigr)^{m},\qquad W_0=\operatorname{row}H_0$$
里。剩下的问题是 $(5b)$ 还能提供什么。$(5b)$ 是"铅笔处处秩 $\omega_0$"，它的**补**是闭集（坏集），
所以 $(5b)$ 本身是 **Zariski 开**条件。于是可行集 $=$ 线性空间 $\cap$ 开集。

## 做法与证明

> **定理（pinned-instance no-go；98 号审计后的定稿）.** 设
> 1. 实例钉住：$\dim(A K_0)=\omega_0=\operatorname{rank}H_0$；
> 2. **固定行协调**：$\operatorname{row}H_{A,0}\subseteq W_0$（$W_0=\operatorname{row}H_0$）；
> 3. 可行集非空；
> 4. 编码变量是自由行参数的**仿射线性**函数。
>
> 记
> $$\mathcal F=\{R:\ (5a)\wedge(5b)\ \text{成立}\}.$$
> 则 $\mathcal F=\mathcal L\cap\mathcal O$，其中 $\mathcal L$ 是线性子空间、$\mathcal O$ 是 Zariski 开集。
> 若 $\mathcal F\ne\varnothing$，则 $\mathcal F$ 在 $\mathcal L$ 中 Zariski 稠密；
> 于是**任何**在 $\mathcal F$ 上恒为零的多项式（例如 $z-xy$）都在整个 $\mathcal L$ 上恒为零。
>
> **域**（98 号 §1.4）：$\mathcal F$ 指**复**可行点时，稠密性直接成立；若取**实**点，
> 非空实可行集含 $\mathcal L(\mathbb R)$ 的非空欧氏开子集，结论相同；若取**有理**点，非空有理可行集足矣。
> 注意"非空复开集"并**不**蕴含含有理点——所以必须条件在 $\mathcal F\ne\varnothing$ 上。

*证明.*
1. 由 353 的引理，每个可行 $R$ 满足 $\operatorname{row}H=W_0$；反之若固定行协调（假设 2）且每个自由行的对
   都落在 $\mathcal T\cap(W_0\times W_0)$，则 $\operatorname{row}H\subseteq W_0$、从而 $(5a)$ 成立。
   所以 $(5a)$ 等价于 $R\in\mathcal L$，而 $\mathcal L$ 是线性子空间（$\mathcal T$、$W_0$ 都是线性空间）。
2. $(5b)$ 的失败集 $\{\exists\lambda:\operatorname{rank}(\lambda H-H_A)<\omega_0\}$ 在 $\mathcal L$ 上闭
   （射影入射簇的紧合投影，见 322），故 $(5b)$ 给出 Zariski 开集 $\mathcal O$。
3. $\mathcal L$ 是复线性空间，不可约；$\mathcal F=\mathcal L\cap\mathcal O$ 非空开 ⟹ Zariski 稠密。
   多项式在稠密开集上为零 ⟹ 在 $\mathcal L$ 上恒零。$\square$

**推论（钉住不能编乘法）.** 若某个非线性关系（例如 $z=xy$）在**所有**可行 $R$ 上成立，
而该关系作为多项式不在整个 $\mathcal L$ 上恒成立，则与定理矛盾。
所以钉住的实例只能表达"由 $\mathcal L$ 的线性条件推出"的关系。

**两个注**：
- 这条与 353 的权衡合起来是完整的：**钉住 ⟹ 线性表达力**（而且这个"线性"是精确的、不只是"看起来线性"）；
- 80 号 §5.2 的"force the intended rank stratum"在**线性限制**方向仍然有用，
  但**不能**用来给乘法门钉层。**（98 号 §6.2 更正）**：$\mathcal L$ 给的是**齐次线性**限制，
  不是任意仿射约束；要模拟 $x_1+x_2=1$ 这类非齐次条件需要**单独构造**，不能从本定理推出。

## 进展

1. 定理与证明已写出（Zariski 稠密 + 不可约，标准论证）。
2. 推论：钉住 ⟹ 无非线性表达力。
3. 于是 sound 乘法门的必要条件被收窄为：
   > **实例必须未钉住**（$\dim(A K_0)>\operatorname{rank}H_0$ 或 $\operatorname{rank}H_0<\omega$），
   > 且"加行逃逸"必须被 $(5b)$ 的坏集覆盖（307 的第六步）。
4. 而"未钉住"恰好是 307 说会逃逸的情形——所以乘法门的全部困难就在这个夹缝里，
   不是我们没试对参数，而是**钉住与非线性互相排斥**。

## 最终结论

1. **钉住救不了乘法**（本定理），这解释了 353 的权衡为什么是硬的。
2. 乘法门的唯一可能形态：**未钉住 + 用坏集惩罚加行**。惩罚机制尚未找到。
3. 对 ARM 翻译（352）是**正面**的：钉住块能精确提供线性（仿射）约束，而且现在有定理保证它不会
   意外引入别的关系——这比"求助于 $L_0$ 钉行"干净得多。

## 放弃原因

- 没有给出"未钉住 + 惩罚"的构造；只证明了"钉住不行"。
- 定理是条件性的（需要 $\mathcal F\ne\varnothing$；空集时平凡），未讨论空集情形下的编码（那时实例不可行，
   可以当"否定"用来编码，但不能当"乘法"用来编码）。
- 没有把"惩罚加行"写成可检验的判据。

## 残留价值

- 一条**排除性定理**：钉住实例的表达力恰好是线性的；
- 把乘法门的必要条件收窄到"未钉住 + 坏集惩罚"，并说明 307 的第六步就是全部困难；
- 对 ARM 翻译是正面结果（钉住块 = 干净的仿射约束机器）。

## 相关文件

- [353](391_multiplication_pinning.md)（钉住引理与权衡）
- [307](../../../q1_false/decision_algorithms/attempts/307_soundness_obligations.md)（三义务与 rank forcing 的失败）
- [303](../../../q1_false/decision_algorithms/attempts/303_79_verdict_lifts.md)、[306](306_80_soundness_correction.md)（乘法门实现与反例）
- [80 号答复](../../../for_expert/archive/80_wiring_copy_gadget-answer.md)（§5.2 / §5.4）
- [322](../../../q1_false/c_stratification/attempts/322_hyperplane_determinism_components.md)（坏集闭，本定理用到）
- [352](../../arm_reduction/attempts/390_arm_translation_analysis.md)（ARM 翻译缺仿射控制）

## 状态

- 定理：**[已证-纸面]**（Zariski 稠密论证）。
- 推论（钉住无乘法）：**[已证-纸面]**。
- 乘法门：**[未得到]**；必要形态已收窄为"未钉住 + 坏集惩罚"。
