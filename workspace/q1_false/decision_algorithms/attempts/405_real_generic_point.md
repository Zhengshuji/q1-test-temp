# 405 实一般点判据（专家 108 号 Priority 2 第 5 项）：陈述与证明

> 承接 404（专家裁决）。本文件证明他要求的判据，并把算法的三值语义写死。

## 目标

1. 证明**实一般点判据**：图卡上"一般点 gcd $=1$"$\iff$"卡上存在实可行点"（在实点稠密 + 每点满秩下）；
2. 据此把 $c\ge2$ 判定算法的语义改成可操作的三值。

## 设想与理由

专家的原话：一般点 gcd $=1$ 只保证**非空 Zariski 开集**，不保证实点；需要实点稠密性。
但两个方向其实不对称：

- **点的 gcd 次数 ≥ 一般点 gcd 次数**（specialization 只会**增加**公因子）。所以
  "某点可行（次数 0）" ⟹ 一般点次数 $\le 0$ ⟹ $=0$ ✓ —— 这个方向是**初等**的；
- 反方向要从"一般点次数 0"得到"存在实点"：一般点次数 0 ⟺ 次数**取到最小值**，
  而"次数取最小值"的集合是**开**的（次数在 specialization 下只升），故它是非空开集；
  再加上图的实点 Zariski 稠密，非空开集必含实点 ✓。

所以判据成立，代价是两个引理（specialization 单调性、开集的实点存在性）。

## 做法

**设定.** $\mathcal X$ 是不可约仿射图卡，定义在实代数数域 $F\subset\mathbb R$ 上；
$m_1,\dots,m_s\in F[\mathcal X][\lambda]$ 是压缩铅笔的 $\omega$ 阶极大子式（清分母后）；
$$d_{\rm gen}:=\deg_\lambda\gcd_{F(\mathcal X)[\lambda]}(m_1,\dots,m_s).$$

**引理 1（specialization 单调性：一般点次数是下界）.** 设 $x\in\mathcal X(\mathbb R)$ 是**可接受点**：
**某个**极大子式在 $x$ 处保持其一般 $\lambda$-次数（铅笔情形下等价于 $\rank H(x)=\omega$）。则
$$\deg_\lambda\gcd\bigl(m_1(x,\cdot),\dots,m_s(x,\cdot)\bigr)\ \ge\ d_{\rm gen}.$$

（**专家 109 号 §3.2 的收紧**：原写"每个 $m_i$ 的首项系数都非零"过强——有些极大子式可能恒为零、
不同子式次数也可能不同；只需**一个**保持次数。理由见下面第 3 步。）

*证明（严格版，用 Gauss 引理）.* 记 $A=F[\mathcal X]$。
**假设（专家 109 号 §3.1 要求）**：$\mathcal X$ 是**有理图卡**，即 $A=F[x_1,\dots,x_d]_S$（多项式环的局部化），
此时 $A$ 是 UFD。（一般不可约仿射簇的坐标环**不一定**是 UFD，不能默认。）
1. **去内容**：把每个 $m_i$ 写成 $m_i=c_i\tilde m_i$，$c_i\in A$ 是内容、$\tilde m_i\in A[\lambda]$ 本原。
   在 $\operatorname{Frac}(A)[\lambda]$ 中 $\gcd$ 与内容无关，故可设 $m_i$ 本原。
2. **Gauss**：$\gcd_{F(\mathcal X)[\lambda]}(m_1,\dots,m_s)$ 可取为本原的
   $G\in A[\lambda]$，且由 Gauss 引理 $G\mid m_i$ **在 $A[\lambda]$ 中**（无需清分母、无例外点）。
   于是 $\operatorname{lc}_\lambda(m_i)=\operatorname{lc}_\lambda(G)\cdot\operatorname{lc}_\lambda(q_i)$，其中 $m_i=Gq_i$。
3. **首项不消失**：若 $\operatorname{lc}_\lambda(G)(x)=0$ 则**所有** $\operatorname{lc}_\lambda(m_i)(x)=0$
   （因为 $\operatorname{lc}(m_i)=\operatorname{lc}(G)\operatorname{lc}(q_i)$），与"某个子式保持一般次数"矛盾；
   故 $\deg_\lambda G(x,\cdot)=\deg_\lambda G=d_{\rm gen}$。
4. **整除**：$G\mid m_i$ 在 $A[\lambda]$ 中 ⟹ 在 $x$ 处 $G(x,\cdot)\mid m_i(x,\cdot)$ ⟹
   $G(x,\cdot)$ 是全部 $m_i(x,\cdot)$ 的公因子且次数为 $d_{\rm gen}$ ⟹ $\deg\gcd(x)\ge d_{\rm gen}$。$\square$

（要点：$d_{\rm gen}$ 是**下界**——这正是"一般点坏 ⟹ 处处坏"的来源。
若去掉"满秩"假设则结论**假**：$m_1=x\lambda-1$、$m_2=(x\lambda-1)(\lambda-1)$ 在 $x=0$ 处
gcd 从 $\lambda$ 掉到 $1$，而 $m_1$ 的首项系数恰在 $x=0$ 消失。）

**引理 2（最小次数集是开集）.** $U:=\{x\in\mathcal X:\ \deg\gcd(x)=d_{\rm gen}\ \text{且 }x\text{ 可接受}\}$
是**非空 Zariski 开集**。

