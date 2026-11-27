# multiplication_gate —— 乘法门 $z=xy$（硬度侧）

> 状态：**活跃**。上级：[q1_true](../README.md)。

## 问题

构造一个 sound 的观测器 gadget，使
$$(5a)\wedge(5b)\iff z=xy$$
（而不是只编码“某参数非零”）。有了它，才能把 $\exists\mathbb R$-难问题归约到 $q1$。

## 已有的组件

- 非零门：完整观测器，$(5b)\iff f\ne0$（`attempts/296`）；
- 输入非零门：$(5a)\wedge(5b)\iff x\ne0$（`attempts/303`）；
- 提升判据：$(H_i,H_{A,i})\in\operatorname{row}[N\ AN]$（`attempts/288`）。

## 卡点

复制整行 $H_2=(H_A)_1$ 会强制 $y_1=1$，破坏乘法；单坐标复制没有机制。需要 copy/format gadget
$(0,y,z)\to(0,1,z)$，或证明其不可能。

## 下一步

1. 把 copy/format 写成精确的压缩层目标（含提升条件）；
2. 先在小 $q$ 上符号搜索（不是随机采样）；
3. 若不可能，写成 no-go 引理。
