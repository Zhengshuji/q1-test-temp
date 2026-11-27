# 352 ARM(3) → q1：前史清点与一次独立的可行性分析

> 用户指定：独立尝试 F（ARM(3) 翻译引理），并先整理项目在这条路线上做过什么。
> **结论先行**：**没有**得到归约；但把"自然嵌入"算清了，并证明了一条**硬约束**：
> q1 的自由数据只有 $d_0\le n-p$ 列，而 ARM 的载体是 $m\times n$——所以**逐行忠实**的线性编码不可能。
> 剩下的可编码部分是一个更弱的翻译（约束可传递，秩条件必须重新编码），这就是下一步的靶子。

## 目标

1. 清点项目在硬度/ARM 路线上的全部记录（避免重复）。
2. 独立分析：ARM(3) 与 q1 的变量和条件能否对上，并给出**必要条件**。

## 设想与理由

83 号：最佳源是 ARM(3)（Majumdar 2026，arXiv:2602.14037），先做**一个翻译引理**，不是完整归约；
障碍预计是"$\mathcal T$ 的逐行同一性"。93/96 号：不要局部乘法门，走**全局秩解码**。
那就先把两边的变量空间与条件形状摊开比较。

## 前史清点（项目在这条路线上做过什么）

| # | 文件 | 做了什么 | 结果/状态 |
|---|---|---|---|
| 1 | [09_hardness_blueprint](../../../q1_true/attempts/09_hardness_blueprint.md) | 形式 A（$\exists\mathbb R$-难）/ B（NP-难）/ C（条件性）；Löfberg gadget 对照表；三大障碍 | **蓝图**；$\rho=2$ 容器唯一 ⟹ 硬度只能从 $\rho\ge3$ 或 $c\ge2$ |
| 2 | [10_hardness_attempt](../../../q1_true/attempts/10_hardness_attempt.md) | 具体尝试"两个成员"编码一位布尔 | **失败**；四卡点：型层非乘积（$(5a)$ 耦合）、$(5b)$ 是开条件需精确打闭集、要覆盖正维整层、$\mathbb F_p$ 不能提升 |
| 3 | [296](../../multiplication_gate/attempts/296_nonzero_gadget_observer.md) | sound 非零门：$(5b)\iff r_2\ne0$，对**所有** $R$ | **成功**（两个 sound 门之一） |
| 4 | [303C](../../../q1_false/decision_algorithms/attempts/303_79_verdict_lifts.md) | sound 输入非零门：$\exists R:(5a)\wedge(5b)\iff x\ne0$ | **成功** |
| 5 | [306](../../multiplication_gate/attempts/306_80_soundness_correction.md) | 乘法门 $z=xy$ | **unsound**（$R=0$ 绕过）；只是 realization |
| 6 | [315](315_83_verdict_roadmap.md) | 83 号落实：硬度源排序（ARM 第一）；Phase B 只做翻译引理 | ARM **未做** |
| 7 | [Majumdar 笔记](../../../../literature/notes/MAJUMDAR_2026_ARM_ER.md) | ARM(3) 是 $\exists\mathbb R$-完全；可借三件技术：违反⟹满秩子式 / gauge block / composition lemma | 记录；注明"没有把 $(H,H_A)$ 模拟成带 gauge 的 $X$" |

**一句话**：局部门路线已被否定（只两个 sound 门），全局翻译引理**一次都没做过**。

## 做法：形状对照

### 1. q1 的自由数据

自由行只通过
$$\Phi=R\,[N\ AN]\in\mathbb C^{m\times d_0},\qquad d_0=\operatorname{rank}[N\ AN]$$
进入条件，且 $R\mapsto\Phi$ 满射（$[N\ AN]$ 行满秩），故 q1 的自由数据恰是 $\Phi\in\mathcal T^{\,m}$。

> **命题（载体界）.** $d_0\le n-p$。

*证明.* 每个 $N$ 的列与每个 $AN$ 的列都落在 $K_0=\ker[C;CA]$ 里，故都被 $C$ 的**每一行**消去；
于是 $[N\ AN]$ 的所有列落在 $\ker C$（$n-p$ 维）里，秩 $\le n-p$。$\square$

**实测（c342）**：$n=4..10$、$p=1,2$ 的 7 个模式上 $d_0\le n-p$ 全部成立，而且**全部取等**（$d_0=n-p$）——
即 $[N\ AN]$ 的列恰好张成 $\ker C$。于是 q1 的载体就是 $m\times(n-p)$ 的。

