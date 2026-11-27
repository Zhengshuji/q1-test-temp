# 487 复杂度审计：直接 $\exists\mathbb R$ 公式的规模；两条优先检查（一条成立、一条否定）

> 承接 [485](../../c_stratification/attempts/485_existsR_encoding.md)/[486](../../c_stratification/attempts/486_recursion_effectivity.md)。按专家建议，487 **不**宣布 XP/FPT，
> 而是做可复核的复杂度账本，并优先检查两件事：① Paper I 的左逆证书能否移植；② Bézout 证书能否压到 $\omega+1$ 个子式。

## 目标

1. 写出直接公式的显式规模（$N,M,d,\tau$）；
2. 检查 ①（Paper I 左逆证书移植）；
3. 检查 ②（小subset 引理）；
4. 明确这些结果**不**支持 $\omega$-FPT 结论。

## 做法

先按专家的四个任务写出公式规模的显式账本（变量数、等式数、次数、子式个数）；再逐条检查他指定的两个压缩路线（Paper I 左逆证书、小 subset 证书）。

## 进展

（见下文任务 1 与优先检查 ①②。）

## 设想与理由

$P(\lambda;z)=\lambda X_1(z)-X_2(z)$ 是 $u\times v$；$\omega$-子式个数
$$s=\binom{u}{\omega}\binom{v}{\omega},\qquad \deg_\lambda f_J\le\omega .$$
Bézout 系数次数界 $D=(s-1)\omega$（485，已按专家改成归纳证明）。

## 进展：任务 1（直接公式规模）

| 量 | 显式表达 |
|---|---|
| Bézout 辅助变量数 | $N_a=s(D+1)=s\bigl((s-1)\omega+1\bigr)=O(s^2\omega)$ |
| 总变量数 | $N_{\text{direct}}=N_z+N_a$（$N_z=\dim$ 卡参数） |
| Bézout 部分等式数 | $\le s\omega+1$（比较 $\lambda^0,\dots,\lambda^{s\omega}$） |
| 参数次数 | $d\le\omega+1$（若 $X_1,X_2$ 对 $z$ **仿射**；否则须先清分母再算） |
| 秩条件 | 析取 $\bigvee_I\det X_{1,I}\ne0$（$s$ 个非零条件，可保持析取） |

**关键观察**：$s=\binom{u}{\omega}\binom{v}{\omega}$ 随矩阵**尺寸**增长，即使 $\omega$ 固定 ✗ ⟹
**该编码不是 $\omega$-参数化的** ⟹ 不能由此推出 $\omega$-FPT ✗。

## 进展：优先检查 ①（Paper I 的左逆证书）

Paper I 的证书是**有界次数多项式左逆** $S(\lambda)(\lambda X-G)=I_\omega$，它要求铅笔在合法约束下可化为
**满列秩的方形（或带固定可逆块）** 形式。

**检查结果：不能直接移植** ✗。理由：$P=\lambda X_1-X_2$ 是 $u\times v$、只在每点秩 $\omega$；
要写成"某个 $\omega\times\omega$ 子式处处可逆"，需要一个**与 $\lambda$ 无关的主元（行+列）选择**——
而这正是 480 里 $Z_{Q,P}$ 的**析取**结构 ✗。逐点存在但整体未必有一个统一选择。

（若在某个分支上**存在**统一的主元选择，则证书可移植 ✓——但这是附加假设，不是一般情形。）

## 进展：优先检查 ②（小 subset 引理）——**成立**，但不构成净收益

> **引理（小证书）.** 若 $\gcd(f_1,\dots,f_s)=1$ 且 $\deg f_j\le\omega$，则存在**至多 $\omega+1$ 个**下标
> $J_1,\dots,J_t$ 使 $\gcd(f_{J_1},\dots,f_{J_t})=1$。

*证明.* 归纳：取 $g=f_1$（$\deg\le\omega$）。逐个加入 $f_i$，令 $g'=\gcd(g,f_i)$；
若 $g'=g$ 则该 $f_i$ 无用（跳过），若 $g'\ne g$ 则 $\deg g'<\deg g$（整除且真）。
每次**有效**加入令次数至少降 $1$，至多 $\omega$ 次 ⟹ 所需子集大小 $\le\omega+1$ ✓。$\square$

**但**：子集选择是**离散选择** ⟹ 编码变成对 $\binom{s}{\le\omega+1}$ 个子集的**析取** ✗。
于是

$$\text{每个析取支的变量数}\ \downarrow\ (\text{到 }(\omega+1)\cdot((\omega+1)\omega+1))\qquad
\text{析取支数}\ \uparrow\ \binom{s}{\le\omega+1}$$

$$ \boxed{\text{小证书把"很多变量"换成"很多析取支"——是 trade-off，不是净收益}}$$

**它的真实价值**：给出**稀疏可验证证书**（只检查 $\omega+1$ 个子式）✓ ——对**验证**有用，对**判定规模**无改善 ✗。

## 最终结论

1. **直接公式规模**已有显式账本；$N_a=O(s^2\omega)$，$s$ 随尺寸增长 ⟹ **不是 $\omega$-参数化** ✗；
2. **①否定**：Paper I 的左逆证书需要 $\lambda$-无关的统一主元选择，一般不存在（正是 480 的析取结构）✗；
3. **②成立**（小证书引理，$\le\omega+1$ 个多项式），但**牺牲析取支数** ⟹ 无净收益 ✗，只有验证价值 ✓；
4. 因此按专家的预设：**当前显式 Bézout 编码证明了 $\exists\mathbb R$ 可判定性，但不是仅由 $\omega$ 控制的参数化证书** ✓
   ——这是一个**否定性但有内容**的结论；
5. 术语按专家改：485 的公式叫"**有限维存在实代数公式**"（existential first-order over the reals），
   不是"量词自由公式"（括号内部才是量词自由）✓。

## 放弃原因

- 没有估 CAD 型量词消去的具体代价（只引"变量数双指数"这一保守基准）；
- 没有估递归树的总节点数（只写了框架）；
- 没有找到能真正压缩证书规模的新编码（①②都未成功）。

## 残留价值

- **可复核的复杂度账本**（$N_a,M,d,s$ 的显式表达）与"非 $\omega$-参数化"的结论；
- **小证书引理**（$\le\omega+1$）+ 它与析取的 trade-off；
- **①的否定**（左逆证书需统一主元选择）——这是一个明确的技术障碍，不是含糊的"未做"。

## 下一步

若继续：寻找**只在某个分支上有统一主元选择**的结构性条件（那是 ① 能成立的充分条件），
或研究能否用"稀疏证书 + 分支枚举"给出一个真正以 $\omega$ 为参数的上界。

## 相关文件

- [485](../../c_stratification/attempts/485_existsR_encoding.md)、[486](../../c_stratification/attempts/486_recursion_effectivity.md)
- [480](../../c_stratification/attempts/480_grassmann_parameterization_of_FW.md)（$Z_{Q,P}$ 的析取结构）
- [484](../../c_stratification/attempts/484_exceptional_recursion.md)

## 状态

- 任务 1（规模账本）：**[已写]**。
- ① 移植：**[已否定]**（需统一主元选择）。
- ② 小证书引理：**[已证-纸面]**，但无净收益。
- XP/FPT：**[未证，且当前编码不支持]**。
