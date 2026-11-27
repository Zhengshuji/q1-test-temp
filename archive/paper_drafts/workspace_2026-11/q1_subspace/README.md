# 子空间（商）归约：从提案到完整纸面证明

> 2026-11-11 起，2026-11-13 收尾。来自对论文后续工作的一个提案：把自由行看作**有序向量组**
> 改为看作**子空间**，从而把参数从 $\kappa_{\rm obs}=rd$ 降到 $\ell=\operatorname{rank}(AN)\le k$。

## 0. 本目录的文件（按用途）

| 文件 | 用途 |
|---|---|
| [PAPER_MAP.md](PAPER_MAP.md) | **写论文时的检索表**：每条命题 → 证明位置 / Lean / 实验 / 文献 |
| [PROOF_fpt_ell.md](PROOF_fpt_ell.md) | **完整纸面证明**（引理 1–10），当前定稿 |
| [AUDIT_fpt_k.md](AUDIT_fpt_k.md) | $k$ 版审计的历史记录（结论已被 PROOF 取代） |
| 本文件 | 过程记录：哪些验证过、哪些是提案、专家往返的结论 |

## 1. 归约（已精确验证）

设 $M=[N\ AN]$（$n\times 2k$），$T=\operatorname{row}M$，$d=\dim T$，
$W_0=\operatorname{row}(L_0M)$，$s=\dim W_0$，$m=d-s$。对 $L=[L_0;R]$ 令
$B=LM=[H\ H_A]$，$W=\operatorname{row}B\subseteq\mathbb R^{2k}$。

**命题 1（沙包与可实现性）.** $W_0\subseteq W\subseteq T$ 且 $\dim(W/W_0)\le r$；
反之，任一满足这两条的子空间 $W$ 都可由某个自由行块实现（用 $W/W_0$ 的一组基在
$u\mapsto uM$ 下的原像作自由行，其余补零）。

**命题 2（条件只依赖 $W$）.** $(5a)\iff\pi_2(W)\subseteq\pi_1(W)$，
$(5b)\iff\dim\pi_\lambda(W)=\dim\pi_1(W)\ \forall\lambda$，其中
$\pi_1(h,g)=h$、$\pi_2(h,g)=g$、$\pi_\lambda(h,g)=\lambda h-g$。

**命题 3（结构界）.** 若 $W$ 可行且 $\omega=\dim\pi_1(W)>0$，则
$\omega+1\le\dim W\le2\omega$。

**命题 4（单调与饱和）.** 补零行使 $\mathrm{DEC}(q)\Rightarrow\mathrm{DEC}(q+1)$；
$r\ge m$ 时 $\mathrm{DEC}(r_0+r)=\mathrm{DEC}(r_0+m)$。因此
$\mathrm{MINDEC}(Q)=\mathrm{DEC}(Q)$。

## 2. 验证记录

- `tools/verification/c320_subspace_reduction.py`：12 个随机有理实例，6 个找到可行见证；
  对每个见证检查沙包、$\dim(W/W_0)\le r$、结构界、**从 $W$ 反解 $R$ 的往返**、补零单调性。
  **0 failure**（首轮 6 failure 是脚本自身的往返实现错——把 $W_0$ 的行也算成了自由行，
  修正为取商基后通过）。
- `tools/verification/c321_dimensional_test.py`：16 个 $(k,d,s,r)$ 组，未发现同组内可行与不可行并存。
  **但这是弱证据**：随机搜索找不到见证只是"没找到"，不是不可行的证明；组内重复也太少。

## 3. OPT 与 FIND 的 FPT 性：依赖链

**结论（条件性）**：$\mathrm{OPT},\mathrm{FIND}\in\mathrm{FPT}(k)$，条件是 $\mathrm{DEC}\in\mathrm{FPT}(k)$
（提案的 Theorem A）。链条是：

1. $q_{\min}=r_0+t_{\min}$（命题 1+2）：任何可行 $L$ 的 $W$ 可压缩到 $t=\dim(W/W_0)$ 行，
   而 $t\le m\le2k$；
