# II.4 的审计：两个被排除的轨迹与非闭像（专家 2026-11-04 §2）

## 目标

专家对 II.4（incidence 维数 + 覆盖判据）提出两条反对意见，要求在把覆盖判据当定理之前解决：

* **Issue A**：像 $S$ 只是可构造集；射影维数定理只对**闭**子簇成立，取闭包不修复（$\mathbb P^{d-1}$ 可能只与
  边界相交，边界点不给有限 $\lambda$ 障碍）。
* **Issue B**：incidence 构造排除了两个轨迹——(B1) $L_0x\ne0$ 而 $z=0$；(B2) $L_0x=0$。二者不能从维数记账里丢掉。

## 设想与理由

旧 II.4 用"坏点直线"（$z=(\lambda I-A)x$ 的射影直线）做维数记账，但它把 $z=0$ 与 $L_0x=0$ 两个轨迹排除在外，
且像只是可构造集。专家的意见是：先把这两点处理掉，再谈覆盖。我的设想是**换语言**：
把"直线 $[z]$ 落在 $\mathcal Z$ 里"改成"$(\lambda I-A)x\in\mathcal Z$"——后者对 $z=0$ 也合法，
并且自然带出必要条件 $x\notin\mathcal Z$。

## 做法

先把"坏点直线"的非正式语言换成**精确的等价条件**（B.13c），再逐条审计。

## 进展

**（1）B.13c（已证，三行）**：$(5a)$ 下
$$(5b)\ \text{在}\ \mathcal Z\ \text{处失败}\iff\exists x\in V\setminus\mathcal Z,\ \lambda:\ (\lambda I-A)x\in\mathcal Z .$$
证明只用 $\mathcal L(\lambda x-Ax)=(\lambda I-\Lambda)\mathcal Lx$（$x\in V$ 时）与
$x\in V\setminus\mathcal Z\iff\mathcal Lx\ne0$。

**这条把 B1 完全解决**：若 $x\in V$、$L_0x\ne0$、$Ax=\lambda x$，则对**每个** $\mathcal Z\subseteq\ker L_0$ 都有
$x\notin\mathcal Z$ 且 $(\lambda I-A)x=0\in\mathcal Z$ ⟹ $(5b)$ 处处失败 ⟹ $q_{\min}=\infty$。
且该情形在"$(C,A)$ 可观测"下是**空**的：$V=\ker[C;CA]\subseteq\ker C$ 不含 $A$ 的特征向量。
（本项目全部实例满足 $(C,A)$ 可观测——因为 $L_0$ 可观测且 $\operatorname{row}L_0\subseteq\operatorname{row}\mathcal O(C,A)$。）

**B1 为什么以前看起来是漏洞**：旧的"坏点直线"语言写的是 $z=(\lambda I-A)x$ 的**射影直线** $[z]$，
$z=0$ 时没有直线；但 B13c 的判据根本不经过 $[z]$，只要求 $(\lambda I-A)x\in\mathcal Z$，故 $z=0$ 也合法 ✓。

**（2）B2（$L_0x=0$）**：此时 $\lambda$ 不被 $L_0$ 确定。但 B.13c 的判据同样不需要"$\lambda$ 由 $x$ 决定"：
对 $x\in V\cap\mathcal Z$ 无贡献（要求 $x\notin\mathcal Z$）；对 $x\in V\setminus\mathcal Z$ 且 $L_0x=0$，
条件变成 $(\lambda I-A)x\in\mathcal Z$ 对某个 $\lambda$ —— 这仍是一个线性条件（$\mathcal Z$ 固定时，
$\{\lambda:(\lambda I-A)x\in\mathcal Z\}$ 是仿射集，可能为空、单点或整条直线）。
所以 B2 不再是"被排除的轨迹"，而是 B.13c 判据里的**普通情形**；
需要单独处理的只是"$(\lambda I-A)x\in\mathcal Z$ 对**所有** $\lambda$ 成立"这种退化（此时 $\mathcal Lx\ne0$
而 $\mathcal L(Ax)=0$、$\mathcal Lx=0$？——后两者矛盾，故实际上不可能对所有 $\lambda$ 成立，
除非 $\mathcal Lx=0$，即 $x\in\mathcal Z$，而 $x\notin\mathcal Z$ 已排除）。**结论：B2 不需要单独处理。**

**（3）Issue A（非闭像）**：仍然有效，且 B.13c 不能修复它。要把覆盖判据变成定理，需要证明
$$\overline{S}\ \text{是闭子簇且}\ \overline{S}=S\quad\text{或}\quad\partial S\ \text{的每一点都不给出新的"避开"可能}.$$
本轮的判断：**不修**，把覆盖判据保持为【条件性】（专家也建议如此，见其 §Q1 排序第 5 项）。
可用的替代是 B.13c（精确判据）——它对**给定** $\mathcal Z$ 是精确的，只是不给出"整族"结论。

**（4）已验证的部分**：C4 的 $q_0=3$ 阶上，对 6 个图卡/参数显式构造 $(x,\lambda_0)$ 并核验
$\operatorname{rank}Q(\lambda_0)=5<h=6$（`drop_certificate.py`）。$\lambda_0$ 依次为
$1,\ 1-2\sqrt3,\ 3-2i,\ \frac52-\frac{\sqrt3}2 i,\ 1-2\sqrt3,\ 2-\sqrt3$ ——
**含无理数与复数**，再次说明谱条件不能只在有理 $\lambda$ 上检验。

## 最终结论

1. **B.13c 已证**：$(5b)$ 失败的精确几何刻画，且自动包含 $x\notin\mathcal Z$ 这一必要条件；
2. **B1 不再是漏洞**：它 ⟺ $q_{\min}=\infty$，且在 $(C,A)$ 可观测下为空；
3. **B2 不是漏洞**：B.13c 的判据不依赖"$\lambda$ 由 $x$ 决定"，B2 只是普通情形；
4. **Issue A（非闭像）仍未解决**：覆盖判据保持【条件性】，不进主结果。

## 放弃原因

不适用（审计完成；Issue A 明确留作未决）。

## 残留价值

* B.13c：一个比"坏点直线"更干净、且**精确**的等价刻画（含 $x\notin\mathcal Z$），可直接进论文 §2–§3；
* 两个"被排除轨迹"的处理方式（B1 是终止情形、B2 是普通情形）；
* 6 个显式掉秩证书（含无理/复数 $\lambda_0$），可作论文的示例。

## 相关文件

- `docs/02`：B.13c（新）、B.13（条件性）、B.12
- `tools/verification/drop_certificate.py`
- 专家答复：`workspace/for_expert/archive/11_next_steps-answer.md` §2
