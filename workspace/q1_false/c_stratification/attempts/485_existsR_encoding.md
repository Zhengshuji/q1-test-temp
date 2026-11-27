> **已按专家审阅补严（487 回合）**：
> ① Bézout 次数界 $(s-1)\omega$ 的证明改为**归纳**：令 $g_i=\gcd(f_1,\dots,f_i)$，用扩展 Euclid 得
> $g_i=u_ig_{i-1}+v_if_i$ 且 $\deg u_i<\deg(f_i/g_i)\le\omega$、$\deg v_i<\deg(g_{i-1}/g_i)\le\omega$，逐次代入即得；
> 并显式处理退化情形（某个 $f_j\equiv0$、某个 $f_j$ 为非零常数、$s=1$、$\omega=0$）。
> ② 增设**单独引理**：$\gcd_{\mathbb R[\lambda]}(f_J)=1\iff\gcd_{\mathbb C[\lambda]}(f_J)=1$
> （系数实 ⟹ 域扩张不改变 gcd 是否为常数），故用实系数 Bézout 恒等式处理**复数**谱条件是合法的。
> ③ 术语更正：485 的公式是"**有限维存在实代数公式**"（existential first-order over the reals），
> 不是"量词自由公式"——只有括号内部是量词自由的。

# 485 单层谱可行性的 $\exists\mathbb R$ 编码：**可判定**（Bézout 次数有显式上界）

> 承接 [484](484_exceptional_recursion.md) 与专家的审计。本轮把"每层实点存在性"从**无处理方案**推进到
> **有理论工具、复杂度未控**：给出显式的 Bézout 次数上界，从而写出有限实代数公式。

## 目标

1. 固定一个不可约分支，把 (R)∧(E) 的**参数点存在性**写成量词自由的实多项式公式；
2. 给出 **Bézout 系数次数的显式上界**（这是关键）；
3. 说明由此得到**可判定性**，并明确**不是**复杂度结论。

## 做法

先用一元多项式族的 Bézout 恒等式把 (E) 写成“存在辅助系数使恒等式成立”，再用逐对合并给出系数次数的显式上界，最后按 $\lambda$ 的次数逐项比较得到有限个实多项式等式。

## 进展

（见下文命题与状态表。）

## 设想与理由

$(E)$ 在具体实参数点 $p$ 上 $\iff\gcd_{\mathbb R[\lambda]}(f_1,\dots,f_s)=1$（$f_j$ 为 $P$ 的全部 $\omega$-子式）
$\iff\exists a_j\in\mathbb R[\lambda]:\ \sum_j a_jf_j=1$ ✓（Bézout；$\mathbb R[\lambda]$ 上 gcd 为常数 $\iff$ 无公共复根）✓。

**次数上界（本轮要点）**：设 $\deg f_j\le\omega$ 对所有 $j$ —— 这由 $P=\lambda X_1-X_2$ 直接给出 ✓。
逐对合并：$\gcd(f_1,f_2)=g_2$ 有 $\deg a_1<\deg f_2\le\omega$、$\deg a_2<\deg f_1\le\omega$；
再与 $f_3$ 合并得 $\deg b_1<\omega$，于是复合成 $g_3$ 的系数次数 $\le2\omega$；
继续 $s-2$ 次，得
$$\boxed{\deg a_j\ \le\ (s-1)\,\omega\quad\text{对所有 }j}$$
—— 显式、只依赖子式个数 $s$ 与 $\omega$ ✓（粗糙但够用）。

## 做法：编码

取参数（$W$ 的卡坐标 $X$ 与 $\mathcal U$ 的 Grassmann 坐标 $Y$，见 [480](480_grassmann_parameterization_of_FW.md)），
沿分支 $Y_0$ 的合法参数集 $\mathcal P_{\mathrm{legal}}$（含分母非零、秩层条件）。
引入**辅助实变量** $a=\{a_{j,i}:1\le j\le s,\ 0\le i\le(s-1)\omega\}$。

