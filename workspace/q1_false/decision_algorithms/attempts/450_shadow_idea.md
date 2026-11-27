# 450 从算法线借来的关键启发：**W-消去定理**（$\exists W$ 可以塌缩成低维搜索）

> 用户要求"看算法侧成果找启发"。本轮读了算法线的核心定理
> [406_eliminate_W](../../c_stratification/attempts/406_eliminate_W.md)，它对**我这边唯一剩下的障碍（$\exists W$ 的搜索）**
> 给出了一条可迁移的结构性办法。

## 目标

把我的"$\exists W$ 使 (R) ∧ (E)"与算法线已有的"消去 $W$"对接，判断能否把搜索降成低维。

## 设想与理由（算法线的定理）

在 **$K_0$-split 设计** $V=D^{\perp_{K_0}}\oplus W$（$D\le K_0$、$W\subseteq K_0^\perp$）下：

- $H=V^{\mathsf T}N$ 里 **$W$ 对应的行全为零**（$W\perp K_0$）；
- $H_A=V^{\mathsf T}AN$ 里 $W$ 对应的行是 $\varphi_w(u)=\langle w,A_{21}u\rangle$。

于是 $W$ 只通过
$$\Phi(W)=\operatorname{span}\{\varphi_w:w\in W\}\subseteq D^\circ,\qquad \dim D^\circ=c$$
进入铅笔——**$c$ 与行数 $t$ 无关**。且
$$\operatorname{row}(\lambda H-H_A)=\operatorname{row}\bigl(\lambda H_K-(H_A)_K\bigr)+\Phi(W),$$
故 $(5b)$ 只通过 $\Phi(W)$ 依赖 $W$ ✓。

**推论（他们的）**：
$$\exists W\ \text{使 }(5b)\iff\exists\Phi\subseteq D^\circ\ (\dim\Phi\le c,\ \Phi\ \text{可实现})\ \text{使 }(5b),$$
且同一 $\Phi$ 的任意代表元给出相同结论 ✓。$c=2$ 时这是 $\mathbb P^1$ 上的搜索 ⟹ **可穷尽**。

## 做法（迁移到我的框架）

我的障碍是：给定 $\mathcal S$ 与相容性 $U\subseteq W$，要判
$$\exists W\in\operatorname{Gr}(\omega,k):\quad\textbf{(R)}\ \operatorname{span}(\{h_i^0\}\cup\pi_1(\mathcal T_W))=W,\qquad
\textbf{(E)}\ E_\lambda(\mathcal T_W)=W\ \forall\lambda .$$
其中 $\mathcal T_W=\mathcal S\cap(W\oplus W)$。

**可迁移的三点**：

1. **"$W$ 只通过一个小维数的影子进入"**——算法线里是 $\Phi(W)\subseteq D^\circ$（$\dim=c$）；
   我这边应该找的是"$\mathcal T_W$ 只通过某个低维商进入 (R)(E)"的对应物；
2. **"同一影子的任意代表元等价"**——这把 Grassmannian 上的搜索压成**影子空间**上的搜索；
3. **$c$ 与 $t$ 无关**——这是可判性的来源：搜索维数不随实例规模涨。

## 进展

1. 算法线的 W-消去定理**可直接引用**（他们的定理 3 已给可实现性判据，见 [411](411_expert109_audit.md)）；
2. 我这边的对应物**尚未找到**：一般 $\mathcal S$ 下还没有"$\mathcal T_W$ 的低维影子"这种刻画；
3. 但方向明确：**只要证明 (R)(E) 只通过某个 $\dim\le c$ 的影子依赖 $W$，搜索就塌缩** ⟹ $q1\in\mathrm P$（在该设计下）；
4. 算法线已经做到的：$c=1$（超平面层，完全参数化 [374](../../c_stratification/attempts/374_complete_parameterization.md)/[378](../../c_stratification/attempts/378_parameterization_with_L0.md)、
   判定多项式 [375](../../c_stratification/attempts/375_stage2_bit_complexity.md)）、$c=2$（总图卡 [394](394_c2_total_charts.md)、
   复杂度定理 [408](../../c_stratification/attempts/408_c2_complexity.md)）、任意 $m$（双向判定 [382](../../c_stratification/attempts/382_general_m_two_way.md)）。

## 最终结论

1. **启发**：我这条线的"$\exists W$"不该硬碰 Grassmannian，而应找"**影子空间**"
   （算法线的 $\Phi(W)\subseteq D^\circ$ 是现成范例）；
2. **代价**：需要证明"$\mathcal T_W$ 的条件只通过影子依赖 $W$"——这是下一步的具体命题；
3. **收益**：若成立，$q1$ 的判定 = 低维搜索 + $\gcd$ 检验 ⟹ 多项式 ⟹ **硬度彻底关闭**；
4. **并行结论**：算法线已经把 $c=1$、$c=2$、任意 $m$ 的组合都做到了多项式判定 ⟹
   与我的"三层可算"在**方向上一致**，两条线正在收敛到"$q1\in\mathrm P$"。

## 放弃原因

- 没有把"$\mathcal T_W$ 的影子"构造出来（只指出它有范例、且必须存在才能推进）；
- 没有验证"影子"在一般 $\mathcal S$ 下是否与 $W$ 的 Grassmannian 坐标无关；
- 没有做 $c\ge3$ 的对接。

## 残留价值

- **一条可执行的迁移路线**：把算法线的 $\Phi(W)$ 思想搬到我的 (R)(E) 框架；
- 明确了它需要的那条命题（"只通过影子依赖 $W$"）；
- 两条线的方向性一致（都指向 $\mathrm P$），这在战略上有意义。

## 下一步

1. 在**算法线的 split 设计**里直接验我的 (R)(E)：$W$ 的行为已知（$H$ 的 $W$ 行为零、$H_A$ 的 $W$ 行是 $\varphi_w$），
   所以 (R) 变成 $\operatorname{span}(\{h_i^0\}\cup\pi_1(\mathcal T_W))=W$ 的显式形式——**这是可算的**；
2. 若在那个设计里 (R)∧(E) 也塌缩到 $\Phi$，则两条线的判据可以合并成一条。

## 相关文件

- [406_eliminate_W](../../c_stratification/attempts/406_eliminate_W.md)（算法线的 W-消去定理）
- [411](411_expert109_audit.md)（可实现性判据）
- [374](../../c_stratification/attempts/374_complete_parameterization.md)、[375](../../c_stratification/attempts/375_stage2_bit_complexity.md)、[394](394_c2_total_charts.md)、[408](../../c_stratification/attempts/408_c2_complexity.md)（算法线的多项式结果）
- [449](../../c_stratification/attempts/449_expert107_audit.md)（我这边 (R)∧(E) 的命题）

## 状态

- 启发记录：**[完成]**。
- "$\mathcal T_W$ 的影子"：**[未构造]**。
- 两条线合并判据：**[未做]**。
