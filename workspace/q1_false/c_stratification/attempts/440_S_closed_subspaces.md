# 440 可行 $W$ 的代数身份：**$\mathcal S$-闭子空间**（图族 = 不变子空间，故可判）

> 承接 439（投影条件：图族 $\iff$ $B$-不变）。本轮把条件写成**对一般 $\mathcal S$ 的内蕴形式**，
> 并指出它的代数身份：**$\mathcal S$-闭子空间**。图族里它是"不变子空间"（多项式可判）；
> 一般 $\mathcal S$ 里它是"线性关系的不变子空间"——与铅笔的 Kronecker 理论同源，**很可能也可判**。
> 这对硬度是不利的证据。

## 目标

1. 把 $\pi_1(\mathcal T_W)=\pi_2(\mathcal T_W)=W$ 改写成对 $\mathcal S$ 内蕴的条件；
2. 认出它的代数身份；
3. 判断它的判定复杂度（对硬度是关键）。

## 设想与理由

$\pi_1(\mathcal T_W)=W$ 说的是：每个 $x\in W$ 都能配上某个 $y\in W$ 使 $(x,y)\in\mathcal S$。即
$$\forall x\in W\ \exists y\in W:\ (x,y)\in\mathcal S .$$
这正是"**$W$ 在关系 $\mathcal S$ 下封闭**"——记
$$\mathcal S(W):=\{y:(x,y)\in\mathcal S\ \text{对某个}\ x\in W\},$$
则条件是 $W\subseteq\pi_1(\mathcal T_W)$，配合维数相等即 $W=\pi_1(\mathcal T_W)$ ✓。对 $\pi_2$ 同理。
合起来：

> **命题.** 层 $\omega$ 在 $W$ 上可行 $\iff$ $W$ 是**$\mathcal S$-闭**的：
> $$\pi_1\bigl(\mathcal S\cap(W\oplus W)\bigr)=W=\pi_2\bigl(\mathcal S\cap(W\oplus W)\bigr).$$

## 做法

把 $\pi_1(\mathcal T_W)=W$ 改写成 $\forall x\in W\ \exists y\in W$ 的形式，再对三个族分别认出它的代数身份。

## 进展

| 族 | $\mathcal S$ | "$\mathcal S$-闭"是什么 | 判定 |
|---|---|---|---|
| 图族 | $\operatorname{graph}(B)$ | $BW\subseteq W$（**$B$-不变**） | **多项式**（有理标准形 / 不变子空间格） |
| 移位族 | $\mathbb Q^{1\times2k}$ | 恒真（全 $\operatorname{Gr}$） | 平凡 |
| 一般 $\mathcal S$ | 任意 $d_0$ 维子空间 | 线性关系 $\mathcal S$ 的**不变子空间** | 与**铅笔的 Kronecker 理论**同源，**很可能多项式** |

**图族的多项式判定（明确写出来）**：给定 $B$ 与固定张成 $U=\operatorname{span}\{h^0,g^0\}$，
存在 $B$-不变的 $\omega$-平面含 $U$ $\iff$ $U$ 的**不变包**
$$U+BU+B^2U+\cdots\ \ (\text{即 }U\text{ 生成的 }B\text{-循环包})$$
维数 $\le\omega$ 且可扩到 $\omega$ 维不变子空间——后者由 $B$ 的不变子空间格（有理标准形）决定 ✓。
两者都是多项式计算 ✓。

## 最终结论（对硬度）

1. **图族可判**（不变包 + 不变子空间格），移位族平凡 ⟹ 这两个族的中间层**多项式可判**；
2. 一般 $\mathcal S$ 的情形化归为"**线性关系的 $\omega$ 维不变子空间是否存在**"——
   这与 **matrix pencil 的 Kronecker 标准形**同源，而那套理论是**多项式**的；
3. 所以**中间层的可行性很可能也是多项式可判的** ⟹ 硬度在本架构上**仍无立足点**；
4. 若要救硬度，需要：**$\mathcal S$ 本身随输入变化、且不变子空间的判定被编码成难问题**——
   但"不变子空间存在性"是有强结构定理的（Kronecker/有理标准形），难以编码 NP-难内容。

## 放弃原因

- 没有把"线性关系的不变子空间"的判定写成完整算法（只指出与 Kronecker 理论同源）；
- 没有证明"一般 $\mathcal S$ 下 $\mathcal S$-闭子空间的存在性是多项式"——只是**很可能**；
- 没有处理固定行补一位的边界。

## 残留价值

- **把可行 $W$ 认成了 $\mathcal S$-闭子空间**（内蕴形式，与所选基无关）；
- 图族的**显式多项式判定**（不变包 + 不变子空间格）；
- 给硬度一个**明确的敌人**：若"$\mathcal S$-闭子空间存在性"是多项式的，硬度就彻底关闭。

## 下一步

1. 把一般 $\mathcal S$ 的"$\mathcal S$-闭子空间"判定写成算法（Kronecker 标准形 + 不变子空间格）；
2. 若成，则中间层全可判 ⟹ 层表可以恢复（但这次是**有证明**的版本）；
3. 若不成，找出它难在哪里——那才是硬度的真凭据。

## 相关文件

- [439](439_projection_shapes.md)（投影条件的形状）
- [438](438_sufficiency.md)（充分构造）
- [437](437_eval_map_criterion.md)（$E_\lambda$）
- [436](436_expert106_audit.md)（106 号裁决）

## 状态

- $\mathcal S$-闭的识别：**[已证-纸面]**。
- 图族多项式判定：**[已证-纸面]**。
- 一般 $\mathcal S$ 的复杂度：**[很可能多项式，未证]**。
