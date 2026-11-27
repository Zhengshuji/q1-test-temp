# 357 候选线性原理（CLP）：$m=1$ 时成立（定理），$m\ge2$ 待测

> 承接 356（98 号审计）与 355（极大性引理）。98 号把"下一步"定为
> **候选线性原理**（CLP），要求先在小维用精确算术验证。本文件给出 CLP 的精确定义，
> 证明它在**单自由行**（$m=1$）时成立，并给出 $m\ge2$ 的检验计划。
> 证书：[c357](../../../../tools/verification/c357_single_row_clp.py)（精确算术，含"公共根恰为 $\lambda=\alpha$"的断言）。

## 目标

1. 精确定义 CLP（98 号的表述需要把"线性子空间"落在哪个空间说清）。
2. 证明 $m=1$ 时 CLP 成立。
3. 给出 $m\ge2$ 的可执行检验方案。

## 设想与理由

98 号的原话：**在每个秩 $\omega$ 的可行轨迹的不可约分量上，可行集要么空、要么在某个线性子空间中 Zariski 稠密。**

要检验它，需要把"可行集"的闭包算清。关键观察：可行集
$$\mathcal F_\omega=\{R:\operatorname{rank}H=\omega,\ (5a),\ (5b)\}=P_\omega\setminus \mathrm{Bad},$$
其中 $P_\omega=\{R:\operatorname{rank}H=\omega,\ (5a)\}$ 是**行列式簇**（闭），$\mathrm{Bad}$ 是 $(5b)$ 的失败集（闭）。于是

- 若 $P_\omega\subseteq\mathrm{Bad}$，则 $\mathcal F_\omega=\varnothing$（CLP 平凡成立）；
- 否则 $\mathcal F_\omega$ 在 $P_\omega$ 中稠密，**闭包 $=P_\omega$**，于是 **CLP $\iff$ $P_\omega$ 的相应分量是线性的**。

这就把 CLP 化成一个纯代数问题：**$P_\omega$ 的不可约分量是不是线性子空间？**

## 做法：$m=1$ 的定理

设实例恰有一个自由行 $(h,g)\in\mathcal T$，固定行满足协调条件 $\operatorname{row}H_{A,0}\subseteq\operatorname{row}H_0$，
$r=\operatorname{rank}H_0$。记
$$H=\begin{bmatrix}H_0\\h\end{bmatrix},\qquad H_A=\begin{bmatrix}H_{A,0}\\g\end{bmatrix}.$$
因 $m=1$，$\operatorname{rank}H\in\{r,r+1\}$。

> **定理 A（$m=1$ 的 CLP）.** 在上述假设下，对每个 $\omega$：
> - $\omega=r$：$\mathcal F_r=\{(h,g)\in\operatorname{row}H_0\times\operatorname{row}H_0:(5b)\}$，
>   是**线性空间 $(\operatorname{row}H_0)^2$ 中的 Zariski 开集**；
> - $\omega>r$：$\mathcal F_\omega=\varnothing$。

*证明.*
**情形 $\omega=r$**：$\operatorname{rank}H=r$ ⟺ $h\in\operatorname{row}H_0$；
$(5a)$ ⟺ $\operatorname{row}H_A\subseteq\operatorname{row}H=\operatorname{row}H_0$，由协调条件即 $g\in\operatorname{row}H_0$。
故 $(5a)$ 与秩条件合起来恰是线性条件 $(h,g)\in(\operatorname{row}H_0)^2$；
$(5b)$ 在其补上闭（322），故给出 Zariski 开集。$\square$

**情形 $\omega=r+1$**：此时 $h\notin\operatorname{row}H_0$。若 $(5a)$ 成立，则
$$g\in\operatorname{row}H_A\subseteq\operatorname{row}H=\operatorname{row}H_0+\langle h\rangle,$$
故存在 $\alpha\in\mathbb C$、$w\in\operatorname{row}H_0$ 使 $g=\alpha h+w$。在 $\lambda=\alpha$ 处
$$\alpha h-g=-w\in\operatorname{row}H_0,$$
而固定部分的铅笔行也在 $\operatorname{row}H_0$ 里（协调条件），故
$$\operatorname{rank}(\alpha H-H_A)\le r<r+1=\operatorname{rank}H,$$
$(5b)$ 失败。所以 $\mathcal F_{r+1}=\varnothing$。$\square$

