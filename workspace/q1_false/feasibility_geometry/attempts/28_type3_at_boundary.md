# 更大的随机实例里出现的 Type III：**都恰在 $r_1=p+r$**

## 目标

检验"一般实例在 $q_0$ 阶（谱区）总有可行解"的说法在更大规模（$n=7,8,9$、$p\\le3$、$r\\le3$）上是否成立，
并寻找新的 Type III 实例作对照。

## 设想与理由

上一轮（[attempts/27](27_bad_locus_blocking.md)）给出坏点像 $\\Phi$ 的阻断框架；
若阻断需要 $\\Phi$ 的像足够大，则维数上要求 $\\dim\\mathbb P(V)\\le\\dim\\mathbb P(K)$，即 $r_1\\le p+r$。
本档系统统计 $r_1$ 与 $p+r$ 的关系同可行性的关联。

## 做法

[search_type3_random.py](../../../../tools/verification/search_type3_random.py)：
$n\\in\\{7,8,9\\}$、$p\\in\\{2,3\\}$、$r\\in\\{1,2,3\\}$、6 个 seed；只保留**谱区**（整数障碍不适用）的实例，
在 $q_0$ 阶抽 40 个候选，判 $(5a)/(5b)$。

## 进展

**新发现的 3 个 Type III 实例**（有候选但全失败）：

| $n$ | $p$ | $r$ | seed | $q_0$ | $r_1$ | $p+r$ | $s_0$ | $t$ | 样本 |
|---|---|---|---|---|---|---|---|---|---|
| 7 | 2 | 2 | 4004 | 2 | 4 | 4 | 5 | 0 | 39 |
| 7 | 3 | 2 | 4001 | 2 | 5 | 5 | 6 | 0 | 38 |
| 8 | 3 | 2 | 4001 | 3 | 5 | 5 | 6 | 1 | 4 |

三个**全部**满足 $r_1=p+r$。其中前两个还有 $\\dim K=d$（$K=\\ker[C;L_0]$ 与 $\\mathcal Z$ 同维），
故**可行族只有一个点**——$(5b)$ 的判定可由该点精确给出。

**总体分组**（谱区实例，按 $r_1$ 与 $p+r$ 的关系）：

| 关系 | 实例数 | 可行 | 不可行（Type III） |
|---|---|---|---|
| $r_1<p+r$ | 12 | 12 | **0** |
| $r_1=p+r$ | 17 | 14 | **3** |
| $r_1>p+r$ | 8 | 8 | **0** |

## 最终结论

1. **观察**：在谱区、$q_0$ 阶，观察到的整族失败（Type III）**只出现在 $r_1=p+r$**（3/3；加上 C4 的 $r_1=p+r=4$，共 4/4）；
2. **但 $r_1=p+r$ 不是充分条件**：该类 17 个实例中 14 个仍可行；
3. **结构解释（部分）**：$r_1=p+r$ ⟺ $\\dim V=\\dim K$（$V=\\ker[C;CA]$、$K=\\ker[C;L_0]$），
   此时坏点映射 $\\Phi:\\mathbb P(V)\\to\\mathbb P(K)$ 是**同维**映射，才可能满射/阻断；
   若 $r_1\\ne p+r$，在本批数据里从未出现阻断；
4. **可判定的子类**：当 $\\dim K=d$ 时可行族退化为单点，$(5b)$ 由该点的极大子式 gcd 精确判定
   （新例 1、2 属此类）。

## 放弃原因

不适用。**未做**：$r_1=p+r$ 时判定"$\\Phi$ 是否阻断"的算法（仍缺）；以及 $r_1<p+r$ 时
"$\\Phi$ 为何总不满射"的结构解释。

## 残留价值

* 3 个新的 Type III 实例（其中 2 个可行族是单点，可精确判定）；
* 一个**强经验规律**：Type III 只在 $r_1=p+r$ 出现（4/4，含 C4）；
* 把"何时需要做谱判定"的范围缩小到边界情形 $r_1=p+r$。

## 相关文件

- [tools/verification/search_type3_random.py](../../../../tools/verification/search_type3_random.py)
- [workspace/q1_false/feasibility_geometry/attempts/27_bad_locus_blocking.md](27_bad_locus_blocking.md)
- [workspace/q1_false/feasibility_geometry/attempts/24_generic_no_type3.md](24_generic_no_type3.md)
- [proof/refuted/C4_type3_counterexample.md](../../../../proof/refuted/C4_type3_counterexample.md)
