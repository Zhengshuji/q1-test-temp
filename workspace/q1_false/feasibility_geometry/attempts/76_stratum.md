# 分层判据（B.16）：按 s = dim(V∩Z) = 按 rank(J_Z|_V) 分层

## 目标

专家 2026-11-04 §9 把"按 $\operatorname{rank}(J_{\mathcal Z}|_V)$ 分层、逐层给出谱判据"列为最有前途的新方向。
本轮做它的第一步：把三层判据写成定理并把"顶层永远可行"这一结论取出来。

## 设想与理由

$J_{\mathcal Z}:V\to X/\mathcal Z$ 的核恰好是 $V\cap\mathcal Z=:S$，故
$$\operatorname{rank}(J_{\mathcal Z}|_V)=\dim V-\dim S,$$
按 $s=\dim S$ 分层就是按秩分层，而 $s$ 正是我们编码（G.1/G.2）里那个 $O(n)$ 项析取的参数——两种做法在此汇合。
逐层把 B.13c 的判据（$\exists x\in V\setminus\mathcal Z,\lambda:(\lambda I-A)x\in\mathcal Z$）写成
"铅笔 $N_{\mathcal Z}(\lambda)=T_{\mathcal Z}-\lambda J_{\mathcal Z}$ 的核是否跑出 $S$"。

## 做法

1. 证明三层判据（B.16）：(a) $s=\dim V$ 可行；(b) $s=0$ 时失败 $\iff$ 铅笔有有限零点；(c) 一般情形的核判据；
2. 核验 $s=0$ 层：在随机可容许 $(\mathcal Z,q)$ 上比较"极大子式 gcd 有正次数"与 B.12 可观性判据。

## 进展

**定理（B.16）**：

| 层 | 判据 |
|---|---|
| $s=\dim V$（$V\subseteq\mathcal Z$）| **谱可行**（$V\setminus\mathcal Z=\varnothing$）|
| $s=0$ | 失败 $\iff\exists\lambda:\operatorname{rank}N_{\mathcal Z}(\lambda)<\dim V$ $\iff$ gcd 有正次数 |
| $0<s<\dim V$ | 失败 $\iff\exists\lambda:\ker N_{\mathcal Z}(\lambda)\not\subseteq S$ |

**核验**：$s=0$ 层上 **402/402** 一致（`stratum_criterion.py`）。
（该脚本用符号 gcd，规模收缩到 40 个实例才有 402 个样本；全量会超时——已记录。）

## 最终结论

1. **分层判据已证**，且与我们编码里的 $s$-析取是同一个分层（两种做法汇合）；
2. **顶层永远可行**：任何 $\mathcal Z\supseteq V$（合法时）谱可行 ⟹ **整族不可行只能发生在 $s<\dim V$ 的层**；
3. $s=0$ 层判据最干净：单射性自动给出 $x\notin\mathcal Z$，故只需"铅笔有有限零点"；
4. 这把"整族不可行"的分析变成"逐层分析"，是走向**分类**（而非两个例子）的第一步。

## 放弃原因

不适用（第一步完成；逐层的完整分类是后续工作）。

## 残留价值

* **B.16** 三层判据 + "顶层可行"这一结构性事实（可用于排除"整族不可行"的某些维数区间）；
* 分层与编码中 $s$-析取的对应（统一了两条线索）；
* $s=0$ 层的 402/402 核验与脚本。

## 相关文件

- `docs/02` B.16、B.13c、B.13e、B.14
- `tools/verification/stratum_criterion.py`
- 专家答复：`workspace/for_expert/archive/14_proofs_and_direction-answer.md` §9
