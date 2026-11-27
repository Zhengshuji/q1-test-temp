# 逐图卡符号 gcd 分析：§8.1 的谱层做到"无网格"

## 目标

用 sympy 把 §8.1 的谱层做成**符号**判定：对每个图卡，算 $P_{\mathcal Z}(\lambda)=[(\lambda I-A)V\,|\,Z(\theta)]$ 的极大子式在
$\mathbb Q(\theta)[\lambda]$ 中的 **gcd**。于是

$$\deg_\lambda\gcd=0\ \Longrightarrow\ \text{一般 }\theta\ \text{下 }(5b)\ \text{成立};\qquad
\deg_\lambda\gcd\ge1\ \Longrightarrow\ \text{一般 }\theta\ \text{下 }(5b)\ \text{失败},$$

并给出**显式公共因子**（这就是掉秩的 $\lambda$ 族）。不需要网格。

## 设想与理由

此前"逐阶判定"依赖网格，专家 §8.1 指出网格不覆盖图卡。而 $(5b)$ 的失败等价于"极大子式有公共根"，
公共根的存在性在 $\mathbb Q(\theta)[\lambda]$ 里正是 **gcd 的次数**——符号可算、可复核、且对**所有** $\theta$ 一致
（除 gcd 表示式的分母零点，需单独检查）。

## 做法

[chart_gcd_analysis.py](../../../../tools/verification/chart_gcd_analysis.py)：

1. 逐图卡构造 $P(\lambda)$（$\mathbb Q[\theta,\lambda]$ 中的矩阵）；
2. 取全部极大子式（非零者）；
3. 在 `QQ.frac_field(θ)` 上求 gcd，报告 $\deg_\lambda$、公共因子、以及**分母**（例外 $\theta$）；
4. 判定：某图卡 $\deg=0$ ⟹ 该阶可行（可代入有理 $\theta$ 取见证）；全部图卡 $\deg\ge1$ ⟹ 一般位置下不可行。

## 进展

**C4 反例（$n=6,p=r=2$，$q_0=3$，两图卡、单参数）**

| 图卡 | 非零子式 | $\deg_\lambda\gcd$ | 公共因子 | 例外 $\theta$（分母）| 例外点上的 $\deg$ |
|---|---|---|---|---|---|
| $(0)$ | 4 | **2** | $\dfrac{4\lambda^2\theta-5\lambda^2-20\lambda\theta+22\lambda+28\theta-17}{4\theta-5}$ | $\theta=5/4$ | **1**（$\lambda-6$）|
| $(1)$ | 4 | **2** | $\dfrac{5\lambda^2\theta-4\lambda^2-22\lambda\theta+20\lambda+17\theta-28}{5\theta-4}$ | $\theta=4/5$ | **1**（$\lambda-6$）|

⟹ 两个图卡在**一般 $\theta$** 上 $\deg=2$、在两个例外点上是 $1$ ⟹ **所有 $\theta$ 都 $\deg\ge1$** ⟹
该阶 $(5b)$ **处处失败**。这是 C4 整族不可行的**第二种证明**（纯代数、机器可复核），
与原来的射影满射论证（[attempts/26](26_c4_proof.md)）独立。

**公开例子（$n=8,p=r=2$，$q=5$，四图卡、三参数）**

| 图卡 | 非零子式 | $\deg_\lambda\gcd$ |
|---|---|---|
| 全部 4 个 | 56 | **0** |

⟹ 一般 $\theta$ 下 $(5b)$ 成立 ⟹ $q=5$ 可行 ✓（与 $q_{\min}=5$ 一致）。

耗时：C4（2 图卡）+ 公开例子（4 图卡 × 56 子式）共约 **158 s**。

## 最终结论

1. **§8.1 的谱层有了符号判定**：逐图卡算 gcd 的 $\lambda$ 次数，**不用网格**；
2. **C4 的整族不可行有了第二个独立证明**（一般点 $\deg=2$ + 例外点 $\deg=1$）；
3. **公开例子 $q=5$ 的可行性**也由符号计算确认（四图卡 $\deg=0$）；
4. **残留的严谨性缺口**：$\deg=0$ 的图卡只证"一般 $\theta$ 可行"——需要显式代入有理 $\theta$ 并用七条一致性检查
   给出见证（下一步自动化）；$\deg\ge1$ 的图卡需检查全部分母零点（C4 已逐个查完）。

## 放弃原因

不适用（阶段性完成）。**未做**：把"见证代入 + 一致性检查"自动化；参数 $\ge4$ 的图卡（子式数与 gcd 成本上升）。

## 残留价值

* 一个**不依赖网格**的逐阶判定工具，且输出可人工复核（公共因子是显式多项式）；
* **C4 的第二种独立证明**（纯代数）；
* 性能基线（6 个图卡、56 子式/图卡、约 158 s），可判断哪些实例可做完整符号分析。

## 相关文件

- [tools/verification/chart_gcd_analysis.py](../../../../tools/verification/chart_gcd_analysis.py)
- [proof/refuted/C4_type3_counterexample.md](../../../../proof/refuted/C4_type3_counterexample.md)（已补第二种证明）
- [docs/08_results.md](../../../../docs/08_results.md) §4（结果汇总已引用）
- [workspace/q1_false/feasibility_geometry/attempts/40_sympy_elimination.md](40_sympy_elimination.md)（$(5a)$ 层的 sympy 消元）
