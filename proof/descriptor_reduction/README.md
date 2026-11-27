# descriptor_reduction —— 左指标 = 约化 descriptor 铅笔的右指标

> **对应 docs 条目**：B.6（见 [docs/02](../../docs/02_theorems_proven.md) §0.1 归并表）

## 陈述

设 $(A,C,L)$ 满足 $(5a)$，$H=[L;CA;C]$，$h=\operatorname{rank}H$，$LA=XL+Y_1CA+Y_2C$，
$D(\lambda)=\operatorname{diag}(\lambda I_q-X,I_p,I_p)$，$J$ 满行秩且 $\ker J=\ker H^{\mathsf T}$。则

$$R(\lambda):=J D(\lambda)^{\mathsf T}=[\lambda E-E X^{\mathsf T}\ \ B],\qquad E=J_1,\ B=[J_2\ J_3]$$

满足

1. $\operatorname{rank}E=\operatorname{rank}L$、$[E\ B]$ 满行秩 $h$；
2. **$R$ 的右最小指标 $=$ $Q_L$ 的左最小指标**。

## 状态

**[已证-纸面]**（[theorem.md](theorem.md)）+ **[Lean 内核]**（`KronFactor.descriptor_ker`：$\ker J=\ker H\Rightarrow\ker(J\circ D)=\ker(H\circ D)$；**差异**：矩阵实例化与 $D$ 依赖 $\lambda$ 的版本未形式化）+ **[精确验证 66/66]**（[verify.py](verify.py)，$n=6,7,8$）。

## 文件

| 文件 | 内容 |
|---|---|
| [theorem.md](theorem.md) | 构造 + 等价链证明 + $\operatorname{rank}E=\operatorname{rank}L$ |
| [verify.py](verify.py) | 66 个铅笔上逐个核对 $\eta(R)=\varepsilon(Q_L)$（**验证不是证明**）|

## 复现

```bash
python proof/descriptor_reduction/verify.py
```

## 意义

把"$Q_L$ 的左指标划分"问题化为"descriptor 铅笔 $[\lambda E-F\ B]$ 的右指标划分"问题
（$[E\ B]$ 满行秩、$\operatorname{rank}E=\operatorname{rank}L$ ⟹ 可接可控性指标理论）。
这是专家 2026-11-02 §4 建议的下一阶段主攻方向。

## 相关

- [proof/t4b_infinite_divisors](../t4b_infinite_divisors/README.md)（B.7：$d_\infty=h-\operatorname{rank}L$）
- [proof/kron_null_module](../kron_null_module/README.md)（B.6）
- [tools/verification/descriptor_pencil.py](../../tools/verification/descriptor_pencil.py)
- [archive/expert_correspondence/expert_review_2026-11-02/README.md](../../archive/expert_correspondence/expert_review_2026-11-02/README.md)（D.4）

## 接已有理论（专家 2026-11-02 §4 的优先级 4）

把 $R(\lambda)=[\lambda E-EX^{\mathsf T}\ B]$ 写成 system pencil $[A'-\lambda E'\ \ B']$：
$$E'=-E,\qquad A'=-EX^{\mathsf T},\qquad B'=B .$$
（左乘 $-I$ 是严格等价，不改变 Kronecker 数据。）

按 SLICOT AG08BZ 的术语（*Zeros and Kronecker structure of a descriptor system pencil*，
<https://www.slicot.org/objects/software/shared/doc/AG08BZ.html>，其引用为 Misra–Van Dooren–Varga,
Automatica 30 (1994)），铅笔 $[A-\lambda E\ B]$ 的**右 Kronecker 指标就是该 descriptor 系统的可控性指标**。于是

> **$Q_L$ 的左最小指标 = descriptor 系统 $(-E,\,-EX^{\mathsf T},\,B)$ 的可控性指标。**

**标准情形**（$E$ 可逆，即 $h=q=r$）：左乘 $E^{-1}$ 得 $R\sim[\lambda I-X^{\mathsf T},\ E^{-1}B]$，
故左指标 = $(X^{\mathsf T},E^{-1}B)$ 的可控性指标（教科书结论）。

细节与检索记录见 [literature/notes/DESCRIPTOR_CONTROLLABILITY_INDICES.md](../../literature/notes/DESCRIPTOR_CONTROLLABILITY_INDICES.md)。
**注意**：这是**术语识别**（我们的量 = 文献里的量），不是把文献定理搬过来；
"右 Kronecker 指标 = 可控性指标"的精确定义（是否要求可控、零指标约定）应以原文为准。
