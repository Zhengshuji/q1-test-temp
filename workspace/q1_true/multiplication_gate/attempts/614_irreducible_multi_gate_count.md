# 614 不可约 $Z'$ 的多门：$\lambda=1$ 处的核-超平面计数

> 2026-11-27。613 之后，检查 $Q=k=6$、$Z'=$ 六阶循环、$H$ 由两个门块组成的可行性。
> 状态：**[已证-纸面]**（计数分析）。

## 设定

$Q=k=6$、$Z'=C_6$（六阶循环置换）。$C_6$ 的特征值 $\lambda$ 为 6 次单位根，
$M(\lambda)=\lambda I-C_6$ 的秩为 5（$\lambda^6=1$ 时），$\operatorname{im}M(\lambda)$ 是 5 维超平面。

## 计数

$$\operatorname{rank}(HM)=\operatorname{rank}M-\dim(\ker H\cap\operatorname{im}M)=5-d .$$
要等于 $\omega=\operatorname{rank}H$ ⇒ $d=5-\omega$。

若 $H$ 是两个秩 2 门块的块对角（$\omega=4$），需要 $d=1$：
$$\dim(\ker H\cap\operatorname{im}M(\lambda))=1 .$$
$\ker H$ 是 2 维（每块 1 维），所以需要**恰好一个**核向量落在 $\operatorname{im}M(\lambda)$（即其与特征向量
$u_\lambda=(1,\lambda,\dots,\lambda^5)$ 的内积为零），另一个不落。

## 含义

- 每个特征值 $\lambda$ 给出一个“二选一”条件：两个块核向量之一与 $u_\lambda$ 正交；
- 6 个特征值给出 6 个这样的条件，可能强制两个块的门关系；
- 但 $\ker H$ 的向量依赖 $R$，条件是关于 $R$ 的多项式方程——需要具体计算才能判断是否等价于两个乘积门。

## 下一步

1. 取两个 598 块的 $H_1,H_2$ 嵌入 6×6 对角，计算 $\ker H$ 与 $\operatorname{im}M(\lambda)$ 的相交；
2. 在 $\lambda=1$ 处解出“哪个核向量正交”的条件，与 $r_1r_2=z_1$、$z_1r_3=z_2$ 比较；
3. 若条件可分离，构造多门；否则不可约 $Z'$ 路线也停。

## 状态

- 计数：**[已证-纸面]**；
- 具体条件：**[未做]**。
