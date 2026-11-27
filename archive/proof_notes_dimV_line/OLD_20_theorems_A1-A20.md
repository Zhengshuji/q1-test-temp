# 旧框架的 20 条定理（A1–A20，节选）

> **来源**：`archive/session_history/52_session_conclusion.md` §7.43.4（原文件 496 KB，此处只摘录该表）。
> **警告**：这是**旧框架**（$q_0$、$d_{CA}$、obs、$(A)/(S)$）的结论，**不得在新框架下直接引用**。
> 新旧对应与现状见 [archive/framework_map/README.md](../framework_map/README.md)。

### 7.43.4 **本会话状态（第 49 次修订）**

$$\boxed{\
\begin{array}{ll}
\textbf{已严格证明（20 条）} & A1\ (\text{Lean});\ A3;\ A4;\ A5;\ A6\ \textbf{充分性};\ A7;\ A8\ (\text{Lean});\ A9;\\
 & \textbf{A10 完整};\ A11;\ \textbf{A11 一般};\ A12;\ A13;\ A14;\ \textbf{A15};\ A16;\ A17;\ A18;\\
 & \boxed{\textbf{A19}：\rho\le\mathrm{obs}}\ ;\quad \boxed{\textbf{A20}：(\text{5a})\wedge(\text{5b})\Rightarrow\alpha_0\in V}\\
\textbf{推论} & \text{可行性}\iff\alpha_0\in V\ ;\quad \text{可行性判定}\in\mathrm{P}\\
\textbf{唯一缺口} & \boxed{\rho=\mathrm{obs}\ (\text{等式部分})}\ \Longrightarrow\ q_{\min}=\mathrm{obs}+1\ \Longrightarrow\ \textbf{q1 为假}\\
\textbf{新工具} & \textbf{almost }(A,\mathcal Z)\text{-不变子空间的铅笔刻画（Willems 1981）}\\
\textbf{q1 状态} & \textbf{既未证明也未证伪}\ ——\ \text{硬度不能来自可行性}\ ✓\\
\textbf{更正} & \mathbf{41}\ \text{处}\\
\textbf{Lean} & \mathbf{73}\ \text{定理};\ \texttt{lake build}\ \to\ \textbf{18134 jobs}
\end{array}}$$


## 读者的正确用法

1. 想知道"某条旧定理现在还算不算" → 查 [framework_map](../framework_map/README.md) 的状态表；
2. 旧框架的核心链条是 `A19 (rho<=obs) + rho=obs ⟹ q_min = obs+1 ⟹ q1 假`，
   该链条的第二步被 2026-10-24 的 $n{=}5$ 反例推翻（$q_{\min}=1<2=\mathrm{obs}+1$）⟹ **旧目标已废**；
3. 但 A1（(5a) 的 4 块形式）、A5/A8（Lean）等**地基性**内容在新框架下仍然成立（见状态表）。
