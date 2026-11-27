# 349 整条纤维全坏（证明，不是采样）：generic gcd 在纤维参数空间上 $\ne1$

> 承接 348（3/5 有证书，2/5 未找到好点）。本文件把 2/5 从"120 个候选全坏"升级为
> **整条纤维全坏**——在纤维的参数空间（$\mathbb P^2$）上算 generic gcd。

## 目标

对 348 的 seed 4245/4246，证明**纤维里每个点都坏**，而不是"采样没找到好点"。

## 设想与理由

固定核方向 $v$（非特征），纤维是
$$\{V\subseteq U^\perp:\ \dim V=q,\ \dim(V\cap K_0)=\omega\}.$$
本项目的模式里 $K_0\cap(U^\perp)$ 恰好 $\omega$ 维，故 $V=(K_0\cap U^\perp)\oplus\langle x\rangle$，
$x$ 跑遍商空间 $U^\perp/(K_0\cap U^\perp)$（3 维）⟹ **纤维 $\cong\mathbb P^2$，不可约**。

于是用 322/343 的判据：**纤维全坏 $\iff$ 该参数族上的 generic gcd $\ne1$**
（坏集闭 + $\mathbb P^2$ 不可约 ⟹ 若 generic 点坏，则处处坏）。

## 做法

把 $x=c_1x_1+c_2x_2+c_3x_3$ 的系数当符号，构造 $L(c)$、$H(c)$、$H_A(c)$，
在 $\mathbb Q(c_1,c_2,c_3)[\lambda]$ 上算 $\omega\times\omega$ 极大子式的 gcd。

## 进展

| seed | 非零子式 | generic gcd | 结论 |
|---|---|---|---|
| 4245 | 3 | $\lambda$ | **纤维全坏**（固定根 $\lambda=0$） |
| 4246 | 1 | $\lambda^3+4\lambda^2+2\lambda-5$ | **纤维全坏**（固定三次因子） |
| 4242 | 4 | $1$ | 纤维**生成好**（与 347 的证书一致） |

**4245 与 4246 的纤维被证明全坏**（不是"没找到好点"）。

**机制**（顺带核对）：4245 的 $\dim(AK_0)=4$、$v\in AK_0$；4246 的 $v\notin AK_0$、$\dim(AK_0)=4$。
所以 4246 的固定根**不是** $\lambda=0$ 那一档（Prop C 只管 $\lambda=0$），是另一类固定根障碍。

## 最终结论

> **重要更正（351 号轮）**：本文的"富余档 $\Rightarrow$ 可行 是错的（4245、4246 已证）"**只对纤维成立，对该实例不成立**。
> 4245 还有**无理**可容许方向（压缩的 $\mu=2\sqrt2$ 特征向量），其纤维 gcd $=1$ ⟹ **该实例其实可行**。
> 采样的 120 个候选全在 $v=e_1$ 的有理纤维里，系统性地漏掉了代数（无理）方向。
> 本文剩下的正确内容是：**纤维 $v=e_1$ 全坏**（generic gcd $=\lambda$ / 三次式），以及纤维判据本身。

1. **纤维全坏是纤维层面的结论**，不能推出实例不可行（实例还有别的 $v$）。
2. 与 Theorem 1 不矛盾：Theorem 1 说的是**无约束**高铅笔生成好；结构族的像可以整个落在坏簇里。
3. **判据的形状**：对每个核方向 $v$ 的纤维，算 $\mathbb P^{q}$ 参数族上的 generic gcd——
   但 $v$ 必须取**压缩矩阵的全部特征向量**（含无理的），见 [350](350_admissible_v_are_eigenvectors.md)。

## 放弃原因

- 只证了**单个 $v$ 的纤维**全坏；实例整体的可行性还要看其它 $v$（$B^\circ$ 是连续族）；
- 没有给出"哪些 $v$ 的纤维全坏"的判别式；
- 只做了 $n=8,p=2$ 一档。

## 残留价值

- 一个**可执行的纤维判据**：$\mathbb P^{r}$ 上的 generic gcd（$r=\dim U^\perp-\omega$）；
- 两个**已证**的"富余档但不可行"实例（4245、4246），推翻"富余档即可行"；
- 与 347 的证书侧配对：4242 有证书 ⟹ 生成好；4245/4246 gcd $\ne1$ ⟹ 纤维全坏。

## 相关文件

- [attempts/348](348_multi_instance_certificates.md)（多实例证书）
- [attempts/347](347_excess_generic_theorem_instance.md)（Theorem 1/2 与单实例证书）
- [attempts/322](322_hyperplane_determinism_components.md)（generic-gcd 判据）
- [attempts/343](343_stratified_cover_fix.md)（有限不可约覆盖）
- [c349](../../../../tools/verification/c349_fibre_all_bad.py)

## 状态

- 4245、4246 的纤维全坏：**[已证-纸面]**（generic gcd $\ne1$）+ **[精确验证]**（c349）。
- 实例整体不可行：**[未证]**（只证了单个 $v$ 的纤维）。
- 纤维判据：**[已证-纸面]**，可执行。
