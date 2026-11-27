# 460 从 Paper I/II 的专家评审里得到的三条hardness 侧工具

> 用户转来专家对 Paper I/II 的评审。本文件摘出**对硬度侧真正有用**的三条，以及它们如何改变我这条线。

## 目标

把评审里可用的技术点接进我这条线（判定形状 + 硬度路线）。

## 设想与理由

评审里大部分是论文定位与发表策略（对硬度侧无用）。真正有用的是几条**已证的数学结论**。

## 做法

从评审里只摘已证的数学结论，逐条判断能否接进我这条线的判据。

## 进展

### 1. **已证的下界 $\dim W\ge\omega+1$**（评审 §2.3 转述 Paper I）

复现他们的论证：若 $\dim W=\omega$（即 $\dim\mathcal T_W=\omega$），则 $W$ 是某线性映射 $F$ 的**图**，
$$W=\{(h,Fh):h\in U\}.$$
$\mathbb C$ 上有限维线性映射必有特征值 $\lambda_0$，故 $\operatorname{rank}(\lambda_0 I-F)<\omega$ ⟹ 谱条件失败。
**所以必须 $\dim\mathcal T_W\ge\omega+1$** ✓。

**对我的用处**：
- 这正是我一直想证未证的"行数下界"（$m\ge\omega+1$ 的来源，见 [417](417_expert104_audit.md)/[428](428_expert105_audit.md) 的"必要条件"）；
- 它与 [452](../../c_stratification/attempts/452_E_simplified.md) 的 (R)(E$'$) 合起来给出**完整的维数约束**：
$$\omega+1\ \le\ \dim\mathcal T_W\ \le\ 2\omega,$$
  中间层可行集在 Grassmannian 的**中间维数层**上。

### 2. **影子是真的：$\dim W\le2\ell$，$\ell=\operatorname{rank}(AN)$**（评审 §2.3 转述 Paper I）

Paper I 证了 $\pi_1(W)=\pi_2(W)\subseteq S=\operatorname{row}(AN)$，故 $\omega\le\ell$，从而
$$\boxed{\dim W\le 2\ell}$$
——**与状态维数 $n$ 无关** ✓✓。

**对我的用处**：这是我在 [450](450_shadow_idea.md) 里要找的"影子"，**已经被 Paper I 证出来了**：
搜索空间的维数上界是 $2\ell$（不是 $n$），所以"$\exists W$"的搜索**天然是 $\ell$-参数化的** ✓。
我在 454/456 里纠结的"开/闭/泛型"问题，**对复杂度不是决定性的**——因为搜索空间本身小。

### 3. **Cauchy–Binet / Gram 压缩**（评审 §2.4）

不必枚举全部最大子式：用 Cauchy–Binet 把谱条件压到一个由 $\ell$ 控制的 **Gram 矩阵**上 ✓。

**对我的用处**：我检查 (R)(E$'$) 时的子式枚举可以用这个压缩，把 $k$ 大的情形也压到 $\ell$。

## 评审里对硬度**直接相关**的判词

> "研究能否把已知的 $\exists\mathbb R$-hard 问题嵌入功能观测器的**两个耦合秩条件**"
> "利用子空间 $W$ 的结构，尝试构造 NP-hardness reduction"
> 并明确把 "DEC 是 P / NP-hard / $\exists\mathbb R$-complete" 列为**最重要的开放问题**。

——这正是我在 [459](../../../q1_true/multiplication_gate/attempts/459_hardness_paths.md) 里列的**未试路径 #1/#2**，而且**被专家明确认可** ✓。

## 最终结论

1. **获得两条已证约束**：$\omega+1\le\dim\mathcal T_W\le2\ell$ ⟹ 中间层的可行集在**中间维数层**上，
   且**维数与 $n$ 无关**（$\ell$-参数化）✓；
2. **"影子"不必再找**：Paper I 已经给出（$\dim\le2\ell$）⟹ 我 450 的猜想在一般情形也成立 ✓；
   ⟹ 454/456 关于"开/闭/泛型"的争论**对复杂度不是关键**（搜索空间已被 $\ell$ 限住）；
3. **硬度路线的正确形态**由评审给出：把 $\exists\mathbb R$-难问题嵌入**两个耦合秩条件**
   —— 这正是我该做的下一步，而且它**不需要**先解决"可行集类型"的问题 ✓。

## 放弃原因

- 没有把 Cauchy–Binet 压缩实现在我自己的 (R)(E$'$) 检查里；
- 没有开始"嵌入 $\exists\mathbb R$-难问题"的具体构造；
- 没有核对 Paper I 的 $\dim W\ge\omega+1$ 与我的 $\mathcal T_W$ 定义是否**逐字**对应（我用的是 $\mathcal S\cap(W\oplus W)$，
  他们用的是 $\operatorname{row}[H\ H_A]$；两者应同构，但要逐一核对）。

## 残留价值

- **两条已证约束**（$\omega+1\le\dim\le2\ell$）接进我的框架；
- **"影子"问题被 Paper I 解决**，我这条线的 450–456 可以收尾；
- **硬度路线被专家确认**：嵌入两个耦合秩条件 ⟹ 这是下一步的主攻方向。

## 下一步

核对两个 $W$ 定义的同构，然后把"$\omega+1\le\dim\mathcal T_W\le2\ell$"写成我框架里的命题；
接着按评审建议，选一个 $\exists\mathbb R$-难问题尝试嵌入 (R)(E$'$)。

## 相关文件

- [450](450_shadow_idea.md)（影子猜想，已被 Paper I 证实）
- [452](../../c_stratification/attempts/452_E_simplified.md)（(R)(E$'$)）
- [459](../../../q1_true/multiplication_gate/attempts/459_hardness_paths.md)（未试路径，与评审建议一致）
- [417](417_expert104_audit.md)（行数下界的早期表述）

## 状态

- 两条约束接入：**[完成]**。
- 两个 $W$ 定义的同构核对：**[未做]**。
- 嵌入 $\exists\mathbb R$-难问题：**[未做]**。
