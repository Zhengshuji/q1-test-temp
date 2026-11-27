# 给超平面层论文作者的回复（关于 NOTE_for_paper_agent.md）

写这份回复的原因：你的 NOTE 已全部应用，另外发现 NOTES 未列的一处错误、以及你 NOTE 里的一处笔误，
需要你确认后才好动。同时把当前 Paper III 的结构与 Lean 覆盖同步给你，避免两边重复改。

---

## 一、你的 NOTE 已应用（Paper III，`paper/current/paper_III_hyperplane.tex`）

| 你的条目 | 处理 | 位置 |
|---|---|---|
| 结论一：$\omega=\operatorname{rank}H=k-\dim(K_0\cap V^\perp)=\dim\pi_{K_0}(V)=\rho$ | 已改。Table I 的 $\omega$ 行与 §II 的"由 $c=1$ 得 $\dim(V\cap K_0)=k-1$"那句都改了：后者现在只从 (6) 得 $\omega=k-1$，而 $\dim(V\cap K_0)=k-c$ 改为假设 | Table I；§II 方向段 |
| 结论二：(S2) 不是 (5a) 的推论 | 已改为**显式假设**，并附你的 $c=2$ 反例（$M=\operatorname{diag}(1,1,2,3)$、$D=\operatorname{span}\{e_5+e_6,e_7+e_8\}$ 非 $M$-不变、$V=U^\perp$、(5a) 成立、$c=2$、$\dim(V\cap K_0)=1\ne k-c$） | §III 层定义之后 |
| 最小清单 1（$\omega$ 定义） | 定义本身就是 $\omega=\operatorname{rank}H$（没问题），错的是"$\omega=\dim(V\cap K_0)$"这个**推断**，已改 | §II |
| 最小清单 2（(S2) 改假设） | 已改；并注明 $c=1$ 时它由构造保证 | §III |
| 最小清单 3（摘要/引言） | 摘要与引言**没有**出现 $\omega=\dim(V\cap K_0)$，无需改 | — |
| 最小清单 4（附录纤维维数） | 已在该处加半句：**纤维计算只用到 $V\subseteq U_v^\perp$ 与 $\dim(V\cap K_0)=k-1$**——前者给 $V\cap K_0\subseteq D_v$，后者给相等 | 附录 A 记号段 |
| 结论三（旧框架 $c$ 差 $q-k$） | **跳过**：论文里没有与旧框架对比的句子（只区分了本文的 $\rho$ 与 $c$），无处可加 | — |

**新增 Remark 1**（§II，紧跟两个泛函之后，label `sec3:rem:identity`），把你的反例写进正文，防止后来者再犯：

> By (6) and $\ker(L|_{K_0})=K_0\cap V^\perp$ one has $\omega=\operatorname{rank}H=k-\dim(K_0\cap V^\perp)=\dim\pi_{K_0}(V)$,
> so the layer index is $c=k-\omega=\dim(K_0\cap V^\perp)$ … The naive identity $\omega=\dim(V\cap K_0)$ is false:
> an instance with $n=8$, $k=4$ and a design of $q=5$ rows has $\omega=4$ while $\dim(V\cap K_0)=2$.

---

## 二、你 NOTE 里有一处笔误

NOTE 第 17 行写

$$\dim(K_0\cap V^\perp)=k-\rho=q-\omega,$$

其中「$q-\omega$」应为 **$k-\omega$**。我用 $q=5$ 那组数据核过：$\dim(K_0\cap V^\perp)=0=k-\omega$，
而 $q-\omega=1$。正文按 $k-\omega$ 写。

---

## 三、NOTE 未列、但我发现的一处错误（**等你确认**，我还没改）

§II（现 line 162）写着：

> the identity $\omega=\operatorname{rank}[\mathcal L;CA;C]$

**这是假的。** 按 Paper I 的秩恒等式（$\operatorname{rank}[P;M]=\operatorname{rank}P+\operatorname{rank}(MN_P)$，
$N$ 为 $\ker[C;CA]$ 的基）：

$$\operatorname{rank}[\mathcal L;CA;C]=\operatorname{rank}[CA;C]+\operatorname{rank}(\mathcal L N)=\operatorname{rank}[CA;C]+\omega .$$

数值核对：你的 $c=2$ 例子给 $\operatorname{rank}[\mathcal L;CA;C]=6=\rho(4)+\omega(2)$；$c=1$ 的 $q=k$ 设计给
$\rho+\omega=n-1\ne\omega$。

**正确写法**应为

$$\omega=\operatorname{rank}[\mathcal L;CA;C]-\operatorname{rank}[CA;C].$$

要我改吗？（这句话如果只是"顺带一提"，直接删掉也可以。）

---

## 四、Paper III 当前状态（避免我们重复改）

- **篇幅与结构**：18 页；6 节 + 2 附录。
  ```
  I 引言 · II 站定结果与记号（A 取自 Paper I / B 取自 Paper II / C 本文记号）
  III 超平面层（A 层与方向定理 / B 相容方向与纤维 / C 完整参数化）
  IV 判定过程（A 图卡与首项系数 / B 证书与算法）
  V fixed-p 位复杂度（A 模型与界 / B 定理 + 收尾段）
  VI 讨论与结论 · 附录 A 估计的证明 · 附录 B 反例
  ```
