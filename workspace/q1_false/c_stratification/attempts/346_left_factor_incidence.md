# 346 左因子形式：坏 ⟺ $\operatorname{im}H$ 撞上 $S$ 的特征线（Claim 11 的几何形状）

> 承接 341（富余档可以好）与 97 号 §11（"结构族是否落在坏铅笔簇内"）。本文件把 Claim 11
> 化成一条**入射条件**：铅笔 = $(\lambda I-S)H$，坏 ⟺ $\operatorname{im}H$ 与 $S$ 的某条特征线相交。

## 目标

把"铅笔坏"改写成可几何化的形式，为 Claim 11（富余档"生成好"）找一条可证的路线。

## 设想与理由

$(5a)$ 是"$\operatorname{row}H_A\subseteq\operatorname{row}H$"，即 $H_A$ 的每行是 $H$ 的行的组合：
$$H_A=S\,H\quad\text{对某个 }S\in\mathbb C^{q\times q}.$$
（这正是 322 闭性证明里用过的"行包含"结构，只是这里显式写出 $S$。）于是铅笔变成
$$P(\lambda)=\lambda H-H_A=(\lambda I-S)H .$$

## 做法

**引理（左因子）.** 设 $(5a)$ 成立，则存在 $S$ 使 $H_A=SH$，且
$$P(\lambda)=(\lambda I-S)H\qquad\forall\lambda .$$

*证明.* 行包含 $\iff H_A=SH$（$S$ 的行是组合系数）；代入即得。$\square$

**推论（坏 = 入射）.** 记 $\operatorname{im}H=H(\mathbb C^k)$（$\dim=\omega$）、$E_\lambda(S)=\ker(\lambda I-S)$。则
$$\operatorname{rank}P(\lambda)=\omega-\dim\bigl(\operatorname{im}H\cap E_\lambda(S)\bigr),$$
故
$$\boxed{\text{坏}\iff\exists\lambda:\ \operatorname{im}H\ \text{与}\ S\ \text{的某条特征线相交}\neq0 .}$$

*证明.* $(\lambda I-S)$ 限制在 $\operatorname{im}H$ 上的核恰是 $\operatorname{im}H\cap E_\lambda(S)$；用秩-零化度。$\square$

**机器核对**（[c346](../../../../tools/verification/c346_left_factor_check.py)）：在 336 与 333 两个实例的可容许点上，
解出 $S$、验证 $SH=H_A$、$(\lambda I-S)H=\lambda H-H_A$、以及秩公式——各 12 个核对点全部通过。

## 进展

1. **坏性的形状变了**：从"某 $\omega$-子式有公共根"变成"一个 $\omega$ 维子空间 $\operatorname{im}H$ 撞上
   $S$ 的有限条特征线"——**入射问题**，与 322 的射影入射闭性证明同一类型。
2. **Claim 11 归结为**：可容许族里是否存在一个 $V$，使 $\operatorname{im}H$ 避开 $S=S(V)$ 的全部特征线。
   注意 $S$ 也随 $V$ 变，所以不是"避开一个固定有限集"。
3. **为什么它可能成立**：$\operatorname{im}H$ 是 $\omega=k-1$ 维，$S$ 的特征线至多 $q$ 条各 1 维；
   "撞上"是**正余维**的条件（$\omega\ge1$ 时每条特征线给一个真闭子集），而 $V$ 的自由度
   （$\operatorname{Gr}(q,U^\perp)$ 的维数）在富余档里更大。经验：341 的 18/27。

## 最终结论

1. 左因子形式是**已证**的（含秩公式与机器核对）。
2. Claim 11 现在有明确的几何形状：**族里能否实现"$\operatorname{im}H$ 避开特征线"**。
3. 尚未证明。真正的难点是 $S$ 与 $V$ 的**耦合**——避开了自己的特征线要靠构造，不能靠维度计数。

## 放弃原因

- 没有证明"存在 $V$ 使 $\operatorname{im}H\cap\bigcup_\lambda E_\lambda(S(V))=0$"；
- 维度计数只给"坏集是真闭子集"的**直觉**，不能替代非包含证明（97 号明确指出这一点）；
- 只做了两个实例的核对，没有一般构造。

## 残留价值

- 一条已证的**左因子引理 + 入射判据**，把坏性变成几何对象；
- 给 Claim 11 一个具体可攻的表述（避开特征线）；
- 与 322 的射影入射闭性、325 的"可观测性"框架接上：$S$ 就是"压缩后的动力学矩阵"。

## 相关文件

- [attempts/341](../../decision_algorithms/attempts/341_excess_regime_correction.md)（富余档可以好：18/27）
- [attempts/342](../../decision_algorithms/attempts/342_expert97_audit.md)（97 号：缺非包含论证）
- [attempts/322](322_hyperplane_determinism_components.md)（闭性：射影入射）
- [attempts/325](325_theorem_c_cost_model.md)（可观测性框架）
- [c346](../../../../tools/verification/c346_left_factor_check.py)

## 状态

- 左因子引理与秩公式：**[已证-纸面]** + **[精确验证]**（c346：两实例各 12 点）。
- Claim 11（富余档生成好）：**[未证]**；现在归结为"避开特征线"的构造问题。