### 2. 逐行忠实编码不可能

若要把 ARM 的 $X\in\mathbb C^{m\times n}$ 用 $\Phi$ 编码且**每行都可辨识**（存在单射线性 $\mathbb C^n\hookrightarrow\mathcal T$），
需要 $n\le d_0\le n-p$——**$p\ge1$ 时不可能**。

> **98 号 §6.1 的限定**：这排除的是**直接逐行编码** $r\mapsto(rN,rAN)$ 忠实表示**任意** $n$ 维载体行；
> 它**不是**"所有翻译都不可能"的定理——用受限行空间或其它表示编码仍有可能。

也就是说：**最朴素的逐行翻译**必须接受"丢掉 $p$ 个方向"（q1 只能看到 $d_0$ 个线性泛函的方向），
但别的编码方式未被排除。

### 3. 还能救的部分：让 ARM 的约束因子化

取一个 $n\times d_0$ 的满列秩 $M$（$\operatorname{col}M=\mathcal T$ 的坐标像），令
$$\Phi=X M\qquad(\text{即 }X\text{ 只通过其列在 }\operatorname{col}M\text{ 上的投影被看到}).$$
则对 $A_\ell=M a_\ell^{\mathsf T}$（每行落在 $\operatorname{col}M$ 里）有
$$\langle A_\ell,X\rangle=\operatorname{tr}(A_\ell^{\mathsf T}X)=\langle a_\ell,\Phi\rangle .$$
**所以"仿射约束"这一半是可以传递的**：它们变成 $\Phi$ 上的线性约束。

而秩条件要小心：$\operatorname{rank}\Phi\le\operatorname{rank}X\le3$，反之给定 $\operatorname{rank}\Phi\le3$ 时
$X=\Phi M^{+}$ 给出 $\operatorname{rank}X\le3$ 且 $XM=\Phi$ ✓。**所以"$\operatorname{rank}X\le3$"翻译成"$\operatorname{rank}\Phi\le3$"是等价的。**

### 4. 于是剩下的任务被精确指认

> **翻译引理 = 构造 $(A,C,L_0)$ 使 q1 的可行集恰为**
> $$\left\{\Phi\in\mathcal T^{\,m}:\ \langle a_\ell,\Phi\rangle=b_\ell,\ \operatorname{rank}\Phi\le3\right\}.$$

而 q1 的条件是 $\operatorname{rank}H=\omega$、$(5a)$、$(\operatorname{rank}(\lambda H-H_A)=\omega\ \forall\lambda)$。
其中只有 $H$ 是 $\Phi$ 的线性像；**没有任何一条直接给"$\operatorname{rank}\Phi\le3$"**。
且注意方向差：q1 的层条件是**等式**（秩恰为 $\omega$）+ $(5a)$ 的**包含**；ARM 的秩界是**不等式**（闭集）。

## 进展

1. 前史清点完成（7 条，含死因）。
2. **载体界 $d_0\le n-p$ 已证**，并在 $n=4..10$、$p=1,2$ 上精确验证；7/7 取等。
3. 由载体界得：**逐行忠实编码不可能**（$p\ge1$）。
4. 但"丢掉 $p$ 个方向"后**约束仍可传递**（$A_\ell=Ma_\ell^{\mathsf T}$ 时 $\langle A_\ell,X\rangle=\langle a_\ell,\Phi\rangle$），
   而秩界可等价地换成"$\operatorname{rank}\Phi\le3$"。
5. 因此翻译引理的靶子被缩成一句：**让 q1 的条件等价于"$\operatorname{rank}\Phi\le3$"（连同线性约束）**。

## 第二个障碍：q1 的**仿射控制**只有固定行

查 Majumdar 的构造（`papers/2602.14037.txt`）：每个 gate 占一个**载体位置** $(r_i,c_i)$，
gadget 用"从不复用的新行/列"（O(1) 个），约束是 $\mathrm{tr}(A_\ell X)=b_\ell$ 型的**一般线性泛函**
（加法门是三项关系，不是钉住单个条目）。