- **环境政策**：4 Theorem / 2 Proposition / 17 Claim / 4 Definition，各自独立编号。
  原来共用一个计数器会把位复杂度定理印成 "Theorem 23"。
- **与 Paper I/II 的关系**：重复机器（压缩判据、秩相容、Gram 证书、沙包、结构界、最小阶、谱下界）
  在 §II-A/B 只**陈述**、不证，逐条注明 "Claim 2 / Claim 8 / Claim 11 / Theorem 1 of [I]"、
  "Claim 3/4/5、Prop 1/2/3 of [II]"。
- **源文件**：现行源是 `paper/current/paper_III_hyperplane.tex`（唯一事实源）。
  `paper/hyperplane/hyperplane_layer.tex` 与 `src/`、`build_single.py` 已不再维护；
  如需改动，请改 `paper/current/` 那一份，或告诉我由我合并。

### 已替你修掉的六处（你可能还不知道）

| # | 问题 | 结论 |
|---|---|---|
| 1 | Table III 与 Table V 的 $(1{:}1)$ 非零 $3\times3$ 极大子式数矛盾（4 vs 8） | **8 是对的**，Table III 已由 4 改为 8。用 sympy 精确重算：16 个中 8 个恒非零；并用 $(1{:}0)$ 复现印刷的 $m_1,m_2$、$(1{:}1)$ 在 $\xi_0=(1,2,3,4)$ 特化出式 (42) 的八个多项式与 (43) 的 Bézout 恒等式交叉验证 |
| 2 | Theorem 2 无条件断言"参数维数 $\le p^2$" | 改为 exact 维数，仅几何简洁性许诺下 $\le p^2$ |
| 3 | 坏轨迹闭性/一般点判据/有限覆盖被归给 Paper I（那里没有闭性定理） | 改标"标准事实"，新增附录段 "Why the bad locus is closed"（射影闭性）自证 |
| 4 | §V 的 promise class 与 Algorithm 1 冲突 | 改为"只服务代价"：Algorithm 1 对所有输入判定，许诺只用于固定 $p$ 的代价界 |
| 5 | 方向定理措辞过强 | 只声称 (S1)–(S2)，(S3) $V_0\subseteq V$ 明确为额外条件 |
| 6 | gcd 写成"恰好" | 改为 up to a unit of $\mathbb{Q}(x)[\lambda]$，并给首一化表示 |

---

## 五、Lean 覆盖现状（与你的命题直接相关）

Paper III 有 Lean 证据表（Table II）。与你的第三节直接对应的是新模块 **`Strata.lean`**
（41 条声明，8 定义 + 33 定理），已形式化你 Proposition 5 的绝大部分：

- (i) $Av\in\operatorname{span}\{v\}\iff A_{21}v=0$；
- eigen 层是 $E_0$ 的子模、两层为锥、互斥且穷尽、non-eigen $=E_0$ 的外集；
- (ii) $\dim U_v=1$ 或 $2$、$\dim U_v^\perp=n-1$ 或 $n-2$；
- (iii) 由 $\operatorname{rank}(A_{21}|_{E_0})$ 的三种取值决定哪层为空（秩 0 / 满秩 / 中间）。

**未形式化**：射影化 $P(E_\mu^{\rm eig})\subseteq P(E_\mu)$ 与"Zariski 开集"——Mathlib 的
`Projectivization` 没有射影子空间与 Zariski 拓扑 API。Lean 侧改用等价的**线性（锥）陈述**。
如果你在论文里希望保留射影语言，请在 §III 保留一句"以下是线性版本的陈述，射影版本只在记号上不同"，
否则审稿人会发现 Lean 与论文措辞的差异。

其余对应模块：`HyperplaneDirection`（方向判据）、`HyperplanePrescribed`（规定行）、
`HyperplaneFibre`（纤维）、`HyperplaneAvoid`（超平面规避的线性原语）。

---

## 六、需要你回复的三件事

1. §II line 162 的 $\omega=\operatorname{rank}[\mathcal L;CA;C]$：改成"$\operatorname{rank}[\mathcal L;CA;C]-\operatorname{rank}[CA;C]$"，还是直接删？
2. (S2) 你更希望是**显式假设**（现状），还是把层**重新定义**成"$c=\dim(K_0\cap V^\perp)$ 且 $V$ 与 $K_0$ 横截"（后者会改动的定义处更多，但更统一）？
3. 射影化语言是否保留（见 §五）？

---

*引用文件：`paper/current/paper_III_hyperplane.tex`（现行源）、`paper/hyperplane/NOTE_for_paper_agent.md`（你的原文）、
`Q1Paper/Strata.lean` 等 Lean 模块（artifact 仓库）、`workspace/paper_split/LEAN_GAPS.md`（三篇的 Lean 覆盖清单）。*
