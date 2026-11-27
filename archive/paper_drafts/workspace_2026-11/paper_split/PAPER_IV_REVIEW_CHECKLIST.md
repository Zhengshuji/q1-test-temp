# Paper IV 修改清单（据专家审查意见 2026-11-22）

目标文件：`paper/current/paper_IV_c2.tex`（唯一事实源）。旧版已归档于 git 历史。
原则：不改结论，只修表述、补证明、正确定义；每条都要能编译且 0/0/0/0。

## P1 数学正确性（必须）

| # | 专家条目 | 具体动作 | 状态 |
|---|---|---|---|
| 1 | ① Claim 3 的 $D\subseteq K_0$ 坐标错误 | $K_0=\operatorname{span}\{e_5..e_8\}$ 而 $D$ 用前四个基向量。引入 $f_i=e_{4+i}$，把 $D$ 写成 $\operatorname{span}\{f_1+f_2,f_3+f_4\}$；并检查 $A,AD,U,V$ 是否同一套坐标 | 待做 |
| 2 | ② $K_0^*$ 与 $D^\circ$ 混淆 | Notation 里删掉"$K_0^*$ is the annihilator of $D$"，改为 $D^\circ=\{\varphi\in K_0^*:\varphi|_D=0\}$、$\dim D^\circ=k-\dim D$；全篇统一用 $D^\circ$ | 待做 |
| 3 | ② 五个量的统一表 | 全文统一：$\omega=\operatorname{rank}H=k-\dim(K_0\cap V^\perp)$、$c=k-\omega$、$t=q-\omega$、$\dim(V\cap K_0)=t$、$\dim D^\circ=\omega$；凡出现 $\dim D^\circ=\dim(V\cap K_0)$ 处一律改 | 待做 |
| 4 | ③ Claim 3 的反例缺完整构造 | 给出 $A$ 的分块形式（$A_{11}=M$ 为 $K_0$ 上的压缩、$A_{21}$ 决定 $AD$ 的补分量），使读者可独立验证 $\dim(D+AD)=3$、$K_0\cap(D+AD)=D$、$c=2$、(5a) 成立 | 待做 |
| 5 | ④ Thm 6 缺 $W_0\subseteq T_D$ 前提 | 把 $W_0\subseteq T_D$ 与 $P_{K_0}(V_0)\subseteq D^{\perp_{K_0}}$ 写进定理假设；显式给出 $\dim\mathcal F_D^{\rm split}=(t-w_0)((n-k)-r(D)-t)$ | 待做 |
| 6 | ⑤ Thm 7 缺坐标同构 | 明确 $\iota_N:K_0^*\to\mathbb R^{1\times k}$、$\ell\mapsto\ell N$，所有行空间等式在 $\iota_N$ 下成立；把 $\Phi(W)=\{\phi_w\}$ 写成 $\Phi(W)=\phi(W)\le D^\circ$ | 待做 |
| 7 | ⑥ Thm 8 的商空间条件 | 补一条独立 Lemma：$f:X\to Y$ 线性、$Z\le\operatorname{im}f$ 时，$\exists S\le X$ 使 $f(S)=Z$、$\dim S=d$ 当且仅当 $\dim Z\le d\le\dim\ker f+\dim Z$；Thm 8 引用它 | 待做 |

## P2 算法正确性（必须）

| # | 专家条目 | 具体动作 | 状态 |
|---|---|---|---|
| 8 | ⑩ Claim 12 缺固定最高次项的显式论证 | 写出：取行/列指标 $I,J$ 使 $\det H_{I,J}\neq0$，则该子式的 $\lambda$-最高次系数 $=[\lambda^\omega]m_{I,J}=\det H_{I,J}\neq0$ 且与图卡参数 $s$ 无关，故 $\deg_\lambda m_{I,J}=\omega$ 在整张图卡上成立 | 待做 |
| 9 | ⑪ Claim 13 的 generic-gcd 等价需独立命题 | 新增 Lemma（specialization and generic gcd）：陈述参数多项式族、存在某成员在每点 $\deg_\lambda=d$、参数空间不可约、函数域、gcd 所在系数域、实点 Zariski 稠密、图卡分母非零点的处理；Claim 13 引用它 | 待做 |
| 10 | ⑫ Thm 14 的正确性需完整等价链 | 写三行等价链（$\exists$ 可行 split 设计 ⟺ $\exists D\in B_{\rm pres}\,\exists W$ 满足 $R_\lambda+\Phi(W)=D^\circ$ ⟺ $\exists\Phi\in\mathcal I_D$ ⟺ 算法返回可行），每步注明依据（Thm 6 / Thm 7–9 / Claim 12–13 + Thm 10） | 待做 |
| 11 | ⑫ 算法枚举的集合不明确 | 显式定义 $\mathcal I_D=\{\Phi\le V_\phi:\Phi_0\subseteq\Phi,\ \dim\Phi-\dim\Phi_0\le t-w_0\le\dim\ker\bar\phi+\dim\Phi-\dim\Phi_0\}$；算法枚举它的有限 chart cover；$\Phi=\{0\}$ 与 $\Phi=V_\phi$ 纳入统一规则 | 待做 |

