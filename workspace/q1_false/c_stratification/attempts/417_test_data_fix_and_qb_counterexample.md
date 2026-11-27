# 417 测试数据的更正 + Q-B 的一个反例：纤维条件**不能**化为维数比较

> 本轮做了两件事，都有结论：
> **(1)** 发现 c411 的测试数据有两个 bug（无效的 $W$、被改动的实例），给出修正版（`c416`）；
> **(2)** 试了 Q-B 的一个自然猜想（"存在可行 $W$ ⟺ 铅笔最低秩与 $\dim\varphi(T_D)$ 的维数比较"），
> **给出反例**：该猜想假；并指出正确的约化形式（Schubert 规避，在 $\dim\le2p$ 的小 Grassmannian 里）。

## 目标

1. 修正 415 的实测数据；
2. 把 Q-B 从"猜想"推进到"已知为假的猜想 + 正确的表述"。

## 设想与理由

Q-B 的自然想法：铅笔行空间 $=R_\lambda+\Phi$（$R_\lambda=\row P_D(\lambda)\subseteq D^\circ$），
$(5b)\iff R_\lambda+\Phi=D^\circ\ \forall\lambda$。对**固定** $\lambda$，"$\Phi$ 与 $R_\lambda$ 横截"在
$\operatorname{Gr}(j,D^\circ)$ 里是开稠密的（维数够时非空），有限交仍非空 ⟹ 似乎只需维数比较：
$$\omega-\min_\lambda r_D(\lambda)\ \le\ \dim\Phi .$$
如果对，纤维就被完全消掉（只剩底空间枚举），$q1$ 的图景会大变。**但它是假的。**

## 做法

**(1)** 复核 c411 的每一行：检查 $W\subseteq T_D$（否则 $(5a)$ 失败）、精确核、以及"4242 变体只替换 $K_0$ 块"
（c411 错误地把 $A$ 的右上块也清零，改了 $A_{21}$）。

**(2)** 对四个实例算 $\omega$、$\min_\lambda\rank P_D(\lambda)$（在 $\omega$ 阶子式 gcd 的根上数值求秩）、
$\dim\varphi(T_D)$、$t$，与"枚举 $T_D$ 内所有候选 $W$ 得到的实际结论"对照。

## 进展

### (1) c411 的两个 bug 与修正数据（`c416`）

**Bug 1（致命）**：`cert` 用了固定的 $W=(0,0,1,1,0,\dots)$，但**没检查 $W\subseteq T_D$**。
对 $A_{21}\ne0$ 的实例该 $W$ 可能不在 $T_D$ 里 ⟹ $(5a)$ 失败 ⟹ 那是**无效设计**，
而脚本照样报了"gcd=0（可行）"。这正是项目纪律 21 说的那种错误（证书必须先断言基本不变量）。

**Bug 2**：c411 的"4242 变体"把 $A$ 的右上块（即 $A_{21}$ 的来源）也清零了，于是**实例本身被改了**，
与 c412/c413 的实例不可比。

**修正后的数据**（`c416`，$W$ 一律取在 $T_D$ 内，逐项断言 $(5a)$ 与精确核）：

| 实例 | $D$ | $r(D)$ | $\dim T_D$ | $\rank\varphi(T_D)$ | 候选 $W$ 的 gcd | 结论 |
|---|---|---|---|---|---|---|
| 块状 $M=\diag(1,2,3,4)$ | $\span\{e_1,e_2\}$ | 0 | 4 | 0 | 全 2 | 不可行 |
| 块状 $M=\diag(R,2,3)$（共轭对） | $\ker(M^2+I)$ | 0 | 4 | 0 | 全 2 | 不可行 |
| 块状 $M=\diag(1,1,1,2)$、$A_{12}$ 秩 1 | $\span\{e_1,e_3\}$ | 1 | 3 | **0** | 全 2 | 不可行 |
| 同上 | $\span\{e_2,e_3\}$ | 0 | 4 | 1 | $2,2,1,2,2,1,\dots$ | 不可行 |
| **4242 变体** $M=\diag(1,1,2,3)$ | $\span\{e_1{+}e_2,e_3\}$ | 1 | 3 | 1 | 含 **0** | **可行** |
| 4242 变体 | $\span\{e_1,e_2\}$ | 1 | 3 | 1 | $2,2,1$ | 不可行 |
| 4242 变体（$c=1$） | $\span\{e_1\}$ | 1 | 3 | 1 | 需 $t=0$（$W=0$），另有 3 处秩降 | 不可行 |

两条要点：

- **类 4 的"可行"是 bug**：修正后它不可行（$\rank\varphi(T_D)=0$ 时 $\Phi\equiv0$，铅笔就是 $D$ 部分；
  其 gcd 为 $(λ-1)(λ-2)$，正次数）。415 里那一行必须改；
- **同一 $D$ 下 gcd 次数随 $W$ 变（1 与 2 都出现）而"正性"不变**——与 402 的观察一致，再次印证
  "图卡判定只需正性"。

