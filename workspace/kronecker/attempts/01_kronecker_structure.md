# Kronecker 结构：观测器诱导铅笔能有哪些型

> 方向：**结构**（Workstream B，专家 2026-11-02 指定的主方向）。既服务 "$q1$ = 假"（若有受限结构 ⟹ 判据）
> 也服务 "$q1$ = 真"（若结构足够自由 ⟹ 可编码）。
> 相关：[workspace/kronecker/README.md](../README.md)、[RESTRICTED_COMPLETION_MODEL.md](../../../proof/layer_program/RESTRICTED_COMPLETION_MODEL.md)。

## 目标

回答：**观测器诱导的铅笔 $Q_{\mathcal V}(\lambda)$ 能实现哪些 Kronecker 型？**
特别地，$(5b)$ 的型（无正则初等因子）是否在 $\mathfrak F_{\rho,c}$ 上可达；若有受限刻画，
是否像 Dodig 的行/列补全那样是**有限条关于不变量（次数、最小指标）的不等式**。

## 设想与理由

- $(5b)$ 已是 Kronecker 型条件（无正则初等因子；左右奇异块都允许）；
- Kronecker 型是**离散**不变量 ⟹ 型条件应是"不等式"而非"$\forall\exists$ 投影"；
- 但自由度是**子空间**（不是独立行）且有 $(5a)$ 与维数型等式 ⟹ 可达集是 Grassmannian 上的 constructible 子集，
  不能直接套 Dodig；
- 因此第一步是**先看清实际能出现什么型**，再谈刻画。

## 做法

1. `tools/verification/kronecker_pencil.py`：精确计算铅笔的 Kronecker 数据
   （normal rank；有限/无穷初等因子；左右最小指标——后者用"按次数截断的线性代数"，不碰多项式算术）；
2. `tools/verification/observer_pencils.py`：从 $(A,C,L_0)$ 与子空间 $\mathcal V$ **构造真实的观测器铅笔**
   （保证是观测器诱导的，而不是随便挑的铅笔），并做 $(5a)/(5b)$ 判定与交叉核对；
3. `tools/verification/kron_struct_scan.py`：按专家的五步程序扫描并输出 TSV。

## 进展

**已完成（2026-11-02）**：

- Kronecker 工具自检通过：$L_2$（右指标 2）、$L_1^{\mathsf T}$（左指标 1）、$J_2(0)$（有限初等因子）、
  $L_1\oplus0$（右指标 $[1,0]$）、常值可逆铅笔（无有限初等因子）、$\lambda I_2$（有有限初等因子，对照）；
- 观测器铅笔构造 + 交叉核对：$L=C$ 与 $L=[C;CA]$（已知可行）被判为 $(5b)$ 成立 ✓，
  且采样路径与 Kronecker 路径一致；
- 五步扫描（4 个实例、$n=6$）：候选族扩大为两族（$A$-不变 + 只满足 $(5a)$ 的模-$\mathcal J$ 不变），
  共 **42 个**铅笔；$(5b)$ 成立 **8 个，全在 $\rho=0$**；$(5a)$ 失败的候选被过滤（过滤前有 2 个 $\rho=1$ 的"可行"铅笔其实是非法候选）。

**观察（证据）**：

| 项 | 记录 |
|---|---|
| 只有右奇异块的可行铅笔 | 本样本 **0** 个 |
| 只有左奇异块的可行铅笔 | 本样本 **0** 个 |
| 可行铅笔的左最小指标 $\varepsilon$ | **非空**（典型 $[1,0]$）⟹ 旧说法"只含右奇异块"**错** ✓ |
| 固定 $\rho$ 下 | 本样本 $\rho\ge1$ 全不可行；$\rho=0$ 全可行 ⟹ 本样本还**没有**出现"同 $\rho$ 既有可行又有不可行" |
| 非法候选的教训 | 过滤前有 2 个 $\rho=1$ 的铅笔满足 $(5b)$ 但**违反 $(5a)$** ⟹ 必须先用 $(5a)$ 过滤 |

**新增（同一日，第二轮）**：

- [tools/verification/kron_known_instances.py](../../../tools/verification/kron_known_instances.py)：
  在**已知可行**实例（$n=6$、$(\rho,c)=(3,1)$）上看型 —— 可行铅笔 $\mathcal V=\langle e_1,e_2,e_3,e_5\rangle$
  的型为"5 个零不变因子 + 左指标 $[4]$ + 右指标 $[0]$"，**左最小指标很大**；
- 顺带修正：`observer_pencils` 的 normal-rank 断言现在会明确指出"这通常意味着 $(5a)$ 失败"——
  在 $L=[C;CA]$ 上它当场抓到了 $(5a)$ 失败（该 $L$ 在这个实例上不是候选）。

