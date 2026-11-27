# 结构化搜索第二个整族 Type III 实例（专家 §Step 2）

> **2026-11-04 更正（重要）**：本文的结论"未找到第二个整族 Type III"只对**筛选式**搜索成立。
> 随后的**反向构造**（`attempts/63`）在 86/86 个实例上于 $q_0+1$ 阶产生了**整族 Type III**，
> 并给出一个 $q_{\min}=4$、**阶差 2** 的显式实例（$q_0=2$ 为 Type I、$q=3$ 整族 Type III、$q=4$ 可行）。
> 教训：$arepsilon=0$ 在随机数据里罕见（0/6000），但**可系统构造**——筛选与构造不是一回事。

## 目标

按专家 2026-11-04 的 Step 2：先用 $\varepsilon=0$ 的**秩判据**（B.13d）定向，再搜"整族 Type III"的
第二个实例；随机采样不算数，必须按结构定向。

## 设想与理由

整族覆盖判据要成立，需要同时满足：

* $\varepsilon=0$（比例性在 $V$ 上恒成立）——现在可用 B.13d 的三情形**秩判据**直接判，不必算 Gröbner；
* **维数取等** $q_0-r=n-r_1-1$（这是覆盖判据唯一能成立的维数情形）；
* $(C,A)$ 可观测、$L_0$ 可观测（否则 $q_{\min}=\infty$）。

于是把搜索改成"先按这三条筛选，再对通过者做整族检验"，且必须把 Type I 与 Type III 区分开
（否则 $h=q+r_1$ 的计数失败会被误当成谱失败）。

## 做法

[structured_type3_search.py](../../../../tools/verification/structured_type3_search.py)：

1. 随机实例（$n\in\{6,7\}$、$p,r\in\{1,2\}$，要求可观测性）；
2. 用 B.13d 判 $\varepsilon=0$；
3. 要求维数取等；
4. 在 $q_0$ 阶枚举全部图卡 × 若干稠密 $\theta$，对每个 (5a)-可行候选算 (5b) 与 $h$，
   把候选分成 **可行 / Type I（$h\ge q+r_1$）/ Type III（$h<q+r_1$ 且失败）**。

## 进展

**（1）B.13d 已被精确验证**：`epsilon_zero_characterization.py` 在 **5983/5983** 个随机实例上，
"$q\equiv0$ on $V$" 与三情形判据完全一致，且覆盖了 $\operatorname{rank}U_0=0$（4 个）、$=1$（3492 个）、
$\ge2$（2487 个）。实现中先踩过一个错：把"$\operatorname{im}U_1\subseteq\operatorname{im}U_0$"写成了
**行**拼接（应在 $\mathbb C^r$ 里做**列**拼接），导致 2967 个假不一致；修正后全对。

**（2）结构化搜索（1500 次随机，129 秒）**：

| 阶段 | 计数 |
|---|---|
| 可观测实例 | 1495 |
| $\varepsilon=0$ | 750（几乎全是 $r=1$，此时 $\varepsilon=0$ 自动）|
| 且**维数取等** | 173 |
| 其中整族失败 | **173（全部是 Type I）** |
| 其中整族 Type III | **0** |

即：在"$\varepsilon=0$ + 维数取等"的筛选后，**所有整族失败都是计数型**，没有新的谱型整族反例。

**（3）聚焦搜索（C4 的参数 $n=6,p=2,r=2$）**：6000 次随机里，$\varepsilon=0$ 且可观测的实例数 **0**。
⟹ 在随机实例族里 $\varepsilon=0$ 极少见（$r=2$ 时尤其），C4 的 $\varepsilon=0$ 是**非一般**的巧合。

## 最终结论

1. $\varepsilon=0$ 现在有**纯秩判据**（B.13d），可用作搜索的定向条件；
2. **筛选式搜索找不到第二个整族 Type III**：命中"$\varepsilon=0$+取等"的实例整族失败都是 **Type I**；
3. 在 $n=6,p=2,r=2$ 的随机族里 $\varepsilon=0$ 本身几乎不出现 ⟹ **C4 依赖非一般的结构巧合**，
   与专家的判断（"这不是余维一现象"）一致；
4. 因此下一步应改为**按构造**生成实例：直接设计 $A$ 使 $(A-\alpha I)V\subseteq\ker L_0$ 而 $V\not\subseteq\ker(A-\alpha I)$
   （即 $U_1=\alpha U_0$ 但 $V$ 不是特征子空间），同时保持 $V=\ker[C;CA]$ 与可观测性——这是"反向设计"问题。

## 放弃原因

不适用（搜索完成，结论明确：筛选式搜索未找到第二例）。

## 残留价值

* B.13d 使 $\varepsilon=0$ 可判（秩判据），并提供 5983/5983 的验证；
* 两个定量事实：**整族失败在筛选后全是 Type I**；**随机族里 $\varepsilon=0$ 几乎不出现**；
* 明确指出下一步是"按构造生成"而不是"筛选"，并给出构造目标（$(A-\alpha I)V\subseteq\ker L_0$）。

## 相关文件

- `docs/02` B.13d（$\varepsilon=0$ 三情形刻画）
- `tools/verification/epsilon_zero_characterization.py`（5983/5983）
- `tools/verification/structured_type3_search.py`（结构化搜索）
- 专家答复：`workspace/for_expert/archive/12_research_direction-answer.md` §Step 2