### (2) Q-B 的猜想及其反例

**猜想（假）**：固定 $D$ 时，存在 $t$ 维 $W$ 使 $(5b)$ 成立 $\iff$
$\omega-\min_\lambda r_D(\lambda)\le\min(t,\dim\varphi(T_D))$。

**反例（类 4b）**：$M=\diag(1,1,1,2)$、$A_{12}=uv^{\mathsf T}$、$D=\span\{e_2,e_3\}$。数据：
$\omega=2$、$\dim T_D=4$、$\rank\varphi(T_D)=1$、$t=1$、$\min_\lambda r_D(\lambda)=1$。
猜想给出 $1\le\min(1,1)=1$ ⟹ **预测可行**；但枚举 $T_D$ 内全部 10 个候选 $W$（4 个基向量 + 6 个两两组合），
**没有一个给出 gcd$=0$**（值只有 1 与 2）⟹ 实际**不可行**。

**失败原因**：$D^\circ$ 是 2 维、$R_\lambda$ 是其中的直线、而 $\Phi$ 只能取 $\varphi(T_D)$ 里那**唯一**一条非零直线。
"$\Phi$ 与 $R_\lambda$ 横截"的集合在 $\operatorname{Gr}(1,D^\circ)$ 里确实是开稠密的，但 $\Phi$ 的范围被
$\varphi(T_D)$ **钉死**；当那条直线恰好等于某个 $R_\lambda$（本例 $\lambda=2$）时，横截失败——
这是**闭条件**，维数比较看不见。

**正确的表述**（Q-B 的现状）：

$$\exists W\ (W_0\subseteq W\subseteq T_D,\ \dim W=t)\ \text{满足 }(5b)
\iff \exists\Phi\in\operatorname{Gr}(\le t,V_\varphi),\ \Phi\supseteq\Phi_0,\ \text{可实现的维数条件},\ 
\forall\lambda:\ R_\lambda+\Phi=D^\circ .$$

即"在**小** Grassmannian $\operatorname{Gr}(j,V_\varphi)$（$\dim V_\varphi\le n-k\le2p$）里找一个
避开有限多个 **Schubert 闭条件** $\{R_\lambda+\Phi\ne D^\circ\}$ 的点"。

- 相比原来的 $\exists W\in\operatorname{Gr}(t-w_0,T_D/W_0)$（$t$ 可到 $n$），这是**大幅缩小**（参数维数 $\le p^2$，与 $c$ 无关）；
- 但**不是**维数比较能替代的：一般需要 Schubert 规避的判定（实点问题仍在，靠 405 的判据）。

## 最终结论

1. **415 的数据要改两处**：类 4 的"可行"是无效 $W$ 造成的（改后不可行）；"4242 变体"必须只替换 $K_0$ 块；
2. **Q-B 的维数比较猜想为假**（类 4b 反例），失败的机制是"$\Phi$ 被 $\varphi(T_D)$ 钉死 + 横截是闭条件下失败"；
3. **Q-B 的正确形式**是"小 Grassmannian 里的 Schubert 规避"，参数空间 $\operatorname{Gr}(\le\min(t,2p),V_\varphi)$，
   维数 $\le p^2$——这仍是值得写的结构定理（"纤维被压到小空间里的 Schubert 问题"），
   但**不是**"纤维被消掉"；
4. 副产品：**gcd 次数随 $W$ 变、正性不变**再次被证实（类 4b 的 1/2 混现）。

## 放弃原因

- 没有判定"Schubert 规避在实点上的可判性"（要用 405 的判据 + 实 Schubert 簇的实点，可能不难，但本轮没做）；
- 没有把"$\min_\lambda r_D(\lambda)$"的精确计算写成算法（本轮用数值求根，只作检验）；
- 类 9 的 $t=0$（$W=0$）情形脚本没覆盖（候选列表里没有空集），应补。

## 残留价值

- **两个数据 bug 的更正**（含"证书必须先断言基本不变量"的教训实例）；
- **一个明确的反例**否掉了 Q-B 最自然的猜想，并说清失败机制；
- **Q-B 的正确表述**：Schubert 规避在小 Grassmannian 里，参数维数 $\le p^2$（与 $c$ 无关）；
- 类 4b 的 gcd 1/2 混现，再次支撑"只需正性"。

## 相关文件

- [attempts/415](415_test_suite_spec.md)（测试集规格与实测数据——本文件更正其两行）
- [attempts/416](../../decision_algorithms/attempts/416_dim_dual_annihilator_fix.md)（$\dim D^\circ=\omega$；铅笔受限于 $D^\circ$）
- [attempts/406](406_eliminate_W.md)（像约化）、[405](../../decision_algorithms/attempts/405_real_generic_point.md)（判据）
- 脚本：[c416](../../../../tools/verification/c416_fixed_test_data.py)（修正版数据）、
  [c413](../../../../tools/verification/c413_minrank_conjecture.py)（猜想检验）、
  [c414](../../../../tools/verification/c414_check_contradiction.py)（矛盾复核）