而 q1 这边：$R=[L_0;R_{\rm free}]$，故
$$\Phi=R[N\ AN]\ \Longrightarrow\ \Phi\ \text{的**前 }r_0\text{ 行被 }L_0\text{ 钉死},\ \text{其余行完全自由}.$$
$(5a)$ 与铅笔条件是**非线性**的，不能当仿射约束用。

于是：

> **命题（仿射控制）. q1 能对自由数据施加的仿射约束只有"钉住前 $r_0$ 行"这一种。**

> **98 号 §6.2 的细化**：固定行（$L_0$）钉住的是**仿射**（非齐次）条件；
> 而"钉住引理"（353）给出的可行集是 $\mathcal L=\{R:(h_i,g_i)\in\mathcal T\cap(W_0\times W_0)\}$
> ——那是**齐次线性**的。两者不要混：钉住块给的是**线性**限制，
> 要模拟 $x_1+x_2=1$ 这种非齐次仿射约束，需要**单独构造**（用固定行的参考数据去平移），
> 不能从定理直接推出。

**后果**：ARM 的一般线性约束 $\langle A_\ell,X\rangle=b_\ell$ 无法用 $L_0$ 编码
（除非每条约束都只涉及被钉住的行——那样的 ARM 实例是平凡的）。
所以"忠实载体 + 线性约束"的翻译**不通**；要编码门关系，只能靠**秩条件**——也就是 gadget 路线，
而 303/306 已证乘法门 **unsound**。

这把 83 号"不要局部门、走全局"的口号变成了一个具体的技术困难：
**全局编码仍然要表达门关系，而表达门关系的唯一工具是秩条件 gadget，现有 gadget 库不足以表达乘法。**

## 最终结论

**没有翻译引理**，但得到三条明确的结构性结论：

1. **载体界**：$d_0\le n-p$（已证、已验证、取等）⟹ 逐行忠实编码不可能；
2. **约束传递**：把载体限制在 $\operatorname{col}M$ 上时，仿射约束可传递、秩界可等价换成 $\operatorname{rank}\Phi\le3$；
3. **仿射控制不足**：q1 只能钉住前 $r_0$ 行 ⟹ 一般线性约束无法编码 ⟹ 门关系只能靠秩条件 gadget，
   而乘法 gadget 已被证 unsound。

**因此 ARM 路线与"局部 gadget 是否 sound"不是两个独立问题**——这是本次最重要的发现。

## 放弃原因

- 没有构造出编码；$\operatorname{rank}\Phi\le3$ 与 q1 条件的桥没找到。
- 只读了 Majumdar 的笔记与部分原文（载体位置、gadget 的 O(1) 行列），未验证 gauge/composition 的可迁移性。
- 没有把"仿射控制不足"写成不可行定理（只是指出 q1 的仿射自由度就是前 $r_0$ 行）。
- 没有检查：门关系能否只用**秩条件**表达（这等价于要一个 sound 乘法 gadget）。

## 残留价值

- 不重复的前史（7 条 + 死因）；
- **载体界 $d_0\le n-p$**（已证 + 已验证），以及由它得到的"逐行忠实编码不可能"；
- **仿射控制命题**：q1 对自由数据的仿射约束只有"钉前 $r_0$ 行"；
- 把下一步从"做归约"改成一句可检验的话：**门关系能否只用秩条件表达**——
  也就是说，ARM 路线最终回到"sound gadget 是否可能"，而不是绕开它。

## 相关文件

- [09_hardness_blueprint](../../../q1_true/attempts/09_hardness_blueprint.md)、[10_hardness_attempt](../../../q1_true/attempts/10_hardness_attempt.md)
- [296](../../multiplication_gate/attempts/296_nonzero_gadget_observer.md)、[303](../../../q1_false/decision_algorithms/attempts/303_79_verdict_lifts.md)、[306](../../multiplication_gate/attempts/306_80_soundness_correction.md)
- [315](315_83_verdict_roadmap.md)、[Majumdar 笔记](../../../../literature/notes/MAJUMDAR_2026_ARM_ER.md)
- [c342](../../../../tools/verification/c342_carrier_dimension.py)

## 状态

- 前史清点：**[完成]**。
- 载体界 $d_0\le n-p$：**[已证-纸面]** + **[精确验证 7 模式]**。
- 仿射控制命题：**[已证-纸面]**（$R$ 的分解 + 前 $r_0$ 行固定）。
- 翻译引理：**[未得到]**；已定位到"门关系能否只用秩条件表达"这个关口。
