# 审计：arXiv:2609.37992 §VII 的数值例子

> 结论：该例子的 `4 ∉ Σ_FO(L)` 与 `ν_min = 5` **不成立**；正确值为 `Σ_FO(L) = {4,5,6}`、`ν_min = 4`。
> 精确有理/符号算术，见 [`tools/verification/c325_fer26b_example_audit.py`](../../../tools/verification/c325_fer26b_example_audit.py)。

## 1. 被审对象

| 项 | 内容 |
|---|---|
| 论文 | J. A. Fernando, *Complete characterization of minimum-order functional observers from Darouach to Luenberger*, arXiv:2609.37992 |
| 本地文件 | [`literature/papers/2609.37992.pdf`](../../../literature/papers/2609.37992.pdf) |
| 论文中的引用键 | 本项目论文的 `fer26b`（参考文献 [4]） |
| 被审位置 | **§VII "Illustrative Example"**，pp. 12–14，分 A–E 五小节 |
| 例子数据 | $n=8$、$p=\operatorname{rank}C=2$、$r=\operatorname{rank}L=2$、$B=e_1+e_8$；$q_0=3$、$n_0-p=6$，可能阶为 $\{3,4,5,6\}$ |
| 论文主张 | $3,4\notin\Sigma_{FO}(L)$、$5,6\in\Sigma_{FO}(L)$，故 $\nu_{\min}=5$。其中 §VII-B 明确写：在 $\mathrm{Gr}(2,4)$ 的六个图上精确检验条件 (S)，**没有任何分支满足**，故 $4\notin\Sigma_{FO}(L)$ |
| 论文条件 | 该文 (8a)–(8c)：$CZ=0$、$LZ=0$；$\operatorname{rank}[Z,\,AZR_Z]=d$，$\operatorname{im}R_Z=\ker(CAZ)$；$\operatorname{rank}[(\lambda I-A)V,\,Z]=\operatorname{rank}[V,\,Z]$ 对所有 $\lambda\in\mathbb C$，其中 $\operatorname{im}V=\ker[C;CA]$ |

## 2. 构造的反例（$q=4$）

取 $d=n-p-q=8-2-4=2$，候选零空间矩阵

$$Z_4=[\,j_*\;\,w_*\,],\qquad
j_*=\begin{pmatrix}390\\-97\\22\\-272\\419\\-58\\252\\-55\end{pmatrix},\quad
w_*=\begin{pmatrix}-369\\174\\403\\251\\-893\\368\\-501\\362\end{pmatrix}.$$

## 3. 验证结果（全部精确）

| 检查 | 结果 |
|---|---|
| $\operatorname{rank}Z_4=d$ | $=2$ ✅ |
| (8a) $CZ_4=0$、$LZ_4=0$ | 精确为零 ✅ |
| $\dim\ker[C;L]=4$；故 $\operatorname{im}Z_4=\ker[C;L]$ | ✅ |
| (8b) $\operatorname{rank}[Z_4,\ AZ_4R]=2$，$R$ 张成 $\ker(CAZ_4)=\operatorname{span}\{e_1\}$ | $=2$ ✅ |
| $\operatorname{im}V=\ker[C;CA]$（$V$ 为 8×4）、$\operatorname{rank}V=4$ | ✅ |
| $\operatorname{rank}[V\ Z_4]$ | $=5$ |
| 铅笔 $P_4(\lambda)=[(\lambda I-A)V\ Z_4]$ 的 28 个 $6\times6$ 极大子式 | **全部恒为零** ✅ |
| 非零 $5\times5$ 子式个数与 gcd | $336$ 个；$\gcd=4$（非零常数）✅ |
| 结论 | $\operatorname{rank}P_4(\lambda)=5=\operatorname{rank}[V\ Z_4]$ 对所有 $\lambda\in\mathbb C$，即 **(8c) 成立** ⟹ **$4\in\Sigma_{FO}(L)$** |

因此论文 §VII-B 的结论与定理 (8) 直接矛盾：$Z_4$ 满足该文自己的三个条件。

## 4. 误差出在哪

$Z_4$ 是 $\ker[C;L]$ 里的二维子空间，必然落在 $\mathrm{Gr}(2,4)$ 的六个标准图之一。所以出错的是 §VII-B 中
"在六个图上把条件 (A) 的完整族参数化出来"这一步——**参数化漏掉了分支**（很可能是条件 (A) 的解集在某个图上不止一个连通分支，
而按"单参数族"处理时只取了一支）。论文的定理 5/6/9 本身不受影响：它们说的是 $\exists Z$，而这里正好给出了一个 $Z$。

## 5. 副产物：$\sigma_1=3$ 的下界是对的

另一份推导用 $\mathcal J=\ker[C;CA;L]$、$D=LA|_{\mathcal J}$ 给出

$$\sigma_1=\dim\mathcal U-\dim\ker D=4-1=3,\qquad \nu_{\min}\ge\sigma_1+1=4 .$$

