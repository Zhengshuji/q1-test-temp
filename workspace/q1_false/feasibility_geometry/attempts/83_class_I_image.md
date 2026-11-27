# B.18c：$p=r=1$ 的"坏像"落在 $\ker c$ 内；$d=1$ 的判据是**像的包含**

## 目标

把 Class I 的中间阶（$d\ge1$）判据化成"集合包含"形式，为"$q\le n-2$ 全不可行"的证明铺路。

## 设想与理由

$p=r=1$ 时对 $x\in V$ 有 $cx=0$、$cAx=0$，故
$$c(\lambda I-A)x=\lambda cx-cAx=0\quad\Longrightarrow\quad \operatorname{im}\psi:=\bigcup_\lambda(\lambda I-A)V\subseteq\ker c .$$
而 $K\subseteq\ker c$ 也是。于是"$d=1$ 的每个 $\mathcal Z=\langle z\rangle$ 都失败"就是"$K\setminus0\subseteq\operatorname{im}\psi$"。
维数：$\dim\ker c=n-1$、$\dim K=n-2$、$\dim\operatorname{im}\psi\le n-2$ ⟹ 两者维数相配，
所以这是"$K$ 是 $\operatorname{im}\psi$ 的一个不可约分支"这种**代数包含条件**。

## 做法

1. 证明三条（像落在 $\ker c$；$d=1$ 失败 $\iff z\in\operatorname{im}\psi$；全称化得包含判据）；
2. 在一个 $n=6$ 实例上取 12 个随机 $z\in K$，检查 $(5a)$、$(5b)$。

## 进展

| 量 | 结果 |
|---|---|
| 结构（1）（2）（3）| 已证（纸面）|
| $n=6$ 实例的 12 个候选 | $(5a)$ **12/12 成立**；$(5b)$ **12/12 失败** |
| 与"$K\subseteq\operatorname{im}\psi$"的一致性 | 一致 |

**实施陷阱（记录）**：判断 $z\in\operatorname{im}\psi$ 不能只在有理 $\lambda$ 上取样——坏 $\lambda$ 可为代数数。
本轮先用取样测试得到"$z\notin\operatorname{im}\psi$"的假象（与 $(5b)$ 失败矛盾），正是这个坑；
必须用消元/结式或对全部代数 $\lambda$ 判定。

## 最终结论

1. **B.18c 已证**：$p=r=1$ 的坏像整块落在 $\ker c$（维数 $n-1$）内，且 $d=1$ 的失败判据是 $z\in\operatorname{im}\psi$；
2. 于是 $d=1$ 的整族不可行 $\iff$ $K\subseteq\operatorname{im}\psi$，而两者维数相配（都是 $n-2$）⟹ 这是一个
   **"超平面 $K$ 是像的一个分支"** 的代数条件；
3. 这把 Class I 的"$q\le n-2$ 全不可行"猜想压成一个**具体的代数包含问题**；
4. 实施上必须避开"只在有理 $\lambda$ 取样"的坑。

## 放弃原因

不适用（判据已化归；包含条件的判定待做）。

## 残留价值

* **B.18c**：一条把 Class I 中间阶判据化为像-包含的结构定理；
* 明确了下一步的判定工具（结式/消元，而非取样）；
* 又一次记录了"坏 $\lambda$ 可为代数数"这个实施陷阱。

## 相关文件

- `docs/02` B.18、B.18b、B.18c、B.17
- `attempts/81`、`attempts/82`

## 补充（同日）：精确成员判据 + d=1 整族列联表

**精确判据**（`tools/verification/membership_test.py`）：$z\in\operatorname{im}\psi$ $\iff$ 增广铅笔
$[\lambda B_V-AB_V\mid z]$ 的 $(d_V+1)$ 阶子式的 gcd 有正次数（或有子式恒零）。
在 **229/229** 个 $(z,\mathcal Z=\langle z\rangle)$ 样本上，"$(5b)$ 失败 $\iff z\in\operatorname{im}\psi$" 完全成立
（此前用有理 $\lambda$ 取样给出假阴性，已由精确判据纠正）。

**d=1 的整族列联表**（240 个随机 $z\in K$）：

| 类别 | 计数 |
|---|---|
| 可容许 $\wedge$ $z\in\operatorname{im}\psi$ | **239** |
| 不可容许 $\wedge$ 成员 | 1 |
| **可容许 $\wedge$ 非成员** | **0** |

⟹ $d=1$（$q=n-2$）**没有可行候选**，与 B.18b（$q=n-1$ 必然可行）合起来给出
$$q_{\min}=n-1\quad(p=r=1,\ \text{本次 240 个样本})$$

**猜想（未证）**：$\operatorname{im}\psi=\ker c$（240/240 支持）。若成立，则 $K\subseteq\operatorname{im}\psi$ 自动成立，
$d=1$ 的整族不可行成为定理。