**新增（同一日，第三轮）**：

- [tools/verification/kron_sweep.py](../../../tools/verification/kron_sweep.py)：扫 12 个实例、59 个合法铅笔，
  找到 **4 个可行（$\rho\ge1$）** 铅笔：$(\rho,c)$ 覆盖 $(4,2)$、$(3,1)$、$(3,2)$；
  左最小指标为 $[5,1]$、$[4]$、$[4,1]$；
- **一条可证的观察**：$(5b)$ ⟹ 右最小指标**全为 $0$**（右零空间常值 ⟹ 可数常数基）⟹
  "受限结构"的非平凡部分**在左侧**（左最小指标 + 无穷初等因子）。这条不是猜想，是推论。

**撤回（2026-11-02，专家复核 §1）**：上一段那条"$(5b)$ ⟹ 右最小指标全为 0"是**错的**。
反例 $Q(\lambda)=\begin{pmatrix}\lambda&1\end{pmatrix}$：秩恒 1，右最小指标 $=1$（零空间随 $\lambda$ 变）。
已登记为 [proof/refuted R18](../../../proof/refuted/README.md)，证书脚本
[kron_identity_probe.py](../../../tools/verification/kron_identity_probe.py)。

**改正后的公式**（专家 §3）：$\sum\eta+\sum\varepsilon+\sum\deg\gamma_k=r$；$(5b)$ 型下为
$\sum\eta+\sum\varepsilon+d_\infty=r$（已在全部可行样本上核对 ✓）。

**新增（同一日，第四轮）：归一化问题已有答案**

[kron_layer_relation.py](../../../tools/verification/kron_layer_relation.py) 核对
$\operatorname{rank}Q_L=j+\operatorname{rank}Q_{\rm quot}$（17 个 $\lambda$ 全过），
但 Kronecker 数据不同（例如可行样本里 $\varepsilon=[4]$ 变成商铅笔的 $\eta=[3]$）⟹
**商化是压缩，不是等价**，不变量不能搬；结构陈述要在原始 $Q_L$ 上写。

**新增（第五轮）：可行样本扩到 101 个（$n=6,7,8$）**

- 加"可观性链"$L_k=[C;CA;\dots;CA^{k-1}]$ 作为**构造性**可行族（**已证-纸面**：$(5b)$ 总成立；
  见 README §4.7 的证明），sweep 得到 **101 个可行铅笔**，$(\rho,c)$ 覆盖 $(0,1)$ 到 $(5,2)$；
- **可行且右指标非零者：0 个** ⟹ 猜想 T4-a 在 101 个样本上未被推翻，但仍**不是证明**。

**新增（第六轮）：T4-a 已升级为定理；T4-b 有了定量猜想**

- **B.6**（[proof/kron_null_module](../../../proof/kron_null_module/README.md)）：$(5a)\Rightarrow$ 右最小指标全为 0
  —— [已证-纸面] + [精确验证 150/150]；
- [kron_dinfty_stats.py](../../../tools/verification/kron_dinfty_stats.py)：103 个可行铅笔上
  恒等式 103/103 ✓、$d_\infty=0\iff\operatorname{rank}L=h$ 103/103 ✓、B.6 103/103 ✓；
  且**全部满足 $d_\infty=h-\operatorname{rank}L$**（一般铅笔只有 $\ge$）⟹ **T4-b 猜想**：无穷部分全是 1 次因子；
- 由 B.6，$\sum\varepsilon=h-d_\infty$ ⟹ T4-c 与 T4-b **等价**，独立的猜想只剩 T4-b。

**新增（第七轮，专家优先级 5/6）**：

- [kron_t4b_search.py](../../../tools/verification/kron_t4b_search.py)：搜 $n=6,7,8,9,10$（每维 6 seed），
  **260 个合法铅笔、188 个可行**，T4-b 两种等价形式**全部成立**，**反例 0 个**；
- **B.6 的 Lean 内核**：[tools/lean/MyProof/KronCoeff.lean](../../../trash/lean_removed_2026-11-19/tools/lean/MyProof/KronCoeff.lean)
  （`RowContains` / `kron_coeff_chain_strong` / `kron_coeff_chain` / `kron_coeff_const` / `kron_coeff_mem_N`），
  `check_lean.sh` 51/51 OK，STATEMENT_MAP 144 声明 / 132 条 / 0 问题。

**新增（第八轮）：T4-b 已证 + 一个度量错误被更正**

- **T4-b 证明**：[proof/t4b_infinite_divisors/theorem.md](../../../proof/t4b_infinite_divisors/theorem.md)
  （六步：分解 $LA=XL+Y_1CA+Y_2C$ → 严格等价 → 反转铅笔 → 局部等价 → 行列式因子 → 不变因子）。
  **只用 $(5a)$，不需要 $(5b)$**；精确验证 **151/151**（$n=6..10$，含 43 个不可行）；
