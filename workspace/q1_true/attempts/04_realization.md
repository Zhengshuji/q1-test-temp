# 路线 04：实现定理（专家优先级 2）

## 目标

给定 $(V,Z,\bar A)$，判断是否存在 $A$ 同时满足 $V=\ker[C;CA]$、诱导出 $\bar A$、且 $(A)$ 成立。

## 设想与理由

专家建议（QA12 §6）：用 $\beta_A:W\to\mathbb R^n/W$、$\beta_A(w)=Aw+W$ 化简，先看耦合是否真的限制。

## 做法

$W=\ker C$（$\dim n-p$）、$V\subseteq W$、$S=V\cap Z$。分解 $A|_W=\beta+\gamma$，$\beta:W\to\mathbb R^n/W$、$\gamma:W\to W$。

## 进展

**定理 F（实现是自由的）**：设 $V\subseteq W$、$\operatorname{codim}_W V\le p$、$Z\subseteq W$、$\bar A:V/S\to W/Z$ 线性。
则存在 $A$ 使 $V=\ker[C;CA]$、$\bar A_A=\bar A$、且 $(A)$ 成立。

*证明*：
1. $\operatorname{codim}_W V=r\le p$ ⟹ 存在 $\beta:W\to\mathbb R^n/W$ 以 $V$ 为核（把 $V$ 的补映到 $\mathbb R^n/W$ 的 $r$ 维子空间）；
2. 取 $\gamma:W\to W$，使 $\gamma|_V$ 在模 $Z$ 下实现 $\bar A$、$\gamma(S)\subseteq Z$、$\gamma(\ker\beta|_Z)\subseteq Z$
   （$\bar A(S)=0$ 保证前两条相容；第三条只在 $S$ 以外约束，自由）；
3. 令 $A|_W=\beta+\gamma$，$A$ 在 $W$ 的补上任意；
4. 则 $w\in W$ 时 $Aw\in W\iff\beta(w)=0\iff w\in V$ ⟹ $V=\ker[C;CA]$ ✓；
5. $\bar A_A(v+S)=Av+Z=\gamma(v)+Z=\bar A(v+S)$ ✓；
6. $(A)$：$CAZ\cong\beta|_Z$，$\ker(CAZ)=\ker(\beta|_Z)$，其上 $Az=\gamma(z)\in Z$ ✓。∎

## 最终结论

**实现几乎无约束**：给定 $(V,Z,\bar A)$（只需 $V\subseteq\ker C$、$\operatorname{codim}_W V\le p$），总能实现。
这与专家的猜测（"耦合可能限制、硬度可能藏在实现里"）**相反**。

**数值验证**（[c245](../../../proof/layer_program/c245_realization_verify.py)，规范坐标 $C=[I_p\mid0]$、$n=6$、$p=2$、
$\bar A=0$、$\gamma(W)\subseteq Z$）：**6/6** 通过——$V=\ker[C;CA]$ 精确匹配、$AV\subseteq Z$、$(A)$ 成立。
（验证的是这个构造，不是定理的全部情形；定理本身是纸面证明。）

**推论**：硬度不可能来自"实现约束"；它只能来自 $A$ 是**给定**的、而 $Z$ 要选这一侧的结构
（即 $(A)$ 对 $A$-固定的限制）。这支持"多项式结局"一侧。

## 放弃原因

（不适用：定理已证，非失败路线。）

## 残留价值

- 排除"实现约束是硬度来源"这一假设；
- 把问题精确定位到"固定 $(A,C,L_0)$ 时 $(A)$ 对 $Z$ 的限制"。

## 相关文件

- [proof/h_bound/README.md](../../../proof/h_bound/README.md)（Theorem C/D/E）
- [archive/expert_correspondence/QA12_2026-10-31.md](../../../archive/expert_correspondence/QA12_2026-10-31.md) §6