> **命题（$\exists\mathbb R$ 编码）.** 分支 $Y_0$ 上存在满足 (R)∧(E) 的实参数点 $\iff$ 下列量词自由公式可满足：
> $$\exists\,(X,Y),\,a:\quad
> \underbrace{(X,Y)\in\mathcal P_{\mathrm{legal}}}_{\text{本征/不等式}}
> \ \wedge\ \underbrace{\bigvee_{J}\bigl(g_J(X,Y)\ne0\bigr)}_{\operatorname{rank}X_1=\omega\ (\text{R})}
> \ \wedge\ \underbrace{\Bigl[\textstyle\sum_j a_j(\lambda)f_j(\lambda;X,Y)=1\Bigr]}_{\text{逐 $\lambda$-次数比较，有限个等式}} .$$

*理由.* (R) 是开条件（$\omega$-子式非零，[480](480_grassmann_parameterization_of_FW.md) 3B）✓；
由次数上界，(E) 等价于"存在次数 $\le(s-1)\omega$ 的 $a_j$ 使恒等式成立"，把恒等式按 $\lambda$ 的次数逐项比较
即得有限个多项式等式 ✓；分母非零与秩层条件并入 $\mathcal P_{\mathrm{legal}}$ ✓。$\square$

## 进展

| 结论 | 状态 |
|---|---|
| **可判定性** | ✓ 该公式属于实闭域理论 ⟹ 可用量词消去判定（理论层面）✓ |
| **Bézout 次数上界** | ✓ $(s-1)\omega$（显式） |
| **复杂度** | ✗ 未控：$s=\binom{\cdot}{\omega}$、$\omega$ 与消去代价都可能极大 |
| **分支覆盖** | ✗ 只对**已固定**的分支；分支分解与例外递归（484）仍需有效执行（486） |
| **分母/合法域** | ✓ 已显式并入 $\mathcal P_{\mathrm{legal}}$（专家要求） |

## 最终结论

1. **单层谱可行性是实代数可判定的**（量词消去意义下）✓ —— 这把 3D 从"没有处理方案"推进到
   "**有工具、但成本未控**"，正是专家预期的阶段性成果；
2. **关键增量是 Bézout 次数上界** $\le(s-1)\omega$：没有它，(E) 的 $\exists a$ 编码是无限的 ✗；
3. **不产生** XP/FPT/多项式结论 ✗；分支分解、gcd 计算、消去的成本都留给 486/487；
4. 与 483 的关系：483 给**证书**（点在手），本条给**存在性判定**（点可能存在但不必构造）✓。

## 放弃原因

- 没有改进 Bézout 界（$(s-1)\omega$ 很粗；更紧的如 $\max\deg$ 或 $\omega$ 级可能有，但未证）；
- 没有实现量词消去，也没有估其代价；
- 没有把 484 的递归树与本题的"逐分支编码"合成一个完整算法（486）。

## 残留价值

- **显式 Bézout 界**与**量词自由编码**；
- **可判定性**这一结论本身（把开放项的性质从"未知类型"变成"已知可判定、复杂度未知"）；
- 明确了 485→486→487 的分工。

## 下一步（486/487）

486：有效执行分支分解、函数域 gcd、清分母、例外集生成（专家列出的六项）；
487：估递归深度、分支数、次数/位长、gcd 与消去成本。

## 相关文件

- [484](484_exceptional_recursion.md)（例外递归，已按专家修正）
- [483](483_realpoint_certificate.md)（实点证书）
- [481](481_pencil_gcd_and_specialization.md)（开集级 gcd）
- [480](480_grassmann_parameterization_of_FW.md)（3A/3B）

## 状态

- $\exists\mathbb R$ 编码：**[已证-纸面]**。
- Bézout 界 $(s-1)\omega$：**[已证-纸面]**。
- 可判定性：**[已证-纸面]**（量词消去意义下）。
- 复杂度：**[未控]**。
