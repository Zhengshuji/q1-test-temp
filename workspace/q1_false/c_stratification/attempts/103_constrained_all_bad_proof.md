# 约束区 $n=5$ 实例：$q=3,\omega=2$ 整层全坏的证明

> 2026-11-08。落实专家 49 号答复 §7 的 Priority C，把 attempts/100 里"200 个测试点全坏"的**猜想**变成定理。
> 工具：`tools/verification/constrained_all_bad_check.py`。状态：**M2**（纸面证明完整；待专家复核升 M3）。

## 目标

对 $n=5,p=1,q=3,r=1$ 的约束区实例，证明 $q=3,\omega=2$ 的**整个可容许层**全坏
（两个 Grassmann 点 $S_1,S_2$ 上的每一点，不只是抽到的 200 个）。

## 设想与理由

约束区（$\ker T\ne0$）的相容纤维被 $xZ_1+yZ_2=0$ 切小；逐点算 gcd 只能给采样证据。
要找的是**一整族共同掉秩的 $\lambda_0$**：若在某个 $\lambda_0$ 处，铅笔 $\lambda_0H-H_A$ 的所有行
都落进同一条线，则秩 $\le1<2=\omega$，该点必坏——且这个论证对参数**一致**成立。

## 做法

**实例**：$n=5$、$p=1$、$q=3$、$r=1$；$C=e_1^{\mathsf T}$；$A$ 的行 $1=e_5^{\mathsf T}$、
列 $2,3,4=e_3,e_2,e_5$；$L_0=e_4^{\mathsf T}$。
则 $K=\langle e_2,e_3,e_4\rangle$（$K$-坐标记为 $E_1,E_2,E_3$）、$\ker T$ 由 $(-e_3,e_2),(-e_2,e_3)$ 生成，
$$Z_1=\begin{pmatrix}0&-1\\-1&0\\0&0\end{pmatrix},\qquad
Z_2=\begin{pmatrix}1&0\\0&1\\0&0\end{pmatrix},\qquad E=L_0N_K=(0,0,1).$$
Grassmann 判据只给两个 $S$（$\sigma=(1,\pm1,0)$），其相容对为
$$S_1:\ x=(a,-a,b),\ y=(-a,a,d);\qquad S_2:\ x=(a,a,b),\ y=(a,a,d).$$
（验证 $xZ_1+yZ_2=0$：$S_1$ 给 $(a,-a)+(-a,a)=0$，$S_2$ 给 $(-a,-a)+(a,a)=0$。）

对每个 $S$ 取两个相容对 $(x,y),(x',y')$，$H=[E;x;x']$、$H_A=[0;y;y']$，$\operatorname{rank}H=2$，$y,y'\in S$ 故可容许。

## 进展

**定理**：$S_1$ 上每个可容许点都在 $\lambda=-1$ 处掉秩；$S_2$ 上每个可容许点都在 $\lambda=+1$ 处掉秩。
因此 $q=3,\omega=2$ 层全坏。

*证明*（$S_1$）：$P(\lambda)=\lambda H-H_A$ 的三行是
$$r_0=(\lambda E)= (0,0,\lambda),\quad
r_1=(\lambda+1)a\,(1,-1,0)+(0,0,\lambda b-d),\quad
r_2=(\lambda+1)a'\,(1,-1,0)+(0,0,\lambda b'-d').$$
在 $\lambda=-1$ 处 $r_1=(0,0,-b-d)$、$r_2=(0,0,-b'-d')$、$r_0=(0,0,-1)$，**全部落在 $\operatorname{span}\{E_3\}$ 里**
$\Rightarrow\operatorname{rank}P(-1)\le1<2$，故坏。$\square$

*证明*（$S_2$）：同理，三行是
$$r_0=(0,0,\lambda),\quad
r_1=(\lambda-1)a\,(1,1,0)+(0,0,\lambda b-d),\quad
r_2=(\lambda-1)a'\,(1,1,0)+(0,0,\lambda b'-d'),$$
在 $\lambda=+1$ 处全部落在 $\operatorname{span}\{E_3\}$ 里 $\Rightarrow$ 坏。$\square$

**机器核验**（`constrained_all_bad_check.py`，纯 `Fraction`）：
$S_1$ 的 394 个可容许参数点、$S_2$ 的 396 个可容许参数点，在各自的 $\lambda_0$ 处
$\operatorname{rank}(\lambda_0H-H_A)\le1$ **全部通过**。

**撤回：$q_{\min}=4$ 是错的**（专家 50 号答复 §4）。数据允许 $q=2$ 的增广
$$L=\begin{pmatrix}e_4^{\mathsf T}\\ e_5^{\mathsf T}\end{pmatrix},$$
它过七条一致性检查（$\operatorname{rank}[C;L]=3$、$\dim\ker=2$、$(5a)$ 成立、$h=3=$ 法秩、$(5b)$ 成立）；
而 $q=1$ 时 $L=L_0=e_4^{\mathsf T}$ 在 $\lambda=0$ 处秩 $2<3$，失败。故
$$\boxed{q_{\min}=2}$$
（$q=2$ 的 $\omega=1$ 层可行，与上面的 $\omega=2$ 层全坏并不矛盾。）

