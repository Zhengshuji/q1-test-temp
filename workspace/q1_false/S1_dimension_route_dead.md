# 负结果：S1 的可行性**不由** (rho, c, mu, nu) 决定

> 2026-10-29。脚本：[probe_s1_invariants.py](../../proof/rho1_layer/probe_s1_invariants.py)（精确算术，4000 次采样）。

## 结果

对满足 $(5a)$ 的随机 $L$（$n=5,6$），按 $(*)$ 辨识层号后统计：

$$(\rho,c,\mu,\nu)\ \longmapsto\ [\#\text{可行},\ \#\text{不可行}]$$

| $(\rho,c,\mu,\nu)$ | 可行 | 不可行 |
|---|---|---|
| $(3,1,0,0)$ | 0 | 3 |
| **$(3,1,1,0)$** | **354** | **160** |
| **$(3,1,1,1)$** | **58** | **15** |

其中 $(*)$：$\rho=\operatorname{rank}[\mathcal L;CA;C]-j$、$c=\dim(\mathcal L\cap\mathcal J)$、
$\mu=\dim(B\cap U)=\dim((\mathcal J A+\mathcal J)\cap(\mathcal V+\mathcal J))-j$、
$\nu=\dim\beta(H)=\dim(((\mathcal V\cap\mathcal J)A)+\mathcal J)-j$。

## 结论

$$\boxed{\ \text{同一组 } (\rho,c,\mu,\nu)\ \text{下既有可行又有不可行} \Longrightarrow \text{可行性不由这四个维数决定}\ }$$

- 这把 §22–§26 的错误（想用维数比较判定 S1）**从一条判据扩展到整类思路** ✗；
- 于是 S1 的判定**必须**保留 $\lambda$ 的量词结构（$=$ §17 的"某极大子式在 $\mathcal A$ 上不恒为零"，其中 $\mathcal A$ 与子式都依赖 $(\mathcal U,\mathcal H)$）；
- **路线重排**：S1 不再有"维数比较"捷径 ⟹ 要么攻 Q-C1（Grassmannian 上的 $\exists$ + 代数条件），要么走硬度（Löfberg gadget）。

## 教训

- 先用**同一不变量组合**分组再看是否两种结论都有（本脚本做法），能在写证明前否掉一整类判据 ✓；
- 与 2026-10-28 的 S1 反例同源：维数计数只给单向信息 ✗。

---

## 追加：更细的秩不变量也**不够**（2026-10-29 第二轮）

把签名加细到 $(\rho,\ \mu,\ \nu,\ \kappa)$（其中 $\kappa=\dim\ker\{(d\tau,d\lambda):d\lambda u_i=\beta(d\tau_i)\ \forall i\}$，
即定理 29.1 里 $E$ 的"零方向维数"），用**构造式**实例（[verify_29_1.py](../../proof/rho1_layer/verify_29_1.py)）分组：

| $(\rho,\mu,\nu,\kappa)$ | 全可行 | 全不可行 |
|---|---|---|
| $(2,1,1,0)$ | 24 | 24 |
| $(2,2,1,0)$ | 49 | 45 |
| $(3,2,2,0)$ | 13 | 5 |
| $(3,3,2,0)$ | 24 | 16 |

$$\boxed{\ \text{4 个组合\textbf{每一个}都同时出现可行与不可行} \Longrightarrow \text{秩型不变量都不决定可行性}\ }$$

**结论**：可行性依赖子空间的**方向几何**，不是任何有限秩签名能决定的 ✗。
这与"该问题是真正的代数几何判定问题"一致 ✓，也说明为什么 §22–§26 那类维数论证必然失败 ✗。

**剩下的只能是**：(a) 完整的 constructible 集非空性（可判定但复杂度未知 ✗），或 (b) 硬度归约 ✗。