我们复算了 $q=4$ 这一例：$\dim\ker[C;CA]=4$ ✅、$\dim\ker[C;CA;L]=2$ ✅、$\operatorname{rank}(LA|_{\mathcal J})=1$ ✅，
故 $\sigma_1=3$ ✅。注意：那份推导里打印的基矩阵 $J$ **最后两行少乘了 151**（把 $151e_7,151e_8$ 也写进了 $1/151$ 的因子），
所以照抄会得到 $CJ\ne0$；用正确的基（把末两行还原为 $e_7,e_8$ 的比例）结论成立。

## 6. 对本文的影响

1. **不影响本文的任何定理**：本文引用 `fer26b` 是为"逐阶刻画的完备性"，不以该数值例子为依据。
2. **不影响本文 §I 的叙述**，但**不得引用该例子的数值**（若将来要举 $\nu_{\min}$ 的例子，必须用自己的构造）。
3. 本文 §I 说"逐阶过程本身不构成复杂度界"，这与本次发现方向一致：该过程不仅在复杂度上无界，**实现上也容易漏分支**。
   但论文里**不点破具体错误**（对在投/预印本作者不友好，且不属于本文的贡献范围）；如需说明，应写成
   "the chart-by-chart test is delicate to implement"。

## 7. 四阶观测器的显式参数：已验

[`tools/verification/c326_fer26b_order4_observer.py`](../../../tools/verification/c326_fer26b_order4_observer.py)
用精确有理算术复核了给定的一组参数（$L_4$ 4×8、$E$ 4×2、$F$ 4×4、$G$ 4×2、$H$ 4×1、$B=e_1+e_8$）：

| 检查 | 结果 |
|---|---|
| $L_4$ 的前两行等于 $L$ | ✅ |
| $\operatorname{rank}[C;L_4]=6$，$\dim\ker[C;L_4]=2$，$\operatorname{im}Z_4\subseteq\ker[C;L_4]$ | ✅ |
| $P=L_4-EC$ 满足 $PA-FP-GC=0$（**精确为 0**，非近似） | ✅ |
| $H=PB$（**精确相等**） | ✅ |
| $F$ 的特征多项式 $\lambda^4+\frac{45089}{8119}\lambda^3+\frac{113757}{8119}\lambda^2+\frac{138461}{8119}\lambda+\frac{62854}{8119}$ | ✅ |
| 精确 Routh–Hurwitz：$a_3a_2-a_1=\frac{4005024514}{65918161}>0$、$a_3a_2a_1-a_1^2-a_3^2a_0=\frac{426756390826420}{535189549159}>0$，其余系数为正 | ✅ |

误差动力学：$e=w-Px$ 给出 $\dot e=Fe$（由上面两式直接推出），$F$ Hurwitz 故
$\|\hat z_{\mathrm{aug}}-L_4x\|\to0$，取其前两行即 $\|\hat z-Lx\|\to0$。
**四阶稳定功能观测器确实存在。**

## 8. 状态

| 项 | 状态 |
|---|---|
| 该例子 $\nu_{\min}=5$ 的错误 | **已精确验证为错误**（符号算术，无采样） |
| 四阶零空间矩阵 $Z_4$ 满足该文 (8a)–(8c) | **已验证**（`c325`） |
| 四阶稳定观测器的显式参数 | **已验证**（`c326`） |
| 该文定理 5/6/9 | 未受影响（本次只涉及例子；定理说的是 $\exists Z$，而这里正给出了一个） |
| 该例子正确的阶谱 | $\Sigma_{FO}(L)=\{4,5,6\}$，$\nu_{\min}=4$ |
| 是否通知原作者 | 待定（对外沟通，需用户决定） |

## 9. 用本文自己的判据直接判定（最重要的一条）

[`tools/verification/c328_example_direct_dec.py`](../../../tools/verification/c328_example_direct_dec.py)
不用该文的 (8a)–(8c)、不用 $Z$、不做图枚举，只取四行观测矩阵 $L=[L_0;R]$（$q=4$，前两行即 $L_0$），
直接检验本项目的两条判据：

| 判据 | 结果 |
|---|---|
| $(5a)$ $\operatorname{rank}[LA;L;CA;C]=\operatorname{rank}[L;CA;C]$ | $7=7$ ✅ |
| $(5b)$ 铅笔 $[\lambda L-LA;\,CA;\,C]$（$8\times8$）的 64 个 $7\times7$ 极大子式 | 全部非零，$\gcd=1$（无公共复根）✅ |
| 更大的子式 | 全部为零，故秩恒为 $7$ ✅ |

**结论：$\mathrm{DEC}(4)$ 接受该实例，故 $q_{\min}\le4$。** 该文报 $\nu_{\min}=5$，因此该数值**确定有误**
（$q_{\min}\le4\ne5$，无需再判 $q=3$ 即可定案）。若要把 $q_{\min}\le4$ 升级为 $=4$，需再证
$\mathrm{DEC}(3)$ 拒绝，即 $t=1$（$\mathrm{Gr}(1,m')$ 上的一参数族）不可行；尚未做，且不影响
"原文 $=5$ 有误"这一结论。