- **R20 更正**：$d_\infty$ 必须用反转铅笔不变因子在 $\mu=0$ 处的**阶**，不是多项式总次数。
  用总次数会得到一个度-2 不变因子 $\tfrac14-\mu+\mu^2$ 被误读成"2 次无穷因子"的假反例。
  `kronecker_pencil.py` 已加 `d_infinity` 字段（$\mu$-adic 赋值之和）。

**第九轮（专家第四封复核之后）**：

- **更正 R21**：左指标的和在 $(5a)$ 下是 $\sum\varepsilon=\operatorname{rank}L-d_{\rm fin}$，
  **不是** $\operatorname{rank}L$；只有 $(5a)+(5b)$ 时才是后者。已在 `verify.py` 里改成核对四条恒等式
  （151 个满足 $(5a)$ 的铅笔，含 43 个不可行，反例 0）；
- **两条新推论**：$d_{\rm fin}\le\operatorname{rank}L$；$(5a)+(5b)$ ⟹ $\operatorname{rank}L\le q+2p-h$
  （谱可行性必要条件）；
- **新方向（专家 §4）**：约化 descriptor 铅笔 $R(\lambda)=J D(\lambda)^{\mathsf T}=[\lambda E-EX^{\mathsf T}\ B]$，
  已证 **$R$ 的右最小指标 $=$ $Q_L$ 的左最小指标**（[proof/descriptor_reduction](../../../proof/descriptor_reduction/README.md)，
  66/66 验证）。左指标划分问题因此变成 descriptor 铅笔的右指标划分问题。

**第十轮（专家 §7 的优先级 4、5）**：

- **任务 4（文献对接）**：把 $Q_L$ 的左最小指标识别为 descriptor 系统 $(-E,-EX^{\mathsf T},B)$ 的
  **可控性指标**（SLICOT AG08BZ 文档：$[A-\lambda E\ B]$ 的右 Kronecker 指标即可控性指标，
  其引用为 Misra–Van Dooren–Varga, Automatica 1994）。记录：
  [literature/notes/DESCRIPTOR_CONTROLLABILITY_INDICES.md](../../../literature/notes/DESCRIPTOR_CONTROLLABILITY_INDICES.md)。
  标准情形（$E$ 可逆）我们给出严格等价 $R\sim[\lambda I-X^{\mathsf T},E^{-1}B]$ ⟹ 左指标 = $(X^{\mathsf T},E^{-1}B)$ 的可控性指标。
- **任务 5（划分的限制）**：
  * [partition_scan.py](../../../tools/verification/partition_scan.py)：203 个 $(5a)$ 铅笔（142 可行）上，
    $\#\varepsilon=s$、$\sum\varepsilon=r$ 全部成立；**没有** $r\le s$ 这种限制；
  * [partition_determinacy.py](../../../tools/verification/partition_determinacy.py)：140 个可行铅笔、35 个
    $(q,p,h,r)$ 组，**没有**发现同组两种划分（不能证明"划分由聚合数据决定"，只说样本内一致）；
  * **推翻专家的 $\operatorname{rank}L\le q+2p-h$**：反例 $n=6$、seed 1001、$q=6$、$r=6$、$s=2$、$\varepsilon=[5,1]$
    （单个左指标可以很大）。

**未做**：descriptor 可控性指标序列的完整可实现性刻画（需要读 Misra–Van Dooren–Varga 1994 原文）。

## 最终结论

待定。当前只有"工具 + 一份小样本的类型地图"，**不构成**结构定理。

## 放弃原因

（暂不适用）

## 残留价值

- 一套可复用的精确工具（Kronecker 数据 + 观测器铅笔构造 + 交叉核对），后续任何"型"的问题都能直接算；
- 一个明确的负面观察：**可行铅笔不是"只有右奇异块"**，纠正了项目早期（`attempts/09_pencil_completion.md` 开头）的
  表述——那条已被专家 2026-10-30 更正过，本实验独立确认；
- 五步扫描的 TSV 可直接作为"受限结构"猜想的原始数据。

## 相关文件

- [workspace/kronecker/README.md](../README.md)
- [proof/layer_program/RESTRICTED_COMPLETION_MODEL.md](../../../proof/layer_program/RESTRICTED_COMPLETION_MODEL.md)（RCP 模型、目标形式 T）
- [workspace/q1_false/attempts/09_pencil_completion.md](../../q1_false/attempts/09_pencil_completion.md)（F12 路线，提出未做）
- [literature/notes/DODIG_2008_row_completion.md](../../../literature/notes/DODIG_2008_row_completion.md)
- 工具：`tools/verification/kronecker_pencil.py`、`observer_pencils.py`、`kron_struct_scan.py`