2. 于是 OPT 只需对 $t=0,1,\dots,m$ 依次问"是否存在可行 $W$"——至多 $2k+1$ 次 DEC；
3. FIND：拿到可行 $W$ 的代数见证后，解 $uM=w$ 得自由行（命题 1 的构造），仍是 $f(k)\operatorname{poly}(\mathcal L)$。

**这个链条没有独立于 Theorem A 的内容**：OPT/FIND 的 FPT 性 $=$ DEC 的 FPT 性 $+$ 归约 $+$ 见证抽取。
所以"OPT/FIND 是否 FPT"与"Theorem A 是否成立"是同一个问题，不能分开解决。

## 4. 实验（c322）

`tools/verification/c322_opt_find.py`：36 个可行见证，全部压缩到自身的 $t$ 并**精确复核**
（$(5a)(5b)$），**0 failure**。各实例找到的最优阶与 $r_0+m$ 的关系符合预期
（例如 $n=5,p=2,r_0=2$ 时 $m=0$，最优阶恰为 $r_0$）。

注意：报告的是 $q_{\min}$ 的**上界**（来自显式见证），不是等号。

## 5. Lean（MyProof）

`MyProof/Q1Subspace.lean`（镜像在 `tools/lean/MyProof/`），`lake env lean` 通过，0 error：

- `range_eq_rowSpan`：行空间 $=$ 行映射 $u\mapsto uM$ 的像；
- `mem_rowSpan_iff_exists_vecMul`：**可实现性**（每个可取行对都有自由行原像）；
- `rowSpan_fromRows_left`：**沙包** $W_0\le W$。

尚未形式化：条件只依赖 $W$（需要 $\pi_\lambda$ 与谱条件）、单调性、$q_{\min}=r_0+t_{\min}$。
这三条需要把 $(5a)(5b)$ 的秩条件也搬进 Lean，工作量比上面三条大一个量级。

## 7. 边界案例（专家 89 号回复给的清单）

`tools/verification/c324_boundary_cases.py`，构造性检查，4/4 PASS：

| 案例 | 断言 | 结果 |
|---|---|---|
| $k=0$（$C=I_n$）| $T=0$，$W=0$ 对一切 $L$ 成立，可行性**不依赖 $R$** | 6 个随机自由行给出同一答案 |
| $m=0$（$W_0=T$）| 可容许的 $W$ 只有 $T$，可行性**不依赖 $R$** | 5 个随机自由行给出同一答案 |
| $W_0=0$、$\omega=0$ 分支 | $W=0$ 可行当且仅当 $W_0=0$，且由 $L_0$ 本身实现 | $L=L_0$ 可行 |
| 复公根铅笔 | $Q(\lambda)=\begin{bmatrix}\lambda&1\\-1&\lambda\end{bmatrix}$，$\det=\lambda^2+1$：实轴满秩、复根 $\pm i$ | gcd 判据必须拒绝，实轴采样会误判 |

第四例正是"不能用有限实 $\lambda$ 采样代替 $\forall\lambda$"的最小反例（对应 §10.1 的禁区条目）。

尚未覆盖的边界：$W_0=T$ 且 $r_0>0$、$s_0>2\omega$ 的剪枝、极大子式恒零、跨图的可行点。

## 8. 专家给的 Lean 优先序（第 1 条已完成）

1. ✅ **压缩恒等式**：`MyProof/Q1Compression.lean` 的 `finrank_range_prod`
   （抽象形式：$\dim\operatorname{range}(f\times g)=\dim\operatorname{range}f+\dim\operatorname{map}g(\ker f)$），
   已入**全图构建**（`lake build MyProof` = 9111 jobs，0 error），公理仅 `propext, Classical.choice, Quot.sound`。
   配套的 `range_restrictToKer` 同批完成。
   **矩阵形式未完成**（本轮试过，卡在两处搬运，已回退，树保持全绿）：
   `rank (fromRows J Q) = rank J + rank (Q*N)`，条件 `range (mulVecLin N) = ker (mulVecLin J)`。
   需要的搬运是 `sumElimEquiv : (m→K)×(q→K) ≃ₗ (m⊕q→K)`（`Sum.elim`），
   然后证 `map e (range (f.prod g)) = range (mulVecLin (fromRows J Q))`。
   **卡点**：(i) `rw [← LinearEquiv.finrank_map_eq …]` 之后 `congr 1` 得到的目标
   不是 `Submodule` 等式（`ext` 报 "No applicable extensionality theorem"），
   需要先看清 `congr` 产生的目标形状；(ii) 末步 `map g (ker f) = range (mulVecLin (Q*N))`
   的 `rw [hker, ← LinearMap.range_comp, ← Matrix.mulVecLin_mul]` 模式匹配不上，
   大概是 `g.comp N.mulVecLin` 与 `Q.mulVecLin ∘ₗ N.mulVecLin` 的定义性差异。
   下一轮从这两个目标打印开始（`set_option pp.all` 或直接 `guard_target`），不要再盲试。
