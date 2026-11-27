# 83 号裁决落实：q1 三结局并存；主线算法，硬度转 ARM(3)

> 2026-11-10。83 号的战略判断：
> - 不能从两条参数化算法推断 q1 的最终复杂度；$\\mathrm P$、$\\exists\\mathbb R$-完全、参数化中间都仍可能；
> - $\\exists\\mathbb R$-完全与固定 $\\kappa_{\\rm obs}$ FPT **不矛盾**（难实例的 $\\kappa$ 可以增长）；
> - 硬度最佳源：**ARM(3)**（仿射秩最小化），其次 matroid realization；
> - 不建议继续局部 multiplication gate；
> - 参数化下界只做 **$q$ 的 W[1]-hard**；$\\kappa_{\\rm obs}$ 的 W[1]-hard 会与 FPT 冲突。
> 状态：**M3（专家裁决）**。

## 目标

落实 83 号的 q1 路线，并更新项目主线。

## 设想与理由

83 号给出战略判断；先记录结论，再更新 Phase A/B/C 路线。

## 做法：四条

### 1. q1 的可能复杂度

三种都未被排除：
- $q1\\in\\mathrm P$；
- $q1$ 是 $\\exists\\mathbb R$-完全；
- 参数化中间：$\\mathrm{XP}(q)$ + $\\mathrm{FPT}(\\kappa_{\\rm obs})$ + $q$ 的 W[1]-hard。

关键逻辑：
$$\\exists\\mathbb R\\text{-完全}\ \not\\Rightarrow\ \\text{固定 }\\kappa\\text{ 不可 FPT},$$
因为难实例可以让 $\\kappa_{\\rm obs}$ 随输入增长。
固定 $q$ 多项式也不排除 $\\exists\\mathbb R$-hard，因为归约需要 $q$ 增长。

### 2. 硬度源排序

| 源 | 匹配度 | 缺口 |
|---|---|---|
| **ARM(3)**（仿射秩最小化，固定秩 3）| 最强：全局秩、仿射约束、gauge | 把 ARM 的任意仿射耦合变成 q1 的逐行 $\\mathcal T$ |
| matroid realization（rank 3）| 强：全局向量依赖 | 用 q1 的全局行空间表达大量子集秩 |
| polynomial-matrix unimodularity | 强：匹配 $(5b)$ | 找特殊 pencil 的硬输入类 |
| 一般 structured matrix completion | 可能 | 需要完全相同的行对限制 |

83 号建议：先做 **ARM(3) → q1 的单个翻译引理**，而不是完整归约。

### 3. sound multiplication

- 没有一般 no-go；
- 已有 no-go 只覆盖：
  - universal-lift + $R=0$ 可行（303 的 bypass）；
  - 固定共享端口 $E_1\\cap E_2=D$ 为固定线；
- 真正的 no-go 需覆盖所有 $A,C,L_0,\\mathcal T,\\omega$ 与全局解码；
- 若再做乘法，应用 **gauge-fixed global rank representation**（固定锚块 + 全局行空间规范），而不是逐行 gate。

### 4. 参数化下界

- $\\kappa_{\\rm obs}$：已有 FPT；W[1]-hard 会推出 FPT=W[1]，不做；
- $q$：已有 XP；W[1]-hard **相容**，是合法方向；
- 归约需让 $q=O(t)$ 而 $\\kappa_{\\rm obs}$ 随图规模增长；
- 可能目标：$q1\\in\\mathrm{XP}(q)$、$q$-W[1]-hard、$\\kappa_{\\rm obs}$-FPT。

## 最终路线（83 号）

**Phase A（最高优先）**：完成算法论文
1. FPT 六引理：压缩、Gram、Bezout、Gram 证书、Cauchy–Binet、比特复杂度；
2. 固定 $q$ 的第二定理（$G=FX$ + 秩一致性）；
3. 显式化 $q1\\in\\exists\\mathbb R$ 的 polynomial left-inverse 证书；
4. 处理 $r=0,k=0,\\omega=0$；
5. 与 Fernando 2026 的定位比较。

**Phase B（次要）**：一个受控硬度实验
1. 读并验证 ARM(3) 的 gauge/composition；
2. 找出 ARM 中跨行耦合的仿射约束；
3. 尝试用固定行做 gauge、用 $\\mathcal T$ 编码仿射约束；
4. 里程碑是一个“翻译引理”，不是完整归约。

**Phase C（更后）**：$q$ 的 W[1]-hard
- 源：Multicolored Clique；
- 要求 $q=O(t)$、$\\kappa_{\\rm obs}$ 增长。

## 论文四定理（83 号）

1. $q1\\in\\exists\\mathbb R$；
2. 固定 $q$：$q1\\in\\mathrm P$，$\\mathcal L^{O(q^2)}$；
3. 固定 $\\kappa_{\\rm obs}$：$q1\\in\\mathrm{FPT}$，$f(\\kappa)\\operatorname{poly}(\\mathcal L)$；
4. 组合上界：
$$T\\le\\min\\{\\mathcal L^{O(q^2)},\\ f(\\kappa_{\\rm obs})\\operatorname{poly}(\\mathcal L)\\}.$$
不写 unrestricted hardness 声明。

## 进展

* q1 三结局的明确表述；
* 硬度源排序（ARM 第一）；
* 参数化下界只做 $q$；
* 三阶段路线与论文四定理。

## 最终结论

* 主线是算法论文，不是继续 gate；
* 硬度只做一个 ARM(3) 翻译实验；
* $q$ 的 W[1]-hard 是后续；
* q1 本身仍开放。

## 放弃原因

* 未做 ARM 翻译；
* 未完成 FPT 比特复杂度；
* 未写论文。

## 残留价值

* 一个明确的战略裁决；
* 论文四定理框架；
* Phase A/B/C 路线。

## 相关文件

* [83 答复](../../../for_expert/archive/83_project_consolidation_q1_roadmap-answer.md)
* [attempts/313](../../../q1_false/decision_algorithms/attempts/313_fpt_proof_sketch.md)
* [attempts/312](../../../q1_false/decision_algorithms/attempts/312_fixed_q_proof_sketch.md)

## 状态

* 裁决落实：**[M3]**。
* ARM 实验：**[未做]**。
