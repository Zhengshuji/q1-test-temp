# 606 最小秩计算：$H_A=HZ'$ 时 $\min\operatorname{rank}H=1$，$(5a)$ 无下界作用

> 2026-11-27。按 ChatGPT 的建议，计算“满足 $(5a)(5b)$ 的最小 $\operatorname{rank}H$”。
> **结论：在可实现形式 $H_A=HZ'$（$AN=NZ'$）下，最小秩为 1（$H=uv^{\mathsf T}$），$(5a)$ 自动成立、不起下界作用。**
> 状态：**[已证-纸面]**。

## 计算

设 $H_A=HZ'$（$AN=NZ'$）。则：
- $(5a)$：$Hv=0\Rightarrow H_Av=HZ'v=0$，**自动**；
- $(5b)$：$\operatorname{rank}(H(\lambda I-Z'))=\operatorname{rank}H$。

取 $H=u v_0^{\mathsf T}$（秩 1），则
$$H(\lambda I-Z')=u\big(v_0^{\mathsf T}(\lambda I-Z')\big).$$
秩恒为 1 $\iff v_0^{\mathsf T}(\lambda I-Z')\ne0\ \forall\lambda\iff v_0$ 不是 $Z'$ 的左特征向量。

对任意块对角 $Z'$，这样的 $v_0$ 存在（一般点）⇒ **$\min\operatorname{rank}H=1$**。

## 后果

- 两块的电路编码中，求解者可选全局秩 1 的 $H$，满足全部条件而不满足任何门；
- $(5a)$ 在 $H_A=HZ'$ 下**恒真**，无法提供 $\operatorname{rank}H\ge m$ 的下界；
- 所以“块对角 + $AN=NZ'$”的框架**先天不健全**。

## 需要的变化

要让 $(5a)$ 非平凡，必须 $AN\ne NZ'$，即 $A$ 在 $\operatorname{im}N$ 上的作用**不完全**留在 $\operatorname{im}N$ 里，
或 $A$ 把 $\operatorname{im}N$ 映到更大的空间，使
$$H_A=LAN$$
的每一行是 $H$ 的行与**固定常数行**（来自 $L_0A N$）的线性组合。
此时 $(5a)$ 变成对 $H$ 行空间与这些固定行的包含关系，可能给出秩下界。

## 下一步

1. 取 $A$ 使 $AN$ 的像包含 $N$ 之外的方向（例如 $A$ 把 $e_1$ 映到 $e_4$）；
2. 重新推导压缩形式：$H_A$ 的行 = $H$ 的行 × 某个固定矩阵 + 固定行；
3. 计算新的 $(5a)(5b)$ 与最小秩，检查能否 $\ge m$。

## 状态

- 最小秩：**[已证-纸面]**（$H_A=HZ'$ 时 =1）；
- 非平凡 $(5a)$ 的设计：**[未做]**。