2. 原秩条件 $\iff$ 两条投影条件；
3. 由 $(5a)$ 与 $\lambda=0$ 的谱条件得 $\pi_1(W)=\pi_2(W)$；
4. 结构维数不等式（含复特征值论证）；
5. 之后才是多项式 gcd 证书与 Cauchy–Binet 系数恒等式。

前四条是线性代数，远比形式化整个实代数判定程序便宜。

**同时入图**：`Q1Subspace.lean`（行空间 = 行映射的像、可实现性、沙包）原先只是单文件编译过、
不在构建图里，本轮一并加入 `scripts/in_build.txt` 与 `blocks.tsv`；五条声明登记进
`tools/lean/STATEMENT_MAP.md`（出处指向 89 号回复第 1 节），四道门全绿。

**踩坑**：给 `scripts/in_build.txt` 追加模块时不能用 `echo >>`（末行无换行会与最后一行粘连），
要用 Python 读入-重写；`printf "A\t..."` 经 PowerShell 传参后制表符会被破坏。

## 9. 尚未解决的部分（这才是 q1）

归约把问题变成：

> 在 $\mathrm{Gr}(t,m)$ 里找一个子空间 $W=W_0\oplus U$，使 $\lambda\pi_1-\pi_2$ 在 $W$ 上
> 对**所有** $\lambda\in\mathbb C$ 都满射。

等价地（取正交补）：$W^{\perp}\subseteq W_0^{\perp}$ 不含任何形如 $(\lambda\alpha,-\alpha)$、
$\alpha\ne0$ 的向量——即**避开一族由 $\lambda$ 参数化的子空间**。

这是"开集非空"型问题，仍然落在 $\exists\mathbb R$ 一侧。归约**降低了参数**（$k$ 而不是 $rd$，
且与 $r$ 无关），但**没有改变判定问题的性质**。

## 4. 下一步（按可行性排序）

1. **精确枚举小实例**：$k\le2$、$m\le2$ 时把 $\mathrm{Gr}(t,m)$ 用稠密有理点网格覆盖，穷举判定
   （而不是随机采样），得到可信的可行性表，看是否有组合规律。这一步能把 c321 的弱证据变成硬数据。
2. **Lean 形式化命题 1–3**：命题 1、2 是线性代数，可直接复用 `finrank_range_prod`；
   命题 3 需要投影的秩与 $\lambda=0$ 的谱条件。这是目前最便宜的一步，且能锁定归约的正确性。
3. **研究"避开谱簇"的结构**：$W^{\perp}$ 不含 $(\lambda\alpha,-\alpha)$ 是什么意思？
   把 $\alpha$ 视为 $U^*$ 的元素，$\lambda$ 变化给出 $\mathbb P^1$ 中的一条有理曲线（Veronese 型），
   问题是子空间与这条族的**相交性**。这条若能化成 rank 条件，就有希望。
4. **不要再用随机搜索当证据**：本项目的纪律是"构造或精确枚举"，随机采样对薄集必错过。

## 5. 与论文的关系

论文（`paper/current/`）按约定暂不改动。若上面第 1–3 步成立，论文的主定理会从
"$f(\kappa_{\rm obs})\operatorname{poly}(\mathcal L)$" 换成
"$f(k)\operatorname{poly}(\mathcal L)$，与 $r$ 无关"，并相应改写 §VI–§VII 与摘要。
