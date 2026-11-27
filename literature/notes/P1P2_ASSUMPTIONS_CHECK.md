# P1/P2 的定理级假设核对清单（专家 QA9 §8 的五点）

> 目的：在"引用 P1/P2 已解决刻画"之前，逐条核对他们的假设与本项目的定义是否一致。
> 状态：2026-10-30，**已核对 4/5**；第 3 条（满行秩/独立性）需再读一节证明。

| # | 假设/约定 | P1/P2 的写法 | 本项目 | 是否一致 |
|---|---|---|---|---|
| 1 | **底域** | 输入取实矩阵 $A\in\mathbb R^{n\times n}$、$C\in\mathbb R^{p\times n}$；谱条件 $\lambda\in\mathbb C$ | 项目定义在 $\mathbb C$ 上；判据对复 $A,C$ 同样成立（多项式恒等式）| **一致**（$\mathbb R\subset\mathbb C$；实输入是我们的特例）✓ |
| 2 | **$L$ 独立** | $r=\operatorname{rank}L$，且要求 $\operatorname{rank}[C;L]=p+r$（把 $L$ 中落在 $\operatorname{row}C$ 的部分先去掉）| 项目的 $L_0$ 任意；层号里 $c_0=\dim(\operatorname{row}L_0\cap\mathcal J)$ 已处理"落在 $\mathcal J$ 里的部分"| **已解决** ✓：$L_0$ 中落在 $\operatorname{row}C$ 的行可去掉（每去一行 $q_{\min}$ 减 1），见 [../../proof/l0_reduction/README.md](../../proof/l0_reduction/README.md)（[精确验证 100/100]）；$\operatorname{row}[C;CA]\setminus\operatorname{row}C$ 的分量**不**需去掉（P2 的假设只要求独立于 $C$）|
| 3 | **增广满行秩** | $\operatorname{rank}\mathcal L=q$（约化增广）| 项目要求 $q$ 行满秩 ✓ | **一致** ✓ |
| 4 | **谱条件类型** | Thm 6 明写 $\Omega_S=\mathbb C$（pole assignability）时 $g_{I,\Theta}$ 为非零常数；$\Omega_S=\{ \Re\lambda\ge0\}$ 对应 detectability | 项目 $(5b)$ 是 $\forall\lambda\in\mathbb C$（= pole assignability）| **一致** ✓（注意：detectability 版本**不是**本项目的问题）|
| 5 | **覆盖的阶范围** | P2 Thm 9：覆盖 $q\in[q_0,\,n_0-p]$ **全部**阶；Thm 2 证明 $(A)$ 在这段上无间隙 | 项目的 $q_{\min}$ 是**最小**可行阶，落在同一区间 | **一致**，且比项目更强（覆盖全部阶）✓ |

## 需要补的两件事

1. **第 2 条的归约**：P2 假设 $\operatorname{rank}[C;L]=p+r$。本项目的 $L_0$ 可以含有 $\operatorname{row}[C;CA]$ 的分量
   （$c_0>0$）。需确认：把 $L_0$ 换成"$L_0$ 模 $\operatorname{row}[C;CA]$ 的独立部分"后，问题是否等价
   （直觉：这些分量可由输出 $C$ 直接提供，所以可去掉；但要写出归约）。
2. **第 4 条的表述**：P2 的 $\Omega_S$ 允许 detectability；本项目只用 $\mathbb C$。引用时须显式说明"我们取 pole assignability"。

## 引用时的措辞（建议）

> "P2 (arXiv:2609.37992) Thm 5/6/9 在**实输入、pole assignability（$\Omega_S=\mathbb C$）、$\mathcal L$ 满行秩**的设定下
> 给出逐阶充要条件与阶谱。本项目取 $\mathbb C$ 上的输入，是其特例；$L_0$ 含 $\operatorname{row}[C;CA]$ 分量时的归约
> 见 §2 的讨论。"