## P3 复杂度（重要）

| # | 专家条目 | 具体动作 | 状态 |
|---|---|---|---|
| 12 | ⑭ 输入规模漏了 $L_0$ | 定义 $\tau=\max\{\text{bits}(A_{ij}),\text{bits}(C_{ij}),\text{bits}((L_0)_{ij})\}$ 或 $\mathcal L=\text{bitlength}(A,C,L_0)$；Thm 17 改为 $\operatorname{poly}(n,\mathcal L)$；同步 Claim 15、附录 A、摘要、引言、结论 | 待做 |
| 13 | ⑮ Claim 15 的高度传播需补细节 | 明确 $N$ 的整数化（清分母）、$P_{K_0}=N(N^{\top}N)^{-1}N^{\top}$ 要求 $N$ 满列秩、代数数域 $L_D$ 的表示与域运算复杂度、Step 9 用 Hadamard 界 $h(\det B)\le rH+O(r\log r)$ 代替概括估计 | 待做 |
| 14 | ⑮ 数域运算与 subresultant 的位复杂度 | 引用标准代数数域精确算法并给出输入规模参数，不能只凭 $[L_D:\mathbb Q]\le k^2$ 断言多项式时间 | 待做 |

## P4 学术表达（建议）

| # | 专家条目 | 具体动作 | 状态 |
|---|---|---|---|
| 15 | ⑧⑬ 术语统一 | 全文 "simple spectrum **over $\mathbb C$**"（不能简化为"实特征值互异"；$\chi_M=(x^2+1)(x^2+2)$ 也是简单谱）；realizability/realisability 统一 | 待做 |
| 16 | ⑨ Remark 7 更精确 | 改为"重复特征值**可能**产生正维不变平面族；其维数与几何取决于 Jordan 结构" | 待做 |
| 17 | ⑦ Thm 10 的复数分支 | 显式写出 $Mu=au-bw$、$Mw=bu+aw$，并指出 $D=\ker f(M)$（$f$ 为对应不可约二次因子），说明可在 $\mathbb Q$ 上表示 | 待做 |
| 18 | ⑯ 定位强调 | §I 突出 **image-space reduction** 而非"不变二维子空间分类"；贡献 3 措辞相应调整 | 待做 |
| 19 | ⑰⑱ 摘要/结论的 promise | 摘要改写为"Under the split condition, simple spectrum over $\mathbb C$, and fixed output dimension, the decision runs in polynomial bit complexity"，不暗示解决 unrestricted $c=2$ | 待做 |
| 20 | ⑲ Prop 11 的层次 | 明确区分：任意 $c$ 成立的结构结论 / 仅 $c=2$ 的有限枚举 / 仅简单谱的多项式算法 | 待做 |
| 21 | ㉑ 格式 | [1]–[3] 用可检索引用或标注 preprint；Thm 10/14/17 假设统一编号；"two-valued decision algorithm" → "exact yes/no decision algorithm"；引言解释 "two-dimensional compressed kernel" = 铅笔的 kernel deficiency $c=2$，不是压缩矩阵的核 | 待做 |

## 执行顺序

1. **P1（1–7）** → 编译 → 提交
2. **P2（8–11）** → 编译 → 提交
3. **P3（12–14）** → 编译 → 提交
4. **P4（15–21）** → 编译 → 提交

每批结束都要：三遍 `pdflatex`、0 error / 0 undef ref / 0 undef cite / 0 overfull、`audit_layout` 0 issue；页数不设上限（专家要求补证明，涨价可接受）。

## 专家判断的保留意见

- **不建议**继续扩到 $c\ge3$，先把 Thm 7 / Thm 8 / Claim 12 / Claim 13 / Thm 17 做成完全严密的链条。
- 专家认为 Claim 13 与 Thm 17 目前**不足以**支撑"已证明"的结论；修订时必须承认这两处的补强是实质性的，而不是排版。
