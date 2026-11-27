# arm_reduction —— ARM(3) 翻译（硬度侧）

> 状态：**关闭（2026-11-27）**：行包含接口 no-go（488）、谱机制无构造（489）；只保留 no-go 与靶子。上级：[q1_true](../README.md)。

## 目标

用 Majumdar 的 ARM(3)（仿射秩最小化，$\exists\mathbb R$-完全）做翻译引理：
把 ARM 的仿射约束 + 单一秩约束搬到 $(5a)\wedge(5b)$ 的压缩层。

## 已有结论（详见 [PLAN.md](PLAN.md)）

- **载体界** $d_0\le n-p$（已证、已验证）⟹ 逐行忠实编码任意 $X$ 不可能；
- 约束可传递（限制到 $\operatorname{col}M$ 后），秩界可换成 $\operatorname{rank}\Phi\le3$；
- 但 q1 的仿射控制只有“钉住前 $r_0$ 行”，且没有一条条件给 $\operatorname{rank}\Phi\le3$；
- 于是门关系只能靠秩 gadget，而乘法 gadget 已 unsound——ARM 与“sound gadget 是否可能”是同一关口。

## 里程碑

一个**翻译引理**（不是完整归约）。当前只做候选接口 $X=[L;L_{\rm fix}]$ 的行包含检验；
三步与失败判据见 [PLAN.md](PLAN.md)。

## 先读

- [PLAN.md](PLAN.md)（现状 + 三步规划）
- `attempts/390_arm_translation_analysis.md`（最完整分析）
- `literature/notes/MAJUMDAR_2026_ARM_ER.md`