**为什么推论会错**：两条独立的错误——

1. **层 ≠ 阶**：整层全坏只排除 $q=3$ 的 $\omega=2$ 层；$q=3$ 的 $\omega=1$ 层、以及 $q=2$ 的 $\omega=1$ 层都可能有可行点。
   这正是 2026-11-07 已经记下的"重要降级"（坏层不推实例不可行），本轮**又踩了一次**；
2. **B.32(c) 不适用**：该实例 $(C,A)$ **不可观测**——$U=\langle e_1,e_4,e_5\rangle$ 是 $A$-不变
   （$e_1A=e_5$、$e_4A=0$、$e_5A=e_1$），$C=e_1\in U$，故 $\operatorname{rank}\mathcal O_C\le3<5$。
   上文写的"$e_1,e_5,e_4,e_3,e_2$ 张成 $\mathbb C^5$"是**错的**（$CA^3=e_4^{\mathsf T}A=0$）。
   B.32(c) 需要可观测性，不能引用。

## 最终结论

* 猜想 → **定理**：约束区这个 $n=5$ 实例的 $q=3,\omega=2$ 层全坏（无需采样）。
* 机制可复用：**若某个 $\lambda_0$ 使纤维内所有点的铅笔行都落在一条固定线里，则该层全坏**。
  这正是"刚性"机制的一般形状（与 48 号报告 $k=2$ 的 scaling 论证同型；这里是 $k=3,d=2$）。
* 与 attempts/100 的关系：那里的 200 点采样是**证据**，这里是**证明**；两者一致。
* **撤回**：$q_{\min}=4$（以及"B.32(c) 给出 4"）作废；正确值 $q_{\min}=2$（$L=[e_4;e_5]$，过七条检查）。

## 放弃原因

* 只做了 $q=3$ 的 $\omega=2$ 层；$q=2$ 的 $\omega=1$ 层是**可行**的（$L=[e_4;e_5]$），所以实例的 $q_{\min}=2$。
* 一般情形的"何时存在公共掉秩 $\lambda_0$"没有判据：这是约束区判据的下一步。

## 残留价值

* 一个完整的、可写进论文的小定理（$q=3$ 的 $\omega=2$ 层全坏），以及"公共 $\lambda_0$"这一可复用模板；
* 机器核验 790 个点；
* **反例价值**：$L=[e_4;e_5]$ 说明"整层全坏"绝不等于"该阶不可行"——这是 2026-11-07 降级的第二个实例，应写进论文的 caution。

## 相关文件

* [tools/verification/constrained_all_bad_check.py](../../../../tools/verification/constrained_all_bad_check.py)
* [workspace/q1_false/c_stratification/attempts/100_q_omega_plus_1_w2.md](100_q_omega_plus_1_w2.md)（200 点采样）
* [proof/B.32/README.md](../../../../proof/B.32/README.md)（B.32(c)：$q_{\min}=n-p$）
* [proof/B.24/README.md](../../../../proof/B.24/README.md)（块判据、专家第二十三轮）

## Lean

* 文件：WSL 树 `MyProof/LayerAllBad.lean`（Windows 备份 `tools/lean/MyProof/LayerAllBad.lean`）。
* 声明（`STATEMENT_MAP` 已登记）：
  * `LayerAllBad.rank_le_one_of_rows_zero` —— 3×3 矩阵若每行前两个坐标为 0，则 `Matrix.rank ≤ 1`；
  * `LayerAllBad.rowForm_rank_le` —— 只有第三列可非零的行形式，秩 ≤1。
* 验证：`lake build MyProof` **exit=0**（整图，9108 jobs）；单文件 `lake env lean MyProof/LayerAllBad.lean` 也 exit=0。
* 差异：Lean 只做**秩不等式**；从相容方程/参数化到"$\lambda_0$ 处三行都在 $\operatorname{span}\{E_3\}$"的推导由纸面 +
  `constrained_all_bad_check.py` 覆盖。故这是 **F2 内核**，不是字面 F3。
* WSL 侧改动：`scripts/blocks.tsv` 加 `B<TAB>LayerAllBad`、`scripts/in_build.txt` 加 `LayerAllBad`、`bash scripts/gen_blocks.sh`。

## 状态

* 定理：**[已证-纸面，M2]**；**Lean 内核 F2 已完成**（`LayerAllBad.lean`，整图 exit=0）；按 (M,F)→L：M2/F2 → L1，专家复核后 M3/F2 → L3。
* **$q_{\min}=4$ 已撤回**；正确值 $q_{\min}=2$（$L=[e_4;e_5]$，过七条检查；专家 50 号答复 §4）。
* 机器核验：$394+396$ 个可容许点全部通过；不构成证明。
* 与 50 号答复的对应：Priority C 的**层**定理成立；**阶**结论撤回。