**这说明**：$m=1$ 时 CLP 成立，而且证明就是**极大性引理**（355）的直接应用——
"加一行"在 $m=1$ 恰好就是"加唯一那一行"，于是引理的惩罚机制正好覆盖整个更高层。

### 精确验证

[c357](../../../../tools/verification/c357_single_row_clp.py) 用 79 号的 $3k$ 通用提升（$k=3,n=9,p=3$）造显式实例，
固定部分取**位移脚手架** $H_0=[v_1;v_2;0]$、$H_{A,0}=[0;v_1;v_2]$（秩 2、处处好）：

| 检验 | 结果 |
|---|---|
| $\omega=2$：$h,g\in\operatorname{row}H_0$ 的两组取样 | 都 $\gcd=1$（可行）✓ |
| $\omega=3$：$h\notin\operatorname{row}H_0$、$g=\alpha h+w$，$\alpha=-2,1,3$，$w=0,v_1$ | 六组全部**不可行**，且 $\gcd$ **恰为 $\lambda-\alpha$** ✓ |
| $\alpha=0,w=0$（退化） | 在 $\lambda=0$ 处平凡失败（$\operatorname{rank}H_A=2<3$）✓ |

**公共根恰为 $\lambda=\alpha$** 这一点把机制钉死了：不是"恰好坏了"，而是坏在由 $g=\alpha h+w$ 决定的那个参数上。

## 进展

1. CLP 被化归为"$P_\omega$ 的分量是否线性"（纯代数问题）；
2. **定理 A 已证**：$m=1$ 时 CLP 成立，两层都验证（含 $\gcd=\lambda-\alpha$ 的精确断言）；
3. 定理 A 是**极大性引理的直接推论**——这解释了 98 号为什么说引理 3 是"最强的一条"。

## 最终结论

1. **$m=1$ 的 CLP 成立**（定理 A）。
2. $m\ge2$ 是真正的问题：那时"加一行"不等于"加全部剩余行"，极大性引理不管用。
3. 检验口径已定：$P_\omega$ 的分量是否线性。

## 放弃原因

- 没有处理 $m\ge2$；也没有给出 $P_\omega$ 非线性的判据；
- 定理 A 依赖固定行协调条件（协调不成立时 $m=1$ 也可行集为空，CLP 仍平凡成立）。

## 残留价值

- 一条**带证书的定理**（$m=1$ 的 CLP），把 98 号的候选原理在一个完整情形上落地；
- 把 CLP 化归成"行列式簇的分量是否线性"——这给了 $m\ge2$ 一个可计算的入口；
- 顺带把"公共根 $=\lambda=\alpha$"这个机制量化了。

## 下一步（$m\ge2$ 的检验计划）

1. 取小实例（$k=3$，$r_0$ 使固定部分好，$m=2$）；
2. 对每个 $\omega$，符号计算 $P_\omega$ 的定义理想（由 $\operatorname{rank}H=\omega$ 与 $(5a)$ 的子式生成），
   判定其分量是否线性（例如找一个二次生成元不是线性形式的组合）；
3. 若有非线性的 $P_\omega$，再验证 $\mathcal F_\omega\ne\varnothing$（找一个精确可行点）——
   那就**否证 CLP**，并指出乘法的可能藏身处；
4. 若小实例全部线性，扩大范围并记录"未找到反例"。

## 相关文件

- [356](394_expert98_audit.md)（98 号裁决与四阶段路线）
- [355](../../../q1_false/c_stratification/attempts/393_maximality_lemma.md)（极大性引理，本定理的工具）
- [354](392_pinned_gadgets_cannot_multiply.md)（pinned no-go）
- [322](../../../q1_false/c_stratification/attempts/322_hyperplane_determinism_components.md)（坏集闭）
- [c357](../../../../tools/verification/c357_single_row_clp.py)

## 状态

- CLP 化归：**[已证-纸面]**（$\mathcal F=P\setminus\mathrm{Bad}$，闭包 $=P$ 或空）。
- 定理 A（$m=1$）：**[已证-纸面]** + **[精确验证]**（c357）。
- $m\ge2$：**[未做]**。