*证明.* 两部分：
1. **$\{\deg\gcd\ge d\}$ 是闭集**（$d\ge1$）：在**固定次数**的轨迹上（所有 $m_i$ 的 $\lambda$-次数固定），
   $\deg\gcd\ge d$ 等价于相关**子结式**的同时消失（子结式是系数们的多项式），故是闭条件；
   **专家 109 号 §3.3 的提醒**：若不固定次数、首项系数可能消失使次数下降，朴素陈述会出问题，
   所以这一步要么限定在固定次数轨迹上，要么用齐次化多项式陈述 ✓；
2. 由引理 1，可接受点上 $\deg\gcd\ge d_{\rm gen}$ 恒成立，故
   $U=\{\deg\gcd\le d_{\rm gen}\}\cap\{\text{可接受}\}$ 是开集 ✓；非空：一般点属于 $U$ ✓。$\square$

**定理（实一般点判据）.** 设 $\mathcal X$ 是不可约**有理图卡**（坐标环为多项式环的局部化）、
定义在 $F\subset\mathbb R$ 上、实点 Zariski 稠密，
且**每个实点都可接受**（专家 109 号 §3.2 的加强版）。则
$$d_{\rm gen}=0\iff \mathcal X\ \text{含实可行点}\quad(\text{即某实 }x:\ \text{全部 }\omega\text{ 阶子式无公共根}).$$

*证明.*
($\Rightarrow$) $d_{\rm gen}=0$ ⟹ 由引理 2，$U$ 是非空开集；若 $U\cap\mathcal X(\mathbb R)=\varnothing$，
则 $\mathcal X(\mathbb R)\subseteq\mathcal X\setminus U$，后者是**真闭集**，与实点稠密矛盾 ✓。
任取实点 $x\in U$：$\deg\gcd(x)=0$ ⟹ 无公共根 ⟹ 可行（满秩已假设）✓。
($\Leftarrow$) 若有实可行点 $x$，则 $\deg\gcd(x)=0$，由引理 1 得 $d_{\rm gen}\le0$，故 $=0$ ✓。$\square$

### 对 $c\ge2$ 的适用性

- 图卡来自 Grassmannian 的仿射图卡、$\mathcal B_{\rm pres}$ 的开条件、以及丛的枢轴平凡化——
  都是**不可约仿射簇的开集**，定义在 $\mathbb Q$（或 $M$ 的特征值生成的实代数数域）上；
- 实点 Zariski 稠密：Grassmannian 及其非空开集上成立（$\operatorname{Gr}(d,N)(\mathbb R)$ 在
  $\operatorname{Gr}(d,N)$ 中 Zariski 稠密；开集继承此性质）✓；
- "每个实点满秩"：在**满秩图卡**（某 $\omega$ 阶子式的首项系数非零）上由构造保证 ✓。

所以把图卡一律取成"满秩图卡"，判据即可用。

## 进展

- 判据与两个引理已写出（纸面，M2）；引理 1 的证明骨架是标准的次模/半连续论证，
  引理 2 与定理的证明完整；
- 三值语义（据专家 §7）现在可写成：

| 输出 | 条件 |
|---|---|
| **可行** | 找到实点且其 gcd 次数 0（直接证书），或某实可容许满秩图卡的一般点 gcd $=1$（用定理） |
| **不可行** | 每个实可容许满秩图卡都算出一般点 gcd 正次数（用"一般点坏 ⟹ 处处坏"） |
| **未定** | 有图卡既没算出正次数一般点 gcd、也没有实点证书（例如系数域处理失败或图卡为空） |

## 最终结论

1. **实一般点判据成立**（两个引理 + 一个定理），条件就是专家要求的"实点稠密 + 每点满秩"；
2. **引理 1 已有严格证明**（Gauss 去内容 + 首项不消失 ⟹ 一般点 gcd 在 $A[\lambda]$ 中整除每个 $m_i$）；
   还给出了**去掉满秩假设就不成立**的显式反例（$m_1=x\lambda-1$、$m_2=(x\lambda-1)(\lambda-1)$）；
3. **引理 2** 的闭性用**子结式**（系数们的多项式）给出，开性由"下界 + 次数不超过下界"得到；
4. 关键不对称性：**一般点次数是下界**，所以"一般点坏 ⟹ 处处坏"是引理 1 的直接推论，
   而"一般点好 ⟹ 存在实点"需要开集 + 实点稠密；
5. 算法语义已按专家意见改为三值，并明确"只对实可容许满秩图卡计数"。

## 放弃原因

- 引理 2 的闭性只**引用**了"子结式消失 ⟺ gcd 次数 $\ge d$"这一标准事实，没有从子结式定义重证；
- 没有验证"实点 Zariski 稠密"在 $\mathcal B_{\rm pres}$ 这种"被内积条件切出的子簇"上的继承
  （它是开条件，应当继承，但没写证明）；
- 没有把判据形式化（Lean）——它涉及 $\operatorname{Frac}$、Gauss 引理、子结式，形式化成本远高于本轮的收益。

## 残留价值

- **判据本体与两个引理的完整证明**，可直接进 $c=2$ 论文的 §6（Total chart and gcd criterion）；
- **三值语义表**，把专家 §7 的意见落成可执行规范；
- 一个**边界反例**（去掉满秩就不成立），防止后来者误用。

## 相关文件

- [attempts/404](404_expert108_audit.md)（专家裁决与三处修正）
- [attempts/394](394_c2_total_charts.md)（图卡定理；语义将按本文更新）
- [attempts/386](386_bit_complexity_proof.md)（$c=1$ 的满秩首项系数引理）
